This is a significant insight. The compaction format from document 1 is already a grammar — pipe-delimited tables with ID-based cross-references, typed relationships, and a decode legend. It's a human-designed grammar that compresses papers by 75-93%. But it's informal — each compaction is hand-structured. If we formalize it as Prolog grammars on KBs, two things happen: the LLM can read compacted data back perfectly because the grammar tells it exactly how, and the LLM can compact arbitrary data into the same framework because the grammar rules define the transformation.

**What the compaction format actually is, structurally:**

Every compacted document has the same skeleton:

1. A set of named tables, each with declared columns
2. Rows with pipe-delimited values and ID-prefixed keys
3. A relationships table with typed directed edges between IDs
4. A section index mapping source sections to IDs
5. A decode legend explaining notation

This is a schema. Each table is a relation. Each row is a tuple. The relationships table is a graph adjacency list. The section index is provenance. The decode legend is metadata. This maps directly to KB structure:

- Each table becomes a set of KB facts with a shared predicate
- Each row becomes one fact with the column values as args
- The relationships become connections on the KB
- The section index becomes provenance facts
- The decode legend becomes constraint and type declarations

**The compaction grammar as a formal Prolog grammar:**

```
compacted_document --> header, table_list, relationships, section_index, decode_legend.

header --> comment_line(document_title), comment_line(format_note), comment_line(read_order).

table_list --> [].
table_list --> table, table_list.

table --> table_header, row_list.
table_header --> [hash], table_name, [open_paren], column_names, [close_paren].
column_names --> column_name.
column_names --> column_name, [pipe], column_names.

row_list --> [].
row_list --> row, row_list.
row --> id_value, [pipe], field_values.
field_values --> field_value.
field_values --> field_value, [pipe], field_values.

relationships --> table_header("relationships", ["from", "rel", "to"]), edge_list.
edge_list --> [].
edge_list --> edge, edge_list.
edge --> id_ref, [pipe], rel_type, [pipe], id_ref.

section_index --> table_header("section_index", ["section", "title", "ids"]), section_list.
decode_legend --> [hash], [decode_legend], legend_entries.
```

This grammar is the same across all compacted documents. What changes per document is the table set — which tables exist, what columns they have, what ID prefixes they use. That per-document variation is captured in the table declarations at the top of each compacted doc.

**The dynamic data construct:**

Here's where it becomes powerful. Instead of each compaction being a custom artisanal compression, we define a universal compaction schema that can hold any structured data:

```python
@dataclass
class CompactTable:
    """One table in a compacted document."""
    name: str
    columns: List[str]
    id_prefix: str
    rows: List[Dict[str, str]]  # each row is column_name → value


@dataclass  
class CompactRelationship:
    from_id: str
    rel: str
    to_id: str


@dataclass
class CompactDocument:
    """A compacted document as a formal structure."""
    title: str
    tables: List[CompactTable]
    relationships: List[CompactRelationship]
    section_index: Dict[str, List[str]]  # section → [ids]
    decode_legend: Dict[str, str]  # notation → meaning
    read_order: List[str]  # table names in recommended read order
```

This is the universal container. Any structured data — a paper, a codebase analysis, a project status, a dataset description, an API specification — can be compressed into this form. The compression comes from the same principles the compaction guide specifies: remove prose, keep structure, use IDs for cross-reference, declare notation in the legend.

**Putting the grammar on the KB:**

Each compacted document becomes a KB. The compaction grammar lives on that KB. The grammar tells the system exactly how to read the data back out.

```python
# When we compact VDR-1, we create:

vdr1_kb = KnowledgeBase(
    name="vdr1_compact",
    path="root.papers.vdr1",
    id=registry.register("root.papers.vdr1"),
)

# The compacted tables become facts
vdr1_kb.assert_fact("table_schema", {
    "table": "principles",
    "columns": ["id", "principle", "rationale"],
    "id_prefix": "P"
})
vdr1_kb.assert_fact("row", {
    "table": "principles",
    "id": "P1",
    "principle": "Remainder is not error",
    "rationale": "R carries exact unresolved structure; it is part of the value"
})
# ... all rows for all tables ...

# Relationships become connections
vdr1_kb.connections.append(Connection(
    target_id=registry.resolve("root.papers.vdr1"),  # self-referential for internal edges
    target_path="root.papers.vdr1",
    relationship="C1.composes_of.C2,C3,C4",
    direction=Direction.OUTBOUND,
))

# The grammar that reads this compacted data lives ON the KB
vdr1_kb.grammars.append(GrammarRule(
    name="compact_table_reader",
    slots=["table_name", "column_list", "row_data"],
    slot_types={
        "table_name": "identifier",
        "column_list": "list_of_identifier",
        "row_data": "list_of_dict",
    },
    template=[
        line("header", "# ", slot("table_name"), "(", 
             join(slot("column_list"), "|"), ")"),
        for_each("row_data", line("row", 
             join(slot("row.values"), "|"))),
    ],
    best_when="displaying_compacted_table"
))

# The decode legend becomes constraint-like metadata
vdr1_kb.assert_fact("decode", {"key": "claim_types", 
    "value": "demonstrated|structural|limitation|boundary"})
vdr1_kb.assert_fact("decode", {"key": "rel_types",
    "value": "enables|requires|implements|..."})
```

