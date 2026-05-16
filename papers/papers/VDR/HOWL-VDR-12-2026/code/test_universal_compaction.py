"""
test_universal_compaction.py

Tests for the universal compaction system.
Run: python3 test_universal_compaction.py
"""

from universal_compaction import (
    # Enums
    SourceCharacter, ColumnType, MountMode, Direction,
    Visibility, ConstraintScope, ConstraintStatus,
    # Structs
    ColumnDef, TableSchema, CompactionProfile, DecodeLegendEntry,
    DecodeLegend, GrammarRule, CompactedRow, CompactedTable,
    CompactedDocument, Connection, Constraint, Fact, Counter,
    LockState, KnowledgeBase, PathRegistry,
    # Functions
    compacted_doc_to_kb, kb_to_compacted_doc, generate_usage_grammar,
    # Data
    STANDARD_TABLES, PROFILES, CompactionPipeline,
)

passed = 0
failed = 0
errors = []


def check(name, condition, detail=""):
    global passed, failed, errors
    if condition:
        passed += 1
        print(f"  PASS: {name}")
    else:
        failed += 1
        msg = f"  FAIL: {name}"
        if detail:
            msg += f" — {detail}"
        print(msg)
        errors.append(name)


def section(title):
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")


# ============================================================
# 1. BASIC TYPES
# ============================================================
section("1. Basic Types and Enums")

check("SourceCharacter has PHILOSOPHY",
      SourceCharacter.PHILOSOPHY.value == "philosophy")
check("SourceCharacter has SPECIFICATION",
      SourceCharacter.SPECIFICATION.value == "specification")
check("ColumnType has ID",
      ColumnType.ID.value == "id")
check("ColumnType has ID_REF",
      ColumnType.ID_REF.value == "id_ref")
check("Direction has INBOUND",
      Direction.INBOUND.value == "inbound")


# ============================================================
# 2. COLUMN AND TABLE SCHEMA
# ============================================================
section("2. Column and Table Schema")

col = ColumnDef("name", ColumnType.IDENTIFIER, required=True,
                description="The thing's name")
check("ColumnDef construction", col.name == "name" and col.col_type == ColumnType.IDENTIFIER)

col_enum = ColumnDef("category", ColumnType.CATEGORICAL,
                     enum_values=["core", "anti-pattern"])
check("ColumnDef with enum", col_enum.enum_values == ["core", "anti-pattern"])

schema = TableSchema(
    name="test_table",
    columns=[
        ColumnDef("id", ColumnType.ID),
        ColumnDef("value", ColumnType.TEXT),
    ],
    id_prefix="TT",
    applicable_when="always",
)
check("TableSchema construction",
      schema.name == "test_table" and schema.id_prefix == "TT")
check("TableSchema has 2 columns", len(schema.columns) == 2)


# ============================================================
# 3. STANDARD TABLE LIBRARY
# ============================================================
section("3. Standard Table Library")

check("STANDARD_TABLES has principles", "principles" in STANDARD_TABLES)
check("STANDARD_TABLES has concepts", "concepts" in STANDARD_TABLES)
check("STANDARD_TABLES has claims", "claims" in STANDARD_TABLES)
check("STANDARD_TABLES has relationships", "relationships" in STANDARD_TABLES)
check("STANDARD_TABLES has section_index", "section_index" in STANDARD_TABLES)
check("STANDARD_TABLES has operations", "operations" in STANDARD_TABLES)
check("STANDARD_TABLES has boundaries", "boundaries" in STANDARD_TABLES)
check("STANDARD_TABLES has entities", "entities" in STANDARD_TABLES)
check("STANDARD_TABLES has fields", "fields" in STANDARD_TABLES)
check("STANDARD_TABLES has phases", "phases" in STANDARD_TABLES)
check("STANDARD_TABLES has builtins", "builtins" in STANDARD_TABLES)
check("STANDARD_TABLES has constraints_table", "constraints" in STANDARD_TABLES)
check("STANDARD_TABLES has components", "components" in STANDARD_TABLES)
check("STANDARD_TABLES has test_results", "test_results" in STANDARD_TABLES)
check("STANDARD_TABLES has failures", "failures" in STANDARD_TABLES)
check("STANDARD_TABLES has findings", "findings" in STANDARD_TABLES)
check("STANDARD_TABLES has benchmarks", "benchmarks" in STANDARD_TABLES)

