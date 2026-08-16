# Devin Prompt Sequence — Computational Alpha Discovery Laboratory v6.0
## Alpha Compound Discovery, Distillation, and Institutional Learning

**Purpose:** A staged, copy-and-paste execution plan for a Devin coding server.  
**Normative architecture:** `Computational Alpha Discovery Laboratory — v6.0`  
**Operating rule:** Give Devin one bounded build prompt at a time. Do not ask it to build the complete laboratory in one task.

---

# 1. What changed from the v5.1 prompt sequence

The v5.1 sequence correctly prioritized calibration, authority, deterministic statistics, KDB contracts, and proprietary Java boundaries. v6.0 preserves those controls but changes the implementation order around a new central research object:

> **The Alpha Compound is the persistent unit of discovery, evidence, and institutional memory.**

The major sequencing changes are:

1. Build `AlphaCompoundSpec`, `ReactionSpec`, evidence states, and the Compound Library projection early.
2. Move compile/test/repair reliability earlier because implementation is the current bottleneck.
3. Close one complete synthetic or approved-data learning loop before implementing broad candidate search.
4. Treat questions as conditional branches, not a mandatory Interviewer stage.
5. Add Compound Distillation and a bidirectional relationship between Compound Library and Alpha Bank.
6. Defer broad/deep/random/human-guided search-policy optimization until the loop works.
7. Enforce the company prohibition on Chinese-origin model lineages.
8. Evaluate the research methodology itself: convergence speed, compound reuse, test efficiency, out-of-sample stability, and differentiated Alpha Bank value.

---

# 2. Recommended execution phases

## Phase A — Calibrated closed loop

Prompts 0–7 produce:

```text
specification discipline
→ repository bootstrap
→ event/authority core
→ Compound Library schemas
→ fake KDB + deterministic statistics
→ controlled expression engine
→ compile/test harness
→ one complete synthetic learning loop
```

Do not proceed to real research unless Prompt 7 passes.

## Phase B — First real FX loop

Prompts 8–11 add:

```text
approved model routing
→ approved KDB adapter
→ frozen real ResearchBrief
→ one real Stage 0–2 campaign
→ scoped Compound Library update
```

## Phase C — Institutional learning and high fidelity

Prompts 12–16 add:

```text
Library-aware retrieval
→ Alpha Bank and Compound Distillation
→ Java adapter
→ recursive compound composition
→ comparative search policies
```

## Phase D — Protected validation and scale

Prompts 17–20 add:

```text
review and selection accounting
→ sealed OOS
→ T0/cross-asset extensions
→ forward shadow and hardening
```

---

# 3. Materials to place in the repository before Prompt 0

Place the normative specification at:

```text
docs/specs/computational_alpha_discovery_v6_0.md
```

Place v5.1 and prior reviews under:

```text
docs/reference/
```

They are historical context only. They do not override v6.0.

Create Git-ignored placeholders:

```text
local_only/kdb/
local_only/java_engine/
local_only/models/
local_only/policy/
```

Never commit:

- credentials;
- real client-flow rows;
- client identifiers;
- proprietary Java source;
- confidential KDB metadata not approved for Git;
- model weights;
- restricted prompt payloads;
- pristine holdout data.

Recommended initial configuration:

```yaml
repo_url: <REPO_URL>
default_branch: main
spec_path: docs/specs/computational_alpha_discovery_v6_0.md
python_runtime: '3.12'
python_environment: uv
pc_runtime: Linux_or_WSL2
postgres: enabled
redis_rq: enabled
artifact_store_v0: local_content_addressed_filesystem
kdb_mode_initial: fake
java_mode_initial: fake
model_mode_initial: mock_or_approved_endpoint
external_models_initial: disabled
allowed_model_origin_policy: non_chinese_origin_only
```

Pin dependencies and container images. Do not use floating `latest` tags.

---

# 4. Global execution contract

Prepend this block to every Devin build prompt.

