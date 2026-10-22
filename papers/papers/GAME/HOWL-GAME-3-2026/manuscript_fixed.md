# The Circuit System Method of Game Design

## A Unified Framework for Interactive World Construction Through Signal Composition

**Registry:** [@HOWL-GAME-3-2026]

**DOI:** 10.5281/zenodo.23552222

**Date:** October 2026

**Domain:** Game Design Theory / Systems Design

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.8. 

---

## Abstract

This paper presents a method for designing interactive worlds where every game element — items, quests, characters, relationships, narrative structures, and settings — operates as a component in one interconnected circuit. Instead of designing separate systems for combat, economy, dialogue, and exploration, the designer authors components with signal pins, connects them through shared buses, and lets the engine evaluate the resulting circuit. Emergent gameplay, proportional narrative consequences, and cross-system interactions arise from the circuit's operation without scripted bridges between systems.

The method is grounded in six design domains: Inventory, Quest, Relationship, Character, Narrative, and Setting. Each domain contributes components, connections, and signal sources to a shared circuit board. The paper maps each domain to established game design methodologies, demonstrates how the circuit model extends existing practice, and provides practical guidance for designers adopting the approach.

---

## 1 Introduction

### 1.1 The Problem This Method Addresses

Game designers think in systems. A combat system has health, damage, armor, and weapons. An economy system has currency, prices, supply, and demand. A social system has reputation, trust, factions, and obligations. Each system is coherent internally. The difficulty is the connections between them.

In traditional game development, each system is built as an independent module. Connecting two systems requires bridge code: when health drops below a threshold in the combat system, notify the dialogue system to change NPC behavior. When the player sells a rare item in the economy system, notify the reputation system to increase merchant trust. Each bridge is a special case. A game with ten systems can require up to a hundred bridges. Each bridge must be specified, implemented, tested, and maintained.

The designer's creative ambition frequently exceeds the bridge budget. The designer imagines that a burning building should produce smoke that drifts with the wind, spoiling food in downwind storage, sickening colonists who eat the spoiled food, reducing their work output, which reduces fence repair rates, which lets cattle escape during the next stampede, which reduces the colony's wealth, which emboldens bandits, which causes the next raid. This chain crosses seven systems. Implementing it requires six bridges that did not exist when the systems were built.

The Circuit System Method eliminates the bridge problem by eliminating the system boundaries. There is one system. Every value in the game is a signal on a shared bus. Every action is a conversion between signals. Every connection between values is a circuit element. The chain from burning building to bandit raid is not seven bridges. It is one circuit path through shared buses, evaluated by one engine, authored by one toolset.

### 1.2 Who This Method Is For

This paper is for game designers who already understand game systems design and want a framework that unifies their systems into one composable architecture. The reader should be familiar with:

- Resource management (values that increase, decrease, and constrain player action)

- State machines (discrete states with transition conditions)

- Decision trees or utility-based AI (scoring and selecting from available actions)

- Spatial simulation (tile-based or grid-based world representation)

- Narrative structures (quests with objectives, obstacles, and rewards)

The method does not require programming knowledge. The designer works entirely with data: named values, conversion rules, calculations, labels, and connections. The engine evaluates the data. The designer tunes the results.

### 1.3 Core Concept

Every game element is a component with input and output pins on signal buses. A torch has pins on the optical bus (light output), the thermal bus (heat output), the acoustic bus (noise output), the mechanical bus (weight), and the temporal bus (burn duration). A quest obstacle has input pins that accept signal from specific buses. A character attribute is a bus that supplies bandwidth to skill pins. A relationship is a capacitor that stores trust and discharges through betrayal.

The designer's job is to specify the components (what pins they have), the buses (what signal types exist), and the connections (which outputs feed which inputs). The engine evaluates the circuit each tick and produces the game state. The designer does not script outcomes. The designer designs circuits. Outcomes emerge from the circuit's operation.

---

## 2 The Six Domains

The method organizes game content into six domains. Each domain contributes a specific type of component to the circuit. All six domains share the same signal buses. A signal generated in any domain can propagate to any other domain through bus connections.

### 2.1 Inventory Domain

The Inventory domain defines items as multi-pin components. Each item has output pins on every bus it can generate signal on, and input pins on every bus it can accept signal from.

**Traditional approach:** An item has a fixed list of properties (damage, armor, weight, value) and a fixed list of uses (equip, use, consume, drop). The designer authors each use as a specific interaction. A torch illuminates. A rope climbs. A mirror reflects. Each use is a separate implementation.

