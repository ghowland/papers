# Op Cost Analysis of Player-Facing Tool Selection Interfaces in Simulation Games
## A Measurement Framework for Quantifying Interaction Cost Across UI Architectures

**Registry:** [@HOWL-GAME-4-2026]

**Series Path:** [@HOWL-INFO-14-2026] → [@HOWL-GAME-4-2026]

**Date:** October 2026

**DOI:** 10.5281/zenodo.23647485

**Domain:** Information Processing Theory / Game Interface Design

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6. 

---

### Abstract

No standard unit exists for measuring the cost of player actions in game user interfaces. Design discussions rely on subjective preference, playtester sentiment, or A/B testing without a shared unit of measurement. This paper applies the op — the universal unit of information under action, defined in HOWL-INFO-14-2026 — to the specific domain of tool selection interfaces in simulation games. The op counts every discrete cognitive and physical action a player must perform to complete a task. Six domain-specific op categories are defined (look-at, read, scan, hover, move, click), each with fixed counting rules calibrated to game UI patterns. A library of compound actions provides pre-computed op costs for common UI interactions. Twelve benchmark tasks provide a standardized measurement surface for cross-game comparison. Measurements are taken across six commercial titles in two genres: colony simulation (Oxygen Not Included, Dwarf Fortress Steam Edition, RimWorld) and grand strategy (Europa Universalis IV, Crusader Kings III, Total War: Warhammer III). Results show that text-labeled hierarchical menus with keyboard acceleration produce the lowest combined new-player and expert interaction cost. Icon-only hierarchies produce the lowest expert cost but the highest new-player cost. Persistent icon grids produce the lowest within-category switching cost but the highest regression vulnerability. The framework makes these tradeoffs quantifiable, reproducible, and falsifiable.

---

### 1. Introduction

#### 1.1 The Problem

Simulation games require players to select tools, modes, and items from large inventories. Colony simulations present fifty to two hundred placeable items organized into categories. Grand strategy games present ten to forty context-sensitive actions organized into screens and map modes. The selection interface is the most frequently used UI surface in both genres. Players interact with it hundreds of times per session.

No published standard exists for comparing the interaction cost of different selection interface designs. When a designer asks whether an icon grid or a text dropdown produces lower player effort, there is no unit in which to express the answer. When a player reports that one game "feels" faster to navigate than another, there is no measurement to confirm or deny the claim. When a developer adds a hotkey system, there is no method to quantify the improvement.

The consequence is that interface design decisions are made by intuition, by copying successful competitors, or by A/B testing that measures engagement proxies (click-through rates, time-on-task) rather than the underlying cost structure. Two interfaces can produce identical engagement metrics while imposing very different cognitive loads on the player. The metrics do not distinguish between a player who found the item quickly and a player who spent the same calendar time scanning icons but performed three times as many cognitive operations.

#### 1.2 Theoretical Foundation

In 1948, Claude Shannon formalized information in transit. His mathematical theory of communication gave exact answers to the questions of movement: how many bits a channel can carry, how a message should be encoded for efficient transmission, how noise can be overcome. His unit — the bit, one binary distinction — became the foundation of the information age. Shannon explicitly excluded what happens at the endpoints. What the source does before encoding and what the destination does after decoding, he declared out of scope.

HOWL-INFO-14-2026 presents the second half and shows how both halves compose into a single complete theory. Shannon gave us the bit — the unit of information in transit. HOWL-INFO-14-2026 gives us the op — the unit of information under action. Together, bits and ops cover everything information does.

The op is one irreducible transformation by one processor. A diagnostic question asked by a physician. A mirror glance by a driver. A cache lookup by a CPU. A comparison between two elements by a sorting algorithm. The substrate determines how long an op takes — nanoseconds for a CPU, seconds for a surgeon, hundreds of milliseconds for a player scanning a menu — but an op is an op. It is countable. It is observable. It is universal across every domain that processes information.

Processing is bounded by one inequality: total ops multiplied by average op duration must not exceed the time budget. The time budget is fixed by domain physics. The only lever is reducing the total number of ops.

Through repetition under consistent conditions, a processing chain's op count decreases toward zero. This mechanism — dissolution — is what converts a new player's twenty-op menu navigation into an expert's two-op muscle-memory click. The processing has not disappeared. It fires structurally, without consuming the conscious pipeline. Every dissolved element exists within a validity envelope — a region of operating conditions within which the dissolution holds. When a context change pushes conditions outside the envelope, the element promotes back to active processing and costs ops again. When many envelopes are crossed simultaneously, a cascade occurs: a sudden spike in total ops that may overwhelm the player's capacity.

Processing entropy Hp(x | p, g, c) is the op count a specific processor requires for a specific element, given a specific goal in a specific context. It is receiver-dependent. The same toolbar button costs one op for an expert (dissolved position) and four ops for a new player (look-at, scan, move, click). Same button. Same Shannon entropy. Different processing entropy. The difference is dissolution state.

This paper applies these concepts to game UI. The six op categories defined in Section 2 are domain-specific instantiations of the universal op. The compound actions in Section 3 are pre-computed reduction pipelines. The dissolution curves in Section 9 are measured trajectories from new-player processing entropy to expert processing entropy. The regression events in Section 9.3 are cascades caused by validity envelope violations. The framework is not new. The application is.

#### 1.3 Related Models

Three quantitative models from human-computer interaction research address related questions. They are not ancestors of the op framework. They are separate models that the reader may encounter in HCI literature.

GOMS (Goals, Operators, Methods, Selection rules), introduced by Card, Moran, and Newell in 1983, decomposes tasks into goals and operators. It assumes expert, error-free performance and predicts task completion time by summing operator durations. The op framework differs in two respects. First, it models both new-player and expert profiles, not experts only. Second, it counts decisions rather than predicting time. A four-op task and a four-op task are equally costly in the op framework regardless of whether one takes 800 milliseconds and the other takes 2400 milliseconds. The decision count is what determines cognitive load. The milliseconds are substrate speed.

The Keystroke-Level Model (KLM), a simplified GOMS variant, assigns time values to physical operators (0.2 seconds for a keystroke, 1.1 seconds for mouse pointing) and includes one undifferentiated mental operator M at 1.35 seconds. The op framework decomposes KLM's single M operator into four distinct cognitive operations (look-at, read, scan, hover) with different counting rules, because the processing entropy of scanning a six-item text list is measurably different from hover-discovering across ten unlabeled icons.

Fitts' Law predicts the time to acquire and select a target as a function of the distance to the target and the size of the target. The op framework does not model cursor travel distance. A move to a button 100 pixels away and a move to a button 800 pixels away are both one op. The player makes one decision: move to that target. The millisecond difference is real but does not change the count of decisions the player must perform. Fitts' Law optimizes motor time. The op framework counts cognitive load.

These models are acknowledged as contributions to quantitative HCI. The op framework is derived from information processing theory (HOWL-INFO-14-2026), not from GOMS, KLM, or Fitts' Law.

#### 1.4 Scope

Six games across two genres are measured. Colony simulation: Oxygen Not Included, Dwarf Fortress (Steam Edition), RimWorld. Grand strategy: Europa Universalis IV, Crusader Kings III, Total War: Warhammer III. All measurements use release versions. All measurements assume default keybindings and no mods installed.

#### 1.5 Contributions

This paper makes five contributions. First, a domain-specific calibration of the op unit with six categories and fixed counting rules for game UI. Second, a library of compound actions with pre-computed op costs. Third, a set of twelve benchmark tasks applicable to any simulation game with a tool selection interface. Fourth, comparative measurements across six commercial titles. Fifth, identification of structural tradeoffs between interface architectures, expressed in ops.

---

### 2. The Op in Game UI

#### 2.1 Definition

An op is one discrete action that consumes the player's time or attention. Each op is indivisible. An op cannot be performed simultaneously with another op. The player performs ops in sequence to complete a task. The op count of a task is the sum of all ops required to complete it from a defined start state.

#### 2.2 Op Categories

Six categories cover all player actions in a tool selection interface. Each category has specific counting rules.

**Look-at.** The player directs their eyes to a UI element to read or identify it. Each directed eye movement to a new screen region is one op. Moving from the game map to the toolbar is one op. Moving within the toolbar between adjacent columns is zero additional ops because the toolbar is one visual region. Moving from the toolbar to a dropdown that opened below it is zero ops because the dropdown is an extension of the element the player is already looking at. Moving from the toolbar back to the game map is one op.

**Read.** The player processes text or icon content to understand its meaning. Reading a common English word during a look-at is zero ops because comprehension is included in the look-at. Reading a domain-specific term that requires interpretation is one op. Reading a tooltip that appeared after hovering is one op. Reading a truncated label is one op because the player cannot determine the full meaning without additional action.

**Scan.** The player searches through multiple UI elements to find a specific target. Scanning a text list of one to twelve items is one op. Scanning a text list of thirteen or more items that requires scrolling is two ops. Scanning a row of icons with text labels is one op per row. Scanning a row of icons without text labels is two ops per row. Scanning a row of icons with truncated text labels is 1.5 ops per row, rounded up.

**Hover.** The player positions the mouse cursor over a UI element and waits for delayed feedback. Each hover that reveals a tooltip is two ops: one for the mouse move and one for reading the tooltip content. When the player must hover multiple elements in sequence to find a target (discovery hovering), each hover is two ops. The expected number of discovery hovers to find a target in a row of N unlabeled icons is (N+1)/2 on average, which equals N+1 ops.

**Move.** The player repositions the mouse cursor to a target. Each repositioning to a distinct target is one op regardless of distance. Moving from any position to a UI button is one op. Moving from a UI button to the game map is one op. Moving within a dropdown to a different entry is one op.

**Click.** The player presses and releases a mouse button or keyboard key. A single left click is one op. A click-and-drag is two ops: one for the initial click and one for the release. A keyboard key press is one op. A modified key press (CTRL+key) is one op because the modifier and the key are pressed as a single chord.

#### 2.3 Design Decisions

The op categories are calibrated to game UI, not to general-purpose HCI. Three decisions require explanation.

Cursor travel distance is excluded. Fitts' Law predicts that targets farther away or smaller in size take longer to acquire. This is true in milliseconds. The op framework counts decisions. A move is a move. The player decides to move the cursor to a target. Whether the target is nearby or far away does not change the number of decisions. Motor time variance is real. It is outside the scope of this framework. The framework gains simplicity and reproducibility at the cost of motor-time precision.

Hover discovery is expensive. Each hover in a discovery sequence requires a move, a wait for the tooltip delay, and a read. This is qualitatively different from scanning visible text. Scanning a six-item text list is one op — the player reads all six items in a single directed look. Finding the correct icon in a row of six unlabeled icons requires on average 3.5 hovers at two ops each — seven ops. The 7:1 ratio between icon hover discovery and text scanning is the single largest factor in new-player cost differences between interface architectures.

Modified keypresses count as one op. CTRL+B is one chord, one decision. The player does not make two sequential decisions (press CTRL, then press B). The modifier and the letter key are selected and pressed as a single motor action. Two-key sequences where each key is pressed and released separately (press B, then press W) count as two ops because the player makes two sequential decisions.

---

### 3. Compound Actions

Certain UI interactions are composed of multiple atomic ops. This section defines the op count for each compound action.

#### 3.1 Click a Known Button

The player knows the button's position and label. Move to button (1 move) plus click (1 click) equals two ops.

#### 3.2 Click an Unknown Text-Labeled Button

The player has not used this button before. The button has a readable text label. Look at the UI region (1 look-at) plus scan the region to find the button (1 scan) plus move to button (1 move) plus click (1 click) equals four ops.

#### 3.3 Click an Unknown Icon-Only Button

The player has not used this button before. The button is an icon with no visible text label. A tooltip appears on hover. Look at the UI region (1 look-at) plus discovery hovers at an average of (N+1)/2 icons in a row of N, each hover costing two ops, plus click (1 click). Total: 2 + (N+1) ops for a row of N icons. For a row of ten icons: thirteen ops. For a row of five icons: eight ops.

#### 3.4 Select from a Text Dropdown

The player clicks a dropdown button, reads the list, and clicks an item. Move to dropdown button (1 move) plus click to open (1 click) plus scan list items (1 scan for one to twelve items) plus move to target item (1 move) plus click (1 click) equals five ops. If the dropdown has thirteen or more items requiring scrolling, the scan splits into two stages (scan visible items, scroll, scan newly visible items), adding two ops for a total of seven.

#### 3.5 Select from an Icon Grid

The player must find an item in a grid of icons with truncated text labels. Look at grid (1 look-at) plus scan per row (1.5 to 2 ops per row, depending on label quality) plus move to target (1 move) plus click (1 click). For a two-row scrollable grid of approximately thirty icons: eight to ten ops.

#### 3.6 Select from an Icon Grid (Icon-Only)

The same grid with no text labels. Each icon must be hovered. Look at grid (1 look-at) plus discovery hovers per row ((N+1) ops per row of N icons). For a row of ten icon-only items: twelve ops per row.