```text
You are implementing one bounded epic of the Computational Alpha Discovery Laboratory v6.0.

Normative specification:
  docs/specs/computational_alpha_discovery_v6_0.md

GLOBAL RULES

1. Work only on the scope explicitly named in this prompt. Do not implement later epics “for completeness.”
2. Read the normative specification and all persistent Devin handoff files before changing code.
3. The Alpha Compound is a persistent research object. Do not collapse compound identity, evidence, and alpha-candidate identity into one table or opaque JSON blob.
4. The Compound Library and Alpha Bank are distinct but linked institutional-knowledge stores. Do not treat one as an alias of the other.
5. Never invent KDB table names, q functions, timestamps, availability semantics, symbology, licenses, cost models, market behavior, or Java-engine capabilities.
6. Questions are conditional. When a material fact is missing, write a focused question or Capability Request and block only the dependent path. Do not insert a mandatory interview into every campaign.
7. Do not inspect, copy, summarize, or modify proprietary Java source. Use only owner-approved manifests, sanitized stubs, adapter endpoints, and fixtures.
8. LLMs never compute statistics, thresholds, evidence states, trial counts, promotion decisions, or state transitions. These are deterministic-code responsibilities.
9. LLMs never write or execute unrestricted q. KDB access is through versioned, reviewed, parameterized templates and a read-only gateway.
10. Every trial, reaction variant, bound compound evaluation, and alpha candidate must be registered before execution.
11. Small expressions are not assumed safe from overfitting. Preserve complete search/trial accounting and frozen data roles.
12. Negative evidence is scoped. A compound shown not to work is deprioritized, not permanently blacklisted. A retry requires a material-difference statement.
13. PostgreSQL is authoritative for events, operational state, approvals, budgets, trial registrations, Compound Library projections, and Alpha Bank projections. Git is authoritative for reviewed schemas, policies, prompts, registries, and frozen human-readable specs. KDB is authoritative for historical data. Large artifacts are content-addressed outside Git.
14. Redis/RQ is transport only. Use PostgreSQL transactional outbox/inbox semantics and deterministic idempotency keys.
15. Never commit secrets, T0 data, real client identifiers, proprietary source, raw restricted model payloads, or pristine holdout data.
16. External model access is disabled unless explicitly enabled. T0 data never reaches an external model. Raw market/client rows never enter prompts.
17. Company policy permits only approved non-Chinese-origin model lineages. Validate base, fine-tune, merge, adapter, and quantization provenance; do not infer origin from the uploader name.
18. Prefer the smallest implementation satisfying the current acceptance tests. Avoid speculative future abstractions.
19. Use schema versions and explicit migrations. Do not silently change persisted meaning.
20. Preserve human readability: consequential objects must be renderable by CLI, traceable by ID, and replayable from stored inputs.
21. Make small intentional commits on a dedicated branch. Do not merge automatically.
22. Before completion, run lint, type, unit, integration, migration, recovery, security, and acceptance tests relevant to this epic.
23. If the prompt conflicts with the normative spec, record the conflict in docs/devin/DECISIONS_NEEDED.md and continue only with non-conflicting work.

MANDATORY COMPLETION REPORT

Provide:
- branch name and commit hashes;
- architecture summary;
- changed-file list;
- exact commands and results;
- PASS/FAIL acceptance table with evidence paths;
- security/data-boundary review;
- migrations;
- unresolved questions and blockers;
- known limitations and deliberately deferred work;
- rollback instructions;
- exact recommended next prompt, without starting it.

Update on every epic:
- docs/devin/STATUS.md
- docs/devin/HANDOFF.md
- docs/devin/TRACEABILITY_MATRIX.md
- docs/devin/DECISIONS.md
- docs/devin/DECISIONS_NEEDED.md
- docs/devin/OPEN_QUESTIONS.md
- docs/devin/KNOWN_LIMITATIONS.md
```

---

# 5. Prompt 0 — Specification ingestion and implementation map

**No production code.**

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Ingest the v6.0 specification, inspect the repository, and produce an implementation map. Do not write production code.

Create or update only documentation and planning artifacts:

1. docs/devin/STATUS.md
2. docs/devin/HANDOFF.md
3. docs/devin/TRACEABILITY_MATRIX.md
4. docs/devin/DECISIONS.md
5. docs/devin/DECISIONS_NEEDED.md
6. docs/devin/OPEN_QUESTIONS.md
7. docs/devin/KNOWN_LIMITATIONS.md
8. docs/devin/IMPLEMENTATION_PLAN.md
9. docs/devin/THREAT_BOUNDARIES.md
10. docs/devin/TEST_STRATEGY.md
11. docs/devin/COMPOUND_MODEL_MAP.md
12. docs/devin/CLOSED_LOOP_ACCEPTANCE_MAP.md

The traceability matrix must map:
- every v6.0 non-negotiable principle;
- Alpha Compound, Reaction, Compound Evidence, Compound Library, Alpha Bank, and Distillation requirements;
- each build epic;
- each acceptance metric;
- each security boundary;
- each deferred search policy;

to proposed modules and tests.

Explicitly distinguish:
- compound construction spec from compound evidence;
- compound identity from candidate-alpha identity;
- Compound Library from Alpha Bank;
- deterministic enumeration from LLM proposal;
- the main research path from conditional question branches;
- structural overfitting controls from statistical controls.

Identify what can be built with fakes and what requires:
- approved KDB templates/endpoints;
- owner-authored Java manifests/stubs;
- approved model endpoints;
- conduct/compliance approval;
- pristine holdout authorization.

Ask no more than seven material questions. Do not ask for information that the specification already supplies.

Deliver a dependency graph that shows Prompts 0–7 ending in one closed synthetic learning loop. Stop after documentation review evidence is ready.
```

## Human gate after Prompt 0

Confirm that Devin correctly understands:

- the persistent research unit is the Alpha Compound;
- Compound Library and Alpha Bank are different;
- distillation is bidirectional;
- questions are conditional;
- first success means a closed learning loop, not a production alpha;
- search policy is deferred;
- model-origin policy is enforced.

---

# 6. Prompt 1 — Repository bootstrap and developer ergonomics

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Bootstrap the repository and local developer environment only. Do not implement research behavior.

Create branch:
  devin/v6-epic-01-bootstrap

Implement:

1. Python 3.12 uv workspace and lockfile.
2. Package/module skeleton matching the v6.0 repository layout.
3. Docker Compose for PostgreSQL and Redis only, with pinned images and health checks.
4. Alembic or approved migration framework.
5. Pytest, Ruff, mypy/pyright, pre-commit, and CI.
6. `lab` CLI skeleton with version/help/doctor commands.
7. Structured JSON logging with correlation fields:
   event_id, thesis_id, campaign_id, compound_id, reaction_id,
   candidate_id, experiment_id, stage, job_id.
8. Content-addressed local artifact-store interface with fake implementation.
9. Configuration layering and .env.example without secrets.
10. Persistent Devin handoff files and Makefile targets:
    bootstrap, test, lint, typecheck, migrate, doctor.

Acceptance:
- clean clone/bootstrap succeeds;
- migrations create and roll back an empty schema;
- CLI doctor reports Postgres/Redis status;
- CI runs lint/type/unit tests;
- secret scan is clean;
- no research semantics are implemented.

Stop after bootstrap evidence is complete.
```