# Verify principles schema structure
p_schema = STANDARD_TABLES["principles"]
check("principles id_prefix is P", p_schema.id_prefix == "P")
check("principles has 3 columns", len(p_schema.columns) == 3)
p_col_names = [c.name for c in p_schema.columns]
check("principles columns are id|principle|rationale",
      p_col_names == ["id", "principle", "rationale"])

# Verify concepts schema
c_schema = STANDARD_TABLES["concepts"]
check("concepts has category enum",
      c_schema.columns[2].enum_values is not None)
check("concepts category includes anti-pattern",
      "anti-pattern" in c_schema.columns[2].enum_values)

# Verify relationships schema
r_schema = STANDARD_TABLES["relationships"]
check("relationships has from|rel|to",
      [c.name for c in r_schema.columns] == ["from", "rel", "to"])
check("relationships rel column is REL_TYPE",
      r_schema.columns[1].col_type == ColumnType.REL_TYPE)


# ============================================================
# 4. COMPACTION PROFILES
# ============================================================
section("4. Compaction Profiles")

check("PROFILES has PHILOSOPHY", SourceCharacter.PHILOSOPHY in PROFILES)
check("PROFILES has SPECIFICATION", SourceCharacter.SPECIFICATION in PROFILES)
check("PROFILES has RESEARCH", SourceCharacter.RESEARCH in PROFILES)
check("PROFILES has METHODOLOGY", SourceCharacter.METHODOLOGY in PROFILES)
check("PROFILES has OPERATIONAL", SourceCharacter.OPERATIONAL in PROFILES)
check("PROFILES has DATA", SourceCharacter.DATA in PROFILES)

phil = PROFILES[SourceCharacter.PHILOSOPHY]
check("PHILOSOPHY requires principles",
      "principles" in phil.required_tables)
check("PHILOSOPHY requires concepts",
      "concepts" in phil.required_tables)
check("PHILOSOPHY always has relationships",
      "relationships" in phil.always_tables)
check("PHILOSOPHY compression target 85-93",
      phil.compression_target == (85, 93))

spec = PROFILES[SourceCharacter.SPECIFICATION]
check("SPECIFICATION requires components",
      "components" in spec.required_tables)
check("SPECIFICATION optional has builtins",
      "builtins" in spec.optional_tables)


# ============================================================
# 5. DECODE LEGEND
# ============================================================
section("5. Decode Legend")

legend = DecodeLegend()
legend.add_enum("rel_types", ["enables", "requires", "implements", "prevents"])
legend.add_enum("claim_types", ["demonstrated", "structural", "limitation"])
legend.add_notation("id_prefix", "P=principle, C=concept, CL=claim")

check("Legend has 3 entries", len(legend.entries) == 3)
check("Legend get_enum_values works",
      legend.get_enum_values("rel_types") == ["enables", "requires", "implements", "prevents"])
check("Legend get_enum_values for missing returns None",
      legend.get_enum_values("nonexistent") is None)
check("Legend notation entry type",
      legend.entries[2].entry_type == "notation")


# ============================================================
# 6. GRAMMAR RULE
# ============================================================
section("6. Grammar Rule")

grammar = GrammarRule(
    name="test_display",
    slots=["id", "name", "detail"],
    slot_types={"id": "id", "name": "identifier", "detail": "text"},
    template=[{"type": "line", "content": ["{id}: {name} — {detail}"]}],
    requires=["table_exists(concepts)"],
    best_when="displaying_concepts",
    connection_pattern="has_outbound(evaluated_by, 1+)",
)
check("GrammarRule construction", grammar.name == "test_display")
check("GrammarRule has 3 slots", len(grammar.slots) == 3)
check("GrammarRule has connection_pattern",
      grammar.connection_pattern == "has_outbound(evaluated_by, 1+)")
check("GrammarRule usage_count starts at 0", grammar.usage_count == 0)


# ============================================================
# 7. COMPACTED DOCUMENT CONSTRUCTION
# ============================================================
section("7. Compacted Document Construction")