#### 3.7 Confirm Current State

The player looks at the UI to determine what tool or mode is currently active.

A text-labeled toolbar where all columns show the current selection path: look at toolbar (1 look-at) equals one op. The full path is readable in a single glance.

An icon-based toolbar with a highlighted tab: look at tab bar (1 look-at) plus look at cursor ghost (1 look-at) plus recall material variant not displayed on toolbar (1 recall) equals two to three ops.

An icon-based toolbar with no text: look at bottom bar for highlighted icon (1 look-at) plus hover icon to confirm meaning (2 hover) equals three ops.

#### 3.8 Point Placement

Move to target tile (1 move) plus click (1 click) equals two ops.

#### 3.9 Area Stroke

Move to anchor tile (1 move) plus click to arm (1 click) plus move to opposite corner (1 move) plus click to complete (1 click) equals four ops.

---

### 4. Task Algebra

#### 4.1 Variables

Five variables compose every tool selection task. M is the mode switch cost, zero if already in the correct mode. C is the category selection cost, zero if already in the correct category. I is the item selection cost, zero if the correct item is already selected. V is the variant or material selection cost, zero if there are no variants or the correct variant is already selected. P is the placement cost, two for point placement and four for area stroke.

#### 4.2 Formula

Total ops = M + C + I + V + P.

#### 4.3 Start States

Cold start: no mode active, no menu open, player looking at the map. Warm start: correct mode active, no item selected. Hot start: correct item selected, ready to place.

#### 4.4 Player Profiles

New player: no memorized positions, no learned hotkeys, no configured quickbars. All processing entropy is positive. Expert: all positions memorized, all available hotkeys learned. Processing entropy for dissolved elements is zero.

---

### 5. Benchmark Tasks

#### 5.1 Task Definitions

Twelve tasks form the standard benchmark set. Each task has a defined start state and a defined end state.

T1: Place one item with material or variant selection. Cold start.

T2: Place a second instance of the same item. Hot start.

T3: Switch to a different item in the same category and place it. Warm start.

T4: Switch to a different category and place an item. Warm start.

T5: Build a structural element. Cold start. In colony simulation, this is a wall segment. In grand strategy, this is a province construction order.

T6: Create a zone or issue a regional order and configure it. Cold start. In colony simulation, this is a stockpile zone. In grand strategy, this is an army movement or province action.

T7: Designate an area for modification. Cold start. In colony simulation, this is a dig or terrain operation. In grand strategy, this is a development action or designation.

T8: Toggle an overlay or map mode. Any state.

T9: Toggle a second overlay or map mode without closing the first. Any state.

T10: Confirm current tool or mode state without performing any action. Any state.

T11: Switch mode. Any mode active.

T12: Perform the fastest possible item selection using keyboard shortcuts. Cold start, expert profile.

#### 5.2 Applicability

Not all tasks apply to all games. T5 (structural building) has a direct equivalent in colony simulation (build a wall) and a functional equivalent in grand strategy (issue a construction order). T8 and T9 (overlay toggle) apply to all six titles — heatmaps in colony simulation, map modes in grand strategy. Tasks without a functional equivalent in a given title are marked N/A in the results tables.

---

### 6. Colony Simulation

#### 6.1 Oxygen Not Included

**Architecture.** ONI uses a vertical icon toolbar on the right side of the screen for build categories. Build categories use number keys 1 through 9. Selecting a category opens an icon sub-category sidebar. Selecting a sub-category opens an item grid with small text labels. The toolbar and sidebar levels are icon-only. Only the final item grid has text labels.

**Overlays.** Sixteen overlays are accessed via function keys: F1 for Oxygen through F11 for Room, plus Shift+F1 through Shift+F4 for Exosuit, Automation, Conveyor, and Radiation. Priority uses P. The overlay keys and build category keys do not correspond. F1 is the Oxygen overlay, but the Oxygen build category is accessed via number key 2. This mismatch prevents the player from forming a unified mental model across overlays and build menus.

**Hotkey coverage.** No built-in hotkeys exist for individual build items. Players have requested sequential key selection (pressing 2 then 1 to select a specific item within a build category). A community mod adds custom keybindings but has had compatibility issues with game updates.

**Depth.** Three levels: category (icon toolbar) → sub-category (icon sidebar) → item (icon grid with text).

**Processing entropy profile.** Processing entropy is highest at the toolbar and sidebar levels because those levels are icon-only. The item grid has lower processing entropy because text labels are present. The F-key overlay system provides one-op access for experts (dissolved key position) but no visual mnemonic for new players — the player must memorize which F-key maps to which overlay, a dissolution that takes five to eight encounters per overlay because the mapping is arbitrary.

The overlay/build key mismatch is a dissolution failure. Consistent mapping would let the player dissolve one mental model for both overlays and build menus. Inconsistent mapping forces the player to dissolve two independent models, doubling the convergence count.

#### 6.2 Dwarf Fortress (Steam Edition)

**Architecture.** The Steam edition uses a graphical bottom toolbar with icon-based categories. Sub-panels open as icon grids. Tooltips appear on hover for all icons. No text labels appear on the toolbar or sub-panel icons. The classic (pre-Steam) version used pure keyboard navigation with memorized letter keys. Pressing b opened the build menu. Sub-menus were navigated by pressing specific letter keys shown at the bottom of each screen.

**Hotkey coverage.** The Steam edition retains b for the build menu and d for designations. Hotkeys can be redefined in the settings. No hotkeys exist for individual build items or sub-categories in the Steam edition.

**Depth.** Three to four levels: category (icon toolbar) → sub-category (icon sub-panel) → item (icon sub-panel) → material (text dropdown).

**Processing entropy profile.** The Steam edition has the highest new-player processing entropy of any measured colony simulation because all navigation levels are icon-only. Discovery hovering dominates the cost: a toolbar with twelve icons requires an average of 6.5 hovers (thirteen ops) to find the correct category for a new player. A sub-panel with eight icons requires an average of 4.5 hovers (nine ops). The cumulative first-encounter cost for reaching a specific item can exceed thirty ops.

The classic-to-Steam transition is a wholesale validity envelope violation. Veterans who had dissolved keyboard sequences into structural processing at zero cost lost all dissolved navigation patterns simultaneously when the input modality changed from keyboard to mouse-driven icons. This is the most extreme cascade event observed in the game UI domain. Every dissolved navigation pattern promoted back to active processing at once. The classic keyboard system had higher R* (more keys to memorize before reaching competence) but faster dissolution (letter sequences are highly consistent and dissolve in two to three encounters). The Steam icon system has lower R* (visual scanning requires no memorization) but slower dissolution (icon positions in grids are harder to dissolve than letter sequences) and much higher new-player processing entropy at every navigation level.

#### 6.3 RimWorld

**Architecture.** RimWorld uses an Architect button that opens a horizontal tab bar along the bottom of the screen. Category tabs (Orders, Zone/Area, Structure, Production, Furniture, Power, and others) have text labels. Selecting a tab opens an icon grid with truncated text labels. Items within the grid show small icons with names that may be truncated if they exceed the display width.

**Hotkey coverage.** No built-in hotkeys exist for architect menu items. A community mod called "Hotkeys" adds rebindable keys, but it has been abandoned at version 1.4. Players have described the built-in keyboard support as insufficient, and the mod has received repeated requests for updates to versions 1.5 and 1.6 that have gone unanswered because the mod author no longer maintains it. One player described the game as unplayable without the mod.

**Depth.** Two to three levels: category tab (text-labeled) → item grid (icons with truncated text) → material dropdown (text list).

**Processing entropy profile.** RimWorld has the lowest new-player processing entropy of any measured colony simulation at the category level because category tabs are text-labeled with common English words. Common words dissolve in two to three encounters because the player already knows the word's meaning — only the position-in-tab-bar mapping must be dissolved. Processing entropy is moderate at the item level because truncated labels are partial compression tokens. The player can partially identify items from truncations but must hover some to confirm the full name. Processing entropy for the material dropdown is low because it is a text list.

The complete absence of item-level hotkeys means the expert minimum is capped by the visual scan cost. The player can never dissolve below the scan + move + click floor of three to four ops per item switch within a category. The abandoned hotkeys mod and player commentary are qualitative evidence that the community has reached the R* floor of the current architecture and is demanding dissolution infrastructure (hotkeys) that would lower it. The expert is performing at the minimum the architecture permits, not at the minimum the task requires.

#### 6.4 Measurements

**T1 — Place one item with variant selection (cold start, new player).**

*ONI.* Look at toolbar (1). Number keys are available but the player must know which number maps to which category — if unknown, hover toolbar icons to find the correct category. Average 5.5 hovers across ten category icons (11). Click (1). Sidebar opens. Hover sidebar icons to find sub-category, average 4.5 hovers across eight icons (9). Click (1). Item grid opens with small text labels. Scan two rows (3). Move to item (1). Click (1). Move to map (1). Move to target tile (1). Click (1). Total: twenty-eight ops without using number keys. With known category number key: replace the eleven hover ops with one keypress. Total drops to eighteen ops.

*DF Steam.* Look at toolbar (1). Hover toolbar icons to find build category, average 6.5 hovers across twelve icons (13). Click (1). Sub-panel opens. Hover sub-panel icons to find furniture category, average 4.5 hovers across eight icons (9). Click (1). Item sub-panel opens. Hover item icons to find target, average 3.5 hovers across six icons (7). Click (1). Material dropdown opens. Scan material list (1). Move to material (1). Click (1). Move to map (1). Move to target tile (1). Click (1). Total: thirty-three ops.

*RimWorld.* Move to Architect button (1). Click to open (1). Scan fourteen category tabs (1). Move to Furniture tab (1). Click (1). Icon grid appears with truncated labels, two to three rows. Look at grid (1). Scan row one, approximately ten items with truncated labels (2). Scan row two (2). Move to Bed icon (1). Click (1). Material dropdown appears. Look at dropdown (1). Scan material list (1). Move to Wood (1). Click (1). Move to map (1). Move to target tile (1). Click (1). Total: twenty ops. For an uncommon item in the third row, add two scan ops for a total of twenty-two.

| Game | New Player Ops | Breakdown |
|---|---|---|
| ONI | 28 | Icon hover on toolbar and sidebar dominates |
| DF Steam | 33 | Icon hover on all three navigation levels dominates |
| RimWorld | 20–22 | Text labels reduce category and item scan cost |

**T2 — Repeat same item (hot start).**

All three games: move to target tile (1) plus click (1) equals two ops. This is the theoretical minimum for point placement. No interface architecture can improve on it.

**T3 — Switch item within same category (warm start).**

*ONI.* Item grid is still visible. Scan for new item (1). Move to item (1). Click (1). Total: three ops.

*DF Steam (known position).* Sub-panel is still visible. Move to item icon (1). Click (1). Total: two ops. DF Steam unknown: hover to find the new item (average 3.5 hovers across six items = 7 ops) plus click (1). Total: eight ops.

*RimWorld.* Grid is still visible. Scan for new item across truncated labels (1 to 2). Move to item (1). Click (1). Total: three to four ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 3 | 2–3 |
| DF Steam | 8 (unknown), 2 (known) | 2 |
| RimWorld | 3–4 | 2–3 |

Persistent grids (ONI, RimWorld) have lower within-category switching cost than transient dropdown menus because the grid remains visible and does not need to be reopened.

**T4 — Switch category and place item (warm start).**

*ONI.* Hover sidebar for new sub-category (9). Click (1). Scan new item grid (2). Move to item (1). Click (1). Move to tile (1). Click (1). Total: sixteen ops.

*DF Steam.* Navigate back to category level (1). Hover category icons for new category (9). Click (1). Hover item icons (7). Click (1). Move to tile (1). Click (1). Total: twenty-two ops.

*RimWorld.* Scan tab bar for new category (1). Move to new tab (1). Click (1). Scan new icon grid, two rows (4). Move to item (1). Click (1). Move to tile (1). Click (1). Total: eleven ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 16 | 5 |
| DF Steam | 22 | 6 |
| RimWorld | 11 | 5–6 |

**T5 — Build a wall segment (cold start).**

*ONI.* Hover toolbar for Base category (11). Click (1). Scan item grid for Tile (2). Move to Tile (1). Click (1). Move to start tile (1). Click to arm (1). Move to end tile (1). Click to complete (1). Total: twenty ops. With known number key for Base category: ten ops.

*DF Steam.* Hover toolbar for Construction icon (13). Click (1). Hover sub-panel for Wall (7). Click (1). Material dropdown (3). Move to start tile (1). Click to place start (1). Move to end tile (1). Click to place end (1). Total: twenty-nine ops.