---

# 7. Prompt 2 — Authority, IDs, event ledger, projections, and outbox

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement the authority/event core.

Create branch:
  devin/v6-epic-02-authority-ledger

Implement:

1. Human-readable ID allocation with internal UUIDs for:
   IDEA, THESIS, CAMPAIGN, FAMILY, CMP, RXN, CAND, EXP,
   EVID, CLAIM, ALPHA, SNAP, DOMAIN, BIND, CAPREQ, EVENT.
2. Append-only event table.
3. Rebuildable current-state projections.
4. Git artifact registration by path, commit, and content hash.
5. Content-addressed artifact references.
6. PostgreSQL transactional outbox/inbox.
7. Deterministic job IDs and idempotent completion commits.
8. Optimistic concurrency or equivalent state-version protection.
9. CLI:
   lab show, lab trace, lab replay-event, lab projection rebuild,
   lab artifact verify.
10. Event schemas for future compound/library/bank operations without implementing those behaviors yet.

Tests:
- reconstruct projections from events;
- reject event mutation/deletion;
- concurrent duplicate intent creates one durable job;
- Redis loss does not lose intent;
- duplicate completion does not duplicate state;
- Git hash mismatch fails closed;
- artifact content mismatch fails closed.

Do not implement KDB, stats, compounds, models, or Java.
```

---

# 8. Prompt 3 — Alpha Compound domain model and Compound Library core

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement v6.0 Alpha Compound schemas, evidence model, lineage, reactions, and a minimal Compound Library projection. No LLM calls and no market-data evaluation.

Create branch:
  devin/v6-epic-03-compound-library-core

Implement Pydantic models, database schemas, migrations, renderers, and CLI for:

1. AlphaCompoundSpec
   - compound_kind;
   - semantic definition;
   - parents;
   - function/reaction reference;
   - executable representation placeholder;
   - expected utility roles;
   - domain requirements;
   - recursive depth;
   - canonical identity fields.
2. ReactionSpec
   - input compounds;
   - function;
   - rationale;
   - expected property;
   - parameter budget;
   - falsification;
   - material difference from prior failures.
3. Compound evidence states:
   HYPOTHESIS, TENTATIVE, SUPPORTED, REPLICATED, CONTRADICTED,
   STALE, SUPPORTED_NEGATIVE, REJECTED_FOR_SCOPE.
4. Scoped CompoundEvidence and CompoundClaim.
5. CompoundContradiction and CompoundNegativeEvidence.
6. CompoundLineage and source/distillation lineage placeholders.
7. Compound Library read projection and immutable evidence events.
8. Reconsideration policy: negative evidence deprioritizes; retry requires a material-difference statement.
9. CLI:
   lab compound new/show/lineage/evidence/add-evidence/contradict/deprioritize/reconsider.
10. Markdown renderer showing scope, utility roles, evidence, contradictions, recency, and reconsideration conditions.

Tests:
- simple and composite compounds validate;
- construction spec cannot be mutated after freeze;
- evidence can be appended without changing the spec;
- unsupported global “good/bad” labels are rejected;
- negative evidence without scope is rejected;
- retry of a deprioritized compound is blocked without material difference;
- lineage cycles are rejected;
- recursive depth is computed deterministically;
- projections rebuild exactly from events.

Do not implement Alpha Bank, KDB, statistics, code generation, or search.
```

---

# 9. Prompt 4 — Fake KDB gateway, evaluation frames, and deterministic statistics

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement data contracts, a fake read-only KDB gateway, aligned evaluation frames, and deterministic statistics sufficient for calibration and compound assays.

Create branch:
  devin/v6-epic-04-fake-kdb-stats

Implement:

1. DomainSpec, DataSnapshot, DataBinding with explicit schema versions.
2. Fake gateway API matching the future real gateway:
   create_snapshot, probe_domain, materialize_primitive,
   build_label, build_environment_blocks, build_evaluation_frame,
   build_interaction_frame, build_ablation_frame.
3. Content hashes and snapshot verification.
4. Point-in-time availability fields and leakage lints.
5. Arrow/Parquet evaluation-frame artifacts.
6. Deterministic Stats Service:
   - Pearson and rank correlation;
   - per-block statistics;
   - sign consistency;
   - block bootstrap;
   - parent and ablation comparison;
   - incremental utility;
   - simple interaction surplus;
   - null and shuffled controls;
   - timestamp perturbation;
   - confidence intervals.
7. Deterministic ReviewCard fields; no LLM narration.
8. Known-answer synthetic fixtures.

Tests:
- planted standalone compound recovered;
- planted interaction-only compound recovered;
- shuffled return rejected at calibrated rate;
- future-data trap rejected;
- ablation identifies the planted contributor;
- evaluation frame is identical for identical inputs;
- snapshot mutation is detected;
- rank statistics are calculated from frames, not inadequate aggregate moments.

