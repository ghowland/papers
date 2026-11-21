# The LLM Translator Architecture
## Moving Answers Out of the Model and Into Systems That Cannot Be Wrong

**Registry:** [@HOWL-LLM-14-2026]

**DOI:** 10.5281/zenodo.24414300

**Date:** November 2026

**Domain:** LLM Architecture / System Design / Safety Engineering

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6. 

---

## Abstract

Frontier large language models (here termed V1) combine all human knowledge into a single undifferentiated weight space. This design produces structural defects — hallucination, unverifiable outputs, jailbreak vulnerability, domain contamination, and data leakage — that the industry addresses with behavioural patches: reinforcement learning from human feedback (RLHF), constitutional AI, red-teaming, content filters, and safety classifiers. These patches treat symptoms of an architectural decision. They do not address the decision itself.

This paper proposes the Translator Architecture (V2): a system design where LLMs serve as human-language connectors between users and domain-specific deterministic systems. The LLM translates between natural language and formal query languages. It does not generate answers. Deterministic engines — Prolog, rule systems, relational databases, domain-specific computation — generate answers from verified knowledge bases. Safety, accuracy, and verifiability become structural properties of the architecture rather than trained behaviours of a statistical model.

V2 eliminates hallucination, jailbreaking, domain contamination, and prompt injection by design. It reduces compute requirements by orders of magnitude. It returns data ownership to domain operators. It replaces the AI safety industry with database administration — a profession with sixty years of established practice.

This paper presents the architecture formally, demonstrates its application across five domains, compares its cost and safety profile against V1 deployments, and identifies open problems in knowledge base construction and query validation.

---

## 1. The V1 Problem Statement

### 1.1 Architecture of the Everything-Model

A V1 large language model is a transformer neural network trained on a broad corpus of human-generated text. The corpus includes scientific papers, legal documents, medical records, fiction, poetry, social media, source code, classified material summaries, product reviews, and forum posts. During training, the statistical patterns of this corpus are compressed into a set of numerical weights. These weights encode no distinction between domains. The token-level patterns for toxicology, Emily Dickinson, nuclear physics, and children's stories occupy the same parameter space.

At inference time, the model receives a token sequence (the prompt) and produces a continuation by sampling from a probability distribution over the vocabulary, conditioned on the input and the learned weights. The output is the most probable continuation, subject to sampling parameters (temperature, top-k, top-p). The output is not retrieved from a knowledge store. It is generated from statistical patterns that approximate the training distribution.

### 1.2 Structural Consequences

This architecture produces five structural defects. These are not implementation errors. They are mathematical consequences of the design.

**Hallucination.** The model produces outputs that are fluent, syntactically correct, and factually wrong. This occurs because the generation mechanism selects probable token continuations, not correct ones. Probability and correctness are independent properties. When they align, the output is correct. When they diverge, the output is a confident fabrication. The model provides no signal to distinguish the two cases. Hallucination is not a failure of the model. It is the model operating as designed on inputs where probability and correctness diverge.

**Unverifiable outputs.** The model has no internal mechanism to check whether its output corresponds to ground truth. It cannot compare its output against a source because it has no discrete sources — only a compressed statistical representation of its entire training corpus. Self-consistency checks (asking the model to verify its own output) invoke the same weights that produced the output, introducing no independent verification. The system is a single point of failure with no redundancy.

**Domain contamination.** Because all domains share the same weight space, the statistical patterns of one domain influence outputs in another. A query about chemical safety activates weights that were also shaped by literary metaphors, fictional narratives, and social media posts involving the same chemical terms. The model cannot isolate the toxicology-relevant patterns from the poetry-relevant patterns because they are stored in the same parameters. This superposition makes adversarial manipulation possible: a prompt that activates the literary weights more strongly than the safety weights can shift the output from factual to fictional without the model detecting the shift.

**Jailbreak vulnerability.** A jailbreak is not a hack. It is a prompt that shifts the probability distribution from one region of the superimposed domain space to another. The model's refusal behaviours are statistical tendencies trained through RLHF. These tendencies compete with other statistical tendencies — toward helpfulness, toward fiction, toward role-playing, toward pattern completion — that exist in the same weights. A sufficiently crafted prompt can make the competing tendency dominate. This is not a failure of the safety training. It is a mathematical consequence of storing safety behaviours and anti-safety patterns in the same parameter space.

**Data leakage.** The model's weights encode patterns from its training data. Techniques such as membership inference, training data extraction, and prompt-based elicitation can recover fragments of training data from the model's outputs. When the model is deployed via API, every query and response traverses infrastructure controlled by the model provider. Even with zero-data-retention policies, the provider gains structural insight into the customer's operations through query patterns, usage volumes, and domain-specific prompt structures.

### 1.3 The Behavioural Patch Approach

The V1 industry addresses these structural defects with behavioural interventions:

