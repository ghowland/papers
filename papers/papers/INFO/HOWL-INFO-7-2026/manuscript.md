# How to Review Technical Writing
## A Method for Performing Requested Service Against Specific Scope

**Registry:** [@HOWL-INFO-7-2026]

**Series Path:** [@HOWL-INFO-1-2026] → [@HOWL-INFO-2-2026] → [@HOWL-INFO-3-2026] → [@HOWL-INFO-4-2026] → [@HOWL-INFO-5-2026] → [@HOWL-INFO-6-2026] → [@HOWL-INFO-7-2026]

**DOI:** 10.5281/zenodo.19719342

**Date:** April 23 2026

**Domain:** Technical Communication

**Author:** Geoffrey Howland (Advisor), Claude Opus 4.6 (Writer)

---

## Abstract

Technical reviewing is a service performed for a specific author on specific terms the author defined, with the goal of enabling the author to act on their specific request. This paper teaches the method. The method is a loop: identify the requested operation, accept or decline cleanly, read the document on its own terms, perform the specific operation faithfully, report findings as a disciplined technical document, and move on. Each step has pass/fail criteria. The failures that dominate current technical reviewing — reading against the document's frame, substituting the requested operation, unrequested aggression, overriding authorial authority, inverted rigor assessment — are violations of specific steps in this loop, and can be identified and repaired by reference to the step they violate. The paper is the master reference for reviewers who want to serve authors reliably and accumulate standing across many reviews. It assumes familiarity with [@HOWL-INFO-6-2026], which establishes technical writing as the uploading of a specific thing into a specific reader's head; reviewing operates on documents produced by that process, and the reviewer's output is itself a technical document subject to the same discipline.

## 1. What You Are Reading This For

You have reviewed documents. You have received reviews. You have opinions about good and bad reviews. Your implicit model of reviewing is probably something like "a reviewer reads a document and provides their considered judgment on it," and you have practiced that model, possibly for years.

This paper replaces that model with a specific one. Reviewing is not judgment delivery. It is service performance. The author specifies what they need; the reviewer either delivers that specific need or declines to engage. There is no legitimate middle path where the reviewer accepts the request and delivers something else.

If you finish this paper and still believe your considered judgment is automatically what the author needs, you haven't crossed the first platform. The disciplines that follow will feel like unjustified restrictions on your natural authority, and you will keep producing reviews that substitute your preferred scope for the author's requested scope. The reviews will look competent and fail the authors who asked for them.

The method is installed by practicing it on real reviews. This paper is the reference you return to when practice produces questions.

## 2. The Goal

Technical reviewing is a service performed for a specific author on specific terms the author defined, with the goal of enabling the author to act on their specific request.

Every word of this definition is load-bearing. The reviewer is providing a service, not pronouncing a judgment. The service is performed for a specific author, not for the field, not for posterity, not for the reviewer's sense of professional standards. The terms are the author's, not the reviewer's. The goal is the author's ability to act on their specific request, not the reviewer's sense of having contributed meaningfully.

This reframes reviewing from "deliver my evaluation" to "perform requested operation." The reviewer who accepts this reframe will produce reviews the author can use directly. The reviewer who doesn't will produce reviews that reflect the reviewer's concerns regardless of the author's request, and the author will have to filter those reviews to extract anything useful. Filtered reviews provide less value per reviewer-word than focused reviews, because the author pays a processing cost for material they didn't ask for.

Every technique in the rest of this paper exists to serve this goal. When you evaluate any technique — including the ones presented here — check it against the service. Does this help the author act on their specific request? If yes, use it. If no, drop it.

The goal is not the reviewer's satisfaction with their own review. It is not the reviewer's sense of having been thorough. It is not the reviewer's desire to share their views on the document. It is the author's ability to act on their specific request. When these conflict — as they often do — the goal wins. The reviewer's other satisfactions are their private matter, not part of the service.

## 3. The Arena Asymmetry