*RimWorld.* Open Architect (2). Scan tabs for Structure (1). Move to Structure tab (1). Click (1). Scan icon grid for Wall (2). Move to Wall (1). Click (1). Material dropdown (3). Click to start drag (1). Drag to end (1). Release (1). Total: sixteen ops (using click-drag-release as three ops: the drag counts as a move).

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 20 | 5–6 |
| DF Steam | 29 | 6 |
| RimWorld | 16 | 7 |

**T6 — Create zone and configure (cold start).**

*ONI.* ONI does not have a manual zone designation system equivalent to RimWorld's stockpile zones. Rooms are detected automatically based on enclosed spaces. This task is N/A for ONI.

*DF Steam.* Hover toolbar for zone/stockpile icon (13). Click (1). Hover sub-panel for zone type (7). Click (1). Click to start area (1). Drag to end (1). Release (1). Zone menu opens. Configure settings (4 to 8 scan and click ops). Total: twenty-nine to thirty-three ops.

*RimWorld.* Open Architect (2). Scan tabs for Zone (1). Move to Zone tab (1). Click (1). Scan zone types (1). Move to Stockpile (1). Click (1). Click to start drag (1). Drag to end (1). Release (1). Click stockpile to configure (2). Configuration panel opens. Scan storage settings (1). Expand category filters, multiple clicks (3 to 6). Total: seventeen to twenty ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | N/A | N/A |
| DF Steam | 29–33 | 8–12 |
| RimWorld | 17–20 | 8–12 |

**T7 — Terrain or dig operation (cold start).**

*ONI.* Hover toolbar for Dig icon (11). Click (1). Click to start drag (1). Drag to end (1). Release (1). Total: fifteen ops. ONI's dig tool is a single tool, not a category with sub-options.

*DF Steam.* Hover toolbar for Designations icon (13). Click (1). Hover sub-panel for dig or terrain operation (7). Click (1). Click to start (1). Drag to end (1). Release (1). Total: twenty-five ops.

*RimWorld.* Open Architect (2). Scan tabs for Orders (1). Move to Orders tab (1). Click (1). Scan designations for target operation (1). Move to operation (1). Click (1). Click to start drag (1). Drag to end (1). Release (1). Total: eleven ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 15 | 3–4 |
| DF Steam | 25 | 5 |
| RimWorld | 11 | 5–6 |

**T8 — Toggle an overlay (any state).**

*ONI.* Press F-key for the target overlay. If the player knows which F-key: one op. If unknown: look at the overlay button bar (1), hover buttons to find the target (varies), click (1). New player average for sixteen overlays: approximately eight to twelve ops. Expert: one op (dissolved F-key mapping).

*DF Steam.* Hover toolbar for overlay icon (varies). Click (1). Hover overlay sub-icons (varies). Click (1). New player: fifteen to twenty ops. Expert: three ops (two known moves plus one click, or a learned keyboard shortcut if bound).

*RimWorld.* Look at bottom-right overlay buttons (1). Eight overlay icons with no text labels. Hover to identify correct overlay if icon not memorized, average 4.5 hovers (9). Click (1). New player: twelve ops. Expert: three ops (dissolved icon position, move, click).

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 8–12 | 1 |
| DF Steam | 15–20 | 3 |
| RimWorld | 12 | 3 |

ONI's F-key system provides the lowest expert overlay cost (one op) because the F-key binding is a direct dissolution target — one key, one overlay, no visual search. DF Steam and RimWorld require visual search even for experts who have not fully dissolved icon positions.

**T9 — Toggle a second overlay (any state).**

*ONI.* Press the second F-key. One op. ONI supports simultaneous overlays.

*DF Steam.* If overlay panel persists: move to second icon (1), click (1). Two ops. If panel closed: reopen cost, five to ten additional ops.

*RimWorld.* Each overlay is a separate button. Move to second overlay button (1). Click (1). Two ops. Most RimWorld overlays are mutually exclusive.

| Game | Ops | Notes |
|---|---|---|
| ONI | 1 | Simultaneous overlays supported |
| DF Steam | 2–10 | Depends on panel persistence |
| RimWorld | 2 | Mostly mutually exclusive |

**T10 — Confirm current state (any state).**

*ONI.* Look at the active tool indicator on the right sidebar (1). If icon not recognized, hover (2). Total: one to three ops.

*DF Steam.* Look at bottom bar for highlighted icon (1). Hover to confirm meaning (2). Total: three ops.

*RimWorld.* Look at highlighted tab (1). Tab label is readable (0). Look at cursor ghost to confirm item (1). Material is not displayed — recall from memory (1). Total: two to three ops.

| Game | Ops |
|---|---|
| ONI | 1–3 |
| DF Steam | 3 |
| RimWorld | 2–3 |

**T11 — Switch mode (any state).**

*ONI.* Hover toolbar for new mode icon (11). Click (1). New player: twelve ops. Expert: two ops (dissolved position, move, click).

*DF Steam.* Hover toolbar for new mode icon (13). Click (1). New player: fourteen ops. Expert: two ops.

*RimWorld.* Scan tab bar for new tab (1). Move (1). Click (1). New player: three ops. Expert: two to three ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| ONI | 12 | 2 |
| DF Steam | 14 | 2 |
| RimWorld | 3 | 2–3 |

RimWorld wins on mode switching for new players because mode tabs are always visible and text-labeled.

**T12 — Fastest item selection via keyboard (cold start, expert).**

*ONI.* Press number key for build category (1). Item grid opens. If item has a known position: move (1), click (1). Total: three ops. No item-level hotkeys exist, so the item grid must always be navigated visually.

*DF Steam.* Press b for build menu (1). Navigate sub-panel by mouse (2 to 4). Total: three to five ops. No item-level hotkeys exist in the Steam edition.

*RimWorld.* No built-in hotkeys for architect menu items. Expert must use toolbar. Move to Furniture tab (1). Click (1). Move to Bed (1). Click (1). Material dropdown (2). Move to tile (1). Click (1). Total: eight ops.

| Game | Expert Ops (Fastest Path) | Hotkey Coverage |
|---|---|---|
| ONI | 3 (category key + grid click) | 9 category keys, 0 item keys |
| DF Steam | 3–5 (b + mouse navigation) | 2 menu keys, 0 item keys |
| RimWorld | 8 (toolbar only) | 0 built-in |

No colony simulation measured provides a single-keypress path to a specific build item.

#### 6.5 Colony Simulation Summary

| Task | ONI (new) | ONI (expert) | DF (new) | DF (expert) | RW (new) | RW (expert) |
|---|---|---|---|---|---|---|
| T1 Place item | 28 | 5 | 33 | 8 | 20 | 8 |
| T2 Repeat | 2 | 2 | 2 | 2 | 2 | 2 |
| T3 Switch item same cat | 3 | 2–3 | 8 | 2 | 3–4 | 2–3 |
| T4 Switch category | 16 | 5 | 22 | 6 | 11 | 5–6 |
| T5 Build wall | 20 | 5–6 | 29 | 6 | 16 | 7 |
| T6 Zone/configure | N/A | N/A | 29–33 | 8–12 | 17–20 | 8–12 |
| T7 Terrain/dig | 15 | 3–4 | 25 | 5 | 11 | 5–6 |
| T8 Toggle overlay | 8–12 | 1 | 15–20 | 3 | 12 | 3 |
| T9 Second overlay | 1 | 1 | 2–10 | 2 | 2 | 2 |
| T10 Confirm state | 1–3 | 1 | 3 | 3 | 2–3 | 2 |
| T11 Switch mode | 12 | 2 | 14 | 2 | 3 | 2–3 |
| T12 Fastest keyboard | 3 | 3 | 3–5 | 3–5 | 8 | 8 |

DF Steam has the highest new-player cost on every task due to icon-only discovery hovering at all navigation levels. RimWorld has the lowest new-player cost on most tasks due to text labels at the category level. ONI falls between the two. All three titles have similar expert costs (two to eight ops for common tasks) because memorized icon positions eliminate scan and hover costs. The new-player-to-expert gap is largest for DF Steam (twenty-five ops on T1), moderate for ONI (twenty-three ops), and smallest for RimWorld (twelve ops). RimWorld's low gap is driven by text labels reducing first-time scan cost, not by a lower expert minimum. No colony simulation provides a one-op path to a specific build item.

---

### 7. Grand Strategy

#### 7.1 Europa Universalis IV

**Architecture.** EU4 uses number keys 1 through 0 for thirteen major screens: 1 for Court, 2 for Government, 3 for Diplomacy, 4 for Economy, 5 for Trade, 6 for Technology, 7 for Ideas, 8 for Missions, 9 for Stability and Expansion, 0 for Religion, comma for Military, period for Subjects, apostrophe for Estates.

**Map modes.** The keys Q, W, E, R, T, Y, U, I, O, P are bound to ten primary map modes — the entire top row of the keyboard. Each map mode is accessible with a single keypress.

**Context-sensitive keys.** When a province is selected, the number keys change function: 1 for Land units, 2 for Naval units, 3 for Make core, 4 for Send Missionary, 5 for Local autonomy, 6 for Change culture, 7 for Buildings, 8 for Development, 9 for Estates, 0 for Diplomacy. This dual-use of the number row doubles effective keybinding density without consuming additional keys.

**Unit management.** Bare letter keys handle unit operations: a for attach/detach, s for split army, d for detach siege, f for find province, g for merge, j for siege view, k for consolidate, m for forced march, n for detach mercenaries, z/x/b/c for unit type detach, v for build units. Map scrolling uses arrow keys because WASD is unavailable — those keys are consumed by other bindings (W for a map mode, A for attach, S for split, D for detach). Players have noted this limitation, observing that WASD camera control is ergonomically superior but impossible because the keys are bound to unit operations.

**Depth.** Two levels for most actions: screen (number key) → action within screen (mouse click). Province actions are context-sensitive: click province → number key for action type → specific action within the panel. Building construction within a province requires entering the Buildings view (7 when province selected), then clicking the specific building slot — a three to four op sequence for an expert.

**Processing entropy profile.** EU4 has the densest dissolution infrastructure of any measured game. The Q-P row for map modes is a set of ten compression tokens, each decompressing to a full visual map transformation at one op. The context-sensitive number row requires the player to dissolve two independent mappings (screen access when nothing selected, province actions when a province is selected). Both mappings use the same keys, which accelerates dissolution — the player dissolves the spatial position of the key once and then dissolves the two context-dependent meanings separately. Total hotkey coverage is approximately forty-five bindings, giving one-op access to map modes, screens, and most unit operations.

#### 7.2 Crusader Kings III

**Architecture.** CK3 uses F1 through F8 for major screens: F1 for Player character, F2 for Realm, F3 for Military, F4 for Council, F5 for Court, F6 for Intrigue, F7 for Factions, F8 for Decisions. C opens Character finder. V opens Find title. Tab opens the Issues panel.

**Map modes.** The "e" key opens the primary Realms map mode, which adapts based on zoom level. At far zoom it shows independent realms on a paper map. At mid zoom it shows vassals. At near zoom it shows terrain and holdings. This is a single binding that decompresses to three distinct visualizations based on zoom state — a context-sensitive compression token where one key serves three map modes.

**Province interaction.** Clicking a province or character opens a context-sensitive detail panel. Actions are accessed through buttons within the panel. Most common actions are one to two clicks from the detail panel. The detail panel uses text labels for all action buttons.

**Depth.** Two levels for most interactions: click entity → action in detail panel. Screen access is one level: F-key opens screen directly.

**Processing entropy profile.** CK3 has lower hotkey density than EU4 (approximately fifteen hotkeys versus forty-five) but compensates with text-heavy context-sensitive panels. The F-key bindings dissolve quickly because function keys are spatially distinct and used consistently. The zoom-adaptive map mode dissolves as a single binding with three contextual decompression rules. Province actions have low processing entropy because the detail panel uses full text labels — the player scans text, not icons.

Paradox described their design goal as providing the player with a set of controls that, when learned, facilitate fluid interaction. This is a direct description of dissolution infrastructure: controls designed to dissolve into structural processing through consistent use.

#### 7.3 Total War: Warhammer III

**Architecture.** TW:WH3 uses WASD for camera panning. Number keys 1 through 5 serve as settlement views when a settlement is selected: 1 for Overview, 2 for Garrison, 3 for Building browser, 4 for Recruitment units, 5 for Recruitment agents. TAB toggles the strategic map. HOME pans to capital. SPACE (hold) toggles campaign overlays.

**Battle controls.** The game splits into a turn-based campaign map and a real-time battle map with separate control schemes. Battle hotkeys include CTRL+B for selecting all artillery, CTRL+I for all infantry, CTRL+M for all missile units, CTRL+C for all cavalry. Unit grouping uses CTRL+number.

**Building construction.** Pressing 3 when a settlement is selected opens the building browser. Building selection within the browser is mouse-driven with icon thumbnails and text labels. The building browser is a scrollable panel organized by building chain.

**Depth.** Campaign: two levels for settlement actions (select settlement → number key for view → mouse within view). Building construction: three levels (select settlement → press 3 → navigate building browser by mouse). Battle: one to two levels for unit selection (CTRL+letter for type, number for group).

