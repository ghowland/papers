# SIML — SILO MARKUP LANGUAGE (TOML FORMAT) — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → siml_sections → element_types → logic_ops → timeline → claims → relationships → sections → decode_legend

# principles(id|principle|rationale)
P1|Silo is successor to the web, not improvement of it|No backward compatibility with HTML/CSS/JS; clean break; protocols replaced not patched
P2|TOML as markup language|Human-readable, no parsing ambiguity, hand-writable in Notepad, typed, hierarchical, comments, widespread library support; natural mapping to structs
P3|Single file defines complete site|One .siml file contains site metadata, themes, styles, pages, containers, elements, commands, logic blocks, data; no build step
P4|Geocities reborn|Everyone can make site in minutes, hand-write in Notepad, customize everything, no coding knowledge required, express creativity freely; but with modern tech
P5|Zero exploits by architecture|No JavaScript execution; LogicBlocks are safe by design; no DOM manipulation; no injection surface
P6|60fps always|Entity-based rendering through Clay layout engine; no virtual DOM; direct entity updates
P7|No external dependencies|No npm, no webpack, no bundling; all capabilities built into Silo runtime (MemDB, Prolog/Siql, LogicBlocks, ContentItems)

# concepts(id|name|category|definition)
C1|SIML|core|Silo Markup Language; TOML-based format defining complete site: structure, style, behavior, data in one file
C2|Container|layout|Layout unit with type (column/row/grid), sizing, padding, alignment, children list; hierarchical nesting; responsive breakpoint overrides
C3|Element|component|Leaf UI component: text, image, button, input, textarea; has type, style reference, event handlers
C4|Style|presentation|Named style block with visual properties (background, color, padding, border_radius, font, shadow); supports hover/active/focus states; theme variable references
C5|Theme|presentation|Named color palette; styles reference via "theme.primary" etc; site.active_theme selects; switchable at runtime
C6|Page|routing|URL path → scene + container mapping; supports dynamic paths (/product/:id); title metadata
C7|Command|interaction|Named event handler mapping element on_click/on_input to logic_block + entity + params
C8|Logic Block|behavior|Ordered sequence of operations (ops) replacing JavaScript; types include get_value, scene_transition, history_push, siql_query, modify_entity, create_entity, fetch, regex_match, set_class, update_text, update_entity_data, scene_update
C9|Template|dynamic_content|Reusable component pattern for scene-driven lists; uses {{data.field}} substitution; applied by scene entity to populate empty container children
C10|Scene|runtime|Controls dynamic content population; has actors (entities), update_frequency; manages container content through entity + template binding
C11|Entity|runtime|UI_Controller or data entity in MemDB; manages container, holds data_query, references template and state_machine
C12|State Machine|behavior|UI state management with named states, transitions (from→to on trigger), on_enter animations and logic blocks; used for modals, data grids, form states
C13|Animation|presentation|Property animation with from/to/duration/easing; triggered by state machine transitions or hover/enter events
C14|Breakpoint|responsive|Named screen width ranges (mobile/tablet/desktop); containers and styles have per-breakpoint overrides via .mobile/.tablet suffixes
C15|MemDB|storage|Built-in in-memory database; TOML data sections parsed directly into MemDB; queried via Siql
C16|Siql|query|Prolog-based query language for MemDB; used in logic blocks for data retrieval and filtering
C17|ContentItems|assets|Automatic asset management system for images and media

