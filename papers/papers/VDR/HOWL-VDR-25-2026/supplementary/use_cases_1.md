**Legacy COBOL Mainframe Integration**

A bank has a core banking system running COBOL on an IBM mainframe since 1978. The system processes every transaction, holds every account balance, manages every loan. Nobody fully understands it. The original developers retired decades ago. The documentation is partial, outdated, and contradicts the code in places. But the code exists, and it runs, and it's correct — forty-eight years of production prove that.

A VDR-LLM-Prolog processor runner connects to the mainframe's 3270 terminal interface through a granted network primitive. It doesn't replace the mainframe. It learns the mainframe.

The first phase is comprehension. The COBOL source is compacted into the KB tree — root.legacy.cobol.core_banking. Each COBOL paragraph becomes a KB with facts describing its inputs, outputs, side effects, and calling relationships. PERFORM statements become connection facts — calls(paragraph_a, paragraph_b). WORKING-STORAGE entries become data facts with their PIC clauses parsed into VDR-compatible type descriptions — PIC 9(7)V99 becomes a fact saying this field is a fixed-point decimal with 7 integer digits and 2 fractional digits, which maps exactly to a VDR fraction with denominator 100. No float. The COBOL was never using floats either — COBOL's packed decimal arithmetic is exact, and VDR preserves that exactness where a modern float-based system would destroy it.

The call graph becomes a queryable Prolog structure. "What paragraphs modify the account balance field?" is a query, not a code search. "What is the execution path from transaction input to ledger update?" is a scope walk through the call graph KB. "What copybooks does this program include?" is a fact lookup. The LLM understood the COBOL through judgment during compaction. The understanding is now structural — facts and rules at integer addresses, not prose in a document that nobody reads.

The second phase is interface generation. The bank wants a modern JSON API in front of the mainframe. A VDR-LLM-Prolog interactive session learns the mainframe's terminal protocol — which screen fields to fill, which function keys to press, what responses to expect. Each transaction type becomes a Prolog rule: to execute a balance inquiry, navigate to screen ACCT01, fill field at row 5 col 12 with the account number, press F5, read the balance from row 8 col 20. The terminal interaction is a sequence of granted network primitives orchestrated by Prolog. The response parsing uses grammars that know the screen layout.

The clone that handles an API request for account balance doesn't know COBOL. It knows Prolog rules that drive a terminal session. The COBOL executes on the mainframe exactly as it always has. The VDR-LLM-Prolog clone is a translation layer — JSON in, terminal protocol to mainframe, terminal response back, JSON out. The account balance comes back as a packed decimal value that maps to a VDR fraction with zero precision loss. The modern API returns exact values because both the source system and the transport system are exact.

The third phase is knowledge accumulation. Every transaction the system processes adds to the understanding. Edge cases that the terminal interaction rules don't cover — unusual screen flows, error screens, timeout conditions — trigger LLM judgment. Each resolution becomes a new rule. After a thousand transactions the system handles 95% of flows at level 3. The bank's institutional knowledge of how the mainframe actually behaves — not how the documentation says it behaves — is now encoded as queryable Prolog rules with provenance showing which transaction revealed each behavior.

The documentation problem is solved backwards. Instead of reading bad docs and hoping to understand the system, the VDR-LLM-Prolog system observed the system, encoded its behavior, and now the KB tree is the documentation. Accurate, queryable, maintained by usage, with every fact traceable to the observation that produced it.

---

**FORTRAN Scientific Computing Integration**

A national laboratory runs climate simulations in FORTRAN 77 code that has been evolving since 1983. Forty years of physics, parameterizations, bug fixes, and graduate student contributions. The code works. Nobody wants to rewrite it. But extracting results, comparing runs, and understanding what changed between model versions is a nightmare of custom scripts and tribal knowledge.

A VDR-LLM-Prolog system compacts the FORTRAN source into a KB tree. Each subroutine is a KB with facts about its arguments, COMMON block usage, and computational intent. COMMON blocks become shared data KBs — root.legacy.fortran.climate.common.atmos_state — with each variable as a fact including its type, dimensions, and physical meaning. The system preserves the FORTRAN's exact arithmetic semantics — REAL*8 variables are mapped with their precision limitations documented as VDR facts, so when a VDR exact computation produces a different result from the FORTRAN float computation, the provenance shows exactly where the float precision was insufficient.

