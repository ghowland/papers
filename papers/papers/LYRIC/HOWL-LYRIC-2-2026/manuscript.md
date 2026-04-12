# The Lyric Engine II
## A Systematic Method for LLM-Assisted Song Refinement from Existing Draft Material

**Registry:** [@HOWL-LYRIC-2-2026]

**Series Path:** [@HOWL-DISC-1-2026] → [@HOWL-LYRIC-1-2026] → [@HOWL-LYRIC-2-2026]

**DOI:** 10.5281/zenodo.19528593

**Date:** March 30 2026

**Domain:** Applied Methodology / AI-Assisted Creative Production

**Status:** Complete

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections and one biographical note were edited by the author. All paper content was LLM-generated using Anthropic's Claude 4.5 Sonnet. 

---

## I. ABSTRACT

This paper documents a systematic method for refining existing song drafts using LLM collaboration. LYRIC-1 documented creation from dense source material. LYRIC-2 documents refinement from existing drafts — human-written, LLM-written, or hybrid. The method was developed through the refinement of three albums: Culture (9 tracks, LLM-written from source papers), Obvious (20 tracks, LLM-written from research corpus), and Dragon's Dice (14 tracks, 6 human-written + 8 LLM-written rock opera).

The primary finding: the LLM's most valuable refinement skill is knowing what to keep. The primary failure mode: adding material that isn't in the draft. The method produces consistent results at 85-90% quality, with the remaining 10-15% requiring human final pass for embodied experience, invented language, gap-shaping, and physical plausibility that the LLM cannot provide.

Twelve new rules (41-52) were derived from specific failures observed during refinement. Six narrative album rules were derived from the Dragon's Dice production. Each rule is the scar tissue of a specific mistake — a character voice flattened, an object that teleported, a bridge that ran twenty lines when eight would hit harder, a vampire who sounded like a supportive girlfriend instead of a predator who loves her prey.

The rule set remains open. Every refinement cycle will generate new failures the current rules don't catch.

---

## II. THE PROBLEM LYRIC-2 SOLVES

LYRIC-1 starts from source material and builds songs. But many practitioners already have songs — rough drafts, LLM first passes, half-finished lyrics, demo recordings with placeholder words. These existing drafts contain structural strengths (emotional arcs, character voices, narrative progressions) alongside consistent weaknesses (object agency, voice flattening, physical impossibility, over-articulation).

The refinement problem is different from the creation problem. Creation asks "what should this song be?" Refinement asks "what is this song already, and what's preventing it from working?"

The draft already contains the song. The refinement reveals it.

---

## III. THE REFINEMENT METHOD

### III.I Assessment

Before changing a single word, review the entire draft against the full rule set (LYRIC-1 Rules 1-40 plus LYRIC-2 Rules 41-52). Identify what works and what doesn't. The assessment produces four categories:

**Keep** — lines, verses, or sections that are already at maximum compression or carry the song's emotional payload. These are untouchable. The discipline is recognizing them and not rewriting them to prove contribution. The best lines in an LLM draft are often already there — buried under scaffolding the LLM built to reach them. The revision process is archaeological: remove what's covering the good lines.

**Fix** — lines with identifiable rule violations that can be corrected without restructuring. Object agency, ban-list words, filler words reaching for rhymes, physically impossible actions, voice flattening. Each fix is targeted — change the minimum necessary.

**Cut** — scaffolding the draft built to reach its good lines. Philosophical passages that restate what scenes already show. Explanations of emotions that are visible in actions. Verses that repeat the thesis of the previous verse in different words. The cut material isn't bad — it's unnecessary. The good lines don't need the scaffolding once the song is tightened.

**Add** — structural elements missing from the draft. A mid-song chorus for pacing. A physical moment showing an object transfer. A callback to an earlier track. Additions must be justified by structural necessity, not by the LLM's desire to contribute. This should be the smallest category.

### III.II The Refinement Ratio

Across the eight tracks rewritten in the Dragon's Dice album, the average intervention was:

| Category | Percentage |
|---|---|
| Keep | 80-85% |
| Fix | 5-10% |
| Cut | 5-10% |
| Add | 0-5% |

The ratio tells the story: refinement is mostly preservation. The LLM's most common error during refinement is changing too much. The draft already contains the song. The refinement reveals it by removing what obscures it.

### III.III The Two-Phase Boundary

Same as LYRIC-1. Phase 1 is the plan — assessment, identification of keep/fix/cut/add, anchor table for any new sections, object inventory for narrative albums. Phase 2 is the rewrite. The boundary is hard. No lyrics are changed until the plan is reviewed and approved by the human practitioner.

The plan catches problems the rewrite would bury. Object continuity errors, wrong character voices, scenes that don't physically make sense, structural pacing issues — all of these are visible in the plan and invisible once the LLM starts generating lyrics. The planning phase is where most of the value is created. The writing phase is execution.

### III.IV Kill Discipline in Refinement

LYRIC-1's kill discipline applies to metaphors: if the metaphor doesn't work after five cycles, kill it. LYRIC-2 adds refinement-specific kill discipline: if a section can't be fixed without rewriting more than 50% of its lines, the section needs replanning, not refinement. The plan should identify this before the rewrite begins.

---

## IV. NEW RULES (41-52)

Each rule derived from a specific failure observed during the refinement process.