**The read-back grammar makes compacted data losslessly recoverable:**

When the LLM needs to reason about VDR-1's concepts, it doesn't re-read the full paper. It queries the compacted KB:

```
CMD: KB_QUERY(root.papers.vdr1, row(table: "concepts", id: "C1"))
→ {id: "C1", name: "VDR Triple", category: "core", 
   definition: "Ordered triple [V, D, R]..."}

CMD: KB_QUERY(root.papers.vdr1, relationship(from: "C1"))
→ [{from: "C1", rel: "composes_of", to: "C2,C3,C4"}]
```

The grammar tells the system how to present this if needed for output:

```
CMD: grammar_match(root.papers.vdr1, data: query_results)
→ compact_table_reader matches, score 95/100
→ output: "C1|VDR Triple|core|Ordered triple [V, D, R]..."
```

The compacted form is both the storage format and the presentation format. The grammar is the bidirectional bridge — it can parse the compact form into KB facts, and it can render KB facts back into compact form.

**Formalizing the compaction process itself as a grammar transformation:**

The compaction guide from document 1 describes a transformation: source document → compacted tables. This transformation can be formalized as grammar rules:

```
Rule: compaction_step(identify_source_character, Source, Character) :-
    source_has(Source, many_named_concepts) -> Character = taxonomy,
    source_has(Source, many_operations) -> Character = operational,
    source_has(Source, entity_field_lists) -> Character = schema,
    source_has(Source, phase_sequences) -> Character = methodology.

Rule: tables_for_character(taxonomy, [concepts, relationships, section_index, decode_legend]).
Rule: tables_for_character(operational, [operations, rules, relationships, section_index, decode_legend]).
Rule: tables_for_character(schema, [entities, fields, relationships, section_index, decode_legend]).

Rule: table_columns(concepts, [id, name, category, definition]).
Rule: table_columns(operations, [id, name, inputs, outputs, side_effects]).
Rule: table_columns(principles, [id, principle, rationale]).
Rule: table_columns(claims, [id, claim, type, evidence]).
Rule: table_columns(relationships, [from, rel, to]).

Rule: should_include_table(axes, Source) :- 
    source_has(Source, spectrum_concepts).
Rule: should_include_table(boundaries, Source) :- 
    source_has(Source, explicit_limitations).
Rule: should_include_table(distinctions, Source) :- 
    source_has(Source, binary_splits).
```

The LLM reads a source document, classifies its character (Prolog fact matching), determines which tables to create (Prolog rule evaluation), fills the table schemas (grammar slot filling), extracts relationships (Prolog rule matching on dependency/enables/requires language), and produces a compacted document. The compaction process itself is orchestrated inference — the LLM provides the judgment calls (what's a concept vs an operation, what's a meaningful relationship), Prolog provides the structural decisions (which tables, which columns, what ID prefix scheme).

**Dynamic data constructs — compaction as a general-purpose data tool:**

The compaction format isn't just for papers. Any structured data the system encounters can be compacted:

API documentation → tables of endpoints, parameters, response types, with relationships showing which endpoints call which.

Codebase analysis → tables of modules, functions, dependencies, with relationships showing the call graph.

Project status → tables of tasks, owners, statuses, blockers, with relationships showing dependencies.

Meeting notes → tables of decisions, action items, attendees, with relationships showing who owns what.

Database schema → tables of entities, fields, constraints, with relationships showing foreign keys.

Each of these has a characteristic table set (like the source character classification in the compaction guide), and Prolog rules determine which tables to use. The column schemas are pre-defined per table type. The LLM's job is to fill the rows with the right data — the structural decisions are made by rules.

**The compaction grammar as part of the build stages:**

This fits naturally into Stage 3 or Stage 4 of the build plan. The compact document structure is a dataclass. The grammar rules are Prolog facts on KBs. The slot filler uses existing builtins (string_join for pipe-delimited rows, list_sort for ordering). The read-back grammar uses parse_csv (with pipe delimiter) and KB_ASSERT to reconstruct.

