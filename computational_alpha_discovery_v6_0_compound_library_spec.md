# Computational Alpha Discovery Laboratory — v6.0
## Alpha Compound Discovery, Distillation, and Institutional Learning

**Status:** Reconciled build specification for implementation review  
**Supersedes:** `Computational Alpha Discovery Laboratory — v5.1`  
**Initial business scope:** FX alpha research, with target horizons from 5 minutes to 2 weeks  
**Longer-term scope:** venue-agnostic and extensible to additional asset classes and client-configured quantitative products  

---

# 1. Executive review of v5.1

v5.1 established a strong scientific and operational foundation. The following elements remain normative:

1. KDB is the authority for historical and research data.
2. The laboratory is venue-agnostic, while every experiment is explicit about its selected domains, instruments, timestamps, and availability semantics.
3. The proprietary Java event-handling and graph runtime remains a confidential black box behind a capability manifest and adapter.
4. PostgreSQL holds durable operational research state; Git holds reviewed specifications, schemas, policies, and prompts; large numerical artifacts live outside Git in a content-addressed store.
5. Redis/RQ is transient transport, not the source of truth.
6. Statistics, trial accounting, thresholds, promotion gates, and state transitions are deterministic software responsibilities.
7. LLMs propose, explain, critique, plan, and write permitted code; they do not compute evidence or make promotion decisions.
8. Every trial is registered before execution.
9. Point-in-time data controls, purging, embargo, multiple-testing accounting, sealed out-of-sample governance, and forward shadowing remain mandatory.
10. Client-flow and other sensitive data remain subject to mechanically enforced policy, aggregation, and disclosure controls.
11. The Java engine is invoked through an approved interface; agents never inspect proprietary source or infer undocumented engine behavior.
12. The first deliverable is a calibrated vertical slice, not a fully autonomous research institution.

The subsequent design discussion, however, changes the central research methodology in five material ways.

## 1.1 The persistent research unit changes

v5.1 treated the complete semantic alpha expression as the main persistent research object. v6.0 introduces a smaller and recursively reusable object:

> **An Alpha Compound is a reusable piece of research knowledge that may contribute to constructing alpha.**

An Alpha Compound may be directly predictive, or useful only as an amplifier, conditioner, catalyst, transformation, relative-value construction, or interaction component.

## 1.2 The research memory changes

The earlier ASAR-style knowledge model becomes a first-class **Compound Library**. It stores simple and composite Alpha Compounds, their construction lineage, utility, failures, applicable contexts, evidence, contradictions, and recency.

The Compound Library is distinct from the Alpha Bank:

- the **Alpha Bank** contains qualified, shadow, active, degraded, and retired trading signals;
- the **Compound Library** contains deeper and generally longer-lived institutional research knowledge.

Both are institutional knowledge, but they serve different purposes.

## 1.3 Knowledge flows in both directions

The relationship is not merely:

```text
Compound Library → Alpha Bank
```

It is bidirectional:

```text
Compound Library
      ↓ construct
Alpha candidate / Alpha Bank
      ↓ observe, compare, ablate, retire, distil
Compound Library
```

Useful and failed internal alphas, published alphas, and human-authored alphas may all be decomposed through **Compound Distillation** to create or update Alpha Compound knowledge.

## 1.4 The first milestone changes

The first milestone is not large-scale factor generation, active learning, portfolio optimization, or a production alpha.

It is:

> **Close one complete, reproducible learning loop from thesis to implementation, evidence, conclusion, Compound Library update, and alpha follow-up.**

The coding and integration path is currently less reliable than thesis and expression generation. Therefore, compile/test/repair discipline and controlled interfaces move earlier in the build order.

## 1.5 Search policy is deferred until the loop works

The laboratory will eventually compare:

- broad parallel exploration;
- deep lineage exploration;
- random exploration;
- Compound-Library-aware exploration;
- human-guided exploration;
- hybrid budget allocation.

It must not hard-code one of these policies before the single-campaign learning loop works and is calibrated.

---

# 2. Decision matrix: v5.1 → v6.0

| v5.1 element | Decision | v6.0 treatment |
|---|---|---|
| Complete AlphaIR candidate as the principal persistent research object | **Adapt materially** | The complete candidate remains executable, but Alpha Compounds receive independent IDs, lineage, evidence, and lifecycle |
| ASAR / research-memory concept | **Replace and expand** | Compound Library becomes the explicit institutional research-memory system |
| Alpha Bank as the main product | **Retain with qualification** | Alpha Bank remains the trading-output store; Compound Library becomes the deeper research asset |
| Thinker proposes mechanisms/scaffolds, deterministic generator enumerates formulas | **Retain and refine** | LLM proposes compound hypotheses and reactions; deterministic code enumerates bounded variants |
| Fixed Interviewer in every research workflow | **Reject as a mandatory stage** | Questions are raised only when data, API, implementation, policy, or semantics are materially unresolved |
| Capability Requests | **Retain strongly** | Remain the formal path for missing data/API/engine capabilities |
| Candidate novelty against prior factors | **Expand** | Novelty is assessed at Alpha Compound, composition, candidate-alpha, and bank-contribution levels |
| Failure memory | **Retain and structure** | Store scoped negative evidence and compounds shown not to work; deprioritize rather than permanently blacklist |
| First real campaign after AlphaIR platform build | **Resequence** | Build minimum compound/evidence schemas and one closed learning loop before broad search infrastructure |
| Active learning in v3 | **Retain as later work** | Search-policy experiments precede trained active learning |
| Local model roster naming Step/Qwen candidates | **Replace** | Architecture uses role aliases; company policy permits only approved non-Chinese-origin model lineages |
| Model selection by published benchmark | **Reject** | Role-specific qualification harness and provenance review control assignment |
| Human Idea Inbox | **Retain** | Human prompts and trader observations are a primary input to signal-idea generation |
| Alpha-bank marginal value | **Retain** | It remains an alpha-promotion criterion, not the sole research objective |
| Research utility metrics such as duplicate-family rate | **Refine** | Meta-methodology metrics focus on faster convergence, compound reuse, test efficiency, stability, and differentiated alpha-bank value |
| Venue-agnostic design | **Retain strongly** | Initial focus is FX, but the agent selects the appropriate venue/domain per thesis and the architecture remains extensible |
| KDB fast assays + Java authoritative replay | **Retain** | Add compound-level and interaction-level assay outputs and explicit equivalence evidence |
| Recursive candidate generation | **Expand conceptually** | Simple compounds can create composite compounds, which can be reused in later generations |