# siml_sections(id|section|toml_key|purpose|example_keys)
SS1|Site metadata|[site]|Name, version, author, active_theme, default_page|name, version, author, active_theme, tagline
SS2|Themes|[theme.*]|Named color palettes|background, text, primary, secondary, success, error, border
SS3|Styles|[style.*]|Named visual property sets with state variants|background, color, padding, border_radius, font_size; .hover, .active, .focus, .mobile
SS4|Pages|[page.*]|URL routing to scenes and containers|path, title, scene, container; [[page.*.dynamic_paths]]
SS5|Containers|[container.*]|Layout hierarchy|layout, width, height, padding, align, justify, gap, grid_columns, children, scene, entity; .mobile, .tablet
SS6|Elements|[element.*]|Leaf components|type, text, src, style, on_click, on_input, placeholder, required, validation
SS7|Commands|[command.*]|Event→logic_block mapping|logic_block, entity, params, debounce
SS8|Logic Blocks|[[logic_block.*.ops]]|Behavioral operation sequences|type, source, result, query, entity, operation, value_var, url, method
SS9|Templates|[template.*]|Reusable dynamic component patterns|type, layout, style, [[template.*.children]] with {{data.field}}
SS10|Data|[[product]] etc|Content as TOML arrays|id, name, price, category, image, description, stock, featured
SS11|Animations|[animation.*]|Property transitions|property, from, to, duration, easing
SS12|State Machines|[state_machine.*]|UI state management|initial_state, [[states]], [[transitions]]
SS13|Breakpoints|[breakpoint.*]|Responsive width ranges|min_width, max_width

# logic_op_types(id|op_type|purpose|key_params)
LO1|get_value|Extract value from params/event/entity|source, result
LO2|scene_transition|Navigate to scene|scene or scene_from_route, scene_param
LO3|history_push|Update browser URL|url_var
LO4|siql_query|Query MemDB via Prolog|query, result
LO5|modify_entity|Change entity state|entity, operation, value_var
LO6|create_entity|Instantiate new entity|entity_type, params
LO7|fetch|HTTP request|url, method, body, result
LO8|regex_match|Pattern validation|pattern, value_var, result
LO9|set_class|Toggle element class|element, class, condition_var, condition_negate
LO10|update_text|Change element text|element, text (with {{entity.field}})
LO11|update_entity_data|Replace entity data|entity, data_var
LO12|scene_update|Refresh scene|scene

# container_layout_types(id|type|behavior)
CL1|column|Vertical stack; children top-to-bottom
CL2|row|Horizontal stack; children left-to-right
CL3|grid|CSS-grid-like; grid_columns, grid_auto_rows, gap

# element_types(id|type|properties)
ET1|text|text, font_size, font_weight, color, text_align, style
ET2|image|src, width, height, alt, object_fit, border_radius
ET3|button|text, style, on_click, enabled_var, cursor
ET4|input|input_type (text/email/search), placeholder, name, required, validation, on_input, style
ET5|textarea|placeholder, name, rows, required, max_length, on_input

# parsing_pipeline
# TOML file → Zig TOML parser → ParsedSite struct → MemDB entities
# One pass: TOML → MemDB
# Container TOML maps directly to UiContainer struct (id=hash(name), container_type, sizing, padding, align, children, scene_id, entity_id)

# what_dies(id|technology|replaced_by)
WD1|HTML|TOML containers + elements
WD2|CSS|TOML styles + themes
WD3|JavaScript|LogicBlocks (visual + safe)
WD4|npm/webpack/bundling|All built-in to runtime
WD5|React/Angular/Vue|Entity system with direct updates
WD6|Bootstrap/Tailwind|Built-in style system
WD7|DOM manipulation|Direct entity updates via MemDB

# what_exists(id|component|status)
WE1|Clay layout engine|Working
WE2|Entity rendering|Working
WE3|Event system|Working (buttons)
WE4|State machines|Working (visible in trace)
WE5|Prolog at 60fps|Working
WE6|Entity inspector|Working
WE7|Siql console|Working
WE8|ContentItems|Working
WE9|Network entities|Working
WE10|Scene system|Working
WE11|TOML parser integration|Needed (~1 week)
WE12|URL routing|Needed (~1 week)
WE13|Template substitution|Needed (~3 days)
WE14|Form validation SMs|Needed (~3 days)
WE15|Responsive breakpoints|Needed (~2 days)