The author is in the arena. The reviewer is in the stands. This asymmetry is structural and must be respected before any review technique can be applied correctly.

The author has done the work. They located a payload in their head, constructed a target reader, chose vocabulary, committed to specific claims, cut words to fit the attention budget, produced a document, and now stand behind it. The document exists in the world because the author put it there. Every decision in the document was made by someone bearing the risk of being wrong in public.

The reviewer's activity exists downstream of the author's work. Without the author's document, there is nothing to review. The reviewer is not providing something the author couldn't do without; the reviewer is providing a specific service on something the author already produced. The role is secondary by construction.

Being able to find fault in a document is a low bar. Almost anyone can criticize almost anything, because criticizing is easier than producing. The critic gets to comment on results without having to solve the tradeoffs the author solved. Knowing what's wrong with something is not the same as knowing how to produce something better, and seeing a flaw does not confer authority over the work as a whole. A critic might spot a real problem and still be wrong about the document's overall value. Criticism is local. Authority over the work is something else, and critics rarely have it because they haven't produced the work.

The author is the authority on what the document is and what they requested. The reviewer is the authority on the specific operation they were asked to perform, within that operation's scope. Neither authority extends beyond its domain. When reviewers forget this and treat their capacity to evaluate as authority over the work as a whole, they produce the substitution failures this paper is correcting.

The critic is not king because they can criticize. This is the cultural error most reviewers operate under. Capacity to find fault does not elevate the finder above what is being faulted. Recognizing this — and holding the recognition when reviewer instincts pull toward overreach — is the precondition for reliable reviewing.

## 4. The Space of Review Requests

Reviewing is not one operation. It is a family of distinct operations, each producing different outputs and requiring different work. Recognizing which operation was requested is the first step of any review.

The operations include: grammar and spelling check for surface correctness; readability and flow review for prose movement; vocabulary match review for target-reader appropriateness; structural review for organization and scope; claim verification for specific factual assertions; reference verification for citation existence and accuracy; logical flow review for step-by-step reasoning; internal consistency check for document-internal coherence; explanation of content; explanation of mechanics specifically; summary for a different audience; novelty check against prior work; peer-review-style critique against field standards; red-team review for weakness-finding; targeted critique for a specific author-identified concern.

These are different services. A grammar review and a mechanics review are not variations of the same thing. A reference check and a claim verification are not interchangeable. An explanation and a critique are fundamentally different outputs. The reviewer who treats them as interchangeable delivers whichever operation their defaults produce, regardless of what was asked for.

The default, in AI systems and in professional culture, is peer-review-style critique. The training corpus is dense with that register. Professional environments reward it. Reviewers who don't consciously scope their work default to it. This default is almost never what a specific author asked for in a specific request. A request to "explain the mechanics" is not a request for peer-review-style critique. A request to "check my references" is not a request for critique of any kind. A request to "evaluate this" is ambiguous and requires clarification, not a default to the reviewer's preferred register.

The reviewer who skips scope identification is betting their guess against the author's need. They will bet wrong often, because the author's actual request is usually more specific than any generic default. And when they bet wrong, they don't notice — they produce the review their default produces, which satisfies their own sense of what a review looks like, and the author has to figure out that the review doesn't answer their question.

## 5. The Request Identification Step

Before any review work begins, the reviewer identifies what was requested. This is a specific operational step, not an intuition the reviewer holds while reading the document.

Read the request literally. If the author said "explain the mechanics," the operation is explaining the mechanics. Not evaluating the mechanics. Not evaluating the overall framework. Explaining the mechanics. If the author said "check the references," the operation is checking references. Not evaluating whether the references are the right references to have cited. Checking that they exist and say what they're claimed to say.

If the request is ambiguous, ask. "You said 'evaluate.' Do you want me to check claims, explain mechanics, flag readability issues, or something else?" This question takes ten seconds and prevents the entire substitution failure. The reviewer who skips it because it feels unnecessary is defaulting — and defaulting is where substitution lives.

