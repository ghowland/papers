# VDR-Prolog Computational Primitives
## Built-in Pure Functions as First-Class Predicate Operations

---

## 1. The Problem With Token-Matched Computation

When a language model is asked to sort a list, reverse a string, compute a factorial, or find the maximum of a set, it does not execute an algorithm. It generates tokens that pattern-match against training examples of those operations. This means:

A sort of 5 items usually works. A sort of 50 items sometimes has errors. A sort of 500 items will fail. The failure mode is not "out of memory" or "timeout" — it is "generated the wrong answer confidently." The model does not know it failed because it was never computing. It was predicting what sorted output looks like.

This is wasteful and unreliable. String reversal is a solved problem. Array sorting is a solved problem. GCD computation is a solved problem. Arithmetic is a solved problem — and yet VDR exists precisely because the LLM's arithmetic is unreliable.

The fix is to make these operations built-in predicates in the Prolog layer. When the system needs to sort a list, it calls a tested, constrained, pure function that produces the correct result every time. The LLM does not generate the sorted output. The primitive computes it. The LLM's role is to recognize that sorting is needed and to frame the result for the user.

---

## 2. What Makes a Good Primitive

A function qualifies as a VDR-Prolog primitive if it satisfies all of the following:

**Pure.** Same inputs always produce the same output. No side effects. No state. No randomness (unless explicitly seeded through the RNG primitive).

**Finite.** Terminates on all valid inputs. Bounded execution time relative to input size. No infinite loops, no unbounded recursion.

**Exact.** Produces the exactly correct result. Not approximately correct. Not usually correct. Exactly correct, verifiable by specification.

**Tested.** Covered by a test suite that exercises edge cases, boundary conditions, and adversarial inputs. The primitive has earned its place through verification.

**Typed.** Inputs and outputs have declared types from the VDR-Prolog term system. Type violations are caught before execution, not discovered in the output.

**Constrained.** The primitive's purpose is narrow and declared. It does one thing. Its constraints (preconditions, postconditions, invariants) are Prolog facts in the constraint system.

---

## 3. Primitive Categories and Examples

### Category 1: String Operations

Operations on atom values and text. Every operation produces an exact result.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| string_reverse | atom → atom | Reverse character order | string_reverse("hello") → "olleh" |
| string_length | atom → number | Character count | string_length("hello") → 5 |
| string_concat | atom, atom → atom | Concatenation | string_concat("he", "llo") → "hello" |
| string_slice | atom, number, number → atom | Substring by start, end | string_slice("hello", 1, 3) → "el" |
| string_contains | atom, atom → bool | Substring test | string_contains("hello", "ell") → true |
| string_split | atom, atom → list(atom) | Split by delimiter | string_split("a,b,c", ",") → ["a","b","c"] |
| string_join | list(atom), atom → atom | Join with delimiter | string_join(["a","b","c"], ",") → "a,b,c" |
| string_trim | atom → atom | Remove leading/trailing whitespace | string_trim("  hi  ") → "hi" |
| string_upper | atom → atom | Uppercase | string_upper("hello") → "HELLO" |
| string_lower | atom → atom | Lowercase | string_lower("HELLO") → "hello" |
| string_replace | atom, atom, atom → atom | Replace all occurrences | string_replace("abab", "b", "x") → "axax" |
| string_starts_with | atom, atom → bool | Prefix test | string_starts_with("hello", "he") → true |
| string_ends_with | atom, atom → bool | Suffix test | string_ends_with("hello", "lo") → true |
| string_pad_left | atom, number, atom → atom | Left-pad to width | string_pad_left("42", 5, "0") → "00042" |
| string_char_at | atom, number → atom | Character at index | string_char_at("hello", 0) → "h" |
| string_to_chars | atom → list(atom) | Explode to char list | string_to_chars("hi") → ["h", "i"] |
| chars_to_string | list(atom) → atom | Implode from char list | chars_to_string(["h", "i"]) → "hi" |

