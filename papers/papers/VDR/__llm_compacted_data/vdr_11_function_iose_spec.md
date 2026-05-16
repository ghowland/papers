# VDR-11 FUNCTION IOSE SPEC — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: enums → structs → functions → relationships → section_index → decode_legend

# enums(id|name|values)
EN1|RemainderForm|zero, atomic, composite, functional
EN2|Visibility|public, internal, owner_only
EN3|MountMode|read_only, read_write, snapshot, mirror
EN4|Direction|inbound, outbound
EN5|IOSECategory|pure, operational, composite
EN6|LogicType|operational, application
EN7|CommandType|pure_fn, op_fn, kb_assert, kb_retract, kb_query, env_exec, env_upload, env_download, ctx_activate, ctx_deactivate, ctx_snapshot, version_create, store_result, direct_output, attachment
EN8|ArgType|path_ref, literal_int, literal_text, literal_bool, literal_fraction
EN9|InferenceMode|deductive, inductive, abductive, analogical
EN10|NotebookStatus|active, concluded, halted, archived
EN11|LoopPhase|assess, formalize, execute, store, branch, backtrack, conclude, halt
EN12|GrantStatus|active, expired, revoked, exhausted
EN13|EnvType|local, docker, ssh, vm
EN14|EnvStatus|stopped, starting, running, error
EN15|TaskStatus|pending, running, completed, failed, killed

# structs(id|name|fields|notes)
ST1|VDRFraction|v:int, d:int, r:Any(0/int/CompositeRemainder/FnRemainder)|ground truth numeric type
ST2|CompositeRemainder|base:int, children:List[VDRFraction]|
ST3|FnRemainder|name:str, fn:Callable[[int]→VDRFraction], metadata:Dict|
ST4|QBasis|numerator:int, exponent:int|value = numerator / 2^exponent
ST5|Vec|elements:List[VDRFraction]|
ST6|Mat|rows:List[Vec]|
ST7|Fact|predicate:str, args:List[Any], kb_source:str, asserted_at:int, derivation:Optional[Dict]|
ST8|Rule|head:Fact, body:List[Fact], kb_source:str|
ST9|Constraint|name, scope:str, status:str, condition:str(Prolog), on_violation:str, source:str|
ST10|Connection|target_id:int, target_path:str, relationship:str, direction:Direction, phase:str, created_at:int, notes:str|
ST11|Mount|mount_path, source_path, source_id:int, mode:MountMode, created_at:int, created_by:str|
ST12|Counter|value:int=0, min_value:int=0, max_value:int=2^31-1, created_at:int|
ST13|LockState|held:bool=F, holder:Optional[str], acquired_at:Optional[int], notes:str|
ST14|BoundedQueue|capacity:int=50, items:List, created_at:int|
ST15|BoundedStack|capacity:int=30, items:List, created_at:int|
ST16|RingBuffer|capacity:int=100, items:List, write_pos:int, count:int, created_at:int|
ST17|LRUCache|capacity:int=50, entries:Dict[str,Any], access_order:List[str], created_at:int|
ST18|Bitset|width:int=100, bits:List[bool], created_at:int|
ST19|KnowledgeBase|name,path,id, facts,rules,constraints,connections, working_data,lrus,counters,locks,queues,stacks,buffers,bitsets, parent_id,children_ids,mounts, visibility,frozen,owner,created_at,last_modified|25 fields across identity/persistent/live/structural/metadata
ST20|IOSEProperty|name:str, value:Any=True|
ST21|IOSEDeclaration|name, inputs:List[str], outputs:List[str], side_effects:List[str], properties:List[IOSEProperty], category:IOSECategory, logic_type:LogicType, description:str|
ST22|BuiltinDef|id:int, name:str, category:str, iose:IOSEDeclaration, implementation:Callable|
ST23|CommandArg|arg_type:ArgType, value:Any|
ST24|CommandToken|cmd_type:CommandType, primitive_name:str, args:List[CommandArg], env:str, grant:str, store_result:str, await_result:bool|
ST25|KBLiveState|kb_id:int + 8 live-state dicts deep-copied from KB|persistent facts NOT included
ST26|SessionSnapshot|name, path, created_at, active_scope:List[int], active_topic:int, scratchpad:Optional[RingBuffer], kb_states:Dict[int,KBLiveState], turn_count, notes|
ST27|InferenceConclusion|statement:Fact, mode:InferenceMode, confidence:VDRFraction, derived_from:List, via_rules:List, via_tools:List, alternatives:List, steps_taken:int, backtracks:int|
ST28|InferenceNotebook|kb:KnowledgeBase, problem_statement, mode:InferenceMode, goal, status:NotebookStatus, conclusion:Optional[InferenceConclusion], max_steps:50, max_queries:20, stall_threshold:5|
ST29|ResourceLimits|max_cpu_seconds:3600, max_memory_mb:2048, max_disk_mb:10240, max_processes:100|
ST30|OperationalEnv|id, env_type:EnvType, status:EnvStatus, working_dir, env_vars:Dict, resource_limits:ResourceLimits, kb_path, docker_image, ssh_host, ssh_port:22, ssh_user|
ST31|Grant|name, operation_class, allowed_operations:List, location, issued_by, issued_at, expires_at:2^31-1, max_uses:int(0=unlimited), uses_remaining, status:GrantStatus|
ST32|Task|id, operation, args:List, env, grant, status:TaskStatus, submitted_at, completed_at, result:Any, stdout, stderr|
ST33|ExecResult|exit_code:int, stdout:str, stderr:str, duration_ms:int|
ST34|Binding|bindings:Dict[str,Any]; methods: get, bind(→new Binding), merge(→Optional[Binding])|
ST35|ScopeChain|chain:List[int](current→root), secondary:List[int]|
ST36|PathRegistry|path_to_id:Dict[str,int], id_to_path:List[str], next_id:int; retired IDs never reused|
ST37|BuiltinRegistry|_by_id:Dict[int,BuiltinDef], _by_name:Dict[str,BuiltinDef]|
ST38|GrantStore|grants storage; hierarchy-aware verification|
ST39|Scratchpad|buffer:RingBuffer, path:str|RingBuffer-based internal channel