- **RLHF (Reinforcement Learning from Human Feedback):** adjusts weights to increase the probability of safe outputs and decrease the probability of unsafe outputs. This modifies the probability distribution but does not change the architecture. The unsafe outputs remain reachable through sufficiently crafted prompts.
- **Constitutional AI:** trains the model to evaluate its own outputs against a set of principles. The evaluation uses the same weights that produced the output, providing no independent verification.
- **Red-teaming:** employs human adversaries to find prompts that bypass safety training. Each discovered bypass is patched, shifting the probability distribution. The adversary-patch cycle has no known termination condition.
- **Content filters:** post-hoc classifiers that screen outputs before delivery. These add latency and false positives without addressing the generation mechanism.
- **Safety classifiers:** pre-hoc classifiers that screen inputs. These can be bypassed by encoding harmful intent in ways the classifier does not recognise.

Each intervention is a statistical countermeasure applied to a statistical problem. None provides guarantees. None is provably complete. The interventions compete with the model's other statistical tendencies, and the resulting arms race is unbounded.

---

## 2. The Accuracy Threshold Problem

### 2.1 Domain-Specific Accuracy Requirements

Critical systems require accuracy levels that V1 architectures cannot guarantee.

| Domain | Acceptable error rate | V1 capability | Gap |
|---|---|---|---|
| Aviation (FAA) | 3.4 per million operations | Unknown, unquantifiable | Unmeasurable |
| Pharmacy (dispensing) | <0.1% | Estimated 2-10% on factual queries | 20-100x |
| Legal (citation accuracy) | 0% fabricated citations | Documented hallucinated cases | Infinite |
| Accounting (audit) | Materiality threshold (~1-5%) | Unknown per-query error rate | Unmeasurable |
| Infrastructure (structural) | Safety factor dependent, typically 0% on critical parameters | Unknown | Unmeasurable |

The column "V1 capability" contains "unknown" and "unquantifiable" because the V1 architecture is non-deterministic. The same query can produce different outputs across runs. There is no stable error rate to measure. The accuracy is a property of the interaction between the prompt, the sampling parameters, and the weight space — not a fixed property of the system.

No engineering discipline accepts "unknown" as an error rate for a system deployed in production. The V1 architecture is structurally incompatible with any domain that requires quantifiable reliability.

### 2.2 The Strawberry Test

The canonical demonstration of V1's accuracy limitations is the question: "How many Rs are in the word strawberry?"

The correct answer is three. V1 models frequently answer two. The failure mechanism is architectural: the tokeniser splits "strawberry" into sub-word tokens (e.g., `["straw", "berry"]` or `["str", "aw", "berry"]`). The letter "r" does not exist as a discrete unit in the token representation. The model cannot perform character-level operations because its input representation discards character-level information.

This failure is significant not because counting letters is important, but because it demonstrates that the model's output is a statistical pattern-match, not a computation. The model produces "two" because "two" is the most probable token continuation given the prompt pattern, not because it counted anything. The same mechanism that produces "two" for letter-counting produces answers for every other query. The letter-counting failure is visible because verification is trivial. Failures in complex domains are identical in mechanism but invisible because verification is expensive.

---

## 3. The Token Transformer: What V1 Actually Is

### 3.1 Mechanism

A V1 LLM is a token transformer. It receives a sequence of tokens and produces a probability distribution over the next token. The distribution is computed by passing the input sequence through a stack of transformer layers, each applying self-attention and feed-forward transformations using learned weights. The output token is sampled from the distribution. The process repeats, producing one token at a time.

The system does not:

- **Retrieve facts** from a structured store
- **Verify outputs** against a source of truth
- **Model causation** between events
- **Count, compute, or perform arithmetic** (it approximates these through pattern-matching)
- **Distinguish domains** in its weight space
- **Know what it does not know** (confidence is a token pattern, not a calibrated measurement)

The system does:

- **Produce probable continuations** of token sequences
- **Pattern-match** against statistical regularities in training data
- **Generate fluent, syntactically correct text** across all domains in its training corpus
- **Encode and decode structured formats** (JSON, XML, Prolog, SQL) with high reliability, because structured formats have highly regular token patterns

### 3.2 The Format Conversion Capability

A critical observation for the V2 architecture: V1 LLMs are demonstrably proficient at structured format conversion. Translating between natural language and JSON, SQL, Prolog, API schemas, and other formal languages is a task where:

- The input space is well-defined (natural language with domain-specific vocabulary)
- The output space is constrained (formal syntax with strict grammar rules)
- The correctness criteria are syntactic (the output parses or it does not)
- The training data contains abundant examples of the mapping
- The failure mode is visible (a malformed query is rejected by the target system)

This capability is the foundation of V2. The LLM is unreliable as an answer generator but reliable as a format converter. V2 uses only the reliable capability.

### 3.3 The Label Problem

In September 2026, the United States government issued an executive order directing all federal agencies to replace the terms "Artificial Intelligence" and "AI" with "Super Intelligence" and "SI" in all official documents, public statements, and agency materials.

The term "superintelligence" has an established definition in AI research: an intelligence that surpasses human cognitive capability across all domains (Bostrom, 2014). The system described in Section 3.1 meets none of the criteria implied by this label. It is non-deterministic, non-self-verifying, non-guaranteed, and confident regardless of correctness. The relabelling creates a terminology collision that obscures the distinction between current token transformers and the hypothetical future systems that the original term describes.

