"""Build the 19-element ClassMic ABCDEF WBS, Project XML and standalone PDF."""
from pathlib import Path
from datetime import date,timedelta
import csv,json,xml.etree.ElementTree as ET
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4,landscape
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'submissions/lab-2026-09-17'
OUT.mkdir(parents=True,exist_ok=True)
TEAM='Temiko Machavariani and Nurtore Arynuruly'
TM='Temiko Machavariani'; NA='Nurtore Arynuruly'
# Two packages per phase; work is total student effort, not elapsed duration.
phases=[
 ('A','Aspiration',[
 ('Opportunity and stakeholders','2026-09-10',1,1,3),
 ('Value proposition and success measures','2026-09-11',1,1,3)]),
 ('B','Business Case',[
 ('Alternatives and feasibility','2026-09-12',1,2,2),
 ('Investment recommendation','2026-09-13',1,2,2)]),
 ('C','Charter',[
 ('Objectives and project boundaries','2026-09-14',1,2,2),
 ('Roles and decision authority','2026-09-15',1,2,2)]),
 ('D','Develop Plans',[
 ('Requirements and linked work plan','2026-09-16',2,4,4),
 ('Risk cost quality and plan review','2026-09-18',1,4,4)]),
 ('E','Execute',[
 ('Sprint 1 sessions queue and controls','2026-09-19',7,18,6),
 ('Sprint 2 audio testing and product report','2026-09-26',7,14,10)]),
 ('F','Finish',[
 ('Evaluation and lessons learned','2026-10-03',3,2,4),
 ('Final recommendation and presentation','2026-10-06',4,2,4)])]
rows=[]; previous=None
for number,(letter,name,children) in enumerate(phases,1):
    uid=len(rows)+1; begin=date.fromisoformat(children[0][1]); last=children[-1];end=date.fromisoformat(last[1])+timedelta(days=last[2]-1)
    rows.append(dict(id=uid,wbs=letter,outline=str(number),level=1,name=f'{letter} {name}',start=begin,finish=end,days=(end-begin).days+1,tm=sum(x[3] for x in children),na=sum(x[4] for x in children),pred=None,summary=True))
    for j,(task,ds,days,tm,na) in enumerate(children,1):
        uid=len(rows)+1;begin=date.fromisoformat(ds)
        rows.append(dict(id=uid,wbs=f'{letter}.{j}',outline=f'{number}.{j}',level=2,name=task,start=begin,finish=begin+timedelta(days=days-1),days=days,tm=tm,na=na,pred=previous,summary=False));previous=uid
for r in rows:
    r['id']+=1
    if r['pred']: r['pred']+=1
    r['outline']='1.'+r['outline']
    r['level']+=1
rows.insert(0,dict(id=1,wbs='0',outline='1',level=1,name='ClassMic',start=date(2026,9,10),finish=date(2026,10,9),days=30,tm=54,na=46,pred=None,summary=True))
leaves=[r for r in rows if not r['summary']]
NS='http://schemas.microsoft.com/project';ET.register_namespace('',NS)
def el(parent,name,value=None):
    n=ET.SubElement(parent,'{'+NS+'}'+name)
    if value is not None:n.text=str(value)
    return n
p=ET.Element('{'+NS+'}Project')
for k,v in [('SaveVersion',14),('UID',1),('Name','ClassMic WBS and Schedule'),('Title','ClassMic ABCDEF Work Breakdown and Schedule'),('Subject','BUS 2010 WBS and schedule lab'),('Manager',NA),('Author',TEAM),('CreationDate','2026-09-17T20:00:00'),('ScheduleFromStart',1),('StartDate','2026-09-10T08:00:00'),('FinishDate','2026-10-09T17:00:00'),('CriticalSlackLimit',0),('CurrencyDigits',2),('CurrencySymbol','AED'),('CurrencyCode','AED'),('CalendarUID',1),('DefaultStartTime','08:00:00'),('DefaultFinishTime','17:00:00'),('MinutesPerDay',480),('MinutesPerWeek',3360),('DaysPerMonth',30),('DefaultTaskType',1),('DurationFormat',7),('WorkFormat',2)]:el(p,k,v)
cals=el(p,'Calendars');cal=el(cals,'Calendar')
for k,v in [('UID',1),('Name','Seven day planning calendar'),('IsBaseCalendar',1),('BaseCalendarUID',-1)]:el(cal,k,v)
week=el(cal,'WeekDays')
for day in range(1,8):
    d=el(week,'WeekDay');el(d,'DayType',day);el(d,'DayWorking',1);times=el(d,'WorkingTimes')
    for start,finish in [('08:00:00','12:00:00'),('13:00:00','17:00:00')]:
        t=el(times,'WorkingTime');el(t,'FromTime',start);el(t,'ToTime',finish)