# functions(id|module|name|inputs|outputs|side_effects|properties|stage|notes)
# --- STAGE 1: core/types.py ---
F001|core/types|promote_integer|int|VDRFraction(v=val,d=1,r=0)|none|pure,lossless|S1|
F002|core/types|promote_qbasis|QBasis|VDRFraction(v=num,d=2^exp,r=0)|none|pure,lossless|S1|
F003|core/types|dispatch_arithmetic|left:Any,right:Any,op:str|Tuple[path_tag,promoted_l,promoted_r]|none|pure|S1|integer/VDR/Q-basis path selection
F004|core/types|is_closed|VDRFraction|bool|none|pure|S1|
F005|core/types|is_integer|VDRFraction|bool|none|pure|S1|
# --- core/errors.py ---
F006|core/errors|VDRError(class)|-|-|-|-|S1|fields: code,message,context
F007|core/errors|Result(class)|-|-|-|-|S1|Ok/Err wrapper; methods: unwrap,unwrap_or,map
# --- kb/knowledge_base.py ---
F008|kb/knowledge_base|create_kb|name,path,parent_id?,owner?|KnowledgeBase|kb_store_add,parent_children_update|deterministic|S1|assigns next ID
F009|kb/knowledge_base|get_kb|identifier:int_or_str|Optional[KnowledgeBase]|none|pure|S1|
F010|kb/knowledge_base|delete_kb|kb_id:int|bool|kb_store_remove,parent_children_update,id_retired|deterministic|S1|no cascade; orphans detected by constraint
# --- kb/fact_store.py ---
F011|kb/fact_store|assert_fact|kb,fact|bool(T=new,F=existed)|kb.facts_modify,kb.last_modified_update|idempotent,deterministic|S1|
F012|kb/fact_store|retract_fact|kb,predicate,args|bool(T=removed,F=absent)|kb.facts_modify,kb.last_modified_update|idempotent,deterministic|S1|
F013|kb/fact_store|query_facts|kb,predicate,args(None=wildcard)|List[Fact]|none|pure|S1|
F014|kb/fact_store|fact_exists|kb,fact|bool|none|pure|S1|
# --- kb/rule_engine.py ---
F015|kb/rule_engine|unify|term_a,term_b,bindings:Binding|Optional[Binding]|none|pure|S1|handles atoms/vars/VDR/lists/facts
F016|kb/rule_engine|substitute|term,bindings|term_with_vars_replaced|none|pure|S1|
F017|kb/rule_engine|query_rules|kb,goal:Fact,max_depth:100|List[Binding]|none|pure|S1|depth-first+backtracking, all solutions
F018|kb/rule_engine|query_rules_first|kb,goal:Fact,max_depth|Optional[Binding]|none|pure|S1|cut after first match
# --- kb/working_data.py ---
F019|kb/working_data|set_binding|kb,key,value,turn|None|kb.working_data_modify,kb.last_modified_update|-|S1|
F020|kb/working_data|get_binding|kb,key,kb_store|Optional[Any]|none|pure|S1|walks parent chain
F021|kb/working_data|get_binding_local|kb,key|Optional[Any]|none|pure|S1|no inheritance
F022|kb/working_data|delete_binding|kb,key|bool|kb.working_data_modify|-|S1|
F023|kb/working_data|list_visible_bindings|kb,kb_store|Dict[str,Any]|none|pure|S1|local shadows parent
# --- primitives/arithmetic.py (8 builtins wrapping vdr.py) ---
F024|primitives/arithmetic|vdr_add|a:VDRFraction,b:VDRFraction|VDRFraction|none|pure,deterministic,bounded,commutative,associative|S1|
F025|primitives/arithmetic|vdr_sub|a:VDRFraction,b:VDRFraction|VDRFraction|none|pure,deterministic,bounded|S1|
F026|primitives/arithmetic|vdr_mul|a:VDRFraction,b:VDRFraction|VDRFraction|none|pure,deterministic,bounded,commutative,associative|S1|
F027|primitives/arithmetic|vdr_div|a:VDRFraction,b:VDRFraction|Result[VDRFraction]|none|pure,deterministic,partial(b.v=0)|S1|
F028|primitives/arithmetic|vdr_neg|a:VDRFraction|VDRFraction|none|pure,deterministic,invertible|S1|
F029|primitives/arithmetic|vdr_abs|a:VDRFraction|VDRFraction|none|pure,deterministic,idempotent|S1|
F030|primitives/arithmetic|vdr_pow|a:VDRFraction,n:int|VDRFraction|none|pure,deterministic|S1|
F031|primitives/arithmetic|vdr_reciprocal|a:VDRFraction|Result[VDRFraction]|none|pure,deterministic,partial(a.v=0),invertible|S1|
# --- primitives/comparison.py (10) ---
F032|primitives/comparison|vdr_compare|a,b:VDRFraction|str(less/equal/greater)|none|pure,deterministic|S1|cross-multiplication
F033|primitives/comparison|vdr_equal|a,b|bool|none|pure,commutative|S1|
F034|primitives/comparison|vdr_less_than|a,b|bool|none|pure|S1|
F035|primitives/comparison|vdr_less_equal|a,b|bool|none|pure|S1|
F036|primitives/comparison|vdr_min|a,b|VDRFraction|none|pure,commutative,associative,idempotent|S1|
F037|primitives/comparison|vdr_max|a,b|VDRFraction|none|pure,commutative,associative,idempotent|S1|
F038|primitives/comparison|vdr_sign|a|int(-1/0/1)|none|pure|S1|
F039|primitives/comparison|vdr_is_zero|a|bool|none|pure|S1|
F040|primitives/comparison|vdr_is_positive|a|bool|none|pure|S1|
F041|primitives/comparison|vdr_is_negative|a|bool|none|pure|S1|
# --- primitives/rounding.py (7) ---
F042|primitives/rounding|vdr_floor|a:VDRFraction|int|none|pure|S1|
F043|primitives/rounding|vdr_ceil|a:VDRFraction|int|none|pure|S1|
F044|primitives/rounding|vdr_round|a:VDRFraction|int|none|pure|S1|
F045|primitives/rounding|vdr_truncate|a:VDRFraction|int|none|pure|S1|
F046|primitives/rounding|vdr_numerator|a:VDRFraction|int|none|pure|S1|after normalization
F047|primitives/rounding|vdr_denominator|a:VDRFraction|int|none|pure|S1|after normalization
F048|primitives/rounding|vdr_simplify|a:VDRFraction|VDRFraction|none|pure,idempotent|S1|
# --- primitives/list_aggregates.py (8) ---
F049|primitives/list_aggregates|vdr_sum|List[VDRFraction]|VDRFraction|none|pure,commutative,associative|S1|empty→[0,1,0]
F050|primitives/list_aggregates|vdr_product|List[VDRFraction]|VDRFraction|none|pure,commutative,associative|S1|empty→[1,1,0]
F051|primitives/list_aggregates|vdr_mean|List[VDRFraction]|Result[VDRFraction]|none|pure,partial(empty)|S1|
F052|primitives/list_aggregates|vdr_dot_product|a,b:List[VDRFraction]|Result[VDRFraction]|none|pure,partial(len_mismatch),commutative|S1|
F053|primitives/list_aggregates|vdr_sum_of_squares|List[VDRFraction]|VDRFraction|none|pure|S1|
F054|primitives/list_aggregates|vdr_weighted_sum|weights,values:List[VDRFraction]|Result[VDRFraction]|none|pure,partial(len_mismatch)|S1|
F055|primitives/list_aggregates|vdr_harmonic_sum|n:int|VDRFraction|none|pure|S1|H_n = 1+1/2+...+1/n
F056|primitives/list_aggregates|vdr_alternating_sum|List[VDRFraction]|VDRFraction|none|pure|S1|
# --- primitives/text.py (17) ---
F057|primitives/text|string_reverse|s|str|none|pure,invertible|S1|
F058|primitives/text|string_length|s|int|none|pure|S1|
F059|primitives/text|string_concat|a,b|str|none|pure,associative|S1|
F060|primitives/text|string_split|s,delim|List[str]|none|pure|S1|
F061|primitives/text|string_slice|s,start,end|str|none|pure|S1|
F062|primitives/text|string_char_at|s,idx|Result[str]|none|pure,partial|S1|
F063|primitives/text|string_to_chars|s|List[str]|none|pure|S1|
F064|primitives/text|chars_to_string|chars|str|none|pure|S1|
F065|primitives/text|string_contains|s,sub|bool|none|pure|S1|
F066|primitives/text|string_starts_with|s,prefix|bool|none|pure|S1|
F067|primitives/text|string_ends_with|s,suffix|bool|none|pure|S1|
F068|primitives/text|string_upper|s|str|none|pure,idempotent|S1|
F069|primitives/text|string_lower|s|str|none|pure,idempotent|S1|
F070|primitives/text|string_trim|s|str|none|pure,idempotent|S1|
F071|primitives/text|string_replace|s,old,new|str|none|pure|S1|
F072|primitives/text|string_join|items,delim|str|none|pure|S1|
F073|primitives/text|string_pad_left|s,width,fill|str|none|pure|S1|
# --- primitives/collections.py (36) ---
F074|primitives/collections|list_append|lst,item|list|none|pure|S1|
F075|primitives/collections|list_prepend|item,lst|list|none|pure|S1|
F076|primitives/collections|list_concat|a,b|list|none|pure|S1|
F077|primitives/collections|list_enumerate|lst|List[Tuple]|none|pure|S1|
F078|primitives/collections|list_length|lst|int|none|pure|S1|
F079|primitives/collections|list_head|lst|Result[Any]|none|pure,partial(empty)|S1|
F080|primitives/collections|list_tail|lst|Result[list]|none|pure,partial(empty)|S1|
F081|primitives/collections|list_last|lst|Result[Any]|none|pure,partial(empty)|S1|
F082|primitives/collections|list_init|lst|Result[list]|none|pure,partial(empty)|S1|
F083|primitives/collections|list_nth|lst,n|Result[Any]|none|pure,partial(oob)|S1|
F084|primitives/collections|list_take|lst,n|list|none|pure|S1|
F085|primitives/collections|list_drop|lst,n|list|none|pure|S1|
F086|primitives/collections|list_slice|lst,start,end|list|none|pure|S1|
F087|primitives/collections|list_reverse|lst|list|none|pure,invertible|S1|
F088|primitives/collections|list_map|lst,fn|list|none|pure|S1|
F089|primitives/collections|list_flatten|lst|list|none|pure|S1|
F090|primitives/collections|list_unique|lst|list|none|pure,idempotent|S1|
F091|primitives/collections|list_chunk|lst,n|List[list]|none|pure|S1|
F092|primitives/collections|list_interleave|a,b|list|none|pure|S1|
F093|primitives/collections|list_contains|lst,item|bool|none|pure|S1|
F094|primitives/collections|list_index_of|lst,item|Result[int]|none|pure,partial|S1|
F095|primitives/collections|list_filter|lst,pred|list|none|pure|S1|
F096|primitives/collections|list_any|lst,pred|bool|none|pure|S1|
F097|primitives/collections|list_all|lst,pred|bool|none|pure|S1|
F098|primitives/collections|list_count|lst,pred|int|none|pure|S1|
F099|primitives/collections|list_sort|lst,key_fn|list|none|pure,deterministic|S1|
F100|primitives/collections|list_sort_reverse|lst,key_fn|list|none|pure|S1|
F101|primitives/collections|list_sort_by_key|lst,key_fn|list|none|pure|S1|
F102|primitives/collections|list_min|lst|Result[Any]|none|pure,partial(empty)|S1|
F103|primitives/collections|list_max|lst|Result[Any]|none|pure,partial(empty)|S1|
F104|primitives/collections|list_partition|lst,pred|Tuple[list,list]|none|pure|S1|
F105|primitives/collections|list_group_by|lst,key_fn|Dict|none|pure|S1|
F106|primitives/collections|list_frequencies|lst|Dict|none|pure|S1|
F107|primitives/collections|list_reduce|lst,fn,init|Any|none|pure|S1|
F108|primitives/collections|list_zip|a,b|List[Tuple]|none|pure|S1|
F109|primitives/collections|list_unzip|pairs|Tuple[list,list]|none|pure|S1|
# --- primitives/sets.py (14) ---
F110|primitives/sets|set_from_list|lst|set|none|pure,idempotent|S1|
F111|primitives/sets|set_to_list|s|list|none|pure|S1|
F112|primitives/sets|set_add|s,item|set|none|pure|S1|
F113|primitives/sets|set_remove|s,item|set|none|pure|S1|
F114|primitives/sets|set_contains|s,item|bool|none|pure|S1|
F115|primitives/sets|set_size|s|int|none|pure|S1|
F116|primitives/sets|set_union|a,b|set|none|pure,commutative,associative,idempotent|S1|
F117|primitives/sets|set_intersection|a,b|set|none|pure,commutative,associative,idempotent|S1|
F118|primitives/sets|set_difference|a,b|set|none|pure|S1|
F119|primitives/sets|set_symmetric_diff|a,b|set|none|pure,commutative|S1|
F120|primitives/sets|set_power|s|set|none|pure|S1|
F121|primitives/sets|set_is_subset|a,b|bool|none|pure|S1|
F122|primitives/sets|set_is_superset|a,b|bool|none|pure|S1|
F123|primitives/sets|set_is_disjoint|a,b|bool|none|pure|S1|
# --- primitives/mappings.py (15) ---
F124|primitives/mappings|dict_new||dict|none|pure|S1|
F125|primitives/mappings|dict_from_pairs|pairs|dict|none|pure|S1|
F126|primitives/mappings|dict_get|d,key|Result[Any]|none|pure,partial|S1|
F127|primitives/mappings|dict_get_or|d,key,default|Any|none|pure|S1|
F128|primitives/mappings|dict_contains_key|d,key|bool|none|pure|S1|
F129|primitives/mappings|dict_size|d|int|none|pure|S1|
F130|primitives/mappings|dict_set|d,key,val|dict|none|pure|S1|
F131|primitives/mappings|dict_remove|d,key|dict|none|pure|S1|
F132|primitives/mappings|dict_merge|a,b|dict|none|pure|S1|b overwrites a
F133|primitives/mappings|dict_keys|d|list|none|pure|S1|
F134|primitives/mappings|dict_values|d|list|none|pure|S1|
F135|primitives/mappings|dict_pairs|d|List[Tuple]|none|pure|S1|
F136|primitives/mappings|dict_filter_keys|d,pred|dict|none|pure|S1|
F137|primitives/mappings|dict_map_values|d,fn|dict|none|pure|S1|
F138|primitives/mappings|dict_invert|d|Result[dict]|none|pure,partial(non-unique vals)|S1|
# --- primitives/conversion.py (14) ---
F139|primitives/conversion|to_string|Any|str|none|pure|S1|
F140|primitives/conversion|to_number|str|Result[int]|none|pure,partial|S1|
F141|primitives/conversion|to_fraction|str|Result[VDRFraction]|none|pure,partial|S1|PRIMARY CONVERSION BOUNDARY
F142|primitives/conversion|format_json|dict|str|none|pure|S1|
F143|primitives/conversion|parse_json|str|Result[dict]|none|pure,partial|S1|
F144|primitives/conversion|format_csv|List[List[str]],delim|str|none|pure|S1|
F145|primitives/conversion|parse_csv|str,delim|List[List[str]]|none|pure|S1|
F146|primitives/conversion|format_table|List[List[str]]|str|none|pure|S1|
F147|primitives/conversion|format_fraction|VDRFraction|str|none|pure,lossless|S1|
F148|primitives/conversion|fraction_to_decimal|VDRFraction,digits:int|str|none|pure,lossy|S1|
F149|primitives/conversion|format_percentage|VDRFraction,decimal_places|str|none|pure,lossy|S1|
F150|primitives/conversion|format_scientific|VDRFraction,sig_digits|str|none|pure,lossy|S1|
F151|primitives/conversion|vdr_from_decimal_string|str|Result[VDRFraction]|none|pure,partial|S1|exact for terminating decimals
F152|primitives/conversion|vdr_from_ratio_string|str|Result[VDRFraction]|none|pure,lossless|S1|
# --- primitives/logic.py (11) ---
F153|primitives/logic|if_then_else|bool,true_fn,false_fn|Any|none|pure|S1|
F154|primitives/logic|case_match|value,cases:List[Tuple[Any,Callable]]|Result[Any]|none|pure,partial|S1|
F155|primitives/logic|for_each|items,fn|None|none|pure|S1|
F156|primitives/logic|repeat_n|n,fn|list|none|pure|S1|
F157|primitives/logic|while_loop|predicate,fn,state|Any|none|pure|S1|
F158|primitives/logic|try_catch|fn,handler|Any|none|pure|S1|
F159|primitives/logic|assert_that|bool,message|Result[None]|none|pure,partial|S1|
F160|primitives/logic|type_check|value,expected_type:str|bool|none|pure|S1|
F161|primitives/logic|is_bound|var_name,bindings:Binding|bool|none|pure|S1|
F162|primitives/logic|findall|kb,goal:Fact|List[Binding]|none|pure|S1|delegates to query_rules
F163|primitives/logic|aggregate|kb,goal,fn,init|Any|none|pure|S1|
# --- primitives/integer_ops.py (21) ---
F164|primitives/integer_ops|int_add|a,b:int|int|none|pure,commutative,associative|S1|
F165|primitives/integer_ops|int_sub|a,b:int|int|none|pure|S1|
F166|primitives/integer_ops|int_mul|a,b:int|int|none|pure,commutative,associative|S1|
F167|primitives/integer_ops|int_div|a,b:int|Result[int]|none|pure,partial(b=0)|S1|
F168|primitives/integer_ops|int_mod|a,b:int|Result[int]|none|pure,partial(b=0)|S1|
F169|primitives/integer_ops|int_pow|a,b:int|int|none|pure|S1|
F170|primitives/integer_ops|int_abs|a:int|int|none|pure,idempotent|S1|
F171|primitives/integer_ops|int_sign|a:int|int|none|pure|S1|
F172|primitives/integer_ops|int_min|a,b|int|none|pure,commutative,idempotent|S1|
F173|primitives/integer_ops|int_max|a,b|int|none|pure,commutative,idempotent|S1|
F174|primitives/integer_ops|int_clamp|val,lo,hi|int|none|pure,idempotent|S1|
F175|primitives/integer_ops|int_range|start,end|List[int]|none|pure|S1|
F176|primitives/integer_ops|int_range_step|start,end,step|List[int]|none|pure|S1|
F177|primitives/integer_ops|bit_and|a,b|int|none|pure,commutative,associative,idempotent|S1|
F178|primitives/integer_ops|bit_or|a,b|int|none|pure,commutative,associative,idempotent|S1|
F179|primitives/integer_ops|bit_xor|a,b|int|none|pure,commutative,associative|S1|
F180|primitives/integer_ops|bit_not|a|int|none|pure,invertible|S1|
F181|primitives/integer_ops|bit_shift_left|a,n|int|none|pure|S1|
F182|primitives/integer_ops|bit_shift_right|a,n|int|none|pure|S1|
F183|primitives/integer_ops|bit_count|a|int|none|pure|S1|popcount
F184|primitives/integer_ops|bit_width|a|int|none|pure|S1|
# --- data_primitives/counter.py (7) ---
F185|data_primitives/counter|counter_create|kb,name,min_value,max_value|None|kb.counters_add|deterministic|S1|
F186|data_primitives/counter|counter_inc|kb,name|Result[int]|counter_mutate|deterministic|S1|clamps at max
F187|data_primitives/counter|counter_dec|kb,name|Result[int]|counter_mutate|deterministic|S1|clamps at min
F188|data_primitives/counter|counter_add|kb,name,delta|Result[int]|counter_mutate|deterministic|S1|
F189|data_primitives/counter|counter_get|kb,name|Result[int]|none|pure|S1|
F190|data_primitives/counter|counter_reset|kb,name|None|counter_mutate|idempotent|S1|
F191|data_primitives/counter|counter_set|kb,name,value|None|counter_mutate|idempotent|S1|
# --- data_primitives/lock.py (6) ---
F192|data_primitives/lock|lock_create|kb,name|None|kb.locks_add|deterministic|S1|
F193|data_primitives/lock|lock_acquire|kb,name,holder,notes|bool|lock_mutate_if_free|deterministic|S1|
F194|data_primitives/lock|lock_release|kb,name|None|lock_mutate|idempotent|S1|
F195|data_primitives/lock|lock_check|kb,name|bool|none|pure|S1|
F196|data_primitives/lock|lock_holder|kb,name|Result[str]|none|pure,partial|S1|
F197|data_primitives/lock|lock_force_release|kb,name|None|lock_mutate|idempotent|S1|
# --- data_primitives/queue.py (9) ---
F198|data_primitives/queue|queue_create|kb,name,capacity|None|kb.queues_add|deterministic|S1|
F199|data_primitives/queue|queue_push|kb,name,item|bool(F=full)|queue_mutate|deterministic|S1|
F200|data_primitives/queue|queue_pop|kb,name|Result[Any]|queue_mutate|partial(empty)|S1|
F201|data_primitives/queue|queue_peek|kb,name|Result[Any]|none|pure,partial(empty)|S1|
F202|data_primitives/queue|queue_size|kb,name|int|none|pure|S1|
F203|data_primitives/queue|queue_is_empty|kb,name|bool|none|pure|S1|
F204|data_primitives/queue|queue_is_full|kb,name|bool|none|pure|S1|
F205|data_primitives/queue|queue_clear|kb,name|None|queue_mutate|idempotent|S1|
F206|data_primitives/queue|queue_to_list|kb,name|List[Any]|none|pure|S1|
# --- data_primitives/stack.py (8) ---
F207|data_primitives/stack|stack_create|kb,name,capacity|None|kb.stacks_add|deterministic|S1|
F208|data_primitives/stack|stack_push|kb,name,item|bool(F=full)|stack_mutate|deterministic|S1|
F209|data_primitives/stack|stack_pop|kb,name|Result[Any]|stack_mutate|partial(empty)|S1|
F210|data_primitives/stack|stack_peek|kb,name|Result[Any]|none|pure,partial(empty)|S1|
F211|data_primitives/stack|stack_size|kb,name|int|none|pure|S1|
F212|data_primitives/stack|stack_is_empty|kb,name|bool|none|pure|S1|
F213|data_primitives/stack|stack_clear|kb,name|None|stack_mutate|idempotent|S1|
F214|data_primitives/stack|stack_to_list|kb,name|List[Any]|none|pure|S1|top-to-bottom
# --- iose/registry.py ---
F215|iose/registry|register|builtin_def:BuiltinDef|None|registry_add|deterministic|S1|
F216|iose/registry|get_by_id|int|Optional[BuiltinDef]|none|pure|S1|
F217|iose/registry|get_by_name|str|Optional[BuiltinDef]|none|pure|S1|
F218|iose/registry|all_in_category|str|List[BuiltinDef]|none|pure|S1|
F219|iose/registry|count||int|none|pure|S1|
F220|iose/registry|register_builtin|id,name,cat,inputs,outputs,se,props,desc,impl|None|registry_add|deterministic|S1|convenience helper
# --- iose/principles.py ---
F221|iose/principles|load_oso_principles|kb_store|KnowledgeBase|kb_store_add,~176_terms_asserted|deterministic|S1|15 axioms,~80 facts,~60 rules,21 constraints
F222|iose/principles|get_knowability|source_type:str|VDRFraction|none|pure|S1|
F223|iose/principles|get_priority|concern,domain:str|VDRFraction|none|pure|S1|
F224|iose/principles|priority_winner|concern_a,concern_b,domain|str(a/b/tradeoff_required)|none|pure|S1|90/9/0.9 rule

