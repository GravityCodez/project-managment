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

The user accepted the Intel build for this release after the separate installation task could not obtain an Apple-silicon version. Version 25.7.1280 completed the final native save/reopen checks. Do not repeat installation as a prerequisite for editing this schedule. Running through Rosetta does not make the app native to Apple silicon. The user can consider a compatible vendor release later.

The course guide describes About > Enter Key activation. Do not put its institutional key into documentation, source code, logs, screenshots or commits. The guide is retained locally and ignored by Git. An account login is different from product-key activation. The user asked to defer login; later said “done”; only claim app capabilities demonstrated by actual open/save operations.

For native macOS file dialogs, open Go to Folder, wait for the field, then type the path. A premature paste or long path immediately after the shortcut may lose its first characters. Re-read the UI before continuing. The native app's task grid has little accessibility text; use screenshots and column-header context menus such as Best Fit.

The authoring helpers resolve the repo root from their own file location. Use managed runtime dependencies. Presentation helpers accept NODE_MODULES_DIR, RUNTIME_NODE_MODULES, RUNTIME_NODE, RUNTIME_PYTHON and PRESENTATIONS_SKILL_DIR. Put each finalization receipt outside the export directory and use a new staging path for a new revision. Inspect every changed page and slide; automated checks do not replace visual QA.

## Recovery and finishing future work

Earlier coursework and ZIPs are preserved in archive/. Bulky old build caches are in ignored .local-archive/; the original Git commit 0b765f6 also contains them. Use docs/original-file-manifest.json to verify preservation. Do not rewrite shared history as routine cleanup.

For a new assignment: confirm its live requirements and due date, select the right inputs, make the artifact self-contained, check assumptions, render and inspect, sanitize irrelevant metadata, run scripts/check_submissions.py, and package an explicit allowlist. Record the release in STATUS.md and CHANGELOG.md. Submission, grading, acceptance and local readiness are distinct states. Do not upload to LMS, send messages or invite collaborators without authorization.

## Final release and delivery

The lab package is complete at submissions/ClassMic_WBS_Lab.zip. It contains exactly the MPP, PDF, XML and CSV. A–C is complete at submissions/ClassMic_Initial_Phases.zip. All direct deliverables and both ZIPs passed the release checker. The native schedule reopened successfully after save and after restarting the app. Read DELIVERY.md for GitHub publication and Telegram delivery verification; do not confuse a review request with approval or an LMS submission.

The professor’s latest reminder requires Computer and/or AI resources on the sprint packages. Both Computer and AI tools are assigned to E.1 and E.2 alongside Temiko and Nurtore. They are cost resources using existing equipment/access, with no added student hours. Existing duration and effort estimates are allowed even though the lab does not assess them. Keep these required resource labels in the submission.

The final XML uses a minimal cost-resource representation that this app imports. An earlier variant with extra optional cost/group fields triggered an input-format exception. Use the current builder and verify any future XML changes by opening them in the native app. The generator does not write MPP: after a schedule edit, import the XML, save the MPP, close and reopen it, then repackage. Keep the four released formats synchronized.

The user authorized the GitHub push and one Telegram delivery to Lourinser (@realnurtore) asking for review. This does not authorize a course submission, further messages, public posting elsewhere or invitations. Keep the institutional license guide and raw tutorial media local. The completed cleanup branch is approach/repo-cleanup-wbs-lab; check the remote and current worktree before future changes.
