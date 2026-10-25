# Public API Research Integration Registry · v0.1.0 (2026-10-25)

Fork source: [public-apis/public-apis](https://github.com/public-apis/public-apis). **This is a research overlay; do not overwrite the upstream README.**

## Status and caveats
- Forked repository confirmed. Registry includes **14 candidate provider APIs**, not 14 live connectors.
- `implementation_status` distinguishes proposed/reference prototype from production collector; `verified_live=false` until actually authenticated, called, and documented.
- Neither MIT licensing of the directory nor `Auth: No` implies unrestricted usage or redistribution. Recheck source terms at execution time.
- No API key, scraped private data, full-text research document, customer identifier, or address should be committed.
- Failed API access must be `unavailable`/unknown, never zero. Preserve `occurred_at`, `available_at`, `retrieved_at`, request URL, SHA-256 of permitted raw response, and provider/version.
- Do not automatically sync fork with upstream without reviewing license changes and security risks.

## Research-specific mapping
| Research | Candidate sources | First acceptable milestone | Data boundary |
|---|---|---|---|
| SEG / Meta-Research | Crossref, OpenAlex, Semantic Scholar, arXiv | DOI canonicalization with mocked and optionally live metadata fetch | citation counts ≠ verified scholarly claims; full-text and reviewers separate |
| Enterprise AI Observatory | OpenAlex, GitHub REST, SEC, World Bank, USPTO, FRED | Read-only OpenAlex/Crossref + GitHub metadata collector, no firm classification | digital trace ≠ validated AI capability |
| Graduation NetOps / AIOps | CISA KEV, NVD; Open-Meteo conditionally | KEV read-only feed; synthetic offline unit tests | no device actuation, no exploit scanning |
| WCLM | World Bank, GitHub, RemoteOK (conditional) | macro trend metadata retrieval, not occupation inference | labor market ≠ remote jobs sample |
| RAD / AIVC | KEV for scenario conditions, academic evidence | reading reference-only adapters and synthetic actions | API observation ≠ human-agent causal effect |
| ESG / HEPV | World Bank, Open-Meteo | aggregated public context only | national / weather indicators ≠ institution ESG score |

## Release gates
1. G0: per-source legal use, privacy, ethics and research unit.
2. G1: API version, response schema, request timeout, 429/403 backoff, raw hash and origin.
3. G2: offline test and semantic data-quality contract.
4. G3: verify time availability, source coverage, duplication, entity resolution, and validity.
5. G4: independent review and reproducible versioned evidence before claiming research results.

## Official plugin comparisons
- **Claude:** https://github.com/anthropics/claude-plugins-official and https://claude.com/marketplace/plugins (official Anthropic-managed listings; external plugins may be third party).
- **Codex:** https://developers.openai.com/plugins and https://developers.openai.com/plugins/build/plugins (skills + MCP + optional UI/hooks).
- **OpenAI Developers for Claude:** https://developers.openai.com/learn/developers-codex-plugin, install only after source and permission review.
- Prefer read-only connectors. Never embed live API keys in a plugin manifest; do not install plugin code implicitly just because this catalogue lists it.

## Verification statement
This document is an **integration design and gated prototype inventory**. It does not claim 14 API calls, live firm panels, field outcomes, peer-reviewed results, or automated Notion/Gmail/Canva synchronization.
