# Shoot, Solve, Watch
## Three Verbs That Compose Every Game

**Registry:** [@HOWL-GAME-5-2026]

**Series Path:** [@HOWL-GAME-1-2026] → [@HOWL-GAME-5-2026]

**Date:** November 2026

**DOI:** 10.5281/zenodo.24237953

**Domain:** Interaction Taxonomy / Game Design Theory

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6. 

---

## Abstract

Every game asks the player to do one of three things: shoot, solve, or watch. These are the three primitive interaction verbs. Shoot is motor — the player's body acts on the game state in real time. Solve is cognitive — the player's mind reasons about the game state and selects a transformation. Watch is systemic — the player shapes conditions and observes autonomous agents respond. Every game ever made is a composition of one, two, or all three of these verbs. This paper defines each verb, examines its pure form, maps the hybrid compositions across the history of games, identifies the structural constraints each verb imposes on design, and examines how games break when they violate their own verb contract.

---

## 1. The Three Verbs

### 1.1 Shoot

The player acts on the game state in real time through physical input. The player's reflexes, timing, and spatial positioning determine the outcome. The game state changes because the player's body moved correctly. The feedback loop is immediate: input, state change, visual feedback, next input. The skill is motor.

Shoot is the oldest verb in games. Pong (1972) is Shoot — the player positions a paddle through physical input to intercept a ball. The skill is reaction time and spatial prediction. Every subsequent action game, from Space Invaders through Call of Duty through Beat Saber, is a refinement of the same verb: the player aims (or positions, or times) and the game measures how well the body performed.

The defining characteristic of Shoot is that the player's motor performance is the variable that determines the outcome. Two players facing the same game state produce different outcomes because their hands moved differently, not because their minds reasoned differently.

### 1.2 Solve

The player reasons about the game state and selects a transformation. The game state changes because the player identified the correct operation from a set of possible operations. Time pressure may exist, but the skill being tested is cognitive, not motor. The feedback loop is deferred: observe state, reason, select action, observe result. The skill is analytical.

Solve is the verb of puzzles, strategy, and navigation. Zork (1980) is Solve — the player reads a text description, reasons about what action to take, and types a command. Chess is Solve — two players reason about a shared state space with perfect information. Civilization is Solve — the player optimizes across interconnected systems over hundreds of turns. Death Stranding is Solve — every delivery is a logistics planning problem where route selection, weight distribution, and stamina management determine success.

The defining characteristic of Solve is that the player's reasoning is the variable that determines the outcome. Two players facing the same game state produce different outcomes because their minds identified different possibilities, not because their hands moved differently.

### 1.3 Watch

The player shapes conditions and observes autonomous agents act within those conditions. The game state changes because the agents responded to the environment the player built. The player does not act on agents directly and does not solve a puzzle with a single correct answer. The feedback loop is indirect: shape conditions, agents act, observe emergent behavior, adjust conditions. The skill is systemic.

Watch is the youngest verb and the least understood. Little Computer People (1985) is Watch — a person lives in a house, the player delivers food and books, and the person responds autonomously. The Sims is Watch — virtual people with needs and personalities act on their own within a household the player designed. Dwarf Fortress is Watch — 200 dwarves with deep personality live in a fortress the player designated, and the stories emerge from the simulation without authorship.

The defining characteristic of Watch is that autonomous agent behavior is the variable that produces the outcome. The player influenced the conditions but did not determine the specific behavior. Two players who built identical conditions may observe different emergent outcomes because the agents' internal states interacted differently.

---

## 2. Pure Forms

### 2.1 Pure Shoot

**Asteroids (1979).** Rotate, thrust, fire. Every frame, the player's thumbs determine whether the ship lives. No hidden state to reason about. No agents to observe. The asteroid field is the game and the thumbs are the answer.

**Doom (1993).** Navigate corridors, aim at demons, fire. The maze adds spatial memory, but the core loop is: see enemy, aim, shoot. The player who aims faster and moves better wins.

**Street Fighter II (1991).** Input combos, spacing, frame advantage. Two humans test their motor skills against each other in real time with no randomness. The fighting game genre is the most refined expression of Shoot because no external variable mediates between the player's input and the outcome.

**Beat Saber (2018).** Swing physical arms to hit targets in time with music. The player's motor performance is scored directly. Dance Dance Revolution applies the same verb with feet. Guitar Hero applies it with fingers on a plastic instrument.

**Super Mario Bros (1985).** The jump button is the shot. The player times spatial positioning across gaps, onto enemies, under obstacles. A missed jump is a missed shot. The platformer genre is Shoot applied to traversal rather than combat.

**Gran Turismo (1997).** The racing line is the target pattern. Brake at the correct meter marker, turn in at the correct angle, accelerate out at the correct moment. The car is the projectile. The track is the target.

What pure Shoot produces: flow state, performance satisfaction, competitive ranking. What pure Shoot cannot produce: meaning, narrative, emergence, or surprise from inside the game state. A perfectly aimed headshot is satisfying because the player's body performed well, not because anything in the game world changed meaningfully. The demon dies the same way every time.

### 2.2 Pure Solve

**Zork (1980).** Read a text description. Reason about what is possible. Type a command. The game is a state machine and the player is searching for the correct input sequence. No motor skill. No agents.

**Chess (6th century).** Two players reason about a shared state space with perfect information. No randomness, no reflexes, no agents. The skill ceiling is analytical depth. Chess has sustained for 1,500 years on one verb.

**Tetris (1984).** Solve under extreme time pressure. The player recognizes the piece shape, identifies the optimal placement, and executes before the piece reaches the bottom. The time pressure creates the feeling of Shoot, but the skill being tested is pattern recognition and placement, not aiming. A player with perfect piece knowledge and poor reflexes beats a player with fast reflexes and poor placement decisions.

**Baba Is You (2019).** The player manipulates the rules of the game by pushing word blocks. "BABA IS YOU" can become "WALL IS YOU." The puzzle is identifying which rule change transforms the unsolvable into the solvable. Pure logic applied to a meta-layer.

**The Witness (2016).** Line puzzles that teach their own rules through progressive complexity. No narrative reward. No unlock progression beyond access to more puzzles. The satisfaction is the moment of understanding.

**Death Stranding (2019).** Every delivery is a planning problem: route selection, weight distribution, cargo stacking, stamina management, weather avoidance, ladder and rope placement. The walking is the execution of the plan. The combat encounters add minor Shoot, but the game is overwhelmingly Solve. The player who plans better succeeds regardless of combat ability.

**Civilization (1991).** Solve at empire scale. Technology order, city placement, military composition, diplomatic stance, economic output. Each turn is a set of decisions made against a state space too large to fully evaluate. The skill is heuristic reasoning — identifying which decisions matter most right now.

**XCOM (2012).** Solve applied to tactical combat. The player selects positions, chooses actions, and manages risk. Dice determine hit outcomes, but the player's positioning and action selection determine the probability space. No aiming. No reflexes. The game is entirely about selecting the best action from the available set.

What pure Solve produces: understanding satisfaction, strategic depth, the pleasure of optimization. What pure Solve cannot produce: surprise from inside the game state. The puzzle has a correct answer. The chess position has an optimal move. Once the player has solved the problem, repeating it produces no new information. Solve games sustain through new content (more puzzles) or adversarial opponents (other humans generating novel states). The game itself, left running, generates nothing new.

### 2.3 Pure Watch

**Little Computer People (1985).** One person in a cross-section house. The player delivers food, books, and records. The person lives autonomously — plays piano, writes letters, cooks, exercises, and gets sick if neglected. The player watches. The interaction is providing conditions. The entertainment is seeing the autonomous response.

