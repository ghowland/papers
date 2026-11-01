# Building Ungameable Trust Networks for Curated Directories
### Decentralized Filtering Without Central Authority

**Registry:** [@HOWL-COMP-19-2026]

**DOI:** 10.5281/zenodo.23852190

**Date:** November 2026

**Domain:** Decentralized Systems / Trust Graph Architecture / Adversarial-Resistant Curation Networks

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6. 

---

## 1. The Problem

Search and discovery on the 2026 internet is broken for three groups: users who want to find real businesses and resources, small businesses who want to be found, and honest affiliate operators who want to earn from genuine recommendations.

Search engines rank results by signals that reward scale, not quality. A local hardware store cannot outrank a content farm that produces ten thousand SEO-optimized pages per day with large language models. Paying for search advertising puts small businesses into bidding wars against companies with orders-of-magnitude larger budgets. Social media demands constant content production — videos, posts, engagement farming — work that has nothing to do with the actual service the business provides.

Review platforms are corrupted. Fake reviews, review bombing, pay-to-play visibility schemes, and extortion dynamics have made star ratings unreliable. Users append "reddit" to their search queries as a trust signal, but Reddit itself is degrading as it monetizes and as marketers infiltrate communities.

AI answer engines attempt to solve the problem by synthesizing responses, but they draw from the same polluted index and introduce hallucination risk. The underlying data is compromised. No amount of summarization fixes a contaminated source.

Honest affiliate operators face the same structural disadvantage. An operator who genuinely tests products and recommends what they believe in cannot compete on volume against content farms that rewrite product descriptions and stuff affiliate links without touching the products. The algorithm cannot distinguish the two. The content farm wins on output volume every time.

Three intermediaries sit between a person and a useful resource: algorithmic ranking that rewards manipulation, centralized moderation that makes uniform visibility decisions for all users, and review systems that are themselves a manipulation surface. All three are failing.

---

## 2. The Directory Model

The system described in this paper is a human-curated link directory. It contains listings — structured entries that point to real businesses, real people, and real resources. Each listing contains a name, a category, a URL or contact method, and a short plain-text description of what the entity does.

Listings are the destination, not an intermediary. There are no articles, no reviews, no content marketing pages. A listing for a hardware store contains the store's name, its URL, its location, and a sentence about what it sells. The user clicks through to the store itself.

A curator is a registered user who creates and maintains listings. Curators are identified by name. There is no anonymous curation. Any registered user becomes a curator by creating their first listing. There is no application process, no approval gate, and no editorial review.

Each curator receives a subdomain — `{curator_name}.directory.cabal` — where their listings are published. The curator controls all content on their subdomain. The platform stores and serves the content but does not select, arrange, modify, or review it.

Multiple curators can list the same entity independently. Each listing is independent. The system does not merge or deduplicate them. Different curators may categorize the same entity differently, write different descriptions, or link to different URLs. This is intentional — the user's trust decisions determine which version they see.

The directory contains text only. No images, no video, no media. A typical listing is under one kilobyte. A category page with one hundred listings is under one hundred kilobytes.

---

## 3. The Trust Graph

Trust is the core mechanism that replaces algorithmic ranking and centralized moderation. Trust is a directed edge from a user to a curator. It is binary — a curator is either trusted or not trusted by a given user. There is no partial trust, no trust score, and no trust level.

When a user trusts a curator, all of that curator's listings become visible in the user's view of the directory. When a user squelches a curator, all of that curator's listings are hidden from the user's view. Squelching does not delete anything. The curator's listings continue to exist. Other users who trust that curator continue to see the listings. Squelching is a local visibility filter that affects only the squelching user's view.

Trust is not transitive by default. If User A trusts Curator B, and Curator B trusts Curator C, User A does not automatically see Curator C's listings.

A user grants trust by clicking a trust button on any listing in their current view. Trust takes effect immediately. A user squelches a curator by clicking a squelch button on any listing in their current view.

### 3.1 View Resolution

When a user browses a category, the system resolves their view through the following steps:

1. Collect all listings in the requested category.
2. Remove all listings created by squelched curators.
3. Remove all listings created by curators in squelched cabals.
4. Show only listings created by trusted curators.
5. Squelching takes precedence over trust. If a user trusts a curator individually but has squelched a cabal that curator belongs to, the curator's listings are hidden.

Listings are displayed in chronological order, newest first. There is no relevance ranking, no popularity sorting, and no engagement-based ordering.

### 3.2 New User Experience

A new user with no trust edges and no squelch edges sees all listings from all curators in their selected categories. This is the unfiltered view. It contains everything — good listings, bad listings, spam, and legitimate curation.

This unfiltered starting point is intentional. The system does not pre-filter for the user. There are no seed curators, no platform-curated starting point, and no editorial selection of recommended curators. The user sees the full landscape and begins building their trust and squelch graph from their own evaluation.