**Why these matter for LLMs:** Token manipulation, output formatting, template filling, vocabulary operations. Every one of these is a common source of LLM errors when done by token prediction. As primitives, they are infallible.

### Category 2: List / Array Operations

Operations on list terms. All produce exact results. Sorting uses declared comparison rules.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| list_length | list → number | Element count | list_length([1,2,3]) → 3 |
| list_append | list, term → list | Add to end | list_append([1,2], 3) → [1,2,3] |
| list_prepend | term, list → list | Add to front | list_prepend(0, [1,2]) → [0,1,2] |
| list_concat | list, list → list | Concatenate | list_concat([1,2], [3,4]) → [1,2,3,4] |
| list_reverse | list → list | Reverse order | list_reverse([1,2,3]) → [3,2,1] |
| list_sort | list, rule → list | Sort by rule | list_sort([3,1,2], ascending) → [1,2,3] |
| list_sort_reverse | list, rule → list | Sort descending by rule | list_sort_reverse([3,1,2], ascending) → [3,2,1] |
| list_sort_by_key | list(term), key_fn → list(term) | Sort by extracted key | list_sort_by_key(people, "age") → sorted by age |
| list_unique | list → list | Remove duplicates, preserve order | list_unique([1,2,1,3]) → [1,2,3] |
| list_flatten | list(list) → list | One-level flatten | list_flatten([[1,2],[3]]) → [1,2,3] |
| list_zip | list, list → list(pair) | Pair-wise zip | list_zip([1,2], ["a","b"]) → [(1,"a"),(2,"b")] |
| list_unzip | list(pair) → (list, list) | Unzip pairs | list_unzip([(1,"a"),(2,"b")]) → ([1,2],["a","b"]) |
| list_head | list → term | First element | list_head([1,2,3]) → 1 |
| list_tail | list → list | All but first | list_tail([1,2,3]) → [2,3] |
| list_last | list → term | Last element | list_last([1,2,3]) → 3 |
| list_init | list → list | All but last | list_init([1,2,3]) → [1,2] |
| list_nth | list, number → term | Element at index | list_nth([10,20,30], 1) → 20 |
| list_take | list, number → list | First N elements | list_take([1,2,3,4], 2) → [1,2] |
| list_drop | list, number → list | Skip first N | list_drop([1,2,3,4], 2) → [3,4] |
| list_slice | list, number, number → list | Sublist by range | list_slice([1,2,3,4,5], 1, 3) → [2,3,4] |
| list_filter | list, predicate → list | Keep matching | list_filter([1,2,3,4], is_even) → [2,4] |
| list_map | list, fn → list | Apply to each | list_map([1,2,3], double) → [2,4,6] |
| list_reduce | list, fn, init → term | Fold left | list_reduce([1,2,3], add, 0) → 6 |
| list_any | list, predicate → bool | Any match | list_any([1,2,3], is_even) → true |
| list_all | list, predicate → bool | All match | list_all([2,4,6], is_even) → true |
| list_count | list, predicate → number | Count matching | list_count([1,2,3,4], is_even) → 2 |
| list_index_of | list, term → number | First occurrence | list_index_of([10,20,30], 20) → 1 |
| list_contains | list, term → bool | Membership test | list_contains([1,2,3], 2) → true |
| list_min | list → term | Minimum element | list_min([3,1,2]) → 1 |
| list_max | list → term | Maximum element | list_max([3,1,2]) → 3 |
| list_enumerate | list → list(pair) | Add indices | list_enumerate(["a","b"]) → [(0,"a"),(1,"b")] |
| list_chunk | list, number → list(list) | Split into chunks | list_chunk([1,2,3,4,5,6], 2) → [[1,2],[3,4],[5,6]] |
| list_interleave | list, list → list | Alternating merge | list_interleave([1,3,5],[2,4,6]) → [1,2,3,4,5,6] |
| list_partition | list, predicate → (list, list) | Split by predicate | list_partition([1,2,3,4], is_even) → ([2,4],[1,3]) |
| list_group_by | list(term), key_fn → dict | Group by key | list_group_by(people, "dept") → {eng: [...], legal: [...]} |
| list_frequencies | list → dict | Count occurrences | list_frequencies([1,1,2,3,3,3]) → {1:2, 2:1, 3:3} |

