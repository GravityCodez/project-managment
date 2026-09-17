import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {FileBlob,Presentation,PresentationFile} from '@oai/artifact-tool';

const workspaceDir='/Users/gravitycodez/Desktop/Project managment';
const skill='/Users/gravitycodez/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const reference='/Users/gravitycodez/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-team-alignment/assets/reference.pptx';
const build=path.join(workspaceDir,'.c1_build');
const finalPath=path.join(workspaceDir,'C1_ClassMic/03_Slides/ClassMic_C1_Three_Slides.pptx');
const imported=await PresentationFile.importPptx(await FileBlob.load(reference));
const proto=imported.toProto();
proto.slides=[proto.slides[8],proto.slides[10],proto.slides[12]];
proto.slides.forEach((s,i)=>s.index=i);
proto.charts=[];

function element(slide,id){const e=slide.elements.find(x=>x.id===id);if(!e)throw new Error('Missing element '+id);return e;}
function para(old,text,size,role='body'){
  const result=structuredClone(old??{});
  const run=structuredClone(result.runs?.[0]??{id:''});
  run.text=text; delete run.fieldType;
  run.textStyle={...run.textStyle,typeface:'Helvetica Neue'};
  if(size)run.textStyle.fontSize=Math.round(size*100);
  if(role==='label')run.textStyle.typeface='Helvetica Neue Medium';
  result.runs=[run];result.inlineNodes=[];
  result.paragraphStyle={...result.paragraphStyle,bulletCharacter:'',marginLeft:0,indent:0,spaceBeforePoints:0,spaceAfterPoints:role==='heading'?850:500};
  result.level=0;
  return result;
}
function text(e,specs){
  const old=structuredClone(e.paragraphs??[]);
  e.paragraphs=specs.map((v,i)=>para(old[Math.min(i,old.length-1)],v[0],v[1],v[2]));
  e.textStyle={...e.textStyle,autoFit:{noAutofit:{}}};
}
function simple(e,value,size){text(e,[[value,size]]);}
function footer(slide,value,id){
  const f=element(slide,id);
  f.placeholderType=undefined;f.placeholderIndex=undefined;
  f.bbox={xEmu:393700,yEmu:6330000,widthEmu:10600000,heightEmu:320000};
  simple(f,value,12);
}
const [s1,s2,s3]=proto.slides;
simple(element(s1,'533'),'ClassMic C1 project charter');
text(element(s1,'14'),[
  ['Draft authorization',18,'heading'],
  ['Test student phones as instructor-controlled microphones to improve classroom audibility and participation. Proposed pilot: 14 weeks, three classrooms, six weeks live and an AED 60,000 ceiling.',16]
]);
simple(element(s1,'532'),'1',10);
const metricValues=[
 ['Success measure','Proposed target','Evidence'],
 ['Session setup','At least 90% within 2 minutes','Timed session records'],
 ['Speaking access','At least 90% audible within 3 seconds of approval','Request and audio timing'],
 ['Audio delay','Median of 700 ms or less','Latency tests'],
 ['Audibility','At least 75% positive feedback','Student and instructor survey'],
 ['Privacy and security','Zero critical incidents','Incident and control records']
];
const te=element(s1,'534');
const table=te.table;
table.columnWidths=[2500000,5000000,3904599];
table.rows=table.rows.slice(0,6);
table.rows.forEach((row,ri)=>{
  row.heightEmu=Math.round(te.bbox.heightEmu/6);
  row.cells=row.cells.slice(0,3);
  row.cells.forEach((cell,ci)=>{
    const value=metricValues[ri][ci];
    cell.text=value;
    cell.paragraphs=[para(cell.paragraphs[0],value,17)];
    cell.paragraphs[0].runs[0].textStyle.bold=ri===0;
    cell.paragraphs[0].paragraphStyle.spaceAfterPoints=0;
    cell.paragraphs[0].paragraphStyle.lineSpacingPercent=105000;
    cell.marginLeft=0;cell.marginRight=110000;cell.marginTop=85000;cell.marginBottom=85000;
    for(const nested of cell.elements??[])nested.paragraphs=structuredClone(cell.paragraphs);
  });
});
footer(s1,'Draft targets and limits require confirmation against the approved ClassMic A2 and B2 outputs.','3');