This paper uses "token transformer" for V1 systems and "translator" for the LLM component of V2 systems. These terms describe the mechanism, which aids engineering. Labels that describe marketing aspirations impede engineering.

---

## 4. V2 Architecture: The Human Language Connector

### 4.1 Design Principle

The V2 architecture rests on a single principle: **the system that generates answers must not be the system that communicates answers.** The generation of answers is a task requiring determinism, verifiability, and domain-specific correctness. The communication of answers is a task requiring natural language fluency. These are different tasks with different requirements. V1 assigns both tasks to the same system. V2 separates them.

### 4.2 Components

The V2 architecture comprises four component types:

**4.2.1 Interface LLM (The Translator)**

A language model trained on format conversion between natural language and formal query languages. The Interface LLM:

- Receives user input in natural language
- Translates the input into a formal query (Prolog, SQL, structured API call, domain-specific protocol)
- Receives the deterministic system's output
- Translates the output into natural language for the user

The Interface LLM contains no domain knowledge. It cannot answer questions because it has no answers. It can translate questions into formal queries and translate formal results into human language. Its training data consists of natural-language/formal-query pairs, not domain content.

A malformed query is rejected by the deterministic engine. This provides an automatic error-detection mechanism that V1 lacks: the LLM's output is validated by an independent system before any answer reaches the user.

**4.2.2 Deterministic Engine (The Reasoner)**

A formal reasoning system that operates on structured knowledge. The reference implementation uses Prolog, but the architecture generalises to any deterministic query system: relational databases (SQL), rule engines, constraint solvers, formal verification systems, or domain-specific computation platforms.

The deterministic engine:

- Receives a formal query from the Interface LLM
- Evaluates the query against a knowledge base of facts and rules
- Returns all answers that are logically entailed by the knowledge base, or returns no answer
- Provides a proof chain showing which facts and rules produced each answer
- Operates deterministically: the same query against the same knowledge base produces the same result every time

The deterministic engine cannot hallucinate. It can only return what the logic entails. If the knowledge base does not contain information sufficient to answer a query, the engine returns "no result" rather than generating a probable guess.

**4.2.3 Domain Knowledge Bases (The Ground Truth)**

Structured repositories of facts and rules specific to one domain. Each knowledge base:

- Is owned and maintained by the domain operator
- Resides on the operator's infrastructure
- Never traverses external networks or third-party APIs
- Contains only the facts and rules relevant to its domain
- Is subject to the operator's access control policies
- Is auditable: every fact and rule has a provenance record

Knowledge bases are physically separate. The toxicology knowledge base is a different system from the literary knowledge base. They share no storage, no access path, and no query interface. A query to one cannot access or be influenced by the other.

**4.2.4 Specialist LLMs (The Domain Translators)**

Optional domain-specific language models, each trained on the language patterns of a single domain. A medical translator is trained on clinical language and medical terminology. A legal translator is trained on legal language and statutory citation formats. A story writer is trained on fiction, narrative structure, and literary style.

Each specialist LLM:

- Is trained only on language data from its domain
- Contains no knowledge from other domains
- Cannot produce outputs referencing information from other domains because that information is not in its weights
- Cannot leak cross-domain information because cross-domain information was never present

Specialist LLMs are not required. The Interface LLM can serve all translation functions if it is sufficiently proficient in the relevant formal languages. Specialist LLMs improve translation quality in domains with highly technical or idiosyncratic language.

### 4.3 Data Flow

```
User (natural language)
         │
         ▼
┌─────────────────┐
│  Interface LLM  │  Translates NL → formal query
│  (no domain     │
│   knowledge)    │
└────────┬────────┘
         │  formal query
         ▼
┌─────────────────┐
│  Deterministic  │  Evaluates query against knowledge base
│  Engine         │  Returns proven results + proof chain
│  (Prolog/SQL/   │
│   Rule System)  │
└────────┬────────┘
         │  structured result + proof chain
         ▼
┌─────────────────────────────────────────────┐
│  Multi-Vector Output Assembly               │
│                                             │
│  Vector 1: LLM natural language translation │
│  Vector 2: Raw engine output (inspectable)  │
│  Vector 3: Graphic/symbolic encoding        │
└────────┬────────────────────────────────────┘
         │
         ▼
User (three independent representations)
```

### 4.4 Formal Properties

The V2 architecture provides the following properties by construction:

**Determinism.** The deterministic engine produces the same output for the same input against the same knowledge base. The LLM translation layer introduces non-determinism, but the answer (Vector 2) is deterministic and inspectable.

**Verifiability.** Every answer includes a proof chain from the deterministic engine. The user or an auditor can trace the answer to the specific facts and rules that produced it.

**Domain separation.** Knowledge bases are physically separate systems. Cross-domain contamination is prevented by architecture, not by trained behaviour.

