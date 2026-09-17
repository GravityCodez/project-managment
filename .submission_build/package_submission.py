from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib
import shutil

ROOT = Path('/Users/gravitycodez/Desktop/Project managment')
OUT = ROOT / 'ClassMic_Submission'

start = '''# ClassMic revised A–D package

Prepared 10 September 2026 for Temiko Machavariani and Nurtore Arynuruly, BUS 2010.

The documents use one proposed scope: a ClassMic browser prototype developed in two weekly sprints, followed by evaluation and a recommendation. The earlier 14-week classroom pilot remains a possible later project. This scope change, the proposed roles, 100 student hours and conditional AED 0 incremental cash estimate still need team and instructor confirmation.

## Files

| Folder | Contents |
| --- | --- |
| A_Aspiration | Revised A2 aspiration: two-page Word document and PDF; three editable slides. |
| B_Business_Case | Revised B2 business case: four-page Word document and PDF; three editable slides. |
| C_Charter | C1 draft charter: two-page Word document and PDF; three editable slides. |
| D_Develop_Plans | Integrated D1–D7 plan; Notion PRD text and requirements import table; schedule table. |
| Supporting_Notes | Source record, evidence status and decisions requiring confirmation. |

The PDF copies have the same content as the Word documents. The slides are editable PowerPoint files. D1 occupies one page, D2 occupies two, the WBS has 18 elements, and both risk registers contain six threats followed by two opportunities.

## Which ZIP to use

- ClassMic_C1_Submission.zip contains the C1 charter, its three-slide deck and the revised A2/B2 Word documents as supporting inputs. Review its evidence note before uploading.
- ClassMic_A_to_D_Package.zip contains the full working set. It is a master package for separate phase submissions; do not treat all nine slides as one C1 deck.

Individual student inputs are handled separately at the team's request. They have not been recreated or included. Earlier drafts are preserved in the workspace archive.

## Before submission

1. Confirm the course-prototype scope, team roles and any actual A2/B2/charter approval. The files deliberately retain draft status where approval is unknown.
2. Add the required genuine charter brainstorming images, or confirm that the instructor accepts the material already submitted separately. The individual SMART note does not establish that a group charter discussion took place.
3. For D, add the team's original WBS/network images and communication brainstorming. Add actual stakeholder feedback when available; proposed requirements are not presented as validated interviews or survey findings.
4. Import ClassMic_Notion_PRD.md and ClassMic_Notion_Requirements.csv into the team's Notion page, check the eight required database fields, and add the page link to D2. No Notion page has been created by this revision.
5. The D3 schedule includes dates, dependencies and a Word Gantt view. ClassMic_Schedule.csv is editable supporting data. The current brief asks for a Gantt chart from MS Project as an input; that source artifact is still needed or its format must be accepted by the instructor.
6. Confirm the proposed early D review by 19 September and sprint dates of 20–26 September and 27 September–3 October. Starting after the published D deadline would not leave two full weeks before E is due.

The fuller decision list is in Supporting_Notes/Evidence_and_Confirmations.md. Nothing in this package records completed tests, purchased resources or approvals that were not supplied.

## LMS requirements checked

The visible [C1 assignment](https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38960) requests a draft charter of at most two pages and at most three slides. Its displayed deadline was 9 September 2026 at 00:00. It was unsubmitted when checked.

The [D assignment](https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38962) is due 22 September at 00:00. Its current D Phase Labs attachment takes precedence over the older generic planning brief for this revision. [E](https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38965) opens 26 September and is due 4 October at 00:00; [F](https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38968) is due 10 October at 00:00. Dates are recorded as displayed in the LMS on 10 September 2026.

No LMS upload or resubmission has been performed.
'''
(OUT / 'START_HERE.md').write_text(start)

evidence_path = OUT / 'Supporting_Notes/Evidence_and_Confirmations.md'
evidence = evidence_path.read_text()
needle = '- Notion page link and access. The PRD and database content are prepared for import but are not hosted in Notion yet.'
replacement = needle + '\n- The D3 brief asks for a Gantt chart from MS Project as an input. The package supplies an editable schedule CSV and a Word Gantt view; an MS Project source artifact or instructor acceptance of this format remains open.'
assert needle in evidence
if 'an MS Project source artifact' not in evidence:
    evidence = evidence.replace(needle, replacement)