Do not implement real q, model calls, or Java.
```

---

# 10. Prompt 5 — Typed expression and reaction engine

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement the minimal typed executable representation for Alpha Compounds and reactions.

Create branch:
  devin/v6-epic-05-expression-engine

Implement:

1. Typed expression graph/tree for registered primitives and functions.
2. Initial allowlist:
   ts_zscore, cs_zscore, ma, ema, diff, lag, ts_rank, cs_rank,
   clip, sign, add, sub, mul, div_safe, min, max, cond_gate,
   residualize, peer_spread.
3. Explicit time-series vs cross-sectional semantics.
4. Units, sampling, windows, availability, reset, and missing-data contracts.
5. Canonicalization:
   - commutative sorting;
   - constant/window normalization;
   - primitive/function semantic versions;
   - no implicit resampling.
6. Compound semantic hash and bound hash.
7. Reaction compilation from parent compounds.
8. Complexity measures:
   depth, node count, parameters, effective search degrees.
9. Deterministic bounded parameter enumeration.
10. Deduplication and batch-diversity selector.
11. Interpreter against fake evaluation frames.
12. CLI render of the expression and compound lineage.

Tests:
- equivalent expressions canonicalize identically;
- semantically different bindings remain separate;
- time-series/cross-sectional misuse fails;
- future availability fails;
- div_safe and NaN rules are total;
- lineage depth limits are enforced;
- candidate variants are registered before evaluation;
- deterministic enumeration is reproducible.

Do not allow arbitrary Python or free-form q as candidate representation.
```

---

# 11. Prompt 6 — Controlled implementation and compile/test/repair harness

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Build the controlled implementation lane and compile/test/repair harness using fake/sanitized interfaces. This epic addresses the current implementation bottleneck.

Create branch:
  devin/v6-epic-06-implementation-harness

Implement:

1. ImplementationPlan schema mapping a CandidateAlphaSpec/compound graph to:
   - KDB template selections;
   - generated Python modules where permitted;
   - fake Java graph/SDK stubs;
   - required tests.
2. Sandboxed code workspace:
   - network disabled;
   - no credentials;
   - read-only fixtures;
   - CPU/memory/time limits;
   - dedicated output directory.
3. Compile/lint/type/unit/integration test harness.
4. Structured failure schema:
   compile_error, missing_interface, type_error, test_failure,
   timeout, policy_violation, unsupported_capability.
5. Bounded repair controller:
   - maximum two local/model repair attempts by policy;
   - exact error bundle supplied;
   - no unrelated file edits;
   - escalation to human/approved stronger model after limit.
6. Fake Coder adapter first; optional approved model adapter behind interface.
7. File allowlist and diff-size limits.
8. Provenance capture for prompts/model/runtime if a real model is used.
9. Golden tasks with injected nonexistent APIs to ensure invention is caught.

Tests:
- valid generated implementation compiles and passes;
- invented interface fails clearly;
- repair changes only allowed files;
- repair limit is enforced;
- network and secrets are unavailable;
- unsupported capability creates a focused Capability Request, not guessed code;
- results are deterministic in model-disabled fixture mode.

Do not connect to proprietary Java source or real KDB.
```

---

# 12. Prompt 7 — First complete synthetic learning loop

**This is the first major acceptance gate.**

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Wire one complete, reproducible synthetic Alpha Compound learning loop. Do not add broad search, Alpha Bank portfolio optimization, sealed data, or real proprietary integrations.

Create branch:
  devin/v6-epic-07-first-closed-loop

Implement a deterministic Governor path:

1. Accept a hand-written or fixture signal idea.
2. Freeze a ResearchBrief.
3. Create a simple Alpha Compound graph and CandidateAlphaSpec.
4. Produce an ImplementationPlan.
5. Compile and test the implementation through the Prompt-6 harness.
6. Register all trials before execution.
7. Run fake-KDB materialization and deterministic statistics.
8. Produce a ReviewCard.
9. Produce a deterministic conclusion state:
   SUPPORTED, UNSUPPORTED, INCONCLUSIVE, or FOLLOW_UP_REQUIRED.
10. Append scoped CompoundEvidence and update the Compound Library projection.
11. If supported, create only an alpha follow-up placeholder; do not promote to a real Alpha Bank.
12. If unsupported, retain scoped negative knowledge and retry conditions.
13. Generate a complete `lab trace` and Markdown closure report.
14. Feed the updated Library into a second fixture idea-generation context and prove the prior result is retrieved.

Run at least four fixture campaigns:
- planted standalone predictor;
- planted interaction-only compound;
- shuffled/null;
- future-data leakage trap.

Acceptance:
- all four reach correct conclusions;
- code compiles/tests or fails through the intended path;
- every result has full lineage;
- negative evidence is retained;
- second-loop context retrieves relevant prior evidence;
- kill/restart resumes without duplicate trials;
- no LLM is required for deterministic fixture acceptance.

Stop after `docs/reports/V0B_CLOSED_LOOP_ACCEPTANCE.md` is complete.
```

## Mandatory human gate after Prompt 7

Do not proceed unless the owner accepts:

- the compound/evidence schema;
- the closed-loop trace;
- the negative-knowledge behavior;
- compile/test/repair behavior;
- data and state reproducibility;
- the decision that broad search remains deferred.

---

# 13. Reusable milestone audit prompt

