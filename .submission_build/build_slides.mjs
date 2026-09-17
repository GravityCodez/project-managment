import fs from 'node:fs/promises';
import path from 'node:path';
import {createHash} from 'node:crypto';
import {pathToFileURL} from 'node:url';
import {FileBlob, Presentation, PresentationFile} from '@oai/artifact-tool';

const root='/Users/gravitycodez/Desktop/Project managment';
const build=path.join(root,'.submission_build');
const skill='/Users/gravitycodez/.codex/plugins/cache/openai-primary-runtime/presentations/26.905.11957/skills/presentations';
const reference='/Users/gravitycodez/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-team-alignment/assets/reference.pptx';
const original=(await PresentationFile.importPptx(await FileBlob.load(reference))).toProto();
const referenceSha256=createHash('sha256').update(await fs.readFile(reference)).digest('hex');
const {finalizePresentation}=await import(pathToFileURL(path.join(skill,'container_tools/artifact_tool_utils.mjs')).href);

function el(s,id){const e=s.elements.find(e=>e.id===id); if(!e)throw Error('Missing '+id);return e;}
function para(old,text,size=18,heading=false){
 const p=structuredClone(old??{});
 const r=structuredClone(p.runs?.[0]??{id:''});
 r.text=text; delete r.fieldType;
 r.textStyle={...r.textStyle,typeface:heading?'Helvetica Neue Medium':'Helvetica Neue',fontSize:Math.round(size*100)};
 p.runs=[r];p.inlineNodes=[];
 p.paragraphStyle={...p.paragraphStyle,bulletCharacter:'',marginLeft:0,indent:0,spaceBeforePoints:0,spaceAfterPoints:heading?850:500};
 p.level=0; return p;
}
function text(e,specs){const old=structuredClone(e.paragraphs??[]);e.paragraphs=specs.map((x,i)=>para(old[Math.min(i,old.length-1)],...x));e.textStyle={...e.textStyle,autoFit:{noAutofit:{}}};}
function simple(e,t,size){text(e,[[t,size??18,false]]);}
function footer(s,id,t){const f=el(s,id);f.placeholderType=undefined;f.placeholderIndex=undefined;f.bbox={xEmu:393700,yEmu:6330000,widthEmu:10600000,heightEmu:320000};simple(f,t,12);}
function make(indices){const p=structuredClone(original);p.slides=indices.map(i=>p.slides[i-1]);p.slides.forEach((s,i)=>s.index=i);p.charts=[];return p;}

function fourRows(s,title,intro,rows,num,foot){
 simple(el(s,'533'),title,30);simple(el(s,'532'),String(num),10);
 text(el(s,'3'),intro);
 const labels=['15','17','19','21'],bodies=['12','16','18','20'];
 for(let i=0;i<4;i++){text(el(s,labels[i]),[[rows[i][0],16,true]]);simple(el(s,bodies[i]),rows[i][1],16);}
 footer(s,'2',foot);
}
function quad(s,title,items,num,foot){
 simple(el(s,'3'),title,30);simple(el(s,'2'),String(num),10);
 for(const [i,id] of ['10','11','4','5'].entries()) text(el(s,id),[[items[i][0],24,true],[items[i][1],18,false]]);
 footer(s,'6',foot);
}
function tabular(s,title,lead,body,values,widths,num,foot,size=17){
 simple(el(s,'533'),title,30);simple(el(s,'532'),String(num),10);
 text(el(s,'14'),[[lead,18,true],[body,16,false]]);
 const e=el(s,'534'), t=e.table;
 t.columnWidths=widths;
 const sample=structuredClone(t.rows);
 t.rows=values.map((vals,ri)=>{
  const row=structuredClone(sample[Math.min(ri,sample.length-1)]);
  row.heightEmu=Math.round(e.bbox.heightEmu/values.length);
  const cells=structuredClone(row.cells);
  row.cells=vals.map((v,ci)=>{
   const c=structuredClone(cells[Math.min(ci,cells.length-1)]);
   c.text=v;c.paragraphs=[para(c.paragraphs[0],v,size,ri===0)];
   c.paragraphs[0].runs[0].textStyle.bold=ri===0;
   c.paragraphs[0].paragraphStyle.spaceAfterPoints=0;
   c.paragraphs[0].paragraphStyle.lineSpacingPercent=105000;
   c.marginLeft=0;c.marginRight=110000;c.marginTop=90000;c.marginBottom=90000;
   for(const x of c.elements??[])x.paragraphs=structuredClone(c.paragraphs);
   return c;
  }); return row;
 }); footer(s,'3',foot);
}