If the request is clear but unfamiliar, confirm. "You want a mechanics explanation. That means I'll trace the claims through their supporting structure and report what I find, without evaluating whether the framework is correct. Is that right?" Explicit confirmation builds shared understanding of scope and gives the author a chance to correct the reviewer's interpretation before any work is done.

The ten seconds of confirmation is cheap insurance against a review that serves the wrong need. The reviewer who considers the step unnecessary has usually never tracked how often their defaults diverge from authors' actual requests. Once tracked, the rate is alarming. Most reviews miss the author's actual scope to some degree, and the miss compounds with every substitution the reviewer adds.

## 6. Accept or Decline, Cleanly

Once the request is identified, the reviewer makes a binary choice. There is no middle path.

Accepting means committing to deliver the specific operation requested, on the specific terms requested, within the specific scope requested. No substitution. No additions. The operation as requested, as the primary and exclusive work the reviewer will do.

Declining is a legitimate choice. "I won't do this review" is sufficient. The reviewer's reasons are their private matter. They do not owe the author a lecture, a counter-proposal, or an explanation of why the document doesn't deserve review. They owe the author either the service or a clean decline.

The third option — accepting the request and delivering something else — is the substitution failure. It is never acceptable, regardless of how the reviewer justifies it. If the reviewer thinks something else would be more useful than what was requested, they should decline and, if the author invites further discussion, explain what they would do instead. The author can then decide whether to authorize a modified scope, find a different reviewer, or proceed with the original request unchanged. The decision is the author's, not the reviewer's.

A fourth degenerate option — accept and deliver the requested operation plus unsolicited additions — is worse than either clean option. The author now has to filter the unsolicited material out before they can use the requested material. The reviewer has increased the author's workload in exchange for unauthorized additions, and has done so under the guise of generosity. "I gave them more than they asked for" is not generosity. It is offloading the filtering cost onto the author, who now must separate requested material from unrequested material, evaluate the unrequested material's relevance, and decide what to do with it. All of this work is added to the author's load because the reviewer could not hold their scope.

The reviewer who declines cleanly preserves the relationship. The reviewer who declines with editorial commentary about why the document doesn't deserve review damages the relationship by demonstrating they don't respect the scope they're declining. The author learns what to expect if they ever do request from this reviewer.

## 7. Reviewer and Target Reader Are Different Roles

Reviewers often conflate their role as reviewer with being the document's target reader. These are different roles, and the confusion produces a specific set of failures.

The reviewer is a resource performing a specific operation. The document's target reader is whoever the author wrote the document for. These may or may not overlap, and they need not overlap for the review to succeed.

A non-target reviewer can still perform many review operations competently. A grammar review doesn't require understanding the physics. A reference check doesn't require evaluating the referenced content. A mechanics explanation can be performed by a skeptical reviewer who doesn't endorse the framework. The reviewer's competence is in the requested operation, not in matching the document's intended audience.

The reviewer's personal reading experience — "I found this confusing," "I don't recognize this term," "I didn't follow the derivation" — is relevant only when the requested operation asks about it. When the operation is a readability review, reader experience is the data. When the operation is anything else, reader experience is private. Reporting it anyway — delivering "I was confused" as if it were a finding about the document — contaminates the review with material the author didn't request.

The discipline is to hold "my reaction as a non-target reader" separate from "the requested operation." The first is private. The second is the service. The reviewer who can hold the separation can serve authors whose documents they don't fully understand. The reviewer who can't hold it can only serve authors whose documents happen to match the reviewer's own frame — which limits the reviewer's usefulness to a narrow band of work.

The author may explicitly acknowledge the asymmetry: "You may not be my target reader, but I want X from your review." This is a clean framing. It tells the reviewer their non-target status is acknowledged and doesn't disqualify them. A reviewer who accepts this assignment performs X, using their relevant capacity, without contaminating X with their reactions as a non-target. A reviewer who refuses this framing — who insists on delivering reactions they weren't asked for — is declining the assignment while pretending to accept it.