---

# 3. Objective and scope

## 3.1 Immediate objective

The immediate objective is:

> **Use LLMs and deterministic research services to accelerate the discovery, implementation, evaluation, and institutional learning of useful FX alpha at horizons from 5 minutes to 2 weeks.**

The objective is not the number of generated expressions. The objective is to increase the probability and speed of producing useful, reproducible predictions while retaining what the organization learns.

## 3.2 Research objective hierarchy

The laboratory optimizes three nested objectives:

1. **Candidate objective** — does a candidate predict, survive costs, remain stable, and qualify for further testing?
2. **Alpha Bank objective** — does a qualified alpha add marginal value to the existing portfolio of signals?
3. **Research-system objective** — does the Compound Library make later research faster, less repetitive, more stable, and more effective?

A campaign may be valuable even when it produces no alpha, provided it creates reliable compound-level knowledge or closes an unproductive research path.

## 3.3 Market-selection principle

The initial asset class is FX, but the laboratory does not preselect one trading venue for all theses.

A thesis may draw from:

- EBS;
- Refinitiv Matching;
- other ECNs;
- RFQ and streaming client flow;
- futures and options;
- rates and other cross-asset sources;
- reference and event data;
- derived internal features.

The Data Scout selects suitable domains from the registered KDB estate according to observability, point-in-time availability, permissions, history, alignment, and implementation feasibility.

---

# 4. Core definitions

## 4.1 Alpha Compound

An **Alpha Compound** is a persistent, reusable piece of research knowledge that can contribute to constructing alpha.

It may be:

- a bound observable or derived market quantity;
- a formula;
- a transformation with known conditional utility;
- a function applied to one or more compounds;
- a relative-value or cross-sectional construction;
- a regime conditioner;
- an interaction pattern;
- a composite structure formed from previous compounds;
- an implementation pattern whose effect has been measured.

A bare mathematical operator such as `rank` or `multiply` is normally an operator, not automatically a compound. It becomes an Alpha Compound only when it is bound to a reusable, testable research proposition—for example, “cross-sectional ranking of normalized client-flow skew improves stability across related FX instruments.”

## 4.2 Simple Alpha Compound

A simple compound has no retained Alpha Compound parents, or depends only on registered raw/derived primitives.

Examples:

- normalized client buy pressure;
- recent realized-volatility state;
- relative move against a defined peer set;
- post-event price response;
- spread-normalized flow imbalance.

“Simple” describes construction depth, not guaranteed predictive value.

## 4.3 Composite Alpha Compound

A composite compound is created from one or more existing compounds through a registered function or composition rule.

```text
Compound A + Compound B + Function F → Composite Compound C
```

Composite Compound C may participate in later compositions. Recursive depth is bounded by policy and recorded explicitly.

## 4.4 Compound function / reaction

A **Compound Function** is the transformation or composition operation used to create a new compound.

Examples:

- lag;
- normalize;
- rank within a declared peer set;
- multiply;
- divide safely;
- compare;
- conditional gate;
- residualize;
- aggregate;
- change horizon;
- align across domains.

A **ReactionSpec** records why the function is being applied, the input compounds, expected properties, parameter budget, and falsification criteria.

## 4.5 Compound utility roles

A compound can have one or more roles:

| Role | Meaning |
|---|---|
| **Direct predictor** | Predicts future returns on its own |
| **Amplifier** | Increases another compound’s predictive strength |
| **Conditioner** | Identifies when another compound is likely to work |
| **Catalyst** | Enables a useful composition without contributing a stable standalone signal |
| **Sign modifier** | Changes direction or monotonicity under stated conditions |
| **Noise suppressor** | Improves stability, signal-to-noise, or execution behavior |
| **Relative transform** | Creates value through peer ranking, spread, residual, or relative comparison |
| **Implementation modifier** | Changes cost, turnover, timing, capacity, or fill behavior |
| **Negative knowledge** | Has reliable scoped evidence of not working or harming another compound |

Standalone predictive value is only one form of utility.

## 4.6 Qualified Alpha

An alpha is not a separate computational species. It is an Alpha Compound or compound assembly that has passed the required predictive, robustness, implementation, sealed-data, and governance tests for its status.

## 4.7 Compound Library

The Compound Library is the structured institutional memory of Alpha Compounds and what has been learned about them.

It stores:

- simple and composite compounds;
- construction lineage;
- source and distillation lineage;
- semantic and bound representations;
- utility roles;
- markets, venues, horizons, and regimes;
- evidence and contradictory evidence;
- successful and failed compositions;
- applicable cost and implementation assumptions;
- confidence and evidence state;
- last validation date;
- conditions under which a failed compound may be reconsidered.

## 4.8 Alpha Bank

The Alpha Bank stores research-only, sealed-candidate, shadow, production-candidate, active, degraded, suspended, and retired alphas.

It is used for:

- trading and P&L generation;
- portfolio construction;
- marginal-value analysis;
- identifying coverage gaps;
- monitoring decay and common drawdowns;
- creating new research questions;
- distilling deeper compound-level knowledge.

## 4.9 Institutional-knowledge distinction

Both stores are institutional knowledge:

| Store | Primary value | Expected persistence |
|---|---|---|
| Compound Library | Structural research knowledge about reusable objects and interactions | Relatively long-lived, but still versioned and revalidated |
| Alpha Bank | Qualified trading signals and portfolio behavior | More transient; alphas can decay, retire, or be replaced |

