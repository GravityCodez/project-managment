# Repository setup and maintenance

/init is completed by the repository-level AGENTS.md, with human onboarding in CONTRIBUTING.md. Codex loads repository instructions from AGENTS.md; the implementation follows the [official custom-instruction guidance](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Identity and project decisions live in separate shared records so a new collaborator does not inherit assumptions about who is speaking.

The repository is an artifact workspace. No server, database, production application or package installation is required to browse its contents.

## Authoring helpers

| Helper | Purpose | Dependencies |
| --- | --- | --- |
| scripts/build_lab_schedule.py | Produce schedule XML, CSV and a readable PDF | Python, reportlab |
| scripts/refresh_initial_documents.py | Rebuild the cleaned A–C documents from the preserved source copies | Python, python-docx |
| scripts/refresh_initial_slides.mjs | Refresh A–C decks without changing their design | Managed Node runtime, artifact-tool and presentation skill helpers |
| scripts/sanitize_metadata.py | Remove irrelevant Office/PDF authoring metadata | Python, lxml, pypdf |
| scripts/check_submissions.py | Verify direct files and ZIP contents | Python, pypdf for required PDF checks |
| scripts/package_submissions.py | Create ZIPs from explicit allowlists and record hashes | Python standard library |

Use the available managed document runtime. If dependencies need installing, pin eligible releases and apply the repo's minimum 48-hour release age. A native cutoff such as uv's exclude-newer setting must cover transitive dependencies too. Keep environments and caches in .build/.

The date-specific document refresh helpers intentionally use the preserved September 10 source set. For a later content revision, update the authoring inputs deliberately; do not repeatedly run them over newer work. The schedule builder replaces XML/CSV/PDF but cannot update MPP. After changing the schedule, import the new XML in Project Plan 365, save the MPP and reopen it before rebuilding the ZIP.

Render documents and slides, inspect them visually, sanitize metadata, run the release checker, package, then check the packages again. Keep rendering receipts and temporary exports outside submissions/. A new presentation helper run creates a fresh staging directory to avoid overwriting finalization receipts.