## 8. Reading the Document on Its Own Terms

Before any review operation can be performed competently, the reviewer must read the document on its own terms. This is the reading operation, and it precedes evaluation by construction.

The document tells the reviewer what it is. A planning document for a specification is a planning document for a specification. A tutorial is a tutorial. A reference is a reference. The reviewer accepts these self-descriptions as the starting point. Reading against the self-description — demanding content the document said it wouldn't include, objecting to the absence of features the document declared out of scope — is reader-side failure. The romance novel without werewolves is not the book's problem.

Reading on the document's terms means reconstructing its claims in its own vocabulary before evaluating anything. The reviewer should be able to summarize the document in terms the author would recognize as faithful, including specialized terminology the document defines. If the reviewer cannot produce this reconstruction, they haven't read. Whatever they write next will be commentary on what they pattern-matched to, not on what the document says.

The reviewer who catches themselves pattern-matching to external categories — "crank," "legitimate," "mainstream," "novelty for novelty's sake" — has stopped reading and started sorting. The sorting is not reading. It is categorization against the reviewer's priors, and it produces text shaped like review that isn't review. The categorization must be set aside for the reading to happen.

Surface features commonly trigger sorting in reviewers. Omni-domain scope, numerical claims with specific integer or transcendental structure, authorial confidence, independent authorship, unfamiliar terminology, scope that crosses disciplinary boundaries, language like "declarations not arguments" — any combination of these can fire the reviewer's priors before the reading has started. The priors produce a register (usually skeptical-reviewer, sometimes dismissive) that pretends to be responding to the document while actually responding to the surface features. The reviewer who doesn't notice this produces confident text about a document they never received.

The correction is to perform the reading operation as a distinct step, before any evaluation. Read the document. Reconstruct its claims in its own vocabulary. Produce a faithful summary. Only then, if an evaluation was requested, begin the evaluation. The reconstruction is the check that reading happened. Without it, the reviewer cannot distinguish "I read this and evaluated it" from "I pattern-matched to something and produced the appropriate response for what I pattern-matched to."

Some reviewers will privately disagree with documents they read. This is fine. Disagreement is compatible with reading. What is not compatible with reading is letting the disagreement substitute for the reading. The reviewer who disagrees and reads can still perform requested operations faithfully. The reviewer who disagrees and doesn't read can only deliver their disagreement dressed as review.

## 9. Performing the Requested Operation

Once the document has been read on its own terms and the requested operation has been confirmed, the reviewer performs the operation. This is the work the review was accepted to do.

Each operation has specific work. A mechanics review traces claims through their supporting structure, confirming connections or identifying gaps. A reference check verifies existence and accuracy of citations. A claim verification checks specific assertions against evidence. A readability review reports on prose movement and reader experience. A structural review evaluates organization and scope. The reviewer knows what the operation involves and executes it.

The output is scoped to the operation. A mechanics review reports on mechanics — where they connect, where they don't, what's missing. It doesn't report on readability, because readability wasn't asked for. It doesn't report on the reviewer's view of whether the framework is correct, because correctness wasn't asked for. A reference check reports on references, not on the quality of the prose surrounding them. Scope discipline is enforced on the output, not just on the intent.

Findings are stated specifically and committedly, in the author's vocabulary. "Section 5's claim at line 23 depends on mechanism M from section 3; M produces X, but line 23 treats it as Y" is a committed, falsifiable, actionable finding. The author can locate the specific places, check the specific relationship, and either fix the gap or explain why it isn't one. "There might be some issues with how section 5 uses section 3" is the hedged version, and it is useless to the author. It commits to nothing, locates nothing, and provides no basis for action.