The new user journey is:

1. Sign up and pay $8/year.
2. Pick categories of interest.
3. See all listings from all curators in those categories.
4. Browse listings. Identify curators whose listings are obviously low-quality.
5. Squelch the bad curators. They and their associated networks disappear from view.
6. Among the remaining curators, find one whose listings consistently point to real, useful entities.
7. Trust that curator. The directory is now filtered by the user's own trust decisions.

### 3.3 Squelch Lists

A user's squelch list — the set of all curators and cabals they have squelched — can be published. Other users can adopt a published squelch list, which applies all squelches in the list to their own view. Adoption can be a one-time snapshot or a live subscription that propagates future additions automatically.

Squelch list sharing allows experienced users to pass their filtering work to new users. A new user who adopts an established squelch list inherits the filtering decisions of an experienced user without performing the evaluation work themselves.

---

## 4. Cabals

A cabal is an algorithmically detected cluster of curators. The system does not formally define cabals and curators do not join them deliberately. A cabal forms when curators trust each other, list the same entities, or operate in the same categories with high mutual endorsement density.

The clustering algorithm — a community detection method such as Louvain or Label Propagation — runs on the curator-to-curator endorsement graph weighted by category overlap. The algorithm runs once per day. Changes between recalculations are not reflected in real time. This prevents rapid cabal restructuring from being used to evade squelch operations.

### 4.1 Cabal-Level Squelch

The default squelch action is cabal-level. When a user squelches a single curator, the system squelches the curator and every other curator in that curator's cabal. The user does not need to identify the cabal, browse membership lists, or make a separate decision. One button press on one bad listing removes the entire associated network from the user's view.

An individual-only squelch is available through a secondary interface for cases where the user objects to one curator but not the rest of the cabal.

### 4.2 Cabal Metadata

Cabal metadata is public. Any user can browse the list of detected cabals, view their members, see their category coverage, and check their stability score. This transparency allows users to make informed decisions about which networks to trust or squelch.

Cabal IDs are stable as long as core membership remains the same. When a cabal fragments, the original ID is retired and new IDs are assigned to the resulting sub-clusters. Cabal IDs are never reused.

### 4.3 Squelch Persistence Through Fragmentation

When a user squelches a cabal, the system records individual squelch edges against every curator in the cabal at the time of the action. These edges persist regardless of future cabal membership changes. If the cabal fragments, every member remains individually squelched. The squelch follows the curator, not the cabal structure.

---

## 5. The Defensive Asymmetry

The system's resistance to manipulation derives from a structural asymmetry between the cost of attack and the cost of defense.

Defense costs one click. A user who sees a bad listing presses one button. The curator who created the listing and every curator in their cabal disappears from the user's view. The squelch propagates through squelch list subscriptions to every user who subscribes to the squelching user's list.

Offense costs real money and real time. Every curator account costs $8/year with a unique payment method. Building trust requires producing listings that real users find valuable. Accumulating cabal membership requires trust links from other curators. The minimum viable attack requires weeks to months of setup. The maximum damage from any attack is temporary partial visibility loss measured in hours.

### 5.1 The Notification System

Every curator has a notification dashboard that displays two separate timelines.

**Untrusted squelches** are squelches from users who never trusted the curator. These indicate that new users are encountering the curator's cabal and rejecting it. This is a weak signal — the users were never in the curator's audience.

**Formerly-trusted squelches** are squelches from users who previously trusted the curator. These indicate that the curator is losing earned audience. Something changed in the cabal that caused users who had accepted the curator's work to reject the entire group. This is a strong signal.

The dashboard includes correlation data. The system compares the timing of new trust edges created by the curator against the timing of squelch spikes. If the curator trusted a new curator on Monday and the squelch rate increased substantially by Wednesday, the new trust addition is flagged as the probable cause.

This gives every curator in a cabal an immediate diagnostic tool. When squelch rates spike, the dashboard tells them which recent trust addition is causing the problem. Every curator is individually incentivized to distrust the bad actor to protect their own visibility. No platform intervention is required.

### 5.2 Self-Policing Through Distributed Self-Interest

The notification system creates a self-policing dynamic. Every curator in a cabal sees the consequences of bad associations in real time. Every curator can independently distrust the bad actor. Every curator is motivated to do so because the bad association directly reduces their own visibility.

The platform does not need a moderation team, a trust-and-safety department, or any form of centralized enforcement. Every curator is their own trust-and-safety department because the costs of bad associations land directly on them and the diagnostic data is in front of them.

---

## 6. Adversarial Analysis

This section examines every known attack vector against the system. Each attack fails. Each attack is self-correcting without platform intervention. Each attack converts attacker effort into platform value during the setup phase.

### 6.1 Sockpuppet Cabals