**Why these matter:** Sorting and filtering are among the most common operations LLMs get wrong at scale. A 20-element sort by token prediction has maybe 95% accuracy. A 100-element sort drops to near zero. As primitives, accuracy is 100% regardless of size.

### Category 3: VDR Arithmetic

Exact fraction operations. These are the VDR operations exposed as Prolog predicates.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| vdr_add | fraction, fraction → fraction | Exact addition | vdr_add(1/3, 1/4) → 7/12 |
| vdr_sub | fraction, fraction → fraction | Exact subtraction | vdr_sub(1/2, 1/3) → 1/6 |
| vdr_mul | fraction, fraction → fraction | Exact multiplication | vdr_mul(2/3, 3/5) → 2/5 |
| vdr_div | fraction, fraction → fraction | Exact division | vdr_div(1/2, 1/3) → 3/2 |
| vdr_neg | fraction → fraction | Exact negation | vdr_neg(3/7) → -3/7 |
| vdr_abs | fraction → fraction | Absolute value | vdr_abs(-3/7) → 3/7 |
| vdr_pow | fraction, number → fraction | Integer power | vdr_pow(2/3, 3) → 8/27 |
| vdr_gcd | number, number → number | Greatest common divisor | vdr_gcd(12, 8) → 4 |
| vdr_lcm | number, number → number | Least common multiple | vdr_lcm(4, 6) → 12 |
| vdr_mod | number, number → number | Modular remainder | vdr_mod(17, 5) → 2 |
| vdr_floor | fraction → number | Floor to integer | vdr_floor(7/3) → 2 |
| vdr_ceil | fraction → number | Ceiling to integer | vdr_ceil(7/3) → 3 |
| vdr_round | fraction → number | Round to nearest integer | vdr_round(7/4) → 2 |
| vdr_numerator | fraction → number | Extract numerator | vdr_numerator(3/7) → 3 |
| vdr_denominator | fraction → number | Extract denominator | vdr_denominator(3/7) → 7 |
| vdr_is_integer | fraction → bool | Denominator is 1 | vdr_is_integer(6/1) → true |
| vdr_simplify | fraction → fraction | Reduce to lowest terms | vdr_simplify(6/4) → 3/2 |
| vdr_compare | fraction, fraction → atom | Ordering | vdr_compare(1/3, 1/2) → less |
| vdr_min | fraction, fraction → fraction | Minimum | vdr_min(1/3, 1/2) → 1/3 |
| vdr_max | fraction, fraction → fraction | Maximum | vdr_max(1/3, 1/2) → 1/2 |
| vdr_sum | list(fraction) → fraction | Sum of list | vdr_sum([1/2, 1/3, 1/6]) → 1 |
| vdr_product | list(fraction) → fraction | Product of list | vdr_product([1/2, 2/3, 3/4]) → 1/4 |
| vdr_mean | list(fraction) → fraction | Arithmetic mean | vdr_mean([1/3, 2/3]) → 1/2 |
| vdr_factorial | number → number | Factorial | vdr_factorial(5) → 120 |
| vdr_binomial | number, number → number | Binomial coefficient | vdr_binomial(10, 3) → 120 |
| vdr_fibonacci | number → number | Nth Fibonacci number | vdr_fibonacci(10) → 55 |

**Why these matter:** Arithmetic is the original motivation for VDR. Every arithmetic operation an LLM does by token prediction is unreliable. As primitives, they are exact.

### Category 4: Set Operations

