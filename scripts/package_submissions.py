"""Package explicit coursework allowlists; internal docs never enter release ZIPs."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
import hashlib,json
ROOT=Path(__file__).resolve().parents[1]
S=ROOT/'submissions'
initial=[]
for folder,stem,key in [('A_Aspiration','ClassMic_A2_Aspiration','A2'),('B_Business_Case','ClassMic_B2_Business_Case','B2'),('C_Charter','ClassMic_C1_Project_Charter','C1')]:
 initial += [S/'initial-phases'/folder/(stem+ext) for ext in ['.docx','.pdf']]
 initial += [S/'initial-phases'/folder/f'ClassMic_{key}_Three_Slides.pptx']
lab=[S/'lab-2026-09-17'/('ClassMic_WBS_and_Schedule'+ext) for ext in ['.mpp','.pdf','.xml','.csv']]
for dest,files,base in [(S/'ClassMic_Initial_Phases.zip',initial,S/'initial-phases'),(S/'ClassMic_WBS_Lab.zip',lab,S/'lab-2026-09-17')]:
 for f in files:
  if not f.is_file():raise FileNotFoundError(f)
 with ZipFile(dest,'w',ZIP_DEFLATED) as z:
  for f in files:z.write(f,f.relative_to(base))
 with ZipFile(dest) as z:
  assert z.testzip() is None
  for f in files:assert z.read(str(f.relative_to(base)))==f.read_bytes()
 print(dest.name,len(files),'coursework files')
manifest=[]
for f in sorted(S.rglob('*')):
 if f.is_file():manifest.append({'path':str(f.relative_to(ROOT)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
(ROOT/'docs/release-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
