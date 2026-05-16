Let me think about this systematically. We need to slice the pie on what the system needs to do — comprehensively, top-down, no gaps, no overlaps. Every builtin has an IOSE declaration. Every category covers its entire domain.

The whole pie is: everything the LLM needs to do that it cannot do reliably by token prediction. We subdivide that into categories, then subdivide each category into specific operations.

Let me enumerate the categories first, then we'll verify they cover the whole space.

---

## Slicing the Pie: What Does the System Need to Do?

**The whole:** All operations the LLM might need, that must be exact.

**First cut — by what kind of thing is being operated on:**

1. Text (strings, characters)
2. Collections (lists, ordered sequences)
3. Numbers (exact arithmetic)
4. Sets (unordered unique collections)
5. Mappings (key-value associations)
6. Vectors and matrices (linear algebra)
7. Statistics and probability
8. Conversion and formatting (between representations)
9. Time (dates, durations, timestamps)
10. Identity (hashing, encoding, checksums)
11. Graphs (nodes, edges, paths)
12. Logic and control flow
13. Knowledge base operations
14. Data primitives (runtime state — VDR-8)
15. Path and mount operations (addressing — VDR-8)
16. Session management (snapshots, clones — VDR-8)
17. Filesystem (external — operational)
18. Code compilation (external — operational)
19. Script execution (external — operational)
20. Linting and analysis (external — operational)
21. Network (external — operational)
22. Process management (external — operational)

That's 16 pure categories and 6 operational categories. Let me verify completeness: is there anything the LLM needs to do exactly that doesn't fit in one of these?

- Pattern matching / regex — removed in VDR-6 addendum, covered by string ops
- Prolog itself — that's the engine, not a primitive category, the KB ops are the interface
- External data integration — covered by network + conversion + KB ops
- Inference orchestration — VDR-9 patterns, not primitives, uses existing categories

The pie is sliced. Now let me write the comprehensive Prolog specification.