Operations on sets represented as deduplicated sorted lists.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| set_from_list | list → set | Deduplicate and sort | set_from_list([3,1,2,1]) → {1,2,3} |
| set_to_list | set → list | Convert to sorted list | set_to_list({1,2,3}) → [1,2,3] |
| set_union | set, set → set | Union | set_union({1,2}, {2,3}) → {1,2,3} |
| set_intersection | set, set → set | Intersection | set_intersection({1,2,3}, {2,3,4}) → {2,3} |
| set_difference | set, set → set | Difference | set_difference({1,2,3}, {2}) → {1,3} |
| set_symmetric_diff | set, set → set | Symmetric difference | set_symmetric_diff({1,2,3}, {2,3,4}) → {1,4} |
| set_is_subset | set, set → bool | Subset test | set_is_subset({1,2}, {1,2,3}) → true |
| set_is_superset | set, set → bool | Superset test | set_is_superset({1,2,3}, {1,2}) → true |
| set_is_disjoint | set, set → bool | No common elements | set_is_disjoint({1,2}, {3,4}) → true |
| set_size | set → number | Cardinality | set_size({1,2,3}) → 3 |
| set_contains | set, term → bool | Membership | set_contains({1,2,3}, 2) → true |
| set_add | set, term → set | Add element | set_add({1,2}, 3) → {1,2,3} |
| set_remove | set, term → set | Remove element | set_remove({1,2,3}, 2) → {1,3} |
| set_power | set → set(set) | Power set | set_power({1,2}) → {{},{1},{2},{1,2}} |

**Why these matter:** Constraint set operations in VDR-Prolog depend on exact set algebra. LLMs frequently make errors with set operations (missing elements in unions, wrong intersection results). As primitives, these are exact by construction.

### Category 5: Dictionary / Map Operations

Operations on key-value stores. Keys are atoms or numbers. Values are any term.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| dict_new | → dict | Empty dictionary | dict_new() → {} |
| dict_from_pairs | list(pair) → dict | Construct from pairs | dict_from_pairs([("a",1),("b",2)]) → {"a":1,"b":2} |
| dict_get | dict, key → term | Lookup (fail if missing) | dict_get({"a":1}, "a") → 1 |
| dict_get_or | dict, key, default → term | Lookup with default | dict_get_or({"a":1}, "b", 0) → 0 |
| dict_set | dict, key, value → dict | Insert or update | dict_set({"a":1}, "b", 2) → {"a":1,"b":2} |
| dict_remove | dict, key → dict | Remove key | dict_remove({"a":1,"b":2}, "a") → {"b":2} |
| dict_contains_key | dict, key → bool | Key exists | dict_contains_key({"a":1}, "a") → true |
| dict_keys | dict → list | All keys | dict_keys({"a":1,"b":2}) → ["a","b"] |
| dict_values | dict → list | All values | dict_values({"a":1,"b":2}) → [1,2] |
| dict_pairs | dict → list(pair) | Key-value pairs | dict_pairs({"a":1,"b":2}) → [("a",1),("b",2)] |
| dict_size | dict → number | Entry count | dict_size({"a":1,"b":2}) → 2 |
| dict_merge | dict, dict → dict | Merge (right wins) | dict_merge({"a":1}, {"a":2,"b":3}) → {"a":2,"b":3} |
| dict_filter_keys | dict, predicate → dict | Keep matching keys | dict_filter_keys(d, starts_with("x")) → filtered |
| dict_map_values | dict, fn → dict | Transform values | dict_map_values({"a":1,"b":2}, double) → {"a":2,"b":4} |
| dict_invert | dict → dict | Swap keys and values | dict_invert({"a":1,"b":2}) → {1:"a",2:"b"} |

**Why these matter:** Working data sets in VDR-Prolog are dictionaries. The LLM's ability to manage scoped bindings depends on reliable dictionary operations. These are also essential for any structured data manipulation.

### Category 6: Linear Algebra Primitives

