# Repository working agreements

## Start here
Read README.md, docs/STATUS.md, docs/TEAM.md, docs/DECISIONS.md, docs/DEADLINES.md, and docs/AGENT_HANDOFF.md before substantive work. This repository contains the ClassMic BUS 2010 coursework, not a deployed application. Follow the current task's phase boundary. Do not complete later course phases merely because drafts exist.

## Submission content
All files under submissions/ and every upload package must stand alone as coursework for the instructor. Include only the requested academic content and the team's names. Keep setup instructions, repository paths and links, cross-references to internal documents, chat history, drafting commentary, checklists, missing-input reminders, validation reports, prompts, and assistant/tool boilerplate out of submitted files, speaker notes, comments, metadata, filenames, and ZIP contents.

Do not add unsolicited AI labels. Required Computer/AI resource names in the WBS are coursework content and must remain. Retain disclosures and attribution explicitly required by the assignment, course, or source license. Never fabricate human brainstorming, signatures, approval, interviews, tests, results, or teammate agreement, and never claim sole human authorship. Keep real assumptions and limitations where they affect the project's conclusions. Record preparation issues and evidence gaps separately in docs/STATUS.md.

Use direct sentences and specific task names. Remove filler, duplicated claims and commentary about drafting. Keep assumptions beside the decisions they affect rather than repeating them in every row. Check stale previews, generic export labels and slide-count metadata as well as visible text. A keyword scan does not replace reading the finished work.

Before release, run scripts/check_submissions.py, visually inspect every changed Word/PDF page and slide, and inspect ZIP members. A text scan alone does not prove clean layout. Use an explicit file allowlist for packages; never zip the repository or a working folder wholesale.

## Organization
- submissions/: current coursework only, separated by assignment.
- working/: unfinished future-phase material; never upload as a final package.
- references/: original course and team sources. Preserve originals; do not invent replacement evidence.
- docs/: collaboration, decisions, deadlines, indexes and validation records. Never include in submissions.
- scripts/: portable authoring and verification helpers.
- archive/: dated historical artifacts; never treat as current or submit them.
- .build/ and .local-archive/: ignored local renders, caches and bulky build history.

Use stable descriptive filenames and repo-relative paths in scripts. Resolve the repo root from the script location. Never hard-code a collaborator's home directory, Python executable or runtime symlink. Archive superseded coursework before replacement and record changes in docs/CHANGELOG.md. Do not rewrite Git history or delete original evidence during routine cleanup.

## Collaboration and recurring decisions
Temiko Machavariani and Nurtore Arynuruly are the confirmed team names. Do not assume every collaborator is Temiko. Ask identity only when attribution or authorization requires it. Preserve the distinction between confirmed identity, selected planning roles, actual agreement, and instructor approval. Consult docs/TEAM.md and docs/DECISIONS.md; record important new facts there with date, source, status and any superseded decision.

Use approach/<short-topic> branches for new work. Coordinate before editing binary documents. Keep each assignment's editable source and its export synchronized. Do not change another person's Git identity, invite collaborators, submit coursework, or message others unless the user authorizes that action. Before publishing course materials, check their sharing permissions. Do not commit license keys, credentials, login state, or personal runtime paths.

## Dependency update safety buffer
For third-party package installations and dependency upgrades, use only releases publicly available for at least 48 hours. Configure the package manager's native minimum-release-age or cooldown setting when available; otherwise verify the release timestamp and select the newest eligible version. Preserve stricter policies. Codex itself is exempt.

## Evidence and verification
Check LMS deadlines live when time-sensitive. Record the display time and timezone; 00:00 means the start of the displayed day. Submitted is different from approved or graded. Document uncertainty rather than guessing. Opening an XML in a native scheduling application and checking dates/dependencies is required before claiming native interoperability. Do not mark planned future tasks complete.