const a=make([13,11,9]);
fourRows(a.slides[0],'ClassMic aspiration',[
 ['A2  Classroom participation',18,true],
 ['Make student questions easier for the whole room to hear while the instructor controls speaking turns.',20,false],
 ['The course project will test a small browser prototype using existing equipment.',18,false]
],[
 ['Problem','When a question is hard to hear, the instructor may need to repeat it or pass a microphone. Local frequency is unmeasured.'],
 ['Proposed value','Students request a turn from their phones. An approved speaker uses the room speaker without passing a microphone.'],
 ['Evidence','The in-class SMART note supports the concept. User demand and performance still need testing.'],
 ['Boundary','Two weekly build sprints and controlled evaluation. A live classroom pilot needs a later decision.']
],1,'Revised ClassMic course proposal. Team and instructor review are pending.');
quad(a.slides[1],'People and decisions',[
 ['Students','Speakers need a simple way to request a turn. Listeners need clear audio. Participation stays optional, with an alternative speaking path.'],
 ['Instructors','Operators need approval, mute and end controls that fit classroom discussion. Their feedback will shape the workflow.'],
 ['Project team','Temiko leads the prototype. Nurtore coordinates requirements, delivery and evaluation. Use these planning roles and check capacity at sprint planning.'],
 ['Review and support','The course instructor is the proposed acceptance authority. Device, sound and accessibility advice depends on available reviewers.']
],2,'Planning roles are selected. Reviewer participation and course acceptance remain open.');
tabular(a.slides[2],'Proposed success measures','Course feasibility test','Five priority user stories, two weekly sprints and a report of actual results. These targets are proposals, not measured outcomes.',[
 ['Measure','Target','Evidence'],
 ['Complete scope','Five stories and all Must checks','Acceptance record'],
 ['Setup and speaking','9/10 setups within 2 min\n27/30 speaking trials within 3 sec','Scripted timed trials'],
 ['Audibility','At least 75% positive feedback\nAt least 5 volunteer reviewers','Counts and sample limits'],
 ['Control and privacy','No unauthorized transmission\nNo saved audio or transcripts','Misuse and storage checks']
],[2300000,5700000,3404599],3,'Separate one-way audio-delay target: 95th percentile at most 150 ms.',17);

const b=make([13,9,11]);
fourRows(b.slides[0],'ClassMic business case',[
 ['B2  Decision requested',18,true],
 ['GO for a limited course prototype using existing resources.',22,false],
 ['A funded classroom pilot stays at REVISE until local need, performance, cost and support are established.',18,false]
],[
 ['Need','Test whether phone microphones make student contributions easier to hear than the current classroom workaround.'],
 ['Value','The course gains a focused project to investigate, build and evaluate. Institutional savings remain unproven.'],
 ['Alternatives','Improve the current process, evaluate a commercial product, or build the small ClassMic prototype.'],
 ['Evidence','Biamp offers a similar core workflow. The case for custom work rests on course learning and testing the browser experience.']
],1,'No pilot results, supplier quote or funding approval are claimed.');
tabular(b.slides[1],'Alternatives and tradeoffs','A bounded comparison','Commercial capability is documented. Prices, local fit and adoption still need validation. Full criteria appear in the B2 document.',[
 ['Option','Potential value','Cost position','Main uncertainty'],
 ['Improve current','Use instructor repetition or an existing mic','No new platform assumed','Does it solve the local problem?'],
 ['Buy or adapt','Existing phone mic and moderator workflow','Hardware and installation quote needed','Room fit and total support cost'],
 ['Custom prototype','Test a browser workflow and course learning','100 student hours proposed\nNo new cash assumed','Audio feasibility and maintenance']
],[2300000,3300000,3000000,2804599],2,'The evidence does not establish that custom development is cheaper or better for a university.',16);
quad(b.slides[2],'Delivery and decision gates',[
 ['Proposed sequence','Review D by 19 September. Sprint 1 runs 20–26 September. Sprint 2 runs 27 September–3 October. Closing runs 4–9 October.'],
 ['Resources','Plan for 100 student hours. Reuse available phones, a laptop and a speaker. Any paid tool or equipment requires a revised estimate.'],
 ['Course acceptance','Complete five Must stories, timed trials and volunteer feedback. Report unmet targets, defects and the limits of the evidence.'],
 ['Future investment','A live pilot needs validated demand, acceptable sound, a commercial comparison, named support and a funded authorization.']
],3,'D review is planned for 19 September. The E opening date controls uploads.');