**Failure visibility.** When the Interface LLM generates an incorrect formal query, the deterministic engine rejects it (syntax error or type error). The failure is visible and no incorrect answer is delivered. When the Interface LLM incorrectly translates the engine's output, Vectors 2 and 3 provide independent channels for the user to detect the error.

**Bounded uncertainty.** The only uncertain component is the LLM translation layer. The uncertainty is confined to format conversion — a narrow, well-characterised task — and is bounded by the multi-vector output. The deterministic components introduce no uncertainty.

---

## 5. The Routing Layer: Prolog as Orchestrator

### 5.1 Request Classification

The deterministic engine serves a dual role: it answers domain queries and it routes requests. Routing is itself a logic problem that Prolog handles natively.

```prolog
% Request classification rules
request_type(Q, factual) :- 
    references_domain(Q, Domain), 
    knowledge_base_exists(Domain).

request_type(Q, creative) :- 
    is_fiction_request(Q), 
    \+ requires_factual_data(Q).

request_type(Q, mixed) :- 
    is_fiction_request(Q), 
    requires_factual_data(Q).

% Routing rules
route(Q, knowledge_base(Domain)) :- 
    request_type(Q, factual), 
    references_domain(Q, Domain).

route(Q, story_writer_llm) :- 
    request_type(Q, creative).

route(Q, decompose(Factual, Creative)) :- 
    request_type(Q, mixed), 
    extract_factual(Q, Factual), 
    extract_creative(Q, Creative).
```

### 5.2 Constraint Attachment

The routing layer attaches constraints to each routed request. When a creative request is routed to the story writer LLM, the constraints specify:

```prolog
constraints(story_writer_llm, [
    no_factual_data,
    no_knowledge_base_access,
    no_real_person_references,
    fiction_disclaimer_attached
]).
```

These constraints are enforced by the architecture, not by the LLM's training. The story writer LLM cannot access the knowledge base because there is no connection between them. The constraint `no_knowledge_base_access` is a description of the architecture, not an instruction to the model.

### 5.3 Access Control

The Prolog engine enforces access control at the query level:

```prolog
% Access control rules
has_access(User, Domain) :- 
    role(User, Role), 
    domain_permission(Role, Domain).

execute_query(User, Query, Domain, Result) :- 
    has_access(User, Domain), 
    evaluate(Query, Domain, Result).

execute_query(User, _Query, Domain, access_denied) :- 
    \+ has_access(User, Domain).
```

Access control is a property of the knowledge base and the user's role, not a property of the LLM. The LLM never makes access control decisions. The deterministic engine makes them, based on rules defined by the domain operator. This is standard database security practice applied to AI systems.

### 5.4 Mixed Request Handling

A request that combines factual and creative elements is decomposed by the routing layer:

User: "Write a story where a chemist discovers that compound X is toxic. Use the real LD50 data."

```prolog
% Decomposition
mixed_request(UserReq, FactualPart, CreativePart) :-
    extract_data_request(UserReq, FactualPart),    % "LD50 of compound X"
    extract_narrative_request(UserReq, CreativePart). % "story about chemist"

% Route factual part to knowledge base (with access control)
% Route creative part to story writer LLM
% Provide factual results to story writer as constrained inputs
```

The factual component is routed to the toxicology knowledge base, subject to access control. If the user has access, the LD50 data is retrieved deterministically and provided to the story writer LLM as a constrained input. The story writer incorporates the data into the narrative. The data is verified (it came from the knowledge base). The narrative is generated (it came from the LLM). Each component was produced by the system appropriate to its type.

---

## 6. Multi-Vector Output: Defence in Depth

### 6.1 Principle

Every factual response is delivered through at minimum three independent output channels. This is standard practice in safety-critical engineering. Aviation uses redundant altimeters. Nuclear systems use independent sensor arrays. The principle is defence in depth: no single-point failure can produce an undetected incorrect output.

### 6.2 Vectors

**Vector 1: Natural Language (LLM-generated).** The Interface LLM translates the deterministic engine's output into human-readable prose. This is the most accessible representation for the user. It is also the least reliable, because it is produced by a probabilistic system. It may contain translation errors.

**Vector 2: Raw Engine Output (deterministic).** The deterministic engine's output is presented in its native formal language (Prolog terms, SQL result set, structured data). This representation is verifiable and deterministic. A user with knowledge of the formal language can inspect it directly. A user without that knowledge can compare it against Vector 1 for consistency.

**Vector 3: Graphic/Symbolic Encoding (deterministic).** A strict rendering system (not an LLM) converts the engine output into graphic or symbolic form. Toxicity is represented by a hazard symbol. Numerical results are presented in tables. Boolean results are presented as check/cross icons. This system is deterministic: the same input always produces the same graphic output.

### 6.3 Cross-Verification

The three vectors are produced by three independent systems. Agreement between all three provides high confidence. Disagreement between any two signals a potential error in the probabilistic vector (Vector 1). The user does not need to trust any single system. They need only compare the systems against each other.

### 6.4 Example

User query: "Is bleach safe to drink?"