An attacker creates multiple accounts with separate payment methods, builds a cabal of fake curators, and populates it with spam listings.

The financial cost is $8 per account per year plus a unique payment method per account. Fifty sockpuppet accounts costs $400/year and requires fifty distinct payment instruments. Payment processors flag bulk account creation from similar instruments.

The sockpuppet cabal appears in the unfiltered view. Real users browse the category, identify the listings as low-quality, and squelch the cabal. One click removes all fifty accounts. The squelch propagates through squelch list subscriptions. The entire cabal goes dark within hours.

The attacker's $400 investment and days of setup produce a few hours of visibility in a text directory with no engagement mechanics. The conversion rate on spam listings during that window is effectively zero. The accounts are permanently burned for every user who squelched them. Recovery requires fifty new accounts with fifty new payment methods and another $400.

### 6.2 Infiltration of an Established Cabal

An attacker creates one account, builds a credible initial listing set, and earns a trust link from an established curator. Once inside the cabal, the attacker introduces spam listings.

The established curator sees a squelch spike correlated with the timing of the trust addition. The dashboard identifies the attacker as the probable cause. The established curator distrusts the attacker. At the next daily recalculation, the cabal reforms without the attacker.

The damage window is at most 24-48 hours. Users must actively browse the category during this window to encounter the spam. There is no push mechanism that surfaces spam to users who are not browsing. The established curator's other cabal memberships are unaffected. Only the specific cabal containing the attacker is impacted.

### 6.3 Slow-Burn Infiltration

An attacker spends months building genuinely useful listings, accumulates trust from multiple curators, and then gradually shifts toward spam or low-quality content.

This is the most expensive attack. The attacker must produce real value for an extended period. When the quality shift begins, formerly-trusted users are the most sensitive to the change because they trusted the curator specifically for quality. Squelch rates spike. Cabal partners see the correlation data and distrust the attacker.

The months of legitimate curation produced real value for users. The attack phase is brief and self-correcting. The system converted the attacker into a productive participant for the majority of their time on the platform.

### 6.4 Bribery of Established Curators

An attacker pays an established curator to trust the attacker's account, providing visibility through the established curator's cabal.

The established curator trusts the attacker. The attacker receives one day of visibility before the curator distrusts them and the cabal recalculates. One day of visibility in a text directory with no engagement mechanics produces near-zero value.

If the curator accepts repeated bribes — trusting a new attacker each day — the notification dashboard shows every other curator in the cabal a daily pattern of trust additions correlated with squelch spikes. Cabal partners distrust the corrupt curator to protect their own visibility. The corrupt curator loses their cabal memberships within two cycles.

The corrupt curator keeps their direct trust edges from users. But they keep landing in cabals that get squelched because they keep linking to bad actors. They flicker between visible and invisible. Their trusted users see repeated disappearances and eventually squelch them permanently through human judgment.

The bribe market cannot sustain itself. The product being sold — brief visibility in a text directory — has no value to the buyer. The act of selling it destroys the seller's network position. The game is self-defeating within days.

### 6.5 Cabal Fragmentation to Evade Squelch

A squelched cabal restructures by having members distrust each other and reform into smaller sub-cabals.

The squelch was recorded against individual curator IDs, not the cabal ID. Every member remains individually squelched regardless of new cabal membership. The cabal ID is retired and never reused. The opt-in auto-squelch setting catches sub-cabals containing a majority of original members.

Fragmentation does not restore visibility.

### 6.6 Mass Account Purchase

A well-funded attacker purchases 50,000 accounts at $400,000/year with 50,000 separate payment methods and builds a coordinated cabal to dominate a category.

The 50,000-account cabal is a single massive cluster in the detection algorithm. A cabal with 50,000 members in a category where legitimate cabals have 5-50 members is anomalous on its face. A user sees one listing from the cabal, recognizes it as commercially motivated, squelches the cabal, and all 50,000 accounts vanish from their view in one click. The squelch propagates through subscriptions. Within a week, every active user who subscribes to established squelch lists has pre-squelched the entire network.

The scale of the attack works against the attacker. A smaller attack evades detection longer but has negligible reach. A larger attack has broader reach but is more obvious and more quickly squelched. There is no good option on the size spectrum.

### 6.7 Astroturfing

A sophisticated attacker creates hundreds of accounts, builds genuinely useful listings over months, and then coordinates a mass squelch of a competitor's cabal to suppress the competitor's visibility.

Squelching only affects the squelcher's view and the views of users who subscribe to the squelcher's squelch list. The astroturf network squelches the competitor. No real user is affected unless they subscribe to an astroturf account's squelch list.

The astroturf accounts cluster together in the detection algorithm because they trust each other. The resulting cabal is visible in the public cabal browsing interface. A recently-formed cabal of hundreds of members in a category where normal cabals have 10-30 members is anomalous. Any user browsing the cabal list can identify the anomaly independently.