# Build a small compacted document manually
doc = CompactedDocument(
    title="VDR-1 Test Compact",
    source_character=SourceCharacter.PHILOSOPHY,
    profile="philosophy",
    tables={},
)

# Add principles table
principles_table = CompactedTable(schema_name="principles")
principles_table.rows.append(CompactedRow(
    id="P1",
    values={"principle": "Remainder is not error",
            "rationale": "R carries exact unresolved structure"}
))
principles_table.rows.append(CompactedRow(
    id="P2",
    values={"principle": "Preserve data, compress shape",
            "rationale": "No operation may discard remainder"}
))
doc.tables["principles"] = principles_table

# Add concepts table
concepts_table = CompactedTable(schema_name="concepts")
concepts_table.rows.append(CompactedRow(
    id="C1",
    values={"name": "VDR Triple", "category": "core",
            "definition": "Ordered triple [V, D, R]"}
))
concepts_table.rows.append(CompactedRow(
    id="C2",
    values={"name": "Value Slot", "category": "slot",
            "definition": "Arbitrary-precision integer numerator"}
))
concepts_table.rows.append(CompactedRow(
    id="C3",
    values={"name": "Denominator Slot", "category": "slot",
            "definition": "Nonzero integer denominator frame"}
))
doc.tables["concepts"] = concepts_table

# Add relationships
rel_table = CompactedTable(schema_name="relationships")
rel_table.rows.append(CompactedRow(
    id="", values={"from": "C1", "rel": "composes_of", "to": "C2,C3"}
))
rel_table.rows.append(CompactedRow(
    id="", values={"from": "P1", "rel": "grounds", "to": "C1"}
))
doc.tables["relationships"] = rel_table

# Add section index
si_table = CompactedTable(schema_name="section_index")
si_table.rows.append(CompactedRow(
    id="", values={"section": "1", "title": "The Problem", "ids": "P1,P2"}
))
si_table.rows.append(CompactedRow(
    id="", values={"section": "2", "title": "The Triple", "ids": "C1,C2,C3"}
))
doc.tables["section_index"] = si_table

# Add decode legend
doc.decode_legend.add_enum("rel_types", ["composes_of", "grounds", "enables"])
doc.decode_legend.add_enum("category_values", ["core", "slot", "state"])

# Test document methods
check("doc.all_ids has 5 IDs",
      set(doc.all_ids()) == {"P1", "P2", "C1", "C2", "C3"})

found = doc.get_by_id("C1")
check("doc.get_by_id finds C1",
      found is not None and found[0] == "concepts" and found[1].values["name"] == "VDR Triple")

check("doc.get_by_id returns None for missing",
      doc.get_by_id("X99") is None)

check("doc.relationships has 2 edges",
      len(doc.relationships()) == 2)

check("doc.section_index has 2 sections",
      len(doc.section_index()) == 2)

check("principles table row_count is 2",
      principles_table.row_count() == 2)

check("concepts get_row by ID works",
      concepts_table.get_row("C2").values["name"] == "Value Slot")

check("concepts get_all_ids",
      concepts_table.get_all_ids() == ["C1", "C2", "C3"])


# ============================================================
# 8. KB INFRASTRUCTURE
# ============================================================
section("8. KB Infrastructure")

registry = PathRegistry()
check("PathRegistry root is 0", registry.resolve("root") == 0)

pid = registry.register("root.papers")
check("register returns new ID", pid == 1)
check("resolve returns same ID", registry.resolve("root.papers") == 1)
check("re-register returns same ID", registry.register("root.papers") == 1)

pid2 = registry.register("root.papers.vdr1")
check("child registration works", pid2 == 2)
check("from_id roundtrip", registry.from_id(2) == "root.papers.vdr1")
check("parent_path works", registry.parent_path("root.papers.vdr1") == "root.papers")
check("parent_path of root is None", registry.parent_path("root") is None)
check("exists works", registry.exists("root.papers") is True)
check("exists false for missing", registry.exists("root.missing") is False)
check("depth of root is 0", registry.depth("root") == 0)
check("depth of root.papers.vdr1 is 2", registry.depth("root.papers.vdr1") == 2)