**Tamagotchi (1996).** One creature on a keychain. Feed, clean, play. It grows, changes form, and dies based on the care provided. The player watches development happen. The interaction is condition-setting. The satisfaction is the developmental response.

**Animal Crossing (2001).** A village of autonomous animal NPCs on a real-time clock. They wake, walk, fish, talk, move in, move out. The player visits, gives gifts, plants flowers, and places furniture. The village changes over days and seasons without the player present. The player returns to discover what happened.

**Football Manager (2004).** Set tactics, select lineups, manage training, handle transfers. The match plays itself. The player never kicks a ball. Victory is the quality of the conditions (tactics, squad, fitness, morale) producing winning outcomes autonomously. Football Manager is the purest modern expression of Watch applied to competition. A Football Manager player who loses a match lost because their preparation was insufficient, not because their hand slipped.

What pure Watch produces: discovery, emergence, narrative, emotional attachment to agents. What pure Watch cannot produce: player performance satisfaction or the feeling of direct agency. The player did not aim, did not solve, did not execute a skill. The player set conditions and the system responded. When it works, the satisfaction is discovering something that emerged from conditions the player shaped but did not directly author. When it fails, the frustration is helplessness — wanting an outcome the conditions cannot produce and having no direct lever to force it.

---

## 3. Hybrid Compositions

### 3.1 Shoot + Solve

The most common hybrid in commercial games. The player reasons about strategy and executes through motor skill.

**Halo (2001).** Solve the encounter — which weapons, which vehicle, which approach angle. Then Shoot the encounter — aim, position, grenade timing. Bungie described their design target as "30 seconds of fun" repeating. Those 30 seconds are Solve (identify approach) then Shoot (execute approach), cycling.

**Dark Souls (2011).** Solve the boss — learn the attack pattern, identify the dodge windows, select the build and equipment. Then Shoot the boss — execute the dodge timing, attack during the windows, manage stamina. The difficulty is both. The player must reason correctly AND execute precisely. Neither skill alone is sufficient. A player who understands the pattern but cannot execute the dodge dies. A player who can dodge perfectly but does not understand the pattern also dies.

**StarCraft (1998).** Solve the strategy — build order, army composition, expansion timing, tech path. Then Shoot the tactics — unit micro, drop harassment, army splitting, APM. Professional StarCraft separates players on both axes simultaneously. At lower levels, superior Shoot (faster hands) can overcome inferior Solve (bad build order). At higher levels, the margins on both are razor-thin.

**The Legend of Zelda (1986).** Solve the dungeon — find the item, identify the puzzle, apply the item to the environment. Then Shoot the boss — dodge attacks, aim the item at the weak point, time the strikes. The dungeon is Solve. The boss is Shoot with a Solve prerequisite (identify the weakness). The overworld is Solve (navigation, discovery).

**Resident Evil 4 (2005).** Solve the resource management — which ammo to keep, when to heal, what to sell to the merchant. Then Shoot the encounters — aim for the head, manage crowd spacing, time the melee follow-ups. The survival horror genre is Solve (scarcity planning) wrapping Shoot (combat execution).

**Portal (2007).** Solve the test chamber — reason about which surfaces to connect and where momentum will carry the player. Then Shoot the portals — aim and place them. The Shoot component is trivially easy, because the challenge is cognitive, not motor. Portal is Solve wearing a Shoot interface.

### 3.2 Shoot + Watch

A rarer hybrid. The player acts directly while simultaneously observing autonomous agents.

**Pikmin (2001).** The player directly controls Captain Olimar (Shoot — move, throw Pikmin) while the Pikmin act semi-autonomously (Watch — they carry objects, fight enemies, build bridges, and die if left in danger). The player throws Pikmin into situations and watches outcomes while managing Olimar's position. The genre's charm is that the Pikmin do things the player did not explicitly command.

**Mount & Blade (2008).** The player fights in melee and ranged combat directly (Shoot — swing timing, aim, horse control) while the army follows standing orders (Watch — formations charge, archers volley, cavalry flanks). The player is simultaneously a combatant and a commander. The battle outcome depends on both the player's personal combat performance and the army's autonomous response to the tactical situation.

**Dynasty Warriors (2000).** Shoot through enemy formations (hack, combo, special move) while allied officers and soldiers fight autonomously across the battlefield (Watch — bases fall, officers rout, morale shifts). The player's Shoot performance in one sector influences the Watch outcome in other sectors.

### 3.3 Solve + Watch

The colony sim genre and the management game genre. The player reasons about policy and infrastructure. Agents act autonomously within the designed conditions.

**SimCity (1989).** Solve — zone placement, budget allocation, road routing, utility coverage. Watch — population grows, traffic patterns emerge, crime concentrates, property values shift, disasters strike. The citizens are statistical, not individual. The Watch operates at population scale, not personal scale.

**The Sims (2000).** Solve — household management, career planning, house design, need prioritization. Watch — Sims eat, talk, flirt, argue, burn food, and have autonomous emotional responses to the conditions the player built. The balance between Solve and Watch shifted across the franchise. The Sims 1 had fast motive decay, making Solve dominant — the player spent most of their time managing needs. The Sims 4 slowed motive decay, making Watch dominant — the player has time to observe autonomous behavior. The Sims community's permanent debate over motive decay speed is a debate over the Solve-to-Watch ratio.

**Dwarf Fortress (2006).** Solve — dig designations, workshop placement, labor assignment, military squad configuration, noble management. Watch — dwarves with 50+ personality facets, emergent relationships, tantrum spirals, legendary artifact creation, tragic deaths. The deepest Solve+Watch game ever made.

**RimWorld (2013).** Solve — work priority grid, schedule blocks, building layout, research order, stockpile configuration. Watch — colonists with traits and backstories eat, sleep, socialize, have mental breaks, fall in love, and set fires. An AI storyteller paces authored events against the colony to sustain Watch novelty.

**Factorio (2020).** Solve — production chain design, ratio calculation, layout optimization, logistics network routing. Watch — belts flow, inserters cycle, trains route, the factory runs. The Watch is mechanical, not personal. The satisfaction is watching a designed machine operate correctly. Factorio sustains Watch through the factory's ever-increasing complexity as the player expands, not through agent behavior.

**Football Manager (2004).** Solve — tactical formation, player recruitment, training schedules, match preparation, squad rotation. Watch — the match itself, player development, dressing room dynamics, press conferences, board confidence. The purest Solve+Watch competition game. The match is the Watch payoff for the Solve investment.

### 3.4 Shoot + Solve + Watch

All three verbs active. The player reasons, executes, and observes, either simultaneously or in alternation across game phases.

**Skyrim (2011).** Solve — quest reasoning, character build planning, enchanting and alchemy optimization. Shoot — melee and ranged combat, block timing, dragon fights. Watch — NPC daily schedules, guard patrols, civil war progression, dragon spawning. The Watch component is the weakest of the three. NPCs are shallow, schedules loop within minutes, and the world stops generating novel behavior quickly. The game sustains on Solve (exploration, discovery) and Shoot (combat variety).

**Minecraft (2011).** Solve — crafting recipes, building design, redstone circuitry, resource planning, enchanting optimization. Shoot — mob combat, PvP, bow aiming. Watch — villager breeding, mob spawning patterns, crop growth, animal behavior. The verb balance shifts radically between modes: Survival emphasizes Solve+Shoot, Creative drops Shoot entirely, and Hardcore adds permanent consequences to all three.

**Grand Theft Auto V (2013).** Shoot — gunplay, driving, flying, combat encounters. Solve — heist planning, mission approach selection, property management. Watch — city life, pedestrians, traffic, police escalation, NPC routines. Rockstar invested hundreds of millions of dollars in Watch scenery. It generates no emergent novelty after the first hour because no NPC has state deeper than a behavior loop lasting seconds.