The target's notification dashboard shows a squelch spike but cannot identify who squelched them or which cabal the squelchers belong to. The target cannot distinguish a coordinated attack from a large number of independent users who all rejected their listings. The defense is not in the target's hands — it is distributed across the user base. Any user who notices the anomalous cabal structure can squelch the astroturf network independently. The squelch propagates through subscriptions.

The months of legitimate curation that built the astroturf network are destroyed when users squelch the anomalous cabal. The setup phase produced real value for the platform. The attack phase destroys the attacker's investment. The target recovers.

### 6.8 Attacks That Cannot Exist

Four categories of attack are structurally impossible in this system:

**Algorithm gaming** cannot exist because there is no ranking algorithm. Listings are chronological. There is no signal to optimize for.

**Engagement manipulation** cannot exist because there are no engagement metrics. No likes, no view counts, no shares, no reactions. There is nothing to inflate.

**Review manipulation** cannot exist because there are no reviews. The only user actions are trust and squelch, both private to the acting user's graph.

**Popularity manipulation** cannot exist because trust counts are not visible to any user. There is no popularity metric, no trending list, and no leaderboard. A curator cannot appear more popular than they are because popularity is not displayed.

---

## 7. Why Small Businesses Win

The activation cost for a small business to participate in this system is extraordinarily low. A business owner pays $8, writes up the businesses they personally trust, and publishes their list at their subdomain. That is a single session of work. Not ongoing content production. Not weekly posts. Not engagement farming. One session, and the referral list exists permanently at a linkable URL.

The knowledge required already exists. The plumber knows which electrician does good work. The electrician knows which hardware supplier is reliable. The bakery owner knows which wholesale flour distributor delivers on time. This knowledge lives in every business owner's head and in informal referral conversations. It is not captured anywhere online in a structured, browsable, linkable form. This system captures it.

When a customer asks "do you know a good electrician," the plumber says the subdomain URL. That replaces a text message, a forgotten conversation, a business card that gets lost. It is a permanent, public referral list maintained by a person with a real reputation attached to it.

When the electrician also signs up and publishes their own trusted businesses, a trust edge forms. The cabal detection picks it up. At 200 curators in a local cabal, the system contains something that does not exist on the internet today: a structured, browsable network of real businesses that vouch for each other. Every listing was placed by a named person. Every trust edge represents a real professional relationship.

Google cannot produce this data because Google indexes pages, not trust relationships between business owners. Reddit cannot produce it because Reddit is organized around topics and anonymous users. Yelp cannot produce it because Yelp's unit is the individual review, not the referral network. No existing platform captures the structure of two hundred businesses that all trust each other and collectively recommend each other to their customers.

### 7.1 Meaningful Edges

On Facebook and LinkedIn, adding a connection costs nothing. There is no consequence to accepting every request. A LinkedIn user with 5,000 connections is not vouching for 5,000 people. They clicked accept 5,000 times with zero risk.

In this system, every trust edge has a cost. If you trust a curator who ends up in a cabal with a spammer, your visibility is affected through that cabal. You lose partial visibility until you break the link. That cost is low enough that people are willing to trust new curators, but high enough that trust edges carry real information.

A 200-person cabal where every member has skin in the game is a fundamentally different data structure than a 5,000-person LinkedIn network where no one risked anything by connecting.

---

## 8. Economic Model

### 8.1 Revenue

The sole revenue source is an $8/year flat subscription per registered user. There is no advertising, no paid placement, no promoted listings, and no platform affiliate cut. Curators can use their own affiliate links independently — the platform does not track, facilitate, or tax affiliate revenue.

Anonymous readers browse the unfiltered view for free. They can see all listings and all curator subdomains. They cannot trust, squelch, or manage a trust graph. The subscription pays for the filtering tool.

### 8.2 Incentive Alignment

With subscription revenue only, the platform's sole incentive is to retain subscribers. Subscribers are retained when the directory is useful. The directory is useful when curators list real, relevant entities. The platform has no financial reason to prefer commercial listings over non-commercial listings, no reason to promote engagement, and no reason to optimize for time-on-site.

Advertising-supported platforms must optimize for engagement and data collection. That optimization produces the dark patterns, algorithmic feeds, and attention-capture mechanics that degrade user experience. Subscription removes that pressure entirely.

### 8.3 Infrastructure Costs

The system stores text data only. No images, no video, no file uploads. At one million users with an average of 200 trust and squelch edges each, the trust graph is 200 million small tuples. At ten million listings with an average of 500 bytes each, the listings database is approximately five gigabytes. The entire dataset fits on a single server with commodity hardware.

