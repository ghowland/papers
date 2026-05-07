## Axis 1: Mechanism Families and Mechanisms

Mechanisms are the primitive building blocks of player experience. They are what the game presents to the player and what the player does in response. Identified by function, not by implementation or aesthetic.

```
mechanism_families(id|family|role)
GF1|Gating|require the player to demonstrate or achieve before proceeding
GF2|Temporal Structure|nested time loops at which play operates
GF3|Information|what the player can observe, infer, or discover
GF4|Agency|how player intent translates to game state change
GF5|Consequence|what happens when the player succeeds or fails
GF6|Pressure|external demands on player attention and resources
GF7|Progression|how player capabilities, knowledge, or access change over time
GF8|Resource Systems|what the player tracks, accumulates, spends, and manages
GF9|System Interaction|how the game's subsystems relate to each other
```

```
mechanisms(id|name|family|definition|sub_types|notes)
```

**GF1 — Gating**

```
GM01|Skill gate|GF1|requires player to execute an action at sufficient quality|dexterity(timing+precision)+optimization(find good-enough solution)+execution(perform known solution under pressure)|Dark Souls dodge timing; Quake aim; platformer jump
GM02|Knowledge gate|GF1|requires player to possess specific information|location(where is X)+procedure(how to do X)+combination(what goes with what)+lore(what is the context)|find the red key; know the NPC's password; know weakness of enemy type
GM03|Resource gate|GF1|requires player to spend or possess resources to proceed|currency+consumable+equipment+capacity(carry weight)+permanent(skill points)|pay 500 gold to enter; need lockpick to open; need 50 STR
GM04|Comprehension gate|GF1|requires player to understand a system well enough to solve|puzzle(put system into target state)+deduction(infer rule from evidence)+pattern(recognize recurring structure)|Zelda dungeon mechanics; Baba Is You rule comprehension; Portal physics
GM05|Traversal gate|GF1|requires player to cover distance or navigate space|walking(continuous cost)+fast-travel-known(first-visit gated then released)+fast-travel-cost(persistent soft gate)+none(instant teleport)|Death Stranding full traversal; Skyrim two-phase; GTA taxi
GM06|Time gate|GF1|requires player to wait|real-time(wall clock)+game-time(simulated clock)+cooldown(action becomes available after delay)+seasonal(event available only at certain times)|mobile game timers; crop growth; ability cooldowns; holiday events
GM07|Discovery gate|GF1|requires player to find the question not just the answer|exploration(find the thing)+experimentation(try combinations)+observation(notice something the game doesn't highlight)|DF hidden system interactions; secret areas; unmarked quests
GM08|Social gate|GF1|requires cooperation or negotiation with other players|group-size(need N players)+role(need specific capability)+trust(need established relationship)+competition(must outperform others)|MMO raid requirements; trading; PvP ranking thresholds
```

**GF2 — Temporal Structure**

```
GM09|Reaction loop|GF2|0.2s — trained motor response to immediate stimulus|timing(hit window)+precision(aim accuracy)+rhythm(repeated pattern)|dodge roll; railgun shot; rhythm game beat
GM10|Tactical loop|GF2|2s — immediate situation reading and action selection|threat assessment+opportunity recognition+micro-positioning|Pac-Man ghost avoidance; DS attack-or-dodge decision; cover selection
GM11|Engagement loop|GF2|10s — completing a discrete interaction unit|combat encounter+conversation+single puzzle+transaction|one firefight; one NPC dialogue; one room of a dungeon
GM12|Navigation loop|GF2|60s — moving between engagement points|pathfinding+landmark orientation+incidental encounters+route optimization|walking between map points; driving across town; exploring a floor
GM13|Objective loop|GF2|300s — completing a quest phase or mission|multi-engagement sequence+gate traversal+evidence gathering+return|Fallout NV quest loop; dungeon clear; mission completion
GM14|Strategic loop|GF2|3000s — long-term planning and build decisions|character build+faction alignment+base layout+resource allocation strategy+campaign planning|skill point allocation; DF fortress design; Civ tech path
GM15|Loop nesting|GF2|active inner loops sustain engagement within outer loops|nested(inner loop demanded during outer)+interrupted(discrete events break outer loop)+empty(outer loop has no inner demand)|Death Stranding 0.2s in 300s = nested; Skyrim walking = empty navigation; RimWorld raid during building = interrupted
```