evidence_path.write_text(evidence)

for letter, folder, stem in [
    ('A', 'A_Aspiration', 'ClassMic_A2_Aspiration'),
    ('B', 'B_Business_Case', 'ClassMic_B2_Business_Case'),
    ('C', 'C_Charter', 'ClassMic_C1_Project_Charter'),
    ('D', 'D_Develop_Plans', 'ClassMic_D_Integrated_Plan'),
]:
    shutil.copy2(ROOT / '.submission_build' / f'render_{letter}' / f'{stem}.pdf', OUT / folder / f'{stem}.pdf')

c1_note = '''CLASSMIC C1 — READ BEFORE UPLOAD

The charter is two pages. The presentation contains three slides.
The PDF and Word charter contain the same material; the Word file is editable.
Supporting_A2_B2 contains the rewritten ClassMic aspiration and business case.

This is a draft awaiting review of the revised course-prototype scope and the
items listed under “Items requiring confirmation” in the charter. It does not
claim approval of the revised A2 or B2.

Individual student inputs are handled separately at the team's request and
are excluded from this ZIP. Genuine team charter-brainstorming images have
not been supplied for this revision. Add them, or confirm that the instructor
accepts the evidence already submitted separately.

No LMS upload has been performed.
'''

full_zip = ROOT / 'ClassMic_A_to_D_Package.zip'
with ZipFile(full_zip, 'w', ZIP_DEFLATED) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and not p.name.startswith('.'):
            z.write(p, p.relative_to(ROOT))

c1_zip = ROOT / 'ClassMic_C1_Submission.zip'
c1_files = {
    'C_Charter/ClassMic_C1_Project_Charter.docx': 'ClassMic_C1/ClassMic_C1_Project_Charter.docx',
    'C_Charter/ClassMic_C1_Project_Charter.pdf': 'ClassMic_C1/ClassMic_C1_Project_Charter.pdf',
    'C_Charter/ClassMic_C1_Three_Slides.pptx': 'ClassMic_C1/ClassMic_C1_Three_Slides.pptx',
    'A_Aspiration/ClassMic_A2_Aspiration.docx': 'ClassMic_C1/Supporting_A2_B2/ClassMic_A2_Aspiration.docx',
    'B_Business_Case/ClassMic_B2_Business_Case.docx': 'ClassMic_C1/Supporting_A2_B2/ClassMic_B2_Business_Case.docx',
}
with ZipFile(c1_zip, 'w', ZIP_DEFLATED) as z:
    for source, target in c1_files.items():
        z.write(OUT / source, target)
    z.writestr('ClassMic_C1/READ_BEFORE_UPLOAD.txt', c1_note)

for zpath in (full_zip, c1_zip):
    with ZipFile(zpath) as z:
        assert z.testzip() is None
        assert len(z.namelist()) == len(set(z.namelist()))
        assert not any('/.' in name or '__MACOSX' in name for name in z.namelist())
        print(zpath.name, len(z.namelist()), 'files;', zpath.stat().st_size, 'bytes')

with ZipFile(full_zip) as z:
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and not p.name.startswith('.'):
            assert hashlib.sha256(z.read(str(p.relative_to(ROOT)))).digest() == hashlib.sha256(p.read_bytes()).digest()
with ZipFile(c1_zip) as z:
    for source, target in c1_files.items():
        assert z.read(target) == (OUT / source).read_bytes()

archive = ROOT / '_Archive/Before_ClassMic_Revision_2026-09-10'
archive.mkdir(parents=True, exist_ok=True)
for name in [
    'CampusCrew_Phase_B_Business_Case.docx',
    'ClassMic_Phase_C_Project_Charter.docx',
    'ClassMic_Phase_D_Integrated_Project_Plan.docx',
    'ClassMic_C1_Draft_Submission.zip',
    'C1_ClassMic',
]:
    source = ROOT / name
    target = archive / name
    if source.exists():
        assert not target.exists(), f'Archive target already exists: {target}'
        shutil.move(str(source), str(target))

(archive / 'README.txt').write_text(
    'Earlier files preserved for reference on 10 September 2026.\n'
    'Use ClassMic_Submission and the new ZIP packages in the workspace root for the revised work.\n'
    'The originals have not been edited; they are archived to prevent accidental submission.\n'
)
print('ZIP integrity and file matches verified. Earlier files archived.')