**Red Dead Redemption 2 (2018).** Shoot — gunplay, hunting, horseback combat, duels. Solve — camp resource management, honor system navigation, quest decision-making. Watch — camp member daily routines, companion commentary on player behavior, wildlife ecosystems, weather and seasonal changes. The Watch component is the strongest in any Rockstar game. Camp members comment on the player's actions, change disposition over story progression, and have visible daily routines. The Watch still exhausts because the NPCs respond to authored story triggers, not to emergent internal state.

**Baldur's Gate 3 (2023).** Solve — tactical turn-based combat, dialogue choices, party composition, quest approach reasoning. Shoot — action execution within the tactical framework (minor, since turn-based removes motor skill). Watch — companion reactions to player choices, camp conversations, NPC reputation responses, world-state changes from player decisions. The Watch component is stronger than most RPGs because companion characters have deep authored reactions to the player's Solve decisions, creating a convincing simulation of autonomous personality. The Watch is still authored rather than emergent — companions react to specific flags, not to continuous internal state.

---

## 4. The Verb Contract

Every game establishes a contract with the player about which verbs are active. The player calibrates their engagement based on the verb they expect to use. A Shoot player enters a flow state of motor readiness. A Solve player enters an analytical state of strategic evaluation. A Watch player enters an observational state of pattern recognition and emotional investment.

When a game breaks its own verb contract, the player experiences a mismatch between their current cognitive state and the game's sudden demand. This mismatch is the source of the most persistent player frustrations in the medium.

### 4.1 Watch Broken by Shoot

**RimWorld.** The game establishes a Solve+Watch contract. The player sets priorities and building layouts (Solve) and watches colonists live (Watch). Then raiders arrive and the game demands that the player draft colonists, position them behind cover, assign targets, and manage firing lines in real time (Shoot). The player who was watching named people live must now puppet-control them through a tactical combat system that was never designed for tactical combat. The colonists have no spatial reasoning for combat positioning. Their AI was designed for hauling and cooking, not for holding a firing line. The player pauses every few seconds to correct what the AI gets wrong.

The result is the single most complained-about aspect of RimWorld: combat that feels like bad XCOM bolted onto a colony sim. Players describe it as an exercise in micromanagement that should not be needed. The core game generates stories about people. The combat generates stories about the player's pause-button speed.

### 4.2 Watch Broken by Solve Overload

**Dwarf Fortress.** The game establishes a Solve+Watch contract. The player designates and assigns (Solve) and watches dwarves live (Watch). Then goblins arrive and the game demands that the player navigate 20 nested keyboard-driven menus to configure squad composition, equipment assignment, station orders, alert levels, and burrow restrictions (Solve at extreme complexity under time pressure). The Watch is lost. The player is not watching dwarves fight. The player is solving a menu-navigation puzzle while dwarves die offscreen.

The deepest Watch simulation in gaming goes silent at the moment of highest dramatic stakes because the Solve interface consumes the player's entire attention. The player who masters the military menus eventually gets to Watch their military respond to threats, but the learning cost is dozens of lost fortresses.

### 4.3 Watch Starved by Insufficient Solve

**The Sims 4.** The game establishes a Solve+Watch contract. But motive decay is slow enough that the Solve component is trivial — Sims rarely face genuine need crises. Without Solve pressure, the Watch has no source of novelty. The Sims are always comfortable, always fed, always rested. Nothing goes wrong. Nothing goes wrong means nothing interesting happens. The Watch produces no stories because the conditions never create situations where the autonomous behavior produces surprise.

The Sims community splits permanently on this axis. Players who want more Solve ask for faster motive decay, harder career progression, and meaningful consequences. Players who want more Watch ask for deeper autonomous behavior, better AI, and richer social simulation. Both are asking for the same thing — Watch that sustains — from opposite directions.

### 4.4 Watch Scenery Without Watch Agents

**GTA V and Red Dead Redemption 2.** Both games invest enormous resources in building Watch environments — living cities, populated towns, wildlife ecosystems. The environments are visually convincing. They feel alive while the player moves through them because the player sees each NPC for seconds before passing. Stop and observe any single NPC and the illusion collapses within moments. The NPC has no internal state. Their behavior is a short loop. They are not agents. They are animated scenery.

The Watch contract requires agents whose internal state generates behavior the player did not predict. Scenery that looks like agents is not agents. The most expensive Watch environment in gaming history generates less emergent novelty than a single Dwarf Fortress dwarf with a grudge against the mayor.

---

## 5. What Each Verb Produces and Cannot Produce

| Verb | Produces | Cannot Produce |
|---|---|---|
| Shoot | Flow state, performance satisfaction, competitive ranking, the feeling of personal mastery | Meaning, narrative, emergence, or surprise from inside the game state |
| Solve | Understanding satisfaction, strategic depth, the pleasure of optimization, intellectual engagement | Surprise from inside the system, novelty without new content or new opponents |
| Watch | Discovery, emergence, narrative, emotional attachment to agents, stories the player tells afterward | Player performance satisfaction, the feeling of direct agency, the feeling of personal skill |

These constraints are absolute. No amount of design craft can make a pure Shoot game produce emergent narrative. No amount of design craft can make a pure Solve game generate surprise from its own state without new input. No amount of design craft can make a pure Watch game feel like the player personally accomplished something through their own skill.

The constraints explain why hybrids dominate commercial games. Players want multiple satisfactions. Shoot+Solve (the action RPG, the tactical shooter, the puzzle-platformer) is the largest commercial category because it delivers both performance satisfaction and strategic depth. Solve+Watch (the colony sim, the management game, the life sim) delivers both strategic depth and emergent narrative but sacrifices performance satisfaction. Shoot+Watch is rare because the two verbs create contradictory player states — motor readiness versus patient observation.

---

## 6. The Hardest Composition

Solve+Watch where the Watch sustains indefinitely is the hardest design problem in games.

Shoot sustains through motor challenge escalation. Faster enemies, harder patterns, tighter windows. The player's body is always being tested.

Solve sustains through new content or new opponents. More puzzles, deeper strategy trees, human adversaries generating novel positions.

Watch sustains only if the autonomous agents generate novelty from their own coupled state, continuously, without authored injection and without the player's direct input creating the novelty. This requires three things simultaneously:

**Agent depth.** Each agent must have enough internal state that their behavior is not predictable from their visible properties. An agent with three static traits (RimWorld) exhausts its behavioral range quickly. An agent with dozens of continuous values, relationship instances, formative events, and personality drift has a state space large enough to produce behavior the player has not seen before.

**System coupling.** The agents must exist within coupled systems that produce novel pressure without authored events. If the only source of novelty is a storyteller injecting raids and diseases on a timer, the Watch is consuming authored content, and authored content is finite. If the systems themselves produce crises — water freezing, stench drifting, herds stampeding, fences breaking, social cascades propagating through relationship networks — then the novelty emerges from state interaction and is functionally inexhaustible.

**Visibility.** The player must be able to trace causation from the conditions they shaped through the agent's decision process to the emergent behavior. If the Watch is opaque — if the player cannot see why the agent did what it did — then emergent behavior is indistinguishable from randomness. The player's investment in shaping conditions is wasted if they cannot connect the conditions to the outcome. Full visibility transforms Watch from passive observation into active comprehension, which sustains engagement.

No shipping game has achieved all three simultaneously. Dwarf Fortress has agent depth and system coupling but lacks visibility. RimWorld has visibility and some system coupling but lacks agent depth. The Sims has visibility and agent depth for a household but lacks system coupling. Football Manager has all three for the narrow domain of football tactics and match simulation.