```text
Act as an independent skeptical auditor. Do not implement new features.

Review the current branch against:
- docs/specs/computational_alpha_discovery_v6_0.md;
- the epic prompt;
- docs/devin/TRACEABILITY_MATRIX.md;
- acceptance evidence.

Check especially:
- compound spec/evidence separation;
- Compound Library vs Alpha Bank separation;
- pre-execution registration;
- negative-evidence scope;
- data leakage;
- deterministic statistics;
- idempotency/recovery;
- invented KDB/Java facts;
- model-origin policy;
- misleading PASS claims.

Classify findings BLOCKER/HIGH/MEDIUM/LOW with file/line evidence. Do not weaken tests or controls to obtain PASS.
```

---

# 14. Prompt 8 — Model router, provenance, and role qualification

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement a minimal model-router interface and qualification harness. Do not make any model a scientific gate.

Create branch:
  devin/v6-epic-08-model-router

Implement:

1. Role aliases:
   reasoner_local, coder_local, narrator_local, utility_local,
   embedding_local, external_hard_coder, external_red_team.
2. Provider-neutral endpoint interface.
3. Mock provider for tests.
4. ModelManifest and full lineage/provenance schema:
   base developer/origin, license, revision, fine-tune/merge/adapter lineage,
   quant artifact, converter, hashes, serving runtime, approval.
5. Policy engine that rejects unapproved Chinese-origin lineages, including derived models.
6. Role-specific qualification harness:
   - thesis/schema tasks;
   - compound-reaction reasoning;
   - coding tasks with hidden tests;
   - narration fidelity traps;
   - structured-output validity;
   - latency/tokens/memory fields.
7. Scored regression probes, not exact text hashes.
8. Budget and escalation policy:
   local high-volume work;
   bounded failure before stronger/external escalation;
   external advisory only.
9. Exact call provenance and payload hash logging.
10. Endpoint health and localhost/tunnel assumptions.

Tests:
- prohibited lineage rejected;
- uploader-name disguise does not bypass base-lineage rule;
- model-disabled mode still works for deterministic pipeline;
- narrator cannot add numbers absent from ReviewCard;
- external provider disabled by default;
- T0 payload is blocked mechanically.
```

---

# 15. Prompt 9A — Real KDB adapter contract

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Prepare the real KDB adapter boundary using only owner-approved contracts. Do not discover schemas and do not write unrestricted q.

Create branch:
  devin/v6-epic-09a-kdb-contract

Required owner input:
- one approved non-T0 DomainSpec;
- one safe historical period;
- approved endpoint/connection wrapper;
- approved template functions;
- timestamp and availability semantics;
- resource budgets;
- snapshot/probe method;
- safe fixtures or extracts.

Implement:
1. Gateway client matching fake API.
2. Parameter schemas and allowlist.
3. Snapshot manifest and integrity verification.
4. Timeout, cancellation, scan budgets, and audit logs.
5. Feature/label/block/evaluation/interaction/ablation materialization.
6. Contract tests proving fake and real adapters return the same logical schema.
7. No raw q entry point.

If any owner input is missing, create a Capability Request and stop only the blocked integration path.
```

## Prompt 9B — Real KDB integration

Use only after the owner approves 9A contracts.

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Connect the approved read-only KDB research endpoint and pass the contract suite.

Do not inspect unrelated tables or infer fields. Execute only approved templates.

Acceptance:
- repeated approved materialization produces verified hashes;
- point-in-time availability tests pass;
- resource-budget violations fail closed;
- KDB identity is read-only;
- no unrestricted query path exists;
- outputs match the fake logical schema;
- incident and snapshot changes are detected.
```

---

# 16. Prompt 10 — First real ResearchBrief and domain selection

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Prepare and freeze the first real FX ResearchBrief. This is a human-reviewed research artifact, not an autonomous search campaign.

Create branch:
  devin/v6-epic-10-first-real-brief

Inputs:
- one human signal idea or approved model-generated idea;
- Compound Library retrieval, which may initially be sparse;
- Alpha Bank context, which may initially be empty;
- approved DomainSpecs;
- current capability manifests.

Implement/workflow:
1. Create draft thesis, mechanism, competing explanations, target and horizon.
2. Identify required observables.
3. Rank suitable domains deterministically plus advisory Data Scout narration.
4. Raise questions only for material unresolved blockers.
5. Create Capability Requests for missing data/API/engine functions.
6. Define initial Alpha Compounds and intended utility roles.
7. Freeze trial, reaction, and candidate budgets.
8. Freeze discovery/composition/validation data roles.
9. Freeze falsification and conclusion states.
10. Render an assumptions digest.
11. Require explicit owner approval before freeze.

Do not run the campaign. Stop after a signed/frozen ResearchBrief and owner acknowledgment.
```

---

# 17. Prompt 11 — First real Stage 0–2 closed loop

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Execute the frozen first real FX ResearchBrief through Stage 0–2 and update the Compound Library.

Create branch:
  devin/v6-epic-11-first-real-loop

Scope:
1. Use the frozen Brief only.
2. Create the approved initial compounds/reactions.
3. Use bounded deterministic variants.
4. Compile/test implementations.
5. Register every trial before execution.
6. Materialize approved KDB evaluation frames.
7. Compute deterministic compound and interaction evidence.
8. Produce ReviewCards and a campaign conclusion.
9. Append scoped Compound Library evidence.
10. Create a follow-up only as new lineage; never rewrite the original thesis.
11. Produce a negative-family closure if appropriate.
12. Generate complete trace and replay evidence.