# Children
registry.register("root.papers.vdr2")
children = registry.children_paths("root.papers")
check("children_paths finds children",
      set(children) == {"root.papers.vdr1", "root.papers.vdr2"})

# KB construction
kb = KnowledgeBase(name="test", path="root.test", id=99)
check("KB construction", kb.name == "test" and kb.id == 99)
check("KB facts start empty", len(kb.facts) == 0)

# Fact operations
f1 = kb.assert_fact("color", {"item": "sky", "value": "blue"}, turn=1)
check("assert_fact returns Fact", f1.predicate == "color")
check("KB has 1 fact", len(kb.facts) == 1)

f2 = kb.assert_fact("color", {"item": "sky", "value": "blue"}, turn=2)
check("assert_fact is idempotent (same fact)", len(kb.facts) == 1)

kb.assert_fact("color", {"item": "grass", "value": "green"}, turn=2)
check("KB has 2 facts after different fact", len(kb.facts) == 2)

results = kb.query_facts("color", {"item": "sky"})
check("query_facts finds matching fact",
      len(results) == 1 and results[0].args["value"] == "blue")

results_all = kb.query_facts("color")
check("query_facts without filter returns all", len(results_all) == 2)

results_none = kb.query_facts("shape")
check("query_facts returns empty for no match", len(results_none) == 0)

retracted = kb.retract_fact("color", {"item": "grass", "value": "green"}, turn=3)
check("retract_fact returns True on success", retracted is True)
check("KB has 1 fact after retract", len(kb.facts) == 1)

retracted2 = kb.retract_fact("color", {"item": "nonexistent"}, turn=3)
check("retract_fact returns False on miss", retracted2 is False)

# Counter
kb.counters["hits"] = Counter(min_value=0, max_value=100)
kb.counters["hits"].inc()
kb.counters["hits"].inc()
kb.counters["hits"].inc()
check("Counter inc works", kb.counters["hits"].get() == 3)

kb.counters["hits"].dec()
check("Counter dec works", kb.counters["hits"].get() == 2)

kb.counters["hits"].add(10)
check("Counter add works", kb.counters["hits"].get() == 12)

kb.counters["hits"].set(50)
check("Counter set works", kb.counters["hits"].get() == 50)

kb.counters["hits"].set(200)
check("Counter clamps at max", kb.counters["hits"].get() == 100)

kb.counters["hits"].reset()
check("Counter reset works", kb.counters["hits"].get() == 0)

# Lock
kb.locks["editing"] = LockState()
check("Lock starts free", kb.locks["editing"].check() is False)

acquired = kb.locks["editing"].acquire("worker_1")
check("Lock acquire succeeds when free", acquired is True)
check("Lock is held after acquire", kb.locks["editing"].check() is True)
check("Lock holder is set", kb.locks["editing"].holder == "worker_1")

acquired2 = kb.locks["editing"].acquire("worker_2")
check("Lock acquire fails when held", acquired2 is False)
check("Lock holder unchanged", kb.locks["editing"].holder == "worker_1")

kb.locks["editing"].release()
check("Lock free after release", kb.locks["editing"].check() is False)

# Reset live state
kb.counters["hits"].set(42)
kb.locks["editing"].acquire("someone")
kb.working_data["temp"] = "value"
kb.reset_live()
check("reset_live clears counter", kb.counters["hits"].get() == 0)
check("reset_live releases lock", kb.locks["editing"].check() is False)
check("reset_live clears working_data", len(kb.working_data) == 0)
check("reset_live preserves facts", len(kb.facts) == 1)


# ============================================================
# 9. COMPACTED DOC → KB CONVERSION
# ============================================================
section("9. Compacted Doc → KB Conversion")

target_registry = PathRegistry()
target_id = target_registry.register("root.papers.vdr1_compact")
target_kb = KnowledgeBase(
    name="vdr1_compact",
    path="root.papers.vdr1_compact",
    id=target_id,
    parent_id=0,
)

compacted_doc_to_kb(doc, target_kb, target_registry)

# Check facts were created
schema_facts = target_kb.query_facts("table_schema")
check("table_schema facts created", len(schema_facts) >= 2)

principle_facts = target_kb.query_facts("principles")
check("principle facts created", len(principle_facts) == 2)

