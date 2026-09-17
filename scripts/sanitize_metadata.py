"""Remove irrelevant authoring metadata without changing coursework content."""
from pathlib import Path
from zipfile import ZipFile,ZIP_DEFLATED
from lxml import etree
from pypdf import PdfReader,PdfWriter
import io
ROOT=Path(__file__).resolve().parents[1]
TEAM='Temiko Machavariani and Nurtore Arynuruly'
for p in (ROOT/'submissions').rglob('*'):
 if p.suffix in {'.docx','.pptx'}:
  with ZipFile(p) as z:entries={n:z.read(n) for n in z.namelist()}
  for n in ['docProps/core.xml','docProps/app.xml']:
   if n not in entries:continue
   root=etree.fromstring(entries[n])
   for el in root:
    name=etree.QName(el).localname
    if name=='creator':el.text=TEAM
    if name in {'lastModifiedBy','Application','AppVersion','Company','Manager','Template','TotalTime','revision','description','keywords','category'}:el.text=''
   entries[n]=etree.tostring(root,xml_declaration=True,encoding='UTF-8',standalone=True)
  with ZipFile(p,'w',ZIP_DEFLATED) as z:
   for n,data in entries.items():z.writestr(n,data)
 elif p.suffix=='.pdf':
  r=PdfReader(p);w=PdfWriter();w.clone_document_from_reader(r)
  w.metadata=None;w.add_metadata({'/Title':r.metadata.get('/Title',p.stem.replace('_',' ')),'/Author':TEAM})
  buffer=io.BytesIO();w.write(buffer);p.write_bytes(buffer.getvalue())
print('Sanitized Office/PDF authoring metadata in submissions only.')