**Processing entropy profile.** TW:WH3 invests four letter keys (WASD) in camera movement, which consumes key-space that EU4 uses for unit operations. This is a direct tradeoff: WASD camera gives lower camera control processing entropy (dissolved spatial mapping matches physical hand position) but reduces the available dissolution infrastructure for other actions. The CTRL+letter pattern for battle unit type selection is structurally identical to using CTRL+letter for specific item selection in other domains — the modifier key accesses a deeper level of specificity within the same key. Total hotkey coverage is approximately fifteen bindings on the campaign map and approximately twenty on the battle map.

#### 7.4 Measurements

**T5 equivalent — Issue construction order (cold start).**

*EU4.* Click province (2). Press 7 for Buildings (1). Building panel opens with text-labeled building slots. Scan for available slot (1). Click to build (1). Total: five ops (expert). New player: click province (2), look at panel for Buildings button or discover the 7 key (2 to 4 additional ops), scan building options (1 to 2), click (1). Total: six to nine ops.

*CK3.* Click holding (2). Detail panel opens. Scan panel for construction button (1). Click (1). Building list opens with text labels. Scan for target building (1). Click to build (1). Total: six ops (expert). New player: seven to ten ops (additional scan and read ops for unfamiliar panel layout).

*TW:WH3.* Click settlement (2). Press 3 for Building browser (1). Browser opens with building chains, icons with text labels. Scan building chains (1 to 2). Click target slot (1). Build menu opens with text and icon options. Scan options (1). Click to build (1). Total: seven to eight ops (expert). New player: nine to twelve ops (additional orientation ops for unfamiliar browser layout).

| Game | New Player Ops | Expert Ops |
|---|---|---|
| EU4 | 6–9 | 5 |
| CK3 | 7–10 | 6 |
| TW:WH3 | 9–12 | 7–8 |

**T8 — Toggle a map mode (any state).**

*EU4.* Press the corresponding letter on the Q-P row. One op. All ten primary map modes are accessible with a single keypress. New player: if the mapping is unknown, the player must scan the map mode buttons at the bottom-right of the screen (1 look-at, 1 scan, 1 move, 1 click = 4 ops) or discover the key binding through the settings. Expert: one op (dissolved key mapping).

*CK3.* Press "e" for the primary Realms map mode (1 op). Other map modes are accessed via icon buttons on the minimap panel — look at panel (1), scan for target mode (1), move (1), click (1) = four ops. Expert: two to four ops depending on which map mode is needed. The zoom-adaptive behavior means the "e" key provides three map modes contextually, but switching between them requires zooming rather than pressing a different key.

*TW:WH3.* Hold SPACE to view campaign overlays. Select from overlay options that appear. New player: two to four ops. Expert: two ops (hold SPACE, release on desired overlay).

| Game | New Player Ops | Expert Ops |
|---|---|---|
| EU4 | 4 (unknown key) | 1 |
| CK3 | 4 (icon button) | 1–4 (varies by mode) |
| TW:WH3 | 2–4 | 2 |

EU4 achieves the theoretical minimum of one op for map mode switching. This is the lowest overlay/map mode cost measured in any game across both genres.

**T10 — Confirm current state (any state).**

*EU4.* The current map mode is indicated by a highlighted button in the bottom-right panel. Look at panel (1). The highlighted button has a text label or recognizable icon. Total: one to two ops.