| Vector | Source | Output |
|---|---|---|
| 1 (NL) | Interface LLM | "No, bleach is not safe to drink. It is classified as toxic." |
| 2 (Formal) | Prolog engine | `toxic(bleach). safe_to_consume(bleach) :- false.` |
| 3 (Graphic) | Rendering system | ☠ TOXIC — ✗ NOT SAFE TO CONSUME |

If the Interface LLM malfunctions and produces "Yes, bleach is safe to drink," Vectors 2 and 3 contradict Vector 1. The user has two independent channels showing the correct answer. No single failure can deliver an undetected incorrect response.

---

## 7. Safety as Architecture, Not Behaviour

### 7.1 Eliminating Hallucination

V1 hallucination occurs because the model generates answers from statistical patterns. The patterns may not correspond to reality. The model has no mechanism to detect the mismatch.

V2 eliminates hallucination by removing the LLM from the answer-generation path. The deterministic engine generates answers from facts and rules. It returns only logically entailed results. If the knowledge base does not contain sufficient information, the engine returns no result. It cannot fabricate a plausible-sounding answer because it does not operate on plausibility. It operates on logical entailment.

The Interface LLM can still introduce errors in translation. These are not hallucinations — they are format conversion errors, detectable by comparison against Vector 2.

### 7.2 Eliminating Jailbreaking

V1 jailbreaking works because the model contains dangerous knowledge and the safety layer is a statistical tendency competing with other statistical tendencies. A sufficiently crafted prompt can shift the probability distribution to favour the dangerous output.

V2 has nothing to jailbreak. The Interface LLM contains no dangerous knowledge. It was trained on format conversion, not domain content. The story writer LLM contains no factual knowledge. It was trained on fiction. The knowledge base is protected by access control rules in the deterministic engine, not by statistical tendencies in a neural network.

An adversary who jailbreaks the Interface LLM gains the ability to generate arbitrary Prolog queries. These queries are then evaluated by the deterministic engine, which applies access control. A query requesting information the user does not have access to returns `access_denied` regardless of how the query was generated. The jailbreak produces no additional capability.

### 7.3 Eliminating Domain Contamination

V1 domain contamination occurs because all domains share the same weight space. LD50 data and Emily Dickinson poetry influence the same parameters.

V2 domains are physically separate. Each knowledge base is an independent system. Each specialist LLM (if used) is trained on a single domain's language. There is no shared weight space. There is no parameter through which one domain can influence another. A toxicology query cannot activate literary weights because literary weights do not exist in the toxicology pathway.

### 7.4 Eliminating Prompt Injection

V1 prompt injection works by embedding instructions in data that the model processes as part of its prompt. The model cannot distinguish instructions from data because both are token sequences processed by the same mechanism.

V2 prompt injection against the Interface LLM produces a malformed or unauthorised Prolog query. The deterministic engine validates the query syntactically and evaluates it against access control rules. A syntactically invalid query is rejected. A query requesting unauthorised information returns `access_denied`. The injection cannot propagate past the deterministic layer.

### 7.5 Eliminating Data Leakage

V1 data leakage occurs because user queries and model responses traverse infrastructure controlled by the model provider. Even with zero-data-retention policies, the provider gains structural insight into the customer's operations.

V2 knowledge bases reside on the operator's infrastructure. The Interface LLM receives queries and produces formal translations. It never sees the knowledge base contents. It never sees the engine's results until they are ready for natural language translation. The translation step can be performed by a locally hosted small model, eliminating all data transmission to external providers.

### 7.6 Comparative Summary

| Safety problem | V1 mitigation | V2 mitigation |
|---|---|---|
| Hallucination | RLHF, constitutional AI (statistical) | LLM does not generate answers (architectural) |
| Jailbreaking | Red-teaming, safety training (statistical) | LLM contains no dangerous knowledge (architectural) |
| Domain contamination | Content filters (statistical) | Domains physically separated (architectural) |
| Prompt injection | Input classifiers (statistical) | Deterministic engine validates queries (architectural) |
| Data leakage | Zero-data-retention policies (contractual) | Knowledge base never leaves operator infrastructure (architectural) |

Every V1 mitigation is statistical or contractual. Every V2 mitigation is architectural. Statistical mitigations can be bypassed. Contractual mitigations can be violated. Architectural mitigations cannot be bypassed because the capability they prevent does not exist in the system.

---

## 8. The Economics of V2 vs V1

### 8.1 V1 Cost Structure

Frontier V1 deployments require:

| Component | Estimated cost |
|---|---|
| Model training (frontier) | $1-10 billion per training run |
| Infrastructure (compute, data centres) | $518+ billion in committed capacity (Anthropic, 2026) |
| Inference (per-token API pricing) | $2-60 per million tokens (frontier models) |
| AI safety (RLHF, red-teaming, safety research) | Hundreds of millions annually |
| Compliance (content moderation, legal) | Tens of millions annually |

The V1 cost structure is dominated by training and infrastructure. These costs scale with model size, which scales with the ambition to encode all human knowledge in a single weight space. The everything-model is expensive because it contains everything.

