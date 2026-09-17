from pathlib import Path
from docx import Document
from docx.shared import Pt
from shutil import copy2, move

root=Path('/Users/gravitycodez/Desktop/Project managment')
package=root/'C1_ClassMic'
backup=root/'.c1_build/before_separate_inputs'
backup.mkdir(exist_ok=True)
charter=package/'02_Group_Charter/ClassMic_C1_Project_Charter.docx'
if not (backup/charter.name).exists(): copy2(charter,backup/charter.name)
d=Document(charter)
old='3. Complete each student’s individual input and attach genuine photos of the team’s charter brainstorming, with dates, participants and decisions. Use the separate input forms and Human Evidence document in this package.'
new='3. Attach genuine photos of the team’s charter brainstorming, with dates, participants and decisions, using the Human Evidence document. Individual student input is handled separately.'
matches=[p for p in d.paragraphs if p.text==old]
assert len(matches)==1
matches[0].text=new
for r in matches[0].runs:r.font.size=Pt(10.5)
d.save(charter)
individual=package/'01_Individual_Inputs'
if individual.exists(): move(str(individual),str(backup/'01_Individual_Inputs'))
readme=package/'START_HERE.txt'
if not (backup/readme.name).exists(): copy2(readme,backup/readme.name)
readme.write_text('''C1 — Develop the Project Charter
ClassMic draft package

CONTENTS
02_Group_Charter: The two-page draft charter and items requiring confirmation.
03_Slides: Three slides for a team presentation.
04_Human_Evidence: A form for genuine brainstorming images and discussion captions.

Individual student submissions are handled separately, as requested. Blank individual-input forms are omitted from this ZIP.

BEFORE UPLOADING
1. Add genuine photos of the team discussing the charter and complete their captions.
2. Link and reconcile the approved ClassMic A2 aspiration and B2 business case. Their repository location is awaiting clarification. The Phase B document currently visible in this workspace describes CampusCrew, a different project.
3. Confirm the draft charter’s appointments, budget, timing, room availability and success measures. Resolve or retain explicitly labeled confirmation items as instructed by your course.
4. Update the three slides if the agreed charter changes, then re-create the ZIP.

The original ClassMic charter supplies the proposed scope, objectives, roles, 14-week schedule, three-classroom pilot and AED 60,000 ceiling. These remain draft information until reconciled with the approved project sources. No approval signatures or missing business-case results have been invented.

LAB READING AS PROVIDED IN THE C1 INSTRUCTIONS
Chapter 5, “AI-Assisted Project Initiation,” pages 147–155.
Chapter 2, selected stakeholder sections, pages 37–53.

SUBMISSION LIMITS
Keep the group charter within two pages and the presentation within three slides. The ZIP includes the group files and a human-evidence form. Individual submissions are handled separately.
''')
print('Updated charter and package guide; moved individual-input forms to the private backup.')
