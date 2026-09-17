# Agent and teammate handoff

Read AGENTS.md first, then STATUS.md, TEAM.md, DECISIONS.md and DEADLINES.md. The current user asked for repo cleanup, refreshed early phases and only the September 17 WBS/schedule lab among upcoming assignments. Do not expand this into completing D, E or F without a new request.

## What to use

Use submissions/ for current coursework and docs/INDEX.md for navigation. The final lab should include the native MPP schedule, matching XML, readable PDF and a CSV table. A–C live under submissions/initial-phases/. All internal instructions, verification, provenance and outstanding evidence belong in docs/, never in submission content or speaker notes.

The confirmed team is Temiko Machavariani and Nurtore Arynuruly. Roles and the 54/46-hour split are planning assignments, not independently confirmed commitments from Nurtore. Do not repeatedly ask Temiko's identity or invent another teammate. A new collaborator may be Nurtore; identify the person only when attribution or authorization matters.

## Critical context

C1 is already Submitted for grading on LMS; this was reconfirmed September 17. An older internal README falsely said it was unsubmitted. B is also submitted, but prior context records its upload as CampusCrew. Local refreshed A–C files are not a resubmission or course approval.

The lab is due September 18 at 00:00, which means the evening of September 17. D is due September 22 at 00:00. The newly visible final product report is due October 3 at 00:00, before E's October 4 cutoff. The revised proposal puts plan review on September 18 and the two sprints on September 19–25 and September 26–October 2. The old D drafts still use earlier dates and require reconciliation before release.

Temiko's original SMART photograph is in references/team/. Nurtore's individual input was reportedly submitted separately. Genuine group charter discussion photos, a hand-drawn WBS/network and pre-prompt communication notes remain unverified; do not generate fake evidence or silently claim those requirements are met. Notion was reportedly set up, but no project URL is recorded.

## Files and tooling

The September 17 native-file verification used Project Plan 365 25.7.1280, an Intel-only build running through Rosetta. Its official BU installer was published February 4, 2025, comfortably outside the 48-hour release buffer, and passed Apple signature/notarization verification outside the sandbox. Sandbox signature checks initially returned a false failure because trust services were unavailable. Never disable security checks to work around that.

The user later reported Apple’s Intel-app compatibility warning and assigned another agent to reinstall and activate a compatible version. Installation was still in progress when this editorial review began. Do not assume 25.7.1280 remains installed. Check architecture separately from signature and successful launch: running under Rosetta does not make an app native to Apple silicon. [Apple recommends an Apple-silicon or Universal build for future compatibility](https://support.apple.com/en-us/102527).

The course guide describes About > Enter Key activation. Do not put its institutional key into documentation, source code, logs, screenshots or commits. The guide is retained locally and ignored by Git. An account login is different from product-key activation. The user asked to defer login; later said “done”; only claim app capabilities demonstrated by actual open/save operations.

For native macOS file dialogs, open Go to Folder, wait for the field, then type the path. A premature paste or long path immediately after the shortcut may lose its first characters. Re-read the UI before continuing. The native app's task grid has little accessibility text; use screenshots and column-header context menus such as Best Fit.

The authoring helpers resolve the repo root from their own file location. Use managed runtime dependencies. Presentation helpers accept NODE_MODULES_DIR, RUNTIME_NODE_MODULES, RUNTIME_NODE, RUNTIME_PYTHON and PRESENTATIONS_SKILL_DIR. Put each finalization receipt outside the export directory and use a new staging path for a new revision. Inspect every changed page and slide; automated checks do not replace visual QA.

## Recovery and finishing future work

Earlier coursework and ZIPs are preserved in archive/. Bulky old build caches are in ignored .local-archive/; the original Git commit 0b765f6 also contains them. Use docs/original-file-manifest.json to verify preservation. Do not rewrite shared history as routine cleanup.

For a new assignment: confirm its live requirements and due date, select the right inputs, make the artifact self-contained, check assumptions, render and inspect, sanitize irrelevant metadata, run scripts/check_submissions.py, and package an explicit allowlist. Record the release in STATUS.md and CHANGELOG.md. Submission, grading, acceptance and local readiness are distinct states. Do not upload to LMS, send messages or invite collaborators without authorization.

## Git handoff

This work is on `approach/repo-cleanup-wbs-lab`. It is prepared as a local collaboration branch; no remote push is part of this task. Review the current branch and its release manifest before publishing. The default remote main branch still contains the previous structure until this branch is published and merged. Keep the institutional license guide and raw tutorial media out of remote commits.

## Pending final save after editorial review

The user twice confirmed that the separate installation task was still running. Do not interrupt that task. The cleaned A–C bundle is complete. The edited lab source is preserved in working/lab-review/ so another collaborator can finish without a local cache.

Once Project Plan 365 is ready, open working/lab-review/ClassMic_WBS_and_Schedule.xml. Confirm the 19 rows and two seven-day sprints, then save to submissions/lab-2026-09-17/ClassMic_WBS_and_Schedule.mpp. Close and reopen the MPP. Copy the matching XML, CSV and PDF from working/lab-review/ into submissions/lab-2026-09-17/. Run the metadata cleaner, package with --only lab, and run the complete submission checker. Finally remove the pending status from STATUS.md and EDITORIAL_REVIEW.md.

The earlier lab ZIP and its four source files remain mutually consistent while this save is pending. The stricter checker flags their old repetitive schedule note, which the new XML replaces with task-specific content. Do not weaken that check to call the older MPP reviewed.