VDR's exact linear algebra exposed as Prolog predicates.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| vec_add | frac_vec, frac_vec → frac_vec | Vector addition | vec_add([1/2,1/3],[1/2,2/3]) → [1,1] |
| vec_sub | frac_vec, frac_vec → frac_vec | Vector subtraction | vec_sub([1,1],[1/2,1/3]) → [1/2,2/3] |
| vec_scale | fraction, frac_vec → frac_vec | Scalar multiply | vec_scale(2, [1/3,1/4]) → [2/3,1/2] |
| vec_dot | frac_vec, frac_vec → fraction | Dot product | vec_dot([1,2],[3,4]) → 11 |
| vec_norm_sq | frac_vec → fraction | Squared norm | vec_norm_sq([3,4]) → 25 |
| mat_add | frac_mat, frac_mat → frac_mat | Matrix addition | exact element-wise |
| mat_mul | frac_mat, frac_mat → frac_mat | Matrix multiply | exact matmul |
| mat_scale | fraction, frac_mat → frac_mat | Scalar multiply | exact scale |
| mat_transpose | frac_mat → frac_mat | Transpose | exact transpose |
| mat_det | frac_mat → fraction | Determinant | exact determinant |
| mat_inv | frac_mat → frac_mat | Inverse | exact inverse |
| mat_solve | frac_mat, frac_vec → frac_vec | Solve Ax=b | exact Cramer |
| mat_rank | frac_mat → number | Rank | exact Gaussian |
| mat_identity | number → frac_mat | Identity matrix | mat_identity(3) → I₃ |
| mat_trace | frac_mat → fraction | Trace | exact sum of diagonal |
| mat_matvec | frac_mat, frac_vec → frac_vec | Matrix-vector product | exact matvec |

**Why these matter:** The VDR-LLM transformer forward pass is a sequence of these operations. Having them as inspectable Prolog predicates means every matrix multiply can be traced in the provenance graph.

### Category 7: Statistical and Probability Primitives

Exact rational statistics.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| stat_mean | list(fraction) → fraction | Arithmetic mean | stat_mean([1/3,2/3,1]) → 2/3 |
| stat_variance | list(fraction) → fraction | Population variance | exact rational |
| stat_median | list(fraction) → fraction | Median | stat_median([1,3,2]) → 2 |
| stat_mode | list → term | Most frequent | stat_mode([1,1,2,3]) → 1 |
| stat_percentile | list(fraction), fraction → fraction | Nth percentile | exact interpolation |
| prob_normalize | list(fraction) → list(fraction) | Normalize to sum 1 | prob_normalize([1,2,3]) → [1/6,1/3,1/2] |
| prob_is_valid | list(fraction) → bool | All ≥0, sum=1 | exact check |
| prob_entropy_terms | list(fraction) → list(fraction) | -p·log(p) terms | exact per term |
| prob_cdf | list(fraction) → list(fraction) | Cumulative distribution | prob_cdf([1/4,1/2,1/4]) → [1/4,3/4,1] |
| prob_expected | list(fraction), list(fraction) → fraction | E[X] = Σ xᵢpᵢ | exact dot product |
| prob_bayes | fraction, fraction, fraction → fraction | Bayes' theorem | exact P(A|B) |
| prob_joint | list(fraction), list(fraction) → frac_mat | Joint probability table | outer product if independent |
| prob_marginal | frac_mat, atom → list(fraction) | Marginalize over axis | row or column sum |
| prob_conditional | frac_mat, number → list(fraction) | Conditional distribution | row normalized |
| softmax | list(fraction), number → list(fraction) | Exact VDR softmax | sum exactly 1 |
| softmax_surrogate | list(fraction), number → list(fraction) | Rational surrogate | sum exactly 1 |

**Why these matter:** The LLM's output is a probability distribution. Every operation on that distribution should be exact. Bayesian updates, expected values, normalization — all done by exact primitives rather than token-predicted arithmetic.

### Category 8: Conversion and Formatting

