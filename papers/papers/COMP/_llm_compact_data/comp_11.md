# NAME DRIVEN DEVELOPMENT — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → components → discipline → contrast → applicability → relationships → sections

# principles(id|principle|rationale)
P1|First act of engineering is exhaustively naming every state change|Before any code, architecture, or design — produce complete flat list of names. List becomes spec, architecture, task list, and documentation simultaneously
P2|If you can name everything that happens, you can build it|Conversely, if you cannot name what happens, you do not yet understand what you are building
P3|Implementation is mechanical process of writing action behind each name|Naming is the primary intellectual labor. Implementation is filling in the skeleton
P4|The enum is the architecture|Not a class hierarchy, not a flowchart, not a box diagram. A flat, ordered, grouped list of names
P5|All conditional logic lives in orchestrator, never in actions|Actions execute and return. Orchestrator is the only component that knows the shape of the program. Everything else knows only its own name
P6|The enum is a living document|Never frozen. Names added, split, merged, removed as understanding evolves. Diff of enum between versions = changelog of capability

# components(id|name|definition|constraints)
K1|Name|Identifier for a single distinct state change the system can undergo. Must be explainable in one sentence. If it cannot, it conceals two things and must be split|One name = one state change. No compound names. Verb-noun pair extracted from spec
K2|Carrier|Single struct type shared across all names. Fixed set of optional fields — source, target, parameter slots, timestamp. Not polymorphic, not specialized per name|One carrier shape. One code path, one logging format, one serialization. Fields not relevant to a given name stay at default. Resist temptation to create specialized carriers per category
K3|Action|Simplest code that does what the name says. Nothing more. Maps 1:1 to a name. Typically 5-50 lines|Never inspects event name (dispatch already answered that). Never calls other actions (emits new event instead). Never decides what happens next. Trivially testable: pass carrier, run, check result
K4|Sequence|The order in which names fire. Linear, branching, or concurrent. All ordering and branching logic lives in orchestrator|Dependencies between names are explicit and declared, not implicit in call order. Orchestrator walks list, populates carrier, fires name, checks result, proceeds or halts
K5|Orchestrator|The component that drives execution. Knows the shape of the program. Reads results, decides next name|Only place conditional logic, branching, and ordering decisions live. Can be loop, state machine, workflow engine, or human
K6|Enum|The canonical flat ordered grouped list of all names. Grouped by domain, ordered by lifecycle within group. Groups begin at round offsets (100, 200, 300) leaving room for additions|The architecture. The spec. The task list. The documentation. Single artifact serving all four roles

# naming_discipline(id|rule|mechanism)
ND1|No code until every name exists|Time spent naming = time not spent refactoring, discovering missing states during integration, debugging implicit transitions
ND2|One sentence explanation test|Name that cannot be explained in one sentence conceals two things — split it
ND3|Incomplete sequence = missing name|A state change happening implicitly that nobody articulated. Find it, name it
ND4|Names that always fire together = merge candidate|Two names with identical carriers in immediate succession — collapse to one
ND5|Names with independent failure modes = split candidate|If two things can fail independently, they are two names, not one
ND6|Groups at round offsets|100, 200, 300... Practical convention for readability and future additions without renumbering

# spec_to_names(id|step|description)
SN1|Input|Natural language specification describing every behavior, interaction, rule. Written in domain language for completeness of thought
SN2|Extraction|Every verb-noun pair is candidate name. "The kernel mounts the root filesystem" → Kernel_Root_Filesystem_Mounted. Decomposition task, not design task
SN3|Method|Manual (developer + text editor), collaborative (team + whiteboard), or LLM-accelerated (spec as input, state changes as output). LLM suited because it's pattern extraction — domain vocabulary from spec ensures consistency
SN4|Quality gate|Developer reads draft critically. Split names that conceal two things. Merge names that always fire together. Fill sequence gaps. Developer judgment is quality gate, extraction method is accelerator

# contrast_with_event_driven(id|dimension|event_driven|name_driven)
CE1|When events defined|During implementation, bottom-up from communication needs. Full set never enumerated in advance|Before implementation. All names exist first. Implementation fills in actions
CE2|Where logic lives|In handlers. on_payment_completed might update inventory, generate invoice, notify shipping, send email, log audit. Handler is locus of complexity|Five separate names: Inventory_Updated, Invoice_Generated, Shipping_Notified, Confirmation_Sent, Audit_Logged. Each does one thing. Orchestrator fires all five
CE3|Completeness testing|Run system, observe behaviors. Missing handler = runtime bug discovered in testing or production|Visible by inspection. Enum is checklist. Every name with implemented action = done. Count unimplemented = remaining work
CE4|Evolution|Add handlers, create new events, wire into existing graph. Impact requires tracing all intersecting event flows|Add names to enum. Visible in one place. Position shows domain. Implementation isolated. Sequencing explicit. Blast radius bounded