Curator subdomains are routing rules against the same database, not separate servers. Adding ten thousand curators adds ten thousand routing rules, not ten thousand servers. Static HTML is generated on listing changes and cached between updates. Trust graph filtering is an in-memory set intersection — computationally trivial.

A typical page load is under 200 kilobytes. At one million daily page views, daily bandwidth is approximately 200 gigabytes, within the capacity of a single commodity server with a CDN for static content.

Estimated annual infrastructure cost at one million users: $50,000-$100,000. At $8 million annual recurring revenue, the platform operates at approximately 99% gross margin on infrastructure. The primary cost is a small engineering team. No moderation team is required. No trust-and-safety team is required. Trust and safety is delegated entirely to users through the squelch mechanism.

### 8.4 Anti-Sockpuppet Economics

At $8/year per account, creating 100 sockpuppet accounts costs $800/year in subscription fees. Each account requires a separate payment method. The operational cost of maintaining 100 separate payment methods with 100 separate identities is the real deterrent. The trust graph dynamics make the investment worthless — the sockpuppet cabal is detected, squelched, and invisible within days. The attacker must repeat the entire setup with new payment methods to try again.

---

## 9. Legal Architecture

### 9.1 Platform as Hosting Provider

The platform operates as a hosting service provider. It provides infrastructure — subdomain hosting, database storage, content delivery, and the trust graph tool. It does not publish, curate, select, or editorially control the content on curator subdomains.

Each curator is the publisher of the content on their subdomain. The curator is legally responsible for the content of their listings.

### 9.2 Content Policy

The platform's terms of service contain one content rule: curators must not publish listings for illegal goods, services, or activities. There are no additional content policies. There are no community guidelines about quality, accuracy, taste, or bias. The trust graph handles quality. The legal system handles legality.

### 9.3 Takedown Process

The platform hosts a reporting form for illegal content. The process is mechanical: receive the report, forward it to the curator, allow 48 hours for the curator to comply or contest. If the curator does not respond, the listing is disabled. If the curator contests, the dispute is between the reporter and the curator. The platform does not evaluate the merit of legal claims.

Three upheld takedowns in 12 months triggers subdomain suspension and manual review. This is the only platform-level judgment in the entire system.

### 9.4 Regulatory Positioning

**US Section 230**: The platform is the interactive computer service. Curators are the information content providers. The user-controlled squelch mechanism is good-faith content filtering under Section 230(c)(2).

**EU Digital Services Act**: The platform is classified as a hosting service. It maintains a notice-and-action mechanism, a point of contact, and publishes annual transparency reports. It does not have the obligations of an online platform under Articles 20-24 because it does not moderate content.

**GDPR**: The platform is the data controller for account data and the data processor for listing data. The trust graph is private. Trust counts are not visible to any user. Right to deletion within 30 days. Data portability via JSON export.

**KOSA**: The platform has no infinite scroll, no autoplay, no push notifications, no algorithmic feeds, no engagement metrics, no direct messaging, no comments, and no social comparison features. It is a text directory. It has no design features that children's online safety legislation identifies as addictive or harmful.

### 9.5 No Content Moderation

The platform does not perform content moderation. It does not review listings before publication. It does not scan for prohibited content. It does not use automated filters, keyword blocklists, or AI classifiers. The only content action is suspension in response to valid legal takedown notices. This is a hosting infrastructure action, not an editorial action.

This distinction matters because content moderation creates editorial liability. A platform that reviews and selectively removes content may be treated as a publisher of the content it keeps. By not moderating, the platform maintains its status as a hosting provider.

---

## 10. Convergence

The system hardens over time. It does not degrade.

Squelch lists accumulate and propagate through subscriptions. New users who adopt established squelch lists inherit the filtering work of experienced users. Known bad actors are pre-squelched before new users encounter them.

Good cabals become denser and more stable. Their stability scores rise. Established curators watch their notification dashboards and respond quickly to bad associations. New members are vetted through the natural social process of trust evaluation.

The cost of attacking increases as the system matures because established squelch lists cover more known attack patterns. The value of legitimate participation increases as trust networks deepen and audiences grow.

Every attack examined in this paper shares a common profile: high cost, temporary visibility, permanent loss of invested resources, and near-zero return. The most effective long-term attacks require the attacker to spend the majority of their investment on legitimate curation. The system converts attack budgets into genuine platform value during the setup phase and nullifies the attack during the execution phase.

The system does not need to escalate consequences for repeated offenses. The consequence is the same every time — temporary partial visibility loss, full recovery after breaking the bad association. Escalation occurs naturally through human behavior. Users who re-trusted a curator after a first incident and see them in a second bad cabal are less likely to re-trust a third time. The platform does not enforce this. Humans enforce it through their own judgment.