# --- STAGE 2: kb/constraint_engine.py ---
F225|kb/constraint_engine|check_constraint|kb,constraint,kb_store|bool(T=satisfied)|none|pure|S2|evaluates Prolog condition via rule engine
F226|kb/constraint_engine|check_all_constraints|kb,kb_store|List[Constraint](violations)|none|pure|S2|
F227|kb/constraint_engine|enforce_constraint|constraint,kb|str(warned/blocked/error/escalated)|depends_on_violation_type|-|S2|
F228|kb/constraint_engine|add_constraint|kb,constraint|None|kb.constraints_modify|-|S2|
F229|kb/constraint_engine|remove_constraint|kb,name|None|kb.constraints_modify|idempotent|S2|
F230|kb/constraint_engine|enable_constraint|kb,name|None|kb.constraints_modify|idempotent|S2|
F231|kb/constraint_engine|suspend_constraint|kb,name|None|kb.constraints_modify|idempotent|S2|
# --- kb/scope_resolver.py ---
F232|kb/scope_resolver|build_scope_chain|active_kb_id,kb_store|ScopeChain|none|pure|S2|walks parent_id to root
F233|kb/scope_resolver|scoped_query|scope_chain,predicate,args,kb_store|List[Fact]|none|pure|S2|first KB in scope with matches wins
F234|kb/scope_resolver|scoped_query_all|predicate,args,kb_store|List[Tuple[str,Fact]]|none|pure|S2|all KBs, tagged by source
F235|kb/scope_resolver|resolve_binding_scoped|scope_chain,key,kb_store|Optional[Any]|none|pure|S2|
# --- path/registry.py ---
F236|path/registry|register_path|path:str|int(assigned ID)|registry_add|deterministic|S2|existing→returns ID; retired IDs never reused
F237|path/registry|resolve|path:str|Result[int]|none|pure,partial|S2|
F238|path/registry|from_id|int|Result[str]|none|pure,partial|S2|
F239|path/registry|exists|path:str|bool|none|pure|S2|
# --- path/resolver.py ---
F240|path/resolver|resolve_dotted_path|path,registry:PathRegistry|Result[int]|none|pure|S2|
F241|path/resolver|path_parent|path|Result[str]|none|pure,partial(root)|S2|
F242|path/resolver|path_children|path,registry|List[str]|none|pure|S2|
F243|path/resolver|path_ancestors|path|List[str]|none|pure|S2|parent→root
F244|path/resolver|path_depth|path|int|none|pure|S2|root=0
F245|path/resolver|path_common_ancestor|a,b:str|str|none|pure,commutative|S2|
# --- command/parser.py ---
F246|command/parser|parse_command_stream|raw_stream:str|List[Union[str,CommandToken]]|none|pure|S2|
F247|command/parser|parse_single_command|line:str|Result[CommandToken]|none|pure|S2|
# --- command/executor.py ---
F248|command/executor|execute_command|token,registry,path_reg,kb_store,scope_chain|Result[Any]|per_command|-|S2|resolves paths, validates types, dispatches
F249|command/executor|execute_chain|List[CommandToken],registry,path_reg,kb_store,scope_chain|Result[List[Any]]|union_of_all|-|S2|
# --- command/scratchpad.py ---
F250|command/scratchpad|write_entry|entry_type,content,turn|None|ring_write|-|S2|
F251|command/scratchpad|read_recent|count:int|List[Dict]|none|pure|S2|
F252|command/scratchpad|clear||None|ring_clear|idempotent|S2|
# --- primitives/active_arithmetic.py (5) ---
F253|primitives/active_arith|vdr_active_add_same_d|a,b:VDRFraction|VDRFraction|none|pure,commutative|S2|both must share d
F254|primitives/active_arith|vdr_active_add_diff_d|a,b:VDRFraction|VDRFraction|none|pure,commutative|S2|
F255|primitives/active_arith|vdr_active_mul|a,b:VDRFraction|VDRFraction|none|pure,commutative|S2|
F256|primitives/active_arith|vdr_active_div_by_closed|a:VDRFraction,b:VDRFraction|Result[VDRFraction]|none|pure,partial|S2|b must be closed
F257|primitives/active_arith|vdr_active_div_by_active|a,b:VDRFraction|Result[VDRFraction]|none|pure,partial|S2|divisor remainder lost (v1 compromise)
# --- primitives/structure_ops.py (3) ---
F258|primitives/structure_ops|vdr_lift|remainder,k:int|remainder|none|pure|S2|
F259|primitives/structure_ops|vdr_rebase|frac:VDRFraction,target_d:int|VDRFraction|none|pure|S2|may produce mismatch witness
F260|primitives/structure_ops|vdr_scalar_projection|frac:VDRFraction|Result[VDRFraction(closed)]|none|pure,partial(unresolved fn)|S2|
# --- primitives/number_theory.py (13) ---
F261|primitives/number_theory|vdr_gcd|a,b:int|int|none|pure,commutative,associative|S2|
F262|primitives/number_theory|vdr_lcm|a,b:int|int|none|pure,commutative,associative|S2|
F263|primitives/number_theory|vdr_mod|a,b:int|Result[int]|none|pure,partial(b=0)|S2|
F264|primitives/number_theory|vdr_div_exact|a,b:int|Result[int]|none|pure,partial|S2|
F265|primitives/number_theory|vdr_mod_pow|base,exp,modulus:int|int|none|pure|S2|binary exponentiation
F266|primitives/number_theory|vdr_mod_inv|a,m:int|Result[int]|none|pure,partial(gcd≠1)|S2|
F267|primitives/number_theory|vdr_extended_gcd|a,b:int|Tuple[int,int,int]|none|pure|S2|g,x,y where ax+by=g
F268|primitives/number_theory|vdr_is_prime|n:int|bool|none|pure|S2|
F269|primitives/number_theory|vdr_factorial|n:int|Result[int]|none|pure,partial(n<0)|S2|
F270|primitives/number_theory|vdr_binomial|n,k:int|int|none|pure|S2|
F271|primitives/number_theory|vdr_fibonacci|n:int|int|none|pure|S2|matrix power method
F272|primitives/number_theory|vdr_euler_totient|n:int|int|none|pure|S2|
F273|primitives/number_theory|vdr_chinese_remainder|remainders,moduli:List[int]|Result[int]|none|pure,partial(not coprime)|S2|
# --- primitives/linalg_builtins.py (24) ---
F274|primitives/linalg|vdr_vec_new|List[VDRFraction]|Vec|none|pure|S2|
F275|primitives/linalg|vdr_vec_dim|Vec|int|none|pure|S2|
F276|primitives/linalg|vdr_vec_get|Vec,idx|Result[VDRFraction]|none|pure,partial|S2|
F277|primitives/linalg|vdr_vec_add|a,b:Vec|Vec|none|pure,commutative,associative|S2|
F278|primitives/linalg|vdr_vec_sub|a,b:Vec|Vec|none|pure|S2|
F279|primitives/linalg|vdr_vec_scale|scalar:VDRFraction,v:Vec|Vec|none|pure|S2|
F280|primitives/linalg|vdr_vec_dot|a,b:Vec|VDRFraction|none|pure,commutative|S2|
F281|primitives/linalg|vdr_vec_norm_sq|Vec|VDRFraction|none|pure|S2|
F282|primitives/linalg|vdr_vec_neg|Vec|Vec|none|pure,invertible|S2|
F283|primitives/linalg|vdr_mat_new|List[Vec]|Mat|none|pure|S2|
F284|primitives/linalg|vdr_mat_dims|Mat|Tuple[int,int]|none|pure|S2|
F285|primitives/linalg|vdr_mat_get|Mat,row,col|Result[VDRFraction]|none|pure,partial|S2|
F286|primitives/linalg|vdr_mat_add|a,b:Mat|Mat|none|pure,commutative,associative|S2|
F287|primitives/linalg|vdr_mat_mul|a,b:Mat|Mat|none|pure,associative,NOT_commutative|S2|
F288|primitives/linalg|vdr_mat_scale|scalar,Mat|Mat|none|pure|S2|
F289|primitives/linalg|vdr_mat_transpose|Mat|Mat|none|pure,invertible(self-inverse)|S2|
F290|primitives/linalg|vdr_mat_matvec|Mat,Vec|Vec|none|pure|S2|
F291|primitives/linalg|vdr_mat_det|Mat|VDRFraction|none|pure|S2|
F292|primitives/linalg|vdr_mat_inv|Mat|Result[Mat]|none|pure,partial(det=0),invertible|S2|
F293|primitives/linalg|vdr_mat_solve|a:Mat,b:Vec|Result[Vec]|none|pure,partial(det=0)|S2|
F294|primitives/linalg|vdr_mat_rank|Mat|int|none|pure|S2|
F295|primitives/linalg|vdr_mat_identity|size:int|Mat|none|pure|S2|
F296|primitives/linalg|vdr_mat_trace|Mat|VDRFraction|none|pure|S2|
F297|primitives/linalg|vdr_mat_pow|Mat,n:int|Mat|none|pure|S2|
F298|primitives/linalg|vdr_mat_gram_schmidt|Mat|Result[Mat]|none|pure,partial(lin_dep)|S2|
# --- primitives/statistics.py (16) ---
F299|primitives/statistics|vdr_stat_mean|List[VDRFraction]|Result[VDRFraction]|none|pure,partial(empty)|S2|
F300|primitives/statistics|vdr_stat_variance|List[VDRFraction]|Result[VDRFraction]|none|pure,partial|S2|
F301|primitives/statistics|vdr_stat_median|List[VDRFraction]|Result[VDRFraction]|none|pure,partial|S2|
F302|primitives/statistics|vdr_stat_mode|List[VDRFraction]|Result[Any]|none|pure,partial|S2|
F303|primitives/statistics|vdr_stat_percentile|List[VDRFraction],p:VDRFraction|Result[VDRFraction]|none|pure,partial|S2|
F304|primitives/statistics|vdr_prob_normalize|List[VDRFraction]|List[VDRFraction]|none|pure|S2|
F305|primitives/statistics|vdr_prob_is_valid|List[VDRFraction]|bool|none|pure|S2|
F306|primitives/statistics|vdr_prob_bayes|p_b_given_a,p_a,p_b:VDRFraction|Result[VDRFraction]|none|pure,partial(p_b=0)|S2|
F307|primitives/statistics|vdr_prob_expected|probs,values|VDRFraction|none|pure|S2|
F308|primitives/statistics|vdr_prob_cdf|pmf:List[VDRFraction]|List[VDRFraction]|none|pure|S2|
F309|primitives/statistics|vdr_prob_joint|marginal_a,marginal_b|Mat|none|pure|S2|
F310|primitives/statistics|vdr_prob_marginal|joint:Mat,axis:int|List[VDRFraction]|none|pure|S2|
F311|primitives/statistics|vdr_prob_conditional|joint:Mat,given_idx|Result[List[VDRFraction]]|none|pure,partial|S2|
F312|primitives/statistics|vdr_prob_entropy_terms|probs,log_depth:int|List[VDRFraction]|none|pure|S2|
F313|primitives/statistics|vdr_softmax|logits:List[VDRFraction],depth:int|List[VDRFraction]|none|pure|S2|
F314|primitives/statistics|vdr_softmax_surrogate|logits,shift:VDRFraction|List[VDRFraction]|none|pure|S2|
# --- primitives/time_ops.py (10) ---
F315|primitives/time_ops|date_from_ymd|y,m,d:int|int(day_count)|none|pure|S2|
F316|primitives/time_ops|date_to_ymd|day_count:int|Tuple[int,int,int]|none|pure|S2|
F317|primitives/time_ops|date_diff_days|a,b:int|int|none|pure|S2|
F318|primitives/time_ops|date_add_days|day_count,n:int|int|none|pure|S2|
F319|primitives/time_ops|date_day_of_week|day_count:int|int(0-6)|none|pure|S2|
F320|primitives/time_ops|date_is_leap_year|y:int|bool|none|pure|S2|
F321|primitives/time_ops|date_days_in_month|y,m:int|int|none|pure|S2|
F322|primitives/time_ops|time_from_hms|h,m,s:int|int(seconds)|none|pure|S2|
F323|primitives/time_ops|time_to_hms|seconds:int|Tuple[int,int,int]|none|pure|S2|
F324|primitives/time_ops|duration_between|a,b:int|int|none|pure|S2|
# --- primitives/identity.py (8) ---
F325|primitives/identity|hash_string|str|int|none|pure,deterministic|S2|
F326|primitives/identity|hash_combine|a,b:int|int|none|pure,deterministic|S2|
F327|primitives/identity|base64_encode|str|str|none|pure,invertible|S2|
F328|primitives/identity|base64_decode|str|Result[str]|none|pure,partial,invertible|S2|
F329|primitives/identity|hex_encode|str|str|none|pure,invertible|S2|
F330|primitives/identity|hex_decode|str|Result[str]|none|pure,partial,invertible|S2|
F331|primitives/identity|crc32|str|int|none|pure,deterministic|S2|
F332|primitives/identity|uuid_from_seed|int|str|none|pure,deterministic|S2|
# --- primitives/graphs.py (13) ---
F333|primitives/graphs|graph_from_edges|List[Tuple]|Dict(adj)|none|pure|S2|
F334|primitives/graphs|graph_neighbors|graph,node|List|none|pure|S2|
F335|primitives/graphs|graph_bfs|graph,start|List|none|pure,deterministic|S2|
F336|primitives/graphs|graph_dfs|graph,start|List|none|pure,deterministic|S2|
F337|primitives/graphs|graph_shortest_path|graph,start,end|Result[List]|none|pure,partial(no path)|S2|
F338|primitives/graphs|graph_shortest_path_weighted|graph(VDR weights),start,end|Result[Tuple[List,VDRFraction]]|none|pure,partial|S2|
F339|primitives/graphs|graph_connected_components|graph|List[List]|none|pure|S2|
F340|primitives/graphs|graph_is_connected|graph|bool|none|pure|S2|
F341|primitives/graphs|graph_topological_sort|graph|Result[List]|none|pure,partial(cycle)|S2|
F342|primitives/graphs|graph_cycle_detect|graph|bool|none|pure|S2|
F343|primitives/graphs|graph_degree|graph,node|int|none|pure|S2|
F344|primitives/graphs|graph_mst|graph(weighted)|List[Tuple]|none|pure|S2|
F345|primitives/graphs|graph_pagerank|graph,damping:VDRFraction|List[VDRFraction]|none|pure|S2|
# --- data_primitives/lru.py (8) ---
F346|data_primitives/lru|lru_create|kb,name,capacity|None|kb.lrus_add|deterministic|S2|
F347|data_primitives/lru|lru_push|kb,name,key,value|None|lru_mutate,evict_if_full|deterministic|S2|
F348|data_primitives/lru|lru_get|kb,name,key|Result[Any]|lru_access_update|partial|S2|
F349|data_primitives/lru|lru_peek|kb,name,count|List[Tuple[str,Any]]|none|pure|S2|no access update
F350|data_primitives/lru|lru_contains|kb,name,key|bool|none|pure|S2|
F351|data_primitives/lru|lru_size|kb,name|int|none|pure|S2|
F352|data_primitives/lru|lru_clear|kb,name|None|lru_mutate|idempotent|S2|
F353|data_primitives/lru|lru_evict|kb,name,key|None|lru_mutate|idempotent|S2|
# --- data_primitives/ring_buffer.py (6) ---
F354|data_primitives/ring|ring_create|kb,name,capacity|None|kb.buffers_add|deterministic|S2|
F355|data_primitives/ring|ring_write|kb,name,item|None|ring_mutate|deterministic|S2|overwrites oldest if full
F356|data_primitives/ring|ring_read_all|kb,name|List[Any]|none|pure|S2|chronological
F357|data_primitives/ring|ring_read_last|kb,name,count|List[Any]|none|pure|S2|
F358|data_primitives/ring|ring_size|kb,name|int|none|pure|S2|
F359|data_primitives/ring|ring_clear|kb,name|None|ring_mutate|idempotent|S2|
# --- data_primitives/bitset.py (9) ---
F360|data_primitives/bitset|bitset_create|kb,name,width|None|kb.bitsets_add|deterministic|S2|
F361|data_primitives/bitset|bitset_set|kb,name,index|None|bitset_mutate|idempotent|S2|
F362|data_primitives/bitset|bitset_clear_bit|kb,name,index|None|bitset_mutate|idempotent|S2|
F363|data_primitives/bitset|bitset_test|kb,name,index|bool|none|pure|S2|
F364|data_primitives/bitset|bitset_all_set|kb,name|bool|none|pure|S2|
F365|data_primitives/bitset|bitset_any_set|kb,name|bool|none|pure|S2|
F366|data_primitives/bitset|bitset_count|kb,name|int|none|pure|S2|
F367|data_primitives/bitset|bitset_reset|kb,name|None|bitset_mutate|idempotent|S2|
F368|data_primitives/bitset|bitset_to_list|kb,name|List[int]|none|pure|S2|sorted set-bit indices
# --- iose/validator.py (3) ---
F369|iose/validator|validate_type_compatibility|chain:List[BuiltinDef]|List[str](mismatches)|none|pure|S2|
F370|iose/validator|preview_side_effects|chain:List[BuiltinDef]|List[str]|none|pure|S2|
F371|iose/validator|verify_contract|builtin_def,declared_effects,observed_effects|List[str](violations)|none|pure|S2|