p1_facts = target_kb.query_facts("principles", {"id": "P1"})
check("P1 fact has correct principle",
      len(p1_facts) == 1 and "Remainder" in p1_facts[0].args.get("principle", ""))

concept_facts = target_kb.query_facts("concepts")
check("concept facts created", len(concept_facts) == 3)

c1_facts = target_kb.query_facts("concepts", {"id": "C1"})
check("C1 fact has correct name",
      len(c1_facts) == 1 and c1_facts[0].args.get("name") == "VDR Triple")

c2_facts = target_kb.query_facts("concepts", {"id": "C2"})
check("C2 fact has correct category",
      len(c2_facts) == 1 and c2_facts[0].args.get("category") == "slot")

# Check section index
si_facts = target_kb.query_facts("section_index")
check("section_index facts created", len(si_facts) == 2)

# Check decode legend
decode_facts = target_kb.query_facts("decode")
check("decode legend facts created", len(decode_facts) >= 2)

rel_decode = [d for d in decode_facts if d.args.get("key") == "rel_types"]
check("rel_types decode entry exists", len(rel_decode) == 1)

# Check connections (from relationships)
check("connections created from relationships", len(target_kb.connections) >= 2)

# Check constraints (from enum declarations)
check("constraints created from decode enums", len(target_kb.constraints) >= 2)

# Check grammars were auto-generated
check("grammars were auto-generated", len(target_kb.grammars) > 0)

grammar_names = [g.name for g in target_kb.grammars]
check("compact_display grammar exists", "compact_display" in grammar_names)
check("document_summary grammar exists", "document_summary" in grammar_names)
check("extract_principles grammar exists", "extract_principles" in grammar_names)
check("extract_concepts grammar exists", "extract_concepts" in grammar_names)
check("detail_principles grammar exists", "detail_principles" in grammar_names)
check("detail_concepts grammar exists", "detail_concepts" in grammar_names)
check("relationship_display grammar exists", "relationship_display" in grammar_names)


# ============================================================
# 10. KB → COMPACTED DOC CONVERSION (ROUNDTRIP)
# ============================================================
section("10. KB → Compacted Doc Roundtrip")

# Store source character for roundtrip
target_kb.assert_fact("source_character", {"value": "philosophy"})

reconstructed = kb_to_compacted_doc(target_kb)
check("Roundtrip produces document", reconstructed is not None)

if reconstructed:
    check("Roundtrip title matches", reconstructed.title == "vdr1_compact")
    check("Roundtrip character matches",
          reconstructed.source_character == SourceCharacter.PHILOSOPHY)
    check("Roundtrip has principles table",
          "principles" in reconstructed.tables)
    check("Roundtrip has concepts table",
          "concepts" in reconstructed.tables)
    check("Roundtrip principles has 2 rows",
          reconstructed.tables["principles"].row_count() == 2)
    check("Roundtrip concepts has 3 rows",
          reconstructed.tables["concepts"].row_count() == 3)

    # Verify specific data survived roundtrip
    rt_c1 = reconstructed.tables["concepts"].get_row("C1")
    check("Roundtrip C1 name preserved",
          rt_c1 is not None and rt_c1.values.get("name") == "VDR Triple")

    rt_p1 = reconstructed.tables["principles"].get_row("P1")
    check("Roundtrip P1 preserved",
          rt_p1 is not None and "Remainder" in rt_p1.values.get("principle", ""))

    check("Roundtrip has section_index",
          "section_index" in reconstructed.tables)

    check("Roundtrip has decode legend entries",
          len(reconstructed.decode_legend.entries) >= 2)


# ============================================================
# 11. USAGE GRAMMAR GENERATION
# ============================================================
section("11. Usage Grammar Generation")

# Create a second KB that will use data from the first
user_registry = PathRegistry()
source_id = user_registry.register("root.papers.vdr1")
source_kb = KnowledgeBase(name="vdr1", path="root.papers.vdr1", id=source_id)
# Add a table_schema fact so generate_usage_grammar can find available tables
source_kb.assert_fact("table_schema", {"table": "concepts", "columns": ["id", "name", "category", "definition"]})
source_kb.assert_fact("table_schema", {"table": "principles", "columns": ["id", "principle", "rationale"]})