**GF3 — Information**

```
GM16|Full observability|GF3|entire game state visible simultaneously|board-visible+no-hidden-state+no-fog|Pac-Man; chess; tactics games; Battle Brothers (combat)
GM17|Partial observability|GF3|some game state hidden by design|fog-of-war+off-screen+unexplored+behind-player|Quake FOV; Skyrim unexplored map; RTS fog
GM18|System opacity|GF3|game systems exist that the player must discover or infer|hidden-mechanics+undocumented-interactions+emergent-behaviors+depth-beyond-UI|DF material properties; hidden damage formulas; unannounced system interactions
GM19|Feedback signal|GF3|game communicates state change to the player|immediate(hit confirmation+damage number)+delayed(quest log update)+ambient(world state change)+absence(lack of signal as information)|damage numbers; health bar change; minimap update; enemy audio cues
GM20|Causal legibility|GF3|player can trace why something happened|short-chain(A caused B)+long-chain(A caused B caused C caused D)+illegible(outcome has no traceable cause)+discoverable(cause exists but requires investigation)|RimWorld mood breakdown cause chain; DF tantrum spiral; Pac-Man ghost behavior
GM21|Information asymmetry|GF3|different parties have different knowledge|player-vs-game(AI knows things player doesn't)+player-vs-player(competitive hidden info)+temporal(player knows now what they didn't know before)|poker hands; fog of war in multiplayer; learning enemy patterns across attempts
```

**GF4 — Agency**

```
GM22|Direct control|GF4|player input maps immediately to game entity action|avatar movement+camera control+action execution+menu selection|Quake player movement; Pac-Man direction; Skyrim combat
GM23|Indirect control|GF4|player sets priorities or rules and autonomous agents execute|work priorities+behavior rules+zone designation+standing orders|RimWorld colonist priorities; DF labor assignments; auto-battle settings
GM24|Authorial creation|GF4|player designs or builds persistent artifacts within the game|freeform(unconstrained placement)+constrained(grid or rules)+functional(creation affects gameplay)+decorative(creation is aesthetic only)|SimCity city layout; Minecraft building; DF room designation; RimWorld base design
GM25|Selection/commitment|GF4|player chooses from presented options with lasting consequence|dialogue choice+build path+faction alignment+permanent upgrade|Fallout NV faction choice; skill tree selection; dialogue that locks quest paths
GM26|Timing agency|GF4|player chooses when to act within a permissive window|when-to-engage+when-to-retreat+when-to-use-consumable+when-to-commit-resources|choosing when to attack in DS; when to pop the power pellet in Pac-Man; when to launch raid in RTS
```

**GF5 — Consequence**

```
GM27|Lethality|GF5|failure results in entity death or destruction|instant(one-shot)+gradual(health depletion)+conditional(specific failure mode)|Rainbow 6 one-shot; Dark Souls health bar; fall damage
GM28|Resource loss|GF5|failure costs accumulated resources|partial(lose some)+total(lose all)+specific(lose particular resource)+permanent(cannot recover)|DS soul loss; inventory drop on death; ammo spent on missed shots
GM29|Progress loss|GF5|failure reverts advancement|checkpoint(return to save)+run-loss(start over)+partial-revert(lose recent gains only)|DS bonfire respawn; roguelike permadeath; losing last 5 minutes to a crash
GM30|State persistence|GF5|consequences remain in the game world|permanent-death(NPC gone forever)+world-change(environment altered)+reputation(faction remembers)+degradation(equipment wears)|Fallout NV faction reputation; weapon durability; permanent NPC death
GM31|Low consequence|GF5|failure has minimal or temporary cost|retry-free(immediate retry no cost)+time-only(lost time is only cost)+cosmetic(failure changes appearance not function)+cushioned(game prevents total loss)|casual game retry; Skyrim quicksave; auto-save before boss; rubber-banding in racing
GM32|Positive consequence|GF5|success grants reward|resource-gain+capability-gain+access-gain+information-gain+narrative-payoff|XP; loot; new area unlocked; quest completion; story revelation
```