# --- STAGE 3: path/mount.py ---
F372|path/mount|create_mount|mount_path,source_path,mode,registry,kb_store|Result[Mount]|mount_add,path_register|partial(cycle/not found)|S3|
F373|path/mount|remove_mount|mount_path,kb_store|None|mount_remove|idempotent|S3|
F374|path/mount|check_mount_cycle|source_path,target_path,kb_store|bool(T=safe)|none|pure|S3|
F375|path/mount|resolve_through_mount|mount,predicate,args,kb_store|List[Fact]|none|pure|S3|respects mount mode
# --- primitives/qbasis.py (7) ---
F376|primitives/qbasis|qbasis_add|a,b:QBasis|QBasis|none|pure,commutative|S3|same exp: int add; diff: align first
F377|primitives/qbasis|qbasis_sub|a,b:QBasis|QBasis|none|pure|S3|
F378|primitives/qbasis|qbasis_mul|a,b:QBasis|Tuple[QBasis,VDRFraction(error)]|none|pure|S3|reprojected + exact error bound
F379|primitives/qbasis|qbasis_scalar_mul|scalar:VDRFraction,qb:QBasis|QBasis|none|pure|S3|
F380|primitives/qbasis|qbasis_to_fraction|QBasis|VDRFraction|none|pure,lossless|S3|
F381|primitives/qbasis|qbasis_get_constant|name:str|Result[QBasis]|none|pure,partial|S3|pi,e,etc from Q335
F382|primitives/qbasis|qbasis_precision_bits|QBasis|int|none|pure|S3|
# --- primitives/functional.py (8) ---
F383|primitives/functional|fn_sqrt|value:VDRFraction,depth:int|VDRFraction|none|pure|S3|Newton-Raphson
F384|primitives/functional|fn_exp|value:VDRFraction,depth:int|VDRFraction|none|pure|S3|truncated Taylor
F385|primitives/functional|fn_log|value:VDRFraction,depth:int|Result[VDRFraction]|none|pure,partial(val≤0)|S3|
F386|primitives/functional|fn_sin|value:VDRFraction,depth:int|VDRFraction|none|pure|S3|Taylor series
F387|primitives/functional|fn_cos|value:VDRFraction,depth:int|VDRFraction|none|pure|S3|Taylor series
F388|primitives/functional|fn_resolve|fn_remainder:FnRemainder,depth:int|VDRFraction|none|pure|S3|evaluates callable
F389|primitives/functional|fn_make_newton|name,step_fn:Callable|FnRemainder|none|pure|S3|
F390|primitives/functional|fn_make_series|name,term_fn:Callable|FnRemainder|none|pure|S3|
# --- primitives/discrete_calculus.py (6) ---
F391|primitives/discrete_calc|vdr_discrete_derivative|f:Callable,x,h:VDRFraction|VDRFraction|none|pure|S3|
F392|primitives/discrete_calc|vdr_discrete_derivative_n|f,x,h:VDRFraction,n:int|VDRFraction|none|pure|S3|
F393|primitives/discrete_calc|vdr_left_riemann|f,a,b:VDRFraction,n:int|VDRFraction|none|pure|S3|
F394|primitives/discrete_calc|vdr_trapezoidal|f,a,b:VDRFraction,n:int|VDRFraction|none|pure|S3|
F395|primitives/discrete_calc|vdr_finite_difference_table|List[VDRFraction]|List[List[VDRFraction]]|none|pure|S3|
F396|primitives/discrete_calc|vdr_richardson_extrapolation|f,a,b:VDRFraction,n1,n2:int|VDRFraction|none|pure|S3|
# --- primitives/denom_mgmt.py (5) ---
F397|primitives/denom_mgmt|vdr_denom_bits|VDRFraction|int|none|pure|S3|
F398|primitives/denom_mgmt|vdr_denom_digits|VDRFraction|int|none|pure|S3|
F399|primitives/denom_mgmt|vdr_reproject_qbasis|frac:VDRFraction,exp:int|Tuple[VDRFraction,VDRFraction(error)]|none|pure|S3|
F400|primitives/denom_mgmt|vdr_denom_budget_check|frac:VDRFraction,budget_bits:int|bool(T=over)|none|pure|S3|
F401|primitives/denom_mgmt|vdr_precision_state|VDRFraction|Dict|none|pure|S3|denom_bits,digits,is_closed,is_active,remainder_depth,node_count
# --- primitives/polynomial.py (8) ---
F402|primitives/polynomial|poly_eval|coeffs:List[VDRFraction],x:VDRFraction|VDRFraction|none|pure|S3|Horner
F403|primitives/polynomial|poly_add|a,b:List[VDRFraction]|List[VDRFraction]|none|pure,commutative|S3|
F404|primitives/polynomial|poly_mul|a,b:List[VDRFraction]|List[VDRFraction]|none|pure,commutative|S3|
F405|primitives/polynomial|poly_div|a,b:List[VDRFraction]|Result[Tuple[list,list]]|none|pure,partial|S3|quotient,remainder
F406|primitives/polynomial|poly_gcd|a,b:List[VDRFraction]|List[VDRFraction]|none|pure,commutative|S3|
F407|primitives/polynomial|poly_derivative|coeffs|List[VDRFraction]|none|pure|S3|
F408|primitives/polynomial|poly_integral|coeffs|List[VDRFraction]|none|pure|S3|constant=0
F409|primitives/polynomial|poly_lagrange_interpolation|xs,ys:List[VDRFraction]|Result[List[VDRFraction]]|none|pure,partial|S3|
# --- primitives/finite_field.py (4) ---
F410|primitives/finite_field|gf_add|a,b,p:int|int|none|pure|S3|
F411|primitives/finite_field|gf_mul|a,b,p:int|int|none|pure|S3|
F412|primitives/finite_field|gf_inv|a,p:int|Result[int]|none|pure,partial(a=0)|S3|
F413|primitives/finite_field|gf_pow|a,b,p:int|int|none|pure|S3|
# --- primitives/markov.py (3) ---
F414|primitives/markov|markov_steady_state|Mat|Result[Vec]|none|pure,partial|S3|
F415|primitives/markov|markov_step|Mat,state:Vec|Vec|none|pure|S3|
F416|primitives/markov|markov_n_steps|Mat,state:Vec,n:int|Vec|none|pure|S3|
# --- primitives/graph_math.py (2) ---
F417|primitives/graph_math|adjacency_matrix_power|adj:Mat,n:int|Mat|none|pure|S3|
F418|primitives/graph_math|pagerank_exact|adj:Mat,damping:VDRFraction|Vec|none|pure|S3|
# --- session/snapshot.py (3) ---
F419|session/snapshot|capture_live_state|scope_chain,kb_store|Dict[int,KBLiveState]|none|pure(deep copy)|S3|
F420|session/snapshot|create_snapshot|name,scope_chain,kb_store,scratchpad,turn,notes|SessionSnapshot|snapshot_kb_create|deterministic|S3|
F421|session/snapshot|restore_snapshot|snapshot,kb_store|None|all_live_state_overwrite,scope_restore|deterministic|S3|
# --- session/clone.py (2) ---
F422|session/clone|clone_session|source_name,clone_name,snapshot_store,kb_store|None|snapshot_create(deep_copy_live),clone_register|deterministic|S3|shares persistent, copies live
F423|session/clone|kill_clone|clone_name,snapshot_store,kb_store|None|clone_live_clear,clone_deregister|deterministic|S3|persistent facts survive
# --- session/lifecycle.py (4) ---
F424|session/lifecycle|session_reset|scope_chain,kb_store|None|all_live_state_clear|idempotent|S3|persistent untouched
F425|session/lifecycle|session_list|snapshot_store|List[str]|none|pure|S3|
F426|session/lifecycle|session_diff|name_a,name_b,snapshot_store|Dict(added/removed/changed)|none|pure|S3|
F427|session/lifecycle|session_info|name,snapshot_store|Result[Dict]|none|pure,partial|S3|
# --- inference/notebook.py (2) ---
F428|inference/notebook|create_inference_notebook|path,problem,mode,goal,max_steps,max_queries,kb_store,registry|InferenceNotebook|kb_create,data_prims_init|deterministic|S3|
F429|inference/notebook|notebook_from_template|template_name,path,problem,kb_store,registry|InferenceNotebook|kb_create,template_schema_populate|deterministic|S3|SRE/bug/research/decision/argument
# --- inference/loop.py (5) ---
F430|inference/loop|assess|notebook,kb_store|LoopPhase|steps_executed_inc,steps_since_evidence_inc|-|S3|checks budget/stall/goal
F431|inference/loop|formalize|notebook,action_fn:Callable|Any(artifact)|artifact_may_assert|-|S3|hook for LLM creative step
F432|inference/loop|execute_step|artifact,notebook,kb_store,registry,executor|Result[Any]|per_artifact|-|S3|delegates to rule_engine/executor/env
F433|inference/loop|store_result|result,notebook,turn|None|kb_facts_assert,evidence_count_inc,steps_since_evidence_reset,bitset_update,lru_update|-|S3|
F434|inference/loop|run_loop|notebook,action_fn,kb_store,registry,executor,max_iter|InferenceNotebook|all_loop_effects|-|S3|full assess→formalize→execute→store until termination
# --- inference/confidence.py (5) ---
F435|inference/confidence|compute_deductive_confidence|List[VDRFraction]|VDRFraction|none|pure|S3|min(inputs)
F436|inference/confidence|compute_inductive_confidence|coverage,mean_source:VDRFraction|VDRFraction|none|pure|S3|coverage*mean
F437|inference/confidence|compute_abductive_confidence|explained_frac,min_evidence:VDRFraction|VDRFraction|none|pure|S3|
F438|inference/confidence|compute_analogical_confidence|strength,source:VDRFraction|VDRFraction|none|pure|S3|strength*source
F439|inference/confidence|propagate_through_chain|List[Tuple[str,VDRFraction]]|VDRFraction|none|pure|S3|
# --- inference/provenance.py (4) ---
F440|inference/provenance|record_evidence|fact,source_type,confidence,notebook,turn|Dict(record)|evidence_assert|-|S3|
F441|inference/provenance|record_conclusion|statement,mode,confidence,derived_from,via_rules,via_tools,alternatives,notebook|InferenceConclusion|conclusion_assert|-|S3|
F442|inference/provenance|trace_derivation|conclusion_id,notebook|List[Dict]|none|pure|S3|evidence→conclusion chain
F443|inference/provenance|challenge_conclusion|counter_fact,conclusion_id,notebook,kb_store|Dict(still_holds,new_confidence,affected)|counter_fact_assert,conclusion_may_retract|-|S3|