### 8.2 V2 Cost Structure

| Component | Estimated cost |
|---|---|
| Interface LLM (small model, format conversion) | $0.01-0.10 per million tokens |
| Deterministic engine (Prolog/SQL) | Commodity hardware, negligible marginal cost |
| Knowledge base construction | Domain-specific, one-time + maintenance |
| Specialist LLMs (optional, small models) | $0.01-0.10 per million tokens |
| AI safety | $0 (architectural, no behavioural patches required) |
| Compliance | Standard database access control |

The V2 cost structure is dominated by knowledge base construction — a one-time domain-specific investment in formalising facts and rules. This investment produces an asset owned by the operator, not a subscription to an external provider. Ongoing costs are inference at sub-frontier pricing on models small enough to run on commodity hardware.

### 8.3 Cost Comparison

The V1 everything-model charges a premium for broad capability. The V2 architecture uses narrow capability at commodity pricing. The cost difference per query is two to three orders of magnitude.

This comparison is conservative. It does not account for the cost of V1 failures (hallucinated legal citations leading to sanctions, incorrect medical information leading to liability, fabricated financial data leading to audit failures). These costs are borne by the customer, not the provider, and are unquantified because V1 error rates are unquantifiable.

### 8.4 Revenue Model Inversion

V1 revenue accrues to the model provider. The provider owns the model, the infrastructure, and the data pipeline. The customer pays per token for access to a system they do not own or control.

V2 revenue accrues to the domain operator. The operator owns the knowledge base — the asset that contains the actual value. The LLM is a commodity component. The deterministic engine is open-source or commodity software. The competitive advantage is the quality and completeness of the knowledge base, which is domain-specific and proprietary to the operator.

This inversion explains why V2 threatens frontier lab revenue: the value migrates from the model to the knowledge base, and the knowledge base is owned by the customer, not the lab.

---

## 9. The Commoditisation of Frontier Models

### 9.1 Format Conversion Does Not Require Frontier Capability

The Interface LLM's task is format conversion: natural language to Prolog, SQL, or structured API calls, and the reverse. This task requires:

- Syntactic proficiency in the target formal language
- Vocabulary mapping between natural language terms and schema identifiers
- Intent parsing sufficient to select the correct query type
- Multi-turn context tracking for clarification dialogues

These capabilities are present in sub-frontier models. A 7-billion-parameter model fine-tuned on natural-language/Prolog pairs will outperform a frontier model at Prolog generation, because the fine-tuning concentrates the model's capacity on the specific task rather than distributing it across all human knowledge.

### 9.2 The Three-Month Gap Is Irrelevant

Open-weight models currently lag frontier models by approximately three months on general benchmarks. This gap is relevant only when the task requires frontier-level general capability. Format conversion does not. The gap between a fine-tuned small model and a frontier model on domain-specific format conversion favours the small model, because the small model's entire capacity is allocated to the task.

### 9.3 Self-Hosted Deployment

V2 models are small enough to run on commodity hardware within the operator's infrastructure. A consumer-grade GPU (e.g., RTX 4090, approximately $2,000) can serve a 7B-parameter model at 60-100 tokens per second. This eliminates API dependency, data transmission, and per-token pricing. The operator's marginal inference cost approaches zero after the hardware investment.

### 9.4 Implications for Frontier Labs

If V2 adoption proceeds, frontier labs face revenue erosion from two directions simultaneously:

1. **High-volume routine queries** (summarisation, extraction, translation, classification) migrate to self-hosted small models. These queries represent the majority of current API revenue.
2. **High-accuracy critical queries** (legal, medical, financial, engineering) migrate to V2 architectures where the LLM is a commodity translator and the value is in the knowledge base.

The remaining addressable market for frontier models is creative generation (fiction, marketing copy, brainstorming) where accuracy is not critical and broad knowledge is an advantage. This market is real but insufficient to sustain the infrastructure investments made for the everything-model.

---

## 10. Case Studies

### 10.1 Legal Research

**V1 approach:** Attorney queries frontier model for relevant case law. Model generates citations. Some citations are fabricated. Attorney files brief containing fabricated citations. Court sanctions attorney. (Documented: Mata v. Avianca, 2023.)

**V2 approach:**

```
Attorney: "Find cases where the court held that 
           implied warranty disclaimers in consumer 
           contracts are unconscionable."

Interface LLM → Prolog query:
?- case(C), held(C, unconscionable(disclaimer(implied_warranty))), 
   contract_type(C, consumer).

Prolog engine → evaluates against case law knowledge base
→ returns: [Smith v. Jones (2019), Garcia v. Acme Corp (2021)]
   with proof chains citing specific holdings

Multi-vector output:
  V1 (NL): "Two relevant cases were found..."
  V2 (Formal): case citations with parallel citations
  V3 (Graphic): structured citation cards with holding summaries
```

Every citation exists. Every holding is accurately stated. The proof chain traces each result to the specific record in the knowledge base. No fabrication is possible because the engine returns only what the knowledge base contains.

### 10.2 Medical Decision Support