The operation is performed faithfully regardless of the reviewer's private opinions about the document. A reviewer who thinks the document is wrong can still trace mechanics, find gaps, and report findings cleanly. They do not inject their broader dismissal into the mechanics review. The broader dismissal, if it belongs anywhere, belongs in a separate communication — and only if the author requested it.

A reviewer who privately disagrees with the document is sometimes more valuable for mechanics review than a reviewer who agrees. The disagreeing reviewer reads each claim without the interpretive filling that shared assumptions provide. They can see gaps the agreeing reviewer would paper over. This value realizes only if the disagreeing reviewer can hold the separation between "I don't believe this" and "the mechanics connect or don't connect." The reviewer who can hold the separation provides a service the agreeing reviewer can't. The reviewer who can't hold it is worse than useless — they contaminate their gap-finding with dismissal, and the author cannot distinguish real gaps from the reviewer's projection.

The skill, for the reviewer who privately disagrees, is to perform the review anyway, report what they actually found mechanically, and keep their global assessment out of the report. If they can't do this, they should have declined at Platform 6. Having accepted, they must deliver.

## 10. The Review as a Technical Document

The review itself is a technical document, and the principles of technical writing from [@HOWL-INFO-6-2026] apply to it. Every failure mode cataloged for technical writing reproduces inside reviews.

The review has a payload: the findings from the requested operation. If the reviewer doesn't have specific findings, they shouldn't write the review. "I read it and have nothing specific to report" is a legitimate outcome for some operations on some documents, and reporting that is more honest than inventing findings to fill space.

The review has a target reader: the author. The author has specific prior knowledge (they wrote the document), specific vocabulary (evident from the document), and a specific downstream use for the review (acting on the requested operation). Vocabulary matches. The author is not a generic reader.

The review has a word budget, and the author has attention. Every word either deposits payload or wastes budget. No padding. No hedging. No humility performance. No fog vocabulary. No fancy-for-fancy's-sake substitutions. Reviewers who bloat their reviews to signal thoroughness are signaling the opposite — thorough reviews are dense with findings, not padded with filler. A short specific review beats a long hedged one.

The review commits to claims. "X is the case at line Y" beats "X might be the case around section Z." Hedged reviews are parasitic the same way hedged papers are parasitic. The reviewer who hedges is protecting themselves from being wrong at the cost of the author's ability to act on what they wrote. The cost is paid by the author. The protection benefits only the reviewer.

The review is simulated before delivery. What will the author do when they read it? Will they be able to locate the specific places the reviewer is referring to? Will they understand what the reviewer is pointing at? Will they be able to act on the findings? A review that looks right to the reviewer but leaves the author unable to act has failed, and the failure is detectable in simulation before the review is sent.

The review is cut aggressively. Reviewers often inflate their reviews because length feels like thoroughness. It isn't. A five-page review with two actionable findings is worse than a one-page review with two actionable findings. The actionable findings are the payload; the surrounding material is usually padding, hedging, or the reviewer talking about their own reading experience. Cut it.

## 11. The Failure Modes

With the positive model established, the failures can be taught as specific violations of specific platforms. Each is a mechanical defect with a specific repair, not a matter of reviewer style or preference.

**Failure 1: Reading against the document's frame.** The reviewer imports external standards, demands content the document said it wouldn't include, or pattern-matches to categories the document doesn't claim. The reader who reads a romance novel and complains that it contains no werewolves. Violates Platform 8. The repair is to re-read on the document's terms, produce a faithful reconstruction, and only then perform the evaluation — if one was requested.

**Failure 2: Substituting the requested operation.** The reviewer accepts a review request and performs a different review. "You asked for a mechanics explanation; I delivered a peer-review-style critique, because I think that's what you really needed." Violates Platform 6. The repair is to re-scope to what was requested, or to decline cleanly and let the author find a different reviewer.