const c=make([9,11,13]);
tabular(c.slides[0],'ClassMic project charter','C1  Draft course authorization','Test student phones as instructor-controlled microphones. Revised A2 and B2 support a limited prototype, controlled evaluation and a later pilot decision.',[
 ['Objective','Proposed target','Evidence'],
 ['O1  Complete scope','Five stories and all Must checks','Acceptance record'],
 ['O2  Practical workflow','9/10 setups within 2 min\n27/30 speaking trials within 3 sec','Scripted timed trials'],
 ['O3  Audibility','At least 75% positive feedback\nAt least 5 volunteer reviewers','Counts and sample limits'],
 ['O4  Control and privacy','No unauthorized transmission\nNo saved audio or transcripts','Misuse and storage checks']
],[2600000,5300000,3504599],1,'Selected one-way delay target: 95th percentile at most 150 ms. Formal course acceptance remains open.',17);
quad(c.slides[1],'Scope and delivery',[
 ['Included scope','Temporary browser sessions, QR or code join, speaking queue, one approved phone microphone, speaker output, recovery and evaluation.'],
 ['Exclusions','Live teaching deployment, recording, transcripts, persistent profiles, grading, attendance, simultaneous microphones and paid production infrastructure.'],
 ['Requirements','Explicit microphone permission, instructor approval and push to talk. Mute, disconnect and end must stop audio. Preserve an alternative speaking route.'],
 ['Milestones','Plan review by 19 September. Sprint 1 on 20–26 September. Sprint 2 on 27 September–3 October. Closeout and final presentation on 4–9 October.']
],2,'Two weekly construction sprints, after the planned review on 19 September.');
fourRows(c.slides[2],'Authority and open decisions',[
 ['Planning responsibilities',18,true],
 ['Course instructor: acceptance authority.\nNurtore Arynuruly: project manager.\nTemiko Machavariani: technical lead.',18,false],
 ['The PM coordinates daily work. The instructor reviews material scope and schedule changes. No university spending authority is implied.',17,false]
],[
 ['Stakeholders','Student speakers and listeners, instructors and the project team. Technical and accessibility reviewers participate if available.'],
 ['Initial risks','Feedback, delay, incompatible devices, unwanted transmission and limited time. Test early and retain a fallback.'],
 ['Resources','Proposed 100 student hours and AED 0 new cash spending through reuse. Confirm equipment, volunteers and capacity.'],
 ['To confirm','Formal course approval, resource access and genuine team evidence. Original individual input and the brainstorming proposal are included.']
],3,'No live deployment or paid commitment is authorized by this draft.');