# progress_tracking(id|property|mechanism)
PT1|Visible completeness|Enum has N names. M implemented. N-M remain. Percentage meaningful because each name = unit of functionality, not unit of code
PT2|Adding feature|Add names to enum → write actions → insert into sequence
PT3|Removing feature|Remove names from enum
PT4|Refactoring|Renaming. Enum diff between versions = capability changelog

# applicability(id|fitness|description)
AP1|Exceptional|Long lifecycle flows: boot processes, order fulfillment, claims processing, manufacturing pipelines. Flow = sequence of names
AP2|Exceptional|Many interacting subsystems: operating systems, games, enterprise platforms, IoT. Each subsystem = group of names. Boundaries = group boundaries
AP3|Exceptional|Completeness-critical: medical records, financial transactions, regulatory compliance. Enum is auditable artifact — every state change listed
AP4|Less natural|Pure data transformation: compilers, image processors, numerical simulations. Complexity lives inside actions, not in sequencing. Names can describe pipeline stages but enumeration value is lower
AP5|Any scale|10 names = well-organized script. 2000 names = comprehensible platform readable in an afternoon. 2000 handlers across 200 files is not
AP6|Language agnostic|Enum can be Zig enum, Python constants, TypeScript union, database table, spreadsheet column. Carrier can be struct, dict, JSON, message queue row. Orchestrator can be loop, state machine, workflow engine, human

# worked_example(id|group|offset|names|count)
WE1|BIOS|100-199|Power_On_Self_Test, Hardware_Enumerated, Boot_Device_Selected, MBR_Loaded, Bootloader_Transferred|5
WE2|Bootloader|200-299|Stage1_Loaded, Stage2_Loaded, Kernel_Located, Kernel_Loaded_To_Memory, Initrd_Loaded, Kernel_Parameters_Set, Control_Transferred|7
WE3|Kernel|300-399|Entered, Page_Tables_Initialized, Memory_Manager_Started, Interrupt_Table_Built, Timer_Started, Console_Initialized, PCI_Bus_Enumerated, Block_Devices_Discovered, Root_Filesystem_Mounted, Initrd_Unpacked, Modules_Loaded, Root_Switched|12
WE4|Init|400-499|Process_Started, Runlevel_Determined, Hostname_Set, Sysctl_Applied, Udev_Started, Devices_Populated, Filesystems_Checked, Filesystems_Mounted, Swap_Enabled, Clock_Synchronized, Loopback_Interface_Up, Network_Interfaces_Configured, Firewall_Rules_Applied, DNS_Resolver_Configured|14
WE5|Services|500-599|Logging_Started, Dbus_Started, Cron_Started, SSH_Started, Audio_Initialized, Bluetooth_Started, Print_Spooler_Started, Network_Manager_Started, VPN_Connected|9
WE6|Display|600-699|GPU_Driver_Loaded, Framebuffer_Initialized, Server_Started, Session_Manager_Started, Login_Screen_Rendered|5
WE7|User|700-799|Credentials_Entered, Authenticated, Session_Created, Environment_Loaded, Autostart_Applications_Launched, Desktop_Rendered, Input_Ready|7
# Total: ~60 names from 7 sentences of natural language spec. Reading top to bottom = understanding the boot process without seeing source code

# relationships(from|rel|to)
P1|grounds|K1,K6,ND1
P2|grounds|P1
P3|derives_from|P1
P4|defines|K6
P5|constrains|K3,K5
P6|defines|K6 lifecycle
K1|carried_by|K2
K1|maps_to|K3
K3|sequenced_by|K4
K4|driven_by|K5
K6|contains|K1 (all instances)
ND1|prevents|refactoring, missing states, implicit transitions
ND2|enforces|K1 atomicity
CE1|distinguishes|NDD from event-driven
CE3|enables|PT1

# section_index(section|title|ids)
1|What NDD Is|P1-P4,K6
2|The Naming Act|K1,ND1-ND6
3|The Carrier|K2
4|The Action|K3,P5
5|The Sequence|K4,K5
6|How This Differs From Event-Driven|CE1-CE4
7|Spec-to-Names Pipeline|SN1-SN4
8|Refinement and Living Enum|P6,ND4,ND5,PT1-PT4
9|Worked Example: OS Boot|WE1-WE7
10|When To Use This|AP1-AP6

# decode_legend
naming_convention: Group_Verb_Noun or Group_Subject_Verb_Past. Grouped by domain, ordered by lifecycle, offsets at 100s
carrier_rule: one struct, one shape, optional fields. Never polymorphic
action_rule: one name → one action. Never inspects event type. Never calls other actions. Never decides what happens next
orchestrator_rule: only place for conditionals, branching, ordering
completeness_test: enum with all names = specification. Unimplemented names = remaining work. Enum diff = capability changelog
id_prefixes: P=principle|K=component|ND=naming_discipline|SN=spec_to_names|CE=contrast_event_driven|PT=progress_tracking|AP=applicability|WE=worked_example