target_usage_id = user_registry.register("root.project.analysis")
target_usage_kb = KnowledgeBase(name="analysis", path="root.project.analysis",
                                id=target_usage_id)

# Generate reference grammar
ref_grammar = generate_usage_grammar(
    source_kb=source_kb,
    target_kb=target_usage_kb,
    usage_type="reference",
    connection_rel="references",
)
check("reference grammar created", ref_grammar.name == "ref_vdr1")
check("reference grammar has 4 slots", len(ref_grammar.slots) == 4)
check("reference grammar on target KB",
      any(g.name == "ref_vdr1" for g in target_usage_kb.grammars))
check("target KB has connection to source",
      any(c.target_id == source_id for c in target_usage_kb.connections))
check("source KB has reverse connection",
      any(c.target_id == target_usage_id for c in source_kb.connections))

# Generate comparison grammar
comp_grammar = generate_usage_grammar(
    source_kb=source_kb,
    target_kb=target_usage_kb,
    usage_type="comparison",
    connection_rel="compares_with",
)
check("comparison grammar created", comp_grammar.name == "compare_with_vdr1")

# Generate evidence grammar
ev_grammar = generate_usage_grammar(
    source_kb=source_kb,
    target_kb=target_usage_kb,
    usage_type="evidence",
    connection_rel="evidence_from",
)
check("evidence grammar created", ev_grammar.name == "evidence_from_vdr1")
check("evidence grammar has confidence slot",
      "confidence" in ev_grammar.slot_types)

# Generate dependency grammar
dep_grammar = generate_usage_grammar(
    source_kb=source_kb,
    target_kb=target_usage_kb,
    usage_type="dependency",
    connection_rel="depends_on",
)
check("dependency grammar created", dep_grammar.name == "deps_on_vdr1")

# Generate summary grammar
sum_grammar = generate_usage_grammar(
    source_kb=source_kb,
    target_kb=target_usage_kb,
    usage_type="summary",
    connection_rel="summarizes",
)
check("summary grammar created", sum_grammar.name == "summary_of_vdr1")

# Check all 5 grammars are on target KB
check("target KB has 5 usage grammars", len(target_usage_kb.grammars) == 5)
check("target KB has 5 connections", len(target_usage_kb.connections) == 5)


# ============================================================
# 12. COMPACTION PIPELINE
# ============================================================
section("12. Compaction Pipeline")

pipe_registry = PathRegistry()
pipe_kbs = {}
root_kb = KnowledgeBase(name="root", path="root", id=0)
pipe_kbs[0] = root_kb

pipeline = CompactionPipeline(registry=pipe_registry, all_kbs=pipe_kbs)

# Test character classification
check("classify PHILOSOPHY from text",
      pipeline._classify_character("The core principle and thesis is that axioms matter")
      == SourceCharacter.PHILOSOPHY)

check("classify API from text",
      pipeline._classify_character("The endpoint returns status code 200 with request body")
      == SourceCharacter.API)

check("classify DATA from text",
      pipeline._classify_character("The entity has a nullable field with a foreign key")
      == SourceCharacter.DATA)

check("classify METHODOLOGY from text",
      pipeline._classify_character("Phase one deliverable is the milestone report")
      == SourceCharacter.METHODOLOGY)

check("classify SPECIFICATION from text",
      pipeline._classify_character("Each module and component has an interface defined by IOSE")
      == SourceCharacter.SPECIFICATION)

check("classify RESEARCH from text",
      pipeline._classify_character("The experiment finding confirms our hypothesis about the result")
      == SourceCharacter.RESEARCH)

check("classify MIXED from unknown text",
      pipeline._classify_character("The quick brown fox jumps over the lazy dog")
      == SourceCharacter.MIXED)

# Test table applicability
principles_schema = STANDARD_TABLES["principles"]
check("principles applicable to text with principles",
      pipeline._table_applicable(principles_schema,
                                  "The core principle is exactness"))
check("principles not applicable to unrelated text",
      not pipeline._table_applicable(principles_schema,
                                      "The quick brown fox"))

