```zig
// ============================================================
// VDRProlog — Complete Function Signature Reference
// Zig 0.14 — Every module, every public function
// ============================================================

// ============================================================
// src/vdr/types.zig
// ============================================================

pub const VlpStatus = enum(i32) {
    ok = 0,
    err_not_init = 1,
    err_invalid_device = 2,
    err_out_of_memory = 3,
    err_invalid_qbasis = 4,
    err_qbasis_mismatch = 5,
    err_kb_not_found = 6,
    err_kb_access_denied = 7,
    err_kb_full = 8,
    err_kb_frozen = 9,
    err_slot_out_of_range = 10,
    err_grant_denied = 11,
    err_session_limit = 12,
    err_prolog_depth = 13,
    err_remainder_overflow = 14,
    err_grammar_invalid = 15,
    err_primitive_bounds = 16,
    err_snapshot_corrupt = 17,
    err_command_parse = 18,
    err_determinism = 19,
    err_auth_invalid = 20,
    err_auth_suspended = 21,
    err_rate_limited = 22,
    err_connection_closed = 23,
    err_timeout = 24,
    err_protocol_malformed = 25,
    err_prolog_no_match = 26,
    err_grammar_capacity = 27,
    err_grammar_type_mismatch = 28,
    err_runner_error_threshold = 29,
    err_runner_connection_loss = 30,
};

pub const VlpQBasis = enum(i32) {
    q16 = 16,
    q32 = 32,
    q335 = 335,
};

pub const VlpFactTag = enum(i8) {
    value = 0,
    text = 1,
    reference = 2,
    timestamp = 3,
    enum_val = 4,
    boolean = 5,
    vector = 6,
    matrix = 7,
    provenance = 8,
    rule_ref = 9,
    grammar_ref = 10,
    counter = 11,
    empty = -1,
};

pub const VlpSourceType = enum(i8) {
    vdr_computation = 0,
    prolog_derivation = 1,
    database = 2,
    prometheus = 3,
    script = 4,
    rest_api = 5,
    published = 6,
    user_stated = 7,
    web_search = 8,
    llm_generated = 9,
    unknown = 10,
};

pub const VlpVisibility = enum(i8) {
    public = 0,
    internal = 1,
    owner_only = 2,
};

pub const VlpGrantClass = enum(i8) {
    filesystem = 0,
    compile = 1,
    execute = 2,
    lint = 3,
    network = 4,
    process = 5,
};

pub const VlpGrantState = enum(i8) {
    active = 0,
    expired = 1,
    exhausted = 2,
    revoked = 3,
};

pub const VlpSessionState = enum(i8) {
    active = 0,
    snapshotted = 1,
    killed = 2,
    frozen = 3,
};

pub const VlpTermType = enum(i8) {
    atom = 0,
    variable = 1,
    integer = 2,
    vdr = 3,
    text = 4,
    list = 5,
    compound = 6,
    vector = 7,
    matrix = 8,
    pair = 9,
};

pub const VlpSlotType = enum(i8) {
    vdr_value = 0,
    text = 1,
    integer = 2,
    enum_val = 3,
    kb_ref = 4,
    grammar = 5,
};

pub const VlpCommandType = enum(i8) {
    kb_assert = 0,
    kb_query = 1,
    kb_retract = 2,
    prolog_query = 3,
    prolog_assert_rule = 4,
    builtin_call = 5,
    grammar_render = 6,
    direct_output = 7,
    op_filesystem = 8,
    op_compile = 9,
    op_execute = 10,
    op_network = 11,
    op_process = 12,
    session_snapshot = 13,
    session_clone = 14,
};

pub const VlpAuditAction = enum(i8) {
    fact_assert = 0,
    fact_retract = 1,
    fact_query = 2,
    rule_fire = 3,
    rule_assert = 4,
    rule_retract = 5,
    grant_check = 6,
    grant_create = 7,
    grant_revoke = 8,
    session_create = 9,
    session_kill = 10,
    snapshot = 11,
    clone = 12,
    op_execute = 13,
    access_denied = 14,
};

pub const VlpRunnerType = enum(i8) {
    poller = 0,
    processor = 1,
    internal = 2,
    batch = 3,
};

pub const VlpRunnerState = enum(i8) {
    stopped = 0,
    running = 1,
    err = 2,
    recycling = 3,
};

pub const VlpTokenClass = enum(i8) {
    command_start = 0,
    direct_output = 1,
    end_of_turn = 2,
    prose = 3,
};

pub const VlpExecutionLevel = enum(i8) {
    l1 = 0,
    l2 = 1,
    l3 = 2,
};

pub const VlpMergePolicy = enum(i8) {
    ours = 0,
    theirs = 1,
    fail_on_conflict = 2,
};

pub const VlpProtocolType = enum(i8) {
    http = 0,
    websocket = 1,
    smtp = 2,
    mqtt = 3,
    raw_tcp = 4,
};

pub const VlpConnectionState = enum(i8) {
    handshake = 0,
    active = 1,
    draining = 2,
    closed = 3,
};

pub const VlpReduceOp = enum(i8) {
    sum = 0,
    max = 1,
    min = 2,
};

// ============================================================
// src/vdr/q16.zig
// ============================================================

pub const Q16 = struct {
    v: i32,
    r0: i16,
    _pad: i16 = 0,

    pub const D: i32 = 65536;

    pub fn add(a: Q16, b: Q16) Q16;
    pub fn sub(a: Q16, b: Q16) Q16;
    pub fn mul(a: Q16, b: Q16) Q16;
    pub fn div(a: Q16, b: Q16) Q16;
    pub fn compare(a: Q16, b: Q16) i32;
    pub fn eql(a: Q16, b: Q16) bool;
    pub fn fromFraction(num: i32, den: i32) Q16;
    pub fn toFraction(self: Q16) struct { num: i32, den: i32 };
    pub fn zero() Q16;
    pub fn one() Q16;
    pub fn negate(self: Q16) Q16;
    pub fn abs_val(self: Q16) Q16;
    pub fn sign(self: Q16) i32;
    pub fn min_val(a: Q16, b: Q16) Q16;
    pub fn max_val(a: Q16, b: Q16) Q16;
    pub fn remainderMagnitude(self: Q16) i32;
    pub fn compact(self: *Q16) void;
    pub fn softmax(logits: []const Q16, probs: []Q16) void;
    pub fn dotProduct(a: []const Q16, b: []const Q16) Q16;
};

// ============================================================
// src/vdr/q32.zig
// ============================================================

pub const Q32 = struct {
    v: i64,
    r0: i32,
    r1: i32,

    pub const D: i64 = 4294967296;

    pub fn add(a: Q32, b: Q32) Q32;
    pub fn sub(a: Q32, b: Q32) Q32;
    pub fn mul(a: Q32, b: Q32) Q32;
    pub fn div(a: Q32, b: Q32) Q32;
    pub fn compare(a: Q32, b: Q32) i32;
    pub fn eql(a: Q32, b: Q32) bool;
    pub fn fromFraction(num: i64, den: i64) Q32;
    pub fn toFraction(self: Q32) struct { num: i64, den: i64 };
    pub fn zero() Q32;
    pub fn one() Q32;
    pub fn negate(self: Q32) Q32;
    pub fn abs_val(self: Q32) Q32;
    pub fn remainderMagnitude(self: Q32) i64;
    pub fn compact(self: *Q32) void;
};

// ============================================================
// src/vdr/q335.zig
// ============================================================

pub const Limb6 = [6]i64;

pub const Q335 = struct {
    v: Limb6,
    r0: Limb6,
    r1: Limb6,
    r2: Limb6,
    r3: Limb6,

    pub fn add(a: Q335, b: Q335) Q335;
    pub fn sub(a: Q335, b: Q335) Q335;
    pub fn mul(a: Q335, b: Q335) Q335;
    pub fn div(a: Q335, b: Q335) Q335;
    pub fn compare(a: Q335, b: Q335) i32;
    pub fn eql(a: Q335, b: Q335) bool;
    pub fn zero() Q335;
    pub fn one() Q335;
    pub fn remainderMagnitude(self: Q335) Limb6;
    pub fn compact(self: *Q335) void;
};

pub fn addLimbs(a: Limb6, b: Limb6) Limb6;
pub fn subLimbs(a: Limb6, b: Limb6) Limb6;
pub fn mulLimbs(a: Limb6, b: Limb6) struct { hi: Limb6, lo: Limb6 };
pub fn shrLimbs(val: Limb6, shift: u32) Limb6;
pub fn compareLimbs(a: Limb6, b: Limb6) i32;
pub fn isZeroLimbs(a: Limb6) bool;

// ============================================================
// src/vdr/reproject.zig
// ============================================================

pub fn q16ToQ32(val: Q16) Q32;
pub fn q32ToQ16(val: Q32) Q16;
pub fn q16ToQ335(val: Q16) Q335;
pub fn q335ToQ16(val: Q335) Q16;
pub fn q32ToQ335(val: Q32) Q335;
pub fn q335ToQ32(val: Q335) Q32;

// ============================================================
// src/kb/types.zig
// ============================================================

pub const VlpProvenance = struct {
    source_type: VlpSourceType,
    source_kb_id: i32,
    source_slot_id: i32,
    confidence: Q16,
    timestamp: i32,
    derivation_rule_id: i32,
};

pub const VlpFact = struct {
    tag: VlpFactTag,
    value: Q16,
    provenance: VlpProvenance,
};

pub const VlpKB = struct {
    name_offset: i32,
    name_length: i16,
    path_offset: i32,
    path_length: i16,
    id: i32,
    facts_offset: i32,
    facts_count: i32,
    facts_capacity: i32,
    rules_offset: i32,
    rules_count: i32,
    rules_capacity: i32,
    constraints_offset: i32,
    constraints_count: i32,
    connections_offset: i32,
    connections_count: i32,
    grammars_offset: i32,
    grammars_count: i32,
    iose_offset: i32,
    working_data_offset: i32,
    lru_table_offset: i32,
    lru_count: i16,
    counter_table_offset: i32,
    counter_count: i16,
    lock_table_offset: i32,
    lock_count: i16,
    queue_table_offset: i32,
    queue_count: i16,
    stack_table_offset: i32,
    stack_count: i16,
    ring_table_offset: i32,
    ring_count: i16,
    bitset_table_offset: i32,
    bitset_count: i16,
    parent_id: i32,
    children_offset: i32,
    children_count: i16,
    children_capacity: i16,
    mounts_offset: i32,
    mounts_count: i16,
    visibility: VlpVisibility,
    frozen: bool,
    owner_offset: i32,
    owner_length: i16,
    created_at: i32,
    last_modified: i32,
    _padding: [58]u8 = [_]u8{0} ** 58,
};

pub const KBCreateConfig = struct {
    name: []const u8,
    parent_id: i32,
    visibility: VlpVisibility,
    owner: []const u8,
    max_facts: i32,
    max_rules: i32,
    max_children: i32,
};

pub const KBStoreConfig = struct {
    max_kbs: i32,
    max_facts: i64,
    max_text_bytes: i64,
    path_index_capacity: i32,
};

// ============================================================
// src/kb/store.zig
// ============================================================

pub const KBStore = struct {
    kbs: []VlpKB,
    kb_count: i32,
    kb_capacity: i32,
    facts: []VlpFact,
    fact_count: i64,
    fact_capacity: i64,
    text: TextStore,
    path_index: PathIndex,

    pub fn init(config: KBStoreConfig) KBStore;
    pub fn deinit(self: *KBStore) void;
    pub fn createKB(self: *KBStore, config: KBCreateConfig) i32;
    pub fn destroyKB(self: *KBStore, kb_id: i32) VlpStatus;
    pub fn getKB(self: *KBStore, kb_id: i32) ?*VlpKB;
    pub fn count(self: *const KBStore) i32;
    pub fn capacity(self: *const KBStore) i32;
    pub fn resolvePath(self: *KBStore, path: []const u8) ?i32;
};

// ============================================================
// src/kb/text_store.zig
// ============================================================

pub const TextStore = struct {
    data: []u8,
    len: i64,
    capacity: i64,

    pub fn init(capacity: i64) TextStore;
    pub fn deinit(self: *TextStore) void;
    pub fn append(self: *TextStore, bytes: []const u8) struct { offset: i32, length: i16 };
    pub fn read(self: *const TextStore, offset: i32, length: i16) []const u8;
};

// ============================================================
// src/kb/fact.zig
// ============================================================

pub fn factAssert(store: *KBStore, kb_id: i32, slot_id: i32, fact: *const VlpFact) VlpStatus;
pub fn factQuery(store: *KBStore, kb_id: i32, slot_id: i32) ?VlpFact;
pub fn factRetract(store: *KBStore, kb_id: i32, slot_id: i32) VlpStatus;
pub fn factSearch(store: *KBStore, kb_id: i32, tag: VlpFactTag, results: []VlpFact) i32;
pub fn factScopedSearch(store: *KBStore, start_kb_id: i32, tag: VlpFactTag, results: []VlpFact) i32;

// ============================================================
// src/kb/tree.zig
// ============================================================

pub fn addChild(store: *KBStore, parent_id: i32, child_id: i32) VlpStatus;
pub fn removeChild(store: *KBStore, parent_id: i32, child_id: i32) VlpStatus;
pub fn getParent(store: *KBStore, kb_id: i32) ?i32;
pub fn getChildren(store: *KBStore, kb_id: i32) []const i32;
pub fn ancestorWalk(store: *KBStore, kb_id: i32, callback: *const fn (i32) bool) void;

// ============================================================
// src/kb/path_index.zig
// ============================================================

pub const PathIndex = struct {
    keys: []i32,
    values: []i32,
    occupied: []bool,
    capacity: i32,
    count: i32,

    pub fn init(capacity: i32) PathIndex;
    pub fn deinit(self: *PathIndex) void;
    pub fn insert(self: *PathIndex, path: []const u8, kb_id: i32) VlpStatus;
    pub fn lookup(self: *const PathIndex, path: []const u8) ?i32;
    pub fn remove(self: *PathIndex, path: []const u8) VlpStatus;
    pub fn computeHash(path: []const u8) i32;
};

// ============================================================
// src/kb/visibility.zig
// ============================================================

pub fn checkAccess(store: *KBStore, user_id: i32, user_visibility: VlpVisibility, kb_id: i32) bool;
pub fn resolveVisibleKBs(store: *KBStore, user_id: i32, user_visibility: VlpVisibility, scope_kb_id: i32, visible: []i32) i32;

// ============================================================
// src/safety/types.zig
// ============================================================

pub const VlpGrant = struct {
    id: i32,
    class: VlpGrantClass,
    state: VlpGrantState,
    holder_user_id: i32,
    target_pattern_offset: i32,
    target_pattern_length: i16,
    max_uses: i32,
    remaining_uses: i32,
    expires_at: i32,
    created_at: i32,
    created_by: i32,
    revoked_at: i32,
    revoked_by: i32,
};

pub const VlpAuditEntry = struct {
    timestamp: i32,
    session_id: i32,
    user_id: i32,
    action: VlpAuditAction,
    target_kb_id: i32,
    target_slot_id: i32,
    grant_id: i32,
    result: i8,
    detail_offset: i32,
};

pub const GrantCheckResult = struct {
    granted: bool,
    grant_id: i32,
};

// ============================================================
// src/safety/grant.zig
// ============================================================

pub const GrantStore = struct {
    grants: []VlpGrant,
    count: i32,
    capacity: i32,

    pub fn init(capacity: i32) GrantStore;
    pub fn deinit(self: *GrantStore) void;
    pub fn create(self: *GrantStore, grant: VlpGrant) VlpStatus;
    pub fn check(self: *GrantStore, user_id: i32, class: VlpGrantClass, target: []const u8, now: i32) GrantCheckResult;
    pub fn revoke(self: *GrantStore, grant_id: i32, revoked_by: i32, now: i32) VlpStatus;
    pub fn list(self: *const GrantStore, user_id: i32, out: []VlpGrant) i32;
    pub fn cleanup(self: *GrantStore, now: i32) i32;
};

// ============================================================
// src/safety/audit.zig
// ============================================================

pub const AuditFilter = struct {
    user_id: ?i32,
    action: ?VlpAuditAction,
    after_timestamp: ?i32,
    before_timestamp: ?i32,
};

pub const AuditRing = struct {
    entries: []VlpAuditEntry,
    capacity: i32,
    head: i32,
    count: i32,

    pub fn init(capacity: i32) AuditRing;
    pub fn deinit(self: *AuditRing) void;
    pub fn write(self: *AuditRing, entry: VlpAuditEntry) void;
    pub fn query(self: *const AuditRing, filter: AuditFilter, out: []VlpAuditEntry) i32;
    pub fn totalCount(self: *const AuditRing) i32;
};

// ============================================================
// src/confidence/types.zig
// ============================================================

pub const CONFIDENCE_TABLE: [11]Q16 = .{
    Q16{ .v = 65536, .r0 = 0 },  // vdr_computation
    Q16{ .v = 65536, .r0 = 0 },  // prolog_derivation
    Q16{ .v = 64225, .r0 = 0 },  // database
    Q16{ .v = 62259, .r0 = 0 },  // prometheus
    Q16{ .v = 62259, .r0 = 0 },  // script
    Q16{ .v = 55705, .r0 = 0 },  // rest_api
    Q16{ .v = 52428, .r0 = 0 },  // published
    Q16{ .v = 45875, .r0 = 0 },  // user_stated
    Q16{ .v = 32768, .r0 = 0 },  // web_search
    Q16{ .v = 19660, .r0 = 0 },  // llm_generated
    Q16{ .v = 0, .r0 = 0 },      // unknown
};

// ============================================================
// src/confidence/propagate.zig
// ============================================================

pub fn assignFromSource(source_type: VlpSourceType) Q16;
pub fn combineAgreeing(confidences: []const Q16) Q16;
pub fn combineConflicting(confidences: []const Q16, penalty: Q16) Q16;
pub fn chain(per_link: Q16, n_links: i32) Q16;
pub fn propagate(store: *KBStore, kb_id: i32, slot_id: i32) Q16;

// ============================================================
// src/prolog/types.zig
// ============================================================

pub const VlpTerm = struct {
    type: VlpTermType,
    data: TermData,
};

pub const TermData = union {
    atom_id: i32,
    var_id: i32,
    int_value: i32,
    vdr_value: Q16,
    text: struct { offset: i32, length: i16 },
    list: struct { head_offset: i32, tail_offset: i32 },
    compound: struct { functor_id: i32, args_offset: i32, args_count: i16 },
};

pub const VlpBinding = struct {
    var_id: i32,
    term: VlpTerm,
};

pub const BindingSet = struct {
    bindings: []VlpBinding,
    count: i32,
    capacity: i32,

    pub fn init(capacity: i32) BindingSet;
    pub fn deinit(self: *BindingSet) void;
    pub fn bind(self: *BindingSet, var_id: i32, term: VlpTerm) VlpStatus;
    pub fn lookup(self: *const BindingSet, var_id: i32) ?VlpTerm;
    pub fn undo(self: *BindingSet, checkpoint: i32) void;
    pub fn checkpoint(self: *const BindingSet) i32;
    pub fn clear(self: *BindingSet) void;
};

pub const VlpRule = struct {
    id: i32,
    head_offset: i32,
    body_offset: i32,
    body_count: i16,
    action_offset: i32,
    action_count: i16,
    fire_count: i32,
    last_fired: i32,
    success_count: i32,
    failure_count: i32,
    created_at: i32,
    creator_session_id: i32,
};

pub const QueryConfig = struct {
    max_depth: i32 = 100,
    max_results: i32 = 100,
};

pub const QueryResults = struct {
    binding_sets: []BindingSet,
    count: i32,
};

pub const PrologFired = struct {
    rule_id: i32,
    bindings: BindingSet,
    actions: []PrologAction,
    action_count: i32,
    confidence: Q16,
};

pub const PrologAction = struct {
    type: enum(i8) { assert_fact, retract_fact, direct_output },
    target_kb_id: i32,
    target_slot_id: i32,
    fact: VlpFact,
};

pub const RuleStats = struct {
    fire_count: i32,
    last_fired: i32,
    success_count: i32,
    failure_count: i32,
};

pub const HygieneCandidate = struct {
    rule_id: i32,
    reason: enum(i8) { stale, failing, orphaned },
    detail: i32,
};

// ============================================================
// src/prolog/term.zig
// ============================================================

pub fn makeAtom(id: i32) VlpTerm;
pub fn makeVar(id: i32) VlpTerm;
pub fn makeInt(val: i32) VlpTerm;
pub fn makeVdr(val: Q16) VlpTerm;
pub fn makeText(offset: i32, length: i16) VlpTerm;
pub fn makeList(head_offset: i32, tail_offset: i32) VlpTerm;
pub fn makeCompound(functor_id: i32, args_offset: i32, args_count: i16) VlpTerm;
pub fn termEql(a: VlpTerm, b: VlpTerm) bool;
pub fn containsVar(term: VlpTerm, var_id: i32, term_store: []const VlpTerm) bool;

// ============================================================
// src/prolog/unify.zig
// ============================================================

pub fn unify(a: *const VlpTerm, b: *const VlpTerm, bindings: *BindingSet, term_store: []const VlpTerm, depth: i32) bool;

// ============================================================
// src/prolog/query.zig
// ============================================================

pub fn query(store: *KBStore, start_kb_id: i32, goal: *const VlpTerm, term_store: []const VlpTerm, config: QueryConfig, results: *QueryResults) VlpStatus;

// ============================================================
// src/prolog/rule.zig
// ============================================================

pub const RuleStore = struct {
    rules: []VlpRule,
    terms: []VlpTerm,
    rule_count: i32,
    rule_capacity: i32,
    term_count: i32,
    term_capacity: i32,

    pub fn init(rule_capacity: i32, term_capacity: i32) RuleStore;
    pub fn deinit(self: *RuleStore) void;
    pub fn assertRule(self: *RuleStore, kb_store: *KBStore, kb_id: i32, head: VlpTerm, body: []const VlpTerm, actions: []const PrologAction) i32;
    pub fn retractRule(self: *RuleStore, rule_id: i32) VlpStatus;
    pub fn fireAll(self: *RuleStore, kb_store: *KBStore, kb_id: i32, results: []PrologFired) i32;
    pub fn fireAndCommit(self: *RuleStore, kb_store: *KBStore, kb_id: i32) i32;
    pub fn getRuleStats(self: *const RuleStore, rule_id: i32) ?RuleStats;
};

// ============================================================
// src/prolog/hygiene.zig
// ============================================================

pub fn hygieneScan(rule_store: *RuleStore, grant_store: *const GrantStore, stale_days: i32, min_success_num: i32, min_success_den: i32, now: i32, candidates: []HygieneCandidate) i32;

// ============================================================
// src/grammar/types.zig
// ============================================================

pub const VlpGrammarSlot = struct {
    name_offset: i32,
    name_length: i16,
    slot_type: VlpSlotType,
    enum_values_offset: i32,
    enum_count: i16,
    default_kb_id: i32,
    default_slot_id: i32,
};

pub const VlpGrammar = struct {
    id: i32,
    template_offset: i32,
    template_length: i32,
    slots: []VlpGrammarSlot,
    slots_count: i16,
    validated: bool,
    created_at: i32,
    creator_session_id: i32,
};

pub const VlpGrammarFill = struct {
    slot_index: i16,
    fill_type: VlpSlotType,
    data: GrammarFillData,
};

pub const GrammarFillData = union {
    vdr_value: Q16,
    text: struct { ptr: []const u8 },
    int_value: i32,
    enum_index: i16,
};

pub const GrammarKBMapping = struct {
    slot_index: i16,
    kb_id: i32,
    slot_id: i32,
};

pub const RenderResult = struct {
    len: i32,
    status: VlpStatus,
};

// ============================================================
// src/grammar/compile.zig
// ============================================================

pub fn compile(template: []const u8, text_store: *TextStore, grammar_out: *VlpGrammar) VlpStatus;

// ============================================================
// src/grammar/render.zig
// ============================================================

pub fn render(grammar: *const VlpGrammar, text_store: *const TextStore, fills: []const VlpGrammarFill, output: []u8) RenderResult;
pub fn renderFromKB(grammar: *const VlpGrammar, text_store: *const TextStore, store: *KBStore, mappings: []const GrammarKBMapping, output: []u8) RenderResult;

// ============================================================
// src/grammar/validate.zig
// ============================================================

pub fn validate(grammar: *const VlpGrammar, text_store: *const TextStore) struct { valid: bool, error_msg: []const u8 };

// ============================================================
// src/grammar/inherit.zig
// ============================================================

pub fn inherit(store: *KBStore, kb_id: i32, grammar_slot: i32) ?*VlpGrammar;

// ============================================================
// src/primitives/types.zig
// ============================================================

pub const LRUEntry = struct {
    key: i32,
    value: VlpFact,
    prev: i32,
    next: i32,
};

pub const CounterState = struct {
    value: i32,
    min_val: i32,
    max_val: i32,
    initial: i32,
};

// ============================================================
// src/primitives/lru.zig
// ============================================================

pub const LRU = struct {
    entries: []LRUEntry,
    index: []i32,
    capacity: i32,
    count: i32,
    head: i32,
    tail: i32,

    pub fn init(capacity: i32) LRU;
    pub fn deinit(self: *LRU) void;
    pub fn get(self: *LRU, key: i32) ?VlpFact;
    pub fn put(self: *LRU, key: i32, value: VlpFact) void;
    pub fn evictOldest(self: *LRU) ?VlpFact;
    pub fn size(self: *const LRU) i32;
    pub fn clear(self: *LRU) void;
};

// ============================================================
// src/primitives/counter.zig
// ============================================================

pub const Counter = struct {
    state: CounterState,

    pub fn init(min_val: i32, max_val: i32, initial: i32) Counter;
    pub fn get(self: *const Counter) i32;
    pub fn increment(self: *Counter, amount: i32) void;
    pub fn reset(self: *Counter) void;
    pub fn atBound(self: *const Counter) struct { at_min: bool, at_max: bool };
};

// ============================================================
// src/primitives/lock.zig
// ============================================================

pub const Lock = struct {
    held: bool,

    pub fn init() Lock;
    pub fn acquire(self: *Lock) bool;
    pub fn release(self: *Lock) VlpStatus;
    pub fn query_held(self: *const Lock) bool;
};

// ============================================================
// src/primitives/queue.zig
// ============================================================

pub const BoundedQueue = struct {
    entries: []VlpFact,
    capacity: i32,
    count: i32,
    head: i32,
    tail: i32,

    pub fn init(capacity: i32) BoundedQueue;
    pub fn deinit(self: *BoundedQueue) void;
    pub fn push(self: *BoundedQueue, fact: VlpFact) bool;
    pub fn pop(self: *BoundedQueue) ?VlpFact;
    pub fn peek(self: *const BoundedQueue) ?VlpFact;
    pub fn size(self: *const BoundedQueue) i32;
    pub fn clear(self: *BoundedQueue) void;
};

// ============================================================
// src/primitives/stack.zig
// ============================================================

pub const BoundedStack = struct {
    entries: []VlpFact,
    capacity: i32,
    top: i32,

    pub fn init(capacity: i32) BoundedStack;
    pub fn deinit(self: *BoundedStack) void;
    pub fn push(self: *BoundedStack, fact: VlpFact) bool;
    pub fn pop(self: *BoundedStack) ?VlpFact;
    pub fn peek(self: *const BoundedStack) ?VlpFact;
    pub fn size(self: *const BoundedStack) i32;
    pub fn clear(self: *BoundedStack) void;
};

// ============================================================
// src/primitives/ring.zig
// ============================================================

pub const RingBuffer = struct {
    entries: []VlpFact,
    capacity: i32,
    count: i32,
    write_pos: i32,

    pub fn init(capacity: i32) RingBuffer;
    pub fn deinit(self: *RingBuffer) void;
    pub fn write(self: *RingBuffer, fact: VlpFact) void;
    pub fn read(self: *const RingBuffer, index: i32) ?VlpFact;
    pub fn size(self: *const RingBuffer) i32;
    pub fn clear(self: *RingBuffer) void;
};

// ============================================================
// src/primitives/bitset.zig
// ============================================================

pub const Bitset = struct {
    bits: []u8,
    n_bits: i32,

    pub fn init(n_bits: i32) Bitset;
    pub fn deinit(self: *Bitset) void;
    pub fn set(self: *Bitset, bit: i32) void;
    pub fn clearBit(self: *Bitset, bit: i32) void;
    pub fn get(self: *const Bitset, bit: i32) bool;
    pub fn popcount(self: *const Bitset) i32;
    pub fn clearAll(self: *Bitset) void;
};

// ============================================================
// src/session/types.zig
// ============================================================

pub const VlpSession = struct {
    id: i32,
    user_id: i32,
    kb_root_id: i32,
    visibility_level: VlpVisibility,
    state: VlpSessionState,
    max_kb_count: i32,
    max_live_memory_bytes: i64,
    max_turns: i32,
    current_turn: i32,
    facts_asserted: i32,
    facts_retracted: i32,
    rules_fired: i64,
    prolog_queries: i64,
    primitive_calls: i64,
    grammar_renders: i64,
    llm_tokens_consumed: i64,
    command_tokens_consumed: i64,
    l1_count: i64,
    l2_count: i64,
    l3_count: i64,
    last_snapshot_id: i32,
    last_snapshot_timestamp: i32,
    parent_session_id: i32,
    clone_generation: i32,
    cached_system_prompt: [2048]i32 = [_]i32{0} ** 2048,
    cached_system_prompt_len: i32 = 0,
    cached_system_prompt_valid: bool = false,
};

pub const SessionConfig = struct {
    kb_root_id: i32,
    user_id: i32,
    visibility_level: VlpVisibility,
    max_kb_count: i32 = 100,
    max_live_memory_bytes: i64 = 16 * 1024 * 1024,
    max_turns: i32 = 0,
    auto_snapshot_interval: i32 = 0,
};

pub const CloneConfig = struct {
    fresh_live: bool = true,
    inherit_rules: bool = true,
    max_turns: i32 = 0,
};

pub const VlpSnapshotHeader = struct {
    magic: [4]u8,
    version: i32,
    timestamp: i32,
    session_id: i32,
    user_id: i32,
    kb_region_size: i64,
    fact_region_size: i64,
    rule_region_size: i64,
    term_region_size: i64,
    text_region_size: i64,
    grammar_region_size: i64,
    live_state_region_size: i64,
    grant_region_size: i64,
    path_index_region_size: i64,
    kb_count: i32,
    fact_count: i64,
    rule_count: i32,
    term_count: i64,
    grammar_count: i32,
    grant_count: i32,
    session_metadata: VlpSession,
    checksum: i32,
    total_size: i64,
};

pub const VlpSnapshot = struct {
    header: VlpSnapshotHeader,
    data: []u8,
};

pub const SnapshotDiff = struct {
    facts_changed: i32,
    rules_changed: i32,
    live_state_changed: bool,
    identical: bool,
};

// ============================================================
// src/session/lifecycle.zig
// ============================================================

pub fn sessionCreate(store: *KBStore, config: SessionConfig) VlpSession;
pub fn sessionDestroy(session: *VlpSession, store: *KBStore) void;
pub fn sessionClone(parent: *VlpSession, store: *KBStore, config: CloneConfig) VlpSession;
pub fn sessionMerge(parent: *VlpSession, child: *VlpSession, store: *KBStore, policy: VlpMergePolicy) VlpStatus;
pub fn sessionKill(session: *VlpSession, store: *KBStore) void;

// ============================================================
// src/session/cow.zig
// ============================================================

pub const COWPage = struct {
    source_ptr: [*]u8,
    private_ptr: ?[*]u8,
    dirty: bool,
};

pub const COWPageTable = struct {
    pages: []COWPage,
    n_pages: i32,

    pub fn init(source_pages: []const [*]u8) COWPageTable;
    pub fn deinit(self: *COWPageTable) void;
    pub fn read(self: *const COWPageTable, page_id: i32) [*]const u8;
    pub fn writeBegin(self: *COWPageTable, page_id: i32) [*]u8;
    pub fn dirtyPages(self: *const COWPageTable, out: []i32) i32;
    pub fn resolve(self: *COWPageTable) void;
};

// ============================================================
// src/session/snapshot.zig
// ============================================================

pub fn snapshotSave(session: *const VlpSession, store: *const KBStore, rule_store: *const RuleStore, grant_store: *const GrantStore) VlpSnapshot;
pub fn snapshotRestore(snapshot: *const VlpSnapshot, session: *VlpSession, store: *KBStore, rule_store: *RuleStore, grant_store: *GrantStore) VlpStatus;
pub fn snapshotSaveToFile(snapshot: *const VlpSnapshot, path: []const u8) VlpStatus;
pub fn snapshotLoadFromFile(path: []const u8) ?VlpSnapshot;
pub fn snapshotDiff(a: *const VlpSnapshot, b: *const VlpSnapshot) SnapshotDiff;
pub fn crc32(data: []const u8) i32;

// ============================================================
// src/engine/context.zig
// ============================================================

pub const VlpContext = struct {
    token_ids: [4096]i32,
    n_tokens: i32,
};

pub fn contextBuild(session: *VlpSession, input: *const VlpInput, store: *KBStore, context: *VlpContext) VlpStatus;

// ============================================================
// src/engine/scratchpad.zig
// ============================================================

pub const Scratchpad = struct {
    buf: []u8,
    len: i32,
    capacity: i32,

    pub fn init(capacity: i32) Scratchpad;
    pub fn deinit(self: *Scratchpad) void;
    pub fn writeResult(self: *Scratchpad, data: []const u8) void;
    pub fn writeError(self: *Scratchpad, status: VlpStatus) void;
    pub fn writeDenied(self: *Scratchpad, kb_id: i32) void;
    pub fn writeGrantDenied(self: *Scratchpad, class: VlpGrantClass) void;
    pub fn clear(self: *Scratchpad) void;
    pub fn getContents(self: *const Scratchpad) []const u8;
};

// ============================================================
// src/engine/token_classify.zig
// ============================================================

pub fn classify(token_id: i32, command_vocab_start: i32, command_vocab_end: i32, direct_output_token: i32, eos_token: i32) VlpTokenClass;

// ============================================================
// src/engine/level_stats.zig
// ============================================================

pub const LevelStats = struct {
    l1_count: i64,
    l2_count: i64,
    l3_count: i64,
    l1_tokens: i64,

    pub fn init() LevelStats;
    pub fn update(self: *LevelStats, level: VlpExecutionLevel, tokens: i32) void;
    pub fn getAutoTriageRate(self: *const LevelStats) struct { num: i64, den: i64 };
    pub fn reset(self: *LevelStats) void;
};

// ============================================================
// src/engine/command_parse.zig
// ============================================================

pub const VlpCommand = struct {
    type: VlpCommandType,
    target_kb_id: i32,
    target_slot_id: i32,
    builtin_id: i32,
    args: [16]VlpTerm,
    args_count: i16,
    grant_required: i8,
};

pub fn commandParse(tokens: []const i32, n_tokens: i32, store: *KBStore, command: *VlpCommand) VlpStatus;

// ============================================================
// src/engine/command_exec.zig
// ============================================================

pub const CommandResult = struct {
    status: VlpStatus,
    result_kb_id: i32,
    result_slot_id: i32,
    rule_fired: bool,
    output_bytes: []const u8,
    output_len: i32,
};

pub fn commandExecute(session: *VlpSession, command: *const VlpCommand, store: *KBStore, rule_store: *RuleStore, grant_store: *GrantStore, audit: *AuditRing, scratchpad: *Scratchpad) CommandResult;

// ============================================================
// src/engine/auto_resolve.zig
// ============================================================

pub const AutoResolution = struct {
    fully_handled: bool,
    grammar: ?*VlpGrammar,
    mappings: [16]GrammarKBMapping,
    n_mappings: i32,
    n_actions: i32,
};

pub fn checkAutoResolution(session: *VlpSession, input: *const VlpInput, auto_results: []const PrologFired, n_fired: i32, store: *KBStore, confidence_threshold: Q16) AutoResolution;

// ============================================================
// src/engine/cycle.zig
// ============================================================

pub const VlpInput = struct {
    token_ids: []const i32,
    n_tokens: i32,
    raw_bytes: ?[]const u8,
};

pub const VlpOutputBuffer = struct {
    buf: []u8,
    len: i32,
    capacity: i32,

    pub fn init(buf: []u8) VlpOutputBuffer;
    pub fn writeToken(self: *VlpOutputBuffer, token_id: i32) void;
    pub fn writeBytes(self: *VlpOutputBuffer, bytes: []const u8) void;
};

pub const CycleResult = struct {
    status: VlpStatus,
    tokens_consumed: i32,
    commands_executed: i32,
    level: VlpExecutionLevel,
    should_recycle: bool,
};

pub fn vlpCycle(session: *VlpSession, input: *const VlpInput, output: *VlpOutputBuffer, store: *KBStore, rule_store: *RuleStore, grant_store: *GrantStore, audit: *AuditRing, llm: *LLMEngine) CycleResult;

// ============================================================
// src/llm/model.zig
// ============================================================

pub const LayerWeights = struct {
    ln1_gamma: []Q16,
    ln1_beta: []Q16,
    qkv_weights: []Q16,
    out_proj: []Q16,
    ln2_gamma: []Q16,
    ln2_beta: []Q16,
    mlp_up: []Q16,
    mlp_down: []Q16,
};

pub const ModelConfig = struct {
    n_layers: i32,
    d_model: i32,
    n_heads: i32,
    d_head: i32,
    vocab_size: i32,
    mlp_dim: i32,
};

pub const Model = struct {
    config: ModelConfig,
    embedding: []Q16,
    layers: []LayerWeights,
    ln_final_gamma: []Q16,
    ln_final_beta: []Q16,
    lm_head: []Q16,

    pub fn init(config: ModelConfig) Model;
    pub fn deinit(self: *Model) void;
    pub fn loadCheckpoint(self: *Model, path: []const u8) VlpStatus;
    pub fn totalParams(self: *const Model) i64;
};

// ============================================================
// src/llm/forward.zig
// ============================================================

pub fn forward(model: *const Model, input_ids: []const i32, kv_cache: ?*KVCache, logits: []Q16) void;
pub fn layerNorm(input: []const Q16, gamma: []const Q16, beta: []const Q16, output: []Q16) void;

// ============================================================
// src/llm/softmax.zig
// ============================================================

pub fn softmaxSurrogate(logits: []const Q16, probs: []Q16) void;

// ============================================================
// src/llm/attention.zig
// ============================================================

pub const AttentionConfig = struct {
    n_heads: i32,
    d_head: i32,
    seq_len: i32,
    causal_mask: bool,
};

pub fn attention(Q: []const Q16, K: []const Q16, V: []const Q16, config: AttentionConfig, output: []Q16) void;

// ============================================================
// src/llm/kv_cache.zig
// ============================================================

pub const KVCache = struct {
    kb_id: i32,
    n_layers: i32,
    max_seq_len: i32,
    n_heads: i32,
    d_head: i32,
    store: *KBStore,

    pub fn init(session_store: *KBStore, config: KVCacheConfig) KVCache;
    pub fn append(self: *KVCache, layer: i32, position: i32, k_vec: []const Q16, v_vec: []const Q16) void;
    pub fn loadRange(self: *KVCache, layer: i32, start_pos: i32, end_pos: i32, k_out: []Q16, v_out: []Q16) void;
    pub fn truncate(self: *KVCache, position: i32) void;
    pub fn currentLength(self: *const KVCache) i32;
};

pub const KVCacheConfig = struct {
    n_layers: i32,
    max_seq_len: i32,
    n_heads: i32,
    d_head: i32,
    parent_kb_id: i32,
};

// ============================================================
// src/llm/generate.zig
// ============================================================

pub fn generateToken(model: *const Model, kv_cache: *KVCache, sampling_config: *const SamplingConfig) i32;
pub fn generateCommand(model: *const Model, kv_cache: *KVCache, store: *KBStore, command_out: *VlpCommand, tokens_used: *i32) VlpStatus;
pub fn generateProse(model: *const Model, kv_cache: *KVCache, max_tokens: i32, output_ids: []i32) i32;

// ============================================================
// src/llm/sampling.zig
// ============================================================

pub const SamplingConfig = struct {
    temperature: Q16 = Q16{ .v = 65536, .r0 = 0 },
    top_k: i32 = 50,
    top_p: Q16 = Q16{ .v = 58982, .r0 = 0 },
    greedy: bool = false,
};

pub fn sampleGreedy(probs: []const Q16) i32;
pub fn sampleTopK(probs: []const Q16, k: i32, rng: *RNG) i32;
pub fn sampleTopP(probs: []const Q16, p_threshold: Q16, rng: *RNG) i32;
pub fn applyTemperature(logits: []const Q16, temperature: Q16, output: []Q16) void;

pub const RNG = struct {
    state: i64,
    pub fn init(seed: i64) RNG;
    pub fn next(self: *RNG) i32;
};

// ============================================================
// src/llm/model.zig (supplement)
// ============================================================

pub const LLMEngine = struct {
    model: Model,
    kv_cache: KVCache,
    sampling_config: SamplingConfig,
    scratchpad: Scratchpad,

    pub fn init(model_config: ModelConfig, kv_config: KVCacheConfig, store: *KBStore) LLMEngine;
    pub fn deinit(self: *LLMEngine) void;
};

// ============================================================
// src/builtins/dispatch.zig
// ============================================================

pub const BuiltinEntry = struct {
    id: i32,
    name: []const u8,
    fn_ptr: *const fn (*BuiltinArgs) BuiltinResult,
    pure: bool,
};

pub const BuiltinArgs = struct {
    store: *KBStore,
    input_facts: [8]VlpFact,
    input_count: i32,
    target_kb_id: i32,
    target_slot_id: i32,
};

pub const BuiltinResult = struct {
    status: VlpStatus,
    output_fact: VlpFact,
    output_kb_id: i32,
    output_slot_id: i32,
};

pub const BuiltinTable = struct {
    entries: [488]?BuiltinEntry,
    count: i32,

    pub fn init() BuiltinTable;
    pub fn dispatch(self: *const BuiltinTable, id: i32, args: *BuiltinArgs) BuiltinResult;
    pub fn lookup(self: *const BuiltinTable, name: []const u8) ?i32;
};

// ============================================================
// src/builtins/text.zig
// ============================================================

pub fn textReverse(input: []const u8, output: []u8) i32;
pub fn textSplit(input: []const u8, delimiter: u8, parts: [][]const u8) i32;
pub fn textContains(haystack: []const u8, needle: []const u8) bool;
pub fn textReplace(input: []const u8, old: []const u8, new: []const u8, output: []u8) i32;
pub fn textJoin(parts: []const []const u8, separator: []const u8, output: []u8) i32;
pub fn textTrim(input: []const u8, output: []u8) i32;
pub fn textUpper(input: []u8) void;
pub fn textLower(input: []u8) void;
pub fn textStartsWith(input: []const u8, prefix: []const u8) bool;
pub fn textEndsWith(input: []const u8, suffix: []const u8) bool;
pub fn textIndexOf(haystack: []const u8, needle: []const u8) i32;
pub fn textSubstring(input: []const u8, start: i32, end: i32, output: []u8) i32;
pub fn textRepeat(input: []const u8, count: i32, output: []u8) i32;
pub fn textPadLeft(input: []const u8, width: i32, pad_char: u8, output: []u8) i32;
pub fn textPadRight(input: []const u8, width: i32, pad_char: u8, output: []u8) i32;
pub fn textCharAt(input: []const u8, index: i32) ?u8;
pub fn textLength(input: []const u8) i32;

// ============================================================
// src/builtins/arithmetic.zig
// ============================================================

pub fn arithAdd(a: Q16, b: Q16) Q16;
pub fn arithSub(a: Q16, b: Q16) Q16;
pub fn arithMul(a: Q16, b: Q16) Q16;
pub fn arithDiv(a: Q16, b: Q16) Q16;
pub fn arithPow(base: Q16, exp: i32) Q16;
pub fn arithReciprocal(a: Q16) Q16;
pub fn arithCompare(a: Q16, b: Q16) i32;
pub fn arithEqual(a: Q16, b: Q16) bool;
pub fn arithMin(a: Q16, b: Q16) Q16;
pub fn arithMax(a: Q16, b: Q16) Q16;
pub fn arithSign(a: Q16) i32;
pub fn arithIsZero(a: Q16) bool;
pub fn arithFloor(a: Q16) i32;
pub fn arithCeil(a: Q16) i32;
pub fn arithRound(a: Q16) i32;
pub fn arithNumerator(a: Q16) i32;
pub fn arithDenominator() i32;
pub fn arithAbs(a: Q16) Q16;
pub fn arithNegate(a: Q16) Q16;
pub fn arithClamp(a: Q16, min_val: Q16, max_val: Q16) Q16;
pub fn arithFromInt(val: i32) Q16;
pub fn arithToInt(a: Q16) i32;
pub fn arithLerp(a: Q16, b: Q16, t: Q16) Q16;
pub fn arithMidpoint(a: Q16, b: Q16) Q16;
pub fn arithDistance(a: Q16, b: Q16) Q16;

// ============================================================
// src/builtins/collections.zig
// ============================================================

pub fn collSort(data: []Q16) void;
pub fn collSortBy(data: []Q16, keys: []const Q16) void;
pub fn collFilter(data: []const Q16, mask: []const bool, output: []Q16) i32;
pub fn collMap(data: []const Q16, op: UnaryOp, output: []Q16) void;
pub fn collReduce(data: []const Q16, op: BinaryOp, initial: Q16) Q16;
pub fn collGroupBy(data: []const Q16, keys: []const i32, groups: []Group) i32;
pub fn collFrequencies(data: []const Q16, values: []Q16, counts: []i32) i32;
pub fn collDistinct(data: []const Q16, output: []Q16) i32;
pub fn collFlatten(arrays: []const []const Q16, output: []Q16) i32;
pub fn collChunk(data: []const Q16, chunk_size: i32, chunks: [][]const Q16) i32;
pub fn collZip(a: []const Q16, b: []const Q16, output: []Pair) i32;
pub fn collUnzip(pairs: []const Pair, a: []Q16, b: []Q16) void;
pub fn collReverse(data: []Q16) void;
pub fn collRotate(data: []Q16, amount: i32) void;
pub fn collTakeFirst(data: []const Q16, count: i32, output: []Q16) i32;
pub fn collTakeLast(data: []const Q16, count: i32, output: []Q16) i32;
pub fn collDropFirst(data: []const Q16, count: i32, output: []Q16) i32;
pub fn collDropLast(data: []const Q16, count: i32, output: []Q16) i32;
pub fn collPartition(data: []const Q16, pred: []const bool, true_out: []Q16, false_out: []Q16) struct { n_true: i32, n_false: i32 };
pub fn collInterleave(a: []const Q16, b: []const Q16, output: []Q16) i32;
pub fn collEnumerate(data: []const Q16, output: []IndexedValue) void;
pub fn collMinBy(data: []const Q16, keys: []const Q16) Q16;
pub fn collMaxBy(data: []const Q16, keys: []const Q16) Q16;
pub fn collScan(data: []const Q16, op: BinaryOp, output: []Q16) void;
pub fn collAll(preds: []const bool) bool;
pub fn collAny(preds: []const bool) bool;
pub fn collNone(preds: []const bool) bool;
pub fn collCount(preds: []const bool) i32;
pub fn collFindFirst(data: []const Q16, target: Q16) ?i32;
pub fn collFindLast(data: []const Q16, target: Q16) ?i32;
pub fn collFindAll(data: []const Q16, target: Q16, indices: []i32) i32;
pub fn collBinarySearch(sorted: []const Q16, target: Q16) ?i32;
pub fn collMerge(a: []const Q16, b: []const Q16, output: []Q16) i32;
pub fn collDeduplicate(sorted: []Q16) i32;
pub fn collWindow(data: []const Q16, window_size: i32, windows: [][]const Q16) i32;
pub fn collCartesianProduct(a: []const Q16, b: []const Q16, output: []Pair) i32;

pub const UnaryOp = enum(i8) { negate, abs_val, square, double, halve };
pub const BinaryOp = enum(i8) { add, sub, mul, min_val, max_val };
pub const Group = struct { key: i32, start: i32, count: i32 };
pub const Pair = struct { a: Q16, b: Q16 };
pub const IndexedValue = struct { index: i32, value: Q16 };

// ============================================================
// src/builtins/sets.zig
// ============================================================

pub fn setUnion(a: []const Q16, b: []const Q16, out: []Q16) i32;
pub fn setIntersection(a: []const Q16, b: []const Q16, out: []Q16) i32;
pub fn setDifference(a: []const Q16, b: []const Q16, out: []Q16) i32;
pub fn setSymmetricDiff(a: []const Q16, b: []const Q16, out: []Q16) i32;
pub fn setIsSubset(a: []const Q16, b: []const Q16) bool;
pub fn setIsSuperset(a: []const Q16, b: []const Q16) bool;
pub fn setIsDisjoint(a: []const Q16, b: []const Q16) bool;
pub fn setContains(set: []const Q16, element: Q16) bool;
pub fn setAdd(set: []Q16, set_len: *i32, element: Q16, capacity: i32) bool;
pub fn setRemove(set: []Q16, set_len: *i32, element: Q16) bool;
pub fn setEqual(a: []const Q16, b: []const Q16) bool;
pub fn setPowerSet(set: []const Q16, output: [][]Q16) i32;
pub fn setFromArray(data: []const Q16, out: []Q16) i32;

// ============================================================
// src/builtins/mappings.zig
// ============================================================

pub const MapEntry = struct { key: i32, value: VlpFact };

pub const VlpMap = struct {
    entries: []MapEntry,
    count: i32,
    capacity: i32,
};

pub fn mapGet(map: *const VlpMap, key: i32) ?VlpFact;
pub fn mapSet(map: *VlpMap, key: i32, value: VlpFact) VlpStatus;
pub fn mapDelete(map: *VlpMap, key: i32) bool;
pub fn mapContainsKey(map: *const VlpMap, key: i32) bool;
pub fn mapKeys(map: *const VlpMap, out: []i32) i32;
pub fn mapValues(map: *const VlpMap, out: []VlpFact) i32;
pub fn mapSize(map: *const VlpMap) i32;
pub fn mapMerge(a: *const VlpMap, b: *const VlpMap, out: *VlpMap, policy: VlpMergePolicy) VlpStatus;
pub fn mapFilterKeys(map: *const VlpMap, pred: []const bool, out: *VlpMap) void;
pub fn mapFilterValues(map: *const VlpMap, pred: []const bool, out: *VlpMap) void;
pub fn mapMapValues(map: *const VlpMap, op: UnaryOp, out: *VlpMap) void;
pub fn mapInvert(map: *const VlpMap, out: *VlpMap) VlpStatus;
pub fn mapClear(map: *VlpMap) void;
pub fn mapEqual(a: *const VlpMap, b: *const VlpMap) bool;
pub fn mapFromArrays(keys: []const i32, values: []const VlpFact, out: *VlpMap) VlpStatus;

// ============================================================
// src/builtins/conversion.zig
// ============================================================

pub fn parseJson(input: []const u8, store: *KBStore, target_kb_id: i32) VlpStatus;
pub fn parseCsv(input: []const u8, store: *KBStore, target_kb_id: i32, delimiter: u8) VlpStatus;
pub fn parseXml(input: []const u8, store: *KBStore, target_kb_id: i32) VlpStatus;
pub fn parseYaml(input: []const u8, store: *KBStore, target_kb_id: i32) VlpStatus;
pub fn toJson(store: *KBStore, kb_id: i32, output: []u8) i32;
pub fn toCsv(store: *KBStore, kb_id: i32, output: []u8, delimiter: u8) i32;
pub fn toFraction(num: i32, den: i32) Q16;
pub fn fromFraction(val: Q16) struct { num: i32, den: i32 };
pub fn formatNumber(val: Q16, precision: i32, output: []u8) i32;
pub fn parseNumber(input: []const u8) ?Q16;
pub fn vdrToDecimalString(val: Q16, precision: i32, output: []u8) i32;
pub fn decimalStringToVdr(input: []const u8) ?Q16;
pub fn baseConvert(value: i64, from_base: i32, to_base: i32, output: []u8) i32;
pub fn timestampToFields(ts: i32) struct { year: i32, month: i32, day: i32, hour: i32, minute: i32, second: i32 };

// ============================================================
// src/builtins/linalg.zig
// ============================================================

pub fn vecAdd(a: []const Q16, b: []const Q16, out: []Q16) void;
pub fn vecSub(a: []const Q16, b: []const Q16, out: []Q16) void;
pub fn vecScale(a: []const Q16, scalar: Q16, out: []Q16) void;
pub fn vecDot(a: []const Q16, b: []const Q16) Q16;
pub fn vecNorm(a: []const Q16) Q16;
pub fn vecNormalize(a: []const Q16, out: []Q16) void;
pub fn vecCross(a: [3]Q16, b: [3]Q16) [3]Q16;
pub fn vecLerp(a: []const Q16, b: []const Q16, t: Q16, out: []Q16) void;
pub fn vecDistance(a: []const Q16, b: []const Q16) Q16;
pub fn matMul(a: []const Q16, b: []const Q16, out: []Q16, m: i32, n: i32, k: i32) void;
pub fn matAdd(a: []const Q16, b: []const Q16, out: []Q16, rows: i32, cols: i32) void;
pub fn matSub(a: []const Q16, b: []const Q16, out: []Q16, rows: i32, cols: i32) void;
pub fn matScale(a: []const Q16, scalar: Q16, out: []Q16, rows: i32, cols: i32) void;
pub fn matTranspose(a: []const Q16, out: []Q16, rows: i32, cols: i32) void;
pub fn matInverse(a: []const Q16, out: []Q16, n: i32) VlpStatus;
pub fn matDeterminant(a: []const Q16, n: i32) Q16;
pub fn matTrace(a: []const Q16, n: i32) Q16;
pub fn matIdentity(out: []Q16, n: i32) void;
pub fn matFromRows(rows: []const []const Q16, out: []Q16, n_rows: i32, n_cols: i32) void;
pub fn matFromCols(cols: []const []const Q16, out: []Q16, n_rows: i32, n_cols: i32) void;
pub fn matGetRow(a: []const Q16, row: i32, cols: i32, out: []Q16) void;
pub fn matGetCol(a: []const Q16, col: i32, rows: i32, cols: i32, out: []Q16) void;
pub fn matGramSchmidt(vectors: []const Q16, orthogonal: []Q16, n_vectors: i32, dim: i32) void;
pub fn matSolve(a: []const Q16, b: []const Q16, x: []Q16, n: i32) VlpStatus;

// ============================================================
// src/builtins/stats.zig
// ============================================================

pub fn statsMean(data: []const Q16) Q16;
pub fn statsVariance(data: []const Q16) Q16;
pub fn statsStddev(data: []const Q16) Q16;
pub fn statsMedian(data: []const Q16, scratch: []Q16) Q16;
pub fn statsMode(data: []const Q16) Q16;
pub fn statsMin(data: []const Q16) Q16;
pub fn statsMax(data: []const Q16) Q16;
pub fn statsRange(data: []const Q16) Q16;
pub fn statsPercentile(data: []const Q16, p: Q16, scratch: []Q16) Q16;
pub fn statsCovariance(x: []const Q16, y: []const Q16) Q16;
pub fn statsCorrelation(x: []const Q16, y: []const Q16) Q16;
pub fn statsNormalize(data: []Q16) void;
pub fn statsHistogram(data: []const Q16, bins: []const Q16, counts: []i32) void;
pub fn statsBayes(prior: []const Q16, likelihood: []const Q16, evidence: Q16, posterior: []Q16) void;
pub fn statsSoftmax(logits: []const Q16, probs: []Q16) void;
pub fn statsEntropy(probs: []const Q16) Q16;

// ============================================================
// src/builtins/graph.zig
// ============================================================

pub const Edge = struct { from: i32, to: i32, weight: Q16 };

pub const Graph = struct {
    nodes: []i32,
    edges: []Edge,
    n_nodes: i32,
    n_edges: i32,
    node_capacity: i32,
    edge_capacity: i32,

    pub fn init(max_nodes: i32, max_edges: i32) Graph;
    pub fn deinit(self: *Graph) void;
};

pub fn graphAddNode(g: *Graph, node_id: i32) VlpStatus;
pub fn graphAddEdge(g: *Graph, from: i32, to: i32, weight: Q16) VlpStatus;
pub fn graphRemoveNode(g: *Graph, node_id: i32) VlpStatus;
pub fn graphRemoveEdge(g: *Graph, from: i32, to: i32) VlpStatus;
pub fn graphBFS(g: *const Graph, start: i32, visited: []i32) i32;
pub fn graphDFS(g: *const Graph, start: i32, visited: []i32) i32;
pub fn graphShortestPath(g: *const Graph, from: i32, to: i32, path: []i32, distance: *Q16) i32;
pub fn graphTopologicalSort(g: *const Graph, sorted: []i32) i32;
pub fn graphConnectedComponents(g: *const Graph, component_ids: []i32) i32;
pub fn graphCycleDetect(g: *const Graph) bool;
pub fn graphPageRankExact(g: *const Graph, n_iters: i32, ranks: []Q16) void;
pub fn graphMarkovSteady(transition: []const Q16, n: i32, steady: []Q16) void;

// ============================================================
// src/builtins/integer_ops.zig
// ============================================================

pub fn intAdd(a: i32, b: i32) i32;
pub fn intSub(a: i32, b: i32) i32;
pub fn intMul(a: i32, b: i32) i32;
pub fn intDiv(a: i32, b: i32) i32;
pub fn intMod(a: i32, b: i32) i32;
pub fn intAbs(a: i32) i32;
pub fn intSign(a: i32) i32;
pub fn intMin(a: i32, b: i32) i32;
pub fn intMax(a: i32, b: i32) i32;
pub fn intClamp(a: i32, min_val: i32, max_val: i32) i32;
pub fn intPow(base: i32, exp: i32) i32;
pub fn intFactorial(n: i32) i64;
pub fn intChoose(n: i32, k: i32) i64;
pub fn bitAnd(a: i32, b: i32) i32;
pub fn bitOr(a: i32, b: i32) i32;
pub fn bitXor(a: i32, b: i32) i32;
pub fn bitNot(a: i32) i32;
pub fn bitShl(a: i32, shift: u5) i32;
pub fn bitShr(a: i32, shift: u5) i32;
pub fn bitPopcount(a: i32) i32;
pub fn bitReverse(a: i32) i32;

// ============================================================
// src/builtins/time.zig
// ============================================================

pub fn timestampNow() i32;
pub fn timestampDiff(a: i32, b: i32) i32;
pub fn timestampAdd(ts: i32, seconds: i32) i32;
pub fn durationFromMs(ms: i64) i32;
pub fn durationFromSec(s: i32) i32;
pub fn durationToMs(d: i32) i64;
pub fn durationToSec(d: i32) i32;
pub fn formatTimestamp(ts: i32, buf: []u8) i32;
pub fn parseTimestamp(text: []const u8) ?i32;
pub fn sleepMs(ms: i32) void;

// ============================================================
// src/seed/init.zig
// ============================================================

pub fn seedInit(store: *KBStore, rule_store: *RuleStore) VlpStatus;

// ============================================================
// src/seed/oso_rules.zig
// ============================================================

pub fn loadOsoRules(store: *KBStore, rule_store: *RuleStore, oso_kb_id: i32) VlpStatus;

// ============================================================
// src/seed/hygiene_rules.zig
// ============================================================

pub fn loadHygieneRules(store: *KBStore, rule_store: *RuleStore, hygiene_kb_id: i32) VlpStatus;

// ============================================================
// src/seed/confidence_table.zig
// ============================================================

pub fn loadConfidenceTable(store: *KBStore, confidence_kb_id: i32) VlpStatus;

// ============================================================
// src/seed/command_vocab.zig
// ============================================================

pub fn loadCommandVocab(store: *KBStore, builtins_kb_id: i32) VlpStatus;

// ============================================================
// src/runner/types.zig
// ============================================================

pub const VlpRunner = struct {
    id: i32,
    runner_type: VlpRunnerType,
    state: VlpRunnerState,
    session: *VlpSession,
    store: *KBStore,
    rule_store: *RuleStore,
    grant_store: *GrantStore,
    audit: *AuditRing,
    llm: *LLMEngine,
    interval_ms: i32,
    max_turns_before_recycle: i32,
    max_consecutive_errors: i32,
    iterations_completed: i64,
    errors_consecutive: i32,
    errors_total: i64,
    last_iteration_ms: i32,
    last_iteration_timestamp: i32,
    recycle_count: i32,
    last_recycle_timestamp: i32,
    notification_kb_id: i32,
    log_kb_id: i32,
};

pub const PollerConfig = struct {
    interval_ms: i32,
    session: *VlpSession,
    store: *KBStore,
    rule_store: *RuleStore,
    grant_store: *GrantStore,
    audit: *AuditRing,
    llm: *LLMEngine,
    notification_kb_id: i32,
    max_consecutive_errors: i32 = 5,
};

pub const ProcessorConfig = struct {
    session: *VlpSession,
    store: *KBStore,
    rule_store: *RuleStore,
    grant_store: *GrantStore,
    audit: *AuditRing,
    llm: *LLMEngine,
    source_url: []const u8,
    max_turns_before_recycle: i32 = 200,
    max_consecutive_errors: i32 = 5,
    compact_rules_kb_id: i32,
    log_kb_id: i32,
};

pub const InternalConfig = struct {
    interval_ms: i32,
    session: *VlpSession,
    store: *KBStore,
    compute_fn: *const fn (*VlpSession, *KBStore) VlpStatus,
};

pub const BatchConfig = struct {
    session: *VlpSession,
    store: *KBStore,
    rule_store: *RuleStore,
    grant_store: *GrantStore,
    audit: *AuditRing,
    llm: *LLMEngine,
    task_queue_kb_id: i32,
    task_queue_name: []const u8,
    max_concurrent: i32,
};

// ============================================================
// src/runner/pool.zig
// ============================================================

pub const RunnerTask = struct {
    runner: *VlpRunner,
    action: enum(i8) { run_cycle, recycle, stop, kill, run_batch_task },
};

pub const ThreadPool = struct {
    threads: []std.Thread,
    n_threads: i32,
    task_queue: BoundedQueue,
    shutdown_flag: std.atomic.Value(i32),

    pub fn init(n_threads: i32) ThreadPool;
    pub fn deinit(self: *ThreadPool) void;
    pub fn submit(self: *ThreadPool, task: RunnerTask) VlpStatus;
    pub fn shutdown(self: *ThreadPool) void;
};

// ============================================================
// src/runner/poller.zig
// ============================================================

pub fn pollerMain(runner: *VlpRunner) void;
pub fn pollerCreate(config: PollerConfig) VlpRunner;

// ============================================================
// src/runner/processor.zig
// ============================================================

pub fn processorMain(runner: *VlpRunner) void;
pub fn processorCreate(config: ProcessorConfig) VlpRunner;
pub fn processorRecycle(runner: *VlpRunner) void;
pub fn processorReconnect(runner: *VlpRunner) VlpStatus;

// ============================================================
// src/runner/internal.zig
// ============================================================

pub fn internalMain(runner: *VlpRunner) void;
pub fn internalCreate(config: InternalConfig) VlpRunner;

// ============================================================
// src/runner/batch.zig
// ============================================================

pub fn batchMain(runner: *VlpRunner) void;
pub fn batchCreate(config: BatchConfig) VlpRunner;

// ============================================================
// src/server/types.zig
// ============================================================

pub const VlpServer = struct {
    listen_fd: i32,
    listen_port: i32,
    protocol: VlpProtocolType,
    protocol_grammar_kb_id: i32,
    max_concurrent: i32,
    template_snapshot: VlpSnapshot,
    template_session_config: SessionConfig,
    auth_kb_id: i32,
    credential_ttl: i32,
    max_session_turns: i32,
    connections: []ServerConnection,
    n_active: std.atomic.Value(i32),
    shutdown_flag: std.atomic.Value(i32),
    total_accepted: i64,
    total_rejected: i64,
    total_requests: i64,
    store: *KBStore,
    rule_store: *RuleStore,
    grant_store: *GrantStore,
    audit: *AuditRing,
    llm: *LLMEngine,
    pool: *ThreadPool,
};

pub const ServerConnection = struct {
    socket: i32,
    session: VlpSession,
    credential: ServerCredential,
    state: VlpConnectionState,
    created_at: i32,
    last_active: i32,
    requests_served: i32,
    output_buf: [65536]u8,
};

pub const ServerCredential = struct {
    user_id: i32,
    visibility_level: VlpVisibility,
    grants: [16]VlpGrant,
    n_grants: i32,
    issued_at: i32,
    expires_at: i32,
    valid: bool,
};

pub const ServerConfig = struct {
    port: i32,
    protocol: VlpProtocolType,
    max_connections: i32,
    credential_ttl: i32,
    max_session_turns: i32,
    idle_timeout: i32 = 300,
    persistent_sessions: bool = false,
    template_snapshot_path: ?[]const u8 = null,
    auth_kb_id: i32,
    backlog: i32 = 128,
};

pub const HealthReport = struct {
    active_connections: i32,
    total_requests: i64,
    active_sessions: i32,
    total_facts: i64,
    total_rules: i32,
    l1_count: i64,
    l2_count: i64,
    l3_count: i64,
    runner_count: i32,
};

pub const RateLimitResult = struct {
    allowed: bool,
    remaining: i32,
    retry_after: i32,
};

// ============================================================
// src/server/listener.zig
// ============================================================

pub fn serverInit(config: ServerConfig, store: *KBStore, rule_store: *RuleStore, grant_store: *GrantStore, audit: *AuditRing, llm: *LLMEngine, pool: *ThreadPool) VlpServer;
pub fn serverAcceptLoop(server: *VlpServer) void;

// ============================================================
// src/server/handler.zig
// ============================================================

pub fn handleConnection(server: *VlpServer, conn: *ServerConnection) void;
pub fn closeConnection(server: *VlpServer, conn: *ServerConnection) void;

// ============================================================
// src/server/auth.zig
// ============================================================

pub fn authenticate(server: *VlpServer, token: []const u8) ?ServerCredential;
pub fn credentialCheck(credential: *ServerCredential, now: i32) bool;
pub fn credentialRevoke(credential: *ServerCredential) void;
pub fn credentialCleanup(server: *VlpServer, now: i32) i32;

// ============================================================
// src/server/rate_limit.zig
// ============================================================

pub const RateLimiter = struct {
    counter_kb_id: i32,
    window_seconds: i32,
    max_requests: i32,

    pub fn init(counter_kb_id: i32, window_seconds: i32, max_requests: i32) RateLimiter;
    pub fn check(self: *RateLimiter, store: *KBStore, user_id: i32, now: i32) RateLimitResult;
};

// ============================================================
// src/server/health.zig
// ============================================================

pub fn healthCheck(server: *VlpServer) HealthReport;
pub fn metricsEndpoint(server: *VlpServer, output: []u8) i32;

// ============================================================
// src/server/reaper.zig
// ============================================================

pub fn reaperScan(server: *VlpServer, now: i32, idle_timeout: i32) i32;

// ============================================================
// src/server/shutdown.zig
// ============================================================

pub fn serverShutdown(server: *VlpServer, timeout_seconds: i32) VlpStatus;

// ============================================================
// src/protocol/http.zig
// ============================================================

pub const HttpRequest = struct {
    method: enum(i8) { get, post, put, delete, head, options, unknown },
    path: []const u8,
    content_length: i32,
    keepalive: bool,
    auth_header: []const u8,
    content_type: enum(i8) { json, form, text, unknown },
    body: []const u8,
};

pub const HttpResponse = struct {
    buf: []u8,
    len: i32,
};

pub fn httpReadRequest(socket: i32, request: *HttpRequest, timeout_ms: i32) VlpStatus;
pub fn httpBuildResponse(output: *const VlpOutputBuffer, request: *const HttpRequest, grammar_kb_id: i32, store: *KBStore, response: *HttpResponse) VlpStatus;
pub fn httpSendResponse(socket: i32, response: *const HttpResponse) VlpStatus;
pub fn httpSendError(socket: i32, status_code: i32, message: []const u8) void;

// ============================================================
// src/protocol/websocket.zig
// ============================================================

pub const WsFrame = struct {
    opcode: enum(i8) { text, binary, ping, pong, close },
    payload: []u8,
    payload_len: i32,
};

pub fn wsUpgrade(socket: i32, request: *const HttpRequest) VlpStatus;
pub fn wsReadFrame(socket: i32, frame: *WsFrame, timeout_ms: i32) VlpStatus;
pub fn wsSendText(socket: i32, payload: []const u8) VlpStatus;
pub fn wsSendClose(socket: i32, code: i32, reason: []const u8) VlpStatus;
pub fn wsSendPong(socket: i32, payload: []const u8) VlpStatus;
pub fn wsHandleLoop(server: *VlpServer, conn: *ServerConnection) void;

// ============================================================
// src/protocol/smtp.zig
// ============================================================

pub fn smtpGreeting(socket: i32, hostname: []const u8) VlpStatus;
pub fn smtpReadCommand(socket: i32, buf: []u8, timeout_ms: i32) i32;
pub fn smtpSendResponse(socket: i32, code: i32, message: []const u8) VlpStatus;

// ============================================================
// src/protocol/mqtt.zig
// ============================================================

pub fn mqttReadConnect(socket: i32, client_id: []u8, username: []u8, password: []u8) VlpStatus;
pub fn mqttSendConnack(socket: i32, return_code: i32) VlpStatus;
pub fn mqttReadPublish(socket: i32, topic: []u8, payload: []u8) VlpStatus;

// ============================================================
// src/protocol/grammars.zig
// ============================================================

pub fn initProtocolGrammars(store: *KBStore, grammar_kb_id: i32, protocol: VlpProtocolType) VlpStatus;

// ============================================================
// src/ops/filesystem.zig
// ============================================================

pub fn fsRead(path: []const u8, store: *KBStore, target_kb_id: i32, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn fsWrite(path: []const u8, store: *KBStore, source_kb_id: i32, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn fsAppend(path: []const u8, data: []const u8, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn fsDelete(path: []const u8, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn fsStat(path: []const u8, grant_store: *GrantStore, user_id: i32) ?struct { size: i64, modified: i32 };

// ============================================================
// src/ops/network.zig
// ============================================================

pub fn netFetch(url: []const u8, method: []const u8, headers: []const u8, body: []const u8, store: *KBStore, target_kb_id: i32, grant_store: *GrantStore, user_id: i32) VlpStatus;

// ============================================================
// src/ops/execute.zig
// ============================================================

pub fn execRun(command: []const u8, args: []const []const u8, store: *KBStore, target_kb_id: i32, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn execRunAsync(command: []const u8, args: []const []const u8, grant_store: *GrantStore, user_id: i32) ?i32;

// ============================================================
// src/ops/compile_op.zig
// ============================================================

pub fn compileCheck(path: []const u8, grant_store: *GrantStore, user_id: i32) VlpStatus;

// ============================================================
// src/ops/process.zig
// ============================================================

pub fn procStart(command: []const u8, args: []const []const u8, grant_store: *GrantStore, user_id: i32) ?i32;
pub fn procKill(pid: i32, grant_store: *GrantStore, user_id: i32) VlpStatus;
pub fn procStatus(pid: i32) ?struct { running: bool, exit_code: i32 };

// ============================================================
// src/config/system_config.zig
// ============================================================

pub const SystemConfig = struct {
    model: ModelConfig,
    model_checkpoint_path: []const u8,
    server: ServerConfig,
    seed_snapshot_path: []const u8,
    max_kbs: i32 = 100_000,
    max_facts: i64 = 10_000_000,
    max_rules: i32 = 100_000,
    max_text_bytes: i64 = 100 * 1024 * 1024,
    max_concurrent_sessions: i32 = 10_000,
    max_runners: i32 = 64,
    audit_capacity: i32 = 1_000_000,

    pub fn defaults() SystemConfig;
};

// ============================================================
// src/config/cli.zig
// ============================================================

pub const CliArgs = struct {
    config_path: []const u8,
    port_override: ?i32,
    shutdown: bool,
};

pub fn parseCli(argv: []const []const u8) CliArgs;

// ============================================================
// src/config/config_file.zig
// ============================================================

pub fn parseConfigFile(path: []const u8, config: *SystemConfig) VlpStatus;

// ============================================================
// src/gpu/device.zig
// ============================================================

pub const DeviceProps = struct {
    n_sms: i32,
    max_shared_mem: i32,
    global_mem_bytes: i64,
    clock_hz: i32,
    has_int8_tensor: bool,
};

pub const DeviceMemoryLayout = struct {
    model_weights_base: i64,
    model_weights_size: i64,
    kb_store_base: i64,
    kb_store_size: i64,
    fact_store_base: i64,
    fact_store_size: i64,
    rule_store_base: i64,
    rule_store_size: i64,
    term_store_base: i64,
    term_store_size: i64,
    text_store_base: i64,
    text_store_size: i64,
    grammar_store_base: i64,
    grammar_store_size: i64,
    live_state_base: i64,
    live_state_size: i64,
    scratch_base: i64,
    scratch_size: i64,
    audit_base: i64,
    audit_size: i64,
};

pub fn deviceInit(device_id: i32) ?DeviceProps;
pub fn deviceAllocLayout(props: DeviceProps, config: SystemConfig) ?DeviceMemoryLayout;
pub fn deviceFreeLayout(layout: *DeviceMemoryLayout) void;
pub fn deviceSynchronize() void;

// ============================================================
// src/gpu/kb_device.zig
// ============================================================

pub fn deviceFactWrite(layout: *const DeviceMemoryLayout, kb_id: i32, slot_id: i32, fact: *const VlpFact) VlpStatus;
pub fn deviceFactRead(layout: *const DeviceMemoryLayout, kb_id: i32, slot_id: i32) ?VlpFact;

// ============================================================
// src/gpu/transfer.zig
// ============================================================

pub fn hostToDevice(host_ptr: [*]const u8, device_offset: i64, bytes: i64) VlpStatus;
pub fn deviceToHost(device_offset: i64, host_ptr: [*]u8, bytes: i64) VlpStatus;
pub fn deviceToDevice(src_offset: i64, dst_offset: i64, bytes: i64) VlpStatus;
pub fn transferQ16Array(host: []const Q16, device_offset: i64) VlpStatus;
pub fn transferQ16ArrayBack(device_offset: i64, host: []Q16) VlpStatus;

// ============================================================
// src/gpu/kernel_mac.zig
// ============================================================

pub fn launchQ16Gemm(a_offset: i64, b_offset: i64, c_offset: i64, m: i32, n: i32, k: i32) VlpStatus;

// ============================================================
// src/gpu/kernel_softmax.zig
// ============================================================

pub fn launchQ16Softmax(input_offset: i64, output_offset: i64, n: i32) VlpStatus;

// ============================================================
// src/gpu/kernel_attention.zig
// ============================================================

pub fn launchQ16Attention(q_offset: i64, k_offset: i64, v_offset: i64, out_offset: i64, config: AttentionConfig) VlpStatus;

// ============================================================
// src/gpu/kernel_layernorm.zig
// ============================================================

pub fn launchQ16LayerNorm(input_offset: i64, gamma_offset: i64, beta_offset: i64, output_offset: i64, n: i32) VlpStatus;

// ============================================================
// src/gpu/kernel_elementwise.zig
// ============================================================

pub fn launchQ16Add(a_offset: i64, b_offset: i64, out_offset: i64, n: i32) VlpStatus;
pub fn launchQ16Sub(a_offset: i64, b_offset: i64, out_offset: i64, n: i32) VlpStatus;
pub fn launchQ16Mul(a_offset: i64, b_offset: i64, out_offset: i64, n: i32) VlpStatus;
pub fn launchQ16Scale(input_offset: i64, scalar: Q16, out_offset: i64, n: i32) VlpStatus;
pub fn launchQ16Compare(a_offset: i64, b_offset: i64, out_offset: i64, n: i32) VlpStatus;

// ============================================================
// src/gpu/kernel_prolog.zig
// ============================================================

pub fn launchPrologUnify(facts_offset: i64, n_facts: i32, query_term: VlpTerm, matches_offset: i64, n_matches: *i32) VlpStatus;

// ============================================================
// src/gpu/kernel_sort.zig
// ============================================================

pub fn launchQ16Sort(data_offset: i64, n: i32) VlpStatus;

// ============================================================
// src/gpu/profiling.zig
// ============================================================

pub const KernelStats = struct {
    elapsed_ns: i64,
    ops_count: i64,
    memory_bytes: i64,
};

pub fn profilingStart() void;
pub fn profilingStop() void;
pub fn profilingGetKernelStats() KernelStats;
pub fn profilingVerifyDeterminism(launch_fn: *const fn () VlpStatus, n_runs: i32, output_offset: i64, output_bytes: i64) bool;

// ============================================================
// src/deploy/gcp_setup.zig
// ============================================================

pub fn gcpCreateInstance(name: []const u8, machine_type: []const u8, gpu_type: []const u8, gpu_count: i32) VlpStatus;
pub fn gcpStartInstance(name: []const u8) VlpStatus;
pub fn gcpStopInstance(name: []const u8) VlpStatus;
pub fn gcpDeleteInstance(name: []const u8) VlpStatus;

// ============================================================
// src/deploy/multi_device.zig
// ============================================================

pub const ModelParallel = struct {
    n_devices: i32,
    layer_assignment: []i32,
    layouts: []DeviceMemoryLayout,

    pub fn init(n_devices: i32, config: ModelConfig) ModelParallel;
    pub fn deinit(self: *ModelParallel) void;
    pub fn pipelineForward(self: *ModelParallel, input_ids: []const i32, logits: []Q16) VlpStatus;
};

// ============================================================
// src/deploy/distributed.zig
// ============================================================

pub const Comm = struct {
    n_ranks: i32,
    rank: i32,

    pub fn init(n_ranks: i32, rank: i32) Comm;
};

pub fn allReduce(sendbuf: []const Q16, recvbuf: []Q16, op: VlpReduceOp, comm: *Comm) VlpStatus;
pub fn broadcast(buf: []Q16, root: i32, comm: *Comm) VlpStatus;
pub fn allGather(sendbuf: []const Q16, recvbuf: []Q16, comm: *Comm) VlpStatus;
pub fn reduceScatter(sendbuf: []const Q16, recvbuf: []Q16, op: VlpReduceOp, comm: *Comm) VlpStatus;
pub fn kbSync(store: *KBStore, kb_id: i32, comm: *Comm) VlpStatus;
pub fn snapshotBroadcast(snapshot: *VlpSnapshot, root: i32, comm: *Comm) VlpStatus;

// ============================================================
// src/deploy/load_balancer.zig
// ============================================================

pub const LoadBalancer = struct {
    instances: [][]const u8,
    n_instances: i32,
    next_index: i32,

    pub fn init(instances: []const []const u8) LoadBalancer;
    pub fn route(self: *LoadBalancer) []const u8;
    pub fn removeUnhealthy(self: *LoadBalancer, instance: []const u8) void;
};

// ============================================================
// src/deploy/monitoring.zig
// ============================================================

pub fn prometheusExport(server: *VlpServer, output: []u8) i32;
```
