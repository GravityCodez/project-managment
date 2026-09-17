import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const root=fileURLToPath(new URL('../',import.meta.url));
const req=createRequire(path.join(process.env.NODE_MODULES_DIR,'../package.json'));
const {FileBlob,PresentationFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const skill=process.env.PRESENTATIONS_SKILL_DIR;
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
const copy=JSON.parse(await fs.readFile(path.join(root,'scripts/editorial_copy.json'),'utf8'));
const build=path.join(root,'.build/initial-slides',new Date().toISOString().replace(/[:.]/g,'-'));
console.log('Staging directory: '+build);
await fs.mkdir(path.join(build,'final'),{recursive:true});
const common=[['by 19 September','by 18 September'],['on 19 September','on 18 September'],['20–26 September','19–25 September'],['27 September–3 October','26 September–2 October'],['4–9 October','3–9 October']];
const replaces=[
 ['The in-class SMART note supports the concept. User demand and performance still need testing.','The proposed phone microphone workflow needs local demand and performance testing.'],
 ['The team must confirm capacity and responsibilities.','These are proposed planning responsibilities.'],
 ['Role assignments and reviewer participation require confirmation.','Team capacity and reviewer availability remain planning assumptions.'],
 ['Measure transport delay separately. Confirm an acceptable threshold before audio acceptance.','One-way audio delay target: 95th percentile at most 150 ms.'],
 ['Full criteria appear in the B2 document.','Compare classroom fit, costs, feasibility and support.'],
 ['Confirm early D review and permission to start construction before the E upload area opens.','Product report due 3 October at 00:00; finish testing by 2 October.'],
 ['Test student phones as instructor-controlled microphones. Revised A2 and B2 support a limited prototype, controlled evaluation and a later pilot decision.','Test student phones as instructor-controlled microphones through a limited prototype and controlled evaluation. Use the findings to assess a future pilot.'],
 ['Authority and open decisions','Governance and resources'],
 ['To confirm','Assumptions'],
 ['Course sponsor and authorization, equipment access, volunteer availability and the proposed 100-hour team capacity.','Delivery assumes course acceptance, available equipment, volunteer reviewers and 100 hours of team capacity.'],
];
for(const [key,folder,owner] of [['A2','A_Aspiration',3],['B2','B_Business_Case',2],['C1','C_Charter',1]]) {
 const source=path.join(root,'archive/2026-09-17-before-reorganization',key==='C1'?'ClassMic_C1_Completed':'ClassMic_Submission/'+folder,`ClassMic_${key}_Three_Slides.pptx`);
 const p=await PresentationFile.importPptx(await FileBlob.load(source));
 const snapshot=await p.inspect({kind:'textbox',maxChars:100000});
 for(const line of snapshot.ndjson.split('\n').filter(Boolean)) {
  const x=JSON.parse(line); if(x.kind!=='textbox'||!x.text)continue;
  const target=p.resolve(x.id);
  for(const [a,b] of [...common,...replaces]) if(x.text.includes(a)) target.text.replace(a,b);
  if(x.slide===1&&x.name?.startsWith('Footer')) target.text=x.text ? 'Temiko Machavariani and Nurtore Arynuruly   BUS 2010' : '';
  if(key==='A2'&&x.text==='Evidence')target.text.replace('Evidence','Concept');
 }
 const edited=await p.inspect({kind:'textbox,table',maxChars:100000});
 const seen=new Set();
 for(const line of edited.ndjson.split('\n').filter(Boolean)){
  const x=JSON.parse(line);
  if(x.kind==='textbox'&&x.text){
   for(const [a,b] of Object.entries(copy.slides[key])) if(x.text.includes(a)){p.resolve(x.id).text.replace(a,b);seen.add(a);}
  }
  if(x.kind==='table'&&x.slide===owner){
   const table=p.resolve(x.id);
   for(const [row,col,text] of copy.tables[key])table.cells.set(row,col,text);
  }
 }
 for(const text of Object.keys(copy.slides[key]))if(!seen.has(text))throw Error('Unmatched editorial replacement: '+text);
 p.slides.items.forEach((s,i)=>s.speakerNotes.textFrame.setText(copy.notes[key][i]));
 const candidatePath=path.join(build,key+'-candidate.pptx'),finalPath=path.join(build,'final',key+'-final-v2.pptx');
 await (await PresentationFile.exportPptx(p)).save(candidatePath);
 await finalizePresentation({workspaceDir:root,candidatePath,finalPath,pythonExecutable:process.env.RUNTIME_PYTHON,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),explicitTotalSlideCount:3,requiredNativeTableOwnerSlides:[owner],layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide',String(owner)],verifyArtifactToolImport:true,receiptPath:path.join(build,key+'-validation.json')});
 await fs.copyFile(finalPath,path.join(root,'submissions/initial-phases',folder,`ClassMic_${key}_Three_Slides.pptx`));
 const checked=await PresentationFile.importPptx(await FileBlob.load(finalPath));
 for(let i=0;i<3;i++){const png=await checked.export({slide:checked.slides.items[i],format:'png',scale:1.25});await fs.writeFile(path.join(build,`${key}-after-${i+1}.png`),new Uint8Array(await png.arrayBuffer()));}
 console.log(key+' refreshed and rendered');
}