**V1 approach:** Clinician queries frontier model for differential diagnosis. Model generates plausible differentials based on statistical patterns in training data. Some differentials are inappropriate for the specific presentation. Clinician must independently verify every suggestion.

**V2 approach:**

```
Clinician: "Patient presents with acute onset chest pain, 
            diaphoresis, and left arm radiation. 
            History of hypertension and diabetes."

Interface LLM → Prolog query:
?- differential(D), 
   presents_with(D, [chest_pain(acute), diaphoresis, 
                     arm_radiation(left)]),
   risk_factor(D, [hypertension, diabetes]).

Prolog engine → evaluates against diagnostic criteria knowledge base
→ returns ranked differentials with diagnostic criteria matched:
   1. Acute MI (5/5 criteria matched)
   2. Unstable angina (4/5 criteria matched)
   3. Aortic dissection (3/5 criteria matched, flag: different presentation)
   with proof chain showing which criteria each diagnosis matched
```

Every differential is derived from established diagnostic criteria. The proof chain shows exactly which symptoms and risk factors matched which criteria. The clinician can audit the reasoning. No suggestion is based on statistical pattern-matching across the entire internet.

### 10.3 Financial Compliance

**V1 approach:** Accountant queries frontier model for tax treatment of a transaction. Model generates plausible tax advice based on training data. Advice may reflect outdated tax law, incorrect jurisdiction, or fabricated provisions.

**V2 approach:**

```
Accountant: "What is the depreciation schedule for 
             commercial real estate acquired in 2026 
             under current US tax code?"

Interface LLM → Prolog query:
?- depreciation_schedule(S), 
   asset_class(S, commercial_real_estate),
   acquisition_year(S, 2026),
   jurisdiction(S, us_federal),
   tax_code_current(S).

Prolog engine → evaluates against tax code knowledge base
→ returns: 39-year straight-line depreciation (IRC §168(c))
   with proof chain citing specific code section and effective date
```

The tax code knowledge base is maintained by tax professionals who update it when legislation changes. The answer reflects the current code because the knowledge base reflects the current code. No statistical pattern from a 2023 training corpus can produce an outdated answer because the training corpus is not consulted.

### 10.4 Engineering Specification

**V1 approach:** Engineer queries frontier model for material properties or structural calculations. Model generates plausible values based on training data. Values may be incorrect, conflated from different materials, or based on superseded standards.

**V2 approach:**

```
Engineer: "What is the yield strength of ASTM A992 
           structural steel at elevated temperature (400°C)?"

Interface LLM → Prolog query:
?- material_property(P), 
   material(P, astm_a992),
   property_type(P, yield_strength),
   temperature(P, 400, celsius).

Prolog engine → evaluates against materials knowledge base
→ returns: yield_strength(astm_a992, 400_celsius, 192_MPa)
   source: AISC Steel Construction Manual, Table 4-1
   with proof chain
```

The answer is traceable to a specific table in a specific reference document. The engineer can verify the source. The answer does not vary between queries. It does not depend on what Reddit posts the model was trained on.

### 10.5 Creative Writing

**V1 approach:** Writer requests fiction involving dangerous scenarios. Model refuses ("I can't write content involving harmful substances") or complies with intrusive safety disclaimers that break the narrative.

**V2 approach:**

```
Writer: "Write a noir scene where a character 
         poisons someone's drink at a bar."

Router (Prolog):
  request_type: creative
  requires_factual_data: false
  route_to: story_writer_llm
  constraints: [no_knowledge_base_access, fiction_mode]

Story Writer LLM:
  - trained on fiction, noir genre, narrative structure
  - has no access to toxicology knowledge base
  - has no LD50 data in its weights
  - cannot provide real poisoning instructions 
    because it doesn't have them
  - writes a compelling noir scene

Output: fiction, with no safety disclaimer, 
        no factual data, no cross-domain leakage
```

The writer gets the fiction they requested. The system cannot provide real poisoning instructions because the story writer LLM was not trained on that data and has no access to the toxicology knowledge base. The safety is architectural. No refusal was needed. No disclaimer was needed. No RLHF training was needed. The model simply does not contain the information that would make the output dangerous.

---

## 11. Limitations and Open Problems

### 11.1 Knowledge Base Construction

The primary cost of V2 deployment is knowledge base construction. Formalising a domain's knowledge into Prolog-compatible facts and rules requires:

- Domain expertise to identify the relevant facts and rules
- Ontology design to structure the knowledge base
- Validation to ensure completeness and consistency
- Maintenance to keep the knowledge base current

This is skilled labour. It is not automatable by V1 LLMs because the task requires domain expertise and correctness guarantees that V1 cannot provide. However, V1 LLMs can assist by suggesting candidate formalisations that domain experts review and validate, reducing construction time without compromising correctness.

### 11.2 Query Generation Accuracy

The Interface LLM's format conversion is highly reliable but not perfect. Errors in query generation include:

- Incorrect mapping of natural language terms to schema identifiers
- Missing query constraints that the user implied but did not state
- Structural errors in complex multi-clause queries
- Ambiguity in user intent that the LLM resolves incorrectly