### IV.I Word and Concept Level

**Rule 41 — Ban word: "game."** Generic strategic container. LLMs reach for "game" to describe any competitive, strategic, or changed situation. "Playing a different game," "that's the game," "the game has changed." Banned. Name the specific activity, competition, or stakes. A brute cages or doesn't cage. A thief steals or doesn't steal. Nobody "plays a game."

### IV.II Character Level

**Rule 42 — The unreliable narrator is a valid structural choice.** When the narrator is wrong, the listener's disagreement creates the meaning. The narrator's incorrectness must be consistent with their established character and visible to the listener through the gap between what the narrator describes and what the description reveals. The narrator never winks at the audience. The gap is the audience's to find.

Derived from: Dragon's Dice Tracks 1-6, where every character is an unreliable narrator who believes they're justified. The Mage describes kidnapping as romance. The Brute describes coercion as efficiency. The Elf describes incompetence as heroism. The listener receives more information than the narrator provides because the narrator's blind spots are visible in what they describe without recognizing.

**Rule 43 — Listener-completed compression (provisional).** Leaving deliberate gaps the listener fills. The song provides the syntax, the listener provides the content. Distinct from metaphor compression (LYRIC-1) where the songwriter encodes the depth. In listener-completed compression, the listener encodes the depth.

The risk for LLMs: filling gaps that should be left empty (projecting cognition — "the napkin knows"), or leaving gaps with no shape (the listener can't decompress). The test: does the gap have a specific shape that a human listener would fill with their own experience? If yes, leave it. If the shape is ambiguous or the LLM would fill it with projected cognition, name the banana instead.

Provisional because the LLM must demonstrate it can shape gaps correctly before this rule is confirmed. Observed in human-written songs (Smerph You, Sell Out, Werewolves Are Just Misunderstood) but not yet successfully replicated by the LLM.

**Rule 44 — Commit to the bit.** Serious or comedic, the premise is entered and never exited. No winking at the audience. No explaining the premise. No origin story unless the origin IS the song. The commitment is the containment. If the internal logic is consistent, the absence of explanation is stronger than any explanation.

Derived from: human-written songs where committed absurdity needed no justification (Unicorn Horns Were Made For Stabbing, Robots and Ninjas, Dolphins Don't Pay Rent). The audience accepts the universe because the physics are internally consistent, not because the songwriter justified the premise.

### IV.III Physical Level

**Rule 45 — Objects move through physically possible actions.** Every object transfer, state change, and interaction must pass the physical plausibility test: could this happen in the physical world the song inhabits? If not, the action is wrong regardless of how well the line reads.

Social manipulation (accepting something handed to you) is smarter and more physically plausible than mechanical manipulation (pickpocketing a six-foot staff from a belt). A manipulator doesn't steal — he gets handed things.

Derived from: Dragon's Dice Track 10, where the Druid's acquisition of the Ring and Staff went through three drafts before the mechanics were physically possible and narratively clean. The final version: the Priestess hands the Druid her staff voluntarily (trust), the Thief holds out the ring to prove innocence and the Druid closes his hand around it (honesty weaponized). Both transfers are voluntary. Neither is physically impossible.

**Rule 46 — Object verbs match object behavior.** Extension of Rule 36 (verbs match the trade) to all objects. Trains run, arrive, come through — they don't land. Planes land. Ships dock. Horses walk. Rivers flow, press, erode — they don't speak or remember. Napkins show what's written, absorb water — they don't know things. The verb set is fixed by the object's nature. All other verbs are projected cognition.

Derived from: "the trains already land" (Obvious album, Flat Track), "the napkin knows" (Obvious album, What If?), "the territory gets his ink" (Culture album, The Map).

### IV.IV Refinement Discipline

**Rule 47 — Don't add what isn't in the material.** The LLM's strongest refinement failure is inventing motivation, emotional tone, or psychological framework that the draft doesn't evidence. If the draft shows the Dragon as accurate, the refinement doesn't add contempt. If the draft shows the Thief as fully in love, the refinement doesn't add guardedness. If the draft shows the Priestess as an archetype, the refinement doesn't add relatable insecurities. Every addition must be evidenced by the existing draft.

Derived from: multiple corrections across Dragon's Dice refinement. The Dragon was given contempt that wasn't in the material. The Thief was given emotional guardedness that contradicted his established behavior. The Brute's cage-petting was reinterpreted through a psychological framework that missed the actual image. Each correction was the human saying "that's not in the material, you added it."

**Rule 48 — Compression serves every song, especially finales and climaxes.** Twenty-line bridges should be eight. Sixteen-line verses should be ten. The LLM's instinct is to expand — more explanation, more philosophy, more scaffolding. The refinement instinct should be to compress.

The test: does this line carry weight the previous line didn't? If no, cut. Does this passage restate what the scene already showed? If yes, cut. If the abstract line is removed, does the specific scene still carry the meaning? If yes, the abstract line is scaffolding.

Derived from: Dragon's Dice Track 14, where dual bridges of twenty lines were compressed to eight without losing any content. Track 9, where the Dragon's verses were shortened and every cut made the wound-lines land harder. Cutting was the primary upgrade tool for LLM output across every track.

**Rule 49 — Specificity over abstraction in every case.** "Reminded me of everything" is vague. "Reminded me of her eyes" is specific, physical, and opens a rhyme chain (eyes/lies/dies). One emerald held to light carries more than a paragraph about "everything."

The test: can you see the specific thing? Can you hold it, touch it, hear it? If the image is something you can see, it's specific. If it's something you can only think, it's abstract. Choose the thing you can see.

Derived from: Dragon's Dice Track 14 correction. The single word change from "everything" to "her eyes" transformed a vague philosophical passage into a physical moment that opened a rhyme chain and carried the same emotional weight in fewer words.

**Rule 50 — The LLM must not flatten character voices to a single register.** Every character drifts toward the same moderate, articulate, self-aware register during LLM refinement. A vampire expresses love through predation ("Where else would I go, love? You're my food"). A brute expresses tenderness through the apparatus of containment (petting the cage, not the rabbit). A dragon expresses accuracy through inhuman scale (measuring in thousands, not decades). A priestess maintains elevation (she suffers the company of fools, she doesn't commiserate with them).

The LLM's instinct is to make every character sound like a thoughtful person having a therapy session. The refinement must push each character back to their extreme.

Derived from: Dragon's Dice Track 13 (vampiress dialogue), Track 9 (dragon voice), Track 8 (priestess register), and Culture album review (dragon/napkin equivalence observation).

**Rule 51 — Filler words to reach a rhyme are always wrong.** "Today," "somehow," "everything" used to pad a line to its rhyme target carry no meaning. If the line needs a word that carries no weight just to land the rhyme, the anchor is wrong or the line needs rebuilding. Every word load-bearing (Rule 8) applies to the rhyme-reaching position most of all, because that's where the LLM is most likely to insert filler.

Derived from: Dragon's Dice Track 10, "I'll hold him still today" where "today" was filler replaced by "he won't get away" which carries the Brute's containment drive.

**Rule 52 — Round numbers are permitted when roundness carries meaning.** Exception to Rule 15. "One hundred years" for an elf works because the point is scale — a century old and treated as a child against a human lifespan of eighty. "A thousand quests" works because it communicates the Dragon's inhuman timescale. The test: is the number's purpose precision or scale? If precision, use the specific number (nine mouths, forty-five days, sixty-seven years). If scale, the round number carries the contrast.

Derived from: Dragon's Dice Track 4, where "one hundred" for the elf's age was flagged as a Rule 15 violation but correctly served as a scale marker against human lifespan.

---

## V. NARRATIVE ALBUM RULES

Rules specific to albums with recurring cast and connected narrative, derived from the Dragon's Dice refinement.

### V.I Object Inventory

For narrative albums, maintain a per-track object inventory in the plan. Every named object must have:

- **Current holder** — who has it right now
- **Acquisition** — how they got it (physical action, not teleportation)
- **Transfer point** — which track, which moment it changes hands
- **Transfer method** — voluntary handoff, theft, abandonment, destruction
- **Story/prop transition** — when it stops driving narrative and becomes set dressing

Objects that aren't tracked will be mentioned inconsistently, transferred through physically impossible actions, or disappear without explanation. The Dragon's Dice production required three drafts of Track 10 before the Ring and Staff transfers were physically plausible and narratively clean.

**The key principle:** after the climax, quest objects become props. They can appear to set scenes (the staff beside the throne) but they no longer drive narrative. The ring on the ground that nobody picks up is the transition from story element to prop. Continuing to track objects as story elements after the climax produces cluttered scenes and false plot threads.

### V.II Character Voice Tracking

Each character in a recurring cast has:

- **Vocabulary set** — the words their world provides (academic for the Mage, transactional for the Brute, chivalric for the Knight, elevated for the Priestess, proximity for the Thief, patience for the Druid)
- **Refrain or verbal tic** — the repeated phrase that defines them (Magic Missile, "for what it's worth," "for great justice," "my cages are empty")
- **Verb discipline** — what actions they perform, consistent with their nature
- **Register** — their position relative to other characters (above, blunt, verbose, quiet, elevated, controlled)

These must be established in the character's introduction and maintained across every subsequent appearance. The LLM's tendency is to flatten all characters to the same register by the climax. Voice tracking prevents this.

### V.III Refrain Degradation

A recurring phrase can arc across an album. The degradation IS the character arc. The phrase doesn't change. The context around it does. The same words carry different weight each time they appear.

**Example — "I cast Magic Missile" across Dragon's Dice:**

| Track | Context | Function |
|---|---|---|
| 1 | Blasting brute, knight, vampire | Weapon, omnipotent solution |
| 7 | "At this whole debate!" | Social weapon, absurd escalation |
| 8 | At a bird, a cloud, the Thief | Petty grievance, comic escalation |
| 10 | "It's not working, nothing's working—" | Complete failure at the ultimate moment |
| 13 | "At my pride / It doesn't work, but at least I tried" | Turned inward, failing, accepted |
| 13 outro | "At the pain / It doesn't work, it never will / But I'm still here" | Final cast. Impotent. He stays anyway. |

The spell degrades from omnipotent to impotent. The impotence is where the character finds something real. When the spell stops working, he's left with just sitting next to someone. That's enough.

### V.IV Genre as Character Psychology

In narrative albums, the style tag for each track can express the character's internal state rather than the album's energy oscillation (LYRIC-1's heartbeat principle). The genre IS the character's self-image or emotional state. The mismatch between genre and content creates dramatic irony the listener feels but can't articulate.

| Character | Genre | Function |
|---|---|---|
| Mage | Power metal, 140 BPM | Chaos, delusion, comedy — he thinks he's in an epic |
| Thief | Romantic folk rock, 95 BPM | Yearning, sincerity, the trap of softness |
| Brute | Dark southern rock, 85 BPM | Hollow obsession, grinding emptiness |
| Knight | Bright indie folk, 110 BPM | Naive optimism, doomed hope — the listener hears doom before the Knight does |
| Druid | Atmospheric dark folk, 70 BPM | Patience, hidden curse, slow revelation |
| Druid (villain) | Sinister cabaret, 100 BPM | Control, satisfaction, the spider at center |

The BPM progression follows character psychology, not heartbeat oscillation. Each track's tempo is its character's internal clock.

### V.V Retroactive Dual Layer

A later track can add a depth layer to earlier tracks retroactively. The villain's song recontextualizes every previous song — the Thief's romance was engineered, the Brute's partnership was manufactured, the Knight's quest was posted by the Druid. The listener replays earlier songs and hears strings that weren't visible on first listen.

This is distinct from LYRIC-1's dual layer, where both layers exist simultaneously in every line. Retroactive dual layer is sequential — the depth is added backward by a later track. The earlier songs are complete on first listen. The later track makes them more complete.

### V.VI Post-Climax Character Resolution

After the climax, characters don't transform — they crack. The change is measured in degrees, not revolutions.

| Character | Degree of Change | Physical Expression |
|---|---|---|
| Brute | One cage left open | A question mark, not freedom |
| Mage | Sits beside the vampiress | Doesn't cast, doesn't save, just sits |
| Knight | Takes off the armor | Not forever — just to see |
| Thief | Returns to stealing | But won't take things that remind him of her |
| Priestess | Wears the crown | Carries the lie, lets the Thief carry the truth |

Nobody is fixed. Nobody is redeemed. They're the same people with one degree of difference. The degree is the story.

---

## VI. LLM FAILURE MODES IN REFINEMENT

Comprehensive list, each observed during the three-album refinement process.

| Failure Mode | How It Manifests | Which Rule Catches It | Frequency |
|---|---|---|---|
| Over-articulation | Characters explain feelings instead of acting them | Rule 48, Rule 9 | Every album, every track |
| Voice flattening | All characters sound thoughtful-articulate-moderate | Rule 50 | Every album, climax tracks worst |
| Object agency | Objects know, want, decide, remember | Rules 21, 46 | Every album, every draft |
| Physical impossibility | Staff slipped from belt, trains landing | Rule 45 | Narrative albums especially |
| Adding unmotivated psychology | Dragon is contemptuous, Thief is guarded | Rule 47 | Consistent in planning phase |
| Filler for rhyme | "Today," "everything" as padding | Rule 51 | Every draft |
| Expanding what should compress | Twenty-line bridges, sixteen-line verses | Rule 48 | Finales and climaxes |
| Protecting characters from extremes | Softening vampires, guarding lovers, moderating archetypes | Rule 50 | Consistent |
| Object continuity loss | Ring appears and disappears, staff untracked | V.I | Narrative albums |
| Equalizing intelligence registers | Dragon sounds like grandmother sounds like napkin | Rule 50 | Consistent |
| Rewriting what already works | Changing 85% when 15% needed fixing | III.II | First pass of every refinement |
| Generic strategic language | "Playing a different game" | Rule 41 | Consistent |
| Over-unifying | Pattern-matching songs separated by 15 years as "in conversation" | Rule 47 | Assessment phase |
| Gradualizing love | Making romance measured and protected when humans fall immediately | Rule 47, Rule 50 | Character refinement |
| Expanding scenes that should connect and move | Adding a sword drawn on a stuck cart | Rule 48 | Narrative refinement |
| Psychologizing when action is sufficient | Adding internal motivation to characters whose actions are self-explanatory | Rule 47 | Consistent |

### Failure Mode by Refinement Phase

| Phase | Most Common Failures |
|---|---|
| Assessment | Over-unifying, adding unmotivated psychology, misreading character dynamics |
| Planning | Object continuity gaps, expanding structure beyond what the song needs |
| First rewrite | Rewriting what already works, voice flattening, filler for rhyme |
| Second rewrite | New agency violations introduced while fixing old ones, over-articulation in added sections |
| Final pass | Minor line-level issues — one filler word, one borderline agency, one voice drift |

---

## VII. COMPARATIVE ANALYSIS: HUMAN VS LLM WRITING

Derived from reviewing eight human-written songs alongside LLM-written albums.

### What Human Writing Does That LLM Writing Cannot

**Invents language.** "Shooty" (Pirates), "cajun" as double-register portmanteau for "caged one" (My Cages Are Empty). The human creates words when existing words don't carry the meaning. The LLM selects from existing vocabulary. Not a rule — a capability boundary. The LLM should not attempt invented words (they will be wrong) but should recognize them in human drafts and preserve them.

**Deliberate misregistration.** Using a word from the wrong register so the listener misreads first and corrects later. "Cajun" reads as Louisiana on first pass and as "caged person" on second. The misreading is load-bearing. The LLM would either explain the double meaning or avoid the ambiguity.

**Writes from inside wrong characters.** The dolphin rent enforcer, the werewolf boyfriend, the aspiring sellout. The LLM-method songs (Culture, Obvious) write from inside right characters — practitioners, observers, builders. The wrong-character perspective generates meaning through the listener's disagreement with the narrator.

**Lets structure be messy when messiness IS the character.** Pirates has inconsistent line lengths because the pirate is rambling. Kill Bots has prose paragraphs because the kid is breathless. Structural looseness that produces character voice. The LLM defaults to structural discipline, which produces clean songs but not character mess.

**Leaves correctly-shaped gaps.** Smerph You outsources its entire vocabulary to the listener. The fight scene in Pirates is skipped entirely. The human trusts the listener to complete the song. The LLM tends to complete the song for the listener, or leaves gaps with no shape.

**Exploits power dynamics.** Love is asymmetric — one person is gone while the other holds the cards. The Thief is lost the moment he sees the Priestess. She holds the cards. The LLM equalizes relationships because equal feels fair. Human relationships aren't fair.

### What LLM Writing Does That Human Writing Benefits From

**Structural discipline.** Four-line verses, consistent rhyme architecture, anchor-first planning. The human songs are structurally loose — sometimes brilliantly, sometimes to their detriment. The LLM provides a framework the human can loosen intentionally.

**Dual-layer encoding.** The Culture album's every line works on two simultaneous levels. The human songs mostly work on one level (with exceptions like Werewolves and Sell Out that approach dual-layer naturally).

**Sensory signature planning.** Identifying the dominant sense before writing. The human songs use whatever sense is available. The LLM assigns and maintains a sensory through-line.

**Ban-list discipline.** The human voice is distinctive enough to carry generic words. The LLM voice isn't — without the ban list, it defaults to room/door/wall/chain/bone vocabulary.

**Source compression.** Turning tech docs and research papers into songs. The human songs compress experience and imagination. The LLM songs compress source documents. Different inputs, same method.

### The Core Difference

The LLM builds outward from specificity: names the banana, describes the scene, encodes the depth, delivers the completed signal. The human builds inward from shape: provides a correctly-shaped absence and the listener fills it with their own experience. Both produce songs. The human method produces songs that are different for every listener. The LLM method produces songs that are the same for every listener but carry a hidden layer for informed listeners.

Neither method is superior. They are different tools for different source material and different purposes.

---

## VIII. THE REFINEMENT CEILING

The method produces consistent results at 85-90% quality. The remaining 10-15% requires human final pass for capabilities the LLM does not possess:

**Embodied experience.** The LLM has never pushed a cart, held emeralds to light, felt yarn tension between two fingers, or sat in a tavern at last call. Physical plausibility can be checked against rules, but physical resonance — the feeling of a scene that only comes from having been a body in the world — cannot be generated.

**Invented language.** Words that don't exist yet but that a character would create under pressure. Human-only technique. The LLM should preserve invented words in human drafts but should not attempt to create them.

**Gap-shaping.** Leaving correctly-shaped absences the listener fills. The LLM tends to fill gaps (projected cognition) or leave gaps with no shape (the listener can't decompress). Rule 43 is provisional until the LLM demonstrates this capability.

**Power dynamics.** Love, authority, respect, fear — all asymmetric in human experience. The LLM equalizes relationships by default. The human practitioner must establish the asymmetry and the LLM must maintain it during refinement rather than correcting it toward balance.

**Misregistration.** Deliberate use of wrong-register words where the listener's misreading is the delivery mechanism. Requires knowing what the listener will assume and being wrong on purpose. The LLM would clarify rather than exploit the ambiguity.

These are the capabilities the human final pass provides. The method does not claim to replace them. The method claims to make them the only things left to do.

---

## IX. PROCESS LESSONS

### IX.I From Culture Album Review

Object agency is the LLM's strongest gravitational pull. It appeared in every track, in every draft, and most persistently in the chorus — the line the listener hears most often. New rule: the chorus line gets the strictest object-agency check.

The ban-list needs contextual exceptions documented. When the banned word IS the thesis (The Window's wall, Threshold's door), the ban may be overridden, but the override must be named and justified in the plan, not discovered during review.

### IX.II From Obvious Album Review

An album of twenty tracks risks losing the listener in volume. But each track must do something different — no two practitioners sharing a domain, no two theses identical. The sequencing does structural work: the heartbeat principle, the genre contrast, the energy oscillation. Move any track and the argument breaks.

Tracks that break structural rules (free verse, no chorus, concept-heavy bridges) can work as album closers if earned by the preceding tracks. But they fail as standalone songs and should be evaluated in album context, not in isolation. Two such tracks were removed from the Obvious album (The Prompt, The Bench) because they broke too many rules and the album didn't need them.

### IX.III From Dragon's Dice Refinement

**The planning phase is where most value is created.** The writing phase is execution. Every structural problem — object continuity, character voice, physical plausibility, pacing — is visible in the plan and invisible once lyrics are being generated.

**Keep what works.** The average refinement preserved 80-85% of the original. The hardest discipline is not rewriting lines that are already right. A rewrite that changes everything is not better — it's just different. Targeted work only.

**Cutting is the primary upgrade tool.** The Dragon's verses got shorter and sounded more ancient. The bridges got shorter and hit harder. The philosophical passages were scaffolding around scenes that already carried the meaning. Almost every improvement came from removing lines, not adding or changing them.

**A mid-song chorus solves pacing without changing content.** Six consecutive character verses with no musical release is a slog regardless of quality. The chorus is a structural breather — it doesn't advance the plot, it states the situation. The listener lands, reorients, continues.

**Climax songs follow dramatic structure, not musical structure.** No chorus, no consistent rhyme scheme, no four-line verses. The architecture is the arc of the event, not the pattern of verse-chorus-verse. Climax songs earn their structural freedom by being the payoff of multiple tracks of setup.

**Social manipulation is smarter than mechanical manipulation.** A manipulator doesn't steal — he gets handed things. The Priestess gives the Druid her staff. The Thief holds out the ring to prove innocence. Both transfers voluntary. Both physically plausible. Both devastating.

**One degree of change is more honest than transformation.** Characters who crack by one degree (one cage open, one seat taken, one piece of armor removed) are more believable than characters who transform. Nobody is fixed. The degree is the story.

---

## X. VALIDATION

**Culture album:** Nine tracks reviewed against 40 rules. Consistent violations identified. Object agency in every track. Ban-list words in 6/9. Chorus lines carried the worst agency violations. All nine tracks assessed as "good enough" — violations were minor and fixable by human final pass.

**Obvious album:** Twenty tracks reviewed. Two tracks removed from album sequence (The Prompt, The Bench) for excessive structural rule-breaking and redundancy. Persistent object agency confirmed across all tracks. Ban-list dependency identified in The Window and Threshold. Eighteen tracks assessed as "good enough." The album arc — fairy tale through specific practitioners to celebration — validated as structurally sound.

**Dragon's Dice album:** Eight tracks rewritten from LLM drafts. All eight reached "good enough for human handoff" within one planning cycle and one writing cycle each. Twelve new rules (41-52) derived from specific failures. Object inventory and character voice tracking methods developed and validated. Refinement ratio confirmed: 80-85% keep, 5-10% fix, 5-10% cut, 0-5% add.

**Human-written songs:** Eight songs reviewed. Five human-only techniques identified that the LLM cannot replicate (invented language, deliberate misregistration, wrong-character perspective, structural messiness as character voice, correctly-shaped gaps). Four techniques identified that the method should incorporate (unreliable narrators, genre as dramatic irony, escalation as structure, committed absurdity without explanation). Two became rules (Rule 42, Rule 44).

---

## XI. FALSIFICATION CRITERIA

**F1.** If the refinement method consistently degrades songs rather than improving them, the assessment framework is wrong.

**F2.** If the 80-85% keep ratio doesn't hold across different source material, the method is over-fitting to the three albums studied.

**F3.** If human practitioners consistently reject "good enough" assessments, the quality threshold is miscalibrated.

**F4.** If the new rules (41-52) eliminate distinctiveness the way LYRIC-1's F3 warns about, the rule set is over-constraining.

**F5.** If the narrative album rules don't transfer to other narrative albums, they're specific to Dragon's Dice rather than general.

**F6.** If the LLM successfully demonstrates gap-shaping (Rule 43), the provisional status should be removed and the technique documented. If it consistently fails, Rule 43 should be downgraded to a human-only technique catalog entry.

---

## APPENDIX A: UPDATED BAN LIST

### Words (LYRIC-1 + LYRIC-2 additions)

| Word | Reason | Exception |
|---|---|---|
| room | Generic container | Literal physical room in scene |
| floor | Generic surface | Literal ground contact |
| wall | Barrier concept | Never (unless the wall IS the thesis — must be named in plan) |
| door | Access concept | Literal door in specific scene |
| key | Access mechanism | Never (unless character is a thief — domain vocabulary) |
| lock | Access mechanism | Never (unless character is a thief — domain vocabulary) |
| building | Generic structure | Never |
| halls | Institutional space | Never |
| parameters | Technical jargon | Intentional bleed only (e.g., inspector's bureaucratic speech) |
| window | Generic transparency | Once per cycle, must be literal |
| shade | Color substitute | Use actual color name |
| dispatch | Institutional process | Never |
| architecture | For non-buildings | Actual buildings only |
| complete | Abstract filler | Use specific physical state |
| settled/resolved | Institutional closure | Never (unless critiquing the word itself) |
| sign | Overuse risk | One per song maximum |
| bone/marrow | LLM "authentic" | Literal animal skeleton only |
| chain | LLM connection | Literal linked metal only |
| something/anything | Vague placeholder | Never — name the banana |
| game | Generic strategic container | Never — name the specific activity |

### Concepts (LYRIC-1 unchanged)

| Concept | Includes | Alternative |
|---|---|---|
| Barriers/containment | wall, fence, barrier, obstacle, partition | Show consequence through action |
| Access/entry | key, lock, gate, threshold, entrance | Show person turned away or walking through |
| Generic structure | room, building, foundation-as-metaphor | Name specific place with domain vocabulary |
| Generic authenticity | "in my bones," "deep inside," "at the core" | Show feeling through physical action |
| "Always there" abstractions | "the climbing's always there" | Name what's present — wind, yarn, forge heat |
| Generic strategy | "playing a different game," "changed the game" | Name the specific action, competition, stakes |

### Patterns (LYRIC-1 unchanged + additions)

| Pattern | Example | Alternative |
|---|---|---|
| "Not X, it's Y" | "It's not the stamp, it's the shoe" | Show both through action |
| "Same X, same Y, different Z" | "Same thread, same window, different light" | Show two experiences as separate scenes |
| "They" as vague antagonist | "They said it was complex" | Name specific character |
| Direct address as attack | "Hey Dr. X, your Y doesn't Z" | Observe mechanism |
| Triple pointing | "That's the X, that's the Y, that's the Z" | Pick strongest, cut others |
| Repeated adjacent anchors | "apart" then "apart" next line | Unique anchor per line |

---

## APPENDIX B: COMPLETE RULES LIST (1-52)

### LYRIC-1 Rules (1-40)

1. Ban-list words
2. Ban-list concepts — semantic role banned, synonyms carry ban
3. No generic rhyme pairs
4. No vague antagonist "they"
5. Name the banana — no vague placeholders
6. Lines fit in a mouth — tempo-calibrated ceiling
7. Line length variation is musical
8. Every word load-bearing
9. Scenes not concepts (the load-bearing rule)
10. Lines read as natural speech
11. Four lines per verse
12. Rhyme-last architecture — anchors first, intentional breaks once
13. Anchor words carry multiple meanings
14. No furniture verses — every verse has a stopping line
15. Round numbers are vague
16. Songs lie to expose truth
17. Complete metaphor containment
18. Domain bleed intentional or absent
19. Compression to earned length (2:30-4:00)
20. Each song has a sensory signature
21. Objects don't know things
22. Animals do what they actually do (Zootopia max)
23. No projected cognition
24. No "not X, it's Y"
25. No "same X, same Y, different Z"
26. No direct address as attack
27. Anger in content, not delivery
28. Emotional register matches position
29. Repetition is rotation
30. Withheld payoff detonates proportionally
31. Misdirect then deliver something better
32. Final delivery breaks the pattern
33. Trust the scene
34. Absent characters need a gesture
35. Cast the song like a film
36. Verbs match the trade
37. Parallel weakness needs a bridge
38. Ugly words don't sing
39. Alternate genders and character types
40. Metaphor must be accessible

### LYRIC-2 Rules (41-52)

41. Ban word: "game" — generic strategic container
42. Unreliable narrator as valid structural choice
43. Listener-completed compression (provisional)
44. Commit to the bit — no winking, no explaining
45. Objects move through physically possible actions
46. Object verbs match object behavior
47. Don't add what isn't in the material
48. Compression serves every song, especially finales and climaxes
49. Specificity over abstraction in every case
50. Don't flatten character voices to a single register
51. Filler words to reach a rhyme are always wrong
52. Round numbers permitted when roundness carries meaning

---

## APPENDIX C: OBJECT INVENTORY TEMPLATE

```
ALBUM: [title]

OBJECT: [name]
  Origin: [where it comes from]
  Track 1: [holder] — [how acquired]
  Track N: [holder] — [how transferred, physical action]
  Track N: [holder] — [how transferred, physical action]
  Story→Prop transition: Track [N] — [moment it stops driving narrative]
  Final location: [where it ends up]

OBJECT: [name]
  [repeat]
```

---

## APPENDIX D: CHARACTER VOICE TRACKING TEMPLATE

```
CHARACTER: [name]

  Role: [protagonist/antagonist/witness/absent]
  Vocabulary set: [domain words]
  Refrain: [repeated phrase, if any]
  Verbal tic: [habitual phrasing]
  Verb discipline: [what actions they perform]
  Register: [elevated/blunt/verbose/quiet/controlled/chaotic]
  
  Voice drift risk: [what the LLM will flatten them toward]
  Correction: [what to push them back toward]
  
  Arc across album:
    Introduction: [track, state]
    Midpoint: [track, state]
    Climax: [track, state]
    Resolution: [track, state]
```

---

## APPENDIX E: REFRAIN DEGRADATION ARC TEMPLATE

```
REFRAIN: [phrase]
CHARACTER: [name]

  Track [N]: [context] — [function: weapon/tool/identity/failure/acceptance]
  Track [N]: [context] — [function]
  Track [N]: [context] — [function]
  Track [N]: [context] — [function]
  
  Arc: [omnipotent → strained → failed → repurposed/accepted]
  Meaning at start: [what it means when first used]
  Meaning at end: [what it means when last used]
  The change: [what changed around the refrain while the refrain stayed the same]
```

---

## APPENDIX F: REFINEMENT ASSESSMENT TEMPLATE

```
TRACK: [number and title]
ALBUM: [title]
ASSESSMENT DATE: [date]

OVERALL: [percentage keep / fix / cut / add]

SECTION-BY-SECTION:

[Section name]
  Status: [keep / fix / cut / add]
  If fix: [specific rule violation, specific correction]
  If cut: [what it restates that another section already carries]
  If add: [structural justification]

[repeat per section]

OBJECT INVENTORY CHECK:
  [object]: [holder at start of track] → [holder at end] — [transfer plausible? Y/N]

CHARACTER VOICE CHECK:
  [character]: [voice consistent with introduction? Y/N] — [drift noted]

STRUCTURAL CHECK:
  Pacing: [does the song need a chorus added for breathing room?]
  Length: [earned or bloated?]
  Chorus rotation: [does meaning change between choruses?]
  
VERDICT: [good enough / needs targeted fixes / needs replanning]
```

---

## APPENDIX G: DRAGON'S DICE OBJECT MAP

| Track | Ring of Rage | Staff of Redemption | Dragon's Dice | Heart of an Elf |
|---|---|---|---|---|
| 1 | Exists (location unspecified) | Exists (with Druid) | With Dragon | In Knight's chest |
| 2 | Thief steals it | Thief steals from Druid, gives to Priestess | With Dragon | In Knight's chest |
| 3-6 | With Thief | With Priestess | With Dragon | In Knight's chest |
| 7-8 | With Thief (unmentioned) | With Priestess (unmentioned) | With Dragon | In Knight's chest |
| 9 | With Thief (Dragon sees it) | With Priestess | Dragon offers dice | Dragon names the heart |
| 10 | Thief produces it to prove innocence → Druid takes it | Priestess hands to Druid voluntarily | With Dragon | Druid isolates Knight to take it, can't |
| 11 | Druid uses it for unstable blast → falls to ground | With Druid (used in blast) | With dead Dragon | Knight keeps it (alive) |
| 12 | On ground in lair, abandoned | Unmentioned | Unmentioned | In Knight's chest |
| 13 | Gone | Unmentioned | Gone | In Knight's chest |
| 14 | Gone | Brought to Priestess as throne-room trophy | Gone | In Knight's chest |

---

## APPENDIX H: DRAGON'S DICE REFINEMENT DATA

| Track | Original Lines | Revised Lines | Keep % | Fix % | Cut % | Add % | Primary Fix |
|---|---|---|---|---|---|---|---|
| 7 Fellowship | ~45 | ~55 | 85 | 5 | 0 | 10 | Added mid-song chorus |
| 8 Journey | ~65 | ~70 | 85 | 5 | 0 | 10 | Rewrote V1 (stuck cart), added choruses |
| 9 Lair | ~80 | ~60 | 70 | 5 | 25 | 0 | Cut Dragon's verses shorter |
| 10 Betrayal | ~70 | ~65 | 75 | 15 | 5 | 5 | Object transfer mechanics |
| 11 One Hundred | ~85 | ~80 | 90 | 5 | 5 | 0 | Minimal — emotional architecture already right |
| 12 Would I Still | ~75 | ~75 | 95 | 5 | 0 | 0 | Near-zero intervention |
| 13 Homecoming | ~65 | ~65 | 80 | 10 | 5 | 5 | Vampiress dialogue, ban word fix |
| 14 Shadow/Throne | ~95 | ~65 | 65 | 5 | 30 | 0 | Major compression — bridges, verses |

### Observations

Songs closest to the emotional climax required the least intervention (Tracks 11, 12). Songs requiring the most intervention had structural problems (Track 10's object mechanics) or length problems (Track 14's uncompressed bridges). The correlation is direct: emotional truth survives LLM drafting better than structural mechanics. The LLM gets feelings more right than physics.

---

## APPENDIX I: HUMAN TECHNIQUE CATALOG

Techniques identified from human-written songs that the LLM cannot replicate. Documented for practitioner awareness — the human final pass is where these live.

| Technique | Example | Why LLM Can't Replicate |
|---|---|---|
| Invented language | "Shooty" (Pirates), "cajun" (Cages) | Requires real-world cultural knowledge exploited through deliberate wrongness |
| Deliberate misregistration | "Cajun" reading as Louisiana then as "caged one" | Requires knowing what the listener will assume and being wrong on purpose |
| Substitution compression | Smerph You — every "smurf" is a listener-completed blank | Requires trusting the listener to supply profanity the song never contains |
| Structural mess as character | Pirates' inconsistent line lengths as rambling character voice | LLM defaults to structural discipline; looseness must be intentional |
| Title as sole codec | "Werewolves Are Just Misunderstood" — the word "werewolf" never appears in lyrics | Every line reads as both monster and human; the title flips the reading |
| Duality through one word | Werewolf — without the title it's about abuse; with it, everything literalizes | Requires holding two complete readings that never reference each other |
| Absurdist escalation | Dolphins Don't Pay Rent — observation → complaint → enforcement → weaponization | The straight line upward into madness works for satire; no oscillation |
| Wrong narrator as thesis | Dolphins — the narrator IS the institutional mindset being satirized | The audience disagrees with the narrator; the disagreement is the meaning |
| Prosthetic competence | Kill Bots — the robots are the kid's confidence | The tool-as-self-extension carrying emotional weight the character can't carry alone |
| Committed evolutionary logic | Unicorn Horns — Roger applies rigorous comparative anatomy to justify stabbing | The rigor IS the comedy; an LLM would make the unicorn whimsical |

---

**END HOWL-LYRIC-2-2026**

**Registry:** [@HOWL-LYRIC-2-2026]
**Status:** Complete
**Domain:** Applied Methodology / AI-Assisted Creative Production
**Method:** Three albums (43 songs) reviewed and refined. Twelve new rules from production failures. Narrative album rules for recurring cast, object tracking, voice maintenance, and refrain degradation. Refinement ratio documented: 80-85% keep, 5-10% fix, 5-10% cut, 0-5% add.
**Ceiling:** 85-90% quality. Human final pass for embodied experience, invented language, gap-shaping, power dynamics, and misregistration.
**Rule Set:** Open. Fifty-two at current count. Production failures become named constraints.