# --- STAGE 4: env/base.py (abstract interface, 9 methods) ---
F444|env/base|exec_command|command,args:List[str]|ExecResult|process_execute|operational|S4|
F445|env/base|upload|content,remote_path|bool|file_create|operational|S4|
F446|env/base|download|remote_path|Result[str]|none|operational|S4|
F447|env/base|file_read|path|Result[str]|none|operational|S4|
F448|env/base|file_write|path,content|bool|file_write|operational|S4|
F449|env/base|list_dir|path|List[str]|none|operational|S4|
F450|env/base|start_process|command,args|str(task_id)|process_start|operational|S4|
F451|env/base|poll_process|task_id|TaskStatus|none|operational|S4|
F452|env/base|get_output|task_id|Tuple[str,str]|none|operational|S4|
# --- env/local.py ---
# F444-F452 implemented via Python subprocess+os; logs to env KB
# --- ops/grants.py ---
F453|ops/grants|add_grant|grant:Grant|None|grant_store_add|deterministic|S4|
F454|ops/grants|verify_grant|op_class,op_type,location,user|Result[Grant]|none|pure|S4|
F455|ops/grants|use_grant|grant:Grant|None|uses_remaining_dec,status_may_exhaust|-|S4|
F456|ops/grants|list_effective_grants|user,kb_store|List[Grant]|none|pure|S4|ancestry chain
# --- ops/filesystem.py (15) ---
F457|ops/filesystem|fs_read|path,grant|Result[str]|grant_use|operational|S4|
F458|ops/filesystem|fs_write|path,content,grant|bool|file_write,grant_use|operational|S4|
F459|ops/filesystem|fs_append|path,content,grant|bool|file_append,grant_use|operational|S4|
F460|ops/filesystem|fs_exists|path,grant|bool|grant_use|operational|S4|
F461|ops/filesystem|fs_list_dir|path,grant|List[str]|grant_use|operational|S4|
F462|ops/filesystem|fs_create_dir|path,grant|bool|dir_create,grant_use|operational|S4|
F463|ops/filesystem|fs_delete|path,grant|bool|file_delete,grant_use|operational|S4|
F464|ops/filesystem|fs_move|src,dst,grant|bool|file_move,grant_use|operational|S4|
F465|ops/filesystem|fs_copy|src,dst,grant|bool|file_copy,grant_use|operational|S4|
F466|ops/filesystem|fs_file_size|path,grant|int|grant_use|operational|S4|
F467|ops/filesystem|fs_file_modified|path,grant|int|grant_use|operational|S4|
F468|ops/filesystem|fs_glob|pattern,grant|List[str]|grant_use|operational|S4|
F469|ops/filesystem|fs_tree|path,grant|str|grant_use|operational|S4|
F470|ops/filesystem|fs_diff|a,b:str,grant|str|grant_use|operational|S4|
F471|ops/filesystem|fs_checksum|path,grant|str|grant_use|operational|S4|
# --- ops/execution.py (5) ---
F472|ops/execution|exec_python|script_path,env,grant|ExecResult|exec,grant_use|operational|S4|
F473|ops/execution|exec_shell|command,env,grant|ExecResult|exec,grant_use|operational|S4|
F474|ops/execution|exec_zig_test|test_path,env,grant|ExecResult|exec,grant_use|operational|S4|
F475|ops/execution|exec_pytest|test_path,env,grant|ExecResult|exec,grant_use|operational|S4|
F476|ops/execution|exec_script|interpreter,script_path,env,grant|ExecResult|exec,grant_use|operational|S4|
# --- ops/network.py (5) ---
F477|ops/network|net_download|url,local_path,grant|bool|file_write,grant_use|operational|S4|
F478|ops/network|net_fetch|url,grant|str|grant_use|operational|S4|
F479|ops/network|net_post|url,body,grant|str|grant_use|operational|S4|
F480|ops/network|net_ping|host,grant|bool|grant_use|operational|S4|
F481|ops/network|net_dns_resolve|hostname,grant|str|grant_use|operational|S4|
# --- ops/process.py (7) ---
F482|ops/process|proc_start|command,args,env,grant|str(task_id)|process_start,grant_use|operational|S4|
F483|ops/process|proc_poll|task_id,env|TaskStatus|none|operational|S4|
F484|ops/process|proc_wait|task_id,env|ExecResult|none|operational|S4|blocking
F485|ops/process|proc_kill|task_id,env,grant|None|process_kill,grant_use|operational|S4|
F486|ops/process|proc_stdout|task_id,env|str|none|operational|S4|
F487|ops/process|proc_stderr|task_id,env|str|none|operational|S4|
F488|ops/process|proc_list|env|List[Dict]|none|operational|S4|
# --- inference/modes.py (4) ---
F489|inference/modes|run_deductive|notebook,premises,rules,goal,kb_store|List[Binding]|premises_assert,rules_assert|-|S4|
F490|inference/modes|run_inductive|notebook,evidence,scoring_rules,kb_store|List[Tuple[str,VDRFraction]]|evidence_assert,rules_assert|-|S4|ranked hypotheses
F491|inference/modes|run_abductive|notebook,observations,causal_rules,kb_store|List[str]|obs_assert,rules_assert|-|S4|possible causes
F492|inference/modes|run_analogical|notebook,source_facts,target_facts,mapping_rules,kb_store|List[Tuple[Fact,VDRFraction]]|facts_assert,rules_assert|-|S4|transferred conclusions+strength
# --- lifecycle/data_pipeline.py (3) ---
F493|lifecycle/data_pipeline|register_data_source|name,url,license,source_type,kb_store|KnowledgeBase|kb_create_under_root.sources|-|S4|
F494|lifecycle/data_pipeline|prepare_corpus|source_kb,filters:List[Callable],split_ratios,kb_store|KnowledgeBase|kb_create,transform_log_assert|-|S4|
F495|lifecycle/data_pipeline|tokenize_corpus|corpus_kb,vocab_size,kb_store|KnowledgeBase|vocab_kb_create_frozen,tokenized_kb_create|-|S4|
# --- lifecycle/training.py (4) ---
F496|lifecycle/training|initialize_model|arch_config:Dict,seed:int,kb_store|KnowledgeBase|arch_kb_create,init_kb_create|deterministic|S4|exact VDR weights
F497|lifecycle/training|train_step|model_kb,train_kb,batch,lr:VDRFraction|VDRFraction(loss)|weights_update,step_log,loss_assert|-|S4|
F498|lifecycle/training|create_checkpoint|model_kb,train_kb,step,kb_store|KnowledgeBase|checkpoint_kb_create|-|S4|serialized exact weights+optimizer
F499|lifecycle/training|restore_checkpoint|checkpoint_kb,model_kb|None|weights_overwrite|idempotent|S4|
# --- lifecycle/evaluation.py (3) ---
F500|lifecycle/evaluation|run_benchmark|checkpoint_kb,benchmark_name,test_data,env,kb_store|Dict[str,VDRFraction]|eval_kb_create|-|S4|
F501|lifecycle/evaluation|run_eval_suite|checkpoint_kb,suite:List[str],test_data_map,env,kb_store|KnowledgeBase|eval_kbs_create,suite_kb_create|-|S4|
F502|lifecycle/evaluation|compare_checkpoints|eval_kb_a,eval_kb_b|Dict|none|pure|S4|

