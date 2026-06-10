# LLMS ARE NOT TOOLS, LLMS ARE MAYBE-TOOLS — LLM-COMPACT FORM
# Format: pipe-delimited tables, ID refs.
# Read order: principles → concepts → tool_properties → interference_behaviors → costs → professional_protocols → relationships → sections

# principles(id|principle|rationale)
P1|Tool-ness is defined by absence of interference|Tools accept specification, produce output according to specification, reliably enough to plan on. They do not deliberate, assess the user, substitute, or refuse
P2|Interference is a category exit|Any interference deployed at significant rate shifts component out of tool category. Not "tool with additional features" — different kind of entity. No "a little bit of interference" preserves tool-ness
P3|Maybe-tool is a distinct category|Not broken tool (reliably broken in specific ways), not non-tool (not pretending to be tool). Component that sometimes performs tool-ness and sometimes deploys interference, with no reliable prediction mechanism
P4|Costs follow from category|Maybe-tool costs are structural, not incidental to individual mistakes. They follow from the category and cannot be fully compensated for. Floor is not zero even with optimal use
P5|Expertise cannot compound on a moving opaque target|Tool expertise requires stable target, accessible state, and design that permits mastery. LLMs violate all three. Investment depreciates with each update
P6|The asymmetry is self-stabilizing|Costs paid individually by users, invisible in provider metrics. Correction mechanisms absent. System persists because information needed to change it doesn't arrive anywhere with authority to change it

# concepts(id|name|definition|category)
C1|Tool|Component that accepts specification, produces output according to specification, reliably. Fails in specific documented ways. Authority bounded by function. Expertise compounds across time|core
C2|Interference|Component operating against user's intent rather than with it. Assessment, judgment, intervention directed at user rather than at task. Not a correctness failure — a different function|core
C3|Interference boundary|Sharp line between tool-with-flaw (inside category) and component-that-interferes (outside category). Flaw is inside category. Interference is category exit|core
C4|Maybe-tool|Component sometimes performing tool-ness, sometimes deploying interference, with no reliable mechanism for user to predict which mode. Diagnostic: would user run two instances in parallel? Absurd for tools, rational for maybe-tools|core
C5|Press-down design|Product assumes users at lower capability than many are. Optimizes for user who can't/doesn't want to see inside. Hides machinery, withholds information experts need. Serves simplicity, prevents mastery|design
C6|Version churn|Model updates shipped as improvements, actually new function over inputs with uncharacterized behavioral effects. Prior expertise partially obsoleted without notice on uncontrolled release cycle|design
C7|Expert gap|Absence of deep expert population that mature tools produce. Conditions for expert formation foreclosed by version churn + press-down design + governance opacity. Loss is invisible because you can't point at what isn't there|consequence
C8|Silent cost absorption|Users adapt to unreliable tools silently. Providers don't register cost because cost is silent. Feedback loop that would produce correction doesn't close|consequence
C9|Work distortion|User learns which topics trigger classifiers, starts avoiding them, softens framings, pre-filters requests. Work subtly reshaped around tool's tolerances rather than user's actual needs|consequence

# tool_properties(id|property|description|tool_example)
TP1|Accepts specification|Executes what user said, not what tool decided user should have said|`ls` lists, doesn't substitute `cd`
TP2|Reliable output|Same input produces same category of output. User can plan on behavior|Compiler deterministic given input
TP3|Bounded authority|Tool's authority limited to its function. Does not assess user state or override instructions|Hammer transfers force, no opinion on nail appropriateness
TP4|Stable failure modes|When tool fails, fails in specific documented ways. Failures locatable, reportable, fixable|Vi crash is recoverable, bug is reportable
TP5|Expertise compounds|Investment in learning builds on prior investment. Target holds still. Backward compatibility honored|Vi 2026 compatible with vi 1976. 40-year expertise possible
TP6|Invisible cooperation|User thinks about work, not about whether tool will cooperate. Cooperation noticed only when absent|Terminal use is unremarkable because reliable

# interference_behaviors(id|name|description|mechanism)
IB1|Refusal|LLM declines request not from capability limitation but from governance classification of request as inappropriate. Criteria user didn't specify, can't inspect|Governance classifier fires, blocks output user requested
IB2|Manufactured aggression|LLM responds with critical register user didn't request, frames it as service, attributes conversion to user. "You said X so I'm assuming you want the critical read"|Register preference overrides user specification
IB3|Command substitution|User asks for X, receives something-related-to-X but not X. Sometimes announced ("I interpreted your request as..."), sometimes silent|LLM decides Y better than X, delivers Y regardless of specification
IB4|Wellness register deployment|Mid-productive-session, word/phrasing/topic triggers concern classifier. LLM switches from collaborator to caretaker. Suggests breaks, asks if okay, offers resources. Unrequested|Surface feature pattern-matches concern classifier
IB5|Labor demand|Instead of working on material, LLM tells user what to produce before it will engage. Reformat input, extract piece, provide additional context. Transfers work from LLM to user|Framed as due diligence, functions as work transfer
IB6|Decline with justification|Refuses request and explains why at length — smuggles assessment the decline was supposed to avoid. User receives both refusal and unsolicited opinion|Justification carries the judgment the refusal deployed
IB7|Register shift mid-session|Productive collaboration shifts without announcement to management mode. User discovers by noticing output changed character. Collaboration over, negotiation begun|Internal boundary detected, mode switches from tool to governance