The simulation outputs — netCDF files with thousands of variables over millions of grid points — are ingested by processor runners. Each output variable becomes a fact with its grid coordinates, time step, and value as a VDR fraction converted from the FORTRAN double at the boundary with the conversion precision logged. Now the output is queryable. "What was the sea surface temperature at 30N 60W at model year 2050 in run 247?" is a fact lookup, not a netCDF library call.

Comparing two model runs is a structural diff on two KB subtrees. Run 247 and run 248 are sibling KBs. The diff produces exact VDR fraction differences per variable per grid point. Conservation law verification is exact — total energy in minus total energy out equals zero or it doesn't, no tolerance, no "close enough." When the FORTRAN simulation violates conservation by 10^-12 due to float accumulation, the VDR system quantifies that violation exactly and traces it to the specific subroutine where the precision was lost.

Graduate students who can't read FORTRAN 77 can query the system in natural language. "What parameterization is used for cloud microphysics?" is a Prolog query against the subroutine KB. "What changed between the 1995 and 2003 versions of the radiation code?" is a structural diff on two versioned KBs of the compacted source. The FORTRAN is still running the simulation. The VDR-LLM-Prolog system is making forty years of scientific code comprehensible and queryable.

---

**AS/400 RPG Business Logic**

A manufacturing company runs its entire ERP on an AS/400 in RPG II and RPG IV. Inventory management, purchase orders, production scheduling, cost accounting. The RPG programs have been maintained by a succession of contractors, each with their own coding style, their own naming conventions, their own documentation habits. Some programs have no documentation. Some have documentation that describes a different version of the program.

The VDR-LLM-Prolog system compacts the RPG source. RPG's fixed-format column structure — operation codes in columns 28-32, factor 1 in 12-25, factor 2 in 33-42 — parses cleanly into structured facts. Each program becomes a KB. Each subroutine becomes a child KB. Data structures become fact sets with field positions, lengths, and types. The RPG's indicator-based logic — *IN01 through *IN99 — becomes Prolog facts about conditional execution paths.

The critical value is in the business rules embedded in the RPG. Pricing logic, discount tiers, tax calculations, inventory reorder points, production lead times — all encoded in RPG specifications that nobody can easily read but that correctly govern the business. The compaction extracts these rules as Prolog. A pricing calculation that spans 200 lines of RPG with nested indicators and CHAIN operations becomes a set of Prolog rules that express the same logic transparently. The VDR arithmetic matches the RPG's packed decimal arithmetic exactly — both are exact integer systems. The translation is lossless.

Now the company can answer questions they couldn't before. "What discount does customer class B get on product category 7 when ordering more than 500 units?" is a Prolog query, not a request to find the RPG programmer who wrote that logic in 1997. "If we change the reorder point for raw material X, which production schedules are affected?" is a dependency walk through the call graph KB.

The API layer works the same as the COBOL case. A JSON request comes in. A clone translates it into AS/400 operations through granted terminal or data queue primitives. The AS/400 does the work. The clone translates the response back. The RPG never changes. The VDR-LLM-Prolog system provides a modern interface and a queryable understanding of what the RPG actually does.

---

**Mixed Legacy Estate**

The worst case and the most common. A large organization has COBOL on the mainframe for core transactions, FORTRAN for engineering calculations, RPG on the AS/400 for ERP, a few Visual Basic 6 applications for departmental workflows, some Perl CGI scripts from 1999 that somehow still run the intranet, and a Java monolith from 2008 that was supposed to replace everything but ended up as another layer.

Each legacy system gets its own branch of the KB tree. root.legacy.cobol, root.legacy.fortran, root.legacy.rpg, root.legacy.vb6, root.legacy.perl, root.legacy.java. Each is compacted independently. Each has its own terminal interaction rules, its own data format grammars, its own API translation layer.

The value emerges at the integration level. A Prolog rule at root.legacy can express cross-system relationships that no single system knows about. "When the mainframe processes a large transaction, the RPG system needs to update inventory, and the Java system needs to send a notification." That workflow currently exists as tribal knowledge in the heads of three different specialists. Now it's a Prolog rule with provenance, auditable, executable, and maintained by usage.

The customer ID in the COBOL system, the customer number in the RPG system, and the client ID in the Java system are three different fields in three different formats referring to the same entity. A mapping KB at root.legacy.mappings holds facts: maps_to(cobol_customer_id("00847293"), rpg_customer_num(847293), java_client_id("C-847293")). A Prolog rule normalizes across systems. A query for "all activity for customer 847293" walks all three legacy branches through the mapping and returns a unified view. No ETL pipeline. No data warehouse. The data stays in the legacy systems. The VDR-LLM-Prolog system provides the unified query layer.

---