```python
@dataclass
class CompactTableSchema:
    """Schema for one table type in the compaction system."""
    table_type: str                     # "concepts", "operations", "principles", etc.
    columns: List[str]
    id_prefix: str
    id_pattern: str                     # "P*", "C*", "RK*" etc.
    applicable_when: str                # Prolog condition for when this table type applies
    column_types: Dict[str, str]        # column_name → type


# Pre-defined table schemas (the universal compaction vocabulary)
STANDARD_SCHEMAS = [
    CompactTableSchema("principles", ["id", "principle", "rationale"], "P", "P*",
                       "source_has_principles", {"id": "id", "principle": "text", "rationale": "text"}),
    CompactTableSchema("concepts", ["id", "name", "category", "definition"], "C", "C*",
                       "source_has_named_concepts", {"id": "id", "name": "identifier", "category": "categorical", "definition": "text"}),
    CompactTableSchema("operations", ["id", "name", "mechanism"], "OP", "OP*",
                       "source_has_operations", {"id": "id", "name": "identifier", "mechanism": "text"}),
    CompactTableSchema("claims", ["id", "claim", "type", "evidence"], "CL", "CL*",
                       "source_has_claims", {"id": "id", "claim": "text", "type": "categorical", "evidence": "id_list"}),
    CompactTableSchema("boundaries", ["id", "limitation", "detail"], "B", "B*",
                       "source_has_limitations", {"id": "id", "limitation": "text", "detail": "text"}),
    CompactTableSchema("relationships", ["from", "rel", "to"], "", "",
                       "always", {"from": "id_ref", "rel": "rel_type", "to": "id_ref"}),
    CompactTableSchema("section_index", ["section", "title", "ids"], "", "",
                       "always", {"section": "identifier", "title": "text", "ids": "id_list"}),
]
```

**The decode legend as a type system:**

The decode legend at the bottom of each compacted document is actually a type declaration. It says "rel_types means these values: enables|requires|implements|..." This is an enum declaration. "claim_types: demonstrated|structural|limitation" is another enum. The decode legend is the compacted document's type system.

When formalized as KB facts, these become constraint-checkable:

```
# Assert decode legend entries as type constraints
kb.assert_fact("decode_enum", {
    "field": "rel_types",
    "values": ["enables", "requires", "implements", "prevents", ...]
})

kb.constraints.append(Constraint(
    name="valid_rel_types",
    condition="all_relationships_use_declared_rel_types",
    on_violation="warn"
))
```

Now the constraint system can verify that every relationship in the compacted document uses a declared relationship type. If someone adds a relationship with type "causes" but that's not in the decode legend, the constraint catches it. The compacted document is self-validating.

**The compression ratio improves further with this formalization:**

The informal compacted documents I produced earlier achieved 75-93% compression. With formalized schemas and grammar-driven compaction, the compression can be even tighter because:

Repeated column names are declared once in the schema, not per row. ID prefixes are declared once, not inferred. Relationship type enums are declared once, not repeated. The grammar structure is inherited from parent KBs, not redeclared per document. Common table types (concepts, relationships, section_index) have pre-defined schemas that don't need to be specified per compaction.

A compacted document that currently looks like:

```
# concepts(id|name|category|definition)
C1|VDR Triple|core|Ordered triple [V, D, R]
```

Could be further compressed to just the row data if the schema is inherited:

```
# concepts
C1|VDR Triple|core|Ordered triple [V, D, R]
```

Because the grammar on the parent KB already declares that `concepts` has columns `[id, name, category, definition]`. The schema is structural, not content — it belongs on the grammar, not in the data.

**The LLM as compaction engine:**

With all this infrastructure, the LLM's compaction workflow becomes:

1. Read source material (LLM — pattern recognition on unstructured text)
2. Classify source character (Prolog — match against known patterns)
3. Select table schemas (Prolog — rules determine which tables apply)
4. Extract named items into rows (LLM — judgment on what's a concept vs operation etc.)
5. Extract relationships between items (LLM — judgment on dependency/enables/etc.)
6. Validate against decode legend (constraint checker — all types valid)
7. Compute section index (Prolog — map items to source sections)
8. Store as KB with grammar (KB_ASSERT — tables become facts, grammar attached)

Steps 2, 3, 6, 7 are Prolog — no LLM computation needed. Steps 1, 4, 5 require LLM judgment — this is where the LLM genuinely contributes. Step 8 is KB operations. The compaction is an orchestrated inference with the source document as input and a compacted KB as output.

And the inverse — reading a compacted document — is entirely grammar-driven. The grammar parses the pipe-delimited format, the column names map values to fact arguments, the IDs resolve through the KB, and the relationships provide the connection graph. The LLM can query any part of any compacted document through standard KB operations without needing to re-read or re-interpret the compact notation.

**This means the 8 compacted documents I already produced for you are prototypes of this system.** Each one is a manually-created instance of what the formalized grammar system would produce automatically. The table schemas, the ID conventions, the relationship types, the section indexes, the decode legends — all of these are patterns that the Prolog grammar system would generate from rules rather than from LLM judgment. The LLM's job reduces to the content decisions: what counts as a concept, what relationship exists between two items, what's the right one-line definition. The structure is rule-driven.