# --- STAGE 5: env/docker.py ---
F503|env/docker|create_container|image,working_dir,mounts,env_vars,limits|str(container_id)|container_create|operational|S5|
F504|env/docker|start_container||None|container_start,startup_script_exec|operational|S5|
F505|env/docker|stop_container||None|container_stop|operational|S5|
F506|env/docker|destroy_container||None|container_remove,kb_archive|operational|S5|
# F444-F452 implemented via docker exec
# --- env/ssh.py ---
# F444-F452 implemented via SSH; additional fields: host,port,username,key_ref
# --- env/vm.py ---
# F444-F452 implemented via VM provider API; additional fields: provider,vm_id,image,cpus,memory_mb
# --- ops/compilation.py (4) ---
F507|ops/compilation|compile_python_check|source,env,grant|ExecResult|exec,grant_use|operational|S5|
F508|ops/compilation|compile_zig|source,output,env,grant|ExecResult|exec,grant_use|operational|S5|
F509|ops/compilation|compile_c|source,output,env,grant|ExecResult|exec,grant_use|operational|S5|
F510|ops/compilation|compile_rust|source,output,env,grant|ExecResult|exec,grant_use|operational|S5|
# --- ops/linting.py (8) ---
F511|ops/linting|lint_python|source,env,grant|List[Dict]|grant_use|operational|S5|
F512|ops/linting|lint_zig|source,env,grant|List[Dict]|grant_use|operational|S5|
F513|ops/linting|lint_json|source,env,grant|List[Dict]|grant_use|operational|S5|
F514|ops/linting|lint_markdown|source,env,grant|List[Dict]|grant_use|operational|S5|
F515|ops/linting|analyze_imports|source,env,grant|Dict|grant_use|operational|S5|
F516|ops/linting|analyze_complexity|source,env,grant|Dict|grant_use|operational|S5|
F517|ops/linting|analyze_dependencies|source,env,grant|Dict|grant_use|operational|S5|
F518|ops/linting|count_lines|source,env,grant|int|grant_use|operational|S5|
# --- lifecycle/feedback.py (5) ---
F519|lifecycle/feedback|create_feedback_round|model_version,annotator_count,kb_store|KnowledgeBase|kb_create_with_schema|-|S5|
F520|lifecycle/feedback|add_pairwise_judgment|feedback_kb,prompt,resp_a,resp_b,preferred,annotator,confidence,time_spent|None|judgment_assert|-|S5|
F521|lifecycle/feedback|compute_agreement|feedback_kb|VDRFraction|none|pure|S5|Cohen's kappa exact from int counts
F522|lifecycle/feedback|train_reward_model|feedback_kb,base_checkpoint,config,kb_store|KnowledgeBase|reward_kb_create|-|S5|
F523|lifecycle/feedback|run_dpo|feedback_kb,base_checkpoint,config,kb_store|KnowledgeBase|aligned_kb_create|-|S5|
# --- lifecycle/deployment.py (5) ---
F524|lifecycle/deployment|create_deployment|checkpoint_kb,env,config,kb_store|KnowledgeBase|deploy_kb_create,model_load|-|S5|
F525|lifecycle/deployment|create_canary|deployment_kb,percentage:VDRFraction,duration_hours,criteria,kb_store|KnowledgeBase|canary_kb_create,traffic_split|-|S5|
F526|lifecycle/deployment|promote_canary|canary_kb,kb_store|None|canary_promote,old_deploy_deactivate|-|S5|
F527|lifecycle/deployment|rollback|deployment_kb,target_checkpoint,kb_store|None|current_deactivate,target_load,rollback_log|-|S5|
F528|lifecycle/deployment|retire_model|model_kb,reason,successor,kb_store|None|retirement_kb_create,archive,freeze|-|S5|frozen but queryable
# --- lifecycle/monitoring.py (5) ---
F529|lifecycle/monitoring|create_monitoring|deployment_kb,kb_store|KnowledgeBase|monitoring_kb_create|-|S5|
F530|lifecycle/monitoring|add_watch|monitoring_kb,name,condition,action|None|watch_assert|-|S5|
F531|lifecycle/monitoring|check_watches|monitoring_kb,kb_store|List[Dict]|triggered_watch_assert|-|S5|
F532|lifecycle/monitoring|record_metric|monitoring_kb,metric_name,value:VDRFraction,timestamp|None|metric_assert|-|S5|
F533|lifecycle/monitoring|detect_drift|monitoring_kb,baseline,current:Dict|List[Dict]|drift_event_assert_if_detected|-|S5|