Type conversion and output formatting primitives.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| to_string | term → atom | Any term to display string | to_string(fraction(3,7)) → "3/7" |
| to_number | atom → number | Parse integer from string | to_number("42") → 42 |
| to_fraction | atom → fraction | Parse fraction from string | to_fraction("3/7") → 3/7 |
| fraction_to_decimal | fraction, number → atom | Decimal with N digits | fraction_to_decimal(1/3, 5) → "0.33333" |
| format_table | list(list(atom)) → atom | Format as aligned text table | rows → formatted string |
| format_json | dict → atom | Serialize to JSON string | exact serialization |
| parse_json | atom → dict | Parse JSON to dict | exact parsing |
| format_csv | list(list(atom)), atom → atom | Format as CSV | rows + delimiter → string |
| parse_csv | atom, atom → list(list(atom)) | Parse CSV to rows | string + delimiter → rows |
| number_to_roman | number → atom | Roman numeral | number_to_roman(42) → "XLII" |
| number_to_words | number → atom | English words | number_to_words(42) → "forty-two" |
| format_fraction | fraction → atom | Display fraction | format_fraction(22/7) → "22/7" |
| format_percentage | fraction, number → atom | Percentage with N decimals | format_percentage(1/3, 2) → "33.33%" |
| format_scientific | fraction, number → atom | Scientific notation | format_scientific(1/30000, 3) → "3.333e-5" |

**Why these matter:** LLMs frequently make formatting errors — wrong decimal places, incorrect rounding, mangled tables. As primitives, formatting is deterministic and correct.

### Category 9: Date and Time

Rational date arithmetic. Dates as integer day counts from epoch. Times as fractions of a day.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| date_from_ymd | number, number, number → number | Year/month/day to day count | date_from_ymd(2026,5,16) → day_number |
| date_to_ymd | number → (number, number, number) | Day count to Y/M/D | inverse |
| date_diff_days | number, number → number | Days between dates | exact integer |
| date_add_days | number, number → number | Add days to date | exact integer |
| date_day_of_week | number → atom | Day name | date_day_of_week(d) → "Saturday" |
| date_is_leap_year | number → bool | Leap year test | date_is_leap_year(2024) → true |
| date_days_in_month | number, number → number | Days in month/year | date_days_in_month(2, 2024) → 29 |
| time_from_hms | number, number, fraction → fraction | Hours/min/sec to day fraction | exact rational |
| time_to_hms | fraction → (number, number, fraction) | Day fraction to H/M/S | exact rational |
| duration_between | fraction, fraction → fraction | Time difference | exact subtraction |

**Why these matter:** Date arithmetic is a notorious source of errors for LLMs (wrong month lengths, leap year mistakes, off-by-one on day counts). As primitives, these use the exact calendar algorithms that have been correct since the Gregorian reform.

### Category 10: Hashing and Encoding

Deterministic byte-level operations. No cryptographic security claims — these are for checksums, identifiers, and deterministic encoding.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| hash_string | atom → number | Deterministic string hash | reproducible integer |
| hash_combine | number, number → number | Combine two hashes | deterministic |
| base64_encode | atom → atom | Base64 encoding | exact |
| base64_decode | atom → atom | Base64 decoding | exact inverse |
| hex_encode | number → atom | Integer to hex string | hex_encode(255) → "ff" |
| hex_decode | atom → number | Hex string to integer | hex_decode("ff") → 255 |
| crc32 | atom → number | CRC32 checksum | deterministic integer |
| uuid_from_seed | number → atom | Deterministic UUID | reproducible from seed |

**Why these matter:** Identifier generation, data integrity checking, and encoding conversions should be deterministic and exact. An LLM generating a base64 encoding by token prediction will make errors. A primitive will not.

### Category 11: Graph Operations

Operations on graphs represented as adjacency structures in the KB.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| graph_from_edges | list(pair) → graph | Construct graph | exact adjacency |
| graph_neighbors | graph, node → list(node) | Adjacent nodes | exact lookup |
| graph_shortest_path | graph, node, node → list(node) | BFS shortest path | exact path |
| graph_shortest_path_weighted | graph, node, node → (list(node), fraction) | Dijkstra with exact weights | exact VDR weights |
| graph_connected_components | graph → list(list(node)) | All components | exact partition |
| graph_is_connected | graph → bool | Connectivity test | exact |
| graph_topological_sort | graph → list(node) | Topological ordering (DAG) | exact or fail if cyclic |
| graph_cycle_detect | graph → bool | Has cycle | exact |
| graph_bfs | graph, node → list(node) | Breadth-first traversal | exact ordering |
| graph_dfs | graph, node → list(node) | Depth-first traversal | exact ordering |
| graph_degree | graph, node → number | Node degree | exact count |
| graph_mst | graph → list(edge) | Minimum spanning tree | exact VDR weights |
| graph_pagerank | graph, fraction → list(fraction) | PageRank with exact damping | exact VDR fractions |