# Test full compaction pipeline
source_text = """
This paper presents the core principle of exact arithmetic.
The first principle is that remainder is not error.
The second principle is preserve data, compress shape.
The main concept is the VDR Triple, an ordered triple [V, D, R].
The claim is that zero drift holds across arbitrary operation chains.
A key boundary is that chaotic dynamics have exponential cost.
"""

compact_result = pipeline.compact(
    source_text=source_text,
    target_path="root.compacted.test_paper",
    character=SourceCharacter.PHILOSOPHY,
)

check("Pipeline produces CompactedDocument",
      isinstance(compact_result, CompactedDocument))
check("Pipeline document has correct character",
      compact_result.source_character == SourceCharacter.PHILOSOPHY)
check("Pipeline document has principles table",
      "principles" in compact_result.tables)
check("Pipeline document has concepts table",
      "concepts" in compact_result.tables)
check("Pipeline document has relationships table",
      "relationships" in compact_result.tables)
check("Pipeline document has section_index table",
      "section_index" in compact_result.tables)

# Check KB was created
compact_kb_id = pipe_registry.resolve("root.compacted.test_paper")
check("Pipeline registered KB path", compact_kb_id is not None)
check("Pipeline KB in all_kbs", compact_kb_id in pipe_kbs)

if compact_kb_id in pipe_kbs:
    compact_kb = pipe_kbs[compact_kb_id]
    check("Pipeline KB has source_character fact",
          len(compact_kb.query_facts("source_character")) == 1)
    check("Pipeline KB has table_schema facts",
          len(compact_kb.query_facts("table_schema")) > 0)
    check("Pipeline KB has grammars",
          len(compact_kb.grammars) > 0)
    check("Pipeline KB has decode legend",
          len(compact_kb.query_facts("decode")) > 0)


# ============================================================
# 13. CROSS-KB USAGE SCENARIO
# ============================================================
section("13. Cross-KB Usage Scenario (Integration)")

# Simulate: we have compacted VDR-1 data and want to use it
# in an inference notebook

int_registry = PathRegistry()
int_kbs = {}

# Root
int_root = KnowledgeBase(name="root", path="root", id=int_registry.register("root"))
int_kbs[int_root.id] = int_root

# VDR-1 compacted data KB
vdr1_id = int_registry.register("root.papers.vdr1")
vdr1_kb = KnowledgeBase(name="vdr1", path="root.papers.vdr1",
                         id=vdr1_id, parent_id=int_root.id)
int_kbs[vdr1_id] = vdr1_kb

# Load our test compacted doc into it
compacted_doc_to_kb(doc, vdr1_kb, int_registry)

# Create inference notebook KB
nb_id = int_registry.register("root.inference.notebook_001")
nb_kb = KnowledgeBase(name="notebook_001", path="root.inference.notebook_001",
                       id=nb_id, parent_id=int_root.id)
int_kbs[nb_id] = nb_kb

# Generate evidence grammar linking notebook to VDR-1
evidence_grammar = generate_usage_grammar(
    source_kb=vdr1_kb,
    target_kb=nb_kb,
    usage_type="evidence",
    connection_rel="evidence_source",
)

check("Integration: evidence grammar created on notebook",
      any(g.name == "evidence_from_vdr1" for g in nb_kb.grammars))
check("Integration: notebook connected to vdr1",
      any(c.target_id == vdr1_id and c.relationship == "evidence_source"
          for c in nb_kb.connections))
check("Integration: vdr1 has reverse connection to notebook",
      any(c.target_id == nb_id and c.relationship == "evidence_source"
          for c in vdr1_kb.connections))

# The notebook can now query VDR-1 data as evidence
# Simulate: query concepts from VDR-1
vdr1_concepts = vdr1_kb.query_facts("concepts")
check("Integration: can query VDR-1 concepts from connection",
      len(vdr1_concepts) == 3)

# Assert findings in notebook that reference VDR-1 IDs
nb_kb.assert_fact("evidence", {
    "source": "root.papers.vdr1",
    "source_id": "C1",
    "claim": "VDR Triple is the core representation",
    "confidence_n": 95,
    "confidence_d": 100,
})
check("Integration: evidence fact asserted in notebook",
      len(nb_kb.query_facts("evidence")) == 1)