tasks=el(p,'Tasks')
for r in rows:
    t=el(tasks,'Task')
    values=[('UID',r['id']),('ID',r['id']),('Name',r['name']),('Type',1),('IsNull',0),('WBS',r['wbs']),('OutlineNumber',r['outline']),('OutlineLevel',r['level']),('Start',f"{r['start']}T08:00:00"),('Finish',f"{r['finish']}T17:00:00"),('Duration',f"PT{r['days']*8}H0M0S"),('DurationFormat',7),('Work',f"PT{r['tm']+r['na']}H0M0S"),('EffortDriven',0),('Milestone',0),('Summary',int(r['summary'])),('Critical',1),('PercentComplete',0),('PercentWorkComplete',0),('ActualWork','PT0H0M0S'),('RemainingWork',f"PT{r['tm']+r['na']}H0M0S"),('ConstraintType',0),('CalendarUID',1),('LevelAssignments',0),('LevelingCanSplit',0)]
    for k,v in values:el(t,k,v)
    if r['pred']:
        pr=el(t,'PredecessorLink');el(pr,'PredecessorUID',r['pred']);el(pr,'Type',1);el(pr,'CrossProject',0);el(pr,'LinkLag',0);el(pr,'LagFormat',7)
    if r['wbs'] in ['D.2','E.2','F.2']:
        el(t,'Deadline',{'D.2':'2026-09-22T00:00:00','E.2':'2026-10-03T00:00:00','F.2':'2026-10-10T00:00:00'}[r['wbs']])
    el(t,'Notes',f"Proposed baseline. Team: {TEAM}. Estimated effort: Temiko {r['tm']} h; Nurtore {r['na']} h. Scheduled dates do not assert actual completion.")
resources=el(p,'Resources')
for uid,name,initials in [(1,TM,'TM'),(2,NA,'NA')]:
    r=el(resources,'Resource')
    for k,v in [('UID',uid),('ID',uid),('Name',name),('Type',1),('IsNull',0),('Initials',initials),('MaxUnits',1),('StandardRate',0),('StandardRateFormat',2),('CalendarUID',1)]:el(r,k,v)
assignments=el(p,'Assignments')
for r in leaves:
    for resource,work in [(1,r['tm']),(2,r['na'])]:
        a=el(assignments,'Assignment')
        for k,v in [('UID',r['id']*10+resource),('TaskUID',r['id']),('ResourceUID',resource),('PercentWorkComplete',0),('Work',f'PT{work}H0M0S'),('Units',work/(r['days']*8)),('Start',f"{r['start']}T08:00:00"),('Finish',f"{r['finish']}T17:00:00")]:el(a,k,v)
ET.indent(p,space='  ')
xml=OUT/'ClassMic_WBS_and_Schedule.xml';ET.ElementTree(p).write(xml,encoding='utf-8',xml_declaration=True)
with (OUT/'ClassMic_WBS_and_Schedule.csv').open('w',newline='') as f:
    w=csv.writer(f,lineterminator="\n");w.writerow(['ID','WBS','Task','Summary','Duration days','Start','Finish','Predecessor FS','Temiko hours','Nurtore hours','Total work hours'])
    for r in rows:w.writerow([r['id'],r['wbs'],r['name'],r['summary'],r['days'],r['start'],r['finish'],r['pred'] or '',r['tm'],r['na'],r['tm']+r['na']])
# Standalone, readable coursework. 19 WBS elements; dependency logic on leaf tasks.
W,H=landscape(A4);c=canvas.Canvas(str(OUT/'ClassMic_WBS_and_Schedule.pdf'),pagesize=(W,H))
c.setTitle('ClassMic WBS and Schedule');c.setAuthor(TEAM);c.setCreator('');c.setProducer('')
navy=colors.HexColor('#17384A');gray=colors.HexColor('#E8EDF0');line=colors.HexColor('#CBD5DA')
def header(subtitle,page):
    c.setFillColor(navy);c.setFont('Helvetica-Bold',21);c.drawString(32,H-39,'ClassMic WBS and Schedule')
    c.setFillColor(colors.black);c.setFont('Helvetica',11);c.drawString(32,H-58,TEAM)
    c.setFont('Helvetica',9);c.drawString(32,H-74,'BUS 2010   17 September 2026   '+subtitle)
    c.setFont('Helvetica',8);c.drawRightString(W-32,20,f'ClassMic   {page}')
