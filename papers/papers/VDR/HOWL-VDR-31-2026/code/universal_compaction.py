"""
universal_compaction.py

The compaction system has three parts:
1. CompactionSchema — how to compress source material into tables
2. ExtractionGrammar — how to read data back out of compacted form  
3. UsageGrammar — how to present/connect/transform compacted data for new purposes

All three live on the KB as persistent fields.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any, Tuple
from enum import Enum


# ============================================================
# ALL ENUMS FIRST (no dependencies on anything else)
# ============================================================

class SourceCharacter(Enum):
    PHILOSOPHY = "philosophy"
    ARCHITECTURE = "architecture"
    SCHEMA = "schema"
    OPERATIONAL = "operational"
    API = "api"
    METHODOLOGY = "methodology"
    SYNTHESIS = "synthesis"
    SPECIFICATION = "specification"
    RESEARCH = "research"
    NARRATIVE = "narrative"
    DATA = "data"
    MIXED = "mixed"

class ColumnType(Enum):
    ID = "id"
    TEXT = "text"
    IDENTIFIER = "identifier"
    CATEGORICAL = "categorical"
    ID_REF = "id_ref"
    ID_LIST = "id_list"
    REL_TYPE = "rel_type"
    FRACTION = "fraction"
    INTEGER = "integer"
    BOOLEAN = "boolean"
    ENUM_LIST = "enum_list"

class Direction(Enum):
    INBOUND = "inbound"
    OUTBOUND = "outbound"

class MountMode(Enum):
    READ_ONLY = "read_only"
    READ_WRITE = "read_write"
    SNAPSHOT = "snapshot"
    MIRROR = "mirror"

class Visibility(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    OWNER_ONLY = "owner_only"

class ConstraintScope(Enum):
    AXIOM = "axiom"
    OPERATIONAL = "operational"
    LEGAL = "legal"
    PROJECT = "project"
    CONVERSATION = "conversation"

class ConstraintStatus(Enum):
    ACTIVE = "active"
    SATISFIED = "satisfied"
    VIOLATED = "violated"
    SUSPENDED = "suspended"
    PARKED = "parked"


# ============================================================
# DATACLASSES (order: no-dependency first, then those that reference earlier ones)
# ============================================================

# --- These have no dataclass dependencies ---

@dataclass
class ColumnDef:
    name: str
    col_type: ColumnType
    required: bool = True
    enum_values: Optional[List[str]] = None
    description: str = ""

@dataclass
class Connection:
    target_id: int
    target_path: str
    relationship: str
    direction: Direction
    phase: str = ""
    created_at: int = 0
    notes: str = ""
    display_grammar: str = ""

@dataclass
class Constraint:
    name: str
    scope: ConstraintScope = ConstraintScope.OPERATIONAL
    status: ConstraintStatus = ConstraintStatus.ACTIVE
    condition: str = ""
    on_violation: str = "warn"
    source: str = ""

@dataclass
class Fact:
    predicate: str
    args: Dict[str, Any] = field(default_factory=dict)
    kb_source: str = ""
    asserted_at: int = 0



# ============================================================
# PART 1: SOURCE CLASSIFICATION AND TABLE SELECTION
# ============================================================

class SourceCharacter(Enum):
    """What kind of document is the source?
    Determines which table set to use."""
    PHILOSOPHY = "philosophy"           # concepts, axes, distinctions, claims
    ARCHITECTURE = "architecture"       # commitments, categories, flows, boundaries
    SCHEMA = "schema"                   # entities, fields, discriminators, enumerations
    OPERATIONAL = "operational"         # operations, rules, gating, anti-patterns
    API = "api"                         # endpoints, parameters, responses, errors
    METHODOLOGY = "methodology"         # phases, steps, deliverables, criteria
    SYNTHESIS = "synthesis"             # diagnostics, capabilities, commitments
    SPECIFICATION = "specification"     # components, interfaces, contracts, constraints
    RESEARCH = "research"              # findings, evidence, methods, conclusions
    NARRATIVE = "narrative"            # events, characters, settings, themes
    DATA = "data"                      # records, fields, types, constraints
    MIXED = "mixed"                    # multiple characters — use union of applicable tables


class ColumnType(Enum):
    """Types for table columns. Used for validation and grammar generation."""
    ID = "id"                          # row identifier with prefix
    TEXT = "text"                       # free text, compressed prose
    IDENTIFIER = "identifier"          # named thing — preserve exact terminology
    CATEGORICAL = "categorical"        # value from declared enum
    ID_REF = "id_ref"                 # reference to another row's ID
    ID_LIST = "id_list"               # comma-separated list of ID references
    REL_TYPE = "rel_type"             # relationship type from declared enum
    FRACTION = "fraction"             # exact VDR fraction as "n/d"
    INTEGER = "integer"               # exact integer
    BOOLEAN = "boolean"               # yes/no, true/false
    ENUM_LIST = "enum_list"           # pipe-separated list of enum values


@dataclass
class ColumnDef:
    """Definition of one column in a compaction table."""
    name: str
    col_type: ColumnType
    required: bool = True
    enum_values: Optional[List[str]] = None   # for CATEGORICAL and ENUM_LIST
    description: str = ""


@dataclass
class TableSchema:
    """Schema for one table type in the compaction system.
    
    IOSE (pure):
      Inputs: source text, extraction rules
      Outputs: list of rows matching this schema
      Side Effects: none
      Properties: deterministic given same extraction judgments
    """
    name: str
    columns: List[ColumnDef]
    id_prefix: str                             # "P", "C", "CL", "RK", etc.
    applicable_when: str                       # Prolog condition
    description: str = ""
    min_rows: int = 0                          # constraint: minimum rows if table is used
    allow_empty: bool = True                   # can table be empty?
    sort_by: Optional[str] = None              # default sort column


@dataclass
class CompactionProfile:
    """Complete compaction profile for a source character type.
    Declares which tables to use, in what order, with what constraints."""
    character: SourceCharacter
    required_tables: List[str]                 # table names that must be present
    optional_tables: List[str]                 # table names included when applicable
    always_tables: List[str]                   # relationships, section_index, decode_legend
    read_order: List[str]                      # recommended reading sequence
    id_prefix_scheme: Dict[str, str]           # table_name → prefix
    compression_target: Tuple[int, int]        # (min%, max%) target compression ratio
    description: str = ""


# ============================================================
# PART 2: THE STANDARD TABLE LIBRARY
# ============================================================

# These are the reusable table schemas. Any compaction picks a subset.
# New table types can be created by the LLM and added to a KB.

STANDARD_TABLES: Dict[str, TableSchema] = {}

def _register(schema: TableSchema) -> TableSchema:
    STANDARD_TABLES[schema.name] = schema
    return schema


# --- Core tables (used across most characters) ---

_register(TableSchema(
    name="principles",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("principle", ColumnType.TEXT),
        ColumnDef("rationale", ColumnType.TEXT),
    ],
    id_prefix="P",
    applicable_when="source_has_principles",
    description="Load-bearing structural principles with rationale",
))

_register(TableSchema(
    name="concepts",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("category", ColumnType.CATEGORICAL,
                  enum_values=["core", "slot", "state", "operation", "semantics",
                               "procedure", "metric", "construction", "anti-pattern"]),
        ColumnDef("definition", ColumnType.TEXT),
    ],
    id_prefix="C",
    applicable_when="source_has_named_concepts",
    description="Named concepts with category and definition. Anti-patterns merge here with category=anti-pattern",
))

_register(TableSchema(
    name="claims",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("claim", ColumnType.TEXT),
        ColumnDef("type", ColumnType.CATEGORICAL,
                  enum_values=["demonstrated", "structural", "limitation",
                               "boundary", "finding", "observation",
                               "design_thesis", "derived"]),
        ColumnDef("evidence", ColumnType.ID_LIST, required=False),
    ],
    id_prefix="CL",
    applicable_when="source_makes_claims",
    description="Assertions with type classification and evidence references",
))

_register(TableSchema(
    name="operations",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("mechanism", ColumnType.TEXT),
        ColumnDef("inputs", ColumnType.TEXT, required=False),
        ColumnDef("outputs", ColumnType.TEXT, required=False),
    ],
    id_prefix="OP",
    applicable_when="source_has_operations",
    description="Named operations with mechanism description",
))

_register(TableSchema(
    name="boundaries",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("limitation", ColumnType.TEXT),
        ColumnDef("detail", ColumnType.TEXT),
    ],
    id_prefix="B",
    applicable_when="source_has_limitations",
    description="Honest limitations and what is NOT claimed",
))

_register(TableSchema(
    name="rules",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("rule", ColumnType.TEXT),
        ColumnDef("enforcement", ColumnType.TEXT, required=False),
    ],
    id_prefix="R",
    applicable_when="source_has_prescriptions",
    description="Actionable prescriptions with enforcement mechanism",
))

_register(TableSchema(
    name="distinctions",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("side_a", ColumnType.TEXT),
        ColumnDef("side_b", ColumnType.TEXT),
        ColumnDef("key_asymmetry", ColumnType.TEXT),
    ],
    id_prefix="DI",
    applicable_when="source_has_binary_splits",
    description="Binary splits with the key asymmetry identified",
))

_register(TableSchema(
    name="axes",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("low_pole", ColumnType.TEXT),
        ColumnDef("high_pole", ColumnType.TEXT),
        ColumnDef("applies_to", ColumnType.TEXT, required=False),
    ],
    id_prefix="AX",
    applicable_when="source_has_spectrums",
    description="Named spectrums with poles",
))

# --- Specification tables ---

_register(TableSchema(
    name="components",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("category", ColumnType.CATEGORICAL),
        ColumnDef("iose_inputs", ColumnType.TEXT, required=False),
        ColumnDef("iose_outputs", ColumnType.TEXT, required=False),
        ColumnDef("iose_side_effects", ColumnType.TEXT, required=False),
    ],
    id_prefix="CO",
    applicable_when="source_has_components_or_modules",
    description="System components with optional IOSE interface summary",
))

_register(TableSchema(
    name="builtins",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("category", ColumnType.CATEGORICAL),
        ColumnDef("signature", ColumnType.TEXT),
        ColumnDef("properties", ColumnType.ENUM_LIST, required=False),
    ],
    id_prefix="BU",
    applicable_when="source_specifies_primitives_or_builtins",
    description="Primitive/builtin operations with signatures",
))

_register(TableSchema(
    name="constraints",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("scope", ColumnType.CATEGORICAL,
                  enum_values=["axiom", "operational", "legal", "project", "conversation"]),
        ColumnDef("condition", ColumnType.TEXT),
        ColumnDef("on_violation", ColumnType.TEXT),
    ],
    id_prefix="CN",
    applicable_when="source_has_constraints",
    description="Declared constraints with scope and violation handling",
))

# --- Data/schema tables ---

_register(TableSchema(
    name="entities",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("description", ColumnType.TEXT),
    ],
    id_prefix="E",
    applicable_when="source_has_data_entities",
    description="Data entities in a schema",
))

_register(TableSchema(
    name="fields",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("entity", ColumnType.ID_REF),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("type", ColumnType.TEXT),
        ColumnDef("required", ColumnType.BOOLEAN),
        ColumnDef("description", ColumnType.TEXT, required=False),
    ],
    id_prefix="F",
    applicable_when="source_has_data_fields",
    description="Fields belonging to entities",
))

# --- Lifecycle/process tables ---

_register(TableSchema(
    name="phases",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("inputs", ColumnType.TEXT),
        ColumnDef("outputs", ColumnType.TEXT),
        ColumnDef("key_constraint", ColumnType.TEXT, required=False),
    ],
    id_prefix="PH",
    applicable_when="source_has_phases_or_stages",
    description="Lifecycle or process phases with inputs/outputs",
))

_register(TableSchema(
    name="test_results",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("domain", ColumnType.IDENTIFIER),
        ColumnDef("tests", ColumnType.INTEGER),
        ColumnDef("passed", ColumnType.INTEGER),
        ColumnDef("failed", ColumnType.INTEGER),
        ColumnDef("notes", ColumnType.TEXT, required=False),
    ],
    id_prefix="TR",
    applicable_when="source_has_test_results",
    description="Test results per domain",
))

_register(TableSchema(
    name="failures",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("test", ColumnType.TEXT),
        ColumnDef("expected", ColumnType.TEXT),
        ColumnDef("got", ColumnType.TEXT),
        ColumnDef("root_cause", ColumnType.TEXT),
    ],
    id_prefix="FL",
    applicable_when="source_has_failure_analysis",
    description="Individual failures with root cause",
))

# --- Research tables ---

_register(TableSchema(
    name="findings",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("finding", ColumnType.TEXT),
        ColumnDef("evidence", ColumnType.ID_LIST, required=False),
        ColumnDef("confidence", ColumnType.FRACTION, required=False),
    ],
    id_prefix="FI",
    applicable_when="source_has_findings",
    description="Research findings with evidence and confidence",
))

_register(TableSchema(
    name="benchmarks",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("name", ColumnType.IDENTIFIER),
        ColumnDef("metric", ColumnType.TEXT),
        ColumnDef("value", ColumnType.TEXT),
        ColumnDef("comparison", ColumnType.TEXT, required=False),
    ],
    id_prefix="BM",
    applicable_when="source_has_benchmarks",
    description="Benchmark results with metrics",
))

# --- Always-present tables ---

_register(TableSchema(
    name="relationships",
    columns=[
        ColumnDef("from", ColumnType.ID_REF),
        ColumnDef("rel", ColumnType.REL_TYPE),
        ColumnDef("to", ColumnType.ID_REF),
    ],
    id_prefix="",
    applicable_when="always",
    description="Typed directed edges between any IDs in the document",
))

_register(TableSchema(
    name="section_index",
    columns=[
        ColumnDef("section", ColumnType.IDENTIFIER),
        ColumnDef("title", ColumnType.TEXT),
        ColumnDef("ids", ColumnType.ID_LIST),
    ],
    id_prefix="",
    applicable_when="always",
    description="Provenance map: source section → IDs defined there",
))


# ============================================================
# PART 3: COMPACTION PROFILES
# ============================================================

PROFILES: Dict[SourceCharacter, CompactionProfile] = {

    SourceCharacter.PHILOSOPHY: CompactionProfile(
        character=SourceCharacter.PHILOSOPHY,
        required_tables=["principles", "concepts", "claims"],
        optional_tables=["axes", "distinctions", "boundaries", "rules"],
        always_tables=["relationships", "section_index"],
        read_order=["principles", "concepts", "axes", "distinctions",
                     "claims", "boundaries", "relationships", "section_index"],
        id_prefix_scheme={"principles": "P", "concepts": "C", "claims": "CL",
                          "axes": "AX", "distinctions": "DI", "boundaries": "B",
                          "rules": "R"},
        compression_target=(85, 93),
        description="Philosophy/principles papers. Mostly prose → high compression.",
    ),

    SourceCharacter.SPECIFICATION: CompactionProfile(
        character=SourceCharacter.SPECIFICATION,
        required_tables=["components", "concepts"],
        optional_tables=["builtins", "constraints", "principles", "claims",
                         "boundaries", "phases", "entities", "fields"],
        always_tables=["relationships", "section_index"],
        read_order=["principles", "components", "builtins", "constraints",
                     "concepts", "boundaries", "claims", "relationships",
                     "section_index"],
        id_prefix_scheme={"components": "CO", "concepts": "C", "builtins": "BU",
                          "constraints": "CN", "principles": "P", "claims": "CL",
                          "boundaries": "B", "phases": "PH", "entities": "E",
                          "fields": "F"},
        compression_target=(75, 85),
        description="System specifications. Already semi-structured → moderate compression.",
    ),

    SourceCharacter.RESEARCH: CompactionProfile(
        character=SourceCharacter.RESEARCH,
        required_tables=["findings", "claims"],
        optional_tables=["benchmarks", "test_results", "failures",
                         "concepts", "boundaries", "principles"],
        always_tables=["relationships", "section_index"],
        read_order=["principles", "findings", "benchmarks", "test_results",
                     "failures", "claims", "boundaries", "relationships",
                     "section_index"],
        id_prefix_scheme={"findings": "FI", "claims": "CL", "benchmarks": "BM",
                          "test_results": "TR", "failures": "FL", "concepts": "C",
                          "boundaries": "B", "principles": "P"},
        compression_target=(80, 90),
        description="Research papers with results. Tables and data → good compression.",
    ),

    SourceCharacter.METHODOLOGY: CompactionProfile(
        character=SourceCharacter.METHODOLOGY,
        required_tables=["phases"],
        optional_tables=["concepts", "rules", "constraints", "claims",
                         "boundaries", "test_results"],
        always_tables=["relationships", "section_index"],
        read_order=["principles", "phases", "rules", "constraints",
                     "concepts", "claims", "relationships", "section_index"],
        id_prefix_scheme={"phases": "PH", "concepts": "C", "rules": "R",
                          "constraints": "CN", "claims": "CL", "boundaries": "B"},
        compression_target=(80, 85),
        description="Process/methodology papers. Phase sequences are already structured.",
    ),

    SourceCharacter.OPERATIONAL: CompactionProfile(
        character=SourceCharacter.OPERATIONAL,
        required_tables=["operations"],
        optional_tables=["concepts", "rules", "constraints", "principles",
                         "claims", "boundaries", "components"],
        always_tables=["relationships", "section_index"],
        read_order=["principles", "operations", "rules", "constraints",
                     "concepts", "components", "claims", "boundaries",
                     "relationships", "section_index"],
        id_prefix_scheme={"operations": "OP", "concepts": "C", "rules": "R",
                          "constraints": "CN", "principles": "P", "claims": "CL",
                          "boundaries": "B", "components": "CO"},
        compression_target=(80, 85),
        description="Operational pattern papers.",
    ),

    SourceCharacter.DATA: CompactionProfile(
        character=SourceCharacter.DATA,
        required_tables=["entities", "fields"],
        optional_tables=["constraints", "concepts", "rules"],
        always_tables=["relationships", "section_index"],
        read_order=["entities", "fields", "constraints", "concepts",
                     "rules", "relationships", "section_index"],
        id_prefix_scheme={"entities": "E", "fields": "F", "constraints": "CN",
                          "concepts": "C", "rules": "R"},
        compression_target=(75, 85),
        description="Data schema documents. Already highly structured.",
    ),
}


# ============================================================
# PART 4: THE DECODE LEGEND SPEC
# ============================================================

@dataclass
class DecodeLegendEntry:
    """One entry in the decode legend."""
    key: str                    # e.g. "rel_types", "claim_types", "field_types"
    description: str            # e.g. "enables|requires|implements|..."
    entry_type: str             # "enum", "notation", "convention", "abbreviation"


@dataclass
class DecodeLegend:
    """The complete decode legend for a compacted document.
    Serves as the type system — all enums and notations declared here."""
    entries: List[DecodeLegendEntry] = field(default_factory=list)

    def add_enum(self, key: str, values: List[str]) -> None:
        self.entries.append(DecodeLegendEntry(
            key=key,
            description="|".join(values),
            entry_type="enum"
        ))

    def add_notation(self, key: str, description: str) -> None:
        self.entries.append(DecodeLegendEntry(
            key=key, description=description, entry_type="notation"
        ))

    def get_enum_values(self, key: str) -> Optional[List[str]]:
        for e in self.entries:
            if e.key == key and e.entry_type == "enum":
                return e.description.split("|")
        return None


# ============================================================
# PART 5: THE COMPACTED DOCUMENT
# ============================================================

class MountMode(Enum):
    READ_ONLY = "read_only"
    READ_WRITE = "read_write"
    SNAPSHOT = "snapshot"
    MIRROR = "mirror"

class Visibility(Enum):
    PUBLIC = "public"
    INTERNAL = "internal"
    OWNER_ONLY = "owner_only"

class ConstraintScope(Enum):
    AXIOM = "axiom"
    OPERATIONAL = "operational"
    LEGAL = "legal"
    PROJECT = "project"
    CONVERSATION = "conversation"

class ConstraintStatus(Enum):
    ACTIVE = "active"
    SATISFIED = "satisfied"
    VIOLATED = "violated"
    SUSPENDED = "suspended"
    PARKED = "parked"

@dataclass
class Connection:
    target_id: int
    target_path: str
    relationship: str
    direction: Direction
    phase: str = ""
    created_at: int = 0
    notes: str = ""
    display_grammar: str = ""

@dataclass
class Constraint:
    name: str
    scope: ConstraintScope = ConstraintScope.OPERATIONAL
    status: ConstraintStatus = ConstraintStatus.ACTIVE
    condition: str = ""
    on_violation: str = "warn"
    source: str = ""

@dataclass
class Fact:
    predicate: str
    args: Dict[str, Any] = field(default_factory=dict)
    kb_source: str = ""
    asserted_at: int = 0

@dataclass
class Counter:
    value: int = 0
    min_value: int = 0
    max_value: int = (2**31) - 1

    def inc(self) -> int:
        self.value = min(self.value + 1, self.max_value)
        return self.value

    def dec(self) -> int:
        self.value = max(self.value - 1, self.min_value)
        return self.value

    def add(self, delta: int) -> int:
        self.value = max(self.min_value, min(self.value + delta, self.max_value))
        return self.value

    def reset(self) -> None:
        self.value = self.min_value

    def set(self, val: int) -> None:
        self.value = max(self.min_value, min(val, self.max_value))

    def get(self) -> int:
        return self.value


@dataclass
class LockState:
    held: bool = False
    holder: Optional[str] = None
    acquired_at: int = 0

    def acquire(self, holder: str = "", turn: int = 0) -> bool:
        if self.held:
            return False
        self.held = True
        self.holder = holder
        self.acquired_at = turn
        return True

    def release(self) -> None:
        self.held = False
        self.holder = None

    def check(self) -> bool:
        return self.held


@dataclass
class GrammarRule:
    """A grammar production rule attached to a KB.
    
    Defines how to present, extract, or transform data from the KB.
    Lives on the KB struct as a persistent field.
    Inherits through the KB tree like constraints.
    
    IOSE (pure):
      Inputs: data matching slot types from KB facts
      Outputs: formatted token stream (for display) or structured data (for extraction)
      Side Effects: none
      Properties: deterministic, bounded
    """
    name: str
    slots: List[str]
    slot_types: Dict[str, str]
    template: List[Any]                          # template lines/structure
    requires: List[str] = field(default_factory=list)
    best_when: str = ""
    connection_pattern: Optional[str] = None     # match on connection topology
    created_at: int = 0
    usage_count: int = 0
    display_grammar: str = ""                    # added for Connection reference
    


@dataclass
class KnowledgeBase:
    name: str
    path: str
    id: int

    # Persistent
    facts: List[Fact] = field(default_factory=list)
    rules: List[Any] = field(default_factory=list)
    constraints: List[Constraint] = field(default_factory=list)
    connections: List[Connection] = field(default_factory=list)
    grammars: List[GrammarRule] = field(default_factory=list)

    # Live state
    working_data: Dict[str, Any] = field(default_factory=dict)
    counters: Dict[str, Counter] = field(default_factory=dict)
    locks: Dict[str, LockState] = field(default_factory=dict)

    # Structural
    parent_id: Optional[int] = None
    children_ids: List[int] = field(default_factory=list)

    # Metadata
    visibility: Visibility = Visibility.PUBLIC
    frozen: bool = False
    owner: Optional[str] = None
    created_at: int = 0
    last_modified: int = 0

    def assert_fact(self, predicate: str, args: Optional[Dict[str, Any]] = None,
                    turn: int = 0) -> Fact:
        args = args or {}
        for f in self.facts:
            if f.predicate == predicate and f.args == args:
                return f
        fact = Fact(predicate=predicate, args=args,
                    kb_source=self.path, asserted_at=turn)
        self.facts.append(fact)
        self.last_modified = turn
        return fact

    def retract_fact(self, predicate: str, args: Optional[Dict[str, Any]] = None,
                     turn: int = 0) -> bool:
        args = args or {}
        for i, f in enumerate(self.facts):
            if f.predicate == predicate and f.args == args:
                self.facts.pop(i)
                self.last_modified = turn
                return True
        return False

    def query_facts(self, predicate: str,
                    match_args: Optional[Dict[str, Any]] = None) -> List[Fact]:
        results = []
        for f in self.facts:
            if f.predicate != predicate:
                continue
            if match_args is None:
                results.append(f)
            else:
                if all(f.args.get(k) == v for k, v in match_args.items()):
                    results.append(f)
        return results

    def reset_live(self) -> None:
        self.working_data.clear()
        for c in self.counters.values():
            c.reset()
        for lk in self.locks.values():
            lk.release()

class PathRegistry:
    def __init__(self) -> None:
        self._path_to_id: Dict[str, int] = {}
        self._id_to_path: List[str] = []
        self._next_id: int = 0
        self.register("root")

    def register(self, path: str) -> int:
        if path in self._path_to_id:
            return self._path_to_id[path]
        pid = self._next_id
        self._next_id += 1
        self._path_to_id[path] = pid
        self._id_to_path.append(path)
        return pid

    def resolve(self, path: str) -> Optional[int]:
        return self._path_to_id.get(path)

    def from_id(self, pid: int) -> Optional[str]:
        if 0 <= pid < len(self._id_to_path):
            return self._id_to_path[pid]
        return None

    def exists(self, path: str) -> bool:
        return path in self._path_to_id

    def parent_path(self, path: str) -> Optional[str]:
        if path == "root":
            return None
        parts = path.rsplit(".", 1)
        if len(parts) == 2:
            return parts[0]
        return None

    def children_paths(self, path: str) -> List[str]:
        prefix = path + "."
        depth = prefix.count(".")
        result = []
        for p in self._path_to_id:
            if p.startswith(prefix) and p.count(".") == depth:
                result.append(p)
        return result

    def depth(self, path: str) -> int:
        return path.count(".")

@dataclass
class CompactedRow:
    """One row in a compacted table."""
    id: str                              # "P1", "C3", "CL7"
    values: Dict[str, str]               # column_name → value (all stored as strings)


@dataclass
class CompactedTable:
    """One table in a compacted document, with schema reference."""
    schema_name: str                     # references a TableSchema by name
    rows: List[CompactedRow] = field(default_factory=list)

    def row_count(self) -> int:
        return len(self.rows)

    def get_row(self, row_id: str) -> Optional[CompactedRow]:
        for r in self.rows:
            if r.id == row_id:
                return r
        return None

    def get_all_ids(self) -> List[str]:
        return [r.id for r in self.rows]


@dataclass
class CompactedDocument:
    """A fully compacted document with all metadata.
    
    This is what gets stored as a KB.
    The tables become facts.
    The relationships become connections.
    The section_index becomes provenance.
    The decode_legend becomes type constraints.
    The grammars for reading/writing this data live on the KB.
    """
    title: str
    source_character: SourceCharacter
    profile: str                                    # profile name used
    tables: Dict[str, CompactedTable]               # table_name → table
    decode_legend: DecodeLegend = field(default_factory=DecodeLegend)
    source_ref: str = ""                            # where the source material came from
    compression_ratio: Optional[float] = None       # actual compression achieved
    compacted_at: int = 0

    def all_ids(self) -> List[str]:
        """Every ID defined in every table."""
        ids = []
        for table in self.tables.values():
            ids.extend(table.get_all_ids())
        return ids

    def get_by_id(self, row_id: str) -> Optional[Tuple[str, CompactedRow]]:
        """Find any row by ID across all tables."""
        for table_name, table in self.tables.items():
            row = table.get_row(row_id)
            if row is not None:
                return (table_name, row)
        return None

    def relationships(self) -> List[CompactedRow]:
        """Get all relationship rows."""
        rel_table = self.tables.get("relationships")
        return rel_table.rows if rel_table else []

    def section_index(self) -> List[CompactedRow]:
        """Get section index rows."""
        si_table = self.tables.get("section_index")
        return si_table.rows if si_table else []


# ============================================================
# PART 6: COMPACTION → KB CONVERSION
# ============================================================

def compacted_doc_to_kb(doc: CompactedDocument, 
                        kb: 'KnowledgeBase',
                        registry: 'PathRegistry') -> None:
    """Load a compacted document into a KB.
    
    Tables → facts (one fact per row, predicate = table name)
    Relationships → connections
    Section index → provenance facts
    Decode legend → constraint-like type metadata
    Grammars → extraction and display grammars auto-generated
    
    IOSE:
      Inputs: CompactedDocument, target KB
      Outputs: None (KB mutated)
      Side Effects: facts asserted, connections added, grammars added
      Properties: deterministic, bounded, idempotent (re-loading same doc is no-op)
    """
    
    # --- Assert table rows as facts ---
    for table_name, table in doc.tables.items():
        if table_name in ("relationships", "section_index"):
            continue  # handled separately
        
        # Assert schema as a fact (so grammar can find it)
        schema = STANDARD_TABLES.get(table_name)
        if schema:
            col_names = [c.name for c in schema.columns]
            kb.assert_fact("table_schema", {
                "table": table_name,
                "columns": col_names,
                "id_prefix": schema.id_prefix,
            })
        
        # Assert each row
        for row in table.rows:
            kb.assert_fact(table_name, {
                "id": row.id,
                **row.values,
            })
    
    # --- Relationships → connections ---
    for rel_row in doc.relationships():
        from_id = rel_row.values.get("from", "")
        to_id = rel_row.values.get("to", "")
        rel_type = rel_row.values.get("rel", "")
        
        # Internal connections (within this KB)
        kb.connections.append(Connection(
            target_id=kb.id,  # self-referential for internal edges
            target_path=kb.path,
            relationship=f"{from_id}.{rel_type}.{to_id}",
            direction=Direction.OUTBOUND,
        ))
    
    # --- Section index → provenance facts ---
    for si_row in doc.section_index():
        kb.assert_fact("section_index", {
            "section": si_row.values.get("section", ""),
            "title": si_row.values.get("title", ""),
            "ids": si_row.values.get("ids", ""),
        })
    
    # --- Decode legend → type metadata ---
    for entry in doc.decode_legend.entries:
        kb.assert_fact("decode", {
            "key": entry.key,
            "description": entry.description,
            "type": entry.entry_type,
        })
        
        # If it's an enum, add a validation constraint
        if entry.entry_type == "enum":
            kb.constraints.append(Constraint(
                name=f"valid_{entry.key}",
                condition=f"all_values_in_enum({entry.key})",
                on_violation="warn",
            ))
    
    # --- Auto-generate grammars ---
    _generate_extraction_grammars(doc, kb)
    _generate_display_grammars(doc, kb)


def _generate_extraction_grammars(doc: CompactedDocument,
                                   kb: 'KnowledgeBase') -> None:
    """Generate grammars that read data out of this compacted KB.
    
    For each table, create a grammar that:
    - Knows the column names and types
    - Can extract rows by ID
    - Can filter rows by column value
    - Can join across tables via ID references
    """
    for table_name, table in doc.tables.items():
        if table_name in ("relationships", "section_index"):
            continue
        
        schema = STANDARD_TABLES.get(table_name)
        if not schema:
            continue
        
        col_names = [c.name for c in schema.columns]
        col_types = {c.name: c.col_type.value for c in schema.columns}
        
        # Extraction grammar: how to query this table
        kb.grammars.append(GrammarRule(
            name=f"extract_{table_name}",
            slots=col_names,
            slot_types=col_types,
            template=[],  # extraction grammars produce data, not display
            requires=[f"table_exists({table_name})"],
            best_when=f"querying_{table_name}_data",
        ))
        
        # ID-reference resolution grammar: for columns that reference other IDs
        for col in schema.columns:
            if col.col_type in (ColumnType.ID_REF, ColumnType.ID_LIST):
                kb.grammars.append(GrammarRule(
                    name=f"resolve_{table_name}_{col.name}",
                    slots=["source_id", "ref_ids", "resolved_rows"],
                    slot_types={
                        "source_id": "id",
                        "ref_ids": "id_list",
                        "resolved_rows": "list_of_dict",
                    },
                    template=[],
                    requires=[f"column_is_ref({table_name}, {col.name})"],
                    best_when=f"following_{col.name}_references_from_{table_name}",
                ))


def _generate_display_grammars(doc: CompactedDocument,
                                kb: 'KnowledgeBase') -> None:
    """Generate grammars that present this KB's data for output.
    
    Creates grammars for:
    - Single row display (detail view of one item)
    - Table display (all rows in a table)
    - Compact pipe-delimited display (re-emit in compacted form)
    - Relationship graph display
    - Summary display (counts and key stats)
    """
    table_names = [t for t in doc.tables.keys()
                   if t not in ("relationships", "section_index")]
    
    # --- Compact re-emission grammar ---
    kb.grammars.append(GrammarRule(
        name="compact_display",
        slots=["table_name", "column_header", "rows"],
        slot_types={
            "table_name": "identifier",
            "column_header": "text",
            "rows": "list_of_text",
        },
        template=[
            {"type": "line", "content": ["# ", "{table_name}", "(", "{column_header}", ")"]},
            {"type": "for_each", "over": "rows", "line": ["{row}"]},
        ],
        best_when="re_emitting_compacted_form",
    ))
    
    # --- Summary grammar ---
    kb.grammars.append(GrammarRule(
        name="document_summary",
        slots=["title", "character", "table_counts", "total_ids",
               "relationship_count"],
        slot_types={
            "title": "text",
            "character": "categorical",
            "table_counts": "dict",
            "total_ids": "integer",
            "relationship_count": "integer",
        },
        template=[
            {"type": "line", "content": ["{title} — ", "{character}"]},
            {"type": "line", "content": ["{total_ids} items, ",
                                          "{relationship_count} relationships"]},
            {"type": "for_each", "over": "table_counts",
             "line": ["  ", "{table_name}", ": ", "{count}", " rows"]},
        ],
        best_when="summarizing_compacted_document",
    ))
    
    # --- Per-table display grammars ---
    for table_name in table_names:
        schema = STANDARD_TABLES.get(table_name)
        if not schema:
            continue
        
        col_names = [c.name for c in schema.columns]
        
        # Single row detail view
        kb.grammars.append(GrammarRule(
            name=f"detail_{table_name}",
            slots=col_names,
            slot_types={c.name: c.col_type.value for c in schema.columns},
            template=[
                {"type": "for_each_column", "format": "{col_name}: {value}"},
            ],
            best_when=f"displaying_single_{table_name}_row",
        ))
    
    # --- Relationship display grammar ---
    kb.grammars.append(GrammarRule(
        name="relationship_display",
        slots=["from_id", "rel_type", "to_id", "from_name", "to_name"],
        slot_types={
            "from_id": "id_ref", "rel_type": "rel_type", "to_id": "id_ref",
            "from_name": "text", "to_name": "text",
        },
        template=[
            {"type": "line", "content": ["{from_name} (", "{from_id}", ") —",
                                          "{rel_type}", "→ ", "{to_name}",
                                          " (", "{to_id}", ")"]},
        ],
        best_when="displaying_relationships",
    ))


# ============================================================
# PART 7: KB → COMPACTED DOCUMENT (REVERSE)
# ============================================================

def kb_to_compacted_doc(kb: 'KnowledgeBase') -> Optional[CompactedDocument]:
    """Reconstruct a CompactedDocument from a KB's facts.
    
    This is the inverse of compacted_doc_to_kb.
    Uses the table_schema facts and extraction grammars on the KB.
    
    IOSE:
      Inputs: KB with compacted data
      Outputs: CompactedDocument
      Side Effects: none
      Properties: pure, deterministic, bounded
    """
    # Find all table schemas
    schema_facts = kb.query_facts("table_schema")
    if not schema_facts:
        return None
    
    title = kb.name
    
    # Determine source character from KB metadata or facts
    char_facts = kb.query_facts("source_character")
    character = SourceCharacter.MIXED
    if char_facts:
        try:
            character = SourceCharacter(char_facts[0].args.get("value", "mixed"))
        except ValueError:
            pass
    
    tables = {}
    
    for sf in schema_facts:
        table_name = sf.args.get("table", "")
        col_names = sf.args.get("columns", [])
        
        # Query all rows for this table
        row_facts = kb.query_facts(table_name)
        rows = []
        for rf in row_facts:
            row_id = rf.args.get("id", "")
            values = {k: str(v) for k, v in rf.args.items() if k != "id"}
            rows.append(CompactedRow(id=row_id, values=values))
        
        tables[table_name] = CompactedTable(schema_name=table_name, rows=rows)
    
    # Reconstruct relationships from connections
    rel_rows = []
    for conn in kb.connections:
        parts = conn.relationship.split(".")
        if len(parts) == 3:
            rel_rows.append(CompactedRow(
                id="",
                values={"from": parts[0], "rel": parts[1], "to": parts[2]}
            ))
    if rel_rows:
        tables["relationships"] = CompactedTable(
            schema_name="relationships", rows=rel_rows)
    
    # Reconstruct section index
    si_facts = kb.query_facts("section_index")
    if si_facts:
        si_rows = [CompactedRow(id="", values=f.args) for f in si_facts]
        tables["section_index"] = CompactedTable(
            schema_name="section_index", rows=si_rows)
    
    # Reconstruct decode legend
    legend = DecodeLegend()
    decode_facts = kb.query_facts("decode")
    for df in decode_facts:
        legend.entries.append(DecodeLegendEntry(
            key=df.args.get("key", ""),
            description=df.args.get("description", ""),
            entry_type=df.args.get("type", "notation"),
        ))
    
    return CompactedDocument(
        title=title,
        source_character=character,
        profile=character.value,
        tables=tables,
        decode_legend=legend,
    )


# ============================================================
# PART 8: USAGE GRAMMAR GENERATION
# ============================================================

def generate_usage_grammar(source_kb: 'KnowledgeBase',
                           target_kb: 'KnowledgeBase',
                           usage_type: str,
                           connection_rel: str) -> GrammarRule:
    """Generate a grammar for using source KB's data in target KB's context.
    
    This is how compacted data becomes useful in new contexts.
    The grammar is created on the target KB and references source KB via connection.
    
    Usage types:
      - "reference": pull specific facts from source for inline citation
      - "comparison": compare items from source with items in target
      - "dependency": trace what in target depends on what in source
      - "summary": summarize source data for target context
      - "evidence": use source data as evidence in target inference
    
    IOSE:
      Inputs: source KB, target KB, usage type, connection relationship
      Outputs: GrammarRule (added to target KB)
      Side Effects: grammar added to target KB, connection added to both KBs
      Properties: deterministic, bounded
    """
    
    # Get source table schemas to know what data is available
    source_schemas = source_kb.query_facts("table_schema")
    available_tables = [s.args.get("table", "") for s in source_schemas]
    
    if usage_type == "reference":
        grammar = GrammarRule(
            name=f"ref_{source_kb.name}",
            slots=["item_id", "item_name", "item_detail", "source_ref"],
            slot_types={
                "item_id": "id_ref",
                "item_name": "identifier",
                "item_detail": "text",
                "source_ref": "text",
            },
            template=[
                {"type": "inline", "content": [
                    "{item_name}", " (", "{item_id}",
                    " from ", "{source_ref}", "): ", "{item_detail}"]},
            ],
            connection_pattern=f"has_outbound({connection_rel}, 1+)",
            best_when=f"citing_data_from_{source_kb.name}",
        )
    
    elif usage_type == "comparison":
        grammar = GrammarRule(
            name=f"compare_with_{source_kb.name}",
            slots=["local_items", "source_items", "comparison_columns"],
            slot_types={
                "local_items": "list_of_dict",
                "source_items": "list_of_dict",
                "comparison_columns": "list_of_identifier",
            },
            template=[
                {"type": "header", "content": ["Comparison: local vs ", "{source_ref}"]},
                {"type": "merged_table", "sources": ["local_items", "source_items"],
                 "columns": "comparison_columns"},
            ],
            connection_pattern=f"has_outbound({connection_rel}, 1+)",
            best_when=f"comparing_with_{source_kb.name}",
        )
    
    elif usage_type == "evidence":
        grammar = GrammarRule(
            name=f"evidence_from_{source_kb.name}",
            slots=["claim_id", "supporting_ids", "supporting_data", "confidence"],
            slot_types={
                "claim_id": "id_ref",
                "supporting_ids": "id_list",
                "supporting_data": "list_of_dict",
                "confidence": "fraction",
            },
            template=[
                {"type": "line", "content": [
                    "Evidence for ", "{claim_id}", ":"]},
                {"type": "for_each", "over": "supporting_data",
                 "line": ["  - ", "{item.id}", ": ", "{item.summary}"]},
                {"type": "line", "content": [
                    "Confidence: ", "{confidence}"]},
            ],
            connection_pattern=f"has_inbound({connection_rel}, 1+)",
            best_when=f"using_{source_kb.name}_as_evidence",
        )
    
    elif usage_type == "dependency":
        grammar = GrammarRule(
            name=f"deps_on_{source_kb.name}",
            slots=["local_id", "depends_on_ids", "dependency_chain"],
            slot_types={
                "local_id": "id_ref",
                "depends_on_ids": "id_list",
                "dependency_chain": "list_of_text",
            },
            template=[
                {"type": "line", "content": [
                    "{local_id}", " depends on:"]},
                {"type": "for_each", "over": "dependency_chain",
                 "line": ["  → ", "{step}"]},
            ],
            connection_pattern=f"has_outbound({connection_rel}, 1+)",
            best_when=f"tracing_dependencies_into_{source_kb.name}",
        )
    
    elif usage_type == "summary":
        grammar = GrammarRule(
            name=f"summary_of_{source_kb.name}",
            slots=["title", "table_counts", "key_items", "key_relationships"],
            slot_types={
                "title": "text",
                "table_counts": "dict",
                "key_items": "list_of_dict",
                "key_relationships": "list_of_text",
            },
            template=[
                {"type": "line", "content": ["{title}"]},
                {"type": "for_each", "over": "table_counts",
                 "line": ["  ", "{table}", ": ", "{count}"]},
                {"type": "line", "content": ["Key items:"]},
                {"type": "for_each", "over": "key_items",
                 "line": ["  ", "{id}", " — ", "{name}"]},
            ],
            connection_pattern=f"has_outbound({connection_rel}, 1+)",
            best_when=f"summarizing_{source_kb.name}",
        )
    
    else:
        raise ValueError(f"Unknown usage type: {usage_type}")
    
    # Add grammar to target KB
    target_kb.grammars.append(grammar)
    
    # Add connection between target and source
    target_kb.connections.append(Connection(
        target_id=source_kb.id,
        target_path=source_kb.path,
        relationship=connection_rel,
        direction=Direction.OUTBOUND,
        display_grammar=grammar.name,
    ))
    
    # Add reverse connection on source
    source_kb.connections.append(Connection(
        target_id=target_kb.id,
        target_path=target_kb.path,
        relationship=connection_rel,
        direction=Direction.INBOUND,
    ))
    
    return grammar


# ============================================================
# PART 9: THE COMPACTION PIPELINE
# ============================================================

@dataclass
class CompactionPipeline:
    """Orchestrates the compaction of source material into a KB.
    
    IOSE (composite):
      Inputs: source_text (str), source_character (SourceCharacter or auto-detect),
              target_kb_path (str)
      Outputs: CompactedDocument stored as KB
      Side Effects: KB created, facts asserted, grammars generated
      Properties: deterministic given same LLM extraction judgments
      Logic Type: operational_logic
      
    The pipeline has Prolog-decidable steps and LLM-decidable steps.
    Prolog steps: profile selection, table schema lookup, constraint validation,
                  grammar generation, ID assignment.
    LLM steps: source character classification (when ambiguous),
               item extraction (what is a concept vs operation),
               relationship extraction (what depends on what),
               definition compression (prose → one-line summary).
    """
    
    registry: Any  # PathRegistry
    all_kbs: Dict[int, Any]  # Dict[int, KnowledgeBase]
    
    def compact(self, source_text: str,
                target_path: str,
                character: Optional[SourceCharacter] = None,
                parent_path: str = "root") -> CompactedDocument:
        """Run the full compaction pipeline.
        
        Steps:
        1. Classify source character (Prolog if unambiguous, LLM if ambiguous)
        2. Select compaction profile (Prolog — deterministic)
        3. Determine applicable tables (Prolog — rule evaluation)
        4. Extract items into rows (LLM — judgment required)
        5. Extract relationships (LLM — judgment required)
        6. Build section index (Prolog — mapping)
        7. Build decode legend (Prolog — collect all enums used)
        8. Validate (constraint checker)
        9. Generate grammars (deterministic from schema)
        10. Store as KB
        """
        
        # Step 1: Character classification
        if character is None:
            character = self._classify_character(source_text)
        
        # Step 2: Profile selection (deterministic)
        profile = PROFILES.get(character)
        if profile is None:
            profile = PROFILES[SourceCharacter.MIXED]
        
        # Step 3: Determine tables (deterministic from profile + source)
        tables_to_use = list(profile.required_tables)
        for opt_table in profile.optional_tables:
            schema = STANDARD_TABLES.get(opt_table)
            if schema and self._table_applicable(schema, source_text):
                tables_to_use.append(opt_table)
        tables_to_use.extend(profile.always_tables)
        
        # Steps 4-5: LLM extraction (these are the expensive steps)
        # In the real system, these are orchestrated inference steps.
        # Here we define the interface that the LLM fills.
        extracted_tables: Dict[str, CompactedTable] = {}
        for table_name in tables_to_use:
            if table_name in ("relationships", "section_index"):
                continue
            schema = STANDARD_TABLES.get(table_name)
            if schema:
                extracted_tables[table_name] = CompactedTable(
                    schema_name=table_name)
                # LLM fills: extracted_tables[table_name].rows = [...]
        
        # Relationships table (LLM fills)
        extracted_tables["relationships"] = CompactedTable(
            schema_name="relationships")
        
        # Step 6: Section index (can be Prolog-assisted)
        extracted_tables["section_index"] = CompactedTable(
            schema_name="section_index")
        
        # Step 7: Decode legend (deterministic — collect enums from schemas used)
        legend = DecodeLegend()
        rel_types_used = set()
        category_enums = set()
        for table_name in tables_to_use:
            schema = STANDARD_TABLES.get(table_name)
            if schema:
                for col in schema.columns:
                    if col.enum_values:
                        legend.add_enum(
                            f"{table_name}_{col.name}_values",
                            col.enum_values)
                    if col.col_type == ColumnType.REL_TYPE:
                        # Collect all rel types actually used
                        pass  # filled after relationship extraction
        
        # Build the document
        doc = CompactedDocument(
            title=target_path.split(".")[-1],
            source_character=character,
            profile=character.value,
            tables=extracted_tables,
            decode_legend=legend,
        )
        
        # Step 8: Validate
        # (constraint checking against decode legend enums)
        
        # Steps 9-10: Create KB and load document
        kb_id = self.registry.register(target_path)
        parent_id = self.registry.resolve(parent_path)
        
        KB = KnowledgeBase
        kb = KB(name=target_path.split(".")[-1], path=target_path,
                id=kb_id, parent_id=parent_id)
        
        kb.assert_fact("source_character", {"value": character.value})
        compacted_doc_to_kb(doc, kb, self.registry)
        
        self.all_kbs[kb_id] = kb
        if parent_id is not None and parent_id in self.all_kbs:
            self.all_kbs[parent_id].children_ids.append(kb_id)
        
        return doc
    
    def _classify_character(self, source_text: str) -> SourceCharacter:
        """Classify source character. Prolog rules for clear cases, LLM for ambiguous.
        
        Clear signals (Prolog-decidable):
          - Has 'axiom', 'theorem', 'proof' → PHILOSOPHY
          - Has 'endpoint', 'request', 'response', 'status code' → API
          - Has 'entity', 'field', 'nullable', 'foreign key' → DATA/SCHEMA
          - Has 'phase', 'step', 'deliverable' → METHODOLOGY
          - Has 'module', 'component', 'interface', 'IOSE' → SPECIFICATION
        
        Ambiguous: falls back to LLM classification.
        """
        text_lower = source_text.lower()
        
        signal_map = {
            SourceCharacter.PHILOSOPHY: ["axiom", "principle", "thesis", "claim"],
            SourceCharacter.API: ["endpoint", "status code", "request body", "response"],
            SourceCharacter.DATA: ["entity", "field", "nullable", "foreign key", "schema"],
            SourceCharacter.METHODOLOGY: ["phase", "deliverable", "milestone", "sprint"],
            SourceCharacter.SPECIFICATION: ["module", "component", "interface", "iose"],
            SourceCharacter.RESEARCH: ["finding", "hypothesis", "experiment", "result"],
        }
        
        scores = {}
        for char, signals in signal_map.items():
            score = sum(1 for s in signals if s in text_lower)
            if score > 0:
                scores[char] = score
        
        if scores:
            return max(scores, key=scores.get)
        
        return SourceCharacter.MIXED  # LLM would classify in real system
    
    def _table_applicable(self, schema: TableSchema,
                          source_text: str) -> bool:
        """Check if a table schema is applicable to the source.
        Simplified check — real system uses Prolog rule evaluation."""
        # Heuristic: check if the applicable_when condition's keywords
        # appear in the source
        condition = schema.applicable_when
        if condition == "always":
            return True
        # e.g. "source_has_principles" → check for "principle" in text
        keyword = condition.replace("source_has_", "").replace("_", " ")
        return keyword.rstrip("s") in source_text.lower()
    