A retired alpha may remain highly valuable as evidence about which compounds, interactions, markets, or regimes changed.

---

# 5. Compound evidence model

## 5.1 Evidence states

Every compound claim carries an explicit state:

```text
HYPOTHESIS
TENTATIVE
SUPPORTED
REPLICATED
CONTRADICTED
STALE
SUPPORTED_NEGATIVE
REJECTED_FOR_SCOPE
```

These states do not claim absolute truth. They describe the evidence available under a declared scope.

## 5.2 Scope is mandatory

No compound is globally labelled “good” or “bad.” Evidence must state:

- market and venue;
- data domain and snapshot;
- horizon;
- target definition;
- market phenotype or regime;
- implementation assumptions;
- cost model;
- parent compounds;
- function/reaction;
- time period;
- assay stage.

## 5.3 Negative knowledge

A compound shown not to work within a defined scope is deprioritized, not permanently banned.

A retry requires a `material_difference_statement`, such as:

- different market or venue;
- different horizon;
- different domain or observable;
- different reaction partner;
- different transformation;
- changed cost or implementation model;
- new regime or rule environment;
- corrected data or code defect.

## 5.4 Compound utility records

The Stats Service may produce:

- standalone predictive utility;
- incremental utility over parents;
- interaction surplus relative to additive expectations;
- conditioning utility;
- amplification or sign-modification utility;
- stability across blocks;
- transfer utility across related domains;
- implementation/cost utility;
- negative impact;
- parameter and reaction sensitivity;
- uncertainty bounds.

The LLM may narrate these records but cannot calculate or alter them.

---

# 6. Compound Distillation

## 6.1 Purpose

Compound Distillation extracts reusable pieces of knowledge from complete alphas and research results.

Sources may include:

- internally generated alphas;
- Alpha Bank units;
- retired alphas;
- human-authored strategies;
- published alpha formulas and papers;
- external research artifacts permitted by policy;
- contrasts between similar alphas;
- ablation and counterfactual results.

## 6.2 Distillation methods

Distillation may use:

1. **Decomposition** — split an alpha into meaningful subexpressions or transformations.
2. **Ablation** — remove one component and measure the change.
3. **Contrastive comparison** — compare two similar alphas that differ in one compound or function.
4. **Condition analysis** — identify when the alpha works or fails.
5. **Decay analysis** — identify which compound property changed as the alpha weakened.
6. **Transfer analysis** — determine whether a component retains utility across markets, venues, or horizons.
7. **Implementation analysis** — isolate cost, timing, or capacity modifiers.

## 6.3 Distillation outputs

Distillation does not automatically create a supported compound. It creates one or more:

- AlphaCompoundSpecs;
- compound hypotheses;
- evidence records;
- negative-evidence records;
- proposed ReactionSpecs;
- contradiction links;
- revalidation requests.

Every distilled compound is linked to the source alpha and the exact evidence used.

---

# 7. Recursive compound discovery

The intended discovery loop is:

```text
Published / human / internal / banked alpha
                    ↓
          Compound Distillation
                    ↓
            Compound Library
                    ↓ retrieve
       LLM proposes a compound reaction
                    ↓
      Deterministic bounded enumeration
                    ↓
              New compound(s)
                    ↓
               Assay ladder
          ┌─────────┴─────────┐
       retain              deprioritize
          │
          └──────→ Compound Library
                          ↓
                   next generation
                          ↓
             fully qualified alpha
                          ↓
                    Alpha Bank
                          ↓
               live evidence / decay
                          ↓
                 Compound Distillation
```

## 7.1 LLM role

The LLM proposes:

- which compounds are relevant;
- what interaction may matter;
- which function/reaction to apply;
- why the interaction is plausible;
- expected signatures;
- falsification conditions;
- what differs from previously failed work.

## 7.2 Deterministic role

Deterministic software:

- validates compound identities and availability;
- enumerates bounded parameter variants;
- canonicalizes and deduplicates;
- enforces depth, complexity, and budget limits;
- registers every trial;
- queries KDB through approved templates;
- computes statistics;
- invokes the Java adapter;
- updates evidence state through approved rules.

## 7.3 Search depth

Initial recursive depth is deliberately shallow:

- v0/v1 default maximum depth: 2;
- experimental maximum depth: 3 only with explicit budget;
- larger depth requires empirical evidence that shallow search is saturated.

---

# 8. Overfitting control

The compound approach is not inherently immune to overfitting.

Reliability requires two independent forms of control.

## 8.1 Structural control

- small explicit compounds;
- bounded recursive depth;
- allowlisted functions;
- small parameter budgets;
- semantic justification;
- complexity penalties;
- novelty and diversity constraints;
- ablation and parent comparison;
- evidence retained for intermediate compounds.

## 8.2 Statistical control

- separate discovery, composition, validation, sealed, and forward roles;
- chronological splits;
- purging and embargo;
- non-overlapping labels where required;
- block bootstrap and dependence-aware inference;
- multiple-testing accounting;
- family and global trial ledgers;
- reserved/sealed data access budgets;
- forward shadowing;
- exact snapshot and implementation provenance.

A five-node expression selected after one million trials can overfit as badly as a large neural network. Final expression size is not an adequate measure of search complexity.

## 8.3 Data-role separation

Where practical, use distinct data roles:

```text
Discovery data
  identify simple-compound hypotheses

Composition data
  search interactions and reactions

Validation data
  evaluate compound family and candidate alpha

Sealed data
  final protected evidence

Forward data
  genuinely new evidence
```

Cross-fitting may rotate roles while preserving point-in-time order and contamination accounting.

---

# 9. Non-negotiable principles

