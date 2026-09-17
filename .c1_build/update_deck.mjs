import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {FileBlob,Presentation,PresentationFile} from '@oai/artifact-tool';
const workspaceDir='/Users/gravitycodez/Desktop/Project managment';
const build=path.join(workspaceDir,'.c1_build');
const skill='/Users/gravitycodez/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const source=path.join(workspaceDir,'C1_ClassMic/03_Slides/ClassMic_C1_Three_Slides.pptx');
const finalPath=path.join(workspaceDir,'C1_ClassMic/03_Slides/ClassMic_C1_Three_Slides_Updated.pptx');
const imported=await PresentationFile.importPptx(await FileBlob.load(source));
const proto=imported.toProto();
let matches=0;
for(const slide of proto.slides)for(const e of slide.elements)for(const p of e.paragraphs??[])for(const r of p.runs??[]){
  if(r.text?.includes('Student input and genuine brainstorming photos are pending.')){
    r.text=r.text.replace('Student input and genuine brainstorming photos are pending.','Genuine brainstorming photos are pending.');matches++;
  }
}
if(matches!==1)throw new Error('Expected one individual-input reminder, got '+matches);
const presentation=Presentation.load(proto);
presentation.slides.items[2].speakerNotes.textFrame.setText('Sources: ClassMic_Phase_C_Project_Charter.docx, stakeholder register, governance, constraints and authorization sections. Role appointments and approval signatures remain unverified. Individual student input is handled separately at the user’s request. Genuine photos of the team discussing the charter are still required. The repository location of the approved ClassMic A2/B2 documents is awaiting clarification.');
const candidatePath=path.join(build,'candidate_separate_inputs.pptx');
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const sourceHash=createHash('sha256').update(await fs.readFile(source)).digest('hex');
const result=await finalizePresentation({
  workspaceDir,candidatePath,finalPath,
  pythonExecutable:'/Users/gravitycodez/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  explicitTotalSlideCount:3,
  requiredNativeTableOwnerSlides:[1],
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','1'],
  fontPolicy:{basis:'reference',families:['Helvetica Neue','Helvetica Neue Medium'],referencePath:source,referenceSha256:sourceHash},
  verifyArtifactToolImport:true,
  receiptPath:path.join(build,'deck_separate_inputs.validation.json')
});
console.log(JSON.stringify({path:result.finalPath,integrity:result.packageIntegrity.status,layoutFindings:result.presentationLayout.findingCount}));
const checked=await PresentationFile.importPptx(await FileBlob.load(finalPath));
for(let i=0;i<checked.slides.items.length;i++){
  const img=await checked.export({slide:checked.slides.items[i],format:'png',scale:1.25});
  await fs.writeFile(path.join(build,'updated-slide-'+(i+1)+'.png'),new Uint8Array(await img.arrayBuffer()));
}
await fs.rename(source,path.join(build,'before_separate_inputs',path.basename(source)));
console.log('Updated deck, rendered all three slides, and archived the previous deck.');