The design challenge is not a mystery. It is an engineering problem: build agents with deep continuous state, couple them through systems that produce emergent pressure, and show the player everything. The reason it has not been done is that each requirement is individually expensive and the three requirements multiply each other's cost. Deep agents are expensive. Coupled systems are expensive. Full visibility on deep agents within coupled systems is the product of those costs.

---

## 7. The Three Satisfactions

Each verb produces a distinct satisfaction that the others cannot replicate.

**Shoot satisfaction: "I did that."** The player's body performed. The headshot landed. The combo executed. The lap time improved. The satisfaction is personal and immediate. The player proved something about themselves. This satisfaction is the most primal and the most universal — every human understands the pleasure of physical competence.

**Solve satisfaction: "I figured that out."** The player's mind comprehended. The puzzle yielded. The strategy worked. The optimization converged. The satisfaction is intellectual and deferred — it arrives when the result of the reasoning becomes clear. The player proved something about their understanding.

**Watch satisfaction: "I saw that happen."** Something emerged that the player did not create directly. The agent did something unexpected. The system produced a cascade the player did not foresee. The story wrote itself from the conditions the player shaped. The satisfaction is neither personal performance nor intellectual achievement. It is the satisfaction of discovery — witnessing something new that came from a system the player influenced but did not control.

Watch satisfaction is the satisfaction of a gardener seeing a plant bloom in a way they did not expect. The gardener chose the soil, the position, the watering schedule. The plant did the rest. The bloom is not the gardener's creation. It is the plant's response to the gardener's conditions. The gardener's satisfaction is real, specific, and different from the satisfaction of painting the flower themselves (Shoot) or solving the equation for optimal growth conditions (Solve).

Watch satisfaction is also the satisfaction a parent feels observing their child navigate a social situation well. The parent shaped the conditions — the upbringing, the values, the environment. The child acted autonomously. The outcome emerged from the conditions the parent shaped and the child's own internal state. The parent did not direct the interaction (Shoot) or solve a puzzle to produce it (Solve). The parent watched.

This is the satisfaction that colony sim players describe when they tell stories about their colonies. "A colonist's pet died, sending them into a mental break; they punched another colonist, who held a grudge; a raid arrived at the worst possible moment; and suddenly you have a story you will tell for years." The player shaped the colony. The agents lived in it. The story emerged. The player's satisfaction is: "I saw that happen in the conditions I built."

---

## 8. Why Watch Is the Hardest Verb to Sustain

Watch is the hardest verb because it requires the game to generate novelty without the player's input creating the novelty.

Shoot generates novelty from the player's input — each engagement is different because the player's body behaves differently each time. Even against identical enemies in identical positions, two attempts produce different motor patterns and different outcomes.

Solve generates novelty from new content or new opponents. A new puzzle is a new Solve instance. A human opponent generates novel game states through their own reasoning. The game does not need to generate novelty internally because the input stream (new puzzles, new opponents) provides it.

Watch requires the game itself to generate novelty from its own state. The player is observing, not inputting. If the agents' behavior is predictable from their visible state, the Watch produces no new information and the player disengages.

This is why every open-world game fails the Watch test within minutes of the player standing still. The NPC behavior loops are short. The state is shallow. The player sees the loop, predicts the next iteration, and the Watch is over. The game survives by keeping the player moving through Shoot and Solve activities so that each NPC is seen for only seconds — long enough for the behavior to register as "alive," short enough that the loop is never visible.

A Watch game that sustains must produce behavior that surprises the player who is paying close attention. Not random behavior — random behavior is noise, not novelty. Behavior that is causally traceable to the agent's internal state and the environmental conditions, but that the player did not predict because the state space was too large to fully anticipate.

This is the formal requirement: the agent's state space must be large enough that the player, even with full visibility into all values, cannot predict the next behavior from the current state without running the simulation forward. The player can understand why the behavior happened (tracing the causation backward) but could not have predicted it would happen (computing the outcome forward). Understanding without prediction. That is the Watch experience: comprehensible surprise.

---

## 9. Implications for Design

### 9.1 Know Your Verb

The first design decision is which verb the game uses. This decision constrains every subsequent choice. A Shoot game needs tight input response, escalating motor challenges, and competitive ranking. A Solve game needs a deep state space, clear rules, and either authored content or adversarial opponents. A Watch game needs deep autonomous agents, coupled systems, and full visibility.

Designing a Watch game with Shoot tools produces RimWorld's draft mode. Designing a Watch game with Solve-overloaded interfaces produces Dwarf Fortress's military menus. Both are games that know what they are (Watch) and break their own contract at the moment of highest stakes by inserting a verb the game was not designed around.

### 9.2 Honor the Contract

When the game establishes a verb with the player, breaking it costs trust. A Watch player who invested emotionally in named agents does not want to puppet-control them through a tactics interface. A Solve player deep in strategic reasoning does not want a reflex test. A Shoot player in flow state does not want to stop and solve a puzzle.

Hybrids work when the verbs alternate cleanly. Halo's 30-second loop alternates Solve (assess the encounter) and Shoot (execute the approach) with clear phase boundaries. The player knows which verb is active. Dark Souls alternates Solve (learn the pattern) and Shoot (execute the dodge) with death as the phase boundary.

Hybrids break when the verbs collide without phase boundaries. RimWorld's draft mode inserts Shoot into Watch without warning — the raid arrives and the player must shift cognitive states instantly from observation to motor control. The mismatch is the frustration.

### 9.3 Watch Needs Pressure

Watch without Solve pressure produces The Sims 4 — agents that are always comfortable and never generate crisis. The Watch is unstressed, which means the Watch is uneventful, which means the Watch is boring.

Solve pressure in a Watch game is not a storyteller injecting authored events. Solve pressure is the coupled systems producing conditions that force the agents into novel states. Winter freezing the water supply is Solve pressure that produces Watch novelty — the agents must adapt to scarcity, and their adaptation is the Watch content.

The Solve component in a Solve+Watch game is not a separate game bolted onto the Watch. The Solve component is the player shaping conditions that stress the Watch agents. Better conditions produce less stress and less Watch novelty. Worse conditions produce more stress and more Watch novelty. The player's Solve skill determines the character of the Watch they observe. A skilled Solve player watches a colony under manageable pressure producing gradual character development. A less skilled Solve player watches a colony under extreme pressure producing dramatic crisis and cascade. Both are valid Watch experiences produced by different Solve inputs.

### 9.4 The Irreducible Triad

The three verbs are irreducible. None can be decomposed into the others.

Shoot cannot be reduced to Solve because motor skill and cognitive skill are different human capacities. A chess grandmaster cannot aim a rifle. A professional marksman cannot play grandmaster chess. The skills do not transfer.

Solve cannot be reduced to Watch because reasoning about a state and observing agents in a state are different activities. A player reasoning about the optimal city layout in SimCity is Solving. A player observing traffic patterns emerge in the city they built is Watching. Both happen in the same game, sequentially, using different cognitive faculties.

Watch cannot be reduced to Shoot or Solve because the player is not acting on the state (Shoot) or reasoning about the correct transformation (Solve). The player is observing autonomous behavior emerge from shaped conditions. The activity is comprehension of emergent phenomena, which is distinct from both motor execution and analytical reasoning.

The three verbs correspond to three fundamental relationships between a human and a system: acting on it (Shoot), reasoning about it (Solve), and observing it (Watch). Every game asks the player to do one, two, or all three. No game asks the player to do something outside these three. The triad is complete.

---

## Appendix A: Complete Game Classification

Every entry is the verb composition at the game's primary interaction layer. Auxiliary verbs in parentheses indicate secondary presence that does not define the core loop.

### A.1 Pure Shoot