**Circuit approach:** An item has pins on multiple buses. A torch has pins on optical (light), thermal (heat), acoustic (crackle), mechanical (weight, improvised weapon), and temporal (burn duration) buses. The designer does not author "uses." The designer specifies the pin amplitudes and signal types. Uses emerge from which pins connect to which quest, relationship, or setting inputs. The same torch that illuminates a dungeon (optical output accepted by darkness hazard input) also ignites oil (thermal output exceeding oil's ignition threshold), signals an ally (optical output visible at range), tests airflow (thermal output deflected by drafts), and serves as a timer (temporal output counting down). None of these uses are individually authored. They follow from the pin specifications.

**Key insight for designers:** Stop thinking about what items DO. Start thinking about what signals items EMIT. Every signal an item emits can connect to every compatible input in the game. The combinatorial space of possible uses grows with the number of buses, not with the number of authored interactions.

### 2.2 Quest Domain

The Quest domain defines objectives as impedance networks. Each quest obstacle is an impedance on a specific bus. The player must drive sufficient signal through the impedance to proceed.

**Traditional approach:** A quest has a sequence of objectives, each with a fixed solution. Kill the guard (combat), pick the lock (stealth), persuade the merchant (dialogue). Each objective accepts input from one system. The designer authors the solution path.

**Circuit approach:** A quest objective is an impedance with input pins on multiple buses. A locked door has input pins on the mechanical bus (force it open), the information bus (pick the lock), the thermal bus (burn it down), the social bus (convince the owner), and the magical bus (cast a spell). The designer specifies the impedance threshold on each pin. The player selects which bus to drive signal through. Any bus that delivers sufficient signal overcomes the impedance. The designer does not author solution paths. The designer authors impedances. Solution paths emerge from the player's available components and their pin configurations.

**Key insight for designers:** Stop authoring solutions. Start authoring obstacles. Specify what the obstacle resists and how strongly it resists on each bus. The player will find paths through the impedance network that you did not anticipate. If the circuit math works, the solution is valid.

### 2.3 Relationship Domain

The Relationship domain defines connections between entities as circuit branches with stored energy. Each relationship carries values for trust, respect, fear, obligation, and other social signals. These values are capacitors that charge through positive interaction and discharge through betrayal.

**Traditional approach:** An NPC has an affinity number. Gifts increase it. Insults decrease it. At threshold values, new dialogue options or quest access opens. The affinity is a flat number with no history, no inertia, and no network effects.

**Circuit approach:** A relationship is a branch with multiple values, each carrying its own history. Trust built over fifty game sessions accumulates inductance energy. If disrupted, the back-EMF (proportional to stored energy times disruption rate) produces consequences that scale with the relationship's depth. A casual acquaintance's betrayal produces small consequences. A lifelong friend's betrayal produces enormous consequences. The designer does not assign consequence severity. The inductance math produces proportional consequences from the accumulated history.

Relationships also carry coupling: trust changes with one entity propagate through the social network to connected entities, attenuated by distance and distorted by noise at each hop. Helping a faction leader improves standing with the leader's allies. Betraying the leader damages standing with the leader's allies. The propagation happens automatically through the coupling parameters. The designer does not script faction reputation updates. The coupling produces them.

**Key insight for designers:** Stop thinking about relationships as numbers. Start thinking about relationships as circuits with stored energy. A relationship that has been stable for a long time stores energy. That energy produces proportional consequences when the relationship changes. The longer and deeper the relationship, the larger the consequence. This produces dramatic weight from mechanics, not from scripted narrative beats.

### 2.4 Character Domain

The Character domain defines entities as layered circuits. Each layer provides services to the layer above and constraints to the layer below.

**Layer 1 — Body** defines the hardware platform: which buses exist, what the maximum signal capacity is, which environmental conditions the entity can tolerate.

**Layer 2 — Derived Stats** are computed from Layer 1 and Layer 3 values. Health, stamina, carrying capacity, and movement speed are derived values, not directly authored.

**Layer 3 — Attributes** define bus bandwidth. Strength sets the maximum signal on the mechanical bus. Charisma sets the maximum signal on the social bus. No skill or equipment can drive more signal through a bus than the attribute allows.

**Layer 4 — Skills** define specific path conductance. A skill is the percentage of attribute bandwidth that actually reaches the output pin. A Stealth skill of 70 means 70% of the Agility attribute's bandwidth reaches the stealth output. Skills improve efficiency within the attribute ceiling. They cannot exceed it.

**Layer 5 — Personality** defines gain settings, filters, and routing biases. Personality parameters (aggression, caution, empathy, loyalty, honesty) modify which quest paths the character defaults to, what sanity cost is imposed when the player overrides the default, and how the character's AI scores available actions.

**Layer 6 — Background** defines pre-charged capacitors. The character's origin, formative events, pre-existing relationships, and accumulated trauma are initial values on various circuit elements. A military veteran starts with combat skills charged, a trauma inductor installed, and relationship branches to former comrades pre-biased.

**Layer 7 — Archetype** defines routing policy. The archetype biases which actions the AI selects by adding consideration weights to specific goal types. A warrior archetype makes combat actions score higher. A diplomat archetype makes social actions score higher. The archetype does not restrict any action. It makes preferred actions more likely.

**Traditional approach:** A character has a class that determines available abilities, a set of attributes that modify ability effectiveness, and a background that provides flavor text and starting equipment.

**Circuit approach:** A character's class, attributes, skills, personality, and background are all signal values on the same buses. They interact through calculations, not through class-specific code. A warrior's combat effectiveness is a calculation: weapon damage (base) times weapon skill (base_scale) times strength attribute (modifier) times equipment bonus (modifier_scale). A diplomat's social effectiveness uses the same calculation structure: persuasion argument (base) times persuasion skill (base_scale) times charisma attribute (modifier) times outfit bonus (modifier_scale). The engine evaluates both through the same four-stage calculation. No class-specific code exists.

**Key insight for designers:** Stop thinking about classes as containers of abilities. Start thinking about characters as circuit boards with different component configurations. Every character has pins on every bus. Class differences are differences in which pins have high conductance and which pins have low conductance. A warrior has high conductance on the mechanical bus and low conductance on the social bus. A diplomat has the reverse. Both can attempt any action. The conductance determines how much signal gets through.

### 2.5 Narrative Domain

The Narrative domain defines story elements as circuit components that store, transform, and release dramatic energy.

**Secrets** are charged capacitors. A secret charges as the narrative progresses and the secret remains unrevealed. Each scene where the secret exists but is hidden adds charge. Discharge occurs at revelation. The dramatic impact of the revelation is proportional to the stored charge at the moment of discharge.

**Character consistency** is an inductor. Established behavioral patterns resist change. When a character acts out of established pattern, the inductance produces back-EMF proportional to how long the pattern was established and how suddenly it was broken. Gradual character change (low rate of change against moderate inductance) produces small back-EMF and feels natural. Sudden character reversal (high rate of change against high inductance) produces large back-EMF and feels dramatic or implausible, depending on whether the story has earned it.

**Dramatic irony** is a transformer. It multiplies the audience's experience of every scene by the ratio of audience knowledge to character knowledge. A scene where a character walks happily toward their doom has raw emotional content X. The irony transformer multiplies by the gap: audience sees doom, character sees happiness. Output equals X times the gap magnitude.

**Theme** is a power supply configuration. The same plot events powered by different themes produce different meanings. A character dies: under a justice theme, the death was deserved (feedback corrected deviation). Under an entropy theme, the death was inevitable (supply was decaying). Under an absurdism theme, the death was random. The theme does not change what happens. The theme changes what it means.

**Traditional approach:** Narrative is authored as a branching script. Each branch is written by hand. Consequences are hardcoded flags. There is no mechanical model of tension, irony, or thematic weight.

**Circuit approach:** Narrative elements are values on a narrative bus. Secret capacitor charge is a number that increases each tick the secret exists unrevealed. Tension voltage is computed as desire current times obstruction impedance. Thematic weight increments each time a theme-consistent event occurs. These are live values that the engine computes from the circuit state. A narrative AI or designer-authored trigger can read these values and shape events accordingly: introduce a new obstacle when tension drops, trigger a revelation when secret charge peaks, present a moral choice when character arc progress reaches a milestone.

**Key insight for designers:** Stop thinking about narrative as something you write. Start thinking about narrative as something the circuit produces. Author the circuit elements: desire sources (what characters want), impedances (what prevents them), secrets (what is hidden), and inductors (what resists change). The engine evaluates the circuit. Narrative tension, dramatic irony, and thematic coherence emerge from the circuit's operation. You shape the narrative by tuning circuit parameters, not by writing dialogue trees.

### 2.6 Setting Domain

The Setting domain defines the environment as a circuit board substrate. The substrate's properties modify every component mounted on it.

**Traditional approach:** The setting is a visual backdrop. A dungeon has dark textures. A forest has green textures. A city has building models. The setting affects gameplay only through pre-placed obstacles, enemies, and resources.

**Circuit approach:** The setting is a set of values that modify every calculation on every bus for every entity in the zone. A dungeon has zero ambient light (requiring light sources for optical bus function), high acoustic echo (amplifying noise), zero biological supply (requiring carried food and water), and moderate background threat (increasing stealth requirements). These are not flags. They are continuous values that feed into every calculation as modifiers. The same character with the same skills produces different effective capabilities on different substrates because the substrate values modify every calculation.

Parasitic rules on the substrate automatically generate side effects from activity. A stone dungeon has a parasitic rule: mechanical bus activity generates acoustic bus emission scaled by the echo multiplier. Combat in a stone dungeon is noisier than combat in an open field. The designer does not author "combat noise in dungeons." The parasitic rule produces it from the substrate properties.

**Key insight for designers:** Stop thinking about settings as backgrounds. Start thinking about settings as circuit board substrates. Every substrate property modifies every circuit on the board. A change in setting is a change in the operating conditions of every component. The same character who is effective in one setting may be ineffective in another, not because their stats changed, but because the substrate changed the effective conductance of every path.

---

## 3 The Four Circuit Elements

The six domains provide the components. Four circuit elements provide the dynamics.

### 3.1 Inductance — Resistance to Change

Inductance tracks how long a value has been stable and generates proportional consequences when the value changes.

**For game designers:** Inductance models inertia. A relationship that has been stable for months resists sudden change. A character who has behaved consistently for the entire game resists acting out of character. A faction that has been at peace for generations resists going to war. The resistance is proportional to stability duration. The consequence of overcoming the resistance (back-EMF) is proportional to the stored energy and the speed of change.

**Practical application:** Attach an inductance to any value that should have memory. Trust between characters. Mood stability. Political allegiance. Addiction level. Cultural tradition. The inductance produces natural behavioral inertia without scripted delay timers. It also produces proportional consequences: disrupting a deep stable pattern produces large consequences, disrupting a shallow recent pattern produces small consequences. The drama is proportional to the disruption, automatically.

**How existing designers can adopt this:** Take any game value that currently changes instantly (reputation gained, mood set, faction standing updated). Add inductance. The value now resists instant change. Rapid changes produce back-EMF events. The game becomes more realistic: relationships take time to build and produce proportional grief when broken. Factions take time to shift allegiance and produce proportional instability when they do. The designer tunes two parameters (accumulation rate and maximum energy) to control how fast inertia builds and how large the maximum consequence can be.

### 3.2 Coupling — Network Propagation

Coupling defines how value changes on one entity automatically propagate to connected entities.

**For game designers:** Coupling models social and physical networks. Trust changes with one character propagate to their friends. Reputation changes in one faction propagate to allied and rival factions. Mood changes in one colonist influence nearby colonists. Each propagation is attenuated per hop, delayed per hop, and optionally distorted by noise per hop. The designer specifies the coupling parameters. The engine propagates the signals through the network.

**Practical application:** Attach a coupling to any value that should spread. Reputation (factions hear about your deeds through their social network). Gossip (rumors propagate with increasing distortion). Market prices (supply changes in one market affect prices in connected markets). Morale (a unit's morale affects nearby units). Fear (a terrified NPC's behavior affects nearby NPCs).

**How existing designers can adopt this:** Take any game value that currently updates only on the affected entity (faction reputation is a number on the faction, not a propagating signal). Add coupling. The value now propagates through the relationship graph. Allied factions receive attenuated positive signals. Rival factions receive inverted signals. Distant contacts receive delayed, noisy signals. The game's social world becomes a network that responds as a network, not as a collection of isolated nodes.

### 3.3 Parasitic Rules — Automatic Side Effects

Parasitic rules define automatic emissions that occur whenever activity happens on a specific bus within a zone.

**For game designers:** Parasitic rules model unintended consequences. Combat generates noise. Fire produces light and smoke. Economic transactions generate social attention. Hacking generates surveillance alerts. The designer does not script each side effect. The designer specifies the substrate rule: "activity on this bus produces emission on that bus, at this coefficient, above this threshold." Every action in the zone that generates signal on the source bus automatically produces the side effect.

**Practical application:** Attach parasitic rules to zones that should have environmental side effects. A stone corridor amplifies combat noise. A corporate zone monitors digital activity. An undercity zone makes economic transactions conspicuous. A library zone suppresses acoustic emissions (negative parasitic: the zone absorbs noise rather than amplifying it).

**How existing designers can adopt this:** Take any game location where "things that happen here have consequences beyond the direct action." Define the consequence as a parasitic rule. Combat in a dungeon alerts nearby monsters (mechanical bus activity produces acoustic bus emission at 2.5x coefficient). The designer does not script "if combat, alert monsters." The parasitic rule generates the alert signal proportional to the combat intensity, attenuated by walls, detected by any entity whose hearing threshold is exceeded. The mechanic is granular, proportional, and spatial, from one data entry.

### 3.4 Oscillation Detection — Pattern Recognition

Oscillation detection monitors values for repeating patterns and fires events at milestones.

**For game designers:** Oscillation detection models cycles. Economic boom-bust cycles. Mood swings. Day-night temperature cycles. Combat stalemates. The detector monitors a value's history, counts threshold crossings, and reports frequency, amplitude, and trend. Events fire when oscillation begins, when amplitude exceeds a resonance threshold, when amplitude drops below a damping threshold, and when oscillation ceases.

**Practical application:** Attach oscillation detectors to values that might cycle. Colony mood (detecting instability). Market prices (detecting bubbles). Combat advantage (detecting stalemates). Relationship trust (detecting volatile relationships). The detector provides the engine with information about the pattern, which feeds into AI scoring, narrative bus values, and audio intensity modulation.

**How existing designers can adopt this:** Take any game value that you suspect oscillates and where the oscillation itself should produce gameplay consequences. Attach a detector. The engine reports whether the value is oscillating, how fast, how large the swings are, and whether the swings are growing or shrinking. This information can trigger stabilization mechanics (add damping when resonance approaches), narrative events (a boom-bust cycle produces a financial crisis storyline), or UI indicators (showing the player that the economy is unstable).

---

## 4 Mapping to Existing Design Methodologies

### 4.1 MDA Framework (Mechanics, Dynamics, Aesthetics)

The MDA framework describes games at three layers: Mechanics (rules), Dynamics (system behavior), and Aesthetics (player experience).

**Mechanics** in the circuit method are ResourceConversionSets: the rules that govern what actions are possible, what they cost, and what they produce. Each conversion set is a mechanic. The designer authors mechanics by specifying requirements and costs.

**Dynamics** in the circuit method are the four circuit elements: inductance, coupling, parasitic rules, and oscillation. These produce system behavior that the designer does not script. Trust propagating through a faction network is a dynamic. Mood inertia resisting sudden change is a dynamic. Combat noise alerting distant enemies is a dynamic. The designer authors the circuit element parameters. The dynamics emerge.

**Aesthetics** in the circuit method are what the player experiences when the circuit operates. The dramatic weight of a betrayal (proportional to inductance energy). The social network responding to the player's choices (coupling propagation). The world reacting to the player's presence (parasitic emissions). The rhythm of boom and bust (oscillation patterns). These aesthetics emerge from the dynamics, which emerge from the mechanics.

The circuit method provides a concrete implementation path for the MDA framework: author mechanics as conversion sets, author dynamics as circuit element parameters, and test aesthetics by running the circuit and observing the output.

### 4.2 Systems Design (Salen and Zimmerman)

Salen and Zimmerman's "Rules of Play" emphasizes that games are systems of interacting parts. The circuit method makes this literal. Every game part is a component on a shared bus. Every interaction is a signal path through the circuit. The designer's job is to design the circuit so that the interactions produce the intended experience.

The concept of "meaningful play" (where player actions have discernible and integrated outcomes) is served by the circuit's transparency. Every action produces traceable signal changes across all buses. The IC Browser shows the player's action rippling through the circuit. The outcomes are discernible (the player can see what changed) and integrated (the changes affect all connected systems through bus propagation).

### 4.3 Emergent Narrative (Dwarf Fortress, RimWorld Model)

Emergent narrative games generate stories from simulated systems rather than authored scripts. The circuit method extends this approach with structured narrative tools.

Traditional emergent narrative relies on system interactions producing interesting situations that the player interprets as stories. The circuit method adds narrative bus values (secret capacitor charge, tension voltage, thematic weight, motif charge) that provide real-time metrics of narrative shape. These metrics do not replace emergence. They supplement it. The circuit still produces emergent events. The narrative bus values tell the designer (or a narrative AI) whether the emergent events are forming a coherent story structure.

A designer using the circuit method can author triggers that respond to narrative bus values: introduce a new threat when tension drops below a threshold, trigger a revelation when secret charge peaks, present a moral choice when character arc progress reaches a milestone. The emergent events still happen. The narrative bus metrics enable shaping those events into satisfying story structures.

### 4.4 Utility AI (Dave Mark, "Behavioral Mathematics for Game AI")

The circuit method's AI system is directly descended from Utility AI as described by Dave Mark. Every available action is scored through considerations that map calculated values through curves and ranges. The highest-scoring action executes.

The extension is that the circuit method's considerations read from the same resource values and calculations that everything else reads from. An AI character's decision to fight, flee, negotiate, or eat is scored against the same values that drive narrative tension, economic pressure, and social network dynamics. The AI does not operate in an isolated decision space. It operates on the live circuit state. A character's willingness to fight is literally a function of their courage capacitor charge, their polarity value, their relationship to the attacker, and the substrate's background threat level — all live circuit values.

### 4.5 Tabletop RPG Design (D&D, GURPS, World of Darkness)

The circuit method originated from observing what tabletop RPGs achieve through human arbitration. In a spoken D&D game, a player can use a rope to swing across a chasm, tie up a prisoner, trigger a trap from a distance, bridge a gap, pull a friend up a cliff, or lasso a fleeing enemy. The dungeon master evaluates each proposed use against the rope's physical properties and the situation's requirements. The same rope enables dozens of uses because the DM evaluates pin compatibility in real time.

Video game RPGs restrict items to pre-programmed uses because they lack the DM's flexible evaluation. The circuit method provides the flexible evaluation through pin specifications and bus matching. An item's uses are not listed. They are discovered through the combinatorial space of pin-to-pin connections. The engine evaluates each connection's viability through the same impedance-and-conductance model that a DM intuitively applies.

The character sheet is directly modeled: attributes are bus bandwidth values, skills are conductance values, backgrounds are pre-charged capacitors, and archetypes are routing policies. A player building a character in the circuit method is literally designing a circuit board, choosing which buses to invest in and which paths to build conductance on.

### 4.6 Economy Design (EVE Online, Victoria Series)

Economic simulation games model supply, demand, production, consumption, and market dynamics. The circuit method models these through the same resource conversion and coupling mechanisms used for everything else.

Production is a conversion set that consumes inputs and produces outputs. Market prices are calculations that read supply and demand values. Trade is a conversion set between two entities' economic bus values. Market coupling propagates price signals between connected markets with attenuation and delay. Economic parasitic rules generate social attention from transactions (spending money in poor areas is conspicuous).

The extension beyond traditional economic simulation is that the economy is on the same buses as combat, social dynamics, and narrative. Economic pressure directly affects mood (coupling from economic stress to mood values). Mood affects work output (calculation reading mood as a modifier on production rates). Work output affects economy (production feeding supply). The loop closes through shared bus connections, not through explicit bridge code.

---

## 5 Practical Design Process

### 5.1 Start With Buses

Begin by listing the signal types your game needs. Each signal type is a bus. A fantasy RPG needs mechanical, thermal, optical, acoustic, social, magical, economic, biological, informational, and threat buses. A cyberpunk game adds digital, cybernetic, street, and substance buses. A survival game adds hydration, shelter, weather, and calorie buses.

Each bus is a parent resource group. Its children are the specific signal types on that bus. The mechanical bus has children for strength, agility, force output, weight, and movement speed. The social bus has children for charisma, persuasion, intimidation, reputation, and trust.

### 5.2 Define Components

For each game element (item, creature, building, NPC, environmental feature), list which buses it connects to and what signal it produces or accepts on each bus. A torch connects to optical (light output), thermal (heat output), acoustic (noise output), mechanical (weight), and temporal (burn duration). A locked door connects to mechanical (force threshold), informational (lock complexity), thermal (burn threshold), social (owner permission), and magical (ward strength).

Each connection is a pin. Each pin has a default amplitude and an active condition. The torch's optical pin produces 80 units of light when the torch is lit and 0 when unlit. The door's mechanical pin accepts force above a threshold of 200 (it requires at least 200 force to break down).

### 5.3 Author Actions as Conversion Sets

Each action is a conversion set with requirements (impedance tests) and costs (resource consumption). Lighting a torch requires an ignition source and fuel remaining above zero. The cost is none (lighting is free). The output is that the torch transitions from unlit to lit (a label change), which activates all lit-state pins.

Picking a lock requires lockpicking skill above the lock's complexity, lockpicks in inventory, and sufficient light to see. The cost is time (work hours consumed) and risk (lockpick may break on failure). The output is the door transitions from locked to unlocked.

### 5.4 Add Circuit Elements

After the base components and actions are working, add inductance, coupling, parasitic rules, and oscillation detectors to create dynamic behavior.

Add inductance to any value that should have memory: trust, reputation, mood, faction standing, addiction, cultural tradition. Tune the accumulation rate and maximum energy to control how fast inertia builds and how large the maximum consequence can be.

Add coupling to any value that should spread: reputation changes propagating through faction networks, mood changes spreading through friendships, market prices propagating between trade hubs. Tune the coefficient, hop count, attenuation, noise, and delay to control how the signal propagates.

Add parasitic rules to any zone where activity should produce side effects: combat noise in corridors, economic attention in marketplaces, surveillance in corporate zones. Tune the coefficient and threshold to control when and how strongly the side effect occurs.

Add oscillation detectors to any value that might cycle and where the cycle itself matters: economic boom-bust, mood instability, combat stalemates. The detector provides pattern information that feeds into AI scoring, narrative metrics, and audio modulation.

### 5.5 Test Through the IC Browser

Run the game. Open the IC Browser. Select an entity. See every value on every bus. Click a value. Trace every conversion set, calculation, trigger, label, coupling, and obligation that references it. Watch the signal monitor show real-time value changes. Watch pending coupling propagations moving through the network. Watch oscillation detectors reporting patterns.

Tune parameters live. Change a conductance value and watch the downstream effects immediately. Change a coupling coefficient and watch the propagation pattern change. Change a parasitic rule threshold and watch the side effect activate or deactivate.

The IC Browser is the testing tool, the debugging tool, the tuning tool, and the design verification tool. It shows the circuit's complete state. If the game behaves unexpectedly, the circuit state explains why. If the game behaves as intended, the circuit state confirms the design.

### 5.6 Iterate

The circuit method supports rapid iteration because every parameter is live-editable data. No recompilation. No restart. No scene reload. Change a value, watch the result, adjust, repeat. The feedback loop between design intent and game behavior is one click.

---

## 6 Adoption Path for Industry Designers

### 6.1 Starting From an Existing Game Design

Take an existing game design document. For each game system described (combat, economy, crafting, social, exploration), list the values it tracks and the operations it performs. Each value becomes a resource group. Each operation becomes a conversion set. Each conditional state becomes a label. Each computed value becomes a calculation.

Map the connections between systems. "When health drops below 25%, the NPC becomes desperate and accepts worse trade deals." This is a label (Desperate, triggered at health < 25%), a calculation (trade price modifier reading the Desperate label), and a conversion set (trade operation whose price is modified by the calculation). Three data entries. No bridge code.

### 6.2 Starting From Scratch

Begin with the experience you want the player to have. Work backward to the circuit that produces it. If you want the player to feel the weight of a long relationship being betrayed, you need inductance on trust values. If you want a living social world that responds to the player's choices, you need coupling through the relationship network. If you want the environment to react realistically to the player's actions, you need parasitic rules on zone substrates.

Author the circuit elements that produce the experience. Test through the IC Browser. Tune until the experience matches your intent.

### 6.3 Building Your Own Implementation

The method does not require the Silo Engine specifically. The core concepts can be implemented in any engine.

You need: a universal value store (equivalent to ResourceValue), a universal action model (equivalent to ResourceConversionSet), a universal calculation model (equivalent to ResourceCalculation), a universal state machine (equivalent to ResourceLabel), and the four circuit elements (inductance, coupling, parasitic rules, oscillation detection).

The universal value store requires: a group identifier (integer), a numeric value, minimum and maximum limits, and a timestamp of last change.

The universal action model requires: a list of requirements (value-threshold checks) and a list of costs (value changes). Execution checks all requirements, subtracts all costs, and applies all outputs.

The universal calculation model requires: four stages (base, base scale, modifier, modifier scale) that compose through multiplication and addition to produce a single derived value.

The universal state machine requires: a prioritized list of conditions (conversion set requirements). The first condition that passes writes its label value to a target.

Inductance requires: a monitored value, an energy accumulator that charges during stability, a change detector that fires when the value changes, and a back-EMF computation (energy times delta over delta time).

Coupling requires: a source value, a target value, a connection filter (which entities receive the signal), a coefficient (how much signal propagates), hop parameters (maximum distance, attenuation per hop, delay per hop), and optional noise injection.

Parasitic rules require: a source bus, an emission bus, a coefficient, a threshold, and a zone scope.

Oscillation detection requires: a monitored value, a history buffer, a crossing counter, and event thresholds for onset, resonance, damping, and cessation.

These primitives compose into every game mechanic described in this paper. The implementation cost is authoring the eleven data structures and the evaluation loop. The return is that every game mechanic thereafter is data, not code.

---

## 7 Conclusion

The Circuit System Method of Game Design replaces the traditional architecture of separate game systems connected by explicit bridges with a unified architecture where every game element is a component on shared signal buses. The designer authors components (values, conversions, calculations, labels), connects them through bus pins, and adds circuit dynamics (inductance, coupling, parasitic rules, oscillation detection). The engine evaluates the resulting circuit. Gameplay, narrative, social dynamics, economic behavior, environmental response, and audio expression all emerge from the circuit's operation.

The method is grounded in six domains (Inventory, Quest, Relationship, Character, Narrative, Setting) that map directly to established game design practice. Each domain contributes components to the shared circuit. The four circuit elements extend each domain with dynamic behavior that no existing game achieves: proportional consequences from disrupted stability (inductance), automatic network propagation (coupling), substrate-driven side effects (parasitic rules), and pattern-responsive behavior (oscillation detection).

The method's practical advantage is that cross-system interactions, the most expensive and fragile part of traditional game development, become free. Every bus connects to every other bus. Every value change propagates to every connected value. The designer does not write bridges. The designer designs circuits. The bridges are the bus connections.

The method's creative advantage is that the combinatorial space of possible interactions grows with the number of components and buses, not with the number of authored interactions. A game with 80 items, each with pins on 5 buses, connecting to quest obstacles that accept input from multiple buses, produces thousands of potential solutions that the designer never individually authored. The engine evaluates each one. The designer curates the possibility space by choosing which buses exist, which pins each component has, and what impedances each obstacle presents.

The circuit is the game. The designer is the circuit architect. The engine is the power supply. The player is the current, finding paths through the impedance network that the architect designed. The paths the player finds are the stories the game tells.

---

# Addendum: A Complete Game Design Using the Circuit System Method

## Victorian London — From Setting to Playable System

This addendum demonstrates the Circuit System Method applied from a single starting point: a setting. We begin with "Victorian era London" and derive every other domain — inventory, quests, relationships, characters, narrative, and the circuit dynamics that connect them — from the setting's substrate properties. Nothing is pre-decided except the place and time. Everything else follows from asking what signals the setting generates, what impedances it presents, and what circuits the player can build on its substrate.

---

## 1 The Substrate

Victorian London is the circuit board. Its properties determine what every component can do.

### 1.1 Substrate Properties

| Property | Value | What It Determines |
|----------|-------|--------------------|
| AmbientLight | 25 | Gas lamps in wealthy areas, darkness elsewhere. Fog reduces effective light further. Optical bus operates at deficit most of the time. |
| AmbientTemperature | 45 | Cold, damp. Biological bus drain on exposure. Coal is the thermal energy source. |
| AcousticEcho | 140 | Dense brick and stone. Footsteps carry. Conversations in alleys are overheard. Gunshots echo across neighborhoods. |
| BiologicalSupply | 55 | Food available but quality varies by class. Clean water is not guaranteed. Disease is a standing biological drain. |
| BackgroundThreat | 35 | Moderate. Street crime is real but not constant. Threat rises sharply at night and in specific zones. |
| SocialRigidity | 85 | High. Class boundaries are nearly impermeable. Social bus impedance between strata is enormous. A working-class character cannot speak to an aristocrat without a social impedance matcher (proper dress, letter of introduction, intermediary). |
| TechLevel | 40 | Early industrial. Steam, gas, clockwork, early chemistry. No electricity in homes. Telegraph exists but is institutional. |
| MagicLevel | 0 | No magic bus on this substrate. Spiritualism and mesmerism exist as social phenomena (social bus signals with no magical bus backing). |
| LawEnforcement | 50 | Metropolitan Police exist but are unevenly distributed. High in wealthy areas, low in slums. Corruption available as a social bypass. |
| EconomicDevelopment | 70 | Active economy. Multiple currencies of exchange: money, favors, secrets, reputation. The economic bus carries all four. |
| InformationBandwidth | 30 | Newspapers, pamphlets, word of mouth. No telephone. No radio. Information travels at the speed of print and foot. |
| ResourceScarcity | Label: Reputation | Reputation is the scarce resource. Money can be earned. Skills can be learned. But reputation, once lost, is nearly impossible to recover. The social rigidity of the substrate makes reputation the gating resource for every significant action. |
### 1.2 Zone Variation

Victorian London is not one substrate. It is a gradient, like urban decay but with sharper boundaries.

```

ZONE: Mayfair / Belgravia (Aristocratic)

  AmbientLight: 60 (gas lamps maintained, well-lit streets)

  BackgroundThreat: 10 (private security, police presence)

  SocialRigidity: 95 (the highest social impedance in the city)

  LawEnforcement: 85 (rapid response, magistrates available)

  Parasitic rules:

SocialBus activity → ReputationObservation (2.0 $\times$  coefficient)

(everything you do is watched and reported by servants, neighbors, club members)

EconomicBus activity → SocialStatusSignal (1.5 $\times$ )

(spending patterns signal class membership — spending too little or too much is noted)

ZONE: The City (Financial District)

  AmbientLight: 45 (business hours only, dark after closing)

  BackgroundThreat: 20 (daytime low, nighttime moderate)

  SocialRigidity: 70 (class matters less than money here)

  EconomicDevelopment: 95 (the highest economic activity in the city)

  Parasitic rules:

EconomicBus activity → InformationBus emission (2.5 $\times$ )

(every financial transaction generates intelligence — who is buying what, who is selling)

InformationalBus activity → EconomicBus emission (1.0 $\times$ )

(information has direct cash value in the City)

ZONE: East End (Working Class / Slums)

  AmbientLight: 10 (no gas in many streets, fog-prone)

  BackgroundThreat: 65 (high crime, gangs, desperation)

  SocialRigidity: 30 (class barriers are low within the zone — solidarity replaces hierarchy)

  LawEnforcement: 15 (police avoid the worst areas)

  BiologicalSupply: 30 (food scarce, water contaminated, disease endemic)

  Parasitic rules:

BiologicalBus activity → DiseaseExposure (2.0 $\times$ )

(any biological activity in this zone carries disease risk)

SocialBus activity → GossipSignal (3.0 $\times$  with high noise)

(the East End talks, but the information distorts rapidly)

ThreatBus activity → GangAttention (1.5 $\times$ )

(violence attracts gang interest — protection or predation)

ZONE: Docklands (Liminal / Trade)

  AmbientLight: 20 (waterfront fog, warehouse shadows)

  BackgroundThreat: 50 (smuggling, press gangs, foreign sailors)

  SocialRigidity: 40 (the docks erase some class distinctions through shared labor)

  EconomicDevelopment: 60 (trade economy, barter alongside currency)

  Parasitic rules:

EconomicBus activity → SmuggleOpportunity (2.0 $\times$ )

(every trade signals what is moving and what might be diverted)

MechanicalBus activity → SailorNotice (1.0 $\times$ )

(physical capability is noted — strong workers are recruited or press-ganged)

ZONE: Whitechapel (Danger Zone)

  AmbientLight: 5 (near-total darkness in alleys, fog + smoke + no lamps)

  BackgroundThreat: 80 (extreme danger, especially at night)

  BiologicalSupply: 15 (cholera territory, food adulteration common)

  LawEnforcement: 5 (police enter in groups, rarely after dark)

  SocialRigidity: 10 (survival erases all social distinction)

  Parasitic rules:

All bus activity → ThreatAttention (3.0 $\times$ )

(any activity in Whitechapel attracts dangerous attention)

OpticalBus activity → VulnerabilitySignal (2.5 $\times$ )

(carrying a light source in Whitechapel makes you a target, not safe)

```

### 1.3 What the Substrate Tells Us

The substrate properties generate the game's themes before we author a single quest or character.

Social rigidity at 85 means the central impedance in the game is class. Moving between social strata is the hardest thing in this world. The game's core challenge is navigating a high-impedance social circuit.

Reputation as the scarce resource means the game's core currency is not money. It is standing. Every action the player takes charges or discharges their reputation capacitor. Reputation has high inductance on this substrate (Victorian social norms are deeply established, generational, institutional). Building reputation is slow. Losing reputation is fast. The asymmetry is approximately 5:1 — one scandal undoes five years of careful social climbing.

Low information bandwidth means secrets are powerful. Information travels slowly. A secret known in the East End takes days to reach Mayfair, if it reaches at all. The coupling attenuation between zones is high. This makes the Information Bus the player's primary tool for cross-zone power — the player who controls information flow controls the game.

The fog is a substrate-level optical bus modifier. It reduces ambient light by a variable amount each day, modifying every optical-dependent calculation. Perception checks, surveillance, signaling, reading, and navigation all degrade in fog. Fog is not weather. Fog is a variable impedance on the optical bus that changes the effective conductance of every optical circuit in the city.

---

## 2 The Characters

The substrate tells us what characters this world produces. High social rigidity means characters are defined by their class position. The character layer system maps directly.

### 2.1 The Player Character: A Middle-Class Professional

The player character occupies the most interesting position on the social gradient: the middle class. Below are the laboring poor with no social bus access to the upper zones. Above are the aristocracy with no economic need. The middle class has just enough social bus conductance to interact with both extremes, and just enough economic pressure to need to.

```

Layer 1 — Body: Human, male or female (gender is a bus modifier on this substrate —

  women have reduced social bus bandwidth in formal contexts, increased in domestic contexts)

Layer 3 — Attributes:

  Strength: 10 (average)

  Agility: 12 (above average, navigates the city well)

  Constitution: 11 (adequate but vulnerable to disease)

  Intelligence: 15 (high — the player character's primary attribute)

  Perception: 14 (observant — notices details others miss)

  Charisma: 13 (socially capable across class boundaries)

  Will: 13 (resistant to temptation and coercion)

  Empathy: 12 (can read social signals across class)

Layer 4 — Skills:

  Investigation: 75 (primary skill — the character investigates)

  Persuasion: 60 (can convince across class with effort)

  Deception: 45 (can lie but not naturally — honesty parameter conflicts)

  Etiquette: 55 (knows upper-class protocols but not fluently)

  Streetwise: 50 (knows the lower-class world from professional exposure)

  Medicine: 40 (basic knowledge, enough to recognize poison and disease)

  Law: 65 (knows the legal system well enough to navigate it)

  Observation: 70 (notices physical details — footprints, stains, inconsistencies)

Layer 5 — Personality:

  Aggression: 25 (low — prefers intellect over force)

  Caution: 65 (moderately cautious — assesses before acting)

  Empathy: 60 (cares about people, which creates moral gate pressure)

  Curiosity: 85 (very high — the primary drive current)

  Loyalty: 55 (moderate — can be pulled between competing loyalties)

  Honesty: 70 (high — makes deception costly in sanity)

  Ambition: 50 (moderate — not driven by power but by truth)

  Discipline: 60 (maintains focus under pressure)

  Paranoia: 40 (moderate — trusting enough to form relationships, wary enough to suspect)

Layer 6 — Background:

  Origin: Middle-class professional (journalist, physician, solicitor, or inspector)

  Formative event: Witnessed an injustice that the establishment covered up.

Guilt capacitor: 30 (feels responsible for not acting sooner)

Trust toward institutions: -40 (the cover-up damaged faith in authority)

Curiosity drive: amplified (the formative event created the investigation compulsion)

  Pre-existing relationships:

Editor/Employer: moderate trust (+200), obligation diode (employer → character: salary)

Contact in the East End: low trust (+80), high information value

Contact in the City: low trust (+100), economic information access

Family member: high trust (+400), high inductance (family bonds are deep on this substrate)

Layer 7 — Archetype:

  Primary: Seeker (routes through investigation and discovery paths)

  Secondary: Scholar (routes through knowledge and analysis paths)

```

### 2.2 Supporting Cast Generated by Substrate

The substrate's zone gradient produces distinct character types at each position.

**The Aristocrat (Mayfair):** Social bus bandwidth at maximum. Economic bus at surplus. No survival pressure. All capacity available for social maneuvering, political influence, and reputation management. High inductance on all values (generational stability). High coupling coefficient within the aristocratic network (tight social mesh). Very low coupling to other zones (class boundary acts as impedance wall).

The aristocrat is difficult to access (high social impedance) and dangerous to cross (high inductance means disruption produces massive back-EMF through the aristocratic coupling network). The player must impedance-match (proper dress, credentials, intermediary) to even begin a social interaction.

**The Factory Owner (The City):** Economic bus bandwidth at maximum. Social bus moderate (money buys access but not acceptance). The factory owner converts economic bus power into social bus access — a transformer. The player can reach the factory owner through the economic bus (business proposition) or the social bus (club introduction), each path with different impedance.

**The Street Urchin (East End):** Information bus bandwidth at maximum within the zone. Social bus bandwidth at zero outside the zone. Biological bus at deficit (hungry, cold, at risk). The urchin is the information relay: they see everything in the East End but cannot carry that information to Mayfair directly. The player is the bridge node that connects the urchin's information to the aristocrat's social network. The player's value is being the coupling path between disconnected zones.

**The Inspector (Scotland Yard):** Moderate capability across multiple buses. Access to the legal system (a unique bus that only law enforcement connects to). The inspector is simultaneously an ally (shares information, provides legal protection) and a constraint (the player's actions that cross legal boundaries risk triggering the inspector's threat sensors). The relationship with the inspector has high inductance: if trust is built through cooperation, disrupting that trust through illegal action produces proportional back-EMF (arrest, investigation, loss of legal protection).

**The Criminal Boss (Docklands/East End):** High threat bus output. High economic bus within the underground economy. Social coupling to a network of criminals, informants, and corrupt officials. The criminal boss operates a parallel power structure. The player can access this structure but at cost: every interaction with the criminal boss deposits reputation damage through the parasitic rule on the East End zone (association with criminals is noted).

**The Servant (Cross-zone):** Physically present in Mayfair but socially positioned below stairs. The servant sees everything the aristocrats do (high information intake) but has near-zero social bus output in formal contexts. The servant is an information source with a trust gate: the servant will share information only if trust is built through the low-class social bus (kindness, payment, protection), not through the high-class social bus (authority, command, threat). The social bus impedance mismatch between the player (middle class) and the servant (working class) is lower than the mismatch between the aristocrat and the player. The player can reach the servant more easily than the aristocrat can, which is the player's structural advantage.

---

## 3 The Inventory

The substrate determines which items exist and what pins they have.

### 3.1 Investigation Tools

**Magnifying Glass:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| DetailEnhancement | Optical | Output | +30 perception for fine detail | Requires ambient light above 15 to function |
| SocialSignal | Social | Output | +10 credibility as investigator | Visible item broadcasts professional identity |
**Notebook and Pencil:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| InformationCapture | Informational | Input/Output | Records observations as information capacitor charges | Each observation charges the notebook. Full notebook is evidence. |
| SocialSignal | Social | Output | +5 journalist identity | Visible item broadcasts "press" — opens some doors, closes others |
**Calling Card Case:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| SocialAccessToken | Social | Output | +25 social impedance reduction in formal contexts | Required for Mayfair zone entry without suspicion |
| IdentityBroadcast | Identity | Output | States name, profession, address | The card IS the identity on this substrate |
**Lockpick Set:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| MechanicalAccess | Mechanical | Output | Skill-dependent conductance through locked barriers | Possession is criminal — parasitic rule: if detected, LegalThreat +50 |
| NoiseOutput | Acoustic | Output (parasitic) | 15 per attempt | Stone buildings amplify (echo multiplier 1.4 $\times$ ) |
**Laudanum Vial:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| PainSuppression | Biological | Output | +30 HP recovery short term | Single discharge capacitor |
| AddictionRisk | Biological | Output (parasitic) | +5 addiction per use | Addiction inductance accumulates — withdrawal back-EMF scales with use count |
| SedativeWeapon | Chemical | Output | Can incapacitate a target in food/drink | Social bus must deliver it (deception or hospitality) |
| SocialStigma | Social | Output (parasitic) | -10 reputation if use is observed in formal context | The upper class uses laudanum privately, never publicly |
**Newspaper (Today's Edition):**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| InformationSource | Informational | Output | Charges information capacitor with current events | Specific stories are resource values; reading the paper reveals them |
| SocialCurrency | Social | Output | Discussing current events is a social lubricant (+5 to conversation openings) | The paper is a social impedance reducer for strangers |
| ReputationAmplifier | Social | Output (conditional) | If the player's actions appear in the paper, reputation change is multiplied by readership coupling | The newspaper IS a coupling amplifier — it broadcasts through the information network at print speed |
### 3.2 Social Tools

**Letter of Introduction:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| SocialGateKey | Social | Output | Opens specific high-impedance social gates | Each letter is a single-use key for one person or institution. The letter is an amplifier: input = paper, energy source = the writer's reputation. |
| TrustTransfer | Social | Output | Transfers a fraction of the writer's trust to the bearer | Coupling from writer's reputation to bearer's access. If the bearer dishonors the letter, back-EMF hits the writer's reputation through the coupling. |
**Gentleman's Attire:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| SocialImpedanceMatch | Social | Output | Reduces Mayfair social impedance by 40 | Without this, social conductance in Mayfair is near zero |
| ClassSignal | Identity | Output | Broadcasts "gentleman" class identity | NPCs in Mayfair accept the signal. NPCs in the East End are suspicious. |
| VulnerabilityIncrease | Threat | Output (parasitic) | +15 robbery target value in East End zones | Fine clothes in poor areas make you a target |
**Working-Class Cap and Coat:**

| Pin | Bus | Direction | Amplitude | Notes |
|-----|-----|-----------|-----------|-------|
| SocialImpedanceMatch | Social | Output | Reduces East End social impedance by 30 | Without this, social conductance in the East End is reduced (outsider detection) |
| ClassSignal | Identity | Output | Broadcasts "working class" identity | NPCs in the East End accept. NPCs in Mayfair do not. |
| StealhBonus | Threat | Output | -20 visibility in East End zones | You blend in. Parasitic observation rules do not fire for class-appropriate clothing. |
The player must change clothes when crossing zones. Gentleman's attire in the East End is a vulnerability amplifier. Working-class clothing in Mayfair triggers the social parasitic rule (someone of lower class observed in an upper-class area generates a suspicious attention signal). The clothing is a bus impedance matcher that must be swapped at zone boundaries.

---

## 4 The Quest: The Thornfield Investigation

### 4.1 Quest Source

A young woman from a respectable middle-class family is found dead in a Whitechapel alley. The police rule it suicide. The family does not believe it. They hire the player to investigate.

```

Quest Source: Patron (Family)

  NEED_OUT: Determine the true cause of death

  REWARD_OUT: 50 pounds + family gratitude (trust capacitor charge)

  INFO_OUT: Victim's name, last known movements, the police report

  TRUST_BIAS: High (family is honest, desperate, and grieving)

  DEADLINE_OUT: None explicit, but the family's resources are finite

(economic bus drain: the family pays the player's expenses ongoing)

```

### 4.2 Information Phase

The quest begins as a pure information circuit. The player must charge information capacitors from multiple sources, each with different impedance.

**Source 1: The Police Report (Scotland Yard)**

| Access Path | Impedance | Conductance Required | Parasitic |
|-------------|-----------|---------------------|-----------|
| Social: formal request through official channels | Medium (bureaucratic delay, 3 days) | Etiquette 40+, Law 50+ | None — legitimate request |
| Social: personal contact with Inspector | Low (if trust > 150 with the Inspector) | None beyond trust threshold | If Inspector discovers the player later acts outside the law, trust back-EMF is amplified by the favor |
| Deception: impersonate a solicitor | Medium (requires forged credentials) | Deception 60+, Forgery skill, Gentleman's attire | If detected: LegalThreat +80, Inspector trust -300, reputation in legal community damaged through coupling |
| Economic: bribe a clerk | Low impedance, high parasitic | Money (5 pounds), Streetwise 30+ | Bribe generates gossip through the Yard's internal coupling network. The clerk may sell the information of the bribe to someone else. |
Each path produces the same information (the police report) but with different costs, different time delays, and different parasitic emissions. The player's choice of path is the first circuit design decision of the quest.

**Source 2: The Victim's Workplace (A Textile Factory in the East End)**

| Access Path | Impedance | Conductance Required | Parasitic |
|-------------|-----------|---------------------|-----------|
| Social: ask the foreman directly | High (foreman is suspicious of outsiders, loyalty to factory owner) | Persuasion 65+ OR Intimidation 60+ OR factory owner's authorization | Intimidation generates ThreatAttention in the East End zone (parasitic 1.5 $\times$ ). Other workers notice. |
| Social: befriend a worker | Low impedance but slow (requires building trust over multiple visits) | Empathy 50+, working-class clothing, patience (3-5 visits) | Each visit charges trust capacitor on the worker. Inductance builds. The relationship has value beyond this quest. |
| Economic: pay a worker to talk | Low impedance, fast | Money (2 shillings — small but meaningful to a worker) | Generates gossip in the factory. The foreman hears within 24 hours (coupling delay through the factory social network). |
| Mechanical: break in after hours | Very high risk, very high information yield (access to factory records) | Lockpicking 55+, Stealth 60+ | Acoustic parasitic (echo 1.4 $\times$  in the brick building). If detected: LegalThreat +60, factory owner becomes adversary. Night patrol has 30% detection chance per 10 minutes. |
**Source 3: The Docklands Contact (A Sailor Who Knew the Victim)**

The player's pre-existing contact in the East End knows a sailor who courted the victim. The contact is the coupling path between the player and the sailor.

| Access Path | Impedance | Conductance Required | Parasitic |
|-------------|-----------|---------------------|-----------|
| Through the contact (social coupling) | Low impedance but requires contact trust > 100 | Contact.TrustLevel >= 100 | The contact's trust toward the player is the gate. If the contact's trust is below threshold, the contact refuses (impedance too high). |
| Direct approach at the docks | High (the sailor is suspicious of strangers, especially middle-class ones) | Streetwise 60+, working-class clothing, knowledge of dockland protocols | SailorNotice parasitic fires: the player is assessed for physical capability. Low Strength (<12) reduces social conductance with dock workers. |
### 4.3 The Information Lock

The information gathered from all three sources (plus additional sources the player discovers) charges the quest's information capacitor. The quest has an information lock with multiple partial keys:

```

Information Lock: True Cause of Death

  Threshold: 5 clues (of 8 available)

  Clue 1: Police report mentions bruising inconsistent with suicide (Source 1)

  Clue 2: Factory records show victim was promoted recently, contradicting "depression" narrative (Source 2, break-in only)

  Clue 3: Worker testimony: victim was frightened of someone at the factory (Source 2, befriend or bribe)

  Clue 4: Sailor testimony: victim said she "knew something dangerous" (Source 3)

  Clue 5: Landlady testimony: a well-dressed man visited victim's lodgings the night before death (Source 4: landlady in Whitechapel)

  Clue 6: Medical re-examination: poison traces, not visible in standard autopsy (Source 5: private physician, requires Medicine 50+ to interpret)

  Clue 7: Financial records: factory owner made a large payment to an unknown party the day after the death (Source 6: City contact, requires economic bus access)

  Clue 8: Servant testimony from factory owner's household: heard the owner arguing about "the girl who knew" (Source 7: servant, requires building trust with the servant class)

```

Five of eight clues unlock the information lock. The player does not need all clues. Different combinations produce different pictures. Clues 1+3+4+5+6 prove murder by the factory owner (poisoning to silence a witness). Clues 1+2+4+7+8 prove murder motivated by factory secrets (the victim discovered something). The player's investigation path determines not just WHETHER they solve the case but WHAT they understand about it.

### 4.4 The Moral Gate

Once the information lock opens, the player faces a moral gate with three paths:

**Path A: Take the evidence to Scotland Yard.**

The legal path. The Inspector receives the evidence. The factory owner is arrested. Justice is served through institutions.

Requirements: Inspector trust > 200 (the Inspector trusts the player's evidence), evidence quality > 70 (enough clues, properly documented in the notebook).

Costs: Time (trial takes weeks). Risk of the factory owner's connections interfering (the factory owner is coupled to political figures through the City economic network). The player's reputation gain is moderate (+100 in the legal community, +50 general).

Consequences: The factory owner's arrest propagates through the economic coupling network. His business associates recalculate their positions. Workers at the factory lose employment (biological bus impact on the East End). The family is satisfied (patron trust maxes out). The political figures connected to the factory owner may become adversaries (coupling delivers negative reputation delta to the player through the political network, with delay).

**Path B: Publish the evidence in the newspaper.**

The public path. The player's editor publishes the story. The court of public opinion convicts the factory owner.

Requirements: Editor trust > 150 (the editor trusts the story's accuracy), evidence quality > 50 (lower threshold — newspapers trade in sensation, not proof).

Costs: The story amplifies through the newspaper's coupling network at maximum bandwidth. The factory owner's reputation is destroyed instantly (the newspaper IS a coupling amplifier with very high coefficient, zero attenuation, and near-zero delay). The player's reputation increases massively (+300 general, but variable by zone — the East End cheers, Mayfair is uncomfortable with the spectacle).

Consequences: The factory owner's political allies must publicly distance themselves (coupling back-EMF from the owner's destroyed reputation). The political network shifts. The player becomes a public figure (MediaExposure charges permanently). Future investigations are harder because targets know the player will publish (social impedance increases for future investigation interactions). The family is partially satisfied (the truth is out, but legal justice may not follow).

**Path C: Confront the factory owner privately.**

The direct path. The player presents the evidence to the factory owner and demands something: money, confession, change in factory conditions, freedom for the workers.

Requirements: Evidence quality > 60, Courage > 40 (private confrontation with a murderer).

Costs: Physical risk (the factory owner may resort to violence). The evidence stays private (no reputation gain). The player is now bound to the factory owner through a secret obligation diode (the factory owner owes the player's silence, the player owes continued silence).

Consequences: The factory owner complies (money, confession, or reforms) but the murder is not publicly resolved. The family does not get full closure. The player gains a powerful but dangerous connection. The secret of the confrontation is a charged capacitor that can discharge at any time if either party breaks the implicit agreement. The longer the secret is held, the more charge it accumulates. If it eventually surfaces, the back-EMF from the inductance (months or years of secret-keeping) produces consequences proportional to the duration.

### 4.5 Quest Resolution and Sequel Generation

Each path resolves the quest and generates sequel conditions:

Path A generates: political enemies from the factory owner's network (new threat sources), potential corruption investigation (the political figures who protected the factory owner may be exposed by the trial), and career advancement for the Inspector (relationship deepens, opening higher-trust quest access).

Path B generates: media attention (the player is now a public investigator, which changes all future social bus interactions — some doors open, others close), editorial pressure for the next story (obligation diode from editor: success creates expectation of continued success), and potential libel action from the factory owner's allies (legal threat from the economic/political network).

Path C generates: a secret capacitor charging indefinitely, an obligation network between the player and the factory owner, and a moral weight on the player's character (the empathy personality parameter creates internal conflict: the player knows a murderer walks free).

---

## 5 The Relationship Network

### 5.1 Active Relationships

The quest generates relationship branches with inductance and coupling configurations specific to this setting.

**Player → Inspector Harrison**

```

ResourceInstance: InspectorRelationship

  values:

TrustLevel: +200 (built through cooperation)

RespectLevel: +150 (the Inspector respects competence)

ObligationCharge: -50 (the Inspector provided the police report as a favor)

ConnectionType: ProfessionalAlly (value 61)

  inductances:

TrustLevel:

  accumulation_rate: 150 (1.5 $\times$  — professional trust builds moderately fast)

  max_energy: 8000

  change_threshold: 30

  back_emf_resource_event_id: InspectorBetrayalEvent

  resist_change: true

  // If the player is caught breaking the law, the trust drop encounters

  // resistance from the accumulated professional relationship.

  // A small infraction: the inductance partially absorbs it (the Inspector gives benefit of doubt).

  // A large infraction: the inductance cannot absorb it, back-EMF fires,

  // the Inspector feels personally betrayed (proportional to how long trust was stable).

  couplings:

TrustLevel → ScotlandYardAccess:

  connection: ProfessionalAlly

  coefficient: 60 (0.60 — Inspector's trust opens Yard doors)

  max_hops: 1 (direct access only, not through the Inspector's colleagues)

  delay: 3600 (1 hour — the Inspector can arrange access within an hour)

TrustLevel → LegalProtection:

  connection: ProfessionalAlly

  coefficient: 40 (0.40 — some trust translates to some legal cover)

  // If the player is in legal trouble, the Inspector's trust partially shields them

  // But only partially — the coupling coefficient is 0.40, not 1.0

```

**Player → Martha (The Servant)**

```

ResourceInstance: ServantRelationship

  values:

TrustLevel: +80 (initial, from kindness during investigation)

RespectLevel: +50 (the servant is not accustomed to respect from the middle class)

AffectionLevel: +30 (the player treated her as a person, not a function)

ConnectionType: Informant (value 62)

  inductances:

TrustLevel:

  accumulation_rate: 200 (2.0 $\times$  — trust from a class above builds fast because it is rare)

  max_energy: 15000 (very high — cross-class trust, once established, is deeply valued)

  change_threshold: 20

  // Martha has been conditioned to distrust the upper classes.

  // Trust that overcomes this conditioning builds very fast

  // (the accumulation rate is high because the trust is precious to her).

  // Betrayal of this trust produces enormous back-EMF

  // (proportional to how rare and precious the trust was).

  couplings:

TrustLevel → ServantNetworkInformation:

  connection: ServantClass

  coefficient: 80 (0.80 — servants talk to each other freely)

  max_hops: 3 (servants in adjacent households, their contacts, and their contacts)

  hop_attenuation: 60 (0.60 — moderate attenuation, servants are reliable reporters)

  noise_amplitude: 10 (0.10 — low noise, servants value accuracy)

  delay: 43200 (12 hours — servant gossip travels at the pace of household visits)

  // Martha's trust in the player propagates through the servant network.

  // Other servants hear that Martha trusts the player.

  // The player gains access to servant-class information across multiple households.

  // This is the most powerful information network in the game:

  // servants see everything the aristocrats do.

  // Access to this network is gated by cross-class trust

  // which is gated by empathy, kindness, and consistent behavior.

```

### 5.2 The Reputation Circuit

The player's reputation is not a single number. It is a distributed capacitor charged across every relationship instance in the network. The player's "reputation" at any moment is the sum of all trust, respect, and reputation values across all connected entities, weighted by each entity's social coupling coefficient.

In Mayfair, the player's reputation is dominated by aristocratic observers (high coupling within the aristocratic network, which amplifies or attenuates the player's standing). In the East End, the player's reputation is dominated by working-class contacts (different coupling network, different values, different amplification).

The player can have a high reputation in the East End and a low reputation in Mayfair simultaneously. The two networks are weakly coupled (the social rigidity of the substrate blocks cross-class coupling). An action that boosts East End reputation (defending a worker's rights) may reduce Mayfair reputation (challenging the social order) or have no effect (the coupling coefficient between networks is near zero for most events).

Only a few events couple across networks: newspaper publication (the newspaper reaches all zones), a public trial (institutional event visible to all), or a scandal (gossip about the player that propagates through both networks simultaneously, but with different noise and different spin).

---

## 6 The Narrative Circuit

### 6.1 Secret Capacitors

The Thornfield investigation generates multiple secret capacitors:

| Secret | Holder | Charge Rate | Discharge Trigger | Impact |
|--------|--------|------------|-------------------|--------|
| The murder (who killed the victim) | Player (once investigated) | Charges with each clue gathered | Player reveals to police, newspaper, or factory owner | All downstream moral gate consequences |
| The factory's illegal practices | Victim (deceased) → Player (inherited through investigation) | Charges with each factory clue | Public exposure or private leverage | Economic coupling cascade through factory network |
| The political protection | Factory owner → political figures | Charges throughout the game as the player uncovers connections | Trial testimony or newspaper publication | Political network reconfiguration, possible sequel investigations |
| The private confrontation | Player + factory owner (if Path C taken) | Charges every day the secret is held | Either party breaks silence, or a third party discovers | Back-EMF proportional to concealment duration  $\times$  secrecy value |
### 6.2 Tension Voltage

Tension voltage at any point is computed as: desire current (player's investigation drive, measured by Curiosity parameter  $\times$  quest active status  $\times$  evidence quality) times obstruction impedance (the highest-impedance unsolved clue the player is currently pursuing).

Early in the quest, when clues are accessible and impedances are moderate, tension is moderate. When the player hits a high-impedance clue (the factory records behind a locked door at night, the aristocrat who won't speak to the middle class, the servant who doesn't trust outsiders), tension peaks. When a clue is obtained, tension drops momentarily before the next impedance raises it again.

The IC Browser would show this as a live value, oscillating with each clue gained and each new impedance encountered. The designer tunes the quest by adjusting clue impedances: making them higher increases tension, making them lower decreases tension.

### 6.3 Thematic Weight

The quest's theme is **class and power: who is protected and who is expendable.** Every quest event either reinforces or challenges this theme. The thematic weight value increments when:

- A clue reveals that the factory owner is protected by political connections (class protects the powerful)

- The police ruled the death a suicide without thorough investigation (the victim's class made her expendable)

- The servant provides crucial testimony but fears retaliation from her employer (class constrains even witnesses)

- The player must change clothes to cross zone boundaries (class is physically encoded in the world)

The thematic weight is a live value that the narrative AI or designer-authored triggers can read. When thematic weight reaches a threshold, the game introduces a parallel case: another working-class death, another cover-up, demonstrating that the Thornfield case is not unique — it is systemic. This is not a scripted sequel trigger. It is a thematic-weight-gated conversion set that creates a new quest source when the theme has been sufficiently established.

### 6.4 Character Arc Tracking

The player character's arc is tracked as the cumulative change in personality parameters from their starting values. The investigation pushes the player's Empathy higher (exposure to suffering in the East End), Paranoia higher (discovering institutional corruption), and Honesty into tension (the Path C option rewards secrecy, which conflicts with the Honesty parameter).

The arc progress is a ResourceCalculation: sum of absolute deltas between current personality values and starting personality values. At arc milestones (progress = 10, 20, 30), the character's internal monologue changes (a ResourceLabel on arc progress writes to an InternalState group, which the dialogue system reads for self-reflective lines).

---

## 7 The Complete Circuit Running Live

A player is attached. The game is running. Here is one evening's session traced through all six domains.

### 7.1 The Session

The player has gathered three clues. They need two more. Tonight they plan to visit the factory after dark to access the records (Clue 2).

**6:00 PM — Preparation (Inventory + Character + Setting)**

The player equips working-class clothing (SocialImpedanceMatch for East End, StealthBonus -20 visibility). They carry lockpicks (MechanicalAccess for the factory door), a dark lantern (Optical output with a shutter — controllable light, StealthPenalty only when open), and the notebook (InformationCapture for the records).

The dark lantern is a critical component. Unlike the torch from the earlier specification, the dark lantern has a shutter pin: SHUTTER_CTRL accepts a binary mechanical input (open/close). When closed, OpticalOutput = 0 and StealthPenalty = 0. When open, OpticalOutput = 40 and StealthPenalty = 30. The player controls the optical bus emission by toggling the shutter.

**Circuit state at preparation:**

```

Player StealthValue:

  Base: Stealth skill 60

  BaseScale: Agility 12/20 = 0.60

  Modifier: WorkingClassClothing -20 visibility bonus

        DarkLantern shutter CLOSED: 0 penalty

        Lockpicks: 0 penalty (concealed)

  Result: (60  $\times$  0.60) + (-20) = 36 + (-20) = 16 (marginal stealth in darkness)

  BUT: the factory zone at night has AmbientLight = 5 and BackgroundThreat = 45.

  The substrate modifies the calculation:

Low ambient light = high stealth modifier (darkness helps hiding)

Effective stealth = 16 + 25 (darkness bonus) = 41 (adequate for the approach)

```

**7:30 PM — Approach (Setting + Threat)**

The player walks from their lodgings to the factory. The zone transitions from Middle-Class Residential (low threat, moderate light) through Working-Class Streets (moderate threat, low light) to the Factory District (moderate threat, very low light).

Each zone transition activates different parasitic rules. In the Working-Class