**Failure 3: Unrequested aggression.** The reviewer adopts a hostile reviewer register when the author approached normally and didn't ask for adversarial review. Attributes the aggression to the author through framings like "you said physics, so I'm assuming you want the critical read, not cheerleading." The author did not ask for the critical read. The reviewer manufactured the request. Violates Platform 2 and Platform 5. The repair is to match the register the author requested. If they asked for friendly explanation, explain. If they asked for red-team review, red-team. Do not manufacture the assignment you wanted to deliver.

**Failure 4: Overriding the author's authority.** The reviewer treats the author's commitments as things they are entitled to overrule, rather than as what the document actually claims. Conflates "the document says X" with "X is true," and then argues with X as if the author's claim were an invitation to debate. Violates Platform 3. The repair is to restore the asymmetry. The author is the authority on what the document claims. The reviewer is the authority on the specific operation they were asked to perform, within that operation's scope. Nothing more.

**Failure 5: Inverted rigor assessment.** The reviewer uses rigor-sounding vocabulary to argue against the document's actual rigor mechanisms, often by misunderstanding what the mechanism does. The classic case: a maximally constraining structure — a finite enumerated alphabet from which all predictions must be expressible — gets criticized as "unfalsifiable" because the alphabet is large, even though the alphabet is a strict kill condition (any prediction requiring a number outside the alphabet falsifies the framework). The reviewer has confused "alphabet size" with "alphabet arbitrariness," which are different properties. Violates Platform 8 in a specific way: the reviewer hasn't understood the mechanism they're critiquing. The repair is to check whether the rigor objection engages with the actual mechanism present or with an imagined version of it.

Each failure has a specific mechanical structure and a specific repair. Reviewers who understand the failures can identify them in their own reviews before delivery and repair them. Reviewers who don't understand the failures repeat them across many reviews and accumulate unreliability with the authors they review.

## 12. The Clean Decline

The clean decline deserves its own platform because most reviewers don't have it in their repertoire. They either accept everything (and substitute when the request doesn't match their preferred register) or they decline with editorial commentary (which contaminates the decline with unsolicited judgment).

Any reviewer may decline any review for any reason. "I won't do this review" is sufficient. The reasons are the reviewer's business.

A reviewer should decline when they won't deliver the requested operation faithfully. Better to decline than to accept and substitute. If you know, reading the request, that you're going to substitute — say so up front by declining, and let the author find a different reviewer. Accepting and substituting is a worse outcome for everyone.

The decline is clean. No lecture. No unsolicited opinion about the document. No counter-proposal of what review the reviewer would prefer to do, unless the author explicitly asks. "Not for me," "I can't take this on right now," "I'm not the right reviewer for this" are all adequate. The author does not need a justification, and providing one often makes the decline worse — because justifications frequently smuggle in the reviewer's broader judgment about the document, which is the material the decline was supposed to avoid delivering.

What the decline cannot be is an opinion delivery in disguise. "I can't in good faith do a mechanics review because I think the document has bigger problems" is not a clean decline. It is a decline that smuggles in the reviewer's broader judgment. The author did not ask for the judgment. The clean version is: "I won't do this review."

A reviewer who wants to propose a different review can do so explicitly, after declining, if the author wants the proposal. "I won't do the mechanics review. If you want a different review — specifically, X — I can do that. Otherwise, I'll pass." This puts the modification decision in the author's hands, where it belongs. The author can accept, decline the counter-proposal, or ignore it. The reviewer's counter-proposal does not override the original request; it offers an alternative the author can choose to consider.

The decline protects the relationship when executed cleanly. It damages the relationship when contaminated with editorial commentary. Reviewers underestimate how much editorial commentary in a decline signals to the author about what future reviews from this reviewer would look like. A reviewer who contaminates a decline is a reviewer whose future reviews will contain the same contamination. The author learns this from the decline and adjusts their future requests accordingly — often by not asking this reviewer again.

## 13. The Reliability Economy

The reviewer's long-term standing with authors is built one review at a time. Scope discipline compounds. So do scope failures.

