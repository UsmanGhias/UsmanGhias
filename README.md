<!-- Profile README for Usman Ghias · https://usmanghias.co.uk -->

<a href="https://usmanghias.co.uk">
  <picture>
    <source type="image/webp" srcset="assets/brand/profile-hero-animated.webp">
    <img src="assets/brand/profile-hero-animated.gif" width="100%" alt="Usman Ghias - Lead Distributed Systems Architect & Enterprise ERP Engineer">
  </picture>
</a>

<div align="center">
  <a href="https://usmanghias.co.uk"><img src="https://img.shields.io/badge/Official_Portfolio-714B67?style=for-the-badge&logo=googlechrome&logoColor=white" alt="View Portfolio"></a>
  <a href="https://www.linkedin.com/in/iusmanghias"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:iusmanghias@gmail.com?subject=Project%20enquiry%20for%20Usman%20Ghias"><img src="https://img.shields.io/badge/Discuss_a_Project-9333EA?style=for-the-badge&logo=gmail&logoColor=white" alt="Discuss a project by email"></a>
  <a href="https://github.com/UsmanGhias"><img src="https://komarev.com/ghpvc/?username=usmanghias&style=for-the-badge&color=38BDF8&labelColor=0B1120&label=PROFILE+VIEWS" alt="Profile Views"></a>
</div>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/proof-strip-dark.svg">
  <img src="assets/brand/proof-strip-light.svg" width="100%" alt="6+ years in production, 91+ Odoo implementations, 185+ projects delivered, 70+ clients, clients across 25+ countries, 4 production applications">
</picture>

# Usman Ghias