No Java high-fidelity run, pristine sealed data, or broad search in this epic.

Acceptance:
- complete real-data lineage;
- reproducible conclusion;
- no result outside registered selection pool;
- no LLM calculation;
- scoped positive or negative compound knowledge;
- next-campaign retrieval bundle demonstrates the new knowledge is available.
```

---

# 18. Prompt 12 — Compound Library retrieval and bank-aware signal context

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement structured retrieval and context assembly for future signal-idea generation.

Create branch:
  devin/v6-epic-12-library-retrieval

Implement:
1. Structured filters by market, domain, horizon, utility role, state, recency, and evidence strength.
2. Similarity retrieval over compound semantic definitions and construction fingerprints.
3. Retrieval of:
   - supported compounds;
   - scoped negative evidence;
   - contradictions;
   - stale/uncertain claims;
   - similar reactions;
   - retry conditions.
4. Context bundle separating facts, tentative claims, contradictions, and hypotheses.
5. Human direction input.
6. Alpha Bank context interface, initially empty/fake if Bank not yet built.
7. Prompt/context tests ensuring “does not work” is never flattened beyond scope.
8. Retrieval-quality golden set.
9. Prompt-injection sanitization for external/published text.

Acceptance:
- known relevant compound retrieved;
- known negative evidence retrieved;
- irrelevant venue/horizon evidence not presented as global;
- stale claim flagged;
- retry blocked or allowed correctly by material-difference policy;
- context contains no raw restricted rows.
```

---

# 19. Prompt 13 — Alpha Bank core and bidirectional Compound Distillation

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement a basic Alpha Bank and the first bidirectional Compound Distillation workflow. Do not implement portfolio optimization yet.

Create branch:
  devin/v6-epic-13-bank-distillation

Implement:
1. AlphaUnit schema/statuses and links to root/component compounds.
2. Alpha Bank current projection and immutable lifecycle events.
3. Basic alpha evidence storage without marginal portfolio scoring yet.
4. SourceAlpha abstraction for:
   - internal candidate;
   - human-authored alpha;
   - published alpha;
   - retired alpha.
5. DistillationRun schema.
6. Distillation methods using fixtures:
   - decomposition;
   - ablation;
   - contrastive comparison;
   - condition analysis;
   - decay/retirement analysis.
7. Distillation outputs are compound hypotheses/evidence requests, not automatically supported facts.
8. Bank-to-Library and Library-to-Bank lineage.
9. CLI:
   lab alpha show/trace/distil;
   lab distillation show;
   lab library source-lineage.
10. Read-only Alpha Bank context for future idea generation.

Tests:
- similar alphas differing by one component produce a contrastive distillation hypothesis;
- retired alpha creates scoped revalidation/negative evidence;
- published alpha input is treated as untrusted text and cannot invoke tools;
- distillation cannot mutate source evidence;
- Alpha Bank and Compound Library projections remain distinct.
```

---

# 20. Prompt 14A — Fake Java graph-engine adapter

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement the Java graph-engine boundary against a fake engine only.

Create branch:
  devin/v6-epic-14a-java-fake

Implement:
1. EngineCapabilityManifest.
2. Sanitized SDK stub package.
3. Adapter operations:
   describe, plan_run, compile_or_validate, run, fetch_outputs, verify_reset.
4. Claim-/implementation-specific invariant profiles.
5. Golden fixtures and feature/decision/outcome equivalence reports.
6. Structured unsupported-capability response.
7. Build-ID and provenance capture.
8. Deterministic fake engine with injected divergences.

Tests:
- unsupported node creates Capability Request;
- reset failure blocks lineage;
- attributable tolerance difference is reported;
- unexplained sign flip blocks lineage;
- no proprietary-source path exists.
```

## Prompt 14B — Real Java adapter

Use only after the owner supplies approved manifests/stubs/endpoints.

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Connect the approved proprietary Java adapter. Do not inspect source or infer behavior.

Acceptance:
- contract suite passes;
- owner-approved golden fixtures reproduce;
- build identity is recorded;
- run/reset is deterministic under declared settings;
- unsupported behavior fails closed;
- no proprietary internals enter Git, prompts, logs, or external providers.
```

---

# 21. Prompt 15 — Recursive Alpha Compound composition

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Add bounded recursive Alpha Compound composition. Do not add active learning or unrestricted search.

Create branch:
  devin/v6-epic-15-recursive-composition

Implement:
1. Reaction proposal schema integration with Compound Composer adapter.
2. Deterministic bounded enumeration.
3. Default max depth 2; optional depth 3 only by explicit policy.
4. Function and parameter allowlists.
5. Parent comparison and ablation requirements.
6. Novelty against:
   - Compound Library;
   - scoped negative evidence;
   - current batch;
   - Alpha Bank components.
7. Batch diversity selection.
8. Retain/deprioritize workflow after assay.
9. New compound registration and lineage.
10. Trial accounting for reactions considered and variants tested.

Tests:
- simple compounds create a composite;
- composite can participate in one later generation within policy;
- depth cap blocks excess recursion;
- known failed reaction is deprioritized;
- materially different retry is permitted;
- intermediate compound with weak standalone but planted interaction utility is retained;
- all variants are registered before execution.
```

---