**GF6 — Pressure**

```
GM33|Disruption pressure|GF6|discrete events that demand immediate response|raids+enemy spawns+random events+environmental hazards+time-limited threats|RimWorld raids; DF forgotten beasts; random dragon in Skyrim
GM34|Constraint pressure|GF6|continuous limits that shape ongoing decisions|budget+map-geography+time-flow+population-cap+technology-prerequisites|SimCity budget; RimWorld map biome; tech tree requirements
GM35|Cognitive load|GF6|total mental demand across all active systems|system-tracking(how many systems active)+state-tracking(how much state to remember)+decision-frequency(how often must choose)+causal-depth(how far back must trace)|DF many-system tracking; chess deep evaluation; RimWorld moderate tracking
GM36|Time pressure|GF6|real-time demands limiting deliberation|continuous(always ticking)+episodic(pressure during events only)+self-paced(player controls time flow)+turn-based(no time pressure per turn)|Quake continuous; RimWorld pausable; chess clock; Civ turn-based
GM37|Escalation|GF6|pressure increases over time or with progress|linear(steady increase)+stepped(jumps at thresholds)+adaptive(responds to player performance)+wave(cycles of intensity)|Pac-Man speed increase; DF increasingly serious threats; Left 4 Dead AI director
```

**GF7 — Progression**

```
GM38|Character advancement|GF7|player entity gains quantitative power|stats+skills+levels+perks+talent-trees|Skyrim skill leveling; DS soul level; RPG experience systems
GM39|Equipment acquisition|GF7|player gains tools that modify capability|weapons+armor+consumables+utility-items+crafted-gear|loot drops; shop purchases; crafted items; found weapons
GM40|Spatial discovery|GF7|map or world knowledge expands|map-reveal+landmark-discovery+fast-travel-unlock+shortcut-discovery+area-access|Skyrim location discovery; DS shortcut unlocks; fog of war clearing
GM41|Knowledge accumulation|GF7|player learns game systems through play|enemy-patterns+system-rules+optimal-strategies+hidden-mechanics+speedrun-routes|learning DS boss patterns; learning DF material properties; learning Pac-Man ghost AI
GM42|Access expansion|GF7|new content or systems become available|zone-unlock+ability-unlock+difficulty-tier+new-game-plus+narrative-branch-access|new areas after boss; new mechanics introduced in later levels; NG+ in DS
GM43|Gate release|GF7|previously gated content becomes freely available|fast-travel-unlock+shortcut-permanent+ability-removes-gate+key-items-persist|Skyrim discovered locations; DS opened shortcuts; Metroid ability-gated areas
```

**GF8 — Resource Systems**

```
GM44|Depletable resource|GF8|consumed on use, must be replenished|health+ammunition+consumables+fuel+food|health potions; bullets; RimWorld food stores; DS estus flask
GM45|Accumulated resource|GF8|grows over time, spent on advancement or gating|experience+currency+reputation+research-points+materials|gold; XP; RimWorld steel/components; Civ science points
GM46|Capacity resource|GF8|bounded pool that constrains other activities|inventory-space+carry-weight+unit-cap+building-space+action-points|Skyrim carry weight; RimWorld colonist count; XCOM action points; SimCity buildable area
GM47|Regenerating resource|GF8|depletes and refills on a cycle|health-regen+stamina+mana+cooldowns+respawning-items|DS stamina bar; shield recharge; Quake item respawn timers; mana regen
GM48|Attention resource|GF8|player's real cognitive capacity allocated across demands|this is the meta-resource — not tracked in-game but consumed by gameplay|splitting attention between base building and raid response; tracking multiple unit positions; monitoring multiple system states simultaneously
```

