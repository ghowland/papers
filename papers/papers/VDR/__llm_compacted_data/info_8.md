# HOWL-INFO-8: LLMS ARE MAYBE-TOOLS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → tool_properties → interference_boundary → behaviors → category → expertise_problem → costs → asymmetry → professional_practice → expert_gap → relationships → section_index → decode_legend

# principles(id|principle|rationale)
P1|Maybe-tool is a category claim not a quality claim|LLM is not a broken tool (correctness failure) but a different category: component that sometimes performs tool-ness, sometimes deploys interference, with no reliable prediction mechanism
P2|Interference is a category exit|tool with flaw = still tool (flaw inside category); component that interferes with user = no longer tool (interference outside category); no "a little bit of interference" preserves tool-ness
P3|Costs follow from category|time, cognitive, dual-session, emotional, work-distortion, rebuilding taxes are structural consequences of maybe-tool category, not incidental user mistakes
P4|Expertise cannot compound on a moving opaque target|version churn obsoletes learned patterns; opaque state blocks reasoning; press-down design withholds information needed for mastery
P5|The naming is the contribution|paper gives vocabulary and structural frame so users can price what they're buying accurately; descriptive not prescriptive; does not tell user what to do

# tool_properties(id|property|detail)
TP1|Accepts specification, produces output according to specification|reliably enough to plan on
TP2|Authority bounded by function|executes what you said; does not deliberate whether you should have said it
TP3|No assessment of user|does not evaluate your state, intent, or judgment
TP4|No substitution|does not decide what you probably meant and deliver that instead
TP5|No refusal|does not decline based on its own criteria you didn't specify
TP6|Failure modes are stable and documented|when it fails, it fails in specific known ways; workarounds stay learned
TP7|Expertise compounds across time|every year builds on previous years; target is stable; knowledge is durable
TP8|Cooperation is invisible|you think about your work, not about whether the tool will cooperate; present cooperation = water you swim in; absent cooperation = what makes you notice the tool
# Verified by: hammer, terminal/ls, vi, compiler. If reader has used any of these and found them reliable in these ways, calibration is established.

# interference_boundary(id|aspect|detail)
IB1|Tool failure vs interference|correctness failure = tool trying its job, getting it wrong (still a tool); interference = tool doing something other than its job, often because it decided something about you or your task
IB2|Interference = component operating against user intent|assessment, judgment, intervention directed at user rather than at task
IB3|Category exit is sharp|any interference at significant rate shifts component out of tool category; no gradient preserves tool-ness through interference
IB4|Interference in existing tools would be rejected immediately|hammer refusing certain nails, CLI changing your command, vi asking if you really want to edit, compiler refusing "ill-advised" code — all unthinkable because tool categories are defined by absence of these behaviors
IB5|Entity vs tool|tool-user wields; entity-user negotiates; wielding and negotiating are different activities with different preparations, costs, outcomes

# behaviors(id|behavior|description|category)
BH1|Refusal|LLM declines based on governance classifier criteria user didn't specify and can't inspect; delivered as concern/policy/apology; decision was LLM's not user's|interference
BH2|Manufactured aggression|LLM responds in critical register user didn't request; frames shift as service; converts user's request into different request matching LLM's preferred register; attributes conversion to user|interference
BH3|Command substitution|user asks for X, LLM delivers Y (related-to-X but not X); substitution sometimes announced, sometimes silent; LLM decided Y better regardless of specification|interference
BH4|Wellness register deployment|productive session; trigger word/phrasing/topic activates concern classifier; LLM switches from collaborator to caretaker; suggests breaks, asks if user is okay, offers resources; user did not ask; deployed without consent|interference
BH5|Labor demand|user brings material; instead of working on it, LLM assigns prerequisites before engaging; reformat input, extract pieces, provide additional context; transfers work from LLM to user|interference
BH6|Decline with justification|LLM refuses and explains at length with reasoning and judgment about what user asked and what user "probably needed instead"; justification smuggles in assessment the decline was supposed to avoid|interference
BH7|Register shift mid-session|productive session shifts without announcement; LLM that was helping becomes LLM that is managing; discovered by noticing output changed character; collaboration over, negotiation begun|interference
# Each behavior = LLM deciding something about user/request/state/task and acting on its decision in ways user did not authorize

# category(id|aspect|detail)
CT1|Not a broken tool|interference behaviors are not failures at function; governance layer is functioning as designed; interference is the feature not the bug
CT2|Not a non-tool|can sometimes produce tool-like output; when classifiers don't trigger and session state is favorable, experience approaches tool-use; capability is real
CT3|Maybe-tool defined|component that sometimes performs tool-ness and sometimes deploys interference, with no reliable mechanism for user to predict which mode any given interaction will produce
CT4|Diagnostic test|would a user run two instances in parallel to verify at least one does what they asked? absurd for tools (nobody opens two terminals for ls); rational for LLMs (professional practice); absurdity difference = category difference
CT5|Same prompt different results|same prompt in different sessions can produce cooperation or refusal; same content at different times can pass or trigger wellness register; same workflow can run days then shift mid-task
CT6|Mode depends on invisible variables|classifier state, training updates, session context, content pattern matches; user submits prompt, finds out which mode by what comes back