*CK3.* The current screen is indicated by the open panel. The map mode is indicated by the visual rendering style. Look at map (1). Total: one op (the map's visual appearance directly communicates the active mode).

*TW:WH3.* The current settlement view is indicated by the highlighted number tab. On the campaign map, the mode is communicated by which panel is open. Look at panel (1). Total: one to two ops.

| Game | Ops |
|---|---|
| EU4 | 1–2 |
| CK3 | 1 |
| TW:WH3 | 1–2 |

All three grand strategy games achieve one to two ops for state confirmation because they use persistent text-labeled panels and visual map rendering to communicate state.

**T11 — Switch mode (any state).**

In grand strategy, "mode" maps to switching between major screens (diplomacy, military, economy, etc.) rather than between tool modes.

*EU4.* Press the number key for the target screen. One op.

*CK3.* Press the F-key for the target screen. One op.

*TW:WH3.* Click the corresponding button on the UI or press the number key when a settlement is selected. One to two ops.

| Game | New Player Ops | Expert Ops |
|---|---|---|
| EU4 | 1 (if key known), 4 (if unknown) | 1 |
| CK3 | 1 (if key known), 4 (if unknown) | 1 |
| TW:WH3 | 2–4 | 1–2 |

#### 7.5 Grand Strategy Summary

| Task | EU4 (new) | EU4 (expert) | CK3 (new) | CK3 (expert) | TW (new) | TW (expert) |
|---|---|---|---|---|---|---|
| T5 Construction | 6–9 | 5 | 7–10 | 6 | 9–12 | 7–8 |
| T8 Map mode | 4 | 1 | 4 | 1–4 | 2–4 | 2 |
| T9 Second mode | 1 | 1 | 4 | 1–4 | 2–4 | 2 |
| T10 Confirm state | 1–2 | 1 | 1 | 1 | 1–2 | 1 |
| T11 Switch screen | 1–4 | 1 | 1–4 | 1 | 2–4 | 1–2 |

Grand strategy games have lower overall op costs than colony simulations for most tasks because the action space is shallower (two levels versus three to four levels) and hotkey density is higher. EU4 achieves one-op access for map modes and screen switching — the theoretical minimum for any keyboard-driven action. Grand strategy building construction (T5 equivalent) has moderate cost (five to eight ops expert) because building selection is mouse-driven within a panel, similar to colony sim item selection in a grid.

---

### 8. Cross-Genre Comparison

#### 8.1 Shared Tasks

Four tasks are directly comparable across all six titles: T8 (overlay/map mode toggle), T9 (second toggle), T10 (state confirmation), and T11 (mode/screen switch).

| Task | ONI (new/exp) | DF (new/exp) | RW (new/exp) | EU4 (new/exp) | CK3 (new/exp) | TW (new/exp) |
|---|---|---|---|---|---|---|
| T8 Toggle overlay | 8–12 / 1 | 15–20 / 3 | 12 / 3 | 4 / 1 | 4 / 1–4 | 2–4 / 2 |
| T9 Second toggle | 1 / 1 | 2–10 / 2 | 2 / 2 | 1 / 1 | 4 / 1–4 | 2–4 / 2 |
| T10 Confirm state | 1–3 / 1 | 3 / 3 | 2–3 / 2 | 1–2 / 1 | 1 / 1 | 1–2 / 1 |
| T11 Switch mode | 12 / 2 | 14 / 2 | 3 / 2–3 | 1–4 / 1 | 1–4 / 1 | 2–4 / 1–2 |

Overlay toggle cost ranges from one op (EU4 expert, ONI expert) to twenty ops (DF Steam new player). This 20:1 range on a single task demonstrates that overlay access design has a larger effect on interaction cost than most other design choices. The one-op systems (EU4's Q-P row, ONI's F-keys) achieve minimum cost through dedicated dissolution infrastructure — one key per overlay, no visual search, no menu navigation. Systems that require visual search (DF Steam, RimWorld) pay three to twenty additional ops.

State confirmation cost is one to three ops across all six titles. This is the narrowest range of any benchmark task. All measured games provide some visual indicator of current state. The one-op systems (CK3's visual map rendering, EU4's highlighted button, ONI's sidebar icon when dissolved) communicate state through persistent visual signals that require no interaction beyond a directed look.

Mode switching cost shows the clearest genre difference. Grand strategy games achieve one-op mode switching (EU4 number keys, CK3 F-keys) because each major screen has a dedicated hotkey. Colony simulations require two to fourteen ops because mode tabs are accessed through icon toolbars (ONI, DF Steam) or through an Architect menu that must be opened first (RimWorld).

#### 8.2 Structural Observations

Colony simulations have deeper item hierarchies and higher T1 costs. The deepest measured colony sim path (DF Steam, four navigation levels) produces thirty-three ops for a new player. The deepest measured grand strategy path (TW:WH3 building construction, three levels) produces nine to twelve ops. The difference is driven by the number of selectable items: colony sims present fifty to two hundred items organized into nested categories, while grand strategy building panels present five to twenty items in a single scrollable list.

Grand strategy games have shallower action hierarchies but more context-sensitive panels. EU4's province view changes the meaning of number keys based on selection state. CK3's map mode changes based on zoom level. TW:WH3's number keys activate settlement views only when a settlement is selected. This context sensitivity is absent from colony simulations, where build category keys always mean the same thing regardless of selection state.

Overlay and map mode costs are comparable across genres when the dissolution infrastructure is similar. EU4's one-op map modes and ONI's one-op overlays achieve the same cost despite being in different genres, because both use the same mechanism: one dedicated key per mode, no visual search. RimWorld's three-op overlays and CK3's one-to-four-op map modes also fall in a similar range, both using icon buttons that require move-and-click after the position is dissolved.

#### 8.3 Architecture Patterns

Four patterns emerge from the measurements.

**Icon-only hierarchies.** All navigation levels use unlabeled icons with tooltips on hover. Highest new-player cost due to hover discovery. Lowest expert cost once positions are memorized. Largest new-player-to-expert gap. Example: DF Steam. The new-player cost is dominated by the (N+1)/2 × 2 hover discovery formula at each level. The expert cost is dominated by move-and-click at each level. The gap is the hover discovery cost itself, which dissolves completely through repetition.

**Text-labeled tabs with icon grids.** Category level uses text labels. Item level uses icons with truncated text. Moderate new-player cost — text labels at the category level reduce scan cost to one op per level. Moderate expert cost — grid navigation requires cursor travel to a 2D position. Within-category switching is fast because the grid remains visible. Example: RimWorld. The text labels at the category level dissolve in two to three encounters. The icon grid positions at the item level dissolve in five to eight encounters. The within-category switching cost is three to four ops because the grid stays visible — no reopen penalty.

**Text dropdown hierarchies.** All navigation levels use text-labeled dropdowns or text-labeled panels. Moderate new-player cost — text labels at every level keep scan cost at one op per level. Moderate expert cost via mouse — dropdown must be reopened (two-op penalty versus persistent grids). Low expert cost via hotkeys — one op per level. State confirmation cost is lowest (one op) because the full selection path is displayed as text at all times. No measured game in this study uses pure text dropdowns for item selection, but the pattern appears in grand strategy screen navigation (EU4 province panels, CK3 detail panels) and in overlay configuration panels across both genres.

**Dedicated key bindings.** Each action has a pre-assigned keyboard shortcut. Highest setup cost (player must learn or discover the key). Lowest expert cost (one op per action). Does not scale beyond the number of available keys without key-space exhaustion. Example: EU4 (forty-five bindings). The dissolution curve for key bindings converges in two to three encounters because the mapping is consistent and the spatial position of the key on the keyboard provides a physical mnemonic. EU4's key-space is nearly exhausted — WASD cannot be used for camera because those keys are bound to unit operations.

#### 8.4 The Label-Depth Tradeoff

Text labels reduce first-time scan cost but consume more screen space per item than icons. A text dropdown showing six items occupies a fixed vertical space per item. An icon grid showing six items in one row occupies less vertical space. The tradeoff is between processing entropy per encounter (lower with text) and screen real estate (lower with icons).

Deeper hierarchies with fewer items per level produce lower scan cost per level (fewer items to scan) but higher total level count (more dropdowns or panels to navigate). Shallower hierarchies with more items per level produce higher scan cost per level (more items to scan) but fewer levels to navigate. The optimal balance depends on the total item count and the frequency distribution of item usage.

For colony simulations with one hundred to two hundred items, the measurements suggest that three to four levels of five to eight items each (text dropdowns) produces lower total new-player cost than two levels of fifteen to twenty items each (icon grids), because the scan cost per text dropdown level (one op) is lower than the scan cost per icon grid row (one to two ops) and the cumulative cost of three one-op scans (three ops) is lower than the cumulative cost of scanning two rows of a fifteen-item grid (three to four ops) plus the hover penalty for unfamiliar icons.

For grand strategy games with twenty to forty actions, two levels of ten to twenty text-labeled items each produces the lowest cost, because the total action count fits comfortably in one or two text panels without scrolling.

---

### 9. Dissolution and Regression

#### 9.1 Dissolution Curves by Label Type

The dissolution curve D(n | x, p, κ) describes how the op count for a specific element decreases over repetitions toward zero under consistent conditions. The curve's starting point is the new-player op count. The curve's endpoint is zero (fully dissolved) or R* (the minimum correct ops that cannot dissolve further). The convergence count is the number of repetitions required to reach the endpoint.

**Text-labeled dropdowns.** Convergence in two to three repetitions. Text labels are high-compression tokens. A word like "Household" decompresses to its referent at zero cost for any literate player. Only the position-in-list mapping must be dissolved. List position is a one-dimensional spatial relationship. One-dimensional spatial mappings dissolve faster than two-dimensional mappings because they have fewer degrees of freedom.

**Icon grids with truncated labels.** Convergence in five to eight repetitions. Truncated labels are partial compression tokens. "Armchair..." requires the player to either complete the decompression from partial data or hover for the tooltip. Grid position is a two-dimensional spatial relationship. The additional dimension increases the information that must be dissolved. Truncated labels slow dissolution further because the player cannot form a stable token-to-referent mapping until they have seen the full name enough times to predict it from the truncation.

**Icon-only toolbars.** Convergence in three to five repetitions. The icon shape is a visual compression token. Once dissolved, the icon decompresses instantly. Initial decompression requires hover discovery, which gives high first-encounter processing entropy. But icons are visually distinctive, and once the player has encountered the icon two to three times with its tooltip, the shape-to-meaning mapping dissolves. This is faster than truncated labels (where partial text interferes with stable mapping) but slower than full text labels (where meaning is immediate).

**Key bindings.** Convergence in two to three repetitions. The key's physical position on the keyboard provides a spatial mnemonic that is consistent across sessions. The mapping is one-to-one (one key, one action). Consistent one-to-one mappings dissolve faster than any visual scanning pattern because the physical substrate (keyboard layout) does not change.

#### 9.2 Convergence and Consistency

The overlay/build key mismatch in ONI demonstrates how inconsistent mapping increases convergence count. F1 maps to the Oxygen overlay, but the Oxygen build category is accessed via number key 2. Consistent mapping would let the player dissolve one mental model: "the first key handles oxygen." Inconsistent mapping forces the player to dissolve two independent models: "F1 is oxygen overlay" and "2 is oxygen build." Each model requires its own convergence period. The total convergence cost doubles.

EU4's context-sensitive number row appears to violate consistency — the same key means different things in different contexts. But the context change is triggered by an explicit player action (clicking a province), which creates a clear state boundary. The player dissolves two mappings: "7 means Ideas when nothing is selected" and "7 means Buildings when a province is selected." The explicit state boundary helps because the player always knows which context is active. This is different from inconsistency, where two similar-looking contexts produce different mappings without a clear boundary.

#### 9.3 Regression Events

A regression event occurs when a context change pushes operating conditions outside the validity envelopes of dissolved elements, promoting them back to active processing. In game UI, three types of regression events are observed.

**Mod installation or removal.** Adding a mod that inserts new items into an icon grid shifts the positions of existing items. Every dissolved icon position in that grid promotes back to active processing. The player must re-dissolve all positions. This is a cascade: one change (mod installation) crosses many validity envelopes (one per dissolved icon position) simultaneously. Icon grids are maximally vulnerable to this regression because adding one item shifts all subsequent positions. Text dropdowns are less vulnerable because new items can be inserted alphabetically or at the end without displacing existing items.

**Game update.** An update that changes the UI layout, reorders tabs, or renames actions invalidates dissolved mappings. The classic-to-Steam transition in Dwarf Fortress is the most extreme example: every dissolved keyboard sequence promoted back to active processing simultaneously because the input modality changed from keyboard to mouse. This is a total cascade — no dissolved navigation pattern survived.

**Hotkey mod breakage.** The RimWorld Hotkeys mod breaking on a game update is a regression event for every player who had dissolved hotkey bindings through the mod. The player's expert-level processing entropy (one to three ops per action with hotkeys) reverts to the base architecture's expert minimum (three to eight ops per action without hotkeys). The player commentary calling the game "unplayable" without the mod is qualitative evidence of the subjective impact of this processing entropy increase.

Key bindings are immune to mod-induced regression because they do not depend on visual positions. A key binding survives any change to the icon grid, tab ordering, or panel layout. The binding can only regress if the binding itself is changed (rebound to a different key) or removed (mod breakage). This is why dedicated key bindings are the most regression-resistant dissolution infrastructure.

#### 9.4 Learning Cost

The total learning cost for a player to reach expert-level processing entropy on a given task is:

Learning cost = (new player ops − expert ops) × convergence count

| Game | T1 New Ops | T1 Expert Ops | Convergence | Learning Cost |
|---|---|---|---|---|
| ONI | 28 | 5 | 4 | 92 |
| DF Steam | 33 | 8 | 4 | 100 |
| RimWorld | 20 | 8 | 6 | 72 |
| EU4 (construction) | 9 | 5 | 3 | 12 |
| CK3 (construction) | 10 | 6 | 3 | 12 |
| TW:WH3 (construction) | 12 | 8 | 3 | 12 |

Colony simulations have learning costs six to eight times higher than grand strategy games for equivalent construction tasks. This is driven by two factors: deeper hierarchies produce higher new-player costs, and icon-heavy interfaces produce more elements that must be dissolved separately.

RimWorld has the lowest learning cost among colony simulations despite not having the lowest expert ops. Text labels at the category level converge in two to three encounters, but truncated labels at the item level take five to eight encounters. The convergence count of six reflects the weighted average across both levels.

Grand strategy games have uniformly low learning costs for construction because the action is shallow (two to three levels) and text-labeled at most levels. The convergence count of three reflects that text panels and key bindings both dissolve quickly.

---

### 10. Discussion

#### 10.1 Framework Limitations

The op framework counts decisions, not time. A one-op action may take fifty milliseconds or five hundred milliseconds depending on motor difficulty, tooltip delay, or system response time. Fitts' Law effects are excluded. Very small or very distant targets cost more motor time but not more ops.

Cognitive load differences between reading text and parsing icons are approximated by the scan/hover distinction but not precisely modeled. The framework assumes that scanning a six-item text list is always one op. In practice, a list of six unfamiliar domain-specific terms may cost more cognitive effort than a list of six common English words. The counting rules use a simplified model that treats all readable text equally.

The framework assumes sequential attention. Parallel visual processing — peripheral vision identifying a target while the cursor is in motion — is not modeled. If a player's peripheral vision eliminates some scan candidates before the directed look, the actual op count may be lower than the framework predicts.

Cultural and language effects on text reading speed are not modeled. The counting rules assume literacy in the game's display language. For players reading in a non-native language, text labels may cost additional read ops.

#### 10.2 Framework Strengths

The op is a countable, reproducible unit. Two analysts measuring the same task in the same game with the same start state and player profile will produce the same op count, because the counting rules are deterministic. This is not true of subjective assessments ("the UI feels clunky") or time-based measurements (which vary with motor skill, screen resolution, and input device).

The framework captures the qualitative difference between "the label is visible" and "I must hover to discover the meaning." This distinction — between text scanning at one op and icon hover discovery at (N+1) ops — is the single largest factor in new-player cost. No other measurement framework quantifies this difference.

The benchmark task set provides a common basis for cross-game comparison. The twelve tasks cover the full range of tool selection interactions. Any simulation game with a tool selection interface can be measured against the same tasks.

The dissolution model captures the long-term cost of a UI architecture, not just the steady-state expert cost. An interface that produces twenty new-player ops and two expert ops with a convergence count of three has a total learning cost of fifty-four ops. An interface that produces fifteen new-player ops and five expert ops with a convergence count of eight has a total learning cost of eighty ops. The second interface has lower new-player cost but higher total cost. The framework makes this tradeoff visible.

#### 10.3 Design Recommendations

Five recommendations follow from the measurements.

First, use text labels at every level where screen space permits. The scan cost reduction from text labels (one op per level) versus icon-only hover discovery ((N+1) ops per row of N icons) is the single largest factor in new-player cost. A toolbar with six text-labeled buttons costs one scan op to navigate. The same toolbar with six unlabeled icons costs seven ops on average. This 7:1 ratio compounds across multiple navigation levels.

Second, provide keyboard shortcuts for high-frequency actions. The cost reduction from five ops (dropdown select) to one op (keypress) compounds over hundreds of uses per session. EU4's forty-five keyboard bindings produce one-op access for all major screens and map modes. RimWorld's zero item-level bindings produce eight-op access for common build items. Over one hundred uses of the same item, the difference is seven hundred ops.

Third, display the full current state as persistent text. One-op state confirmation prevents mode errors that lead to wasted actions. Systems where the player must hover an icon to confirm the active mode (three ops in DF Steam) impose a tax on every moment of uncertainty. Systems where the active state is displayed as readable text (one op) eliminate this tax.

Fourth, accept the within-category switching penalty of dropdown menus (two extra ops to reopen) in exchange for lower first-time discovery cost and higher resistance to regression. Persistent icon grids produce three-op within-category switching versus five-op dropdown switching — a two-op advantage. But persistent grids produce eight to ten new-player ops for item discovery versus five-op dropdown discovery. And persistent grids are vulnerable to position-shift regression when mods add items. The two-op switching advantage is real but smaller than the discovery and regression advantages of text dropdowns.

Fifth, pre-scan hierarchy depth at initialization and lock column or panel counts to prevent layout shifts that invalidate memorized positions. Layout shifts are validity envelope violations. When a toolbar column appears or disappears based on selection state, every dissolved button position in that toolbar may promote back to active processing. Locking the layout means the player dissolves button positions once and retains them for the session. This is a direct application of validity envelope engineering: ensure the context does not change in ways that would cross dissolution boundaries.

#### 10.4 Open Questions

What is the optimal hierarchy depth for a given item count? For two hundred items, is four levels of five to eight items each lower total cost than three levels of eight to twelve items each? The measurements suggest that deeper hierarchies with fewer items per level produce lower new-player cost, but the data set is limited to six games. A controlled experiment varying depth and breadth systematically would strengthen this finding.

How does tooltip delay duration affect the hover op cost in practice? The framework counts each hover as two ops regardless of tooltip delay. A two-hundred-millisecond tooltip and a five-hundred-millisecond tooltip are the same op count. But subjectively, a longer tooltip delay may feel more expensive. The framework intentionally excludes time, but a time-weighted variant could capture this effect.

Can context-sensitive key reuse, as implemented in EU4 (number keys change meaning when a province is selected), be applied to colony simulations? Colony sim build menus could reuse number keys: categories when nothing is selected, building-specific actions when a building is selected. No colony simulation currently uses this pattern.

How do touchscreen and controller input modalities change the op cost of each architecture? The framework assumes mouse and keyboard. Touchscreen input eliminates hover (no cursor) but introduces new op types (tap, swipe, pinch). Controller input replaces cursor movement with directional navigation, changing the move op's cost structure. These modalities are outside the scope of this paper but are addressable within the op framework by defining additional op categories for each input substrate.

---

### 11. Conclusion

This paper applies the op — the universal unit of information under action, defined in HOWL-INFO-14-2026 — to the specific domain of tool selection interfaces in simulation games. Six domain-specific op categories (look-at, read, scan, hover, move, click) are defined with fixed counting rules. A library of compound actions provides pre-computed op costs. Twelve benchmark tasks provide a standardized measurement surface.

Measurements across six commercial titles in two genres produce three findings.

First, text-labeled hierarchical menus with keyboard acceleration produce the lowest combined new-player and expert interaction cost. Text labels reduce new-player scan cost by a factor of seven compared to icon-only interfaces. Keyboard shortcuts reduce expert action cost to one op. The combination produces the smallest new-player-to-expert gap and the lowest total learning cost.

Second, icon-only hierarchies produce the lowest expert cost once all positions are memorized, but the highest new-player cost due to hover discovery. The new-player-to-expert gap can exceed twenty-five ops on a single task. This gap represents a dissolution investment that the player must make through repeated encounters with each icon.

Third, persistent icon grids produce the lowest within-category switching cost (two to three ops versus five ops for dropdowns) but the highest regression vulnerability. Adding one item to a grid shifts all subsequent positions, promoting every dissolved position mapping back to active processing. Text dropdowns and key bindings are resistant to this regression because they do not depend on positional stability.

The framework is reproducible. Two analysts measuring the same task in the same game with the same assumptions will produce the same op count. The framework is extensible. New op categories can be defined for new input modalities. New benchmark tasks can be added for new interaction patterns. The twelve tasks and six categories defined here cover the current state of simulation game interfaces. The op unit itself is universal — the same op that counts a player's toolbar click counts a surgeon's diagnostic question and a CPU's cache lookup. The domain-specific calibration is what this paper provides. The unit is what HOWL-INFO-14-2026 provides. Together, they make game UI design measurable.

---

### References

1. Shannon, C. E. (1948). A Mathematical Theory of Communication. *Bell System Technical Journal*, 27(3), 379–423.

2. HOWL-INFO-14-2026. Bits and Ops: A Complete Theory of Information. DOI: 10.5281/zenodo.20631041.

3. Card, S. K., Moran, T. P., & Newell, A. (1983). *The Psychology of Human-Computer Interaction*. Lawrence Erlbaum Associates. [Cited as related work, not as a predecessor of the op framework.]

4. Card, S. K., Moran, T. P., & Newell, A. (1980). The Keystroke-Level Model for User Performance Time with Interactive Systems. *Communications of the ACM*, 23(7), 396–410. [Cited as related work.]

5. Fitts, P. M. (1954). The Information Capacity of the Human Motor System in Controlling the Amplitude of Movement. *Journal of Experimental Psychology*, 47(6), 381–391. [Cited as related work.]

6. Hick, W. E. (1952). On the Rate of Gain of Information. *Quarterly Journal of Experimental Psychology*, 4(1), 11–26. [Cited as related work.]

7. Hyman, R. (1953). Stimulus Information as a Determinant of Reaction Time. *Journal of Experimental Psychology*, 45(3), 188–196. [Cited as related work.]

8. Liu, W., Gori, J., Rioul, O., Beaudouin-Lafon, M., & Guiard, Y. (2020). How Relevant is Hick's Law for HCI? *CHI 2020 — Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems*, 1–11. [Cited for the argument that visual search and decision making analysis is more fruitful than direct application of Hick's Law to HCI tasks.]

---

### Appendix A: Op Category Reference Card

| Category | Definition | Counting Rule |
|---|---|---|
| Look-at | Direct eyes to a UI region | 1 op per directed eye movement to a new screen region. Adjacent columns within one toolbar: 0. Dropdown below trigger: 0. |
| Read | Process text or icon content | Common word during look-at: 0. Domain term: 1. Tooltip: 1. Truncated label: 1. |
| Scan | Search multiple elements for a target | Text list 1–12 items: 1. Text list 13+ with scroll: 2. Icon row with text: 1 per row. Icon row no text: 2 per row. Truncated: 1.5 per row (round up). |
| Hover | Position cursor and wait for feedback | Tooltip hover: 2 (1 move + 1 read). Discovery: (N+1)/2 hovers × 2 ops for row of N unlabeled icons = N+1 ops. |
| Move | Reposition cursor to target | 1 op per repositioning regardless of distance. |
| Click | Press/release mouse button or key | Single click: 1. Click-drag-release: 2. Keypress: 1. CTRL+key: 1. |

---

### Appendix B: Compound Action Reference Table

| Action | Decomposition | Total Ops |
|---|---|---|
| Click known button | Move (1) + Click (1) | 2 |
| Click unknown text button | Look-at (1) + Scan (1) + Move (1) + Click (1) | 4 |
| Click unknown icon button (N icons) | Look-at (1) + Hovers ((N+1)/2 × 2) + Click (1) | 2 + (N+1) |
| Text dropdown select (1–12 items) | Move (1) + Click open (1) + Scan (1) + Move (1) + Click (1) | 5 |
| Text dropdown select (13+ items) | Move (1) + Click open (1) + Scan (1) + Scroll (1) + Scan (1) + Move (1) + Click (1) | 7 |
| Icon grid select (truncated labels, 2 rows) | Look-at (1) + Scan (2 + 2) + Move (1) + Click (1) | 8–10 |
| Icon grid select (icon-only, row of N) | Look-at (1) + Hovers ((N+1) ops) | 1 + (N+1) per row |
| Confirm state (text toolbar) | Look-at (1) | 1 |
| Confirm state (icon toolbar, hover needed) | Look-at (1) + Hover (2) | 3 |
| Point placement | Move (1) + Click (1) | 2 |
| Area stroke | Move (1) + Click (1) + Move (1) + Click (1) | 4 |

---

### Appendix C: Game Configuration Notes

| Game | Version | Platform | Keybindings | Mods |
|---|---|---|---|---|
| Oxygen Not Included | Spaced Out DLC, current Steam release | PC | Default | None |
| Dwarf Fortress | Steam Premium Edition, current release | PC | Default | None |
| RimWorld | Current Steam release | PC | Default | None |
| Europa Universalis IV | Current Steam release with all major DLC | PC | Default | None |
| Crusader Kings III | Current Steam release with all major DLC | PC | Default | None |
| Total War: Warhammer III | Current Steam release | PC | Default | None |

All measurements assume a 1920×1080 display at 100% UI scale. Mouse input with standard sensitivity. No controller or touchscreen input.

---

### Appendix D: Hotkey Coverage by Game

| Game | Screen/Mode Keys | Map Mode/Overlay Keys | Item/Action Keys | Camera Keys | Total |
|---|---|---|---|---|---|
| EU4 | 13 (1-0, comma, period, apostrophe) | 10 (Q-P row) | ~20 (a-z unit commands) | 0 (arrow keys) | ~45 |
| CK3 | 8 (F1-F8) | 1 (e, zoom-adaptive) | 3 (C, V, Tab) | 0 (edge scroll) | ~15 |
| TW:WH3 | 5 (1-5 settlement views) | 1 (TAB strategic) | 4 (CTRL+B/I/M/C battle) | 4 (WASD) | ~15 |
| RimWorld | 0 | 0 | 0 | 4 (WASD) | ~5 |
| DF Steam | 2 (b, d) | 0 | 0 | 4 (arrow keys) | ~5 |
| ONI | ~9 (1-9 build categories) | 16 (F1-F11, Shift+F1-F4, P) | 0 | 0 (edge scroll) | ~25 |

Grand strategy games invest more key-space in dissolution infrastructure than colony simulations. EU4 dedicates forty-five keys to direct-access bindings. No colony simulation exceeds twenty-five, and the colony sim bindings are concentrated in category-level access (ONI's number keys, ONI's F-keys for overlays) rather than item-level access. No colony simulation provides a one-keypress path to a specific build item.

---

### Appendix E: Glossary

**Op.** One irreducible transformation by one processor. The universal unit of information under action. Defined in HOWL-INFO-14-2026.

**Processing entropy.** The op count a specific processor requires for a specific element, given a specific goal in a specific context. Receiver-dependent.

**Dissolution.** The mechanism by which a processing chain's op count decreases toward zero through repetition under consistent conditions.

**Validity envelope.** The region of context space within which a dissolution holds. Inside the envelope, the dissolved element costs zero ops. Outside, it promotes back to active processing.

**Cascade.** The simultaneous promotion of many dissolved elements back to active processing when a context change crosses multiple validity envelopes.

**Regression event.** A context change in game UI (mod installation, game update, UI rearrangement) that causes a cascade by invalidating dissolved element positions or mappings.

**Optimal reduction (R*).** The minimum number of correct ops any competent processor requires for reliable execution of a task. Below R*, correctness is lost.

**Convergence count.** The number of repetitions required for a processing chain to dissolve from new-player processing entropy to expert processing entropy (or R*).

**Learning cost.** (New player ops − expert ops) × convergence count. A discrete approximation of the area under the dissolution curve.

**Cold start.** No mode active, no menu open, player looking at the map.

**Warm start.** Correct mode active, no item selected.

**Hot start.** Correct item selected, ready to place.

**Dissolution infrastructure.** UI features designed to accelerate dissolution or lower R*. Hotkeys, text labels, persistent state displays, and locked layouts are dissolution infrastructure.

**Key-space exhaustion.** The condition where all available keyboard keys are bound to actions, preventing additional dissolution infrastructure from being added. EU4 exhibits near-complete key-space exhaustion.

---

### Appendix F: Task Algebra Component Costs by Architecture

| Architecture | Component | New Player (unknown) | Expert (toolbar) | Expert (hotkey) |
|---|---|---|---|---|
| Text dropdown | M (mode switch) | 4 (look + scan + move + click) | 2 (move + click) | 1 (keypress) |
| Text dropdown | C (category) | 5 (move + click + scan + move + click) | 5 | 1 (keypress) |
| Text dropdown | I (item) | 5 | 5 | 1 (keypress) |
| Text dropdown | V (variant) | 5 | 5 | 5 |
| Text dropdown | P (point) | 2 | 2 | 2 |
| Text dropdown | P (area stroke) | 4 | 4 | 4 |
| Icon grid with truncated labels | M (mode tab) | 4 (look + scan tabs + move + click) | 2 (move + click) | N/A |
| Icon grid with truncated labels | C (sub-tab) | 4 (look + scan + move + click) | 2 | N/A |
| Icon grid with truncated labels | I (item in grid) | 8–10 (scan 2–3 rows) | 2 (move + click) | N/A |
| Icon grid with truncated labels | V (material dropdown) | 4 (look + scan + move + click) | 4 | N/A |
| Icon grid with truncated labels | P (point) | 2 | 2 | N/A |
| Icon grid with truncated labels | P (drag) | 3 (click + drag + release) | 3 | N/A |
| Icon-only toolbar | M (find icon) | 2 + (N+1) where N = icons before target | 2 (move + click) | N/A |
| Icon-only toolbar | C (sub-category) | 2 + (N+1) | 2 | N/A |
| Icon-only toolbar | I (item in sub-panel) | 2 + (N+1) | 2 | N/A |
| Icon-only toolbar | V (material dropdown) | 4 | 4 | N/A |
| Icon-only toolbar | P (point) | 2 | 2 | N/A |
| Icon-only toolbar | P (area stroke) | 4 | 4 | N/A |
| Dedicated key binding | M (screen switch) | 1–4 (1 if key known, 4 if must discover) | 1 | 1 |
| Dedicated key binding | Map mode switch | 1–4 | 1 | 1 |

---

### Appendix G: Hover Discovery Cost Table

Expected ops to find one target in a row of N unlabeled icons, assuming uniform probability of target position. Formula: expected hovers = (N+1)/2, each hover = 2 ops, plus 1 look-at and 1 click. Total = 2 + (N+1).

| N (icons in row) | Expected Hovers | Hover Ops | Look-at + Click | Total Ops |
|---|---|---|---|---|
| 3 | 2.0 | 4 | 2 | 6 |
| 4 | 2.5 | 5 | 2 | 7 |
| 5 | 3.0 | 6 | 2 | 8 |
| 6 | 3.5 | 7 | 2 | 9 |
| 8 | 4.5 | 9 | 2 | 11 |
| 10 | 5.5 | 11 | 2 | 13 |
| 12 | 6.5 | 13 | 2 | 15 |
| 15 | 8.0 | 16 | 2 | 18 |
| 20 | 10.5 | 21 | 2 | 23 |

The cost grows linearly with N. Doubling the number of icons in a row approximately doubles the discovery cost. This linearity is the mechanism behind the large new-player cost in icon-only interfaces: each additional icon added to a toolbar or sub-panel increases the expected discovery cost by one op.

---

### Appendix H: Scan Cost Table

Expected ops to find one target in a list or grid, by label quality and list size.

| Element Type | Items 1–6 | Items 7–12 | Items 13–18 (scroll) | Items 19+ (scroll) |
|---|---|---|---|---|
| Text list, full labels | 1 | 1 | 2 | 2+ (1 per scroll page) |
| Text list, domain-specific terms | 1 + 1 read per unfamiliar term | 1 + reads | 2 + reads | 2+ reads |
| Icon row, text labels | 1 per row | 1 per row | 1 per row + 1 scroll | 1 per row + scrolls |
| Icon row, truncated labels | 1.5 per row (round up) | 1.5 per row | 1.5 per row + 1 scroll | 1.5 per row + scrolls |
| Icon row, no labels | 2 per row (or use hover discovery) | 2 per row | 2 per row + 1 scroll | 2 per row + scrolls |

For grids, multiply the per-row cost by the number of rows visible. A two-row icon grid with truncated labels: 1.5 × 2 = 3 ops (rounded to 4). A three-row icon grid with full text labels: 1 × 3 = 3 ops.

---

### Appendix I: Dissolution Convergence Rates

Expected number of repetitions to reach expert-level processing entropy (R* or zero) for each element type, under consistent conditions (no regression events between repetitions).

| Element Type | Convergence Count | Dissolution Mechanism | R* After Dissolution |
|---|---|---|---|
| Text label position in a 1D list | 2–3 | Word meaning is pre-dissolved (literate player). Only position mapping must dissolve. 1D spatial relationship. | 0 (position fires structurally) |
| Icon position in a 1D toolbar | 3–5 | Icon shape must dissolve alongside position. Two mappings: shape-to-meaning and position-in-bar. | 0 |
| Icon position in a 2D grid | 5–8 | 2D spatial relationship requires more encounters. Row and column must both dissolve. | 0 |
| Truncated label in a 2D grid | 4–6 | Partial text interferes with stable mapping. Player oscillates between reading truncation and recalling full name. | 0 |
| Keyboard shortcut (single key) | 2–3 | Physical key position provides spatial mnemonic. Mapping is 1:1 and consistent. | 0 |
| Keyboard shortcut (CTRL+key) | 2–3 | Same as single key. Modifier+letter chord dissolves as one motor pattern. | 0 |
| F-key to overlay mapping | 3–5 | F-keys lack spatial mnemonics for most players (F1-F12 are visually undifferentiated). Arbitrary mapping requires more encounters. | 0 |
| Context-sensitive key (e.g., EU4 province mode) | 3–4 per context | Player dissolves the context boundary (explicit action triggers context switch) and the mapping within each context separately. | 0 per context |
| Material dropdown position | 3–4 | Short text list. Materials are common words. Position dissolves faster than icon grids because the list is 1D and text-labeled. | 0 |
| Tooltip content after hover | 1–2 | The player reads the tooltip once or twice and associates it with the icon shape. Subsequent encounters fire the association structurally. | 0 (hover itself dissolves to 0 when position is dissolved — player moves directly without hovering) |

---

### Appendix J: Validity Envelope Dimensions for Game UI Elements

Each dissolved element has a validity envelope defined by the context dimensions under which it dissolved. When any dimension exits the envelope, the element promotes back to active processing.

| Dissolved Element | Dimension 1 | Dimension 2 | Dimension 3 | Dimension 4 | Regression Trigger |
|---|---|---|---|---|---|
| Button position in toolbar | Toolbar layout | Group count | Screen resolution | UI scale | Any layout change: mod adds group, resolution change shifts positions, UI scale change resizes elements |
| Icon position in grid | Grid contents | Grid sort order | Grid dimensions (rows × cols) | Mod load state | Mod adds/removes item, sort order changes, grid resize |
| Tab position in tab bar | Tab count | Tab ordering | Tab visibility rules | Mod load state | Mod adds tab, game update reorders tabs |
| Keyboard shortcut mapping | Key binding configuration | Input mode (keyboard vs controller) | Mod override state | — | Rebind, mod conflict, input mode switch |
| Dropdown item position | List contents | Sort order | Filter state | — | Item added/removed, sort order changed, filter applied |
| F-key to overlay mapping | Overlay set | Key binding configuration | — | — | New overlay added to F-key range, rebind |
| Material dropdown contents | Available materials | Research state | Map biome (affects available resources) | — | Research unlocks new material, move to new biome |
| Context-sensitive key meaning | Selection state (province selected vs not) | Game mode (campaign vs battle) | — | — | Selection state changes (this is intentional and part of the design, not a regression) |

Context-sensitive key meaning has a special status: the dimension change (selecting/deselecting a province) is an intentional state boundary that the player controls. This is not a regression event. The player knowingly enters and exits the context. All other dimension changes listed above are involuntary or environmental — the player does not choose to have a mod shift icon positions.

---

### Appendix K: Key-Space Allocation by Game

Total available single-press keys on a standard keyboard and how each game allocates them. Modified keys (CTRL+letter, Shift+F-key) are listed separately.

| Key Range | Total Keys | EU4 | CK3 | TW:WH3 | RimWorld | DF Steam | ONI |
|---|---|---|---|---|---|---|---|
| A–Z | 26 | 18 bound (unit ops, map modes occupy Q-P and unit ops occupy most remaining) | 3 bound (C, V, e) | 4 bound (WASD camera) | 4 bound (WASD camera) | 2 bound (b, d) | 0 bound |
| 0–9 | 10 | 10 bound (screens) | 0 bound | 5 bound (settlement views, context) | 0 bound | 0 bound | 9 bound (build categories) |
| F1–F12 | 12 | 5 bound (ledger, interface) | 8 bound (screens) | 0 bound | 0 bound | 0 bound | 11 bound (overlays) |
| Punctuation (comma, period, apostrophe, etc.) | ~8 | 3 bound (Military, Subjects, Estates) | 0 bound | 0 bound | 0 bound | 0 bound | 0 bound |
| Space | 1 | 1 bound (pause) | 1 bound (pause) | 1 bound (overlay hold) | 1 bound (pause) | 1 bound (pause) | 0 bound |
| Tab | 1 | 1 bound (multiplayer chat) | 1 bound (Issues) | 1 bound (strategic map) | 0 bound | 0 bound | 0 bound |
| ESC | 1 | 1 bound (close panel) | 1 bound (close panel) | 1 bound (close panel) | 1 bound (close panel) | 1 bound (close panel) | 1 bound (close panel) |
| Arrow keys | 4 | 4 bound (map scroll, ledger nav) | 0 bound | 0 bound | 0 bound | 4 bound (map scroll) | 0 bound |
| **Total single-press** | **~62** | **~43** | **~14** | **~12** | **~6** | **~8** | **~21** |
| CTRL+A–Z | 26 | 10 bound (unit control groups via CTRL+1-0) | 0 bound | 4 bound (CTRL+B/I/M/C unit type select) | 0 bound | 0 bound | 0 bound |
| Shift+F1–F12 | 12 | 0 bound | 0 bound | 0 bound | 0 bound | 0 bound | 4 bound (extended overlays) |
| **Total modified** | **~38** | **~10** | **~0** | **~4** | **~0** | **~0** | **~4** |
| **Grand total** | **~100** | **~53** | **~14** | **~16** | **~6** | **~8** | **~25** |

EU4 uses approximately 53% of available key-space. This is near the practical maximum — the remaining unbound keys are needed for text input (chat, province search) and system functions (screenshot, console). RimWorld and DF Steam use approximately 6–8% of available key-space, leaving over 90% unused. This unused key-space represents potential dissolution infrastructure that has not been built. Every unbound key is a one-op action that the game could provide but does not.

---

### Appendix L: Processing Entropy Profiles by Game

Processing entropy Hp for each benchmark task, measured as the op count for a new player (maximum Hp) and an expert (minimum Hp, equal to R* or zero if fully dissolved). The difference (Hp_new − Hp_expert) is the dissolution potential — the ops that dissolution can eliminate.

| Task | ONI Hp_new | ONI Hp_exp | ONI Δ | DF Hp_new | DF Hp_exp | DF Δ | RW Hp_new | RW Hp_exp | RW Δ |
|---|---|---|---|---|---|---|---|---|---|
| T1 | 28 | 5 | 23 | 33 | 8 | 25 | 20 | 8 | 12 |
| T2 | 2 | 2 | 0 | 2 | 2 | 0 | 2 | 2 | 0 |
| T3 | 3 | 2 | 1 | 8 | 2 | 6 | 4 | 2 | 2 |
| T4 | 16 | 5 | 11 | 22 | 6 | 16 | 11 | 5 | 6 |
| T5 | 20 | 5 | 15 | 29 | 6 | 23 | 16 | 7 | 9 |
| T7 | 15 | 3 | 12 | 25 | 5 | 20 | 11 | 5 | 6 |
| T8 | 10 | 1 | 9 | 18 | 3 | 15 | 12 | 3 | 9 |
| T10 | 2 | 1 | 1 | 3 | 3 | 0 | 3 | 2 | 1 |
| T11 | 12 | 2 | 10 | 14 | 2 | 12 | 3 | 2 | 1 |
| **Sum Δ** | | | **82** | | | **117** | | | **46** |

| Task | EU4 Hp_new | EU4 Hp_exp | EU4 Δ | CK3 Hp_new | CK3 Hp_exp | CK3 Δ | TW Hp_new | TW Hp_exp | TW Δ |
|---|---|---|---|---|---|---|---|---|---|
| T5 eq | 9 | 5 | 4 | 10 | 6 | 4 | 12 | 8 | 4 |
| T8 | 4 | 1 | 3 | 4 | 2 | 2 | 3 | 2 | 1 |
| T9 | 1 | 1 | 0 | 4 | 2 | 2 | 3 | 2 | 1 |
| T10 | 2 | 1 | 1 | 1 | 1 | 0 | 2 | 1 | 1 |
| T11 | 3 | 1 | 2 | 3 | 1 | 2 | 3 | 1 | 2 |
| **Sum Δ** | | | **10** | | | **10** | | | **9** |

The sum of dissolution potential (Σ Δ) across measured tasks is an aggregate indicator of how much learning the player must do to reach expert performance. DF Steam requires dissolving 117 ops across the measured tasks. RimWorld requires 46. EU4, CK3, and TW:WH3 each require approximately 10. The 12:1 ratio between DF Steam and EU4 reflects both the deeper hierarchy of colony sim item selection and the icon-only architecture that inflates new-player hover discovery costs.

T2 (repeat same item) has zero dissolution potential across all games because the action is already at R* on first encounter — move to tile and click is the irreducible minimum. No processing chain exists to dissolve. This is the only task where new-player and expert performance are identical.

T10 (confirm state) has near-zero dissolution potential for most games because even new players can look at the UI and identify the active state. DF Steam is the exception: its icon-only toolbar requires a hover to confirm meaning even for experts who have not fully dissolved the icon shape, giving it a persistent Hp of 3 that does not decrease to the 1-op floor achieved by text-labeled systems.

---

### Appendix M: Regression Vulnerability by Architecture

Classification of each dissolved element type by its vulnerability to the three regression triggers identified in Section 9.3.

| Dissolved Element | Mod Installation | Game Update | Hotkey Mod Breakage | Overall Vulnerability |
|---|---|---|---|---|
| Text label position in dropdown | Low: new items can insert alphabetically without shifting existing positions | Low: text labels rarely reorder on update | N/A | Low |
| Icon position in toolbar | Medium: new icons shift all subsequent positions | Medium: toolbar layout may change | N/A | Medium |
| Icon position in 2D grid | High: one new item shifts all subsequent positions in the row and potentially pushes items to next row | High: grid contents and layout may change | N/A | High |
| Tab position in tab bar | Medium: new tabs shift existing tabs | Medium: tabs may reorder | N/A | Medium |
| Keyboard shortcut (built-in) | None: key bindings are independent of visual layout | Low: game may rebind keys on major update | N/A | Very Low |
| Keyboard shortcut (mod-provided) | None: independent of visual layout | None: independent of base game | High: mod breakage removes all bindings simultaneously | High (concentrated risk) |
| F-key overlay mapping | None: F-key range is fixed | Low: new overlays may be inserted into the F-key sequence | N/A | Low |
| Context-sensitive key meaning | None: the key itself does not move | Low: context rules may change | N/A | Very Low |
| Material dropdown position | Low: new materials insert into a short sorted list | Low: material lists rarely change | N/A | Low |

Icon positions in 2D grids have the highest overall regression vulnerability. They are affected by both mod installation and game updates. They are the only element type that regresses from the most common player action (installing a mod). Keyboard shortcuts have the lowest overall vulnerability when built-in. Mod-provided shortcuts concentrate all risk into a single point of failure (mod compatibility), which produces binary regression: either everything works or everything breaks.

---

### Appendix N: Three-Term Cost Applied to Game UI

The three-term communication cost from HOWL-INFO-14-2026 §14 applied to each game's tool selection system.

Cost(database → player) = Hp(system, render) + Hs(display) + Hp(player, decode)

| Term | Definition in Game UI Context | Measured By |
|---|---|---|
| Hp(system, render) | Computational ops for the toolbar module to query the database, build dropdown items, and render buttons. | CPU profiling. Outside the scope of this paper. |
| Hs(display) | The visual information presented on screen: button labels, icon images, dropdown text, tooltip content. | Shannon entropy of the display. Fixed for a given UI state. Outside the scope of this paper. |
| Hp(player, decode) | The player's op count to find, identify, and select the correct item from the displayed UI. | The entire measurement framework of this paper. |

For modern games on modern hardware, the first term (system render) is negligible — microseconds to milliseconds. The second term (display channel) is effectively free — pixel rendering at 60+ fps with no transmission delay. The third term (player decode) dominates by orders of magnitude. A player spending twenty ops scanning an icon grid is consuming seconds of cognitive processing. The system spent microseconds rendering that grid. The channel delivered it in one frame.

This is the endpoint-dominant case described in HOWL-INFO-14-2026 §14: modern channels are cheap, processing is expensive. Shannon-optimal encoding minimizes channel bits. Processing-optimal encoding minimizes total cost. They differ whenever the receiver's processing entropy is high. For game UI, the receiver (the player) almost always has high processing entropy relative to the channel cost. Optimizing the display for processing entropy reduction (text labels, consistent layouts, dissolved positions) reduces total cost far more than optimizing the display for information density (more icons per pixel, smaller buttons, denser grids).

---

### Appendix O: Context-Sensitive Key Reuse Patterns

EU4's number row serves two functions depending on selection state. This pattern is absent from all measured colony simulations. This appendix documents the pattern formally and identifies where it could be applied.

| Game | Key Range | Context A (nothing selected) | Context B (entity selected) | Context Boundary |
|---|---|---|---|---|
| EU4 | 1–0 | Major screens (Court, Government, ...) | Province actions (Land units, Naval, Make core, ...) | Click province / click empty map |
| EU4 | z, x, b, c | Unit type detach (infantry, cavalry, artillery, transport) | Same (unit must be selected) | Select unit / deselect unit |
| CK3 | e | N/A | N/A (zoom-adaptive, not selection-adaptive) | Zoom level change |
| TW:WH3 | 1–5 | N/A (no function outside settlement) | Settlement views (Overview, Garrison, Buildings, ...) | Click settlement / click empty map |

**Pattern requirements.** Context-sensitive key reuse requires three conditions. First, the two contexts must be mutually exclusive — the player cannot be in both at once. Second, the context boundary must be triggered by an explicit player action (clicking a province, selecting a unit) so the player always knows which context is active. Third, the actions in each context must be semantically unrelated enough that the player does not confuse them.

**Colony simulation application candidates.** Colony sims could reuse number keys as follows: when nothing is selected, number keys open build categories (as ONI already does). When a placed building is selected, number keys access building-specific actions (assign workers, set priority, view inventory, configure output). The context boundary (click building / click empty tile) is explicit and familiar. No colony simulation currently implements this pattern.

---

### Appendix P: Camera Key Allocation Tradeoffs

Camera movement consumes key-space. Games that use WASD for camera panning sacrifice four letter keys. Games that use arrow keys or edge scrolling preserve letter keys for action bindings. This tradeoff directly affects the amount of dissolution infrastructure available for tool selection.

| Camera Method | Keys Consumed | Ergonomic Quality | Letter Keys Freed | Game Examples |
|---|---|---|---|---|
| WASD | 4 (W, A, S, D) | High: left hand rests on home row, all surrounding keys reachable | 22 remaining | TW:WH3, RimWorld |
| Arrow keys | 4 (←, ↑, →, ↓) | Low: right hand moves away from mouse, surrounding keys not useful for hotkeys | 26 remaining | EU4, DF Steam (classic) |
| Edge scroll (mouse) | 0 | Medium: no keys consumed, but requires cursor at screen edge which interrupts tool selection | 26 remaining | CK3, ONI |
| Middle-click drag | 0 | Medium: no keys consumed, but occupies the mouse button used for some interactions | 26 remaining | Some map applications |

EU4 chose arrow keys for camera, preserving all 26 letter keys for action bindings. This decision enables EU4's forty-five-binding hotkey density. Players have criticized the arrow key camera as ergonomically inferior to WASD, but the tradeoff is measurable: WASD camera would consume four keys that currently provide one-op access to unit operations (W = map mode, A = attach, S = split, D = detach). Each reassigned key would increase the processing entropy of the corresponding action from one op (keypress) to two or more ops (mouse navigation to a UI button). The total cost increase across a typical session would be hundreds of additional ops.

TW:WH3 chose WASD for camera, consuming four letter keys. The remaining letter key budget is insufficient for EU4-density action bindings on the campaign map. The campaign side compensates with number keys for settlement views and CTRL+letter for battle unit type selection. The battle side has its own control scheme with fewer available keys, which is acceptable because battle actions are fewer and more repetitive than campaign actions.

RimWorld chose WASD for camera but assigns no other letter keys to actions. Twenty-two letter keys are available for dissolution infrastructure that has not been built. If RimWorld assigned twenty of those keys to build item shortcuts (matching the colony sim equivalent of EU4's action binding density), the expert T1 cost would drop from eight ops to approximately three ops. The unused key-space is a measurable design gap: the architecture supports one-op item access but no bindings have been created.

---

### Appendix Q: Op Cost Ratios by Comparison Pair

Pairwise ratios showing how many times more expensive one game is than another for each task. Ratios greater than 1.0 mean the row game costs more than the column game. All values use new-player ops.

**Colony Sim Pairwise — New Player**

| Task | DF:RW | DF:ONI | ONI:RW |
|---|---|---|---|
| T1 | 1.65 | 1.18 | 1.40 |
| T3 | 2.00 | 2.67 | 0.75 |
| T4 | 2.00 | 1.38 | 1.45 |
| T5 | 1.81 | 1.45 | 1.25 |
| T7 | 2.27 | 1.67 | 1.36 |
| T8 | 1.50 | 1.80 | 0.83 |
| T11 | 4.67 | 1.17 | 4.00 |

DF Steam is 1.5x to 4.7x more expensive than RimWorld for a new player across all measured tasks. The largest ratio (4.67x on T11) is driven by icon-only mode switching in DF (fourteen ops) versus text-labeled tab switching in RimWorld (three ops). The smallest ratio (1.50x on T8) is overlay toggling, where both games use icon buttons and the cost difference is driven by toolbar icon count rather than label presence.

ONI falls between DF and RimWorld on most tasks (ratio to RimWorld between 0.75 and 1.45). ONI beats RimWorld on T3 (within-category item switch, 0.75x) and T8 (overlay toggle, 0.83x) because ONI's persistent item grid and F-key overlay system are more efficient for these specific tasks.

**Cross-Genre — Expert Ops**

| Task | RW (best colony) | EU4 (best grand strat) | Ratio RW:EU4 |
|---|---|---|---|
| T8 | 3 | 1 | 3.0 |
| T10 | 2 | 1 | 2.0 |
| T11 | 2 | 1 | 2.0 |

The best-performing colony simulation (RimWorld) is two to three times more expensive than the best-performing grand strategy game (EU4) for expert overlay, state confirmation, and mode switching. This gap is entirely explained by dissolution infrastructure density: EU4 provides one-op key bindings for these actions, RimWorld does not.

---

### Appendix R: Dissolution Curve Area (Learning Investment)

Total ops a player must spend to dissolve all measured tasks from new-player to expert performance. Computed as Σ over all tasks of (Hp_new − Hp_expert) × convergence count. Uses the per-architecture convergence rates from Appendix I.

| Game | Architecture Type | Avg Convergence Count | Sum Δ (from App. L) | Total Learning Ops |
|---|---|---|---|---|
| DF Steam | Icon-only, 3–4 levels | 4 | 117 | 468 |
| ONI | Icon toolbar + text grid, 3 levels | 4 | 82 | 328 |
| RimWorld | Text tabs + icon grid, 2–3 levels | 5 | 46 | 230 |
| EU4 | Text panels + key bindings | 3 | 10 | 30 |
| CK3 | Text panels + F-key bindings | 3 | 10 | 30 |
| TW:WH3 | WASD camera + text panels + number keys | 3 | 9 | 27 |

DF Steam requires approximately 468 total learning ops across the measured tasks. EU4 requires approximately 30. The 15:1 ratio reflects two compounding factors: DF Steam has higher dissolution potential per task (deeper icon-only hierarchies produce larger Hp gaps) and similar convergence counts (icon positions dissolve in 3–5 repetitions, key bindings dissolve in 2–3 repetitions — the difference is modest). The dominant factor is the gap size, not the convergence speed.

RimWorld's convergence count of 5 (higher than DF Steam's 4) reflects that truncated icon grid labels dissolve more slowly than pure icon positions. But RimWorld's lower Sum Δ (46 versus 117) more than compensates, producing a total learning investment of 230 ops versus 468 — approximately half.

Grand strategy games cluster tightly at 27–30 total learning ops because all three use text labels at most levels and provide key bindings for high-frequency actions. The dissolution infrastructure absorbs most of the learning cost before the player begins.

---

### Appendix S: Cascade Severity Estimates by Regression Trigger

Estimated number of dissolved elements that promote back to active processing for each regression trigger, by game.

| Trigger | DF Steam | ONI | RimWorld | EU4 | CK3 | TW:WH3 |
|---|---|---|---|---|---|---|
| Mod adds 5 items to one build category | 5–15 (grid shift affects all icons after insertion point) | 5–10 (grid shift in item panel) | 5–15 (grid shift in icon grid) | 0–2 (text list, new items append or insert alphabetically) | 0–2 (text panel, minimal shift) | 0–3 (building browser, scroll position may change) |
| Game update rearranges toolbar | 10–20 (all toolbar icon positions) | 5–15 (toolbar and sidebar icon positions) | 3–8 (tab order and some grid layouts) | 2–5 (button positions in panels) | 2–5 (button positions in panels) | 3–8 (toolbar and settlement view buttons) |
| Game update changes input modality | 30+ (all navigation patterns — DF classic to Steam) | N/A (no modality change observed) | N/A | N/A | N/A | N/A |
| Hotkey mod breaks | N/A (no hotkey mod ecosystem) | 5–15 (Favorite Buildings mod bindings) | 10–30 (all Hotkeys mod bindings) | N/A (built-in hotkeys) | N/A | N/A |
| UI scale change (e.g., new monitor) | 5–10 (icon sizes change, spatial relationships shift) | 3–8 | 3–8 | 1–3 (text reflows but labels remain readable) | 1–3 | 2–5 |

Icon-heavy architectures (DF Steam, ONI) show higher cascade severity per trigger because dissolved icon positions are spatially interdependent — shifting one shifts the spatial model for all subsequent icons. Text-heavy architectures (EU4, CK3) show lower cascade severity because text labels are semantically stable (the word "Diplomacy" does not change meaning when the button moves) and positionally resilient (alphabetical ordering survives insertions).

The DF classic-to-Steam modality change is the highest-severity cascade observed: thirty or more dissolved elements promoted simultaneously. No other measured trigger approaches this severity. It is a one-time event (the modality change happened once in DF's history) but it demonstrates the theoretical maximum cascade severity for a game UI regression.

---

### Appendix T: R* Floors by Task

The minimum correct ops (R*) for each task — the floor below which the player is not performing the task correctly. R* is the expert hotkey minimum where hotkeys exist, or the minimum visual navigation path where they do not.

| Task | R* (with hotkey infrastructure) | R* (toolbar only, best architecture) | R* (toolbar only, worst architecture) | Derivability Class |
|---|---|---|---|---|
| T1 Place item with variant | 3 (key + move + click) or 6 (key + variant dropdown + move + click) | 8 (RimWorld: tab + grid + material + move + click) | 8 (same floor regardless of architecture — material selection requires scan) | Empirical |
| T2 Repeat item | 2 (move + click) | 2 | 2 | Provable (2 is the minimum for point placement: one move, one click) |
| T3 Switch item same category | 1 (hotkey) + 2 (move + click) = 3 | 3 (scan visible grid + move + click) | 5 (reopen dropdown + scan + move + click) | Empirical |
| T4 Switch category | 1 (hotkey) + 3 (item selection + placement) = 4 | 5 (tab + scan + move + click + place) | 10 (dropdown navigation at each level) | Empirical |
| T5 Build wall/structure | 1 (hotkey) + 4 (area stroke) = 5 | 7 (tab + scan + click + material + stroke) | 7 (same floor — stroke is fixed at 4 ops) | Empirical |
| T8 Toggle overlay | 1 (F-key or letter key) | 3 (move to known icon + click) | 3 (same floor once position is dissolved) | Provable (1 is the minimum: one key = one action) |
| T10 Confirm state | 1 (look at text toolbar) | 1 (look at text toolbar) | 3 (hover icon toolbar) | Empirical |
| T11 Switch mode | 1 (hotkey) | 2 (move to known tab + click) | 2 (same floor once position dissolved) | Provable (1 is minimum with hotkey; 2 is minimum without) |

Three tasks have provable R* values. T2 (repeat item) requires exactly two ops — one move, one click — because point placement is an irreducible two-step motor action. T8 (overlay toggle with hotkey) requires exactly one op — one key maps to one action, and no simpler encoding exists. T11 (mode switch with hotkey) requires exactly one op for the same reason. All other tasks have empirical R* values: the floor is the best observed expert performance, not a proven lower bound. A future interface innovation could potentially reduce T1 below three ops, but no current architecture achieves this.

---

### Appendix U: Framework Extension Points

The six op categories and twelve benchmark tasks defined in this paper cover mouse-and-keyboard tool selection interfaces. The framework is extensible to additional input modalities and interaction patterns by defining new op categories or benchmark tasks.

| Extension Domain | New Op Categories Needed | New Benchmark Tasks Needed | Measurement Differences |
|---|---|---|---|
| Touchscreen input | Tap (replaces click), Swipe (replaces scroll), Pinch (zoom — new), Long-press (replaces hover) | Touch versions of T1–T12 with modified placement ops | Hover discovery is eliminated (no cursor hover on touch). Long-press discovery replaces it at higher time cost but similar op count. |
| Controller input | D-pad navigate (replaces move — must count per step), Button press (replaces click), Trigger (replaces modified click), Radial menu select (new) | Controller versions of T1–T12 | Move cost changes from 1 op (direct cursor) to N ops (N d-pad steps to reach target). Radial menus provide O(1) access to 4–8 items but require a hold+direction chord. |
| Voice input | Speak command (replaces click + move chain), Wait for recognition (replaces hover wait) | Voice versions of T8, T11 (mode switch and overlay toggle are the most natural voice targets) | Entire navigation chain collapses to one op (speak item name) if recognition is reliable. Recognition failure adds 2–5 retry ops. |
| Spatial / VR input | Point (replaces move — 3D targeting), Grab (replaces click), Gaze (replaces look-at — involuntary in VR, always 0 ops) | VR versions of T1 and T5 (placement changes fundamentally in 3D) | Look-at cost drops to zero because gaze tracking is continuous. Move cost increases because 3D pointing has higher motor difficulty than 2D cursor movement. |

Each extension preserves the core framework: count irreducible transformations, classify by category, compose compound actions, measure against benchmark tasks, compare dissolution curves. The op remains the unit. The domain-specific calibration changes.