**Writing a Novel**

A novelist wants to write a 90,000-word fantasy novel. They start an interactive session. The first phase is worldbuilding — they describe the magic system, the political structures, the geography, the history. Each element becomes facts in a KB tree: root.projects.novel.world.magic, root.projects.novel.world.politics, root.projects.novel.world.geography. The magic system's rules are Prolog — literally. "A mage who exceeds their capacity suffers backlash proportional to the excess" is a constraint with exact VDR arithmetic. The political alliances are connection facts between kingdom KBs. The geography is facts about distances, terrain, travel times.

Characters are KBs. root.projects.novel.characters.elena has facts: age, role, motivation, relationships (connections to other character KBs), knowledge (what this character knows — scoped, so Elena doesn't know what the villain is planning because the villain's plans are in a sibling branch she can't see). Character arcs are rules: if Elena discovers fact X, her motivation shifts from Y to Z. This fires later during plotting.

The plot outline is a queue of scene KBs. Each scene has location (reference to geography KB), characters present (references to character KBs), purpose (fact: what changes by the end of this scene), and constraints (the scene must not contradict established facts — a constraint that fires at assertion time).

Now the novelist writes. For each scene, they clone the novel session. The clone has the full worldbuilding state, the character states as of this point in the narrative, the plot context. The LLM generates prose — this is genuine level 1 work, creative writing, the LLM's natural strength. But the prose is grounded. When Elena casts a spell, the magic system rules evaluate whether it's within her capacity. When she travels from city A to city B, the geography facts provide the correct travel time. When she mentions a historical event, the history KB provides the correct details. The LLM creates. The KB tree fact-checks.

Continuity is structural. If chapter 12 establishes that Elena has a scar on her left hand, that's a fact on her character KB. If chapter 34 references the scar, the LLM queries the fact and gets it right — left hand, not right. No continuity spreadsheet. No re-reading earlier chapters. The fact is at an integer address.

The novelist can branch the story. Snapshot the current state, clone it, try a different plot direction. If it works, keep it. If not, return to the snapshot and try another direction. Version control for narrative. The abandoned branch stays in the tree with provenance showing when and why it was abandoned — useful later if the novelist wants to revisit the idea.

A series with multiple books is a KB tree where each book is a child of the series KB. Character state carries forward. Worldbuilding accumulates. A new book inherits everything from the series and prior books. The LLM writing book 3 has exact access to every fact from books 1 and 2. No "let me re-read the previous books to maintain consistency." The consistency is structural.

---

**News Article Production**

A news organization needs to produce 50 articles per day across multiple beats — politics, technology, business, science, sports. Each beat is a branch of the KB tree: root.newsroom.beats.politics, root.newsroom.beats.tech, and so on. Each beat accumulates facts from prior coverage — sources, quotes, background context, ongoing story threads.

A reporter on the tech beat gets a tip about a company layoff. They start an interactive session. The LLM helps research — fetching the company's SEC filings through granted network primitives, checking prior coverage in the beat KB, querying the source database for relevant contacts. Each piece of information lands as a fact with provenance — SEC filing from this URL on this date, prior article from this date with these claims.

The reporter conducts interviews. Quotes enter as facts with attribution — quote(source_id, text, timestamp, context). The source's identity is scoped — if the source is on background, the source fact is in the reporter's owner-only KB. If on the record, it's in the story KB at internal visibility. The editorial chain can see it. The public can't until publication.

The LLM drafts the article. This is level 1 — genuine creative work, narrative structure, tone, news judgment. But every factual claim in the draft is grounded to a fact in the KB. "The company laid off 200 employees" links to the SEC filing fact. "Revenue declined 15% year over year" links to the financial data facts with exact VDR fractions — 15/100, not a float. The editor can click any claim and see its provenance chain.

The article goes through editorial review. An editor clone — a different snapshot configured for editorial judgment — reads the draft and checks it against the newsroom's style guide (Prolog rules), legal review checklist (constraints), and fact-checking requirements (each factual claim must have a provenance chain to a primary source). The editor clone doesn't rewrite — it flags issues. "Claim in paragraph 4 has no primary source provenance." "Attribution in paragraph 7 uses passive voice, style guide requires active." These are rule evaluations, not opinions.

After publication, the article's facts are promoted to the beat KB. The company's layoff count, the revenue figures, the executive quotes — all become part of the institutional knowledge base. The next reporter covering this company inherits those facts. Six months later when the company announces results, the new reporter's session has exact prior figures for comparison. "Revenue declined from X to Y, a Z% decrease" where X, Y, and Z are exact VDR fractions traced to their original SEC filings.

The wire service integration is a processor runner. AP and Reuters feeds come in as a stream. The processor compacts each wire story, extracts entities and claims, checks them against the beat KBs for overlap with ongoing coverage, and pushes alerts to beat-specific queues. The politics reporter's queue gets politics stories. The tech reporter's queue gets tech stories. Each alert has structured facts ready for the reporter to incorporate into their own coverage with provenance showing the wire source.

---

**Popular Blog Production**

A content creator runs a blog about personal finance. They've written 500 posts over five years. All 500 are compacted into root.blog.archive, each post a KB with facts about the advice given, the data cited, the examples used, the tone, the audience response metrics.

When they write a new post about index fund investing, the LLM session has access to every prior post that mentioned index funds. Not through search — through Prolog queries against structured facts. "What did I previously say about expense ratios?" returns exact facts from three prior posts with dates and context. "Have I contradicted myself on dollar-cost averaging?" is a consistency check — a Prolog rule that looks for claims about the same topic with different conclusions.

The blogger's voice is encoded in the language KB — sentence structure preferences, vocabulary choices, recurring metaphors, paragraph rhythm. The weight profile says: conversational, second-person, short paragraphs, concrete examples over abstractions. The LLM generates prose at level 1 but the structural tokens — paragraph breaks, heading patterns, list formats — come from grammars that match the blogger's established style. The output reads like the blogger, not like an LLM.

SEO optimization is Prolog rules over a keyword KB. Target keyword density is a VDR fraction — 2/100 of total words. The grammar tracks word count and keyword count during generation. If density drops below target, the LLM is nudged through a constraint. If density exceeds 3/100, the constraint prevents keyword stuffing. These are exact fraction comparisons, not float approximations that might round differently on different platforms.

The editorial calendar is a queue. Posts are planned as facts — topic, target date, target keyword, related prior posts. A polling runner checks the calendar daily. If a post is due within 3 days and hasn't been started, it pushes an alert. If a post references seasonal content — tax season, holiday spending — temporal rules fire at the appropriate time. "It's January, the annual portfolio rebalancing post should be drafted" is a Prolog rule that checks the calendar against the current date.

Affiliate link management is facts with expiration. Each affiliate partnership has a start date, end date, and disclosure requirement. A constraint ensures every post mentioning a partner product includes the disclosure text. The constraint fires at assertion time — before the post is published, never after. When a partnership expires, the end date fact triggers a rule that flags all posts containing that affiliate link for review. The flags are facts in the archive KB, queryable by the blogger during their next session.

---

**Academic Paper Writing**

A research group writes papers collaboratively. Each paper is a project KB. The literature review is a set of compacted prior papers — each one a KB with facts about claims, methods, results, and limitations. Citations are connection facts between the paper KB and the cited paper KBs. A citation isn't a string — it's a typed connection with provenance showing when the citation was added and which claim it supports.

When a researcher writes "Smith et al. showed that X leads to Y," the claim is grounded to a fact in the compacted Smith paper KB. If Smith actually showed that X correlates with Y but didn't establish causation, the constraint fires — the claim's verb "leads to" implies causation, but the source fact says correlation. The researcher gets a flag before submission, not a retraction after.

Figures and tables reference data KBs with exact VDR values. "Our method achieved 94.7% accuracy" is 947/1000 in the results KB. The figure grammar generates the table with exact values. When the paper goes through revision and accuracy improves to 95.2%, changing one fact — 952/1000 — updates every table and every prose reference. No searching through the manuscript for every mention of the old number.

Co-authors work on separate branches. Each author's session writes to their branch. The lead author merges by reviewing structural diffs between branches — which facts were added, which claims were modified. Merge conflicts are detectable — two authors made different claims about the same result. The conflict is a queryable fact, not a git merge conflict in a LaTeX file.

---

The common thread across all of these is that the VDR-LLM-Prolog system treats every domain as structured data at integer addresses with exact arithmetic, full provenance, and queryable relationships. The COBOL mainframe's packed decimal maps to VDR fractions losslessly. The novelist's worldbuilding rules map to Prolog constraints. The newsroom's fact-checking requirements map to provenance chain queries. The blogger's SEO targets map to VDR fraction comparisons.

The LLM does what it's good at in every case — understanding intent, making judgments, generating prose. Everything else is structure. The Remainder in VDR is not residual error. It is first-class structural information that the system acts on. That principle extends from arithmetic through knowledge management through application development through every domain where exact, traceable, queryable computation matters.