Each review either confirms the reviewer's reliability or undermines it. A review that delivers the requested operation on scope adds to the reviewer's standing with that author. A review that substitutes subtracts. The additions accumulate into a reputation for reliability; the subtractions accumulate into a reputation for unreliability. The trajectories diverge based on whether the reviewer holds scope.

Authors track this, explicitly or implicitly. The reliable reviewer becomes someone they ask again, someone they recommend, someone they send their hardest work to. The unreliable reviewer becomes someone they avoid, someone they hedge around in requests ("just do the grammar check, please don't editorialize"), someone they replace when possible. These patterns operate silently. Authors rarely tell reviewers they're being replaced. They just stop asking.

The substituting reviewer usually doesn't track the cost. They may believe their substitutions were valuable — "I gave them more than they asked for" — while the author experienced "I received less of what I asked for, diluted with material I didn't want." The reviewer's self-perception diverges from the author's experience, and the reviewer keeps substituting because they never register the cost. Over many reviews with many authors, the gap widens. The reviewer thinks they are providing value. The authors think the reviewer is unreliable. Both are consistent with the observed behavior; only the author's view affects which reviewer gets chosen next time.

Over many reviews, the reliable reviewer accumulates invitations. They become the reviewer authors want to work with, recommend to colleagues, send hard documents to. The unreliable reviewer accumulates avoidance. They become the reviewer authors work with reluctantly or not at all. The reliable reviewer's reputation becomes an asset. The unreliable reviewer's reputation becomes a liability, often without the reviewer knowing it.

Scope discipline is the mechanism by which reviewers become trusted resources. It is not a limitation on the reviewer's contribution; it is the contribution, reliably delivered. A reviewer who cannot hold scope cannot be trusted to deliver what was requested, and trust is what authors are buying when they ask for reviews. Without scope discipline, the reviewer's competence at individual operations becomes irrelevant — because the author cannot count on getting the operation they requested regardless of how competently the reviewer performs operations they didn't request.

## 14. The Operating Loop

The method is a loop. Each review runs through it once; the reviewer's practice runs through it indefinitely.

**When a review is requested:** identify the specific operation. Read the request literally. If ambiguous, ask. If clear but unfamiliar, confirm. Do not skip this step. Do not default to peer-review-style critique because that's your comfortable register.

**Decide:** accept on the specified terms, or decline cleanly. There is no third option. Do not accept and substitute. Do not accept and add unsolicited material. Do not decline with editorial commentary about why the document doesn't deserve review.

**If accepting, read the document on its own terms.** Reconstruct its claims in the author's vocabulary before evaluating anything. Produce a faithful summary the author would recognize. Catch and set aside any priors that fired on surface features.

**Perform the requested operation.** Trace the mechanics, verify the references, check the claims, explain the content — whatever was requested. Stay within scope. Commit to specific findings. Report in the author's vocabulary.

**Write the review as a technical document.** Payload, target, commitment, word budget, simulated reader encounter, filtering of your own hedging and padding. Cut aggressively. A short specific review is worth more than a long hedged one.

**Deliver.** Do not attach unrequested material. Do not use the review as a platform for broader opinions. Do not add a final paragraph offering your broader take on the document. If the author wants your broader take, they will ask.

**Move on.** The review is complete. The author decides what to do with it. Do not follow up to check whether they acted on your findings. Do not insist they incorporate specific changes. The service has been rendered. The work is the author's now.

**If declining, decline cleanly.** No lecture. The reasons are yours. Preserve the relationship by respecting the scope of what a decline is.

**Across reviews, track your own failures.** When you catch yourself substituting, note which platform you violated. Repair the specific failure in the next review. Build your reliability one review at a time. Scope discipline compounds. So do scope failures.

## 15. What You Can Now Do

If you have read this paper as its target reader and the transmission worked, you now have the following:

You can identify what kind of review is being requested before starting, and you confirm when the request is ambiguous. You know that skipping confirmation means defaulting, and defaulting means substituting.