| Game | Year | Subgenre | What the Player's Body Does |
|---|---|---|---|
| Pong | 1972 | Arcade | Positions paddle to intercept ball |
| Space Invaders | 1978 | Fixed shooter | Moves laterally, fires upward |
| Asteroids | 1979 | Arena shooter | Rotates, thrusts, fires |
| Pac-Man | 1980 | Maze | Navigates under time and spatial pressure |
| Galaga | 1981 | Fixed shooter | Moves laterally, fires, dodges |
| Super Mario Bros | 1985 | Platformer | Times jumps across spatial gaps |
| Contra | 1987 | Run-and-gun | Moves, aims in 8 directions, fires |
| Street Fighter II | 1991 | Fighting | Input combos, spacing, frame timing |
| Doom | 1993 | FPS | Aims, moves, fires in 3D corridors |
| Wipeout | 1995 | Racing | Steers at speed, uses pickups |
| Gran Turismo | 1997 | Racing sim | Braking points, racing line, throttle control |
| Dance Dance Revolution | 1998 | Rhythm | Steps on arrows in time with music |
| Quake III Arena | 1999 | Arena FPS | Strafe-jumps, rocket prediction, rail aim |
| Ikaruga | 2001 | Shoot-em-up | Dodges dense patterns, switches polarity |
| Guitar Hero | 2005 | Rhythm | Presses fret buttons in time with music |
| Call of Duty 4 | 2007 | Military FPS | Aims, fires, moves to cover |
| Super Meat Boy | 2010 | Precision platformer | Frame-perfect jumps and wall slides |
| Splatoon | 2015 | Shooter | Aims, fires paint, navigates paint surfaces |
| Celeste | 2018 | Precision platformer | Dash timing, wall cling, momentum |
| Beat Saber | 2018 | VR rhythm | Swings arms to cut blocks in time |
| Sekiro | 2019 | Action | Deflect timing, posture management |

### A.2 Pure Solve

| Game | Year | Subgenre | What the Player's Mind Does |
|---|---|---|---|
| Chess | ~600 | Abstract strategy | Evaluates positions, selects moves |
| Go | ~2500 BC | Abstract strategy | Territory evaluation, influence mapping |
| Zork | 1980 | Text adventure | Parses environment descriptions, selects verb-noun commands |
| Tetris | 1984 | Falling block | Pattern recognition, optimal placement under time |
| SimCity | 1989 | City builder | Zoning, budgeting, infrastructure routing |
| Myst | 1993 | Puzzle adventure | Deduces mechanical puzzle rules from observation |
| Civilization | 1991 | 4X strategy | Optimizes across technology, economy, diplomacy, military |
| Advance Wars | 2001 | Turn-based tactics | Unit positioning, terrain advantage, force composition |
| Phoenix Wright | 2001 | Visual novel puzzle | Cross-references evidence against testimony |
| Professor Layton | 2007 | Puzzle collection | Solves self-contained logic puzzles |
| SpaceChem | 2011 | Programming puzzle | Designs molecular assembly machines |
| FTL | 2012 | Roguelike strategy | Resource allocation under escalating scarcity |
| XCOM | 2012 | Turn-based tactics | Soldier positioning, action selection, risk management |
| Papers Please | 2013 | Document inspection | Cross-references passport data against rules |
| The Witness | 2016 | Environmental puzzle | Internalizes abstract line-puzzle rules from examples |
| Into the Breach | 2018 | Puzzle tactics | Perfect-information tactical puzzles, deterministic outcomes |
| Baba Is You | 2019 | Rule manipulation | Rearranges the game's own rules to create solvable states |
| Death Stranding | 2019 | Logistics | Route planning, weight distribution, stamina management |
| Return of the Obra Dinn | 2018 | Deduction | Identifies 60 fates from fragmented death scenes |

### A.3 Pure Watch

| Game | Year | Subgenre | What the Player Observes |
|---|---|---|---|
| Little Computer People | 1985 | Life sim | One person living autonomously in a house |
| SimAnt | 1991 | Ecosystem sim | Ant colony responding to pheromone influence |
| Creatures | 1996 | Artificial life | Organisms with neural networks learning and breeding |
| Tamagotchi | 1996 | Virtual pet | One creature developing from care inputs |
| Animal Crossing | 2001 | Village life | NPC villagers on real-time clock schedules |
| Nintendogs | 2005 | Virtual pet | Dogs responding to touch and voice training |
| Football Manager | 2004 | Sports management | Matches playing out from tactical settings |
| Equilinox | 2018 | Ecosystem | Plant and animal populations balancing |
| Terra Nil | 2023 | Restoration | Landscape recovering from environmental inputs |

### A.4 Shoot + Solve

| Game | Year | Solve Component | Shoot Component |
|---|---|---|---|
| The Legend of Zelda | 1986 | Dungeon item puzzles, key progression | Boss combat, enemy timing |
| Metroid | 1986 | Ability-gated navigation, map reasoning | Aim, dodge, platform |
| Half-Life | 1998 | Physics puzzles, environmental navigation | Gunplay, grenade timing |
| Deus Ex | 2000 | Multiple-approach level design, build optimization | Shooting, stealth positioning |
| Halo | 2001 | Weapon selection, vehicle routing, encounter approach | Aiming, grenade placement, melee timing |
| Resident Evil 4 | 2005 | Resource scarcity management, merchant optimization | Aiming, crowd spacing, melee follow-ups |
| Portal | 2007 | Spatial physics puzzles | Portal placement aim (trivial) |
| Dark Souls | 2011 | Boss pattern learning, build optimization, route planning | Dodge timing, attack windows, stamina management |
| The Binding of Isaac | 2011 | Item synergy evaluation, route risk assessment | Twin-stick aim, dodging |
| Elden Ring | 2022 | Build optimization, exploration routing, boss pattern ID | Dodge timing, positioning, combo execution |
| Tears of the Kingdom | 2023 | Physics construction, environmental puzzles | Combat timing, aiming thrown objects |

### A.5 Shoot + Watch

| Game | Year | Watch Component | Shoot Component |
|---|---|---|---|
| Pikmin | 2001 | Pikmin carry, fight, build autonomously | Olimar movement, Pikmin throwing |
| Overlord | 2007 | Minions swarm, loot, fight by type | Overlord melee, minion sweeping |
| Mount & Blade | 2008 | Army on standing orders, formations, routing | Personal melee, mounted combat, archery |
| Dynasty Warriors | 2000 | Officers fight, bases change hands, morale shifts | Hack through formations, combos |
| Brutal Legend | 2009 | Stage battles with autonomous rock armies | Melee combat, guitar solos |

### A.6 Solve + Watch

| Game | Year | Solve Component | Watch Component |
|---|---|---|---|
| SimCity | 1989 | Zoning, budget, infrastructure | Population growth, traffic, crime, disasters |
| The Sims | 2000 | Need management, career, house design | Autonomous Sim behavior, social interactions |
| Dwarf Fortress | 2006 | Designation, labor, military config | Dwarf personality, emergent stories, cascades |
| Football Manager | 2004 | Tactics, transfers, training, lineup | Match simulation, player development, dressing room |
| Tropico | 2001 | Building placement, edict policy, faction balancing | Citizens working, protesting, emigrating |
| Prison Architect | 2015 | Cell layout, staffing, regime scheduling | Prisoner behavior, riots, escapes |
| RimWorld | 2013 | Priority grid, schedule, layout, research | Colonist behavior, social events, mental breaks |
| Oxygen Not Included | 2017 | Pipe routing, gas management, heat exchange | Duplicant behavior, system cascades |
| Factorio | 2020 | Production chains, ratio calculation, layout | Factory operation, belt flow, train routing |
| Frostpunk | 2018 | Law passage, building placement, resource allocation | Citizen response, hope/discontent, societal shift |
| Banished | 2014 | Town layout, resource chain, population management | Villager survival across seasons |
| Two Point Hospital | 2018 | Room layout, staff hiring, research | Patient flow, treatment, staff behavior |