**GF9 — System Interaction**

```
GM49|Independent systems|GF9|game systems operate without affecting each other|parallel-progression+isolated-mechanics+non-interacting-subsystems|Skyrim alchemy and smithing as separate systems (mostly)
GM50|Coupled systems|GF9|output of one system feeds input of another|resource-chain+stat-dependency+prerequisite-chain|RimWorld food→mood→productivity→defense; crafting material chains
GM51|Emergent interaction|GF9|systems combine to produce outcomes not individually designed|unscripted-combinations+cascading-effects+player-discovered-synergies|DF fluid dynamics + fortress design = flooding defense; RimWorld animal revenge chain events; Breath of the Wild fire+wind+grass
GM52|Feedback loops|GF9|system output reinforces or dampens its own input|positive(success breeds success)+negative(success breeds difficulty)+stabilizing(extremes self-correct)+destabilizing(problems cascade)|death spiral (wounded colonists can't fight, more get wounded); rich-get-richer snowball; rubber-banding
```

---

## Axis 2: Properties

Properties are contracts about player experience. They claim that something holds across play. They are not mechanisms — they are qualities that emerge from mechanism configuration.

```
property_bands(id|band|role)
PB1|Engagement|claims about whether and how the game holds player attention
PB2|Fairness|claims about the relationship between player action and outcome
PB3|Comprehensibility|claims about whether the player can understand what is happening
PB4|Progression|claims about how the player's experience changes over time
PB5|Expression|claims about whether the player can realize their intent
```

```
properties(id|name|band|claim|conditions|partial_provision|does_not_claim)
```

**PB1 — Engagement**

```
GP01|Pacing|PB1|the rate of new content, challenge, and reward stays within a productive range for the target player|target player specified; productive range means neither overwhelmed nor bored|well-paced in early game but padded in late game|that the game is fun — only that delivery rate is calibrated
GP02|Tension|PB1|the player experiences meaningful uncertainty about outcomes they care about|requires stakes (consequence) + uncertainty (information incompleteness or skill challenge) + investment (player cares about outcome)|tension in combat but not in exploration|that tension is constant — peaks and valleys are part of pacing
GP03|Flow|PB1|challenge matches player skill closely enough to sustain absorbed engagement|requires calibrated difficulty + clear feedback + achievable-feeling goals|flow in core loop but not in menus or inventory management|that the game is easy — flow can occur at very high difficulty if skill matches
GP04|Cognitive budget fit|PB1|total cognitive demand across all active loops stays within target player's capacity|target player specified; all active loops counted; demand includes tracking + deciding + executing|fits during normal play but overwhelms during crisis peaks|that the game is simple — only that demand is matched to audience
```

**PB2 — Fairness**

```
GP05|Attributability|PB2|player successes and failures feel caused by the player's own decisions and actions|requires consequence to follow legibly from action; randomness if present must be within player's risk assessment|attributable in combat but not in random loot|that outcomes are deterministic — only that outcomes are traceable to player action within the game's randomness model
GP06|Anticipatability|PB2|the player can prepare for challenges if they attend to available information|requires information model sufficient for preparation; consequence model harsh enough to motivate preparation|anticipatable for repeat encounters but not first encounters|that surprises never happen — only that the game doesn't punish based on unknowable information
GP07|Consistency|PB2|same game situations produce same ranges of outcomes|rules don't change arbitrarily; systems behave reliably; exceptions are rare and signaled|consistent within a system but not across patches or updates|that outcomes are predictable — complex system interaction may produce surprising-but-consistent results
GP08|Proportionality|PB2|the severity of consequences matches the magnitude of the player's error or the challenge's difficulty|small mistakes have small costs; large mistakes have large costs; easy challenges give small rewards; hard challenges give large rewards|proportional in combat but not in instant-death traps|that the game is gentle — only that consequence scales with error
```

**PB3 — Comprehensibility**