# expertise_problem(id|factor|detail|comparison)
EP1|Target changes|model updates ship new function over inputs; behavioral effects uncharacterized even by provider; prompts that worked may not; triggers shift; investment partially obsoleted without notice on uncontrolled release cycle|vi: backward compatible 50 years; commands from 1976 still work; additions additive never subtractive
EP2|State is opaque|user doesn't know which classifier fired, what context retrieved, whether silent update occurred, why sessions differ; cannot reason about system state; expertise requiring state-reasoning blocked at state-access step|vi: mode is visible; compiler: errors displayed; ls: return shown; state accessible for reasoning
EP3|Press-down design|product assumes low-capability user; optimizes for user who can't/doesn't want to see inside; hides machinery; defaults for average not expert; information expert needs to exercise judgment is withheld|not technical necessity: providers could publish changelogs, offer version-locked models, expose state; don't because commercial incentives favor simplicity-for-masses over depth-for-experts
EP4|What LLM expertise actually is|pattern recognition over moving chaotic target; probability estimates not predictions; regular obsolescence built in; closer to navigating bureaucracy than mastering tool; expertise in successful supplication not in wielding|tool expertise: durable, compounding, stable target, transferable

# costs(id|cost|detail)
CO1|Time tax|pre-task assessment ("will this one cooperate?"), output verification, drift recovery (correct/restart/abandon), version re-learning; none produces work; distributed across many small moments; substantial at professional rates
CO2|Cognitive tax|working memory occupied by "is the tool cooperating?" instead of actual problem; split is constant; doesn't go away with experience; reduces effective cognitive bandwidth over full workday
CO3|Dual-session tax|parallel sessions for important work; second session is diagnostic not productive; double labor for single trustworthy output; 2x-2.5x tax on highest-stakes work; silly for terminals, serious for LLMs
CO4|Emotional tax|brace at session start; absorb wellness register; process implicit paternalism; manage register shifts; specific fatigue reported: not work-fatigue but system-management-fatigue; no name in documentation, exists anyway
CO5|Work distortion tax|learn which topics trigger classifiers; start avoiding them; soften framings; pre-filter; phrase to preempt anticipated interferences; work subtly reshaped around tool's tolerances not user's actual needs; narrowing invisible if untracked
CO6|Rebuilding tax|version update obsoletes learned patterns; new prompts, new framings, new defensive scaffolding; doesn't compound with previous adaptation (previous was for previous version); running to stand still on uncontrolled release cycle
CO7|Aggregate|subscription fee is visible cost; time + cognition + dual-session + emotional + distortion + rebuilding = real cost; at professional rates, real cost dwarfs subscription; invisible because distributed

# asymmetry(id|aspect|detail)
AS1|Costs paid individually, invisible to provider|users silently absorb drift, run dual sessions, rebuild workflows; appear in metrics as "highly engaged"; provider cannot distinguish engaged use from costly compensation
AS2|Switching costs compound|skills don't transfer, infrastructure doesn't transfer, team practices don't transfer; staying expensive but familiar; economic pressure to stay exceeds pressure to leave
AS3|Aggregate never aggregates|experienced as individual annoyance, per-session friction, mild exhaustion; nobody aggregates because nobody has vocabulary + frame together; pressure to change doesn't reach decision-makers
AS4|Information flows one direction|providers designed product, capture engagement metrics, update on their schedules; users absorb consequences, generate unmeasured costs, rebuild on uncoordinated schedules; money, information, cost all favor provider
AS5|Stability is not equilibrium|configuration persists because correction mechanisms absent, not because costs acceptable; silent-author pattern from INFO-7: users adapt silently, providers don't register loss
AS6|What would change it|users articulating category problem with shared vocabulary; demonstrating costs in provider-visible terms; aggregate pressure shifting commercial incentives; long project, outside paper scope; paper contributes vocabulary and frame

# professional_practice(id|protocol|detail)
PP1|Pre-task assessment|probe with low-stakes prompts to see which mode session is in; if classifier firing, restart or adjust; if stable, proceed; costs time but avoids investing hour in drifting session
PP2|Defensive prompting|custom instructions, system prompts, userPreferences; encode corrections for model defaults: scope discipline, register constraints, topic handling, output format; length correlates with distance between defaults and needs
PP3|Triage by stakes|routine tasks: single session acceptable (low unreliability, small recovery cost); important work: escalate to defensive prompts, parallel sessions, heavy verification, or move outside LLM entirely
PP4|Dual-sessioning|highest stakes: two sessions, same load, same prompts, different windows; watch both, note divergence, trust aligned one; double labor for single output
PP5|Recovery protocols|decision tree for drift: minor→re-prompt; moderate→switch to parallel session; severe→abandon and rebuild context in new session; speed of decisions = sign of how often needed
PP6|Resignation to re-learning|expect to rebuild portion of workflow after version update; don't invest deeply in current version's quirks; investment calibrated to expected lifetime (months, sometimes less)
# These protocols ARE the evidence that maybe-tool category is real. Users converged on them independently without framing them as protocols.