**Why these matter:** The KB hierarchy is a graph. Topic dependencies are a graph. Provenance chains are directed acyclic graphs. Graph operations on these structures must be exact, and the results must be traceable.

### Category 12: Regular Expression and Pattern Matching

Deterministic string pattern matching. Not LLM-style fuzzy matching — exact regex execution.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| regex_match | atom, atom → bool | Full string match | regex_match("abc123", "[a-z]+[0-9]+") → true |
| regex_search | atom, atom → list(atom) | Find all matches | regex_search("a1b2c3", "[0-9]") → ["1","2","3"] |
| regex_replace | atom, atom, atom → atom | Replace matches | regex_replace("a1b2", "[0-9]", "X") → "aXbX" |
| regex_split | atom, atom → list(atom) | Split by pattern | regex_split("a1b2c", "[0-9]") → ["a","b","c"] |
| regex_capture | atom, atom → list(atom) | Capture groups | regex_capture("2026-05-16", "([0-9]+)-([0-9]+)-([0-9]+)") → ["2026","05","16"] |
| glob_match | atom, atom → bool | Glob pattern match | glob_match("hello.py", "*.py") → true |
| wildcard_match | atom, atom → bool | Simple wildcard | wildcard_match("abc", "a?c") → true |

**Why these matter:** Data validation, input parsing, and pattern extraction are core to any data processing system. LLMs frequently generate incorrect regex or misapply pattern matching. As primitives, the regex engine is deterministic and tested.

### Category 13: Logic and Control Flow

Prolog-native control predicates.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| if_then_else | bool, fn, fn → term | Conditional evaluation | if_then_else(X > 0, pos, neg) |
| case | term, list(pair(pattern, fn)) → term | Pattern match dispatch | switch-like |
| for_each | list, fn → void | Apply fn to each element | side-effect iteration |
| repeat_n | number, fn → list | Apply fn N times, collect | repeat_n(3, fn) → [r1,r2,r3] |
| while | predicate, fn, state → state | Iterate while predicate holds | loop with accumulator |
| try_catch | fn, handler → term | Execute with error handler | error recovery |
| assert_that | bool, atom → void | Runtime assertion | assert_that(X > 0, "must be positive") |
| type_check | term, type → bool | Runtime type check | type_check(fraction(1,2), fraction) → true |
| is_bound | variable → bool | Variable bound test | Prolog-specific |
| findall | template, goal → list | Collect all solutions | standard Prolog |
| aggregate | goal, fn, init → term | Fold over solutions | custom aggregation |

### Category 14: KB and Constraint Operations

Operations on the knowledge base itself, exposed as primitives.

| Primitive | Signature | Description | Example |
|-----------|-----------|-------------|---------|
| kb_assert | fact → void | Add fact to active KB | kb_assert(age("bob", 32)) |
| kb_retract | fact → void | Remove fact from active KB | kb_retract(age("bob", 32)) |
| kb_query | predicate, args → list(result) | Query active scope | exact Prolog query |
| kb_query_in | kb_name, predicate, args → list(result) | Query specific KB | bypass scope |
| kb_query_across | predicate, args → list(kb_name, result) | Query all KBs | tagged results |
| kb_list_facts | kb_name → list(fact) | All facts in KB | complete dump |
| kb_list_rules | kb_name → list(rule) | All rules in KB | complete dump |
| kb_active_scope | → list(kb_name) | Currently in-scope KBs | scope chain |
| kb_switch_topic | topic_name → void | Change active topic | scope update |
| constraint_check | constraint_name → bool | Verify specific constraint | exact check |
| constraint_check_all | → list(violation) | Verify all active | full sweep |
| constraint_add | constraint → void | Add to active KB | assertion |
| constraint_remove | constraint_name → void | Remove from active KB | retraction |
| constraint_enable | constraint_name → void | Activate | status change |
| constraint_suspend | constraint_name → void | Suspend | status change |

