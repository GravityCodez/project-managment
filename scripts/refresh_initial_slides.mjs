import fs from 'node:fs/promises';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {createRequire} from 'node:module';
const root=fileURLToPath(new URL('../',import.meta.url));
const req=createRequire(path.join(process.env.NODE_MODULES_DIR,'../package.json'));
const {FileBlob,PresentationFile}=await import(pathToFileURL(req.resolve('@oai/artifact-tool')).href);
const skill=process.env.PRESENTATIONS_SKILL_DIR;
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);
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
const notes={
 A2:['ClassMic proposes a controlled classroom microphone prototype. Demand and performance are hypotheses to test.','Nurtore Arynuruly is the proposed project manager and Temiko Machavariani the proposed technical lead. Participation by reviewers depends on availability.','Targets describe a small feasibility study. Report the actual feedback numerator and denominator. Measure one-way audio delay separately from speaking activation.'],
 B2:['Biamp Crowd Mics supports phone microphones and moderator control. Source: https://www.biamp.com/products/families/crowd-mics (accessed 17 September 2026). Commercial capability does not establish local demand or a quoted cost.','Sources: https://www.biamp.com/products/families/crowd-mics and https://www.biamp.com/products/families/crowd-mics/faq (accessed 17 September 2026). The 100-hour and AED 0 estimates assume available student capacity and existing resources.','Proposed planning review: 18 September. Two seven-day sprints: 19–25 September and 26 September–2 October. The product report is due 3 October at 00:00; execution evidence is due 4 October at 00:00. Closing work is due 10 October at 00:00.'],
 C1:['The scope and performance figures are proposed acceptance targets. No test outcomes are asserted. Speaking activation includes the time from instructor approval until a ready speaker is audible.','Two weekly sprints end on 2 October to leave the product report ready before 3 October at 00:00. Live classroom deployment requires separate authorization.','The proposed allocation is 54 hours for Temiko Machavariani and 46 for Nurtore Arynuruly. The course instructor accepts assessed deliverables and reviews material changes.']
};
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
 p.slides.items.forEach((s,i)=>s.speakerNotes.textFrame.setText(notes[key][i]));
 const candidatePath=path.join(build,key+'-candidate.pptx'),finalPath=path.join(build,'final',key+'-final-v2.pptx');
 await (await PresentationFile.exportPptx(p)).save(candidatePath);
 await finalizePresentation({workspaceDir:root,candidatePath,finalPath,pythonExecutable:process.env.RUNTIME_PYTHON,
 integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),explicitTotalSlideCount:3,requiredNativeTableOwnerSlides:[owner],layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide',String(owner)],verifyArtifactToolImport:true,receiptPath:path.join(build,key+'-validation.json')});
 await fs.copyFile(finalPath,path.join(root,'submissions/initial-phases',folder,`ClassMic_${key}_Three_Slides.pptx`));
 const checked=await PresentationFile.importPptx(await FileBlob.load(finalPath));
 for(let i=0;i<3;i++){const png=await checked.export({slide:checked.slides.items[i],format:'png',scale:1.25});await fs.writeFile(path.join(build,`${key}-after-${i+1}.png`),new Uint8Array(await png.arrayBuffer()));}
 console.log(key+' refreshed and rendered');
}