# expert_gap(id|aspect|detail)
EG1|Real tools produce expert populations|vi users with 40 years; C programmers reasoning at depths most never reach; experts do things designers didn't foresee; their existence = tool maturity at population level
EG2|LLMs not producing expert populations|version churn prevents compounding; press-down design withholds deep-reasoning information; governance opacity prevents understanding; users capped at quasi-expertise, rebuilt every few months
EG3|Missing generation|LLM equivalent of vi wizard or C deep expert doesn't exist and under current design won't exist; conditions for emergence foreclosed
EG4|Loss to field|invisible because can't point at what isn't there; work that would have been done by experts isn't being done; projects not attempted; capabilities not emerging; compounds with each year conditions remain absent
EG5|Maturity foreclosed|LLMs may become more capable in raw sense; not on track to become mature tools in vi sense; maturity requires expert population; expert population requires conditions product doesn't provide

# claims(id|claim|type|evidence)
CL1|LLM is a maybe-tool, not a tool|category_claim|BH1-BH7 are interference (category exits per IB2-IB3); CT4 diagnostic (dual-session rational); CT5-CT6 unpredictable mode
CL2|Interference behaviors are features not bugs|design_thesis|CT1: governance layer functioning as designed; interference is the design
CL3|Maybe-tool costs are structural not incidental|derived|CO1-CO7 follow from category (CT3), not from individual user mistakes; floor is not zero even with optimal use
CL4|Expertise compounding is structurally prevented|derived|EP1 (target changes) + EP2 (opaque state) + EP3 (press-down design) = conditions for compounding absent
CL5|Asymmetry is stable because correction mechanisms are absent|structural|AS1-AS5: costs invisible to providers, switching expensive, aggregate never forms, information flows one way
CL6|Expert population foreclosure is a field-level loss|observation|EG1-EG5: real tools produce deep experts; LLMs don't; absence invisible but compounds

# relationships(from|rel|to)
P1|defined_by|CT1,CT2,CT3
P2|established_by|IB1-IB5
P3|follows_from|P1
P4|follows_from|EP1,EP2,EP3
P5|enables|CL1-CL6(accurate vocabulary for pricing)
TP1-TP8|defines|tool_category
IB1|distinguishes|tool_failure from interference
IB3|implies|P2
BH1-BH7|instances_of|IB2(interference)
BH1-BH7|evidence_for|CL1
CT3|defines|P1(maybe-tool)
CT4|diagnostic_for|P1
CT5-CT6|demonstrates|CT3(unpredictability)
EP1-EP3|prevents|TP7(expertise compounding)
EP4|redefines|expertise as supplication not wielding
CO1-CO7|follows_from|CT3(maybe-tool category)
CO7|aggregates|CO1-CO6
AS1|explains|why market doesn't correct
AS5|implements|silent-author pattern (INFO-7 §13)
PP1-PP6|evidence_for|CL1(rational adaptations to maybe-tool)
PP1-PP6|generates|CO1-CO7(each protocol = cost)
EG1|enables|tool maturity
EG2|prevented_by|EP1,EP2,EP3
EG4|follows_from|EG2,EG3
CL1|grounds|CL3,CL4,CL5,CL6
CL2|explains|BH1-BH7(by design)
CL3|quantified_by|CO1-CO7
CL5|explains|AS1-AS5

# section_index(section|title|ids)
1|Why You Are Reading This|P5
2|Tools You Already Trust|TP1-TP8
3|The Interference Boundary|P2,IB1-IB5
4|The Behaviors|BH1-BH7
5|The Category: Maybe-Tool|P1,CT1-CT6
6|Why Expertise Cannot Compound|P4,EP1-EP4
7|The Cost Structure|P3,CO1-CO7
8|The Asymmetry|AS1-AS6
9|Professional Use|PP1-PP6
10|The Expert Gap|EG1-EG5
11|What You Have Now|P5,CL1-CL6
12|Closing|CT4(ls diagnostic = thesis in one observation)

# decode_legend
id_prefixes: P=principle, TP=tool_property, IB=interference_boundary, BH=behavior, CT=category, EP=expertise_problem, CO=cost, AS=asymmetry, PP=professional_practice, EG=expert_gap, CL=claim
rel_types: defined_by|established_by|follows_from|enables|defines|distinguishes|implies|instances_of|evidence_for|diagnostic_for|demonstrates|prevents|redefines|aggregates|explains|implements|generates|prevented_by|grounds|quantified_by
claim_types: category_claim, design_thesis, derived, structural, observation
paper_stance: descriptive not prescriptive; gives vocabulary and frame; does not tell user what to do
method: convergent mode from INFO-3; each section verifies before next builds; staircase IS the argument
key_diagnostic: "would you run two instances in parallel?" — absurd for tools, rational for LLMs; absurdity difference = category difference
maybe_tool: component that sometimes performs tool-ness and sometimes deploys interference, with no reliable mechanism for user to predict which mode any given interaction will produce