# timeline(id|date|milestone)
TL1|January 2026|Game 2 ships on Silo
TL2|February 2026|Silo Web v1.0: TOML sites, 60fps, zero exploits, MCP live editing, visual LogicBlock editor
TL3|March 2026|First Silo sites: portfolios, shops, blogs, communities
TL4|Q2 2026|Geocities moment: explosion of creativity, thousands of handcrafted sites
TL5|Q3-Q4 2026|Migration: HTML→SIML converter, hosting ($5/month), domain system, Siql-powered search
TL6|2027|Critical mass: 1M+ sites, traditional web declining, major apps rewritten, SimpleMailSilo
TL7|2028|New normal: Silo Browser default, SIML standard, JavaScript legacy

# claims(id|claim|type|depends_on)
CL1|Silo is not the web but better; it is the successor to the web|axiom|P1
CL2|TOML provides zero parsing ambiguity with human-writability that HTML/CSS/JS never achieved|derivation|P2
CL3|Single .siml file replaces entire web toolchain (HTML+CSS+JS+npm+webpack+framework)|derivation|P3,P7
CL4|No JavaScript means no injection attacks, no XSS, no code execution vulnerabilities|derivation|P5,C8
CL5|LogicBlocks replace JavaScript with safe, visual, declarative operation sequences|derivation|C8,P5
CL6|Silo is an OS/universal runtime, not a browser or game engine|reframe|P1
CL7|~3 weeks of work from current state to Silo Web v1.0|estimate|WE1-WE15
CL8|Geocities died because HTML got complex; Silo won't because TOML stays simple forever|claim|P2,P4

# relationships(from|rel|to)
P1|defines|C1
P2|format_for|C1
P3|enables|P4
P5|enabled_by|C8
P6|enabled_by|WE1
P7|eliminates|WD4
C1|contains|SS1,SS2,SS3,SS4,SS5,SS6,SS7,SS8,SS9,SS10,SS11,SS12,SS13
C2|contains|C3
C2|styled_by|C4
C3|styled_by|C4
C4|references|C5
C6|routes_to|C10
C6|routes_to|C2
C7|invokes|C8
C8|queries|C16
C8|modifies|C11
C9|populates|C2
C10|manages|C11
C10|uses|C9
C11|stored_in|C15
C12|controls|C2,C3
C13|triggered_by|C12
C14|overrides|C2,C4
C15|queried_by|C16
WD1|replaced_by|C2,C3
WD2|replaced_by|C4,C5
WD3|replaced_by|C8

# section_index(section|title|ids)
1|Why TOML|P2
2|SIML in TOML Format|C1,SS1-SS10,C2,C3,C4,C5,C6,C7,C8
3|Advanced Examples|C9,C10,C11,C12,C13,C14,SS11,SS12,SS13,ET4,ET5
4|Complete E-Commerce Example|—(full worked example demonstrating all sections together)
5|TOML Parsing to Silo Structures|parsing pipeline
6|The Geocities Comparison|P4,CL8
7|The New Web Emerges|WD1-WD7,P1,P5,P6,P7,CL6
8|Timeline to Launch|WE11-WE15
9|What You Have Right Now|WE1-WE15,CL7
10|The Vision|TL1-TL7
11|You're Not Building a Browser|CL1,CL6

# decode_legend
siml_sections: site|themes|styles|pages|containers|elements|commands|logic_blocks|templates|data|animations|state_machines|breakpoints
layout_types: column|row|grid
element_types: text|image|button|input|textarea
logic_op_types: get_value|scene_transition|history_push|siql_query|modify_entity|create_entity|fetch|regex_match|set_class|update_text|update_entity_data|scene_update
status_values: Working|Needed
template_syntax: {{data.field}} for dynamic substitution
theme_reference: "theme.property_name" in style values
container_responsive: .mobile/.tablet suffix overrides on containers and styles
parsing: TOML→Zig structs→MemDB (one pass)
claim_types: axiom|derivation|reframe|claim|estimate
rel_types: defines|format_for|enables|enabled_by|eliminates|contains|styled_by|references|routes_to|invokes|queries|modifies|populates|manages|uses|stored_in|controls|triggered_by|overrides|queried_by|replaced_by
silo_identity: OS/universal runtime; successor to web; not browser, not game engine
+standalone: this doc self-contained