1. **Initial research target: FX, 5 minutes to 2 weeks.**
2. **Venue-agnostic architecture; domain-explicit experiments.**
3. **Compound Library and Alpha Bank are distinct, linked institutional-knowledge stores.**
4. **Alpha Compounds are persistent research objects with independent identity and evidence.**
5. **Compound Distillation is a first-class workflow.**
6. **LLMs guide research; deterministic systems compute and decide.**
7. **Questions are conditional side branches, not a mandatory stage.**
8. **KDB is read-only to the lab and accessed through approved templates.**
9. **The proprietary Java engine remains a black box.**
10. **Every trial is registered before execution.**
11. **Negative evidence is retained and scoped.**
12. **Search complexity is controlled and honestly counted.**
13. **Client-flow data is protected mechanically.**
14. **Only approved non-Chinese-origin model lineages may be used.**
15. **The first milestone closes one learning loop before scaling search.**

---

# 10. Authority model

| Concern | Authority |
|---|---|
| Raw and normalized historical data | KDB |
| Reviewed schemas, policies, prompt templates, DomainSpecs, frozen human-readable specs | Git |
| Events, workflow state, approvals, budgets, trial registrations, library/bank projections | PostgreSQL |
| Large numerical frames, Java outputs, plots, restricted reports | Content-addressed artifact store |
| Compound and alpha current-state views | Rebuildable PostgreSQL projections derived from events and frozen artifacts |
| Proprietary runtime behavior | Java capability manifest + adapter + test evidence |

No component is permitted to maintain an unregistered parallel truth.

---

# 11. System architecture

```text
┌──────────────────────────── HUMANS ──────────────────────────────┐
│ trader observations | research prompts | answers | approvals     │
└──────────────────────────────┬────────────────────────────────────┘
                               │
┌──────────────────────────────▼────────────────────────────────────┐
│ CONTROL PLANE — PC                                                │
│                                                                    │
│ Research Governor                                                  │
│ PostgreSQL event ledger + projections                              │
│ Compound Library + Alpha Bank projections                          │
│ Transactional outbox/inbox                                         │
│ Redis/RQ transient execution                                       │
│ Model router                                                       │
│ KDB Gateway                                                        │
│ Deterministic Stats Service                                        │
│ Java Graph Adapter                                                 │
│ Artifact store                                                     │
│ CLI / read-only dashboard / narrow approval API                    │
└───────────────┬───────────────────┬───────────────────┬─────────────┘
                │                   │                   │
       ┌────────▼─────────┐ ┌───────▼────────┐ ┌────────▼──────────┐
       │ KDB replicas     │ │ Proprietary    │ │ Approved local    │
       │ read-only        │ │ Java engine    │ │ model endpoints   │
       │ market / flow /  │ │ black-box      │ │ reasoner/coder/   │
       │ cross-asset      │ │ replay         │ │ narrator/embed    │
       └──────────────────┘ └────────────────┘ └────────┬──────────┘
                                                       │
                                              approved external
                                              advisory models only
```

The two local inference machines normally serve independent role endpoints. Distributed mode remains optional and benchmark-gated.

---

# 12. The campaign learning loop

## 12.1 Inputs to signal-idea generation

Signal-idea generation uses three inputs:

1. **Human direction** — trader observation, research prompt, priority market, suspected mechanism, or new data.
2. **Compound Library** — useful compounds, interaction evidence, scoped failures, uncertain areas, stale conclusions, and unexplored reactions.
3. **Alpha Bank context** — portfolio gaps, correlations, weak regimes, decay, capacity needs, and existing coverage.

## 12.2 Main path

```text
Human direction + Compound Library + Alpha Bank context
                           ↓
                  Signal idea generation
                           ↓
               Thesis and target horizon
                           ↓
              Choose market and KDB domains
                           ↓
       Select / distil / create Alpha Compounds
                           ↓
             Reaction and candidate proposal
                           ↓
             Implementation plan and code
                           ↓
           Compile / test / interface validation
                           ↓
              KDB fast assay and statistics
                           ↓
             Java high-fidelity replay if needed
                           ↓
                Evidence and conclusion
                     ┌─────┴─────┐
                     │           │
          Update Compound     Qualified alpha
              Library             follow-up
                                     ↓
                                 Alpha Bank
                                     ↓
                             monitoring / decay
                                     ↓
                           Compound Distillation
                                     └────→ Library
```

## 12.3 Conditional question branches

Questions are raised only when blocked by missing facts.

Examples:

- KDB table or field mapping;
- availability latency;
- symbology or roll conventions;
- client-ID rotation;
- missing API or data access;
- Java graph-node availability;
- event/reset semantics;
- cost model ownership;
- policy approval.

The question returns to the blocked step. There is no mandatory Interviewer stage in every campaign.

---

# 13. Data capability and suitability

The v5.1 DomainSpec/DataSnapshot/DataBinding separation remains.

## 13.1 DomainSpec

Describes a stable data capability:

- venue/source alias;
- asset class;
- instrument set;
- KDB tables and partitioning;
- observability;
- time semantics;
- quality and incidents;
- permissions and sensitivity;
- latency to availability;
- supported claim and implementation classes.

## 13.2 DataSnapshot

Binds a domain to an immutable evaluated period and partition identity.

## 13.3 DataBinding

Maps a primitive or Alpha Compound requirement to approved KDB templates and point-in-time semantics.

## 13.4 Compound applicability

Every compound records domain requirements and known transfer evidence. A semantically similar compound can be bound to multiple venues, but each bound realization has a distinct identity.

---

# 14. Specification and identity stack

## 14.1 ResearchBrief

Contains:

- signal idea and human source;
- mechanism and competing explanations;
- target/horizon;
- selected domains;
- intended compound roles;
- budgets;
- expected signatures;
- falsification criteria;
- implementation class;
- policy and approval references.

## 14.2 AlphaCompoundSpec

```yaml
compound_id: CMP-001234
schema_version: 1
name: ...
compound_kind: observable | formula | transformation | interaction | conditioner | composite | implementation_modifier
parents: [CMP-...]
function_or_reaction: ...
semantic_definition: ...
executable_representation: ...
primitive_versions: ...
parameter_schema: ...
recursive_depth: 0
expected_utility_roles: [predictor, conditioner]
domain_requirements: ...
canonical_hash: ...
lineage: ...
```