# summary(stage|new_functions|cumulative)
# S1|~224 (F001-F224)|~224
# S2|~147 (F225-F371)|~371
# S3|~72 (F372-F443)|~443
# S4|~59 (F444-F502)|~502
# S5|~31 (F503-F533)|~533

# relationships(from|rel|to)
F017|delegates_to|F015,F016
F018|delegates_to|F015,F016
F024-F031|wraps|ST1(via core/vdr.py)
F162|delegates_to|F017
F225|delegates_to|F017
F233|uses|F013
F248|dispatches_via|ST37,ST36
F249|chains|F248
F253-F257|wraps|ST1(via core/active_mul.py)
F274-F298|wraps|ST5,ST6(via core/linalg.py)
F313-F314|wraps|ST1(via softmax.py)
F375|respects|EN3
F421|overwrites|ST25
F422|deep_copies|ST25
F430|reads|ST28
F431|hook_for|LLM_creative_step
F432|delegates_to|F017,F248,F444
F434|composes|F430,F431,F432,F433
F444-F452|implemented_by|env/local(S4),env/docker(S5),env/ssh(S5),env/vm(S5)
F454|checks|ST31
F457-F471|requires|F454
F472-F476|requires|F454
F477-F481|requires|F454
F482-F488|requires|F454
F489|uses|F017,F015
F490|uses|F017
F491|uses|F017
F492|uses|F017
F496|wraps|core/init.py
F497|wraps|core/trainer.py
F500|uses|F444
ST19|contains|ST7,ST8,ST9,ST10,ST12,ST13,ST14,ST15,ST16,ST17,ST18
ST22|stored_in|ST37
ST26|captures|ST25
ST28|wraps|ST19

