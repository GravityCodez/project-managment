# Working together

Clone `https://github.com/GravityCodez/project-managment.git`, open the folder, and read AGENTS.md and docs/STATUS.md. Set your own Git name and email in your clone; do not copy another teammate's identity. No application installation is needed to read the repository.

Start a branch named `approach/<short-topic>`. State which assignment and files you are taking in the team's coordination channel. Word, PowerPoint and Project files do not merge safely as text, so have one editor per artifact at a time. Pull the latest changes before starting. Review changes together before merging.

Edit the relevant coursework in submissions/ or unfinished work in working/. Archive the preceding release before replacing it. When using a builder, change its inputs as well as its outputs. Update docs/STATUS.md and docs/CHANGELOG.md, and add enduring decisions to docs/DECISIONS.md. Keep evidence and approvals accurate.

Run `python3 scripts/check_submissions.py` and inspect all changed pages/slides visually. Authoring helpers may require python-docx, lxml, pypdf, reportlab or an Office-compatible renderer; use an available managed runtime and follow the 48-hour dependency policy rather than installing unpinned current releases. Generated QA files belong in .build/.

Only package explicit coursework files. Keep documentation, license information, personal paths, build logs and preparation notes out of packages. One teammate uploads the reviewed release and records the exact LMS status and date. Do not assume a committed file has been submitted or accepted.

The instructor's source materials may carry sharing restrictions. The software installation guide is local-only because it contains an institutional key; an authorized teammate can obtain it from the course LMS. Repository invitations and access changes require an explicit request with the teammate's account.
