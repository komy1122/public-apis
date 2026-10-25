# Research API × Program/Idea Crosswalk — 2026-10-25 delta v0.2

**Purpose:** proposal and merge-evidence map for [14-provider registry](api_registry.json). Research programs and research questions retain their distinct research units; no commercial-data grants, API credentials or proof of scientific validity. Source is a discovery directory, not each provider's contract. **Network default OFF; mock-first.**

## Existing independent programs (9)
| Program | API candidates | Read-only use/initial gate | Explicitly excluded inference |
|---|---|---|---|
| AIVC | Crossref/OpenAlex metadata; World Bank context only if prespecified | Prior-art identifiers & independent macro control metadata; [AIVC draft PR #5](https://github.com/komy1122/ai-adoption-to-value/pull/5) | Causality and team/workflow effects from API counts |
| RAD | CISA KEV + NVD; Crossref/OpenAlex references | Simulated vulnerability-priority scenario provenance; [RAD draft PR #11](https://github.com/komy1122/risk-adaptive-delegation/pull/11) | 'RiskAdaptive' as fourth permission mode; real exploit |
| EAO | OpenAlex, Crossref, GitHub REST, SEC EDGAR, USPTO ODP, FRED, World Bank | Metadata provenance and missingness by firm×quarter; [EAO draft PR #25](https://github.com/komy1122/enterprise-ai-observatory/pull/25) | Real AI capability score from presence of public digital traces |
| WCLM | World Bank country-year, FRED vintage, conditional RemoteOK/GitHub REST | [Merged #1](https://github.com/komy1122/workforce-competency-labor-mobility/pull/1) adds offline World Bank indicator context | Worker mobility/skill/treatment effect from macro data |
| SEG | Crossref DOI, OpenAlex/SS/arXiv discovery | [Merged #2](https://github.com/komy1122/scholarly-evidence-graph/pull/2) adds offline DOI candidate and rejection of mismatched DOI | Verified passage or claim–citation edge |
| ScholarEvolve | Crossref/OpenAlex/arXiv discovery through SEG, no autonomous write | Holdout audit and citation provenance; no independent scientific-agent training | Improved scientific reasoning from number of retrieved papers |
| Synthetic Persona/BDT | Public macro World Bank only if approved as aggregate context | Synthetic/human validation proposal; no live recruitment | N synthetic agent runs = N actual human participants |
| ZTA MSP | CISA KEV, optional NVD | [ZTA draft #3](https://github.com/komy1122/graduation-ai-network-ops/pull/3) global reference with mock parser | Local customer asset compromise / action authority |
| Explainable AIOps | CISA KEV/NVD reference; research Crossref | Safe synthetic incident fixtures | Operational MTTR and calibrated human reliance from threat catalogs |

## Twelve candidate RQs (not independently approved 12 projects)
| Candidate | Sources | Unit, measure and gate |
|---|---|---|
| GATE | CISA KEV optional as scenario labels; GitHub for tool audit examples | action episode, policy decision vs executed authority, require trace reconciliation |
| HARC | Crossref/OpenAlex prior-art identifiers | operator×incident, correct use of AI advice, consented human benchmark |
| EDP | Crossref/OpenAlex, arXiv version | claim×source version, corrections, drift recall and source hash |
| AOR | CISA KEV/NVD for fault labels | incident×action, risk-weighted loss/rollback; static baselines |
| SEGI | World Bank macro only, NCS/ESCO/O*NET source-license review | occupation×skill×time, demonstrated performance evidence (not credential assertion) |
| GID | research literature & GATE audit fixtures | policy×enforcement, measurement under AIVC/GATE |
| EACS | GitHub public repos; OpenAlex patents/SEC only with entity resolution | firm×time coverage corrected; within EAO P1 |
| SAIL | Crossref/OpenAlex prior-art | person×task×week unaided retention, ethics/IRB |
| STRG | World Bank aggregate contextual only if licensed, not participant proxy | synthetic/human matched scenario, external validity |
| AMPI | KEV/NVD advisory categories | memory/tool injection **defensive sandbox**, authority bypass attempts |
| SSIA | Crossref/OpenAlex/arXiv + frozen reference | agent×held-out scientific claim, groundedness and leakage |
| IAD | KEV incident severity contextual only | approval_id×action_hash×time, accountability audit |

## Verified source constraints / change-sensitive terms (2026-10-25)
- **Crossref** official REST docs: https://www.crossref.org/documentation/retrieve-metadata/rest-api/ and https://www.crossref.org/documentation/retrieve-metadata/rest-api/access-and-authentication/. Public/polite access; use a truthful contact mailto and identifying User-Agent; obey runtime rate/concurrency response headers and 429; publisher abstracts can have separate copyright. No 'DOI exists therefore claim true'.
- **OpenAlex** official authentication docs: https://help.openalex.org/api/authentication/ . Free-key/keyless budgets and cursor rules vary with tier; dynamically observe actual response headers and current official API terms, never hardcode blanket quotas. Do not serialize API keys, query URLs containing API keys, or login credentials. 
- **GitHub REST** https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api . Throttling/search rate varies by token and endpoint. Repository stars/hiring signals are weak firm capability proxies.
- **World Bank** https://datahelpdesk.worldbank.org/knowledgebase/articles/889392 and https://www.worldbank.org/ext/en/legal/terms-conditions . V2 access does not require a key. Data use and APIs have terms including restrictions on commercial API-facilitated uses; dataset-specific licenses/provenance and attribution must be checked before redistribution. Country-year ≠ human outcomes.
- **CISA KEV** https://github.com/cisagov/kev-data . Government-canonical cisa.gov feed mirrored in official CISA repo, CC0 data, changes continuously; compare timestamps and dataset SHA, never assert a customer CVE exposure from KEV presence alone.
- **NVD** https://nvd.nist.gov/developers/vulnerabilities . NVD CVEs are not direct observations of exploitation on a private network.
- **Others** USPTO ODP, SEC EDGAR, FRED, arXiv, Semantic Scholar, RemoteOK, Open-Meteo, AbuseIPDB: read current provider terms/auth/PII/rate restrictions prior to first live call. For potential IP addresses NEVER submit private/customer addresses to 3rd-party reputation APIs without lawful approval.

## CI and merge ledger, confirmed against GitHub Actions
| Repo/PR | Current reviewed status | Check evidence | Outcome |
|---|---|---|---|
| SEG #2 | MERGED into main | GitHub Actions [synthetic smoke successful](https://github.com/komy1122/scholarly-evidence-graph/actions/runs/40157766278), npm test & demo | merge SHA `9b34b063a30822a06163fca6173978b8191ab5a7`; metadata adapter, not paper validation |
| WCLM #1 | MERGED into main | GitHub Actions [synthetic smoke successful](https://github.com/komy1122/workforce-competency-labor-mobility/actions/runs/40157768195), npm test & demo | merge SHA `4630ee67d484288a604b2d61fc9b5e884b27775a`; macro adapter, not worker outcome |
| ZTA #3 | DRAFT, HOLD | [Python starter checks failed](https://github.com/komy1122/graduation-ai-network-ops/actions/runs/40157865148), 47/50 passed; [portable matrix passed](https://github.com/komy1122/graduation-ai-network-ops/actions/runs/40157865147) | `src.reproduce` import error and line-ending-sensitive dataset hash; cannot merge |
| EAO #25 | DRAFT, HOLD | No workflow runs linked to inspected head | read-only OpenAlex/Crossref/GitHub probe needs CI and per-provider legal/performance checks |
| AIVC #5, RAD #11, fork #1 | DRAFT, HOLD | No linked workflow runs on inspected heads | docs and canonical registry only; needs code/schema validation and review |
| EAO #23 (prior 9+12 audit) | DRAFT, HOLD | `mergeable=false` in inspection | manual conflict reconciliation needed; no automatic merge |

## Cross-app synchronization contract
Notion/Drive describe evidence gate, primary repo, PR/commit SHA, last verified time, test outcome and **scope limits**. Gmail is a **notification evidence source only**, never a commit oracle. Canva slides are derivative dissemination, not the research/source of truth. Context7 returns current software docs, not peer-reviewed evidence. No automated bidirectional sync is implemented by these metadata adapters.