# The grammar tells us how to display this evidence
ev_grammars = [g for g in nb_kb.grammars if g.name == "evidence_from_vdr1"]
check("Integration: evidence grammar has confidence slot",
      len(ev_grammars) == 1 and "confidence" in ev_grammars[0].slot_types)

# Verify grammar connection_pattern
check("Integration: evidence grammar has inbound connection pattern",
      ev_grammars[0].connection_pattern == "has_inbound(evidence_source, 1+)")


# ============================================================
# 14. GRAMMAR INHERITANCE CONCEPT
# ============================================================
section("14. Grammar Inheritance Through KB Tree")

# Create a KB tree where child inherits parent grammars
inh_registry = PathRegistry()

inh_root_id = inh_registry.register("root")
inh_root = KnowledgeBase(name="root", path="root", id=inh_root_id)
inh_root.grammars.append(GrammarRule(
    name="basic_list",
    slots=["items"],
    slot_types={"items": "list"},
    template=[{"type": "for_each", "over": "items", "line": ["- ", "{item}"]}],
    best_when="listing_items",
))

inh_project_id = inh_registry.register("root.project")
inh_project = KnowledgeBase(name="project", path="root.project",
                             id=inh_project_id, parent_id=inh_root_id)
inh_project.grammars.append(GrammarRule(
    name="code_block",
    slots=["language", "code"],
    slot_types={"language": "identifier", "code": "text"},
    template=[{"type": "fenced", "language": "{language}", "content": "{code}"}],
    best_when="displaying_code",
))

inh_sub_id = inh_registry.register("root.project.vdr")
inh_sub = KnowledgeBase(name="vdr", path="root.project.vdr",
                         id=inh_sub_id, parent_id=inh_project_id)
# vdr KB has no grammars of its own — inherits from project and root

# Collect grammars walking up the tree
def collect_inherited_grammars(kb, all_kbs):
    """Walk up tree, collect grammars. Child overrides parent by name."""
    grammars = {}
    current_id = kb.id
    while current_id is not None:
        current_kb = all_kbs.get(current_id)
        if current_kb is None:
            break
        for g in current_kb.grammars:
            if g.name not in grammars:  # first (most local) wins
                grammars[g.name] = g
        current_id = current_kb.parent_id
    return list(grammars.values())

all_inh_kbs = {
    inh_root_id: inh_root,
    inh_project_id: inh_project,
    inh_sub_id: inh_sub,
}

vdr_grammars = collect_inherited_grammars(inh_sub, all_inh_kbs)
vdr_grammar_names = [g.name for g in vdr_grammars]

check("Inheritance: vdr inherits basic_list from root",
      "basic_list" in vdr_grammar_names)
check("Inheritance: vdr inherits code_block from project",
      "code_block" in vdr_grammar_names)
check("Inheritance: vdr has 2 inherited grammars",
      len(vdr_grammars) == 2)

# Test override: vdr adds its own basic_list that shadows root's
inh_sub.grammars.append(GrammarRule(
    name="basic_list",
    slots=["items"],
    slot_types={"items": "list"},
    template=[{"type": "numbered", "over": "items", "line": ["{n}. ", "{item}"]}],
    best_when="listing_items_numbered",
))

vdr_grammars2 = collect_inherited_grammars(inh_sub, all_inh_kbs)
check("Override: vdr now has its own basic_list",
      any(g.name == "basic_list" and g.best_when == "listing_items_numbered"
          for g in vdr_grammars2))
check("Override: root basic_list is shadowed",
      not any(g.name == "basic_list" and g.best_when == "listing_items"
              for g in vdr_grammars2))
check("Override: code_block still inherited",
      any(g.name == "code_block" for g in vdr_grammars2))


# ============================================================
# RESULTS
# ============================================================
section("RESULTS")

total = passed + failed
print(f"\n  Total:  {total}")
print(f"  Passed: {passed}")
print(f"  Failed: {failed}")

if errors:
    print(f"\n  Failed tests:")
    for e in errors:
        print(f"    - {e}")

print()
if failed == 0:
    print("  ALL TESTS PASSED")
else:
    print(f"  {failed} TESTS FAILED")

exit(0 if failed == 0 else 1)