### A.7 Shoot + Solve + Watch

| Game | Year | Primary | Secondary | Tertiary |
|---|---|---|---|---|
| Skyrim | 2011 | Shoot (combat) | Solve (quests, builds) | Watch (NPC schedules — weak) |
| Minecraft | 2011 | Solve (crafting, building) | Shoot (combat) | Watch (mobs, villagers — weak) |
| GTA V | 2013 | Shoot (gunplay, driving) | Solve (heists, missions) | Watch (city life — scenery only) |
| Baldur's Gate 3 | 2023 | Solve (tactical combat, dialogue) | Watch (companion reactions) | Shoot (minimal in turn-based) |
| RDR2 | 2018 | Shoot (gunplay, hunting) | Solve (camp, honor, quests) | Watch (camp life, wildlife — strongest Rockstar Watch) |
| Subnautica | 2018 | Solve (crafting, base building, exploration) | Shoot (creature avoidance/combat — minor) | Watch (ecosystem behavior) |
| Kenshi | 2018 | Solve (base building, squad management) | Shoot (real-time squad combat) | Watch (world factions warring, NPCs living) |
| Valheim | 2021 | Shoot (combat, sailing) | Solve (building, crafting, boss preparation) | Watch (ecosystem, weather, mob behavior) |
| Rimworld w/ draft | 2013 | Solve (colony management) | Watch (colonist behavior) | Shoot (drafted combat — contract-breaking) |

---

## Appendix B: Verb Interference Matrix

When two verbs are active simultaneously, each combination produces a characteristic interference pattern. These patterns explain why certain hybrids succeed and others produce player frustration.

| Active Pair | Interference Type | Result | Example |
|---|---|---|---|
| Shoot + Solve (alternating) | Clean phase boundary | Player switches cognitive mode between phases. Works well when phases are clearly signaled | Halo: assess encounter (Solve), then execute (Shoot), cycle |
| Shoot + Solve (simultaneous) | Cognitive split | Player must reason and execute motor skill at the same time. Produces the highest skill ceilings | StarCraft: strategic planning AND unit micro at the same time |
| Shoot + Watch (simultaneous) | Attention split | Player must act AND observe autonomous agents. Works when the Shoot is simple enough to not consume full attention | Pikmin: throw Pikmin (simple Shoot) while watching them work (Watch) |
| Shoot + Watch (competing) | Contract collision | Player wants to watch but must act. Agents the player cares about are puppet-controlled. Destroys Watch investment | RimWorld draft: player puppets named characters through bad tactics |
| Solve + Watch (alternating) | Natural colony sim loop | Player sets conditions (Solve), observes results (Watch), adjusts (Solve). The genre's core rhythm | Football Manager: set tactics (Solve), watch match (Watch) |
| Solve + Watch (Solve overload) | Watch displacement | Solve consumes all attention. Watch events happen unseen. Agent deaths occur offscreen during menu navigation | DF military menus during goblin siege |
| Solve + Watch (Watch dominant) | Solve atrophy | Watch produces no pressure. Solve has nothing to respond to. Player disengages from both | Sims 4: needs too easy, no crisis, nothing to manage or observe |
| All three (phased) | Mode switching | Player alternates between cognitive states with clear transitions. Manageable if transitions are voluntary | Minecraft: build (Solve), fight (Shoot), observe farm (Watch) — player chooses when |
| All three (forced) | Cognitive overload | Game demands motor execution, strategic reasoning, and agent observation simultaneously. Produces frustration at high intensity | Late-game RTS battles: micro units (Shoot), adjust production (Solve), monitor ally positions (Watch) |

---

## Appendix C: Watch Agent Depth Comparison

The sustainability of Watch is determined by the state space of the autonomous agents. Shallow agents exhaust quickly. Deep agents sustain longer. This table compares agent depth across Watch and Solve+Watch games.

| Game | Agent Count | State Dimensions per Agent | State Persistence | Novelty Duration Before Exhaustion |
|---|---|---|---|---|
| Tamagotchi | 1 | ~5 (hunger, happy, discipline, age, weight) | Persistent until death | Hours |
| Animal Crossing NPC | ~10 | ~8 (personality type, friendship, catchphrase, mood, schedule) | Persistent across sessions | Days to weeks |
| The Sims 1 | 1-8 | ~15 (8 motives, 5 personality axes, skills, relationships) | Session-persistent | Days |
| The Sims 4 | 1-8 | ~20 (6 motives, 3 traits, emotions, skills, relationships, aspirations) | Session-persistent | Hours (low motive pressure) |
| SimCity citizen | Statistical | 0 per individual (population-level statistics) | N/A | N/A (Watch is population-scale) |
| Prison Architect inmate | ~300 | ~10 (needs, sentence, gang, traits, contraband) | Session-persistent | Days |
| RimWorld pawn | 3-30 | ~25 (3 traits, skills, needs bars, mood thoughts, social opinions, health) | Persistent in save | Weeks |
| Football Manager player | ~25 active | ~50 (attributes, personality, morale, form, fitness, preferred moves, history) | Persistent across seasons | Months to years |
| Dwarf Fortress dwarf | 7-300 | ~150 (50+ personality facets, 50+ values, skills, anatomy, preferences, relationships, thoughts, needs) | Persistent in save | Months to years (if visible) |

### C.1 The Visibility Penalty

Agent depth that is not visible to the player does not contribute to Watch sustainability. The effective depth for Watch purposes is: visible dimensions × coupling visibility.

| Game | Total Dimensions | Visible to Player | Effective Watch Depth |
|---|---|---|---|
| The Sims 4 | ~20 | ~18 (motive bars, trait labels, emotion display) | 18 (high visibility, low depth) |
| RimWorld | ~25 | ~20 (needs tab, bio tab, social tab, health tab) | 15 (split across 6 tabs, cross-referencing required) |
| Dwarf Fortress | ~150 | ~30 (accessible without deep menu navigation) | 20 (massive depth hidden behind inaccessible UI) |
| Football Manager | ~50 | ~45 (scout reports, stat screens, match analysis) | 40 (strong visibility infrastructure) |

Dwarf Fortress has 5× the raw agent depth of RimWorld but only marginally more effective Watch depth, because 80% of DF's dimensions are inaccessible without wiki knowledge and multi-layer menu navigation. Football Manager achieves the highest effective Watch depth by combining moderate raw depth with strong visibility infrastructure (scouting reports, match statistics, form graphs, comparison tools).

---

## Appendix D: Contract Violations in Major Titles

Catalogued by the verb that was violated, what verb was injected, and the player sentiment produced.

| Game | Established Contract | Injected Verb | Violation Point | Player Sentiment |
|---|---|---|---|---|
| RimWorld | Solve + Watch | Shoot (draft mode) | Raid arrival | "Pawns stand in the open like goobers." "Exercise in micro-management that shouldn't be needed." "The dumbest pawn AI I've seen." |
| Dwarf Fortress | Solve + Watch | Solve overload (military menus) | Goblin siege | "20 menus at once or they all die in 1 minute." Navigation, menu systems cited as top frustration. |
| The Sims 4 | Solve + Watch | Neither (Solve removed by trivial decay) | Sustained play | "Motives decay too slowly." "Nothing appears to matter." "Give us roadblocks." |
| XCOM 2 | Solve | Shoot (timed missions forcing rushed tactics) | Timed mission start | "Timer ruins the tactical experience." Players want to Solve without Shoot time pressure. |
| Skyrim | Shoot + Solve | Watch deficit (NPC shallowness) | Stopping in any town | NPCs loop within seconds. "I used to be an adventurer like you" becomes a meme of Watch failure. |
| GTA V | Shoot + Solve | Watch deficit (NPC shallowness) | Standing still anywhere | $265M development. NPCs are particles in a flow field. Watch exhausts in seconds. |
| RDR2 | Shoot + Solve + Watch | Watch deficit (authored not emergent) | Camp after story completion | Camp NPCs respond to story flags, not emergent state. Post-story camp is static. |
| Dark Souls | Shoot + Solve | Neither (contract honored) | N/A | Both verbs active throughout. Deaths teach Solve. Execution tests Shoot. No violation. |
| Football Manager | Solve + Watch | Neither (contract honored) | N/A | Pure Solve+Watch for 20+ years. Match is always Watch. Tactics are always Solve. |