```
GP09|Legibility|PB3|the player can perceive the current game state with sufficient clarity to make informed decisions|requires feedback signals + UI clarity + state representation|legible for core systems but not for hidden subsystems|that the game is transparent — some opacity is intentional (fog of war, hidden enemy stats)
GP10|Causal clarity|PB3|the player can understand why outcomes occurred|requires traceable cause-effect chains at the depth the player needs for their current loop level|clear for immediate causes but opaque for systemic cascades|that every cause is shown — only that causes are discoverable at appropriate effort
GP11|System learnability|PB3|the player can discover how game systems work through play|requires systems to be consistent enough to learn + feedback to confirm or deny hypotheses|learnable for core mechanics but not for rare edge cases|that the game teaches explicitly — learning through experimentation and failure is valid
GP12|Depth|PB3|more remains to discover or master beyond initial understanding|requires system interaction or combinatorial complexity that exceeds surface presentation|deep in core systems but shallow in side systems|that depth is visible — hidden depth is still depth
```

**PB4 — Progression Quality**

```
GP13|Mastery curve|PB4|player skill and knowledge grow in a satisfying trajectory|requires calibrated difficulty escalation + new challenges that test new skills + plateaus that feel temporary|good mastery curve in combat but flat in crafting|that mastery is linear — plateaus and breakthroughs are normal
GP14|Investment return|PB4|time and effort spent translate into meaningful capability or access gain|requires progression mechanisms that reward engagement proportionally|good return on main quest but poor return on side activities|that all time spent is equally rewarded — some activities can be their own reward
GP15|Meaningful choice|PB4|player decisions produce distinguishable outcomes they can perceive and evaluate|requires branching consequences that the player can observe diverging|meaningful in faction choice but not in dialogue options that converge|that choices are permanent — reversibility doesn't negate meaningfulness if the experience of choosing was real
GP16|Discovery satisfaction|PB4|finding new content, mechanics, or interactions feels rewarding|requires things to find + signals that finding occurred + novelty relative to what's known|satisfying for major discoveries but routine for minor ones|that all content is hidden — deliberately placed discoverable content is valid
```

**PB5 — Expression Quality**

```
GP17|Creative freedom|PB5|the player's authorial intent can be meaningfully realized through game mechanisms|requires authorial agency + sufficient building vocabulary + system responsiveness to player-created artifacts|free in building but constrained by resources or physics|that expression is unconstrained — constraints can enhance creative expression
GP18|Resilience of expression|PB5|player-created artifacts survive disruption pressure long enough to be satisfying|requires disruption frequency low enough or defenses strong enough that creations persist|resilient to minor events but destroyed by major ones|that creations are permanent — only that the ratio of build-time to survival-time feels worthwhile
GP19|Systemic responsiveness|PB5|the game's systems respond meaningfully to what the player builds or creates|requires coupled systems that evaluate player-created artifacts|responsive to structural choices but not to decorative ones|that response is always positive — negative response (your design failed) is still responsiveness
```

---

## Axis 3: Principles

Principles are rules governing design choices. They select among mechanisms and constrain how properties are realized. They do not perform work or make claims about specific guarantees.

```
principle_groups(id|group|role)
PG1|Gating discipline|govern how and when the game restricts the player
PG2|Information discipline|govern what the player knows and when
PG3|Consequence discipline|govern the cost structure of play
PG4|Tempo discipline|govern the rhythm and timing of experience
PG5|Complexity discipline|govern how much the game demands of the player
PG6|Expression discipline|govern the player's creative and strategic agency
```

```
principles(id|name|group|rule|reasoning|counter_principles)
```

**PG1 — Gating Discipline**