# 22. Prompt 16 — Search-policy experiment framework

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement a controlled framework to compare search policies. Do not declare a winner and do not train a surrogate model.

Create branch:
  devin/v6-epic-16-search-policy

Implement policies:
1. broad_parallel;
2. deep_lineage;
3. random_baseline;
4. compound_library_aware;
5. human_guided.

Requirements:
- identical frozen budgets where comparison requires;
- deterministic seeds;
- common candidate/function universe where appropriate;
- complete trial accounting;
- no pristine data use;
- policy cannot change evidence or gates;
- human-guided inputs are recorded and scoped.

Meta-methodology outputs:
- trials/dead ends to useful follow-up;
- expensive assays per useful candidate;
- reuse of supported compounds;
- repeated-failure rate;
- out-of-sample degradation on non-pristine validation;
- diversity against Alpha Bank;
- token and human-time costs.

Run only synthetic/approved validation fixtures initially. Stop after the framework and one controlled comparison report.
```

---

# 23. Prompt 17 — Deterministic review, selection accounting, and Stage 5

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement Stage-5 deterministic review and selection accounting.

Create branch:
  devin/v6-epic-17-review-selection

Implement:
1. chronological walk-forward primary estimates;
2. optional CPCV robustness;
3. CSCV/PBO as its own procedure;
4. DSR for Sharpe-like outcomes only;
5. trial-pool hierarchy:
   N_global_raw, N_related_history, N_selection_pool_raw,
   N_selection_pool_effective, N_reactions_considered,
   N_bound_variants_tested;
6. FDR/selection controls as frozen policy;
7. deterministic ReviewCard with thresholds and flags;
8. optional Evidence Narrator using only ReviewCard;
9. mechanism-review advisory memo;
10. provisional Alpha Bank marginal-value interface using frozen bank snapshot;
11. no LLM gate.

Tests:
- narrator trap: never invents numbers;
- unrelated global trial count is reported but not mechanically misused;
- related-history sensitivity is reported;
- CPCV and CSCV/PBO cannot be conflated;
- ReviewCard reproducible;
- fail/pass cannot be changed by narration.
```

---

# 24. Prompt 18 — Sealed OOS lifecycle

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Implement protected validation using sacrificial integration holdout first. Do not use pristine data until separately authorized.

Create branch:
  devin/v6-epic-18-sealed-oos

Implement:
1. integration holdout service;
2. pristine vintage schema and separate-identity deployment contract;
3. approved candidate/family hashes only;
4. aggregate-output allowlist;
5. lifetime information ledger;
6. related-family contamination propagation;
7. per-campaign and global budgets;
8. human authorization;
9. ordinary-worker access denial tests;
10. promotion of newly arriving time into forward vintages.

Acceptance:
- plumbing proven on sacrificial data;
- ordinary workers cannot read sealed mount;
- close variants cannot evade budget by renaming;
- every returned field is logged as consumed information;
- pristine activation remains disabled until owner approval.
```

---

# 25. Prompt 19 — T0 client flow and cross-asset extensions

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Add T0 client-flow and cross-domain capability extensions only after conduct/security approval.

Create branch:
  devin/v6-epic-19-t0-cross-asset

Implement:
1. conduct approval objects and expiry;
2. T0 aggregation, minimum cohorts, suppression, and output DLP;
3. client-ID rotation/lookback checks;
4. latency-to-availability checks;
5. observation/selection-bias statements;
6. cross-domain alignment profiles;
7. session/roll/greeks metadata;
8. tier-aware Compound Library evidence;
9. red-team exfiltration tests;
10. capability requests for missing flow/cross-asset data.

No raw T0 row may enter a prompt or general artifact store.
```

---

# 26. Prompt 20 — Forward shadow, meta-learning, hardening, and handoff

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Complete forward-shadow automation, research-system evaluation, operational hardening, and owner handoff. Do not add speculative research features.

Create branch:
  devin/v6-epic-20-forward-hardening

Implement/verify:
1. forward snapshot intake;
2. AlphaUnit monitoring and decay states;
3. distillation triggers on success, degradation, comparison, and retirement;
4. Compound claim revalidation/staleness;
5. research-system metrics:
   faster convergence, compound reuse, expensive tests, stability,
   Alpha Bank differentiation, institutional forgetting;
6. deterministic weekly evidence pack;
7. optional advisory synthesis;
8. no trained active-learning surrogate until policy data threshold;
9. clean install, migration, backup/restore, projection rebuild;
10. Redis-loss and worker-crash drills;
11. KDB and Java failure drills;
12. sealed isolation drill;
13. dependency/license/SBOM/model-provenance audit;
14. prompt-injection and data-exfiltration tests;
15. performance characterization;
16. service runbooks and read-only dashboard;
17. final owner smoke-test checklist.

Required reports:
- FINAL_ACCEPTANCE_REPORT.md
- CLOSED_LOOP_REPRODUCIBILITY.md
- RESEARCH_SYSTEM_METRICS.md
- SECURITY_AUDIT.md
- RECOVERY_DRILL.md
- PERFORMANCE_BASELINE.md
- MODEL_PROVENANCE_AUDIT.md
- OWNER_HANDOFF.md

Stop at release-candidate review. Do not deploy or promote any alpha automatically.
```

---

# 27. Fresh-session resume prompt

```text
You are resuming the Computational Alpha Discovery Laboratory v6.0.

