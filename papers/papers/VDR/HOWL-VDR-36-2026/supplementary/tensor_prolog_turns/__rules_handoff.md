```
TENSORPROLOG_CODE_RULES_V1

LANGUAGE|Zig 0.14|No float anywhere|All numeric types are i8/i16/i32/i64/i128 or VDR structs containing those

TYPES|Prefer i32 for general values|i16 for remainders and counts|i64 for accumulators and wide products|i128 only inside mul/div for widening|Use @intCast for narrowing, @as for widening|Tagged unions for VlpTerm|Pack enums as i8|Align structs for cache (pad VlpKB to 256 bytes)

NAMING|snake_case for functions|PascalCase for types and structs|UPPER_SNAKE for constants|vlp_ prefix on types exported across modules (VlpStatus, VlpFact, etc)|No prefix on functions within their own module (add not q16_add — the struct method handles namespacing)|Test functions: test "descriptive lowercase name"

ARITHMETIC|Q16.D = 65536 never stored in struct|Multiply = widening i64 product then divTrunc by D and mod by D|Division = numerator * D / denominator|Softmax = shift-square-divide, last element absorbs rounding so sum = D exactly|Remainder is first-class — always i16 r0 field, never discarded silently|Compare same-D values by v then r0 directly, no cross-multiply needed when D is identical

STRUCTURE|Each src/ module gets a types.zig if it has shared types|Modules import siblings via @import("../module/file.zig")|Tests in test/ import via @import("../src/module/file.zig")|build.zig wires test targets per phase|No heap allocation in hot paths — use pre-allocated slabs passed as slices|Every data structure bounded at creation (capacity set at init, never grows)

COMMENTS|Brief mechanical only|Never duplicate what the code says|One line max per function explaining WHY not WHAT|No prose paragraphs in code|OK to have zero comments if the code is obvious

OUTPUT_FORMAT|Write all code for a turn as a single markdown code block with zig syntax highlighting|File boundaries marked by // ============ src/path/file.zig ============ comment lines|Source files first, then test files|If a mistake happens mid-file keep writing forward — never restart a module to save tokens|Errors get fixed in test+debug phase later

TURN_SIZING|Target ~1200 lines per turn|Source and tests ship together in same turn|Dependencies flow strictly downward — turn N never imports turn N+1|Each turn's tests should be runnable given all prior turns compiled

TEST_STYLE|Use std.testing.expect and std.testing.expectEqual|Helper functions like expectEql(a,b) for common comparisons|Test names are lowercase descriptive phrases: test "add remainder carry"|Cover: normal case, edge case, boundary, roundtrip, determinism where relevant|Determinism tests: run 1000 iterations memcmp to reference|Softmax tests always verify sum == D exactly via integer equality not tolerance

ERROR_HANDLING|Functions return VlpStatus for operations that can fail|Functions return ?T (optional) for lookups that may not find anything|Functions return the value directly for pure arithmetic that cannot fail (Q16.add always succeeds)|No exceptions, no panics in production paths — @panic only in unreachable branches|Division by zero returns zero value, not panic

IMPORTS|Each file imports only what it needs|Use const alias = @import for types used repeatedly|Standard library via const std = @import("std")|Sibling modules via relative path @import

MEMORY|No allocator in Q16/Q32/Q335 arithmetic — all stack/inline|KBStore and substores take slices allocated by caller|TextStore is append-only byte array — caller provides backing slice|Bounded primitives (LRU, queue, stack, ring, bitset) take capacity at init, backed by caller slice or fixed array

PATTERNS|Saturating arithmetic for counters (clamp not wrap)|Copy-on-write via page table struct with dirty bits|Snapshots are contiguous binary blobs: header + regions + CRC32|Prolog unification is recursive with explicit depth counter, not stack-based|Grammar rendering walks template bytes copying literals and rendering fills at slot positions

INVARIANTS_TO_MAINTAIN|Softmax output sum == D always (integer equality)|KB facts at integer addresses return exactly what was asserted|Bounded primitives never exceed declared capacity|Snapshot restore produces byte-identical state|Clone COW writes never visible to parent|Access check returns false for invisible KBs — data absent not filtered|Grant check happens before any side effect

WHAT_NOT_TO_DO|No floating point types anywhere (f16 f32 f64 — none)|No tolerance-based comparison|No epsilon parameters|No NaN/Inf checks|No loss scaling|No gradient clipping|No dynamic memory growth after init|No global mutable state — all state in explicit structs passed as parameters|No async/await — use threads and blocking queues for runners|Do not restart a module if you make a mistake — keep writing, fix later
```