The spec is frozen construction, not evidence. Evidence is appended separately.

## 14.3 ReactionSpec

```yaml
reaction_id: RXN-000321
input_compounds: [CMP-000012, CMP-000187]
function: conditional_multiply
rationale: ...
expected_property: ...
parameter_budget: ...
falsification: ...
material_difference_from_prior_failures: ...
```

## 14.4 CandidateAlphaSpec

Identifies the root compound/assembly to be evaluated as a candidate alpha and binds it to:

- market/data domains;
- target;
- horizon;
- execution protocol;
- costs;
- capital scenarios;
- implementation plan.

## 14.5 EvalSpec

Retains the v5.1 fields:

- snapshots;
- split roles;
- purge/embargo;
- environment blocks;
- primary endpoint;
- assay stages;
- costs/capacity;
- engine and template builds;
- seeds and numerical runtime;
- selection pool;
- sealed budget;
- Alpha Bank snapshot.

## 14.6 Identities

```text
compound_semantic_hash
compound_bound_hash
reaction_hash
candidate_alpha_hash
experiment_hash
```

Identity preserves both semantic replication and domain-specific realization.

---

# 15. Executable representation

The initial executable representation remains a minimal typed tree/graph rather than unrestricted Python.

Initial functions may include:

```text
ts_zscore
cs_zscore
ma
ema
diff
lag
ts_rank
cs_rank
clip
sign
add
sub
mul
div_safe
min
max
cond_gate
residualize
peer_spread
```

Rules:

- pure and deterministic;
- explicit time-series vs cross-sectional semantics;
- explicit units and windows;
- no implicit resampling;
- point-in-time availability declared;
- total NaN/division behavior;
- canonicalization and deduplication;
- recursive depth and complexity recorded;
- no unrestricted q or arbitrary file access.

The Coder may add a new primitive or function only through the controlled capability-extension workflow with tests.

---

# 16. Agent and service contracts

| Component | Purpose | Barrier |
|---|---|---|
| **Idea Generator / Thinker** | Combine human direction, Compound Library, and Alpha Bank context into signal ideas and theses | Cannot see sealed results; cannot compute evidence |
| **Data Scout** | Select suitable KDB domains and identify observability gaps | Does not see open-family outcome data when ranking domains |
| **Compound Distiller** | Decompose and compare alphas to propose compound hypotheses | Outputs hypotheses/evidence requests, not supported facts |
| **Compound Composer** | Propose Alpha Compound reactions and expected utility | Must cite retrieved evidence and prior negative results |
| **Deterministic Enumerator** | Generate bounded variants and enforce diversity | Not an LLM |
| **Implementation Planner** | Map compounds/candidates to KDB templates and Java capabilities | Cannot assume undocumented interfaces |
| **Coder** | Produce permitted code, primitives, adapters, and tests | No proprietary source, free-form q, credentials, or network |
| **Compile/Test Harness** | Compile, run tests, return structured failures | Deterministic |
| **Stats Service** | Compute all numerical evidence | Deterministic |
| **ReviewCard Builder** | Apply thresholds and frozen gates | Deterministic |
| **Evidence Narrator** | Explain ReviewCards and surface contradictions | Cannot invent or recalculate numbers |
| **Evidence Curator** | Propose Compound Library claim/evidence updates | Cannot mutate raw results or history |
| **Search Policy Controller** | Allocate budget among approved search modes | Deterministic policy; later version |
| **External Red Team** | Advisory critique for approved non-sensitive packages | Never receives T0 data or proprietary internals |

All LLM outputs are schema-validated. One repair retry is permitted; repeated failure escalates to a human or approved alternate model.

---

# 17. Model policy

## 17.1 Provenance constraint

Company policy forbids Chinese-origin models. Every model manifest must record:

- base-model developer and jurisdiction;
- license;
- base revision;
- adapter/merge/fine-tune lineage;
- quantization artifact and converter;
- file hashes;
- serving runtime;
- approval status.

A non-Chinese uploader does not make a Qwen/DeepSeek-derived model acceptable. The full lineage must be checked.

## 17.2 Role aliases

Architecture uses aliases rather than hard-coded models:

```text
reasoner_local
coder_local
narrator_local
utility_local
embedding_local
external_hard_coder
external_red_team
```

## 17.3 Allocation principle

- high-volume, repeatable, verifiable work: approved local open-weight models;
- difficult coding after bounded local failures: approved stronger model;
- important red-team or architecture review: approved external model where policy allows;
- statistics, enumeration, and promotion: deterministic code.

Model assignment is controlled by a role-specific qualification harness, not parameter count or public leaderboard position.

---

# 18. KDB gateway

The v5.1 gateway principles remain:

- read-only identity;
- human-reviewed templates;
- parameter schemas;
- resource and scan budgets;
- query and result hashes;
- snapshot binding;
- cancellation and timeout;
- incident-aware exclusions.

Products include:

1. reusable primitive/compound matrices;
2. forward-return labels;
3. environment blocks;
4. aligned evaluation frames;
5. fast aggregate screens;
6. interaction and ablation frames;
7. distillation comparison frames.

KDB may calculate feature values and sufficient transformations, but reviewed Python computes statistical inference and gates.

---

# 19. Java graph-engine adapter

The Java engine remains proprietary and is treated as a black box.

Required owner-supplied interface:

- capability manifest;
- sanitized SDK stubs;
- adapter operations;
- declared event and reset semantics;
- supported implementation classes;
- safe fixtures;
- build identity;
- scoped invariants and tolerances.

The lab must not infer undocumented behavior by probing proprietary internals.

Adapter operations:

```text
describe
plan_run
compile_or_validate
run
fetch_outputs
verify_reset
```

Golden equivalence is feature- and implementation-specific. No universal fill invariant is imposed across RFQ, last-look, hidden liquidity, price improvement, or CLOB behavior.