header('ABCDEF work breakdown and linked baseline',1)
y=H-115;left=32;taskx=82;chartx=365;chartw=W-397;dx=chartw/30;rowh=19
c.setFillColor(navy);c.rect(left,y-3,W-64,23,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('Helvetica-Bold',9);c.drawString(left+5,y+5,'WBS');c.drawString(taskx,y+5,'Phase or work package')
start=date(2026,9,10)
for d in [0,5,10,15,20,25]:c.drawCentredString(chartx+(d+.5)*dx,y+5,(start+timedelta(days=d)).strftime('%d %b'))
c.drawRightString(W-37,y+5,'09 Oct')
ys={}
for i,r in enumerate(rows):
    yy=y-23-i*rowh;ys[r['id']]=yy+7
    c.setFillColor(gray if r['summary'] else (colors.HexColor('#F8FAFB') if i%2==0 else colors.white));c.rect(left,yy-3,W-64,rowh,fill=1,stroke=0)
    c.setFillColor(colors.black);c.setFont('Helvetica-Bold' if r['summary'] else 'Helvetica',9)
    c.drawString(left+5,yy+4,r['wbs']);c.drawString(taskx+(0 if r['summary'] else 9),yy+4,r['name'])
    a=(r['start']-start).days;b=(r['finish']-start).days+1
    c.setFillColor(navy if r['summary'] else colors.HexColor('#3585A2'))
    c.rect(chartx+a*dx+1,yy+(6 if r['summary'] else 2),(b-a)*dx-2,4 if r['summary'] else 11,fill=1,stroke=0)
# A thin FS connector links every work package to its successor.
c.setStrokeColor(colors.HexColor('#536C7A'));c.setLineWidth(.6)
for a,b in zip(leaves,leaves[1:]):
    x1=chartx+((a['finish']-start).days+1)*dx-1;x2=chartx+(b['start']-start).days*dx+1
    ya=ys[a['id']];yb=ys[b['id']];mid=max(x1,x2)+3
    pth=c.beginPath();pth.moveTo(x1,ya);pth.lineTo(mid,ya);pth.lineTo(mid,yb);pth.lineTo(x2,yb);c.drawPath(pth)
    c.line(x2,yb,x2+3,yb+2);c.line(x2,yb,x2+3,yb-2)
c.setFont('Helvetica',9);c.setFillColor(colors.black)
c.drawString(32,75,'19 WBS elements: one project root, six phases and 12 linked work packages. All dependencies are finish-to-start with zero lag.')
c.drawString(32,59,'The 30-day baseline uses a seven-day calendar. Each build sprint spans seven days; effort totals 100 student hours.')
c.drawString(32,43,'Dates and effort are planning estimates. This schedule does not report completed project work.')
c.showPage();header('Durations responsibilities and constraints',2)
cols=[32,61,109,365,412,460,508,556,623,685,810]
headers=['ID','WBS','Work package','Days','Start','Finish','Pred','Temiko h','Nurtore h','Total h']
y=H-110;c.setFillColor(navy);c.rect(32,y-3,W-64,23,fill=1,stroke=0);c.setFillColor(colors.white);c.setFont('Helvetica-Bold',9)
for x,t in zip(cols,headers):c.drawString(x+4,y+5,t)
for i,r in enumerate(leaves):
    yy=y-25-i*22;c.setFillColor(gray if i%2==0 else colors.white);c.rect(32,yy-4,W-64,22,fill=1,stroke=0);c.setFillColor(colors.black);c.setFont('Helvetica',9)
    vals=[str(r['id']),r['wbs'],r['name'],str(r['days']),r['start'].strftime('%d %b'),r['finish'].strftime('%d %b'),str(r['pred'] or '-'),str(r['tm']),str(r['na']),str(r['tm']+r['na'])]
    for x,t in zip(cols,vals):c.drawString(x+4,yy+4,t)
yy=y-25-len(leaves)*22;c.setFont('Helvetica-Bold',9);c.drawString(113,yy+4,'Total effort');c.drawString(560,yy+4,'54');c.drawString(627,yy+4,'46');c.drawString(689,yy+4,'100')
style=ParagraphStyle('body',fontName='Helvetica',fontSize=9,leading=12,textColor=colors.black)
text=[
 '<b>Dependency chain.</b> A.1 → A.2 → B.1 → B.2 → C.1 → C.2 → D.1 → D.2 → E.1 → E.2 → F.1 → F.2. The serial chain controls the baseline finish. Summary phases roll up their children and carry no duplicate dependency links.',
 '<b>Calendar and effort.</b> Working windows are 08:00–12:00 and 13:00–17:00 every day. A duration day is an eight-hour scheduling window, not eight hours assigned to each person. Resource assignments distribute the separate effort estimates across those windows.',
 '<b>Release constraints.</b> Plan review target: 18 September. Planning submission: 22 September at 00:00. Sprint 1: 19–25 September. Sprint 2: 26 September–2 October. Product report: 3 October at 00:00. Execution evidence: 4 October at 00:00. Final presentation: 10 October at 00:00.',
 '<b>Assumptions.</b> Both team members can provide the estimated effort, existing equipment is available, and the instructor accepts the proposed sequencing. Review scope and dates if these assumptions fail. No paid resources or live classroom deployment are authorized.'
]
ypos=yy-16
for txt in text:
    txt=txt.replace('→','to').replace('–','-');para=Paragraph(txt,style);_,h=para.wrap(W-64,H);para.drawOn(c,32,ypos-h);ypos-=h+8
c.save()
# Meaningful structural and arithmetic checks.
assert len(rows)==19 and len(leaves)==12
assert sum(r['tm'] for r in leaves)==54 and sum(r['na'] for r in leaves)==46
for a,b in zip(leaves,leaves[1:]):assert a['finish']+timedelta(days=1)==b['start'] and b['pred']==a['id']
assert [r['days'] for r in leaves if r['wbs'].startswith('E.')]==[7,7]
assert next(r for r in leaves if r['wbs']=='E.2')['finish']==date(2026,10,2)
print('Created XML, CSV and 2-page PDF; verified 19 WBS elements, 11 FS links, 100 hours and two full weekly sprints.')