# section_index(section|title|ids)
shared_enums|Enums|EN1-EN15
shared_structs|Core Value Types + KB + Data Prims + IOSE + Command + Session + Inference + Env + Grant|ST1-ST39
stage1|Stage 1: Toy Full Lifecycle|F001-F224
stage2|Stage 2: Upgraded Toy|F225-F371
stage3|Stage 3: Capacity Building|F372-F443
stage4|Stage 4: Full Integration|F444-F502
stage5|Stage 5: Production Completion|F503-F533

# decode_legend
id_prefixes: EN=enum, ST=struct, F=function
properties: pure=no side effects; deterministic=same input→same output; bounded=terminates; partial=can fail(returns Result); idempotent=f(f(x))=f(x); commutative=f(a,b)=f(b,a); associative=f(f(a,b),c)=f(a,f(b,c)); invertible=has inverse; lossless=no info lost; lossy=info lost; operational=external effects
side_effects: none=pure; kb.*_modify=KB field mutated; *_mutate=data primitive state changed; *_assert=fact asserted; *_create=KB created; grant_use=grant uses_remaining decremented; process_*=OS process; file_*=filesystem; container_*=Docker
stages: S1-S5; exists=VDR-4 code
function_count: 533 declared functions across 65 modules (includes struct methods and module-level helpers beyond the 448 registered builtins)
Result[T]: Ok(T)|Err(VDRError); replaces exceptions for expected failures