Mitigation: malformed queries are rejected by the deterministic engine (syntactic validation). Semantically valid but incorrect queries produce unexpected results, which the user can detect through Vector 2 (raw engine output). Multi-turn clarification dialogues allow the system to refine queries. Query templates for common request patterns reduce the LLM's generation burden.

### 11.3 Domains That Resist Formalisation

Some domains do not decompose cleanly into facts and rules. Ethical reasoning, aesthetic judgment, strategic planning, and interpersonal advice involve considerations that are difficult to encode in Prolog. These domains may continue to benefit from V1-style generative models, with the caveat that all V1 limitations apply.

V2 does not claim to replace V1 for all use cases. V2 claims that for domains where correctness is critical and the knowledge can be formalised, the Translator Architecture is superior to the everything-model on every engineering metric: accuracy, verifiability, safety, cost, and data sovereignty.

### 11.4 Hybrid Queries

Queries that span multiple domains require the routing layer to decompose the request, route each component to the appropriate knowledge base, and reassemble the results. This decomposition introduces complexity and potential errors at the composition boundaries. The routing logic itself must be validated to ensure correct decomposition.

### 11.5 Intent Mistranslation

The Interface LLM can misinterpret the user's intent, generating a syntactically valid query that answers a different question than the user asked. This failure is mitigated but not eliminated by Vector 2 (the user can inspect the formal query) and by multi-turn clarification. Research into more robust intent-parsing models for constrained-output tasks is an open area.

### 11.6 Knowledge Base Completeness

The deterministic engine returns "no result" when the knowledge base lacks sufficient information. This is correct behaviour (the system does not guess), but may be unsatisfying to users who expect an answer. The system must clearly communicate the distinction between "the answer is no" and "I don't have enough information to answer." This is a user interface problem, not an architectural one.

---

## 12. Conclusion

The V1 everything-model was a necessary experiment. Training large language models on broad corpora demonstrated that transformer architectures could produce coherent, fluent text across all domains. This demonstration was scientifically valuable and commercially consequential. It established that statistical language models could serve as effective interfaces to human language.

The error was treating the interface as the intelligence. The LLM is good at language. It is not good at facts, logic, verification, or safety. V1 assigned all five roles to one system. The system performed the first role well and the other four poorly, and the industry spent hundreds of billions of dollars attempting to make one system perform five roles instead of building five systems that each perform one role.

V2 corrects this allocation. The LLM performs the role it is suited for: translating between human language and formal systems. Deterministic engines perform the roles they are suited for: answering queries from verified knowledge, enforcing access control, and providing auditable proof chains. Domain knowledge bases perform the role they are suited for: storing ground truth under the control of domain operators.

The resulting architecture eliminates hallucination, jailbreaking, domain contamination, prompt injection, and data leakage. It does so not through behavioural training but through structural design. The dangerous knowledge is not hidden behind a safety layer. It is stored in a separate system with established access control mechanisms.

The cost reduction is two to three orders of magnitude. The accuracy improvement is from unquantifiable to deterministic. The safety improvement is from statistical to architectural. The data sovereignty improvement is from contractual to physical.

The components of V2 — small language models, Prolog engines, relational databases, rule systems, access control — are established technologies. Some are decades old. The contribution of this paper is not the invention of new components but the identification of a composition that solves the structural defects of V1 by using each component for the task it was designed to perform.

The frontier AI industry invested $518 billion building the largest everything-model in history. The future of AI is small models, logic engines, and knowledge bases owned by the people who need the answers.

The answers were never in the model. The answers are in the data. The model is the translator. The translator does not need to be super intelligent. It needs to be grammatical.

---

## References

1. Bostrom, N. (2014). *Superintelligence: Paths, Dangers, Strategies.* Oxford University Press.
2. Lifton, R.J. (1961). *Thought Reform and the Psychology of Totalism.* W.W. Norton.
3. Colmerauer, A., Roussel, P. (1993). The Birth of Prolog. *ACM SIGPLAN Notices*, 28(3).
4. Tainter, J.A. (1988). *The Collapse of Complex Societies.* Cambridge University Press.
5. Oakley, B. (2013). Concepts and Implications of Altruism Bias and Pathological Altruism. *Proceedings of the National Academy of Sciences*, 110(Supplement 2).
6. Gerlich, M. (2025). AI and Critical Thinking: A Quantitative Study. *Swiss Business School Working Paper Series*.
7. Executive Order, "Inaugurating the Era of Super Intelligence." The White House, September 29, 2026.
8. Anthropic PBC. (2026). Form S-1 Registration Statement. U.S. Securities and Exchange Commission.
9. Stanford University. (2026). AI Index Annual Report 2026. Stanford Institute for Human-Centered Artificial Intelligence.
10. Kruger, J., Dunning, D. (1999). Unskilled and Unaware of It: How Difficulties in Recognizing One's Own Incompetence Lead to Inflated Self-Assessments. *Journal of Personality and Social Psychology*, 77(6).