simple(element(s2,'3'),'Scope and delivery');
simple(element(s2,'2'),'2',10);
text(element(s2,'10'),[
 ['Included scope',24,'heading'],
 ['Browser and QR join, temporary sessions, speaking queue, instructor controls, one active phone microphone, room speaker output, user guidance and pilot evaluation.',18]
]);
text(element(s2,'11'),[
 ['Exclusions',24,'heading'],
 ['Recording, stored audio or transcripts, voice identification, speech-based attendance or grading, simultaneous microphones, permanent profiles, remote learning and campus-wide rollout.',18]
]);
text(element(s2,'4'),[
 ['High level requirements',24,'heading'],
 ['Explicit microphone permission, instructor approval, push to talk and mute/end controls. Preserve privacy and accessible participation, with a physical microphone or instructor-repeat fallback.',18]
]);
text(element(s2,'5'),[
 ['Deliverables and milestones',24,'heading'],
 ['W1 charter and kickoff. W2–3 requirements. W4–6 prototype. W7–8 testing and user acceptance. W9–14 six-week pilot, evaluation and sponsor decision.',18]
]);
footer(s2,'Schedule and resource commitments remain subject to confirmation.','6');

simple(element(s3,'533'),'Authority and confirmation');
simple(element(s3,'532'),'3',10);
text(element(s3,'3'),[
 ['Proposed leadership',18,'heading'],
 ['Sponsor: Dean of Academic Affairs.\nProject manager: Nurtore Arynuruly.\nTechnical lead: Temiko Machavariani.',18],
 ['On approval, the PM manages daily work within agreed limits. The sponsor approves material changes. Control owners approve readiness.',18]
]);
for(const [id,value] of [['15','Stakeholders'],['17','Initial risks'],['19','Assumptions'],['21','To confirm']]) {
 const e=element(s3,id);text(e,[[value,16,'label']]);
}
simple(element(s3,'12'),'Teaching and Learning, instructors, students, IT/AV, privacy and security, accessibility, Finance and Procurement.',16);
simple(element(s3,'16'),'Feedback, delay, incompatible devices, privacy misuse and low adoption. Test rooms, train users and retain a fallback.',16);
simple(element(s3,'18'),'Stable Wi-Fi, speakers, compatible phones and available reviewers. Proposed limits: 14 weeks, three rooms, AED 60,000.',16);
simple(element(s3,'20'),'Approved ClassMic A2/B2, role appointments, dates, rooms and evaluation method. Student input and genuine brainstorming photos are pending.',16);
footer(s3,'The available CampusCrew business case is for a different project. ClassMic approval is unverified.','2');

const presentation=Presentation.load(proto);
const notes=[
 'C1 draft charter. Sources: ClassMic_Phase_C_Project_Charter.docx, sections 1 to 4 and 10. All values are carried forward from that existing draft. Approved ClassMic A2/B2 outputs and sponsor approval were not supplied. CampusCrew_Phase_B_Business_Case.docx concerns a different project. Success targets require confirmation of definitions, measurement window, sample sufficiency and acceptance owner.',
 'Sources: ClassMic_Phase_C_Project_Charter.docx, sections 3, 4 and 10. The relative milestones are proposed and have no confirmed calendar dates. The final pilot includes the six weeks from Week 9 through Week 14. Recording and persistent audio or transcript storage remain excluded.',
 'Sources: ClassMic_Phase_C_Project_Charter.docx, stakeholder register, governance, constraints and authorization sections. Role appointments and approval signatures have not been verified. Actual individual input from Temiko Machavariani and Nurtore Arynuruly and real photos of charter brainstorming were not supplied. The package contains labeled forms for the team to complete.'
];
presentation.slides.items.forEach((s,i)=>s.speakerNotes.textFrame.setText(notes[i]));
const candidatePath=path.join(build,'candidate.pptx');
await (await PresentationFile.exportPptx(presentation)).save(candidatePath);
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const referenceSha256=createHash('sha256').update(await fs.readFile(reference)).digest('hex');
const result=await finalizePresentation({
 workspaceDir,candidatePath,finalPath,
 pythonExecutable:'/Users/gravitycodez/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
 layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
 explicitTotalSlideCount:3,
 requiredNativeTableOwnerSlides:[1],
 layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide','1'],
 fontPolicy:{basis:'reference',families:['Helvetica Neue','Helvetica Neue Medium'],referencePath:reference,referenceSha256},
 verifyArtifactToolImport:true,
 receiptPath:path.join(build,'deck.validation.json')
});
console.log(JSON.stringify(result));
const checked=await PresentationFile.importPptx(await FileBlob.load(finalPath));
for(let i=0;i<checked.slides.items.length;i++){
 const preview=await checked.export({slide:checked.slides.items[i],format:'png',scale:1.25});
 await fs.writeFile(path.join(build,'slide-'+(i+1)+'.png'),new Uint8Array(await preview.arrayBuffer()));
}
console.log('Created and rendered three-slide deck.');