The long-term equilibrium is a self-policing network of curators with real reputations, real audiences, and real incentives to maintain quality. The system selects for participants who find it more profitable to curate honestly than to attack. This is not an aspiration. It is a structural property of the economic incentives embedded in the architecture.

---

# HOWL-COMP-19-2026 — Appendix

---

## Table A — Listing Fields

| Field | Type | Required | Constraints |
|---|---|---|---|
| Name | text | yes | max 200 characters |
| Category path | text | yes | full hierarchy, multiple paths permitted |
| URL | URL | conditional | at least one of URL or contact method required |
| Contact method | text | conditional | phone, email, or physical address |
| Description | text | yes | max 500 characters, plain text only, no markup or links |
| Commercial flag | boolean | yes | set by curator, determines whether listing is commercial |
| Affiliate URL | URL | no | curator's own affiliate link, platform does not track or process |
| Created by | user ID | automatic | set at creation |
| Created at | timestamp | automatic | set at creation |
| Updated at | timestamp | automatic | set on any modification |

---

## Table B — User Tiers and Capabilities

| Capability | Anonymous (free) | Registered ($8/yr) | Curator ($8/yr) |
|---|---|---|---|
| Browse unfiltered aggregated view | yes | yes | yes |
| Browse curator subdomains | yes | yes | yes |
| Search by keyword, category, curator | yes | yes | yes |
| Trust curators | no | yes | yes |
| Squelch curators and cabals | no | yes | yes |
| Manage personal trust graph | no | yes | yes |
| See filtered view based on trust graph | no | yes | yes |
| See trust network indicators | no | yes | yes |
| Publish squelch list | no | yes | yes |
| Adopt and subscribe to squelch lists | no | yes | yes |
| Toggle unfiltered view override | no | yes | yes |
| Create, update, remove listings | no | no | yes |
| Access curator notification dashboard | no | no | yes |
| Set affiliate URLs on listings | no | no | yes |

---

## Table C — Trust Edge States

| State | Meaning | How entered | Effect on view | Participates in squelch lists |
|---|---|---|---|---|
| Trusted | user explicitly trusts curator | trust button | curator's listings visible | no |
| Squelched | user explicitly rejects curator | squelch button | curator's listings hidden, cabal members hidden | yes |
| Undefined | no edge exists | default state, or after clearing an edge | listings hidden unless unvetted toggle is on | no |

---

## Table D — Squelch Scope Comparison

| Action | Trigger | Scope | Recorded as | Persistence through cabal recalculation |
|---|---|---|---|---|
| Cabal squelch (default) | squelch button, primary action | curator + all current cabal members | individual edges per curator ID | yes, edges follow curator IDs |
| Individual squelch | squelch button, secondary menu | single curator only | one edge for that curator ID | yes |
| Cabal auto-squelch (opt-in) | sub-cabal contains majority of previously squelched cabal | all members of qualifying sub-cabal | individual edges per curator ID | yes |

---

## Table E — Notification Signal Types

| Signal | Source | Meaning | Strength | Recoverable by curator action |
|---|---|---|---|---|
| Untrusted squelch | user who never trusted the curator | cabal rejected on first impression | weak | no — user was never in audience |
| Formerly-trusted squelch | user who previously trusted the curator | earned audience lost due to cabal change | strong | yes — break bad association, reappear under clean cabal, formerly-trusted users can re-trust |

---

## Table F — Notification Dashboard Data

| Data element | Content | Update frequency |
|---|---|---|
| Squelch count (untrusted) | aggregate count over 24h, 7d, 30d windows | real-time |
| Squelch count (formerly-trusted) | aggregate count over 24h, 7d, 30d windows | real-time |
| Cabal targeted | which cabal the squelch was applied to | per event |
| Correlation data | list of curator's recent trust additions with percentage change in squelch rate following each addition | recalculated on each new squelch event |
| Timeline | time-series of squelch events, separated by signal type | continuous |

---

## Table G — Cabal Metadata

| Field | Type | Visibility | Purpose |
|---|---|---|---|
| Cabal ID | stable identifier | public | squelch targeting, browsing |
| Member list | set of curator IDs | public | user evaluation, squelch scope |
| Category coverage | set of category paths | public | user evaluation |
| Size | integer | public | anomaly detection by users |
| Stability score | float | public | indicates cabal maturity — high means established, low means forming or fragmenting |

---

## Table H — Cabal Lifecycle Events

| Event | Trigger | Effect on cabal ID | Effect on existing squelches |
|---|---|---|---|
| Formation | clustering algorithm detects new group | new ID assigned | none |
| Member added | curator's trust links change, recalculation places them in existing cluster | ID unchanged | existing squelches of this cabal do not auto-apply to new member |
| Member removed | curator distrusts a link, recalculation places them elsewhere | ID unchanged if core remains | curator's individual squelch edges persist under new cabal |
| Fragmentation | core membership diverges into sub-clusters | original ID retired, new IDs assigned to each sub-cluster | individual curator squelch edges persist, opt-in auto-squelch catches majority-overlap sub-cabals |
| Dissolution | all trust links between members broken | ID retired permanently | individual squelch edges persist but cabal-level squelch becomes inert |

