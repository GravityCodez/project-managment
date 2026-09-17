import fs from 'node:fs/promises';
import {FileBlob,PresentationFile} from '@oai/artifact-tool';
const file='/Users/gravitycodez/.codex/plugins/cache/openai-curated-remote/openai-templates/0.1.1/skills/artifact-template-team-alignment/assets/reference.pptx';
const p=await PresentationFile.importPptx(await FileBlob.load(file));
await fs.writeFile('.c1_build/reference.proto.json',JSON.stringify(p.toProto()));
console.log('PROTO KEYS',Object.keys(p.toProto()));
console.log('SLIDE HELP',JSON.stringify(p.help('slide',{search:'delete',include:['index','notes'],maxChars:5000})));
console.log('TABLE HELP',JSON.stringify(p.help('table',{search:'remove',include:['index','notes'],maxChars:3000})));
console.log('LAYOUTS',JSON.stringify(await p.inspect({kind:'layout',maxChars:2000})));
for(const index of [8,10,12]) {
 const s=p.slides.items[index];
 console.log('SLIDE',index+1,JSON.stringify(await p.inspect({kind:'textbox,shape,table',target:{id:'sl/'+s.id},maxChars:16000})));
 await fs.writeFile('.c1_build/reference-'+(index+1)+'.layout.json',await (await s.export({format:'layout'})).text());
}