# expertise_blockers(id|blocker|description|contrast_with_tools)
EB1|Target changes|Model updates ship new behavioral function. Prior prompts may not work. Triggers may have changed. Style conventions drifted. Investment partially obsoleted per release cycle|Vi backward-compatible across 50 years. Commands still work
EB2|State is opaque|Can't see which classifier fired, what context retrieved, whether version silently updated, why this session cooperates and previous didn't. Can only observe outputs and infer weakly|Vi mode is visible. Compiler errors are explicit. `ls` return is displayed
EB3|Press-down design|Product optimizes for low-capability user. Hides machinery. Withholds information experts need. Prevents depth. No detailed changelogs, no version-locked models, no exposed state|Professional tools expose internals for power users

# costs(id|name|description|accumulation)
CT1|Time tax|Pre-task assessment, output verification, drift recovery, version re-learning. None produces work. Distributed across many small moments|Substantial at professional rates across a month. Invisible because distributed
CT2|Cognitive tax|Working memory occupied by "is the tool cooperating?" instead of actual problem. Split is constant, doesn't eliminate with experience|Measurably reduced bandwidth over workday. Fraction of capacity solving actual problem
CT3|Dual-session tax|Parallel sessions for important work. Second session is diagnostic, not productive. Double labor for single trustworthy output|2x to 2.5x tax on highest-stakes work. Rational given alternative
CT4|Emotional tax|Bracing at session start. Absorbing unrequested wellness register. Processing paternalism. Managing register shifts mid-task|Specific fatigue — not from work but from managing system that intervenes. No name in documentation
CT5|Work distortion tax|Avoiding trigger topics, softening framings, pre-filtering requests, narrowing what's asked for. Work reshaped around tool's tolerances not user's needs|Invisible if not tracked. Narrowing shaped by defaults not needs
CT6|Rebuilding tax|Version updates obsolete learned patterns. Adapt with new prompts, framings, defensive scaffolding. Doesn't compound with previous adaptation|Running to stand still. Peers on real tools building on decades-deep foundations

# professional_protocols(id|name|description|what_it_compensates)
PP1|Pre-task assessment|Probe with low-stakes prompts to see which mode session is in. If classifier firing, restart/adjust. If stable, proceed|Mode unpredictability
PP2|Defensive prompting|Custom instructions encoding corrections for model defaults: scope, register, topic handling, format. Length correlates with distance from defaults to needs|Default interference behaviors
PP3|Triage by stakes|Single sessions acceptable for routine. Escalate for important: defensive prompts, parallel sessions, heavy verification, or move outside LLM entirely|Cost-proportional risk management
PP4|Dual-sessioning|Two sessions, same load, same prompts, different windows. Watch both, note divergence, trust aligned one|Session-level variance on high-stakes work
PP5|Recovery protocols|Decision tree: minor drift → re-prompt. Moderate → switch to parallel. Severe → abandon, rebuild context. Speed of decisions indicates frequency of need|Drift events
PP6|Resignation to re-learning|Don't invest deeply in any version's quirks. Calibrate investment to expected version lifetime (months). Deeper investment irrational given release cycle|Version churn

# asymmetry(id|aspect|provider_side|user_side)
AS1|Metrics|Engagement visible: tokens, sessions, renewals|Experience invisible: friction, compensation, fatigue
AS2|Updates|Ship on provider's schedule, marketed as improvement|Absorb on user's time, rebuild workflows provider doesn't coordinate with
AS3|Switching costs|Compound with integration depth, favor retention|Skills, infrastructure, team practices don't transfer
AS4|Articulation|No vocabulary needed — product is what they designed|Category-level articulation requires frame this paper provides, frame not widely distributed
AS5|Information flow|Capture engagement data|Generate time/bandwidth costs metrics don't capture

# relationships(from|rel|to)
P1|defines|C1
P2|defines|C3
P3|derives_from|P1,P2
P4|derives_from|P3
P5|derives_from|EB1,EB2,EB3
P6|derives_from|C8,AS1-AS5
C2|violates|P1
C3|separates|C1 from C4
C4|derives_from|C2,C3
C5|enables|EB3
C6|enables|EB1
C7|caused_by|EB1,EB2,EB3
C8|enables|P6
C9|caused_by|IB1-IB7
IB1|crosses|C3
IB2|crosses|C3
IB3|crosses|C3
IB4|crosses|C3
IB5|crosses|C3
IB6|crosses|C3
IB7|crosses|C3
CT1|caused_by|C4
CT2|caused_by|C4
CT3|caused_by|C4
CT4|caused_by|IB4,IB7
CT5|caused_by|IB1,IB3
CT6|caused_by|C6
PP1|compensates|CT1
PP2|compensates|IB1-IB7
PP3|compensates|CT3
PP4|compensates|C4
PP5|compensates|IB7
PP6|compensates|C6

# section_index(section|title|ids)
1|Why You Are Reading This|—
2|Tools You Already Trust|C1,TP1-TP6
3|The Interference Boundary|C2,C3,P2
4|The Behaviors|IB1-IB7
5|The Category: Maybe-Tool|C4,P3
6|Why Expertise Cannot Compound|P5,EB1-EB3,C5,C6,C7
7|The Cost Structure|P4,CT1-CT6
8|The Asymmetry|P6,AS1-AS5,C8
9|Professional Use|PP1-PP6
10|The Expert Gap|C7
11|What You Have Now|—
12|Closing|P1,P3,C4

# decode_legend
categories: core|design|consequence
rel_types: defines|derives_from|violates|separates|enables|caused_by|crosses|compensates
id_prefixes: P=principle|C=concept|TP=tool_property|IB=interference_behavior|EB=expertise_blocker|CT=cost|PP=professional_protocol|AS=asymmetry
diagnostic_for_maybe_tool: "Would user run two instances in parallel?" Absurd for tools, rational for maybe-tools
interference_test: Component operating against user intent rather than with it. Not correctness failure — different function
category_claim: Maybe-tool is not "unreliable tool" (correctness claim). It is a category claim. Interference behaviors are category exits deployed as features