const decks=[
 {key:'A2',proto:a,folder:'A_Aspiration',notes:[
 'Sources: ClassMic in-class SMART note supplied by the user, prior ClassMic charter, revised A2 document. The audibility problem is a hypothesis without a measured local baseline. The course-prototype scope is proposed for review. No approval or user study is claimed.',
 'Source: revised ClassMic A2 aspiration and C1 charter. Planning roles are selected. Formal course acceptance and technical reviewer participation remain open.',
 'Source: revised ClassMic A2 and C1. Timed-trial and volunteer sample sizes are proposed course feasibility methods. They are not statistically representative. Transport delay has a separate measurement and a selected 95th percentile target of 150 milliseconds.'
 ]},
 {key:'B2',proto:b,folder:'B_Business_Case',notes:[
 'Sources: revised ClassMic B2 and A2. Biamp Crowd Mics official product overview https://www.biamp.com/products/families/crowd-mics reviewed 10 September 2026 documents smartphone microphone and moderator functions. This is product capability evidence, not local demand or a supplier quotation. Custom prototype work is recommended for the course, not as a proven superior institutional purchase.',
 'Sources: Biamp product overview https://www.biamp.com/products/families/crowd-mics and FAQ https://www.biamp.com/products/families/crowd-mics/faq reviewed 10 September 2026. Hardware purchase and professional installation require a quote. The 100-hour estimate and AED 0 incremental cash assumption are proposed by the revised B2/D plan. No vendor price comparison or cost saving is asserted.',
 'Sources: revised B2 and D3/D5. LMS D https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38962, E https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38965, F https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38968 reviewed 10 September 2026. Published cutoffs are 22 September, 4 October and 10 October at 00:00 as displayed. E opens 26 September. D review is scheduled for 19 September. The upload opening date does not state a restriction on earlier work.'
 ]},
 {key:'C1',proto:c,folder:'C_Charter',notes:[
 'Sources: revised ClassMic A2, B2 and C1. The C1 LMS brief https://lms.mbzuai.ac.ae/mod/assign/view.php?id=38960 requests a draft with explicit confirmations, at most two pages and three slides. All measures are proposed. Ready-speaker trials measure time from instructor approval to audible speech. Transport delay is separate, with median and 95th percentile reported and a selected 95th percentile target of 150 milliseconds.',
 'Sources: revised C1 charter and D1-D3 plan. The course scope contains five priority stories and two one-week sprints. The earlier 14-week funded classroom pilot is outside the current course authorization. The proposed schedule requires D review by 19 September before the two build sprints; the E upload area opens on 26 September.',
 'Sources: revised C1 charter and evidence record. The course instructor is a proposed acceptance authority whose name and agreement remain unconfirmed. The team has not supplied original charter brainstorming images. The package includes Temiko’s original SMART note and a separately labelled AI-assisted brainstorming proposal. No group meeting or another student’s input is invented. No approval, funding, live deployment or completed testing is implied.'
 ]}
];

for(const item of decks.filter(d => d.key === 'C1')){
 const presentation=Presentation.load(item.proto);
 presentation.slides.items.forEach((s,i)=>s.speakerNotes.textFrame.setText(item.notes[i]));
 const candidatePath=path.join(build,item.key+'_candidate.pptx');
 const finalPath=path.join(build,'revised_slides',`ClassMic_${item.key}_Three_Slides_revised.pptx`);
 await (await PresentationFile.exportPptx(presentation)).save(candidatePath);
 const owner=item.key==='A2'?3:item.key==='B2'?2:1;
 await finalizePresentation({workspaceDir:root,candidatePath,finalPath,
  pythonExecutable:'/Users/gravitycodez/.cache/codex-runtimes/codex-primary-runtime/dependencies/python/bin/python3',
  integrityValidatorPath:path.join(skill,'container_tools/inspect_presentation_package_integrity.py'),
  layoutValidatorPath:path.join(skill,'container_tools/inspect_presentation_layout_geometry.py'),
  explicitTotalSlideCount:3,requiredNativeTableOwnerSlides:[owner],
  layoutArgs:['--expected-slide-size-emu','12192000,6858000','--validate-bullet-geometry','--validate-heading-fit','--require-native-table-slide',String(owner)],
  fontPolicy:{basis:'reference',families:['Helvetica Neue','Helvetica Neue Medium'],referencePath:reference,referenceSha256},
  verifyArtifactToolImport:true,receiptPath:path.join(build,item.key+'_completion_validation.json')});
 const checked=await PresentationFile.importPptx(await FileBlob.load(finalPath));
 for(let i=0;i<3;i++){
  const png=await checked.export({slide:checked.slides.items[i],format:'png',scale:1.25});
  await fs.writeFile(path.join(build,`${item.key}_slide_${i+1}.png`),new Uint8Array(await png.arrayBuffer()));
 }
 console.log(item.key+' finalized and rendered');
}