Before work:
1. Read docs/specs/computational_alpha_discovery_v6_0.md.
2. Read all docs/devin files.
3. Inspect Git status, current branch, recent commits, migrations, and tests.
4. Reconstruct the current bounded epic and acceptance criteria.
5. Verify no proprietary/secret/T0 material is uncommitted.
6. Run current smoke tests.
7. Report your understanding, blockers, and exact next bounded action.

Do not infer scope from chat memory. Repository specs and signed decisions are authoritative.
Do not begin a different epic without its explicit prompt.
```

---

# 28. Defect-repair prompt

```text
[PREPEND GLOBAL EXECUTION CONTRACT]

TASK: Repair only these failed acceptance criteria:

<PASTE FAILURES AND EVIDENCE>

Rules:
- reproduce first;
- identify root cause;
- add regression test;
- do not redesign unrelated modules;
- do not weaken thresholds/security/lineage checks;
- do not delete fixtures;
- preserve compound evidence and trial history;
- if persisted meaning changes, add migration and rollback;
- run focused and full current-epic suites;
- provide before/after evidence.

Stop after named failures are repaired or clearly blocked.
```

---

# 29. Pull-request review prompt

```text
Act as a skeptical maintainer reviewing the current branch against:
- docs/specs/computational_alpha_discovery_v6_0.md;
- the epic prompt;
- docs/devin/TRACEABILITY_MATRIX.md;
- acceptance evidence.

Do not add features. Check for:
- Alpha Compound identity/evidence conflation;
- Compound Library/Alpha Bank conflation;
- missing distillation lineage;
- mandatory-question workflow accidentally introduced;
- unregistered trials/reactions;
- leakage or data-role contamination;
- LLM-calculated statistics or decisions;
- free-form q;
- invented Java/KDB facts;
- model-origin policy bypass;
- scoped negative evidence flattened into global truth;
- non-idempotent state;
- misleading PASS claims;
- premature search/active-learning features.

Classify BLOCKER/HIGH/MEDIUM/LOW with exact file/line and violated requirement. Do not merge automatically.
```

---

# 30. Human review gates

| After prompt | Human decision |
|---|---|
| 0 | Confirm architecture understanding and proprietary boundaries |
| 3 | Approve Alpha Compound/evidence/Library semantics |
| 4 | Approve statistical known-answer and interaction tests |
| 6 | Approve implementation sandbox and repair behavior |
| 7 | Confirm one complete loop works before real integration |
| 8 | Approve model provenance and role assignments |
| 9A | Supply/approve KDB contract |
| 10 | Approve first real ResearchBrief and assumptions |
| 11 | Review first real evidence and Library update |
| 13 | Approve Alpha Bank/Distillation semantics |
| 14A | Supply/approve Java stubs and manifest |
| 16 | Review search-policy comparison before scale |
| 17 | Review statistical selection policy |
| 18 | Review sealed isolation before pristine activation |
| 19 | Conduct/security approval for T0 |
| 20 | Release-candidate review |

---

# 31. What not to ask Devin to do

Do not ask:

```text
Build the whole laboratory from the v6 spec.
```

```text
Connect to KDB and discover the tables yourself.
```

```text
Inspect the proprietary Java engine to work out its behavior.
```

```text
Generate thousands of Python strategies and keep the profitable ones.
```

```text
Treat every operator or AST node as a proven Alpha Compound.
```

```text
Mark a compound globally good or bad.
```

```text
Let an LLM calculate statistics or update evidence states directly.
```

```text
Use the same sample to discover compounds, search compositions, and claim independent validation.
```

```text
Use a Chinese-origin model because the quantized artifact was uploaded by a non-Chinese account.
```

```text
Use pristine holdout data to test plumbing.
```

```text
Optimize search policy before one closed loop works.
```

---

# 32. Minimum owner-supplied interface package

## KDB

```text
- one approved non-T0 DomainSpec;
- one safe snapshot period;
- approved endpoint/connection wrapper;
- reviewed templates/functions;
- time and availability semantics;
- resource budgets;
- integrity/probe method;
- safe fixtures or extracts.
```

## Java

```text
- EngineCapabilityManifest;
- sanitized SDK stubs;
- adapter contract;
- event/reset semantics;
- supported implementation classes;
- safe golden fixtures;
- build-ID mechanism;
- scoped invariants/tolerances.
```

## Models

```text
- approved endpoint addresses and auth;
- model manifests with complete lineage;
- non-Chinese-origin approval;
- exact revision/quant/runtime hashes;
- role qualification results;
- no market-data credentials on inference hosts;
- external provider disabled until approved.
```

## Governance

```text
- conduct/compliance scope;
- T0 aggregation/suppression policy;
- external-payload policy;
- sealed authorization policy;
- Alpha Bank policy;
- human approval identities and expiry.
```

---

# 33. Practical recommendation

Give Devin Prompts 0–7 first and stop.

The most important early deliverable is not a dashboard, a large factor generator, an active-learning system, or a production alpha. It is evidence that the lab can:

```text
receive a thesis
→ represent Alpha Compounds
→ create and test implementation
→ calculate deterministic evidence
→ reach a scoped conclusion
→ update the Compound Library
→ use that knowledge in the next loop
```

Only after that closed loop is reproducible should Devin receive real KDB integration, real model endpoints, Java integration, recursive search, sealed validation, or sensitive data.
