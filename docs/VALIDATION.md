# Verification record

Completed 17 September 2026, including the final [editorial review](EDITORIAL_REVIEW.md), professor’s resource reminder and refreshed native MPP.

## Preservation and repository organization

All 278 original regular files in the pre-cleanup inventory were located at their archived or reference destinations and matched their original SHA-256 hashes byte for byte. See archive-preservation.json. Two old runtime dependency symlinks remain only within the ignored historical build folders. No shared history was rewritten and no original student evidence was altered.

The institutional installer guide, which contains a product key, is excluded by .gitignore. Build output, downloaded video, transcript, Whisper environment and model cache are also ignored. Current submission packages use explicit allowlists and contain no internal Markdown documentation, scripts, manifests or checklists.

## Refreshed initial phases

A2 is 2 pages; B2 is 4 pages; C1 is 2 pages. Each has a matching PDF and an editable deck of exactly 3 slides. Every document page and all 9 slides were rendered and visually inspected. The decks retain their existing design and editable tables. The presentation package, slide-count, heading-fit, geometry and import checks passed. The imported reference fonts emitted decoder warnings; final rendered text was readable with no clipped or overlapping content. No PowerPoint application check is claimed.

The content pass removed preparation checklists, references to other internal documents and stale dates. Office and PDF metadata was cleaned. Real project assumptions, limitations and legitimate external academic citations remain. Required missing human evidence is recorded in STATUS.md rather than fabricated or embedded as preparation instructions in the coursework.

## WBS lab

The XML and CSV contain 19 elements: one project root, six summaries and twelve leaf work packages. There are eleven finish-to-start links, all with zero lag. Every leaf except the first has one predecessor; all are reachable, ordered and connected across phase boundaries. Summary tasks have no duplicate predecessor links.

Arithmetic checks confirm 54 estimated hours for Temiko, 46 for Nurtore and 100 total. The seven-day calendar has eight scheduling hours per day, distinct from assigned effort. Both execution sprints span seven consecutive calendar days. The second ends October 2; the last project package ends October 9. All completion percentages remain zero because this is a proposed baseline, not a claimed execution record.

Project Plan 365 25.7.1280 imported the final XML without an error, displayed the ClassMic root and ABCDEF hierarchy, and saved the native MPP. The saved MPP was closed and reopened from disk; the hierarchy, both seven-day sprints and four assigned resources per sprint were retained. The native file also reopened after restarting the app. This establishes native Project Plan 365 open/save/reopen behavior. Microsoft Project itself was not run.

Computer and AI tools are non-labour cost resources allocated to E.1 and E.2, with zero additional cash cost under the existing-access assumption. Their assignments do not inflate the 100 student hours. An XML variant with optional cost/group fields failed to import; the minimal resource encoding imported successfully. The generator’s final XML was structurally identical to the imported source.

The standalone two-page PDF was rendered and inspected after the final resource update. It contains the names, hierarchy, Gantt view, dates, predecessor IDs, effort allocation and schedule assumptions. It is a readable report of the schedule, not a simulated application screenshot. The approved native MPP, PDF and complete ZIP were later submitted on LMS by 22:55 Dubai; see lab-submission-receipt.json.

## Release checks

scripts/check_submissions.py checks all direct deliverables and each ZIP member. It scans Office text, notes and metadata; external file relationships; comments and tracked changes; PDF text and page counts; deck slide counts; XML/CSV content; MPP container, identity and required-resource markers; XML sprint assignments and durations; CSV sprint resource names; package integrity; and prohibited internal filenames/content. These checks supplement visual review and native open/save/reopen verification, and do not certify academic approval or exhaustively parse the MPP binary format.

The package builder confirms every ZIP member matches its source byte for byte. release-manifest.json records final hashes. The initial-phase ZIP has 9 files; the lab ZIP has 4 files.

The tutorial was transcribed locally with faster-whisper 1.2.1 using base.en and CPU int8. All new package releases were restricted by uv's native exclude-newer cutoff to September 15, 2026 at 00:00 UTC, more than 48 hours before installation. The local transcript informed the project-root hierarchy and the use of ClassMic instead of the demonstration name Pluto.

Git attributes disable text normalization for archive/reference originals and CSV deliverables so their checked-in bytes retain the recorded hashes across clones. Internal documentation links and authoring-helper syntax were also checked.

Final publication checks confirmed that tracked files exclude candidate key strings from the local institutional guide, release hashes match every current file, internal documentation links resolve, authoring helpers parse, and no runtime symlinks or files over 50 MB remain in the tracked working tree. Delivery results are in DELIVERY.md.

The submitted source files were checked against the unchanged approved ZIP before upload. LMS subsequently showed all three filenames (MPP, PDF and ZIP), Submitted for grading, Not graded, and submission 1 hour 4 minutes early. No remote-byte hash comparison is claimed; recorded hashes are for the selected local source files. The scheduled monitor is paused.