```prolog
% ================================================================
% VDR-LLM-Prolog — Comprehensive Builtin Specification
% The Complete Primitive Set, Sliced from the Whole
%
% Method: Comprehensive (OSO C17, C16)
%   1. Define the whole: all operations the LLM needs
%   2. Slice into categories by operand type
%   3. Slice each category into specific operations
%   4. Every operation has an IOSE declaration
%   5. Verify: no gaps, no overlaps, parts sum to whole
%
% Categories:
%   Pure (16 categories, no side effects, no grants):
%     1. Text           2. Collections     3. Arithmetic
%     4. Sets           5. Mappings         6. Linear Algebra
%     7. Statistics     8. Conversion       9. Time
%    10. Identity      11. Graphs          12. Logic/Control
%    13. KB Operations  14. Data Primitives
%    15. Path/Mount     16. Session
%
%   Operational (6 categories, side effects, require grants):
%    17. Filesystem    18. Compilation     19. Execution
%    20. Linting       21. Network         22. Process
%
% Structure per primitive:
%   builtin(Id, Name, Category, Inputs, Outputs, SideEffects,
%           Properties, Description)
%
% Properties include:
%   pure, operational, idempotent, deterministic, bounded,
%   commutative, associative, invertible
% ================================================================


% ================================================================
% CATEGORY DECLARATIONS
% Each category owns a domain. No domain gaps. No overlaps.
% ================================================================

category(1, text, pure,
    "Operations on character sequences. Covers: construction,
     decomposition, search, transformation, comparison.
     Domain boundary: operates on atoms/strings only.
     Does not cover: pattern matching with backtracking (removed),
     parsing of structured formats (see conversion)").

category(2, collections, pure,
    "Operations on ordered sequences. Covers: construction,
     access, transformation, search, sorting, partitioning,
     aggregation. Domain boundary: operates on lists/arrays.
     Does not cover: unordered collections (see sets),
     key-value pairs (see mappings)").

category(3, arithmetic, pure,
    "Exact rational arithmetic. Covers: basic operations,
     comparison, rounding, number theory, combinatorics.
     Domain boundary: operates on VDR fractions and integers.
     Does not cover: vector/matrix operations (see linalg),
     statistical aggregates (see statistics)").

category(4, sets, pure,
    "Operations on unordered unique collections. Covers:
     construction, membership, algebra (union/intersection/
     difference), comparison. Domain boundary: set semantics
     (no duplicates, no order). Does not cover: ordered
     sequences (see collections), key-value (see mappings)").

category(5, mappings, pure,
    "Operations on key-value associations. Covers: construction,
     lookup, mutation, iteration, merging. Domain boundary:
     unique keys mapping to values. Does not cover: ordered
     sequences (see collections), working data bindings
     (see KB operations for scoped bindings)").

category(6, linalg, pure,
    "Exact rational linear algebra. Covers: vector operations,
     matrix operations, solving, decomposition. Domain boundary:
     fraction vectors and fraction matrices. Does not cover:
     scalar arithmetic (see arithmetic), statistical operations
     on vectors (see statistics)").

category(7, statistics, pure,
    "Statistical and probabilistic operations on exact fractions.
     Covers: descriptive statistics, probability distributions,
     normalization, Bayesian operations, softmax. Domain boundary:
     aggregate measures over collections of fractions. Does not
     cover: individual arithmetic (see arithmetic), time series
     analysis (compose from statistics + collections)").

category(8, conversion, pure,
    "Conversion between representations. Covers: type conversion,
     formatting for display, parsing structured formats (JSON,
     CSV), number representation. Domain boundary: transforms
     between equivalent representations. Does not cover:
     computation (see arithmetic), text manipulation
     (see text for string ops)").

category(9, time, pure,
    "Date and time operations. Covers: date construction,
     calendar arithmetic, day-of-week, leap year, duration.
     Domain boundary: Gregorian calendar and fractional day
     time. Does not cover: timestamps as integers (see
     arithmetic), time zones (future extension)").

category(10, identity, pure,
    "Hashing, encoding, and identity operations. Covers:
     deterministic hashing, base64, hex, CRC32, UUID generation
     from seed. Domain boundary: identity and integrity
     operations. Does not cover: cryptographic security
     (not specified), encryption (not specified)").

category(11, graphs, pure,
    "Graph algorithms. Covers: construction, traversal, shortest
     path, connectivity, topological sort, cycle detection,
     spanning tree, PageRank. Domain boundary: node-edge
     structures. Does not cover: tree-specific operations
     (KB tree uses path operations)").

category(12, logic, pure,
    "Control flow and logic operations. Covers: conditional
     evaluation, pattern dispatch, iteration, error handling,
     type checking, Prolog solution collection. Domain boundary:
     flow control and meta-operations. Does not cover: KB
     operations (see KB), data primitive operations (see
     data primitives)").

category(13, kb_ops, pure,
    "Knowledge base operations. Covers: fact assertion,
     retraction, query (scoped, cross-scope, specific KB),
     listing, topic switching, constraint operations. Domain
     boundary: the Prolog KB engine interface. Does not cover:
     data primitives in KBs (see data primitives), path
     addressing (see path operations)").

category(14, data_primitives, pure,
    "Runtime state data structures in the KB struct. Covers:
     LRU caches, counters, locks, queues, stacks, ring buffers,
     bitsets. Domain boundary: bounded, named, scoped working
     memory. Does not cover: persistent facts (see KB ops),
     session-level snapshots (see session)").

category(15, path_mount, pure,
    "Universal addressing and mounting. Covers: path resolution,
     path navigation, mount creation and management, connection
     operations. Domain boundary: the dotted-path namespace and
     cross-branch references. Does not cover: KB content
     operations (see KB ops)").

category(16, session, pure,
    "Session state management. Covers: snapshot, restore, reset,
     clone, kill, diff, info. Domain boundary: session-level
     live state capture and lifecycle. Does not cover: individual
     data primitive operations (see data primitives), persistent
     KB operations (see KB ops)").

category(17, filesystem, operational,
    "File and directory operations. Covers: read, write, append,
     existence check, listing, creation, deletion, move, copy,
     size, modification time, glob, tree, diff, checksum.
     Domain boundary: file system interaction within granted
     paths. Requires: filesystem grant").

category(18, compilation, operational,
    "Code compilation. Covers: Python syntax check, Zig
     compilation, C compilation, Rust compilation. Domain
     boundary: source code to binary/bytecode transformation.
     Requires: compile grant").

category(19, execution, operational,
    "Script and command execution. Covers: Python, shell,
     Zig test, pytest, arbitrary script with interpreter.
     Domain boundary: running code in sandboxed environments.
     Requires: execute grant").

category(20, linting, operational,
    "Code analysis without execution. Covers: Python lint,
     Zig lint, JSON validation, Markdown check, import analysis,
     complexity metrics, dependency graph, line counts. Domain
     boundary: static analysis. Requires: lint grant (read)").

category(21, network, operational,
    "Network operations. Covers: download, fetch (GET), POST,
     ping, DNS resolve. Domain boundary: HTTP and network
     protocol interaction. Requires: network grant").

category(22, process, operational,
    "Process lifecycle management. Covers: start, poll, wait,
     kill, stdout read, stderr read, list. Domain boundary:
     background process supervision. Requires: process grant").


% ================================================================
% VERIFICATION: CATEGORIES COVER THE WHOLE
% ================================================================

% The whole pie: everything the LLM needs to do exactly
fact(whole_pie, "All operations the LLM might need that must
     be exact, deterministic, or externally executed rather
     than predicted by token generation").

% Verify no gaps: every operation type maps to exactly one category
rule(no_gaps :-
    forall(operation_type(OpType),
        (category_covers(Cat, OpType),
         note("Every operation type has a home")))).

% Verify no overlaps: no operation type in two categories
rule(no_overlaps :-
    forall(operation_type(OpType),
        (findall(C, category_covers(C, OpType), Cats),
         length(Cats, 1),
         note("Every operation type has exactly one home")))).

% The pure/operational boundary
rule(pure_operational_boundary(Category, pure) :-
    category(_, Category, pure, _)).
rule(pure_operational_boundary(Category, operational) :-
    category(_, Category, operational, _)).


% ================================================================
% BUILTIN SPECIFICATION FORMAT
%
% builtin(Id, Name, Category, IOSE, Properties, Description)
%
% IOSE = iose(Inputs, Outputs, SideEffects)
% Properties = list of atoms from:
%   [pure, operational, idempotent, deterministic, bounded,
%    commutative, associative, invertible, partial]
%
% partial = may fail on some inputs (e.g., dict_get on missing key)
% bounded = guaranteed to terminate in bounded time relative
%           to input size
% ================================================================


% ================================================================
% CATEGORY 1: TEXT (17 primitives)
% Slicing: construction | decomposition | search | transform |
%          comparison
% Every string operation an LLM might need, that token prediction
% gets wrong. No pattern-matching with backtracking.
% ================================================================

% --- construction ---
builtin(1, string_concat, text,
    iose([atom, atom], [atom], []),
    [pure, deterministic, bounded, associative],
    "Concatenate two strings").

builtin(2, string_join, text,
    iose([list(atom), atom], [atom], []),
    [pure, deterministic, bounded],
    "Join list of strings with delimiter").

builtin(3, string_pad_left, text,
    iose([atom, number, atom], [atom], []),
    [pure, deterministic, bounded],
    "Left-pad string to target width with fill character").

builtin(4, chars_to_string, text,
    iose([list(atom)], [atom], []),
    [pure, deterministic, bounded, invertible],
    "Construct string from character list").

% --- decomposition ---
builtin(5, string_split, text,
    iose([atom, atom], [list(atom)], []),
    [pure, deterministic, bounded],
    "Split string by delimiter into list").

builtin(6, string_slice, text,
    iose([atom, number, number], [atom], []),
    [pure, deterministic, bounded],
    "Extract substring by start and end index").

builtin(7, string_char_at, text,
    iose([atom, number], [atom], []),
    [pure, deterministic, bounded, partial],
    "Character at index. Fails if index out of range").

builtin(8, string_to_chars, text,
    iose([atom], [list(atom)], []),
    [pure, deterministic, bounded, invertible],
    "Decompose string to character list").

builtin(9, string_length, text,
    iose([atom], [number], []),
    [pure, deterministic, bounded],
    "Count characters in string").

% --- search ---
builtin(10, string_contains, text,
    iose([atom, atom], [bool], []),
    [pure, deterministic, bounded],
    "Test if string contains substring. O(n*m)").

builtin(11, string_starts_with, text,
    iose([atom, atom], [bool], []),
    [pure, deterministic, bounded],
    "Test if string starts with prefix").

builtin(12, string_ends_with, text,
    iose([atom, atom], [bool], []),
    [pure, deterministic, bounded],
    "Test if string ends with suffix").

% --- transformation ---
builtin(13, string_reverse, text,
    iose([atom], [atom], []),
    [pure, deterministic, bounded, invertible],
    "Reverse character order").

builtin(14, string_upper, text,
    iose([atom], [atom], []),
    [pure, deterministic, bounded],
    "Convert all characters to uppercase").

builtin(15, string_lower, text,
    iose([atom], [atom], []),
    [pure, deterministic, bounded],
    "Convert all characters to lowercase").

builtin(16, string_trim, text,
    iose([atom], [atom], []),
    [pure, deterministic, bounded, idempotent],
    "Remove leading and trailing whitespace").

builtin(17, string_replace, text,
    iose([atom, atom, atom], [atom], []),
    [pure, deterministic, bounded],
    "Replace all occurrences of pattern with replacement").


% ================================================================
% CATEGORY 2: COLLECTIONS (36 primitives)
% Slicing: construction | access | transformation | search |
%          sorting | partitioning | aggregation | combination
% The critical category. Sorting alone justifies the system.
% ================================================================

% --- construction ---
builtin(18, list_append, collections,
    iose([list, term], [list], []),
    [pure, deterministic, bounded],
    "Add element to end of list").

builtin(19, list_prepend, collections,
    iose([term, list], [list], []),
    [pure, deterministic, bounded],
    "Add element to front of list").

builtin(20, list_concat, collections,
    iose([list, list], [list], []),
    [pure, deterministic, bounded, associative],
    "Concatenate two lists").

% --- access ---
builtin(21, list_length, collections,
    iose([list], [number], []),
    [pure, deterministic, bounded],
    "Count elements").

builtin(22, list_head, collections,
    iose([list], [term], []),
    [pure, deterministic, bounded, partial],
    "First element. Fails on empty list").

builtin(23, list_tail, collections,
    iose([list], [list], []),
    [pure, deterministic, bounded, partial],
    "All elements except first. Fails on empty list").

builtin(24, list_last, collections,
    iose([list], [term], []),
    [pure, deterministic, bounded, partial],
    "Last element. Fails on empty list").

builtin(25, list_init, collections,
    iose([list], [list], []),
    [pure, deterministic, bounded, partial],
    "All elements except last. Fails on empty list").

builtin(26, list_nth, collections,
    iose([list, number], [term], []),
    [pure, deterministic, bounded, partial],
    "Element at index. Fails if index out of range").

builtin(27, list_take, collections,
    iose([list, number], [list], []),
    [pure, deterministic, bounded],
    "First N elements").

builtin(28, list_drop, collections,
    iose([list, number], [list], []),
    [pure, deterministic, bounded],
    "All elements after first N").

builtin(29, list_slice, collections,
    iose([list, number, number], [list], []),
    [pure, deterministic, bounded],
    "Sublist by start and end index").

% --- transformation ---
builtin(30, list_reverse, collections,
    iose([list], [list], []),
    [pure, deterministic, bounded, invertible],
    "Reverse element order").

builtin(31, list_map, collections,
    iose([list, fn], [list], []),
    [pure, deterministic, bounded],
    "Apply function to each element, collect results").

builtin(32, list_flatten, collections,
    iose([list(list)], [list], []),
    [pure, deterministic, bounded],
    "One-level flatten of nested lists").

builtin(33, list_unique, collections,
    iose([list], [list], []),
    [pure, deterministic, bounded, idempotent],
    "Remove duplicates preserving first occurrence order").

builtin(34, list_enumerate, collections,
    iose([list], [list(pair)], []),
    [pure, deterministic, bounded],
    "Pair each element with its index").

builtin(35, list_chunk, collections,
    iose([list, number], [list(list)], []),
    [pure, deterministic, bounded],
    "Split into fixed-size chunks").

builtin(36, list_interleave, collections,
    iose([list, list], [list], []),
    [pure, deterministic, bounded],
    "Alternating merge of two lists").

% --- search ---
builtin(37, list_contains, collections,
    iose([list, term], [bool], []),
    [pure, deterministic, bounded],
    "Membership test").

builtin(38, list_index_of, collections,
    iose([list, term], [number], []),
    [pure, deterministic, bounded, partial],
    "Index of first occurrence. Fails if not found").

builtin(39, list_filter, collections,
    iose([list, predicate], [list], []),
    [pure, deterministic, bounded],
    "Keep elements matching predicate").

builtin(40, list_any, collections,
    iose([list, predicate], [bool], []),
    [pure, deterministic, bounded],
    "True if any element matches predicate").

builtin(41, list_all, collections,
    iose([list, predicate], [bool], []),
    [pure, deterministic, bounded],
    "True if all elements match predicate").

builtin(42, list_count, collections,
    iose([list, predicate], [number], []),
    [pure, deterministic, bounded],
    "Count elements matching predicate").

% --- sorting ---
builtin(43, list_sort, collections,
    iose([list, rule], [list], []),
    [pure, deterministic, bounded, idempotent],
    "Sort by declared comparison rule. O(n log n).
     Output is permutation of input with same length").

builtin(44, list_sort_reverse, collections,
    iose([list, rule], [list], []),
    [pure, deterministic, bounded, idempotent],
    "Sort descending by declared comparison rule").

builtin(45, list_sort_by_key, collections,
    iose([list(term), key_fn], [list(term)], []),
    [pure, deterministic, bounded, idempotent],
    "Sort by extracted key value").

builtin(46, list_min, collections,
    iose([list], [term], []),
    [pure, deterministic, bounded, partial],
    "Minimum element. Fails on empty list").

builtin(47, list_max, collections,
    iose([list], [term], []),
    [pure, deterministic, bounded, partial],
    "Maximum element. Fails on empty list").

% --- partitioning ---
builtin(48, list_partition, collections,
    iose([list, predicate], [list, list], []),
    [pure, deterministic, bounded],
    "Split into pass and fail lists by predicate").

builtin(49, list_group_by, collections,
    iose([list(term), key_fn], [dict], []),
    [pure, deterministic, bounded],
    "Group elements by extracted key into dictionary").

builtin(50, list_frequencies, collections,
    iose([list], [dict], []),
    [pure, deterministic, bounded],
    "Count occurrences of each distinct element").

% --- aggregation ---
builtin(51, list_reduce, collections,
    iose([list, fn, init], [term], []),
    [pure, deterministic, bounded],
    "Left fold with accumulator and initial value").

% --- combination ---
builtin(52, list_zip, collections,
    iose([list, list], [list(pair)], []),
    [pure, deterministic, bounded],
    "Pair-wise zip. Length is min of inputs").

builtin(53, list_unzip, collections,
    iose([list(pair)], [list, list], []),
    [pure, deterministic, bounded, invertible],
    "Separate list of pairs into two lists").


% ================================================================
% CATEGORY 3: ARITHMETIC (26 primitives)
% Slicing: basic ops | comparison | rounding | extraction |
%          number theory | combinatorics | list aggregates
% Every value is an exact VDR fraction.
% ================================================================

% --- basic operations ---
builtin(54, vdr_add, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact rational addition").

builtin(55, vdr_sub, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded],
    "Exact rational subtraction").

builtin(56, vdr_mul, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact rational multiplication").

builtin(57, vdr_div, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact rational division. Fails on zero denominator").

builtin(58, vdr_neg, arithmetic,
    iose([fraction], [fraction], []),
    [pure, deterministic, bounded, invertible],
    "Exact negation").

builtin(59, vdr_abs, arithmetic,
    iose([fraction], [fraction], []),
    [pure, deterministic, bounded, idempotent],
    "Absolute value").

builtin(60, vdr_pow, arithmetic,
    iose([fraction, number], [fraction], []),
    [pure, deterministic, bounded],
    "Integer power of exact fraction").

% --- comparison ---
builtin(61, vdr_compare, arithmetic,
    iose([fraction, fraction], [atom], []),
    [pure, deterministic, bounded],
    "Return less, equal, or greater").

builtin(62, vdr_min, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded, commutative, associative, idempotent],
    "Minimum of two fractions").

builtin(63, vdr_max, arithmetic,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded, commutative, associative, idempotent],
    "Maximum of two fractions").

% --- rounding ---
builtin(64, vdr_floor, arithmetic,
    iose([fraction], [number], []),
    [pure, deterministic, bounded],
    "Floor to integer").

builtin(65, vdr_ceil, arithmetic,
    iose([fraction], [number], []),
    [pure, deterministic, bounded],
    "Ceiling to integer").

builtin(66, vdr_round, arithmetic,
    iose([fraction], [number], []),
    [pure, deterministic, bounded],
    "Round to nearest integer").

% --- extraction ---
builtin(67, vdr_numerator, arithmetic,
    iose([fraction], [number], []),
    [pure, deterministic, bounded],
    "Extract numerator").

builtin(68, vdr_denominator, arithmetic,
    iose([fraction], [number], []),
    [pure, deterministic, bounded],
    "Extract denominator").

builtin(69, vdr_is_integer, arithmetic,
    iose([fraction], [bool], []),
    [pure, deterministic, bounded],
    "True if denominator is 1").

builtin(70, vdr_simplify, arithmetic,
    iose([fraction], [fraction], []),
    [pure, deterministic, bounded, idempotent],
    "Reduce to lowest terms").

% --- number theory ---
builtin(71, vdr_gcd, arithmetic,
    iose([number, number], [number], []),
    [pure, deterministic, bounded, commutative, associative],
    "Greatest common divisor").

builtin(72, vdr_lcm, arithmetic,
    iose([number, number], [number], []),
    [pure, deterministic, bounded, commutative, associative],
    "Least common multiple").

builtin(73, vdr_mod, arithmetic,
    iose([number, number], [number], []),
    [pure, deterministic, bounded, partial],
    "Modular remainder. Fails on zero divisor").

% --- combinatorics ---
builtin(74, vdr_factorial, arithmetic,
    iose([number], [number], []),
    [pure, deterministic, bounded],
    "Factorial. Input must be non-negative integer").

builtin(75, vdr_binomial, arithmetic,
    iose([number, number], [number], []),
    [pure, deterministic, bounded],
    "Binomial coefficient C(n, k)").

builtin(76, vdr_fibonacci, arithmetic,
    iose([number], [number], []),
    [pure, deterministic, bounded],
    "Nth Fibonacci number").

% --- list aggregates (arithmetic domain, list input) ---
builtin(77, vdr_sum, arithmetic,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact sum of fraction list").

builtin(78, vdr_product, arithmetic,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact product of fraction list").

builtin(79, vdr_mean, arithmetic,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact arithmetic mean. Fails on empty list").


% ================================================================
% CATEGORY 4: SETS (14 primitives)
% Slicing: construction | membership | algebra | comparison
% Foundation for constraint sets, tag groups, permission sets.
% ================================================================

% --- construction ---
builtin(80, set_from_list, sets,
    iose([list], [set], []),
    [pure, deterministic, bounded, idempotent],
    "Deduplicate and sort list into set").

builtin(81, set_to_list, sets,
    iose([set], [list], []),
    [pure, deterministic, bounded],
    "Convert set to sorted list").

builtin(82, set_add, sets,
    iose([set, term], [set], []),
    [pure, deterministic, bounded, idempotent],
    "Add element to set. Idempotent if already present").

builtin(83, set_remove, sets,
    iose([set, term], [set], []),
    [pure, deterministic, bounded, idempotent],
    "Remove element from set. Idempotent if not present").

% --- membership ---
builtin(84, set_contains, sets,
    iose([set, term], [bool], []),
    [pure, deterministic, bounded],
    "Membership test").

builtin(85, set_size, sets,
    iose([set], [number], []),
    [pure, deterministic, bounded],
    "Cardinality").

% --- algebra ---
builtin(86, set_union, sets,
    iose([set, set], [set], []),
    [pure, deterministic, bounded, commutative, associative, idempotent],
    "Union of two sets").

builtin(87, set_intersection, sets,
    iose([set, set], [set], []),
    [pure, deterministic, bounded, commutative, associative, idempotent],
    "Intersection of two sets").

builtin(88, set_difference, sets,
    iose([set, set], [set], []),
    [pure, deterministic, bounded],
    "Elements in first set not in second").

builtin(89, set_symmetric_diff, sets,
    iose([set, set], [set], []),
    [pure, deterministic, bounded, commutative],
    "Elements in either set but not both").

builtin(90, set_power, sets,
    iose([set], [set(set)], []),
    [pure, deterministic, bounded],
    "Power set. Warning: 2^n growth").

% --- comparison ---
builtin(91, set_is_subset, sets,
    iose([set, set], [bool], []),
    [pure, deterministic, bounded],
    "True if first is subset of second").

builtin(92, set_is_superset, sets,
    iose([set, set], [bool], []),
    [pure, deterministic, bounded],
    "True if first is superset of second").

builtin(93, set_is_disjoint, sets,
    iose([set, set], [bool], []),
    [pure, deterministic, bounded],
    "True if no common elements").


% ================================================================
% CATEGORY 5: MAPPINGS (15 primitives)
% Slicing: construction | access | mutation | iteration |
%          combination
% Working data sets are dictionaries at the implementation level.
% ================================================================

% --- construction ---
builtin(94, dict_new, mappings,
    iose([], [dict], []),
    [pure, deterministic, bounded],
    "Create empty dictionary").

builtin(95, dict_from_pairs, mappings,
    iose([list(pair)], [dict], []),
    [pure, deterministic, bounded],
    "Construct from list of key-value pairs").

% --- access ---
builtin(96, dict_get, mappings,
    iose([dict, key], [term], []),
    [pure, deterministic, bounded, partial],
    "Lookup value by key. Fails if key missing").

builtin(97, dict_get_or, mappings,
    iose([dict, key, default], [term], []),
    [pure, deterministic, bounded],
    "Lookup value by key with default for missing").

builtin(98, dict_contains_key, mappings,
    iose([dict, key], [bool], []),
    [pure, deterministic, bounded],
    "Test if key exists").

builtin(99, dict_size, mappings,
    iose([dict], [number], []),
    [pure, deterministic, bounded],
    "Count of key-value entries").

% --- mutation (returns new dict, original unchanged) ---
builtin(100, dict_set, mappings,
    iose([dict, key, value], [dict], []),
    [pure, deterministic, bounded],
    "Insert or update entry. Returns new dict").

builtin(101, dict_remove, mappings,
    iose([dict, key], [dict], []),
    [pure, deterministic, bounded, idempotent],
    "Remove entry by key. Returns new dict").

builtin(102, dict_merge, mappings,
    iose([dict, dict], [dict], []),
    [pure, deterministic, bounded],
    "Merge two dicts. Second wins on key conflict").

% --- iteration ---
builtin(103, dict_keys, mappings,
    iose([dict], [list], []),
    [pure, deterministic, bounded],
    "All keys as sorted list").

builtin(104, dict_values, mappings,
    iose([dict], [list], []),
    [pure, deterministic, bounded],
    "All values as list").

builtin(105, dict_pairs, mappings,
    iose([dict], [list(pair)], []),
    [pure, deterministic, bounded],
    "All key-value pairs as list").

builtin(106, dict_filter_keys, mappings,
    iose([dict, predicate], [dict], []),
    [pure, deterministic, bounded],
    "Keep entries where key matches predicate").

builtin(107, dict_map_values, mappings,
    iose([dict, fn], [dict], []),
    [pure, deterministic, bounded],
    "Transform all values, preserving keys").

builtin(108, dict_invert, mappings,
    iose([dict], [dict], []),
    [pure, deterministic, bounded, partial],
    "Swap keys and values. Fails if values not unique").


% ================================================================
% CATEGORY 6: LINEAR ALGEBRA (16 primitives)
% Slicing: vector ops | matrix ops | solving | properties
% All operations on exact VDR fraction vectors and matrices.
% ================================================================

% --- vector operations ---
builtin(109, vec_add, linalg,
    iose([frac_vec, frac_vec], [frac_vec], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact vector addition").

builtin(110, vec_sub, linalg,
    iose([frac_vec, frac_vec], [frac_vec], []),
    [pure, deterministic, bounded],
    "Exact vector subtraction").

builtin(111, vec_scale, linalg,
    iose([fraction, frac_vec], [frac_vec], []),
    [pure, deterministic, bounded],
    "Exact scalar-vector multiplication").

builtin(112, vec_dot, linalg,
    iose([frac_vec, frac_vec], [fraction], []),
    [pure, deterministic, bounded, commutative],
    "Exact dot product").

builtin(113, vec_norm_sq, linalg,
    iose([frac_vec], [fraction], []),
    [pure, deterministic, bounded],
    "Exact squared L2 norm (avoids sqrt)").

% --- matrix operations ---
builtin(114, mat_add, linalg,
    iose([frac_mat, frac_mat], [frac_mat], []),
    [pure, deterministic, bounded, commutative, associative],
    "Exact matrix addition").

builtin(115, mat_mul, linalg,
    iose([frac_mat, frac_mat], [frac_mat], []),
    [pure, deterministic, bounded, associative],
    "Exact matrix multiplication. Not commutative").

builtin(116, mat_scale, linalg,
    iose([fraction, frac_mat], [frac_mat], []),
    [pure, deterministic, bounded],
    "Exact scalar-matrix multiplication").

builtin(117, mat_transpose, linalg,
    iose([frac_mat], [frac_mat], []),
    [pure, deterministic, bounded, invertible],
    "Matrix transpose. Self-inverse").

builtin(118, mat_matvec, linalg,
    iose([frac_mat, frac_vec], [frac_vec], []),
    [pure, deterministic, bounded],
    "Exact matrix-vector product").

% --- solving ---
builtin(119, mat_solve, linalg,
    iose([frac_mat, frac_vec], [frac_vec], []),
    [pure, deterministic, bounded, partial],
    "Exact solve Ax=b. Fails if singular").

builtin(120, mat_inv, linalg,
    iose([frac_mat], [frac_mat], []),
    [pure, deterministic, bounded, partial, invertible],
    "Exact matrix inverse. Fails if singular").

% --- properties ---
builtin(121, mat_det, linalg,
    iose([frac_mat], [fraction], []),
    [pure, deterministic, bounded],
    "Exact determinant").

builtin(122, mat_rank, linalg,
    iose([frac_mat], [number], []),
    [pure, deterministic, bounded],
    "Exact rank via row reduction").

builtin(123, mat_identity, linalg,
    iose([number], [frac_mat], []),
    [pure, deterministic, bounded],
    "Identity matrix of given size").

builtin(124, mat_trace, linalg,
    iose([frac_mat], [fraction], []),
    [pure, deterministic, bounded],
    "Exact trace (sum of diagonal)").


% ================================================================
% CATEGORY 7: STATISTICS AND PROBABILITY (16 primitives)
% Slicing: descriptive | probability | distribution | softmax
% All operations produce exact VDR fractions.
% ================================================================

% --- descriptive ---
builtin(125, stat_mean, statistics,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact arithmetic mean. Fails on empty list").

builtin(126, stat_variance, statistics,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact population variance. Fails on empty list").

builtin(127, stat_median, statistics,
    iose([list(fraction)], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact median. Fails on empty list").

builtin(128, stat_mode, statistics,
    iose([list], [term], []),
    [pure, deterministic, bounded, partial],
    "Most frequent element. Fails on empty list").

builtin(129, stat_percentile, statistics,
    iose([list(fraction), fraction], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Exact Nth percentile. N in [0,1]").

% --- probability ---
builtin(130, prob_normalize, statistics,
    iose([list(fraction)], [list(fraction)], []),
    [pure, deterministic, bounded, idempotent],
    "Normalize to exact sum 1. Idempotent on valid distributions").

builtin(131, prob_is_valid, statistics,
    iose([list(fraction)], [bool], []),
    [pure, deterministic, bounded],
    "True if all non-negative and sum exactly 1").

builtin(132, prob_entropy_terms, statistics,
    iose([list(fraction)], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Individual -p*log(p) terms as rational approximations").

builtin(133, prob_cdf, statistics,
    iose([list(fraction)], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Exact cumulative distribution function").

builtin(134, prob_expected, statistics,
    iose([list(fraction), list(fraction)], [fraction], []),
    [pure, deterministic, bounded],
    "Exact expected value: sum(p_i * x_i)").

builtin(135, prob_bayes, statistics,
    iose([fraction, fraction, fraction], [fraction], []),
    [pure, deterministic, bounded],
    "Exact Bayes theorem: P(A|B) from P(B|A), P(A), P(B)").

% --- distribution operations ---
builtin(136, prob_joint, statistics,
    iose([list(fraction), list(fraction)], [frac_mat], []),
    [pure, deterministic, bounded],
    "Joint probability table from independent marginals").

builtin(137, prob_marginal, statistics,
    iose([frac_mat, atom], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Marginalize joint table over specified axis").

builtin(138, prob_conditional, statistics,
    iose([frac_mat, number], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Conditional distribution from joint table given row/col").

% --- softmax ---
builtin(139, softmax, statistics,
    iose([list(fraction), number], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Exact VDR softmax via truncated Taylor exp at given depth.
     Output sums to exactly 1").

builtin(140, softmax_surrogate, statistics,
    iose([list(fraction), number], [list(fraction)], []),
    [pure, deterministic, bounded],
    "Rational surrogate softmax via square-shift kernel.
     Output sums to exactly 1. No transcendentals").


% ================================================================
% CATEGORY 8: CONVERSION AND FORMATTING (14 primitives)
% Slicing: type conversion | structured format | display format |
%          number representation
% ================================================================

% --- type conversion ---
builtin(141, to_string, conversion,
    iose([term], [atom], []),
    [pure, deterministic, bounded],
    "Any term to display string representation").

builtin(142, to_number, conversion,
    iose([atom], [number], []),
    [pure, deterministic, bounded, partial],
    "Parse integer from string. Fails on non-numeric").

builtin(143, to_fraction, conversion,
    iose([atom], [fraction], []),
    [pure, deterministic, bounded, partial],
    "Parse fraction from string (e.g. '3/7' or '0.5').
     Fails on unparseable. This is the conversion boundary
     where external approximate data enters the exact system").

% --- structured format ---
builtin(144, format_json, conversion,
    iose([dict], [atom], []),
    [pure, deterministic, bounded],
    "Serialize dictionary to JSON string").

builtin(145, parse_json, conversion,
    iose([atom], [dict], []),
    [pure, deterministic, bounded, partial],
    "Parse JSON string to dictionary. Fails on invalid JSON").

builtin(146, format_csv, conversion,
    iose([list(list(atom)), atom], [atom], []),
    [pure, deterministic, bounded],
    "Format rows as delimited text with given separator").

builtin(147, parse_csv, conversion,
    iose([atom, atom], [list(list(atom))], []),
    [pure, deterministic, bounded],
    "Parse delimited text to rows with given separator").

% --- display format ---
builtin(148, format_table, conversion,
    iose([list(list(atom))], [atom], []),
    [pure, deterministic, bounded],
    "Format as aligned text table with column padding").

builtin(149, format_fraction, conversion,
    iose([fraction], [atom], []),
    [pure, deterministic, bounded],
    "Display fraction as 'p/q' string").

builtin(150, format_percentage, conversion,
    iose([fraction, number], [atom], []),
    [pure, deterministic, bounded],
    "Display fraction as percentage with N decimal places").

builtin(151, format_scientific, conversion,
    iose([fraction, number], [atom], []),
    [pure, deterministic, bounded],
    "Display fraction in scientific notation with N digits").

builtin(152, fraction_to_decimal, conversion,
    iose([fraction, number], [atom], []),
    [pure, deterministic, bounded],
    "Display fraction as decimal string with N digits").

% --- number representation ---
builtin(153, number_to_roman, conversion,
    iose([number], [atom], []),
    [pure, deterministic, bounded, partial],
    "Roman numeral. Fails if out of range 1-3999").

builtin(154, number_to_words, conversion,
    iose([number], [atom], []),
    [pure, deterministic, bounded],
    "English word representation of integer").


% ================================================================
% CATEGORY 9: TIME (10 primitives)
% Slicing: construction | arithmetic | properties
% Gregorian calendar with exact integer day counts.
% ================================================================

% --- construction ---
builtin(155, date_from_ymd, time,
    iose([number, number, number], [number], []),
    [pure, deterministic, bounded],
    "Year, month, day to day count from epoch").

builtin(156, date_to_ymd, time,
    iose([number], [number, number, number], []),
    [pure, deterministic, bounded, invertible],
    "Day count to year, month, day").

builtin(157, time_from_hms, time,
    iose([number, number, fraction], [fraction], []),
    [pure, deterministic, bounded],
    "Hours, minutes, seconds to fractional day").

builtin(158, time_to_hms, time,
    iose([fraction], [number, number, fraction], []),
    [pure, deterministic, bounded, invertible],
    "Fractional day to hours, minutes, seconds").

% --- arithmetic ---
builtin(159, date_diff_days, time,
    iose([number, number], [number], []),
    [pure, deterministic, bounded],
    "Days between two date day-counts").

builtin(160, date_add_days, time,
    iose([number, number], [number], []),
    [pure, deterministic, bounded],
    "Add N days to a date day-count").

builtin(161, duration_between, time,
    iose([fraction, fraction], [fraction], []),
    [pure, deterministic, bounded],
    "Exact time difference between two fractional day values").

% --- properties ---
builtin(162, date_day_of_week, time,
    iose([number], [atom], []),
    [pure, deterministic, bounded],
    "Day name (monday..sunday) from date day-count").

builtin(163, date_is_leap_year, time,
    iose([number], [bool], []),
    [pure, deterministic, bounded],
    "Leap year test for given year").

builtin(164, date_days_in_month, time,
    iose([number, number], [number], []),
    [pure, deterministic, bounded],
    "Days in given month of given year").


% ================================================================
% CATEGORY 10: IDENTITY (8 primitives)
% Slicing: hashing | encoding | checksum | generation
% All deterministic. Same input, same output, any platform.
% ================================================================

% --- hashing ---
builtin(165, hash_string, identity,
    iose([atom], [number], []),
    [pure, deterministic, bounded],
    "Deterministic string hash to integer").

builtin(166, hash_combine, identity,
    iose([number, number], [number], []),
    [pure, deterministic, bounded],
    "Combine two hash values into one").

% --- encoding ---
builtin(167, base64_encode, identity,
    iose([atom], [atom], []),
    [pure, deterministic, bounded, invertible],
    "Base64 encoding").

builtin(168, base64_decode, identity,
    iose([atom], [atom], []),
    [pure, deterministic, bounded, invertible, partial],
    "Base64 decoding. Fails on invalid base64").

builtin(169, hex_encode, identity,
    iose([number], [atom], []),
    [pure, deterministic, bounded, invertible],
    "Integer to hexadecimal string").

builtin(170, hex_decode, identity,
    iose([atom], [number], []),
    [pure, deterministic, bounded, invertible, partial],
    "Hexadecimal string to integer. Fails on invalid hex").

% --- checksum ---
builtin(171, crc32, identity,
    iose([atom], [number], []),
    [pure, deterministic, bounded],
    "CRC32 checksum of string").

% --- generation ---
builtin(172, uuid_from_seed, identity,
    iose([number], [atom], []),
    [pure, deterministic, bounded],
    "Deterministic UUID v4 from integer seed.
     Same seed always produces same UUID").


% ================================================================
% CATEGORY 11: GRAPHS (13 primitives)
% Slicing: construction | traversal | path | structure |
%          weighted | ranking
% Node IDs are integers (from path registry or user-defined).
% ================================================================

% --- construction ---
builtin(173, graph_from_edges, graphs,
    iose([list(pair)], [graph], []),
    [pure, deterministic, bounded],
    "Construct adjacency structure from edge list").

% --- traversal ---
builtin(174, graph_neighbors, graphs,
    iose([graph, node], [list(node)], []),
    [pure, deterministic, bounded],
    "Adjacent nodes of given node").

builtin(175, graph_bfs, graphs,
    iose([graph, node], [list(node)], []),
    [pure, deterministic, bounded],
    "Breadth-first traversal order from start node").

builtin(176, graph_dfs, graphs,
    iose([graph, node], [list(node)], []),
    [pure, deterministic, bounded],
    "Depth-first traversal order from start node").

% --- path ---
builtin(177, graph_shortest_path, graphs,
    iose([graph, node, node], [list(node)], []),
    [pure, deterministic, bounded, partial],
    "BFS shortest path (unweighted). Fails if no path").

builtin(178, graph_shortest_path_weighted, graphs,
    iose([graph, node, node], [list(node), fraction], []),
    [pure, deterministic, bounded, partial],
    "Dijkstra with exact VDR weights. Fails if no path").

% --- structure ---
builtin(179, graph_connected_components, graphs,
    iose([graph], [list(list(node))], []),
    [pure, deterministic, bounded],
    "All connected components as lists of nodes").

builtin(180, graph_is_connected, graphs,
    iose([graph], [bool], []),
    [pure, deterministic, bounded],
    "True if graph has exactly one connected component").

builtin(181, graph_topological_sort, graphs,
    iose([graph], [list(node)], []),
    [pure, deterministic, bounded, partial],
    "Topological ordering for DAGs. Fails if cycle exists").

builtin(182, graph_cycle_detect, graphs,
    iose([graph], [bool], []),
    [pure, deterministic, bounded],
    "True if graph contains a cycle").

builtin(183, graph_degree, graphs,
    iose([graph, node], [number], []),
    [pure, deterministic, bounded],
    "Degree (edge count) of given node").

% --- weighted ---
builtin(184, graph_mst, graphs,
    iose([graph], [list(edge)], []),
    [pure, deterministic, bounded],
    "Minimum spanning tree with exact VDR weights").

% --- ranking ---
builtin(185, graph_pagerank, graphs,
    iose([graph, fraction], [list(fraction)], []),
    [pure, deterministic, bounded],
    "PageRank with exact rational damping factor.
     Returns exact VDR fraction scores per node").


% ================================================================
% CATEGORY 12: LOGIC AND CONTROL (11 primitives)
% Slicing: conditional | iteration | error handling |
%          type checking | prolog meta
% ================================================================

% --- conditional ---
builtin(186, if_then_else, logic,
    iose([bool, fn, fn], [term], []),
    [pure, deterministic, bounded],
    "Evaluate first fn if true, second if false").

builtin(187, case_match, logic,
    iose([term, list(pair(pattern, fn))], [term], []),
    [pure, deterministic, bounded, partial],
    "Pattern dispatch. Fails if no pattern matches").

% --- iteration ---
builtin(188, for_each, logic,
    iose([list, fn], [void], []),
    [pure, deterministic, bounded],
    "Apply function to each element for side effect").

builtin(189, repeat_n, logic,
    iose([number, fn], [list], []),
    [pure, deterministic, bounded],
    "Apply function N times, collect results").

builtin(190, while_loop, logic,
    iose([predicate, fn, state], [state], []),
    [pure, deterministic],
    "Iterate while predicate holds. Bounded by predicate
     convergence. Use with counter guard for safety").

% --- error handling ---
builtin(191, try_catch, logic,
    iose([fn, handler], [term], []),
    [pure, deterministic, bounded],
    "Execute fn. If it fails, execute handler instead").

builtin(192, assert_that, logic,
    iose([bool, atom], [void], []),
    [pure, deterministic, bounded, partial],
    "Runtime assertion. Fails with message if false").

% --- type checking ---
builtin(193, type_check, logic,
    iose([term, type], [bool], []),
    [pure, deterministic, bounded],
    "Test if term matches declared type").

builtin(194, is_bound, logic,
    iose([variable], [bool], []),
    [pure, deterministic, bounded],
    "Test if Prolog variable is bound to a value").

% --- prolog meta ---
builtin(195, findall, logic,
    iose([template, goal], [list], []),
    [pure, deterministic, bounded],
    "Collect all Prolog solutions matching goal").

builtin(196, aggregate, logic,
    iose([goal, fn, init], [term], []),
    [pure, deterministic, bounded],
    "Fold over all Prolog solutions with accumulator").


% ================================================================
% CATEGORY 13: KB OPERATIONS (15 primitives)
% Slicing: assertion | retraction | query | listing |
%          scoping | constraints
% The interface between the LLM and the Prolog engine.
% ================================================================

% --- assertion ---
builtin(197, kb_assert, kb_ops,
    iose([fact], [void], [kb_fact_added, mutation_logged]),
    [pure, deterministic, bounded],
    "Assert fact into active KB. Idempotent if fact exists").

% --- retraction ---
builtin(198, kb_retract, kb_ops,
    iose([fact], [void], [kb_fact_removed, mutation_logged]),
    [pure, deterministic, bounded],
    "Retract fact from active KB. Idempotent if fact absent").

% --- query ---
builtin(199, kb_query, kb_ops,
    iose([predicate, args], [list(result)], []),
    [pure, deterministic, bounded],
    "Query active scope. Returns all matching facts").

builtin(200, kb_query_in, kb_ops,
    iose([kb_path, predicate, args], [list(result)], []),
    [pure, deterministic, bounded],
    "Query specific KB by path, bypassing scope").

builtin(201, kb_query_across, kb_ops,
    iose([predicate, args], [list(kb_path, result)], []),
    [pure, deterministic, bounded],
    "Query all KBs. Results tagged with source KB path").

% --- listing ---
builtin(202, kb_list_facts, kb_ops,
    iose([kb_path], [list(fact)], []),
    [pure, deterministic, bounded],
    "All facts in named KB").

builtin(203, kb_list_rules, kb_ops,
    iose([kb_path], [list(rule)], []),
    [pure, deterministic, bounded],
    "All rules in named KB").

builtin(204, kb_active_scope, kb_ops,
    iose([], [list(kb_path)], []),
    [pure, deterministic, bounded],
    "List of currently in-scope KB paths").

% --- scoping ---
builtin(205, kb_switch_topic, kb_ops,
    iose([topic_name], [void], [scope_changed]),
    [pure, deterministic, bounded],
    "Change active topic and scope chain").

% --- constraints ---
builtin(206, constraint_check, kb_ops,
    iose([constraint_name], [bool], []),
    [pure, deterministic, bounded],
    "Verify specific constraint. Returns pass/fail").

builtin(207, constraint_check_all, kb_ops,
    iose([], [list(violation)], []),
    [pure, deterministic, bounded],
    "Verify all active constraints. Returns violations").

builtin(208, constraint_add, kb_ops,
    iose([constraint], [void], [constraint_added]),
    [pure, deterministic, bounded],
    "Add constraint to active KB").

builtin(209, constraint_remove, kb_ops,
    iose([constraint_name], [void], [constraint_removed]),
    [pure, deterministic, bounded],
    "Remove constraint from active KB").

builtin(210, constraint_enable, kb_ops,
    iose([constraint_name], [void], [constraint_activated]),
    [pure, deterministic, bounded, idempotent],
    "Activate a suspended constraint").

builtin(211, constraint_suspend, kb_ops,
    iose([constraint_name], [void], [constraint_suspended]),
    [pure, deterministic, bounded, idempotent],
    "Suspend an active constraint").


% ================================================================
% CATEGORY 14: DATA PRIMITIVES (53 primitives)
% Slicing: LRU (8) | counters (7) | locks (6) | queues (9) |
%          stacks (8) | ring buffers (6) | bitsets (9)
% All bounded. All named. All scoped to KB. All non-blocking.
% ================================================================

% --- LRU caches (8) ---
builtin(212, lru_create, data_primitives,
    iose([name, capacity], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named LRU cache on active KB").

builtin(213, lru_push, data_primitives,
    iose([name, key, value], [void], [lru_entry_added, oldest_evicted_if_full]),
    [pure, deterministic, bounded],
    "Insert or update entry. Evicts oldest if at capacity").

builtin(214, lru_get, data_primitives,
    iose([name, key], [term], [access_time_updated]),
    [pure, deterministic, bounded, partial],
    "Lookup by key. Updates access time. Fails if not found").

builtin(215, lru_peek, data_primitives,
    iose([name, count], [list(entry)], []),
    [pure, deterministic, bounded],
    "Most recent N entries without updating access times").

builtin(216, lru_contains, data_primitives,
    iose([name, key], [bool], []),
    [pure, deterministic, bounded],
    "Key membership test").

builtin(217, lru_size, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Current entry count").

builtin(218, lru_clear, data_primitives,
    iose([name], [void], [all_entries_removed]),
    [pure, deterministic, bounded, idempotent],
    "Remove all entries").

builtin(219, lru_evict, data_primitives,
    iose([name, key], [void], [entry_removed]),
    [pure, deterministic, bounded, idempotent],
    "Remove specific entry by key").

% --- counters (7) ---
builtin(220, counter_create, data_primitives,
    iose([name, min, max], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named counter with bounds on active KB").

builtin(221, counter_inc, data_primitives,
    iose([name], [number], [counter_mutated]),
    [pure, deterministic, bounded],
    "Increment by 1. Clamps at max. Returns new value").

builtin(222, counter_dec, data_primitives,
    iose([name], [number], [counter_mutated]),
    [pure, deterministic, bounded],
    "Decrement by 1. Clamps at min. Returns new value").

builtin(223, counter_add, data_primitives,
    iose([name, delta], [number], [counter_mutated]),
    [pure, deterministic, bounded],
    "Add delta (positive or negative). Clamps at bounds").

builtin(224, counter_get, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Read current value").

builtin(225, counter_reset, data_primitives,
    iose([name], [void], [counter_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Reset to min_value").

builtin(226, counter_set, data_primitives,
    iose([name, value], [void], [counter_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Set to specific value. Clamps at bounds").

% --- locks (6) ---
builtin(227, lock_create, data_primitives,
    iose([name], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named non-blocking lock on active KB").

builtin(228, lock_acquire, data_primitives,
    iose([name, holder, notes], [bool], [lock_state_changed]),
    [pure, deterministic, bounded],
    "Set lock flag. Returns true if was free, false if held.
     Never blocks").

builtin(229, lock_release, data_primitives,
    iose([name], [void], [lock_state_changed]),
    [pure, deterministic, bounded, idempotent],
    "Clear lock flag. Idempotent on free lock").

builtin(230, lock_check, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "Return true if lock is held").

builtin(231, lock_holder, data_primitives,
    iose([name], [text], []),
    [pure, deterministic, bounded, partial],
    "Return holder identifier. Fails if free").

builtin(232, lock_force_release, data_primitives,
    iose([name], [void], [lock_state_changed, force_release_logged]),
    [pure, deterministic, bounded, idempotent],
    "Release regardless of holder. Admin operation").

% --- queues (9) ---
builtin(233, queue_create, data_primitives,
    iose([name, capacity], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named bounded FIFO queue on active KB").

builtin(234, queue_push, data_primitives,
    iose([name, item], [bool], [queue_mutated]),
    [pure, deterministic, bounded],
    "Push to back. Returns false if full. Never blocks").

builtin(235, queue_pop, data_primitives,
    iose([name], [term], [queue_mutated]),
    [pure, deterministic, bounded, partial],
    "Remove and return front item. Fails if empty").

builtin(236, queue_peek, data_primitives,
    iose([name], [term], []),
    [pure, deterministic, bounded, partial],
    "Read front item without removing. Fails if empty").

builtin(237, queue_size, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Current item count").

builtin(238, queue_is_empty, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "True if queue has no items").

builtin(239, queue_is_full, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "True if queue is at capacity").

builtin(240, queue_clear, data_primitives,
    iose([name], [void], [queue_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Remove all items").

builtin(241, queue_to_list, data_primitives,
    iose([name], [list(term)], []),
    [pure, deterministic, bounded],
    "Read all items as list in FIFO order without removing").

% --- stacks (8) ---
builtin(242, stack_create, data_primitives,
    iose([name, capacity], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named bounded LIFO stack on active KB").

builtin(243, stack_push, data_primitives,
    iose([name, item], [bool], [stack_mutated]),
    [pure, deterministic, bounded],
    "Push to top. Returns false if full").

builtin(244, stack_pop, data_primitives,
    iose([name], [term], [stack_mutated]),
    [pure, deterministic, bounded, partial],
    "Remove and return top item. Fails if empty").

builtin(245, stack_peek, data_primitives,
    iose([name], [term], []),
    [pure, deterministic, bounded, partial],
    "Read top item without removing. Fails if empty").

builtin(246, stack_size, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Current item count").

builtin(247, stack_is_empty, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "True if stack has no items").

builtin(248, stack_clear, data_primitives,
    iose([name], [void], [stack_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Remove all items").

builtin(249, stack_to_list, data_primitives,
    iose([name], [list(term)], []),
    [pure, deterministic, bounded],
    "Read all items top-to-bottom without removing").

% --- ring buffers (6) ---
builtin(250, ring_create, data_primitives,
    iose([name, capacity], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named fixed-size circular buffer on active KB").

builtin(251, ring_write, data_primitives,
    iose([name, item], [void], [ring_mutated, oldest_overwritten_if_full]),
    [pure, deterministic, bounded],
    "Write item. Overwrites oldest if at capacity").

builtin(252, ring_read_all, data_primitives,
    iose([name], [list(term)], []),
    [pure, deterministic, bounded],
    "All items in chronological order").

builtin(253, ring_read_last, data_primitives,
    iose([name, count], [list(term)], []),
    [pure, deterministic, bounded],
    "Most recent N items").

builtin(254, ring_size, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Current item count (up to capacity)").

builtin(255, ring_clear, data_primitives,
    iose([name], [void], [ring_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Reset buffer to empty").

% --- bitsets (9) ---
builtin(256, bitset_create, data_primitives,
    iose([name, width], [void], [primitive_created]),
    [pure, deterministic, bounded],
    "Create named fixed-width bit array on active KB").

builtin(257, bitset_set, data_primitives,
    iose([name, index], [void], [bitset_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Set bit at index. Idempotent if already set").

builtin(258, bitset_clear_bit, data_primitives,
    iose([name, index], [void], [bitset_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Clear bit at index. Idempotent if already clear").

builtin(259, bitset_test, data_primitives,
    iose([name, index], [bool], []),
    [pure, deterministic, bounded],
    "Test bit at index").

builtin(260, bitset_count, data_primitives,
    iose([name], [number], []),
    [pure, deterministic, bounded],
    "Count of set bits").

builtin(261, bitset_all_set, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "True if all bits are set").

builtin(262, bitset_any_set, data_primitives,
    iose([name], [bool], []),
    [pure, deterministic, bounded],
    "True if any bit is set").

builtin(263, bitset_reset, data_primitives,
    iose([name], [void], [bitset_mutated]),
    [pure, deterministic, bounded, idempotent],
    "Clear all bits").

builtin(264, bitset_to_list, data_primitives,
    iose([name], [list(number)], []),
    [pure, deterministic, bounded],
    "Indices of all set bits as sorted list").


% ================================================================
% CATEGORY 15: PATH AND MOUNT (17 primitives)
% Slicing: resolution | navigation | mounting | connections
% ================================================================

% --- resolution ---
builtin(265, path_resolve, path_mount,
    iose([text], [number], []),
    [pure, deterministic, bounded, partial],
    "Dotted path to integer ID. Fails if path not registered").

builtin(266, path_from_id, path_mount,
    iose([number], [text], []),
    [pure, deterministic, bounded, partial],
    "Integer ID to dotted path. Fails if ID not registered").

builtin(267, path_exists, path_mount,
    iose([text], [bool], []),
    [pure, deterministic, bounded],
    "Test if dotted path is registered").

% --- navigation ---
builtin(268, path_parent, path_mount,
    iose([text], [text], []),
    [pure, deterministic, bounded, partial],
    "Parent path. Fails on root").

builtin(269, path_children, path_mount,
    iose([text], [list(text)], []),
    [pure, deterministic, bounded],
    "All child paths").

builtin(270, path_ancestors, path_mount,
    iose([text], [list(text)], []),
    [pure, deterministic, bounded],
    "All ancestor paths from parent to root").

builtin(271, path_depth, path_mount,
    iose([text], [number], []),
    [pure, deterministic, bounded],
    "Depth in tree. Root is 0").

builtin(272, path_common_ancestor, path_mount,
    iose([text, text], [text], []),
    [pure, deterministic, bounded],
    "Nearest common ancestor of two paths").

% --- mounting ---
builtin(273, kb_mount, path_mount,
    iose([mount_path, source_path, mode], [void],
         [mount_created, mount_cycle_checked]),
    [pure, deterministic, bounded, partial],
    "Mount source KB at mount path. Fails if cycle detected.
     Modes: read_only, read_write, snapshot, mirror").

builtin(274, kb_unmount, path_mount,
    iose([mount_path], [void], [mount_removed]),
    [pure, deterministic, bounded, idempotent],
    "Remove mount point. Idempotent if not mounted").

builtin(275, kb_mount_info, path_mount,
    iose([mount_path], [mount_record], []),
    [pure, deterministic, bounded, partial],
    "Mount details. Fails if not a mount point").

builtin(276, kb_list_mounts, path_mount,
    iose([kb_path], [list(mount_record)], []),
    [pure, deterministic, bounded],
    "All mounts in specified KB").

% --- connections ---
builtin(277, connection_add, path_mount,
    iose([kb_path, connection], [void], [connection_added]),
    [pure, deterministic, bounded],
    "Add typed connection to KB").

builtin(278, connection_remove, path_mount,
    iose([kb_path, target_path, relationship], [void], [connection_removed]),
    [pure, deterministic, bounded, idempotent],
    "Remove connection. Idempotent if not present").

builtin(279, connection_list, path_mount,
    iose([kb_path], [list(connection)], []),
    [pure, deterministic, bounded],
    "All connections from specified KB").

builtin(280, connection_query, path_mount,
    iose([relationship_type], [list(kb_path, kb_path)], []),
    [pure, deterministic, bounded],
    "Find all KB pairs connected by given relationship type").

builtin(281, connection_graph, path_mount,
    iose([], [graph], []),
    [pure, deterministic, bounded],
    "Build graph from all connections in current scope.
     Node IDs are KB integer IDs from path registry").


% ================================================================
% CATEGORY 16: SESSION MANAGEMENT (8 primitives)
% Slicing: capture | restore | lifecycle | comparison
% ================================================================

% --- capture ---
builtin(282, session_snapshot, session,
    iose([name, notes], [void], [live_state_captured, snapshot_kb_created]),
    [pure, deterministic, bounded],
    "Capture all live state atomically. Stored under
     root.sessions.<name>").

% --- restore ---
builtin(283, session_restore, session,
    iose([name], [void], [all_live_state_overwritten]),
    [pure, deterministic, bounded, idempotent],
    "Restore all live state from named snapshot.
     Idempotent: restoring same snapshot twice gives same state").

builtin(284, session_reset, session,
    iose([], [void], [all_live_state_cleared]),
    [pure, deterministic, bounded, idempotent],
    "Clear all live state to defaults. Persistent KB content
     untouched. Idempotent").

% --- lifecycle ---
builtin(285, session_clone, session,
    iose([source_name, clone_name], [void],
         [independent_live_state_copy_created]),
    [pure, deterministic, bounded],
    "Create independent session from snapshot. Clone gets own
     live state, shares persistent KBs").

builtin(286, session_kill, session,
    iose([name], [void], [clone_live_state_destroyed]),
    [pure, deterministic, bounded, idempotent],
    "Destroy cloned session's live state. Persistent KB
     assertions survive. Idempotent on dead clone").

builtin(287, session_list, session,
    iose([], [list(text)], []),
    [pure, deterministic, bounded],
    "List all saved snapshot names").

% --- comparison ---
builtin(288, session_diff, session,
    iose([name_a, name_b], [diff], []),
    [pure, deterministic, bounded],
    "Structured comparison of two snapshots. Shows added,
     removed, changed data primitive values").

builtin(289, session_info, session,
    iose([name], [session_metadata], []),
    [pure, deterministic, bounded, partial],
    "Metadata about snapshot: turn count, KB count, size.
     Fails if snapshot not found").


% ================================================================
% CATEGORIES 17-22: OPERATIONAL PRIMITIVES
% All require positive credential grants (VDR-6).
% All log execution to environment KB.
% All have declared side effects.
% ================================================================


% ================================================================
% CATEGORY 17: FILESYSTEM (15 primitives)
% Grant class: filesystem
% ================================================================

builtin(290, fs_read, filesystem,
    iose([path], [content], [file_accessed]),
    [operational, deterministic, bounded],
    "Read file contents. Grant: filesystem(read)").

builtin(291, fs_write, filesystem,
    iose([path, content], [void], [file_created_or_overwritten]),
    [operational, deterministic, bounded],
    "Create or overwrite file. Grant: filesystem(write)").

builtin(292, fs_append, filesystem,
    iose([path, content], [void], [file_appended]),
    [operational, deterministic, bounded],
    "Append content to file. Grant: filesystem(write)").

builtin(293, fs_exists, filesystem,
    iose([path], [bool], [file_accessed]),
    [operational, deterministic, bounded],
    "Check file existence. Grant: filesystem(read)").

builtin(294, fs_list_dir, filesystem,
    iose([path], [list(entry)], [directory_accessed]),
    [operational, deterministic, bounded],
    "List directory contents. Grant: filesystem(read)").

builtin(295, fs_create_dir, filesystem,
    iose([path], [void], [directory_created]),
    [operational, deterministic, bounded, idempotent],
    "Create directory and parents. Idempotent if exists.
     Grant: filesystem(write)").

builtin(296, fs_delete, filesystem,
    iose([path], [void], [file_or_directory_removed]),
    [operational, deterministic, bounded],
    "Delete file or directory. Grant: filesystem(delete)").

builtin(297, fs_move, filesystem,
    iose([source_path, dest_path], [void], [file_moved]),
    [operational, deterministic, bounded],
    "Move or rename. Grant: filesystem(write)").

builtin(298, fs_copy, filesystem,
    iose([source_path, dest_path], [void], [file_copied]),
    [operational, deterministic, bounded],
    "Copy file. Grant: filesystem(write)").

builtin(299, fs_file_size, filesystem,
    iose([path], [number], [file_accessed]),
    [operational, deterministic, bounded],
    "File size in bytes. Grant: filesystem(read)").

builtin(300, fs_file_modified, filesystem,
    iose([path], [timestamp], [file_accessed]),
    [operational, deterministic, bounded],
    "Last modification timestamp. Grant: filesystem(read)").

builtin(301, fs_glob, filesystem,
    iose([pattern], [list(path)], [directory_accessed]),
    [operational, deterministic, bounded],
    "Find files matching glob pattern. Grant: filesystem(read)").

builtin(302, fs_tree, filesystem,
    iose([path], [tree_listing], [directory_accessed]),
    [operational, deterministic, bounded],
    "Recursive directory listing. Grant: filesystem(read)").

builtin(303, fs_diff, filesystem,
    iose([path_a, path_b], [diff], [files_accessed]),
    [operational, deterministic, bounded],
    "Diff two files. Grant: filesystem(read)").

builtin(304, fs_checksum, filesystem,
    iose([path], [number], [file_accessed]),
    [operational, deterministic, bounded],
    "Compute file hash. Grant: filesystem(read)").


% ================================================================
% CATEGORY 18: COMPILATION (4 primitives)
% Grant class: compile
% ================================================================

builtin(305, compile_python_check, compilation,
    iose([source_path], [result], [cpu_used]),
    [operational, deterministic, bounded],
    "Python syntax verification. Grant: compile").

builtin(306, compile_zig, compilation,
    iose([source_path, output_path], [result], [cpu_used, file_created]),
    [operational, deterministic, bounded],
    "Zig compilation. Grant: compile").

builtin(307, compile_c, compilation,
    iose([source_path, output_path], [result], [cpu_used, file_created]),
    [operational, deterministic, bounded],
    "C compilation. Grant: compile").

builtin(308, compile_rust, compilation,
    iose([source_path, output_path], [result], [cpu_used, file_created]),
    [operational, deterministic, bounded],
    "Rust compilation. Grant: compile").


% ================================================================
% CATEGORY 19: EXECUTION (5 primitives)
% Grant class: execute
% ================================================================

builtin(309, exec_python, execution,
    iose([script_path], [result], [arbitrary_side_effects]),
    [operational],
    "Run Python script. Grant: execute").

builtin(310, exec_shell, execution,
    iose([command], [result], [arbitrary_side_effects]),
    [operational],
    "Run shell command. Grant: execute").

builtin(311, exec_zig_test, execution,
    iose([test_path], [result], [cpu_used]),
    [operational, deterministic],
    "Run Zig test suite. Grant: execute").

builtin(312, exec_pytest, execution,
    iose([test_path], [result], [cpu_used]),
    [operational],
    "Run pytest. Grant: execute").

builtin(313, exec_script, execution,
    iose([interpreter, script_path], [result], [arbitrary_side_effects]),
    [operational],
    "Run script with specified interpreter. Grant: execute").


% ================================================================
% CATEGORY 20: LINTING AND ANALYSIS (8 primitives)
% Grant class: lint (read-only)
% ================================================================

builtin(314, lint_python, linting,
    iose([source_path], [list(issue)], [file_read]),
    [operational, deterministic, bounded],
    "Python linter. Grant: lint").

builtin(315, lint_zig, linting,
    iose([source_path], [list(issue)], [file_read]),
    [operational, deterministic, bounded],
    "Zig linter. Grant: lint").

builtin(316, lint_json, linting,
    iose([source_path], [bool], [file_read]),
    [operational, deterministic, bounded],
    "JSON validation. Grant: lint").

builtin(317, lint_markdown, linting,
    iose([source_path], [list(issue)], [file_read]),
    [operational, deterministic, bounded],
    "Markdown checker. Grant: lint").

builtin(318, analyze_imports, linting,
    iose([source_path], [list(module)], [file_read]),
    [operational, deterministic, bounded],
    "List Python imports. Grant: lint").

builtin(319, analyze_complexity, linting,
    iose([source_path], [metrics], [file_read]),
    [operational, deterministic, bounded],
    "Cyclomatic complexity metrics. Grant: lint").

builtin(320, analyze_dependencies, linting,
    iose([source_path], [graph], [file_read]),
    [operational, deterministic, bounded],
    "Module dependency graph. Grant: lint").

builtin(321, count_lines, linting,
    iose([source_path], [line_counts], [file_read]),
    [operational, deterministic, bounded],
    "Line counts by type (code, comment, blank). Grant: lint").


% ================================================================
% CATEGORY 21: NETWORK (5 primitives)
% Grant class: network
% ================================================================

builtin(322, net_download, network,
    iose([url, local_path], [void], [network_request, file_created]),
    [operational],
    "Download URL to file. Grant: network").

builtin(323, net_fetch, network,
    iose([url], [content], [network_request]),
    [operational],
    "HTTP GET, return content. Grant: network").

builtin(324, net_post, network,
    iose([url, body], [response], [network_request]),
    [operational],
    "HTTP POST. Grant: network").

builtin(325, net_ping, network,
    iose([host], [bool], [network_request]),
    [operational, bounded],
    "Check host reachability. Grant: network").

builtin(326, net_dns_resolve, network,
    iose([hostname], [ip_address], [network_request]),
    [operational, bounded],
    "DNS lookup. Grant: network").


% ================================================================
% CATEGORY 22: PROCESS MANAGEMENT (7 primitives)
% Grant class: process
% ================================================================

builtin(327, proc_start, process,
    iose([command, args], [task_id], [process_created]),
    [operational],
    "Start background process. Grant: process").

builtin(328, proc_poll, process,
    iose([task_id], [status], []),
    [operational, bounded],
    "Check process status. Grant: process").

builtin(329, proc_wait, process,
    iose([task_id], [result], [blocks_until_complete]),
    [operational],
    "Wait for process completion. Grant: process").

builtin(330, proc_kill, process,
    iose([task_id], [void], [process_terminated]),
    [operational, bounded],
    "Terminate process. Grant: process").

builtin(331, proc_stdout, process,
    iose([task_id], [text], []),
    [operational, bounded],
    "Read current stdout buffer. Grant: process").

builtin(332, proc_stderr, process,
    iose([task_id], [text], []),
    [operational, bounded],
    "Read current stderr buffer. Grant: process").

builtin(333, proc_list, process,
    iose([], [list(process_info)], []),
    [operational, bounded],
    "List active processes. Grant: process").


% ================================================================
% VERIFICATION RULES
% Confirm the specification is comprehensive (OSO C17)
% ================================================================

% Total count
rule(total_primitive_count(Total) :-
    findall(Id, builtin(Id, _, _, _, _, _), Ids),
    length(Ids, Total)).
% Expected: 333

% Count by category
rule(category_count(Category, Count) :-
    category(_, Category, _, _),
    findall(Id, builtin(Id, _, Category, _, _, _), Ids),
    length(Ids, Count)).

% Verify all IDs are sequential with no gaps
rule(ids_sequential :-
    total_primitive_count(Total),
    forall(between(1, Total, Id), builtin(Id, _, _, _, _, _))).

% Verify no duplicate names
rule(no_duplicate_names :-
    forall((builtin(Id1, Name, _, _, _, _), builtin(Id2, Name, _, _, _, _)),
        Id1 = Id2)).

% Verify all pure primitives have no operational side effects
rule(pure_have_no_op_side_effects :-
    forall((builtin(_, _, Cat, iose(_, _, SE), Props, _),
            category(_, Cat, pure, _)),
        (not(member(network_request, SE)),
         not(member(file_created, SE)),
         not(member(process_created, SE)),
         not(member(arbitrary_side_effects, SE))))).

% Verify all operational primitives are in operational categories
rule(operational_in_operational_categories :-
    forall((builtin(_, _, Cat, _, Props, _),
            member(operational, Props)),
        category(_, Cat, operational, _))).

% Verify every IOSE has inputs and outputs declared
rule(all_iose_declared :-
    forall(builtin(_, _, _, iose(I, O, _), _, _),
        (is_list(I), is_list(O)))).

% Summary
rule(specification_summary(Summary) :-
    total_primitive_count(Total),
    findall(Cat-N, category_count(Cat, N), Cats),
    findall(Cat, category(_, Cat, pure, _), PureCats),
    findall(Cat, category(_, Cat, operational, _), OpCats),
    length(PureCats, NumPure),
    length(OpCats, NumOp),
    Summary = summary(
        total_primitives(Total),
        pure_categories(NumPure),
        operational_categories(NumOp),
        total_categories(22),
        category_counts(Cats))).


% ================================================================
% EXPECTED COUNTS
%
% Category                  Count   Running Total
% 1.  Text                    17          17
% 2.  Collections             36          53
% 3.  Arithmetic              26          79
% 4.  Sets                    14          93
% 5.  Mappings                15         108
% 6.  Linear Algebra          16         124
% 7.  Statistics              16         140
% 8.  Conversion              14         154
% 9.  Time                    10         164
% 10. Identity                 8         172
% 11. Graphs                  13         185
% 12. Logic/Control           11         196
% 13. KB Operations           15         211
% 14. Data Primitives         53         264
% 15. Path/Mount              17         281
% 16. Session                  8         289
%     --- pure subtotal ---  289
% 17. Filesystem              15         304
% 18. Compilation              4         308
% 19. Execution                5         313
% 20. Linting                  8         321
% 21. Network                  5         326
% 22. Process                  7         333
%     --- operational ---     44
%     === TOTAL ===          333
%
% Pure: 289 across 16 categories
% Operational: 44 across 6 categories
% Grand total: 333 across 22 categories
%
% Every category owns a domain.
% No domain gaps. No overlaps.
% Parts sum to whole.
% Comprehensive (OSO C17). Sliced from the pie (OSO C16).
% Every primitive has an IOSE declaration (OSO C12, C13).
% ================================================================
```