---

## Table I — Attack Vector Summary

| Attack | Setup cost | Visibility window | Self-correction mechanism | Attacker recovery path | Net value to attacker |
|---|---|---|---|---|---|
| Sockpuppet cabal | $8/account + unique payment methods | hours | users squelch, propagates via squelch list subscriptions | must create entirely new accounts and payment methods | near zero |
| Infiltration | one account + time to build credible listings | 24-48 hours | established curator sees correlation in dashboard, distrusts attacker | must rebuild trust relationship with a different curator | near zero |
| Slow-burn | months of legitimate curation | days after quality shift begins | formerly-trusted users squelch, cabal partners see correlation data | must invest months again | negative — attacker produced real value during setup then lost position |
| Bribery (single) | bribe payment to established curator | one recalculation cycle | curator distrusts attacker next day | must pay another bribe | near zero — one day of text directory visibility has no conversion value |
| Bribery (repeated) | ongoing bribe payments | flickering — one day on, one day off | cabal partners see daily correlation pattern, distrust corrupt curator within two cycles | corrupt curator loses cabal memberships, bribe product becomes worthless | negative — destroys the asset being purchased |
| Cabal fragmentation | coordination to restructure trust links | none | individual squelch edges persist across all cabal changes | none — fragmentation does not restore visibility | zero |
| Mass account purchase (50k) | $400,000/yr + 50,000 payment methods | days before squelch propagation saturates | anomalous cabal size visible in public interface, one-click cabal squelch | must create 50,000 new accounts with new payment methods | near zero |
| Astroturfing | months of legitimate curation across hundreds of accounts | target suppression limited to astroturf subscribers only | anomalous cabal size visible in public interface, users squelch independently | months of setup destroyed | negative — setup phase produced platform value, attack phase destroyed attacker position |

---

## Table J — Attacks That Cannot Exist

| Attack category | Why it is structurally impossible |
|---|---|
| Algorithm gaming | no ranking algorithm exists — listings are chronological |
| Engagement manipulation | no engagement metrics exist — no likes, views, shares, or reactions |
| Review manipulation | no review system exists — only trust and squelch, both private |
| Popularity manipulation | trust counts are not visible to any user — no leaderboard, no trending, no popularity metric |
| Advertising injection | no ad inventory exists — visibility cannot be purchased at any price |
| SEO | search operates on closed dataset only — no web crawl, no inbound link weighting, no term density reward beyond baseline relevance |

---

## Table K — API Endpoints

### Read (public, authenticated)

| Method | Path | Auth required | Description |
|---|---|---|---|
| GET | /categories | no | category hierarchy, scoped to user trust graph if authenticated |
| GET | /categories/{path}/listings | no | listings in category, unfiltered if anonymous, trust-filtered if authenticated |
| GET | /categories/{path}/listings?view=unfiltered | yes | all listings with no trust or squelch filtering |
| GET | /curators/{id} | no | curator profile, listing count |
| GET | /curators/{id}/listings | no | all listings by curator, unfiltered |
| GET | /cabals | no | all detected cabals with metadata |
| GET | /cabals/{id}/members | no | member list for a cabal |
| GET | /search?q={query}&category={path} | no | full-text search, unfiltered if anonymous, trust-filtered if authenticated |
| GET | /{curator_name}.directory.cabal/listings | no | all listings on curator's subdomain |
| GET | /{curator_name}.directory.cabal/categories | no | category structure for curator's subdomain |

### Trust management (authenticated)

| Method | Path | Description |
|---|---|---|
| POST | /user/trust/{curator_id} | trust a curator |
| POST | /user/distrust/{curator_id} | remove trust edge, return curator to undefined state |
| POST | /user/squelch/{curator_id}?scope=cabal | squelch curator and entire cabal (default) |
| POST | /user/squelch/{curator_id}?scope=individual | squelch curator only |
| DELETE | /user/trust/{curator_id} | clear trust edge |
| POST | /user/adopt-squelch-list/{user_id} | adopt another user's squelch list |
| POST | /user/publish-squelch-list | publish own squelch list |
| GET | /user/trust | own trust and squelch edges |
| GET | /user/squelch-lists | own published and subscribed squelch lists |

### Curator (authenticated, curator only)