**Lead Distributed Systems Architect & Enterprise ERP Engineer**  
Founder & Principal Architect at [CODCrafters](https://codcrafters.org) · Remote Worldwide

I design enterprise ERP systems, transaction backends, and offline-first mobile products. Over the past 6 years, I have delivered 91+ Odoo builds and 185+ total projects across Europe, the Middle East, and North America, reducing query response times by over 60% on multi-million row PostgreSQL databases.

**Open to work now.** Odoo architect and senior backend roles, remote or in the GCC with sponsorship, available immediately. Also seeking PhD positions in distributed systems for the 2026/27 intake. [Email me](mailto:iusmanghias@gmail.com) or see [my portfolio](https://usmanghias.co.uk).

---

## What I architect

- **Enterprise ERP & Database Engines**: Odoo 15 to 19, Python ORM, PostgreSQL query profiling, PgBouncer pooling, OWL reactive components, and zero-bloat modular architecture.
- **Cryptographic Compliance**: ZATCA Phase 2 E-Invoicing engine for Saudi Arabia and GCC, implementing ECDSA secp256k1 signing, SHA-256 UBL 2.1 XML hashing, QR code TLV digests, and automated clearance API handshakes.
- **Distributed Product Engineering**: Offline-first mobile systems on Flutter (Riverpod, Hive, SQLite) syncing with Next.js web applications and REST APIs.
- **Lightweight DevOps**: Self-hosted developer infrastructure on Linux, Docker, Nginx, and cloud clusters.

---

## Enterprise systems: [CODCrafters](https://codcrafters.org)

<a href="https://codcrafters.org">
  <img src="assets/brand/codcrafters-enterprise-ecosystem.webp" width="100%" alt="CODCrafters: Enterprise Odoo, integrations, AI, mobile apps and the systems connected to them">
</a>

#### Automotive & parts distribution
- **Context**: European distributor managing multi-currency parts catalogues, workshop orders, dynamic pricing, and EU VAT rules across split processes.
- **Architecture**: Odoo 17/18 Enterprise with PostgreSQL and OWL. Designed 15+ custom modules for real-time carrier APIs and optimized ORM query paths.
- **Result**: Cut core report generation latency by 60%, delivering sub-second response times on heavy concurrent inventory lookups. [Automotive case study](https://www.codcrafters.org/industries/automotive)

#### Healthcare & hospital operations
- **Context**: Multi-department hospital running clinical records, billing, pharmacy stock, and insurance claims in disconnected tools.
- **Architecture**: Centralized Odoo HMS covering patient journeys, lab diagnostic workflows, pharmacy inventory, and automated billing.
- **Result**: Unified administrative and clinical operations into one database of record with role-based access control. [Healthcare case study](https://www.codcrafters.org/industries/healthcare)

#### ZATCA Phase 2 cryptographic e-invoicing
- **Context**: Saudi enterprise requiring automated, tamper-proof electronic invoice clearance under ZATCA Phase 2 mandate.
- **Architecture**: Native Python and Odoo cryptographic engine generating canonical XML UBL 2.1, ECDSA digital signatures, cryptographic invoice hashing, and TLV Base64 QR encoding.
- **Result**: 100% compliant real-time API clearance with ZATCA Fatoora portal without third-party recurring SaaS fees.

---

## Product engineering: CLIVORA

<img src="assets/work/clivora-product-ecosystem.webp" width="100%" alt="CLIVORA product ecosystem: Android application, web console, and connected workspace modules">

#### [CLIVORA](https://clivora.io): Offline-First Freelancer & Agency Workspace
Freelancers and agencies often juggle separate tools for CRM, tasks, timesheets, and invoicing. CLIVORA combines these into one synchronized workspace on Web and Android.
- **Role**: Founder and Principal Architect; designed full backend, database schemas, and mobile sync engine.
- **Architecture**: Flutter mobile client with offline-first local storage (Hive + SQLite) syncing with Next.js web console and REST endpoints.
- **Availability**: Live at [clivora.io](https://clivora.io) and published on [Google Play](https://play.google.com/store/apps/details?id=org.codcrafters.clivora).

---

## Experience & academic research

- **Founder & Principal Architect**, CODCrafters (2022 - present)  
  Directing enterprise ERP deliveries, performance audits, and custom software engineering for clients across 25+ countries.
- **Senior Odoo Spreadsheets & BI Specialist**, Plectar, Switzerland (2025 - present)  
  Multi-dimensional financial and operational modeling, OWL dashboard engineering, and legacy reporting migrations.
- **MS in Software Engineering**, Quantic School of Business and Technology, Washington D.C., USA  
  Graduating October 2026. Cumulative academic standing: **94.75%**, proctored comprehensive exam score: **92%**.
- **BS in Software Engineering (Distinction)**, PUCIT, Lahore  
  Appointed 3-time University Teaching Assistant for Data Science, Computer Networks, and Object-Oriented C++.
- **Research Preprint**: Zenodo DOI [10.5281/zenodo.22843765](https://doi.org/10.5281/zenodo.22843765)  
  Focus on low-latency microservice architecture and transaction routing in enterprise ERP systems.
- **Doctoral Research Focus**: Actively seeking prospective Ph.D. scholarships and doctoral supervisor alignment in Distributed Systems and High-Concurrency Database Engines for 2026/2027 intake.

---

## Distributed systems research

My research question comes from a production problem. A mobile ERP client goes offline for hours, keeps writing invoices, tasks and time entries across several related tables, and must reconcile with PostgreSQL later without silently losing or overwriting anyone's work. Last-write-wins loses data, and CRDTs are expensive on a low-end Android phone and awkward for relational rows.

**Durable Edge-Outbox Synchronization: Managing Relational Divergence in Intermittent Mobile Enterprise Workloads**  
Muhammad Usman Khan, Zenodo preprint, September 2026. [DOI 10.5281/zenodo.22843765](https://doi.org/10.5281/zenodo.22843765)

The paper formalises the sync layer of CLIVORA (240 Dart source files, 90,868 lines, Drift/SQLite at schema version 18):

- A durable transactional outbox. Every mutation gets a UUIDv4 idempotency key scoped to its owner and moves through a six-state automaton (pending, processing, retrying, conflicted, permanently_failed, completed) with exponential backoff capped at eight attempts.
- Cloud reconciliation over a per-user WebSocket channel against PostgreSQL under row-level security, with a 500 ms sliding debounce that collapses bursts of change events into one pass.
- Divergence is staged, never resolved silently. Conflicts land in `sync_conflict_entries` on the device and `crm_sync_conflicts` in PostgreSQL, with two deterministic operators, take-cloud and keep-local. Keep-local re-enqueues the local state as a new outbox operation, so every write to the cloud still goes through one authorised path.
- In a seeded microbenchmark of the outbox model (10 trials of 1,000 operations), ingestion through durable SQLite WAL commit averaged 25.1 ms (SD 2.8 ms, p99 31.3 ms), and storage shrank to 9.1% of peak after post-sync tombstone sweeps.

**Questions I want to work on in a PhD**

- Exactly-once effects across an edge SQLite replica and a server PostgreSQL database, when the network, the app process and the server can each fail mid-operation.
- Conflict detection that understands relational constraints (foreign keys, unique keys, ledger balance) instead of treating rows as independent documents.
- ERP ledgers as a testbed for consistency under partition: which accounting invariants can be kept locally, and which need coordination.

---

## Open-source engineering

<img src="assets/brand/open-source-flow.webp" width="100%" alt="Open Source Engineering: Contributing practical improvements to Python tooling, release automation, database integrations, and developer infrastructure">

<div align="center">
  <a href="https://github.com/UsmanGhias"><img src="https://img.shields.io/badge/Open_Source-Active_Contributions-9333EA?style=for-the-badge&logo=github&logoColor=white" alt="Open Source Contributions" /></a>
  <a href="https://github.com/UsmanGhias"><img src="https://img.shields.io/badge/Pull_Requests-Merged_&_Active-10B981?style=for-the-badge&logo=git&logoColor=white" alt="Pull Requests" /></a>
  <a href="https://github.com/UsmanGhias"><img src="https://img.shields.io/badge/Code_Reviews-Active_Maintainer-38BDF8?style=for-the-badge&logo=githubactions&logoColor=white" alt="Code Reviews" /></a>
</div>

<br/>

<div align="center">
  <a href="https://github.com/UsmanGhias">
    <img src="https://github-readme-streak-stats.herokuapp.com/?user=UsmanGhias&theme=tokyonight&hide_border=true&background=0B1120&stroke=30363D&ring=9333EA&fire=F5B800&currStreakNum=C084FC&sideNums=F0F6FC&sideLabels=9DA7B3&dates=5F6368" alt="Usman Ghias GitHub Streak Stats" />
  </a>
</div>

<br/>

**Selected Pull Requests & Contributions:**
- [zifter/clickhouse-migrations #105](https://github.com/zifter/clickhouse-migrations/pull/105): Migrated PyPI release workflow to Trusted Publishing (OIDC).
- [progovoy/vmn #173](https://github.com/progovoy/vmn/pull/173): Added `--base` option to `vmn show` command.
- [cubrid-lab/sqlalchemy-cubrid #455](https://github.com/cubrid-lab/sqlalchemy-cubrid/pull/455): Fixed dialect reflection error mapping for syntax errors.
- [ehtishammubarik/websieve #47](https://github.com/ehtishammubarik/websieve/pull/47): Preserved code block indentation during page sanitization.

**Merged upstream (2026):**
- [strelov1/freehire #3688](https://github.com/strelov1/freehire/pull/3688): Added Odoo, DuckDB, DeepSeek, DSPy, LiteLLM, SGLang and Mastra to the skills dictionary (3.3k-star job aggregator).
- [strelov1/freehire-mcp #11](https://github.com/strelov1/freehire-mcp/pull/11): Added `profile`, `contribute` and `my_contributions` tools to the MCP server for parity with the CLI.
- [cubrid-lab/sqlalchemy-cubrid #732](https://github.com/cubrid-lab/sqlalchemy-cubrid/pull/732): Removed the Python 3.10 `asyncio.TimeoutError` branch from `is_disconnect`.
- [00200200/repro-lens #55](https://github.com/00200200/repro-lens/pull/55) and [#100](https://github.com/00200200/repro-lens/pull/100): Reproducibility rules R118 (unseeded Polars sampling) and R127 (unseeded Hugging Face dataset shuffle).

**In review:** [SectorLabs/django-postgres-extra #299](https://github.com/SectorLabs/django-postgres-extra/pull/299): prune `index_together` in `PostgresModelState.render` for Django 5.1+.

---

## GitHub activity

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/UsmanGhias/UsmanGhias/output/github-stats-dark.svg">
  <img src="https://raw.githubusercontent.com/UsmanGhias/UsmanGhias/output/github-stats-light.svg" width="100%" alt="GitHub activity: contributions, commits, pull requests, public repositories, followers and most used languages">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/UsmanGhias/UsmanGhias/output/github-contribution-grid-snake-dark.svg">
  <img src="https://raw.githubusercontent.com/UsmanGhias/UsmanGhias/output/github-contribution-grid-snake.svg" width="100%" alt="Contribution graph animation">
</picture>

---

## Technical stack

| Domain | Technologies |
| :--- | :--- |
| **ERP & Databases** | Odoo 15 to 19 · Python ORM · PostgreSQL · PgBouncer · Redis · SQLite · Hive |
| **Web & Mobile** | TypeScript · Next.js · React · Flutter · Riverpod · FastAPI · TailwindCSS |
| **Compliance & APIs** | ZATCA Phase 2 (ECDSA, UBL 2.1, QR TLV) · REST · GraphQL · XML-RPC / JSON-RPC |
| **DevOps & Cloud** | Linux · Docker · Nginx · Odoo.sh · AWS · GitHub Actions · Self-Hosted Clusters |

---

## Contact & inquiries

Building a new platform, modernizing an ERP instance, or discussing doctoral research?

[Official Portfolio](https://usmanghias.co.uk) · [Email Inquiry](mailto:iusmanghias@gmail.com) · [LinkedIn](https://www.linkedin.com/in/iusmanghias) · [CODCrafters](https://codcrafters.org) · [Upwork](https://www.upwork.com/freelancers/usmanghias) · [WhatsApp](https://wa.me/923126912440)