```
GR01|Gate for function not duration|PG1|every gate should serve a gameplay purpose (teaching, testing, pacing) — never exist solely to extend play time|gates that exist only for duration feel like padding; players recognize and resent content-free time sinks|time gates in free-to-play serve monetization not gameplay; valid as business mechanism but violates this principle as game design
GR02|Match gate to demonstrated need|PG1|the type of gate should test what the player needs to demonstrate for the next content to be meaningful|a skill gate before a skill-demanding section is coherent; a fetch quest before a story revelation is incoherent unless the fetch teaches something needed|sometimes gates serve pacing even when the type doesn't match the upcoming content
GR03|Release gates that have served their purpose|PG1|once a gate's function is fulfilled, continuing to impose it is cost without benefit|Skyrim fast travel after first visit; DS shortcuts after area mastery; the gate taught or tested what it needed to|some games intentionally never release traversal gates (survival games) as a persistent resource cost
GR04|Signal gates clearly|PG1|the player should know a gate exists and roughly what it requires before investing effort toward it|invisible gates produce frustration because the player cannot plan; visible gates produce anticipation and goal-setting|discovery gates are intentionally unsignaled — the search itself is the gameplay; this principle applies to progression gates not discovery gates
```

**PG2 — Information Discipline**

```
GR05|Match information to consequence|PG2|don't punish the player for things they couldn't have known or reasonably anticipated|high-consequence actions require sufficient information for the player to make an informed choice; ambush by a previously-invisible enemy that one-shots you violates this|first encounters are inherently low-information; this principle requires either low consequence on first encounter or sufficient pre-encounter signals
GR06|Reward observation|PG2|players who attend carefully to available information should gain advantage over those who don't|if attentive play and inattentive play produce the same outcomes, the information system is decorative not functional|some information should be subtle enough that only attentive players notice, creating a skill gradient in observation itself
GR07|Make state observable to the degree needed for the active loop|PG2|the player needs different information at different loop levels — show what's needed for the current decision timescale|0.2s loop needs immediate visual/audio feedback; 300s loop needs quest tracker and map; 3000s loop needs character sheet and build planner|too much information at the wrong loop level is noise; showing strategic data during a twitch fight is clutter
GR08|Legibility scales with system depth|PG2|deeper systems need more legibility investment to remain comprehensible|DF's depth with DF's legibility is niche; RimWorld's depth with RimWorld's clearer UI is broader; simplifying the UI without simplifying the system is the ideal|full legibility of very deep systems can reduce discovery satisfaction; some opacity serves gameplay
```

**PG3 — Consequence Discipline**

```
GR09|Consequence proportional to error|PG3|small mistakes should cost little; large mistakes should cost much; unavoidable situations should cost nothing|disproportionate punishment feels unfair; disproportionate leniency removes tension; punishing the unavoidable feels arbitrary|some games intentionally use high consequence for small errors (one-shot mechanics) as a genre-defining choice; this creates high anticipation play
GR10|Consequence legible before commitment|PG3|the player should understand what they risk before taking an action with significant cost|blind commitment to high-consequence actions feels like a gotcha; informed commitment creates tension and meaningful choice|roguelikes intentionally obscure some consequences as part of the discovery model; the principle applies most to irreversible choices
GR11|Provide recovery paths proportional to consequence severity|PG3|the harder the punishment, the more the game should provide ways to recover or avoid it|Dark Souls loses your souls but lets you retrieve them; permadeath games give you meta-knowledge that persists|some games intentionally provide no recovery as a difficulty commitment
GR12|Couple consequence to expression when expression exists|PG3|in games with authorial creation, disruption should test the creation rather than randomly destroy it|RimWorld raids test your defenses (coupled); random meteor on your base (uncoupled) feels arbitrary; coupled disruption validates expression|pure destruction events serve the fantasy of unpredictability in some games (asteroid in SimCity); genre-dependent
```

**PG4 — Tempo Discipline**

