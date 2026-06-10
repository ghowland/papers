# SiQL — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: thesis → mapping → advantages → claims

# thesis(id|claim)
T1|SiQL is a SQL-replacement using Prolog for queries
T2|Prolog can do everything SQL can do, plus recursion, graph traversal, logic composition, dynamic queries, type safety, auto-complete
T3|SQL can only query. Prolog queries AND reasons. Zero compromises, pure upside

# sql_to_prolog(id|sql_category|sql_feature|prolog_mechanism|example)
S1|SELECT|SELECT columns|Rule head|result(Name, Health) :-
S2|SELECT|SELECT *|Return entity|result(Actor) :-
S3|SELECT|SELECT DISTINCT|distinct|distinct
S4|SELECT|SELECT AS (alias)|Head variable names|result(PlayerName, HP) :-
S5|FROM|FROM|DR path|character.name(Actor, Name)
S6|FROM|FROM multiple tables|Multiple paths|actor(A), faction(F)
S7|FROM|Table alias|Variable|A is the alias
S8|WHERE|= |Unification|faction_id(A, enemy)
S9|WHERE|<, >, <=, >=|Comparison|Health < 50
S10|WHERE|!=|\=|Faction \= player
S11|WHERE|BETWEEN|Range|Health >= 20, Health <= 80
S12|WHERE|IN|Member|member(Faction, [enemy, neutral])
S13|WHERE|NOT IN|\+ member|\+ member(Faction, [player, ally])
S14|WHERE|LIKE|Pattern match|prefix(Name, "Skeleton")
S15|WHERE|IS NULL|Var check|var(Value) or Value = null
S16|WHERE|IS NOT NULL|Nonvar|nonvar(Value)
S17|WHERE|AND|Comma|A, B, C
S18|WHERE|OR|Semicolon|A ; B
S19|WHERE|NOT|\+|\+ enemy(A)
S20|JOIN|INNER JOIN|Shared variable|faction_id(A, F), faction.name(F, Name)
S21|JOIN|LEFT JOIN|Optional match|(faction_id(A, F), faction.name(F, Name) ; Name = null)
S22|JOIN|RIGHT JOIN|Flip left join|Same pattern, different order
S23|JOIN|FULL OUTER JOIN|Union of left joins|Two clauses
S24|JOIN|CROSS JOIN|No shared var|actor(A), faction(F)
S25|JOIN|SELF JOIN|Different vars|actor(A), actor(B), A \= B
S26|ORDER|ORDER BY ASC|sort|sort(Health, asc)
S27|ORDER|ORDER BY DESC|sort|sort(Health, desc)
S28|ORDER|ORDER BY multiple|sort list|sort([Faction, Health])
S29|LIMIT|LIMIT|limit|limit(10)
S30|LIMIT|OFFSET|offset|offset(20)
S31|AGG|COUNT(*)|count/2|count(A, enemy(A), N)
S32|AGG|COUNT(DISTINCT)|count + distinct|count(A, enemy(A), N) distinct(A)
S33|AGG|SUM|sum/3|sum(H, character.health.value(A, H), Total)
S34|AGG|AVG|avg/3|avg(H, character.health.value(A, H), Mean)
S35|AGG|MIN|min/3|min(H, character.health.value(A, H), Lowest)
S36|AGG|MAX|max/3|max(H, character.health.value(A, H), Highest)
S37|AGG|GROUP BY|Implicit in aggregation|Grouped by unbound vars
S38|AGG|HAVING|Condition after agg|count(..., N), N > 5
S39|SET|UNION|Multiple clauses|Two rules, same head
S40|SET|UNION ALL|Multiple + all|all (keep duplicates)
S41|SET|INTERSECT|Both conditions|rule1(X), rule2(X)
S42|SET|EXCEPT|Negation|rule1(X), \+ rule2(X)
S43|SUB|Subquery in WHERE|Rule call|enemy(A) :- evil_faction(A.faction)
S44|SUB|Correlated subquery|Shared variable|Variable flows into sub-rule
S45|SUB|EXISTS|\+ \+|\+ \+ enemy(A)
S46|SUB|NOT EXISTS|\+|\+ enemy(A)
S47|COND|CASE WHEN|Conditional clauses|Multiple rules with guards
S48|COND|COALESCE|Default|(Value = X ; X = default)
S49|COND|NULLIF|Conditional null|(A = B -> X = null ; X = A)
S50|COND|CAST|Type conversion|float(X, Y) builtin
S51|DML|INSERT|assert|assert(character.health.value(5, 100))
S52|DML|UPDATE|retract + assert|retract(old), assert(new)
S53|DML|DELETE|retract|retract(character(5, _))
S54|DML|UPSERT|Conditional|(exists(X) -> update(X) ; insert(X))

# prolog_advantages(id|feature|sql_capability|prolog_capability)
PA1|Recursion|CTE (clunky, verbose)|Native — 2 lines vs 8 lines for ancestor query
PA2|Graph traversal|Impossible without known depth or recursive CTE|Trivial — nearby(X, N) with connected/2
PA3|Pattern matching|LIKE only|Full unification
PA4|Logic composition|Views (static)|Rules (dynamic, rules call rules)
PA5|Backtracking|N/A|Native
PA6|Negation as failure|NOT EXISTS (limited)|\+ (general)
PA7|Meta-queries|N/A|Query the rules themselves
PA8|Type safety|Schema-external|DR paths validated
PA9|Auto-complete|Tool-dependent|Schema-driven

# objections_addressed(id|concern|reality)
OA1|Prolog is slow|Ground term matching = direct comparison
OA2|Prolog is weird|DR paths make it readable
OA3|SQL is standard|Your engine, your standard
OA4|Tooling|You're building the tooling

# decode_legend
sql_categories: SELECT|FROM|WHERE|JOIN|ORDER|LIMIT|AGG(aggregation)|SET(set operations)|SUB(subqueries)|COND(conditionals)|DML(data manipulation)
id_prefixes: T=thesis|S=sql_to_prolog_mapping|PA=prolog_advantage|OA=objection_addressed
DR: Data Record path notation — schema-driven dot-separated field access
core_claim: SQL is query language bolted onto relational algebra. Prolog is logic that happens to query data. Full SQL feature parity plus recursion, graph traversal, logic composition, dynamic queries