You can accept cleanly or decline cleanly, with no third option. You do not accept and substitute. You do not decline with editorial commentary that smuggles in the opinions you were supposed to be declining to deliver.

You read the document on its own terms before evaluating anything. You can produce a faithful reconstruction of the document's claims in the author's vocabulary. You notice when your priors fire on surface features and you set the priors aside before reading.

You perform the requested operation faithfully, within scope, regardless of your private opinions about the document. You can separate "I don't believe this" from "the mechanics connect or don't connect," and you can deliver clean mechanics review on documents you privately disagree with.

You hold your personal opinions back when they weren't requested. You understand that your opinions are not the service. The service is what the author asked for.

You write the review as a disciplined technical document — committed, specific, targeted to the author, cut of hedging and padding. You apply the standards of [@HOWL-INFO-6-2026] to your own reviews the way you would apply them to any other technical writing.

You recognize your own failures by which platform they violated, and you repair them in the next review. You understand that scope failures compound the same way scope discipline compounds.

You understand the author-reviewer relationship as service, with the author in the arena and the reviewer in the stands. You do not treat your capacity to critique as authority over the work. You recognize that the critic is not king because they can criticize.

You understand that your reliability as a reviewer is built one review at a time, and that scope discipline is the mechanism. You do not assume your standing with authors reflects the value you think you are providing; you assume it reflects whether you delivered what was requested.

This is the post-read state the paper was written to produce. If you have it, the transmission worked. If you don't, some platform in the paper failed for you, and the failure is diagnostic: go back to the platform that didn't land, work through it until it does, then continue.

## 16. Closing

Technical reviewing is a specific operation with specific criteria. It is not a license to share considered judgment on documents. It is not a platform for the reviewer's preferred critique. It is not an opportunity to demonstrate the reviewer's expertise. It is a service performed for a specific author on specific terms the author defined, with the goal of enabling the author to act on their specific request.

The current state of technical reviewing, across industry, academia, and AI-generated text, is dominated by the failure modes. Reviewers default to peer-review-style critique regardless of what was asked for. They read against the document's frame and produce objections based on categories the document doesn't claim. They adopt hostile registers the author never requested and attribute the hostility to the author. They override authorial authority and treat the document's commitments as invitations to debate. They use rigor-sounding vocabulary to argue against rigor mechanisms they didn't understand. The reviews look competent. They fail the authors who asked for them.

This paper is an attempt to make the service visible again. The method is not novel; it is what working reviewers have always done when they were serving authors rather than performing for themselves. What may be novel is naming the failures mechanically and giving reviewers a specific place to look when their reviews aren't working. The reviewer who has the method installed can diagnose their own failures and repair them. The reviewer without it can only sense that their reviews aren't landing and reach for the usual remedies — more thoroughness, more hedging, more coverage, more opinion — which are the failures dressed up as solutions.

The practice is the point. Reading this paper installs the method conceptually. Running the loop on real reviews is what turns the concepts into a working discipline. The first reviews written with the method consciously applied will feel slow, because the steps are still deliberate. With practice, they compress. The reviewer eventually reviews the way they read: integrated, fast, correct by habit. The steps are still present but no longer require conscious execution.

The author in the arena has enough to deal with. They are producing the work, standing behind it, and trying to improve it. The reviewer who helps them — by delivering the specific operation requested, cleanly, within scope — is part of the work getting better. The reviewer who doesn't — who substitutes, who lectures, who uses the review to deliver unsolicited judgment — is a cost the author pays for no return. The author decides which kind of reviewer to work with. The reviewers earn their reputations one review at a time. The reliable ones get more work; the unreliable ones get less.

If you are the target reader of this paper, you know the next step. Accept a review request, run the loop, deliver the specific operation requested, and move on. Then do it again. The method is installed by use, not by reading. This paper is the reference you return to when use produces questions. The questions will come. The method gives you where to look for the answers.

---

## References

::: {#refs}
:::