```
GR13|Active inner loops sustain outer loops|PG4|long-duration activities need continuous player engagement at a shorter timescale to remain interesting|Death Stranding walking works because balance is a 0.2s inner loop; Skyrim walking is empty because there's no inner loop until an encounter event|some games intentionally use empty traversal for atmospheric purposes; this is an aesthetic choice that works against engagement
GR14|Vary loop intensity over time|PG4|sustained high intensity exhausts; sustained low intensity bores; alternation sustains engagement|action sequences need quiet aftermath; building phases need disruption punctuation; the cycle of tension and release is structural|some games commit to sustained intensity (Doom Eternal) or sustained calm (Stardew Valley) as genre identity
GR15|Interruptions should arrive at a frequency the target player can absorb|PG4|too frequent overwhelms; too infrequent removes challenge and tension; frequency should match the authorial or strategic loop it's interrupting|RimWorld's raid frequency is calibrated to colony development pace; DF's can overwhelm because more things generate interruptions|adaptive difficulty systems (Left 4 Dead AI Director) try to solve this dynamically
GR16|Self-directed and imposed activities should be coupled|PG4|the things the player wants to do and the things the game makes them do should reinforce each other|building defenses (self-directed) is motivated by raids (imposed); if they're unrelated the player resents the imposed activities|sandbox games sometimes decouple these intentionally, letting the player opt out of imposed activities
```

**PG5 — Complexity Discipline**

```
GR17|Depth through interaction not enumeration|PG5|prefer fewer systems that interact richly over many systems that operate independently|chess has few piece types but deep interaction; a game with 50 independent crafting materials has enumeration without depth|some games use large variety as content (Pokemon collection); enumeration can serve completionism goals
GR18|Introduce systems at the rate the player can absorb|PG5|new mechanics should arrive when previous ones are understood, not before|tutorial pacing; DS introduces one enemy type per area; overwhelming front-load causes abandonment|expert players may find gradual introduction patronizing; difficulty/experience settings can address this
GR19|Cognitive demand should serve gameplay purpose|PG5|every system the player must track should contribute to meaningful decisions|tracking 12 resource types is justified if they create interesting tradeoffs; tracking 12 that all do the same thing is waste|some cognitive complexity serves flavor or simulation fidelity even if it doesn't create strategic depth; genre-dependent
GR20|Reduce depth for breadth of audience, not by removing interaction|PG5|when simplifying, preserve system coupling and remove system count rather than making systems independent|RimWorld simplified DF by having fewer systems that still interact, not by having the same systems disconnected|sometimes isolating systems serves accessibility — letting players engage with one system without being forced into others
```

**PG6 — Expression Discipline**

```
GR21|Constraints enhance expression|PG6|creative freedom is more satisfying with meaningful constraints than without them|Minecraft creative mode is less engaging than survival for most players because unlimited resources remove the puzzle of expression; constraints make choices meaningful|pure sandbox/creative modes serve a different need (relaxation, pure authoring); the principle applies to expression-as-gameplay
GR22|Expression should be testable|PG6|the game should provide feedback on whether the player's creation works|SimCity tests your city with traffic and budget; RimWorld tests your base with raids; untested expression has no gameplay loop|decorative expression (house decorating in Skyrim) is valid without testing; this principle applies to functional expression
GR23|Protect expression investment proportionally|PG6|the longer the player worked on something, the more the game should protect it from instant destruction|a wall that took 3 hours to build shouldn't be destroyed in 3 seconds by a random event with no counterplay; destruction should be proportional to construction investment or at minimum be preventable|some games use disproportionate destruction as a difficulty signature; genre choice
```

---

## Cross-References Still Needed

The infrastructure taxonomy has several structural elements we haven't built yet but will need:

- **Double citizens** — words that name both mechanism and property (progression, depth, challenge)
- **Spanning mechanisms** — mechanisms that genuinely belong to two families
- **Orthogonality distinctions** — pairs that sound related but are independent
- **Confusions** — commonly conflated pairs with distinguishing questions
- **The triangle** — how mechanisms provide properties, properties require mechanisms, principles select among mechanisms
- **Application layer** — game genre classification by structural profile (the equivalent of AC01–AC33)
- **Gap analysis** — where game design vocabulary diverges from what's actually happening structurally
- **Fast locator** — symptom-to-family reverse index (game feels padded → check GF1 gating calibration)