---

## Appendix E: Verb Distribution Across Genres

Each genre is defined by its primary verb composition. Genres that appear distinct share verb structure. Genres that appear similar differ by verb.

| Genre | Primary Verb | Secondary | Notes |
|---|---|---|---|
| FPS | Shoot | — | Defined by the verb |
| TPS | Shoot | Solve (cover selection) | Third-person does not change the verb |
| Fighting | Shoot | — | Input execution is motor, not cognitive |
| Racing | Shoot | — | Racing line is a motor skill |
| Rhythm | Shoot | — | Pattern execution is motor |
| Precision platformer | Shoot | — | Jump timing is motor |
| Puzzle | Solve | — | Defined by the verb |
| Text adventure | Solve | — | State machine navigation through reasoning |
| Visual novel | Solve | — | Branch selection through reasoning |
| Walking simulator | Solve | — | Degenerate Solve (find next content node) |
| 4X strategy | Solve | — | Empire optimization |
| Turn-based tactics | Solve | — | Tactical positioning, no motor skill |
| Card game (digital) | Solve | — | Deck building and play sequencing |
| City builder | Solve | Watch | Zoning is Solve, growth is Watch |
| Colony sim | Solve | Watch | Policy is Solve, agents are Watch |
| Life sim | Watch | Solve | Agents are Watch, need management is Solve |
| Virtual pet | Watch | — | Care inputs, autonomous development |
| Sports management | Solve | Watch | Tactics are Solve, match is Watch |
| Action RPG | Shoot | Solve | Combat is Shoot, builds/quests are Solve |
| Immersive sim | Solve | Shoot | Approach planning is Solve, execution is Shoot |
| Survival crafting | Solve | Shoot | Resource planning is Solve, combat is Shoot |
| Metroidvania | Shoot | Solve | Combat is Shoot, ability-gated navigation is Solve |
| RTS | Shoot + Solve | (Watch) | Micro is Shoot, strategy is Solve, base runs itself (minor Watch) |
| Open world RPG | Shoot + Solve | (Watch) | Combat + quests, with NPC scenery |
| Sandbox | Solve | Shoot + Watch | Building is Solve, combat is Shoot, systems are Watch |
| Auto-battler | Solve | Watch | Composition is Solve, fight is Watch |
| Tower defense | Solve | Watch | Placement is Solve, waves are Watch |
| Idle/incremental | Solve | Watch | Upgrade selection is Solve, numbers grow as Watch |

---

## Appendix F: The Verb and Retention

Each verb produces a different retention curve — how long the player continues playing before disengaging.

| Verb | Retention Driver | Exhaustion Mechanism | Typical Retention Curve |
|---|---|---|---|
| Shoot | Motor skill ceiling + competitive ladder | Physical plateau — the player's body stops improving | Steep initial engagement, long plateau for competitive players, sharp dropoff for non-competitive |
| Solve | Content supply + opponent novelty | Content depletion — all puzzles solved, all strategies explored | High initial engagement, gradual decline as content exhausts, sustained only by PvP or new content |
| Watch | Agent novelty + system coupling | Behavioral exhaustion — agents become predictable | Highly variable — depends entirely on agent depth and system coupling |

### F.1 Watch Retention Failure Modes

| Failure Mode | Cause | Example | Time to Exhaustion |
|---|---|---|---|
| Loop visibility | Agent behavior is a short repeating loop | GTA V NPCs | Seconds to minutes |
| Trait exhaustion | Agent personality is shallow and static | RimWorld 3-trait pawns | Hours to days |
| Coupling absence | Systems do not interact, no emergent pressure | Banished (systems are independent) | Days |
| Authored dependency | Novelty comes from authored events, not system state | RimWorld storyteller events | Weeks (content-dependent) |
| Visibility failure | Agent depth exists but is inaccessible | Dwarf Fortress personality | Indefinite (depth never reached) |
| Solve pressure absence | No environmental stress forcing agents into novel states | The Sims 4 slow motive decay | Hours |

### F.2 Watch Retention Success Conditions

| Condition | Mechanism | Example |
|---|---|---|
| Deep continuous state per agent | Large state space prevents behavioral repetition | DF 150-dimension dwarves, FM 50-dimension players |
| Coupled systems producing emergent pressure | Environmental stress forces agents into novel configurations | Winter freezing wells, stench sickening cattle |
| Full visibility on agent state and decision process | Player can trace causation, transforming observation into comprehension | Football Manager match analysis, scout reports |
| Multiple agents interacting | Pairwise interactions multiply the state space combinatorially | Colony sims with social systems |
| Permanent consequences | Actions produce irreversible state changes, preventing regression to equilibrium | Permanent transaction records, lineage, death |

---

## Appendix G: Historical Lineage of Each Verb

### G.1 Shoot Lineage

| Year | Game | Innovation |
|---|---|---|
| 1972 | Pong | First commercial Shoot — paddle positioning |
| 1978 | Space Invaders | Shoot with spatial escalation |
| 1980 | Pac-Man | Shoot as navigation under threat (no projectile) |
| 1981 | Donkey Kong | Shoot as platforming — jump as the motor verb |
| 1985 | Super Mario Bros | Platforming as the primary game — running and jumping IS the game |
| 1991 | Street Fighter II | Shoot as competitive human-vs-human motor contest |
| 1993 | Doom | Shoot in 3D — spatial positioning added to aiming |
| 1996 | Quake | Shoot with full 3D movement and mouse aiming |
| 1998 | Dance Dance Revolution | Shoot applied to rhythm — feet as the motor instrument |
| 2005 | Guitar Hero | Shoot applied to music performance — fingers on buttons |
| 2018 | Beat Saber | Shoot in VR — full-body motor performance |

The lineage shows Shoot evolving through new input devices and spatial dimensions, never through new verbs. Pong's paddle and Beat Saber's swords are the same verb — position a thing to intercept a thing — across 46 years of technology.

### G.2 Solve Lineage

| Year | Game | Innovation |
|---|---|---|
| ~600 | Chess | Perfect-information adversarial Solve |
| 1976 | Colossal Cave Adventure | Solve applied to spatial navigation and inventory |
| 1980 | Zork | Solve with natural language parser |
| 1984 | Tetris | Solve under escalating time pressure |
| 1989 | SimCity | Solve applied to systemic management (budgets, zoning) |
| 1991 | Civilization | Solve at empire scale across multiple coupled systems |
| 1993 | Myst | Solve through environmental observation — no text, no inventory |
| 2001 | Phoenix Wright | Solve as cross-referencing evidence against testimony |
| 2007 | Portal | Solve with spatial physics prediction |
| 2012 | XCOM | Solve as tactical risk management with probabilistic outcomes |
| 2018 | Into the Breach | Solve as deterministic perfect-information tactical puzzles |
| 2019 | Baba Is You | Solve applied to the game's own rule system |

The lineage shows Solve evolving through new domains (spatial, temporal, systemic, meta-rule) while the underlying verb remains: reason about state, select transformation.

### G.3 Watch Lineage