| Method | Path | Description |
|---|---|---|
| POST | /listings | create listing |
| PUT | /listings/{id} | update own listing |
| DELETE | /listings/{id} | mark own listing inactive |
| GET | /curator/notifications/squelch-summary | aggregate squelch counts by signal type, 24h/7d/30d |
| GET | /curator/notifications/correlation | recent trust additions with squelch impact data |
| GET | /curator/notifications/timeline | time-series of squelch events by type |
| GET | /curator/takedowns | own takedown case history |
| POST | /curator/takedowns/{case_id}/contest | contest a takedown report |

### Reporting (no auth required)

| Method | Path | Description |
|---|---|---|
| POST | /report | submit takedown report — requires listing URL, reason, reporter email |

### Authentication

| Detail | Value |
|---|---|
| Token type | signed JWT bearer token |
| Token expiry | 24 hours |
| Refresh token expiry | 30 days |
| Read rate limit | 100 requests/minute/user |
| Write rate limit | 10 requests/minute/user |
| Unauthenticated requests | rejected on all endpoints except public read and reporting |

---

## Table L — Listing Velocity Limits

| Account age | Maximum listings per day |
|---|---|
| 0-30 days | 10 |
| 31+ days | 50 |

---

## Table M — Takedown Escalation

| Threshold | Action | Reversible |
|---|---|---|
| 1 upheld takedown | listing disabled | yes — curator contests and listing is re-enabled |
| 2 upheld takedowns in 12 months | listings disabled individually | yes — curator contests each |
| 3 upheld takedowns in 12 months | full subdomain suspension, manual review | yes — review may reinstate with warning or terminate permanently |

---

## Table N — Infrastructure Estimates at 1 Million Users

| Metric | Value |
|---|---|
| Trust graph edges | 200 million tuples (200 avg edges/user) |
| Listings database | ~5 GB (10 million listings at 500 bytes avg) |
| Typical page load | < 200 KB |
| Daily bandwidth at 1M daily page views | ~200 GB |
| Server requirement | single commodity server + CDN for static subdomain content |
| Estimated annual infrastructure cost | $50,000–$100,000 |
| Annual recurring revenue at $8/user | $8,000,000 |
| Gross margin on infrastructure | ~99% |
| Primary cost center | engineering personnel |
| Moderation team required | no |
| Trust and safety team required | no |

---

## Table O — Regulatory Compliance Summary

| Regulation | Classification | Key obligations | Features that reduce exposure |
|---|---|---|---|
| US Section 230 | interactive computer service | none beyond existing protections | curators are information content providers; user squelch is good-faith filtering under 230(c)(2) |
| EU Digital Services Act | hosting service | notice-and-action mechanism, point of contact, EU legal representative, terms of service, annual transparency report, notify authorities for serious criminal offenses | no content moderation avoids online platform obligations under Articles 20-24 |
| GDPR | data controller (account data), data processor (listing data) | lawful basis (contract performance), right to deletion within 30 days, right to data portability (JSON export), privacy of trust graph | minimal data collection, no public trust counts, trust graph private to each user |
| KOSA | not applicable | none | no infinite scroll, no autoplay, no push notifications, no algorithmic feeds, no engagement metrics, no DMs, no comments, no social comparison features |

---

## Table P — Data Stored Per User

| Data element | Storage | Deletion on account cancellation |
|---|---|---|
| Email address | platform database | deleted within 30 days |
| Payment method | third-party payment processor, not stored by platform | cancelled with processor |
| Trust graph edges | platform database | deleted within 30 days |
| Squelch list | platform database | deleted within 30 days |
| Squelch list subscriptions | platform database | deleted within 30 days |
| Login timestamps | platform database | deleted within 30 days |
| Listings (if curator) | platform database, curator subdomain | retained unless curator separately requests deletion |

---

## Table Q — Search Ranking Properties

| Property | Value |
|---|---|
| Scoring method | full-text search, term frequency and field matching |
| Field weighting | name matches rank higher than description matches |
| Personalization | none — same query returns same ranking for all users at same auth level |
| Trust graph effect | filtering only — removes results, does not reorder |
| Engagement signals | none — no click-through weighting, no popularity signal |
| External signals | none — no inbound links, no web crawl, no domain authority |
| Keyword stuffing defense | no term density reward beyond baseline relevance threshold |

---

## Table R — Defensive Properties Summary

| Property | Mechanism | Who enforces it |
|---|---|---|
| Financial cost of entry | $8/year + unique payment method per account | payment processors |
| Temporal cost of trust | trust requires real listings that real users find valuable | users through trust/squelch decisions |
| Collective visibility of consequences | notification dashboard shows squelch spikes with correlation data to every cabal member | each curator independently |
| Asymmetric action cost | one squelch removes entire cabal; rebuilding requires recreating entire trust network | users through one-click squelch |
| Squelch propagation | squelch list subscriptions spread defensive filtering across user base | users through voluntary subscription adoption |
| System hardening over time | accumulated squelch lists pre-squelch known bad actors for new users | users through squelch list publishing and adoption |