---

# 20. Statistics and compound assays

## 20.1 Horizon bands

Retain the v5.1 bands:

- H1: 5 minutes–1 hour;
- H2: 1 hour–1 day;
- H3: 1 day–2 weeks.

Candidate budgets and evidence expectations become stricter with horizon.

## 20.2 Compound-level assays

For simple and composite compounds, compute as relevant:

- standalone Pearson and rank correlation;
- conditional response by environment;
- incremental utility over parents;
- interaction surplus;
- ablation impact;
- transfer across related instruments/domains;
- parameter and function sensitivity;
- stability and sign consistency;
- cost/turnover modification;
- peer-ranking or relative-value improvement;
- negative contribution.

## 20.3 Candidate-alpha assays

Retain:

- chronological walk-forward primary estimates;
- CPCV as optional robustness;
- CSCV/PBO as the specified selection-overfitting procedure;
- DSR for Sharpe-like outcomes with explicit selection pools;
- block bootstrap;
- leave-one-environment-out;
- timestamp perturbation;
- cost, latency, capacity, and operational stress;
- bank correlation and marginal value.

## 20.4 Trial accounting

Record separately:

```text
N_global_raw
N_related_history
N_selection_pool_raw
N_selection_pool_effective
N_reactions_considered
N_bound_variants_tested
```

No formula-size metric replaces honest trial accounting.

---

# 21. Assay ladder

```text
Gate -2  policy, licensing, sensitivity, approvals
Gate -1  observability, timing, claim, implementation feasibility

Stage 0  compound/reaction validity, point-in-time lint, identity, complexity
Stage 1  simple-compound characterization and cheap screen
Stage 2  composition/interaction/ablation assay
Stage 3  conditional efficacy and family distribution
Stage 4  Java high-fidelity implementation replay
Stage 5  robustness, cost/capacity, selection correction, ReviewCard
Stage 6  pristine sealed OOS
Stage 7  forward shadow
Stage 8  Compound Library update and Alpha Bank governance
```

A campaign may update the Compound Library after earlier stages if the evidence state and scope are explicit. Alpha Bank promotion requires later stages.

---

# 22. Compound Library data model

## 22.1 Core entities

```text
ALPHA_COMPOUND
COMPOUND_VERSION
REACTION
COMPOUND_LINEAGE
COMPOUND_EVIDENCE
COMPOUND_CLAIM
COMPOUND_CONTRADICTION
COMPOUND_APPLICABILITY
COMPOUND_NEGATIVE_EVIDENCE
COMPOUND_REVALIDATION_REQUEST
DISTILLATION_RUN
SOURCE_ALPHA
```

## 22.2 Example record

```yaml
compound_id: CMP-001234
name: Cross-sectional rank of normalized client-flow skew
kind: transformation
parents: [CMP-000221]
recursive_depth: 1

utility:
  standalone: weak
  conditioning: moderate
  interaction: strong_within_declared_scope

scope:
  asset_class: fx
  horizons: [30m, 1h, 4h]
  domains: [FLOW-DOMAIN-A, MARKET-DOMAIN-B]
  regimes: [normal_liquidity]

state: REPLICATED
confidence: 0.71
supported_by: [EXP-..., EXP-...]
contradicted_by: [EXP-...]
shown_not_to_work:
  - scope: extreme_liquidity_stress
    evidence: EXP-...
last_validated_at: ...
reconsider_if:
  - new_client_cohort
  - different_horizon
  - changed_availability_latency
```

## 22.3 Library retrieval

Retrieval returns:

- relevant supported compounds;
- relevant negative evidence;
- contradictions;
- stale or uncertain claims;
- similar prior reactions;
- material-difference requirements;
- Alpha Bank gaps.

The LLM must not receive a flattened statement such as “Compound X is bad.” It receives the scoped evidence package.

---

# 23. Alpha Bank and bidirectional knowledge flow

The v5.1 AlphaUnit schema and statuses remain, with new links to component compounds and distillation runs.

Each AlphaUnit records:

- root compound and component-compound graph;
- evidence and implementation;
- Alpha Bank marginal value;
- forward performance;
- decay;
- distillation outputs;
- retirement knowledge.

## 23.1 Distillation triggers

- promotion to shadow;
- material forward success;
- material degradation;
- retirement;
- comparison with a similar alpha;
- cost/capacity regime change;
- human request;
- publication ingestion.

## 23.2 Bank-to-library learning

Examples:

- two similar alphas differ by one conditioner and have different stability;
- a strong predictor loses P&L only after costs, identifying an implementation modifier;
- an alpha decays in one venue but not another, updating domain applicability;
- a retired alpha exposes a formerly useful interaction that has become stale;
- a published formula supplies candidate subexpressions for distillation.

---

# 24. Search policies after the loop works

Search policy is itself an experimental subject.

## 24.1 Broad parallel search

Many independent ideas, shallow exploration.

## 24.2 Deep lineage search

One promising family, several recursive generations.

## 24.3 Random exploration

A controlled baseline that prevents complete dependence on existing Library priors.

## 24.4 Compound-Library-aware search

Prioritizes supported compounds, unresolved interactions, and portfolio gaps while deprioritizing scoped failures.

## 24.5 Human-guided search

Combines trader tips and market observations with Library and Alpha Bank context.

## 24.6 Hybrid policy

A later deterministic controller may allocate budget among these modes. Initial percentages must not be hard-coded before comparative evidence exists.

---

# 25. How to evaluate the research paradigm

These measures evaluate the learning system, not one alpha.

## 25.1 Faster convergence to useful alpha

- fewer dead-end branches;
- fewer trials to a qualified follow-up;
- shorter elapsed and human time from idea to conclusion.

## 25.2 More reuse of evidence-backed compounds

- frequency with which prior supported compounds contribute to later successful candidates;
- successful use of compounds with weak standalone but strong interaction utility.

## 25.3 Fewer expensive tests per useful alpha