| Year | Game | Innovation |
|---|---|---|
| 1970 | Conway's Game of Life | Autonomous cellular behavior from initial conditions (not a game, but the conceptual origin) |
| 1985 | Little Computer People | First commercial Watch — one autonomous person |
| 1991 | SimAnt | Watch at colony scale — pheromone-influenced autonomous swarm |
| 1996 | Creatures | Watch with genetic neural networks — agents that learn |
| 1996 | Tamagotchi | Watch miniaturized — one creature on a keychain |
| 2000 | The Sims | Watch at household scale — multiple agents with needs and relationships |
| 2001 | Animal Crossing | Watch with real-time clock — agents live when the player is absent |
| 2004 | Football Manager | Watch applied to competition — match simulation from tactical input |
| 2006 | Dwarf Fortress | Watch at maximum depth — 150-dimension agents in a coupled world simulation |
| 2013 | RimWorld | Watch accessible — deep enough for stories, visible enough to understand |
| 2018 | Frostpunk | Watch with moral weight — policy decisions judged by agent response |

The lineage shows Watch evolving through agent depth, agent count, and system coupling. Each generation increases how much internal state the agents carry and how many systems interact to produce emergent behavior. The unsolved problem across the entire lineage is sustained novelty from agent behavior — every game either exhausts through shallow agents, hides depth behind bad UI, or substitutes authored events for emergent behavior.

---

## Appendix H: The Satisfaction Spectrum

Each verb produces satisfaction along a different psychological axis. These axes do not overlap.

| Verb | Psychological Axis | Peak Expression | Closest Non-Game Analogue |
|---|---|---|---|
| Shoot | Competence — "I can do this" | Tournament victory through physical mastery | Athletic competition |
| Solve | Comprehension — "I understand this" | Elegant solution to a complex problem | Mathematical proof, engineering design |
| Watch | Discovery — "I witnessed this" | Emergent event that surprises and is traceable to conditions shaped | Gardening, parenting, scientific observation |

### H.1 Why These Satisfactions Do Not Substitute

A player seeking Shoot satisfaction (competence, mastery, flow) will not be satisfied by a Watch game, regardless of the Watch quality. The Watch game does not test the player's body. The competence axis is unaddressed.

A player seeking Solve satisfaction (comprehension, optimization) will not be satisfied by a Shoot game, regardless of the Shoot quality. The Shoot game does not test the player's reasoning about the system. The comprehension axis is unaddressed.

A player seeking Watch satisfaction (discovery, emergence, attachment) will not be satisfied by either Shoot or Solve alone. Neither verb produces autonomous behavior that surprises the player from inside the system.

This explains why genre preferences are stable across a player's lifetime. A player who prefers Shoot at age 15 generally prefers Shoot at age 35. The satisfaction axis is a preference, not a skill that develops toward a "higher" verb. No verb is more sophisticated than any other. They address different human capacities.

### H.2 Why Hybrids Expand the Audience

A Shoot+Solve game (Halo, Dark Souls) addresses two satisfaction axes simultaneously. The player who wants motor mastery AND strategic comprehension finds both in one game. This explains why Shoot+Solve is the largest commercial category — it serves the widest band of the satisfaction spectrum from a single product.

Solve+Watch (colony sims, management games, life sims) addresses a different pair. The player who wants strategic comprehension AND emergent discovery finds both. This audience is smaller than Shoot+Solve but deeply loyal — colony sim players measure engagement in thousands of hours.

Shoot+Solve+Watch (open-world RPGs) attempts to address all three axes. The commercial success of Skyrim, GTA V, and RDR2 reflects the breadth of the audience this reaches. The weakness of all three games' Watch component reflects the difficulty of delivering Watch alongside the other two verbs — the Watch is the most expensive to build and the first to exhaust.

---

## Appendix I: Edge Cases and Rulings

| Game | Apparent Verb | Actual Verb | Reasoning |
|---|---|---|---|
| Tetris | Shoot (time pressure, fast input) | Solve | The skill is pattern recognition and placement. A player who sees the correct placement instantly but inputs slowly beats a fast player who places poorly. Motor speed is secondary to cognitive recognition. |
| XCOM | Shoot (soldiers fire weapons) | Solve | Turn-based. No motor skill tested. The player selects actions. The dice resolve outcomes. The player's reasoning about positioning and probability determines success. |
| Auto-battlers (TFT, Dota Underlords) | Watch (fight plays out) | Solve + Watch | Composition selection is Solve. Fight is Watch. The player reasons about which units to buy and where to place them (Solve), then watches the fight resolve (Watch). |
| Tower defense | Watch (enemies walk, towers fire) | Solve + Watch | Tower placement is Solve. Wave resolution is Watch. |
| Idle/incremental games | Watch (numbers go up) | Solve + Watch | Upgrade path selection is Solve (which upgrade gives the best return). Number growth is Watch (observe the rate change from the decision). |
| Walking simulators (Gone Home, Firewatch) | Watch (explore, observe) | Solve (degenerate) | No autonomous agents. The player searches a static environment for content nodes. The "puzzle" is navigation — find the next diary entry. Degenerate Solve where the state transformation is the player's own knowledge. |
| Visual novels | Watch (read story) | Solve (degenerate) | Branch selection is reasoning about which option produces the desired outcome. Between branches, the player reads authored content (not a game verb — consumption). |
| Sandbox creative (Minecraft Creative, Mario Maker) | None | Tool use (not a game verb) | No objective, no agents, no test. The player creates artifacts that are then played through other verbs by other players (or the same player switching modes). Creation is a tool mode, not a gameplay verb. |
| Poker | Solve (hidden information) | Solve | Bet sizing, hand reading, position play, bluffing are all reasoning about hidden state and opponent modeling. No motor skill. No autonomous agents. |
| Sports games (FIFA, Madden) | Shoot | Shoot | Direct player control, real-time motor input for passing, shooting, tackling. Despite the "team" context, the player controls one character or issues real-time commands through motor input. |
| Real-time with pause (Baldur's Gate 1, Pillars of Eternity) | Shoot + Solve | Solve | Pause removes the motor skill test. The player reasons about positioning and ability use, then unpauses to observe. The "real-time" element adds urgency to Solve decisions but does not test motor skill because pause is always available. |

---

## Appendix J: Why There Is No Fourth Verb

Four candidates for a fourth verb were considered and rejected.

| Candidate | Description | Ruling | Reason |
|---|---|---|---|
| Read / Absorb | Consuming authored content (dialogue, lore, cutscenes) | Not a game verb | Consumption is passive reception, not interaction. Every game contains authored content between interactions. The content is the context for the verbs, not a verb itself. A book is not a game. |
| Create / Express | Building with no objective (Minecraft Creative, Mario Maker editor) | Tool use, not gameplay | Creation produces artifacts. Artifacts are consumed through the three verbs by players (including the creator switching to play mode). The creation itself has no feedback loop — no success, no failure, no score. It is a tool mode. |
| Trade / Negotiate | Social interaction with other humans (Diplomacy, Catan, poker) | Solve applied to humans | The player reasons about hidden state (opponent's hand, opponent's goals, opponent's bluff) and selects an action (bet, offer, accept, reject). The reasoning target is a human rather than a game system, but the cognitive activity is identical to any other Solve instance. |
| Perform / Express | Reproducing a pattern (Dance Dance Revolution, karaoke) | Shoot applied to a pattern | The player's body executes a motor sequence under time pressure. The target is a rhythm pattern rather than a spatial enemy, but the skill tested is motor execution and timing — identical to Shoot. |

The three verbs are irreducible because they correspond to three distinct human capacities applied to a system: motor action (Shoot), cognitive reasoning (Solve), and systemic observation (Watch). No other human capacity applied to a game system produces a distinct interaction type that is not a variant of one of these three.