---

## 4. How the LLM Uses Primitives

The LLM does not call primitives directly. It recognizes that a computation is needed, identifies the appropriate primitive, and delegates. The result comes from the primitive, not from token generation.

**Without primitives:**
```
User: "Sort these numbers: 47, 3, 91, 15, 28, 66, 42, 7, 83, 19"
LLM: [generates tokens that predict what a sorted list looks like]
Output: "3, 7, 15, 19, 28, 42, 47, 66, 83, 91"
(probably correct for 10 items, unreliable for 100)
```

**With primitives:**
```
User: "Sort these numbers: 47, 3, 91, 15, 28, 66, 42, 7, 83, 19"
LLM: [recognizes sorting intent, delegates to primitive]
Action: list_sort([47, 3, 91, 15, 28, 66, 42, 7, 83, 19], ascending)
Primitive returns: [3, 7, 15, 19, 28, 42, 47, 66, 83, 91]
Output: "3, 7, 15, 19, 28, 42, 47, 66, 83, 91"
(correct regardless of list size)
```

The LLM's value-add is intent recognition and result framing. The primitive's value-add is correct computation. Neither needs to do the other's job.

**With KB integration:**
```
User: "Sort the characters in story B by age"
LLM: [recognizes sorting intent + KB query]
Action: 
  1. kb_query_in(kb_characters_b, binding(Name, number(Age)), Results)
     → [("bob_age", 59), ("margaret_age", 45)]
  2. list_sort_by_key(Results, second, ascending)
     → [("margaret_age", 45), ("bob_age", 59)]
Output: "Margaret (45) then Bob (59)"
(correct by construction — data from KB, sorting by primitive)
```

---

## 5. The Primitive Constraint Invariants

Every primitive carries Prolog constraints that the system can verify:

```
constraint("list_sort_output_length", axiom, active,
    condition(forall(list_sort(In, _, Out), list_length(In) =:= list_length(Out))),
    on_violation("error")).

constraint("list_sort_output_sorted", axiom, active,
    condition(forall(list_sort(In, ascending, Out), is_sorted(Out, ascending))),
    on_violation("error")).

constraint("list_sort_output_permutation", axiom, active,
    condition(forall(list_sort(In, _, Out), is_permutation(In, Out))),
    on_violation("error")).

constraint("vdr_add_commutative", axiom, active,
    condition(forall(vdr_add(A, B, R1), vdr_add(B, A, R2), R1 =:= R2)),
    on_violation("error")).

constraint("prob_normalize_sums_to_one", axiom, active,
    condition(forall(prob_normalize(In, Out), vdr_sum(Out) =:= 1)),
    on_violation("error")).

constraint("softmax_sums_to_one", axiom, active,
    condition(forall(softmax(In, _, Out), vdr_sum(Out) =:= 1)),
    on_violation("error")).
```

The primitives are not just tested at development time. They carry their invariants as runtime constraints that the Prolog system can verify on every call. A list_sort that produces an output of different length than its input violates an axiom. The violation is detected immediately, exactly, and traced to the specific call.

---

## 6. What This Changes

Current LLMs are universal but unreliable. They can attempt any computation but guarantee none. The VDR-Prolog primitive system inverts this: it provides a growing set of operations that are guaranteed correct, and the LLM's role shifts from "compute everything by token prediction" to "orchestrate reliable primitives and explain their results."

This is not tool use in the current sense (calling external APIs with opaque implementations). The primitives are inside the system. They are Prolog predicates. Their results are KB facts. Their constraints are verifiable. Their provenance is tracked. They are first-class members of the exact arithmetic, logical provenance, constraint-verified knowledge system.

The LLM becomes the conductor. The primitives are the orchestra. Each instrument plays its part exactly. The conductor arranges them into something meaningful. Neither needs to do the other's job, and the result is better than either could produce alone.