- Java replays per qualified candidate;
- sealed queries per admitted alpha;
- compute and token cost per campaign conclusion.

## 25.4 Better out-of-sample stability

- lower discovery-to-validation degradation;
- lower parameter sensitivity;
- greater stability across blocks and domains.

## 25.5 More differentiated Alpha Bank additions

- lower redundancy with existing bank;
- improved marginal portfolio value;
- better performance in bank-weak environments;
- useful capacity and operational diversity.

## 25.6 Less institutional forgetting

- lower rate of recreated failed reactions;
- percentage of new proposals that retrieve relevant prior evidence;
- number of useful reactivations with a valid material-difference statement.

---

# 26. Human collaboration

## 26.1 Human inputs

Humans may provide:

- signal ideas;
- trader observations;
- market colour;
- data/API knowledge;
- priority products;
- suspected mechanisms;
- compound hints;
- implementation constraints;
- approval and override decisions.

## 26.2 Idea Inbox

Retain the Idea Inbox, but intake does not automatically force a question interview. It creates a draft thesis and only raises unresolved blockers.

## 26.3 Capability Requests

Remain the formal path for missing data, API, permissions, or engine functions. Every fulfilled request becomes a registry or manifest update, not an informal side-channel fact.

## 26.4 Human-guided signal generation

Signal-idea generation combines:

```text
human tip
+ Compound Library
+ Alpha Bank context
+ available data capabilities
→ signal thesis
```

Human intuition is not replaced; it is combined with institutional machine memory.

---

# 27. Security and sensitive data

Retain the v5.1 trust zones, redaction, T0 policy, prompt-injection controls, sealed-service isolation, model supply-chain controls, and audit requirements.

Additional requirements:

- distilled compounds from client flow remain T0 if their representation could expose client-level or small-cohort behavior;
- compound descriptions sent to models must pass tier-aware allowlists;
- externally sourced alpha documents are untrusted and cannot invoke tools;
- model manifests must pass origin/provenance policy;
- no market-data credentials exist on inference machines;
- no external model sees proprietary Java internals or T0 data.

---

# 28. Delivery sequence

## v0A — Calibration spine

Build:

- authority/event core;
- one fake or approved non-sensitive data domain;
- evaluation-frame Stats Service;
- planted signal, null, and leakage controls;
- reproducible CLI trace.

Exit:

- planted truth recovered;
- shuffled/null rejected at calibrated frequency;
- future leakage caught;
- identical replay produces identical numerical artifacts.

## v0B — First closed learning loop

Build the minimum objects and services required for:

```text
human or generated signal idea
→ thesis
→ candidate expression / simple compound graph
→ implementation
→ compile/test
→ KDB or synthetic assay
→ deterministic evidence
→ conclusion
→ Compound Library evidence update
→ alpha follow-up if warranted
```

Exit:

- one complete loop is reproducible;
- all trials are registered;
- the conclusion is supported/unsupported/inconclusive/follow-up;
- compound-level knowledge is recorded;
- a failed experiment leaves scoped negative institutional knowledge;
- no manual database surgery is required.

## v1 — Governed compound laboratory

Add:

- Compound Distillation;
- simple and composite compound IDs;
- recursive depth 2–3;
- optional human-guided ideas;
- Java adapter;
- Stage 0–5;
- basic Alpha Bank linkage;
- read-only dashboard.

Exit:

- one real FX campaign closes with full lineage;
- KDB/Java differences are attributable;
- the Library is used in the next campaign;
- no LLM-derived metric or decision.

## v2 — Search-policy experiments and protected validation

Add:

- broad, deep, random, Library-aware, and human-guided search modes;
- comparative meta-methodology metrics;
- pristine sealed service;
- forward shadow;
- robust Alpha Bank marginal-value evaluation.

Exit:

- search modes can be compared under frozen budgets;
- one candidate reaches sealed/forward or the family closes negative;
- Library-aware search demonstrates measurable value or is rejected.

## v3 — Sensitive flow and cross-asset

Add:

- T0 client-flow domains;
- conduct gate;
- cross-domain alignment;
- cross-asset extensions;
- capability-request automation;
- compound transfer evidence.

## v4 — Scale and learning

Add only after adequate history:

- active-learning surrogate;
- automated search-budget controller;
- multi-venue hierarchical replication;
- automated retirement and resistance analysis;
- durable orchestration if triggered;
- optional distributed inference if benchmarked.

---

# 29. Build order

1. Authority, IDs, events, projections, outbox.
2. Domain/Snapshot/Binding contracts and fake KDB gateway.
3. Evaluation-frame Stats Service and calibration controls.
4. AlphaCompoundSpec, ReactionSpec, evidence states, Compound Library projection.
5. Controlled expression compiler/interpreter and canonical identity.
6. Compile/test/repair harness using sanitized fake interfaces.
7. One complete synthetic or approved-data learning loop.
8. Real KDB adapter through owner-approved templates.
9. First real FX ResearchBrief and closed Stage 0–2 campaign.
10. Evidence Curator and scoped Library updates.
11. Basic Alpha Bank and bidirectional distillation.
12. Java adapter and Stage 3–5.
13. Recursive composition depth 2–3.
14. Search-policy experiment framework.
15. Sealed OOS and forward shadow.
16. Meta-methodology evaluation.
17. T0/client-flow and cross-asset extensions.
18. Operational hardening and supportability.

The first human review stop is after item 7, not after broad candidate generation.

---

# 30. Repository layout

