"""Clean release metadata and stale previews without changing coursework text."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from lxml import etree
from pypdf import PdfReader, PdfWriter
import argparse, io, re

ROOT = Path(__file__).resolve().parents[1]
TEAM = 'Temiko Machavariani and Nurtore Arynuruly'
TITLE = {'A2':'ClassMic Aspiration','B2':'ClassMic Business Case','C1':'ClassMic Project Charter'}


def clean_office(path):
    with ZipFile(path) as z:
        entries = {name: z.read(name) for name in z.namelist()}
    # Generic Word-template thumbnails are not previews of the actual coursework.
    thumbnails = {name for name in entries if name.startswith('docProps/thumbnail.')}
    for name in thumbnails:
        del entries[name]
    for name in ['_rels/.rels', '[Content_Types].xml']:
        if name not in entries:
            continue
        tree = etree.fromstring(entries[name])
        for child in list(tree):
            target = child.get('Target', '').lstrip('/')
            part = child.get('PartName', '').lstrip('/')
            if target in thumbnails or part in thumbnails:
                tree.remove(child)
        entries[name] = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)
    slide_count = sum(bool(re.fullmatch(r'ppt/slides/slide\d+\.xml', n)) for n in entries)
    note_count = sum(bool(re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', n)) for n in entries)
    remove = {'lastModifiedBy','Application','AppVersion','Company','Manager','Template','TotalTime',
              'revision','description','keywords','category','created','modified','lastPrinted',
              'Pages','Words','Characters','Lines','Paragraphs','CharactersWithSpaces'}
    for name in ['docProps/core.xml','docProps/app.xml']:
        if name not in entries:
            continue
        tree = etree.fromstring(entries[name])
        for child in list(tree):
            key = etree.QName(child).localname
            if key in remove:
                tree.remove(child)
            elif key == 'creator':
                child.text = TEAM
            elif key == 'title':
                phase = next((key for key in TITLE if f'_{key}_' in path.name), None)
                if phase:
                    child.text = TITLE[phase]
            elif key == 'PresentationFormat':
                child.text = 'On-screen Show (16:9)'
            elif key == 'Slides':
                child.text = str(slide_count)
            elif key == 'Notes':
                child.text = str(note_count)
        entries[name] = etree.tostring(tree, xml_declaration=True, encoding='UTF-8', standalone=True)
    with ZipFile(path, 'w', ZIP_DEFLATED) as z:
        for name, data in entries.items():
            z.writestr(name, data)


def clean_pdf(path):
    reader = PdfReader(path)
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.metadata = None
    writer.add_metadata({'/Title':(reader.metadata or {}).get('/Title',path.stem.replace('_',' ')), '/Author':TEAM})
    buffer = io.BytesIO()
    writer.write(buffer)
    path.write_bytes(buffer.getvalue())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=ROOT/'submissions')
    args = parser.parse_args()
    for path in args.root.rglob('*'):
        if path.suffix in {'.docx','.pptx'}:
            clean_office(path)
        elif path.suffix == '.pdf':
            clean_pdf(path)
    print('Removed irrelevant metadata and stale previews; retained titles, team names and accurate slide counts.')