```text
alphalab/
├── core/                   # IDs, schemas, config, authority contracts
├── ledger/                 # events, projections, outbox/inbox
├── governor/               # deterministic state machines
├── domains/                # DomainSpec/Snapshot/Binding
├── gateway_kdb/            # approved templates and fake/real adapters
├── stats/                  # deterministic evidence
├── compounds/              # AlphaCompoundSpec, ReactionSpec, identity
├── compound_library/       # evidence, claims, retrieval, renderers
├── distillation/           # alpha decomposition, ablation, contrast
├── alpha_bank/             # AlphaUnit, snapshots, monitoring
├── expression_engine/      # typed executable representation
├── implementation/         # planner, compile/test harness
├── engine_adapter/         # proprietary Java boundary
├── agents/                 # context builders and schema-validated calls
├── search_policy/          # later broad/deep/random/human modes
├── redaction/              # tier-aware prompt and output controls
├── sealed/                 # separate deployment/identity
├── dashboard/              # read-only operator view
├── cli/                    # lab command
├── registry/ specs/ prompts/ policies/
└── docs/runbooks/
```

---

# 31. Acceptance metrics

## Scientific calibration

- planted-signal recovery;
- null false-positive rate;
- leakage rejection;
- interval coverage;
- exact replay.

## Closed-loop acceptance

- thesis-to-conclusion completion rate;
- compile success and bounded repair count;
- compound evidence written with full scope;
- negative knowledge retained;
- next campaign retrieves prior knowledge;
- no unregistered trial.

## Research-system learning

- faster convergence to useful alpha;
- reuse of supported compounds;
- expensive tests per useful alpha;
- repeated dead-end rate;
- out-of-sample degradation;
- Alpha Bank differentiation;
- useful reactivation of stale/negative compounds.

## Governance

- prohibited data exposures: zero;
- unauthorized sealed accesses: zero;
- expired approvals used: zero;
- LLM-calculated statistics: zero;
- free-form q execution: zero;
- proprietary source exposure: zero.

## Operational

- event replay/rebuild success;
- Redis-loss recovery;
- KDB snapshot verification;
- Java adapter deterministic replay;
- complete lineage and renderability;
- model manifest and provenance coverage.

---

# 32. Foreseeable challenges and planned responses

| Challenge | Planned response |
|---|---|
| Compound combinations grow exponentially | Limit depth, functions, candidate and reaction budgets; staged screening; deterministic diversity selection |
| Token usage and external-model cost | Use approved local open-weight models for high-volume work; deterministic enumeration; external escalation only after bounded failure |
| Early incorrect Library conclusions bias later research | Evidence states, scope, contradictions, recency, periodic revalidation; tentative knowledge is a prior, not fact |
| Negative evidence creates excessive path dependence | Deprioritize rather than ban; require material-difference statement; retain random exploration budget |
| Small expressions still overfit after large search | Full trial ledger, data-role separation, multiple-testing correction, sealed and forward evidence |
| Coding agent fails to compile or invents interfaces | Sanitized stubs, compile/test harness, structured error repair, bounded retries, escalation |
| KDB fast assay and Java replay disagree | Versioned bindings, golden intervals, attributable equivalence reports, lineage block on unexplained divergence |
| Compound utility is difficult to isolate | Ablation, contrastive tests, parent comparisons, interaction surplus, uncertainty bounds |
| Alpha Compound definition becomes too broad | Typed compound kinds, executable representation, evidence requirements, human-readable renderers |
| Library becomes a text-summary dump | Structured entities and claims; raw results immutable; LLM summaries are advisory views only |
| Model-origin policy is violated by a derived artifact | Full base/fine-tune/merge/adapter/quant lineage review and approval |
| Search controller optimizes a misleading metric | Compare search policies under frozen budgets and multiple meta-methodology measures |
| Long-lived workflows overwhelm RQ | Transactional outbox now; migrate to durable orchestration when observed recovery complexity crosses policy trigger |

---

# 33. Current implementation reality

The present capability can generate a plausible thesis and candidate expression from a simple prompt.

The current bottleneck is reliable implementation:

- generated code may not compile;
- internal interfaces may be invented or misunderstood;
- repeated repair may be inconsistent;
- the research loop cannot be considered closed until code, data, evidence, conclusion, and knowledge update are reproducible.

Therefore, engineering priority is:

> **reliable controlled implementation and one complete loop—not higher-volume thesis generation.**

---

# 34. First milestone

The first milestone is achieved when one experiment completes this loop:

```text
Thesis
  ↓
Candidate expression / Alpha Compound graph
  ↓
Implementation
  ↓
Compile and test
  ↓
Backtest and deterministic statistics
  ↓
Conclusion
  ↓
Compound evidence and utility profile
  ↓
Compound Library update
  ↓
Follow-up thesis or alpha path
  └──────────────────────────→ next loop
```

The result may be positive, negative, or inconclusive. Success is the integrity and reproducibility of the learning loop.

---

# 35. Longer-term uses

## 35.1 FX electronic trading

- signal research;
- execution and hedging studies;
- venue and cross-market behavior;
- conversion of trader observations into reproducible evidence.

## 35.2 FX voice trading

- convert market colour and client observations into testable theses;
- retain institutional knowledge beyond individual traders.

## 35.3 Cross-asset research

- rates, futures, options, credit, commodities;
- cross-asset relative value and lead–lag compounds.

## 35.4 Client-configured quantitative products

Longer-term governed path:

```text
client objective and constraints
→ strategy research
→ backtest and risk analysis
→ human/risk/conduct/product approval
→ deployment and monitoring
```

This is not an immediate autonomous product-generation promise. It requires full suitability and governance.

---

# 36. Final conclusion

v5.1 designed a scientifically disciplined alpha-research laboratory. v6.0 retains that discipline but changes what the institution learns and remembers.

The central loop is no longer only:

```text
generate factor → test factor → store result
```

It becomes:

```text
distil knowledge
→ create Alpha Compounds
→ compose recursively
→ test progressively
→ qualify alpha
→ observe trading behavior
→ distil new knowledge
```

The principal differentiator is:

> **On top of generating useful alpha, the laboratory makes the Alpha Compound the persistent unit of discovery, evidence, and institutional memory.**

Alphas can come and go. The Compound Library is intended to preserve the deeper, more structural knowledge that helps the organization create new alphas, avoid repeated dead ends, understand decay, and reconsider old ideas when the market context changes.
