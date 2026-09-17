from pathlib import Path
from datetime import datetime, timedelta
from xml.etree import ElementTree as ET
import csv, shutil, json

ROOT = Path('/Users/gravitycodez/Desktop/Project managment')
BUILD = ROOT / '.submission_build'
# Reuse the reviewed document styles without executing the main document builds.
exec((BUILD / 'build_submission.py').read_text().split('# A2\n')[0])
HUMAN = OUT / 'Human_Input'
HUMAN.mkdir(exist_ok=True)
source = Path('/var/folders/3b/ww4znj5s4gj4_h7qvmw9b1d40000gn/T/codex-clipboard-37a65679-cfc0-4393-b02c-3cb3b409a793.png')
photo = HUMAN / 'Temiko_Original_ClassMic_SMART_Note.png'
shutil.copy2(source, photo)

d = base('ClassMic Individual Input', 'Temiko original input')
d.add_paragraph('ClassMic Individual Input', 'Title')
p(d, 'Temiko Machavariani   |   Original in-class SMART note', size=10)
p(d, 'This is the original photograph supplied by Temiko. The crossed-out ideas and earlier 14-week proposal remain visible. The revised course plan uses two build sprints and reserves the larger pilot for a later decision.', size=10)
d.add_picture(str(photo), width=Inches(5.3))
d.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
d.save(HUMAN / 'Temiko_ClassMic_Individual_Input.docx')

d = base('ClassMic Brainstorming and Planning Decisions', 'AI assisted planning', body_size=10.5)
title(d, 'ClassMic Brainstorming and Planning Decisions', 'Companion to A2 B2 C1 and D')
p(d, 'Purpose: develop a coherent charter and plan from the ClassMic concept. Temiko confirmed the two team names and delegated the remaining planning choices to the assistant. This supplement records the resulting AI-assisted proposal. It does not report a past team meeting, quotations or Nurtore’s personal input.', lead='Purpose:')
h(d, 'Evidence we actually have')
p(d, 'Temiko’s original SMART note proposes instructor-controlled phone microphones, one active speaker, existing equipment, low delay and 75% positive feedback. His current instruction requests a complete ClassMic package and authorizes planning decisions. No completed group discussion, interview or test results were supplied.')
h(d, 'Charter brainstorming')
table(d, ['Planning question', 'Options considered', 'Selected direction and reason'], [
    ['What problem is worth testing?', 'A quiet question, a listener at the back, or time spent passing a microphone.', 'Use audibility as the hypothesis. These are typical scenarios, not observations attributed to our class.'],
    ['What could solve it?', 'Instructor repetition, an existing physical mic, a commercial phone-mic system, or a small browser prototype.', 'Build the small prototype for course learning and compare it with the current speaking process. No claim that custom software is the best institutional purchase.'],
    ['Who controls the microphone?', 'Open microphones or an instructor-approved queue.', 'One approved push-to-talk speaker, with mute, removal and end controls. This reduces interruption and makes control testable.'],
    ['How much can the course deliver?', 'A live campus pilot or a controlled two-sprint build.', 'Five Must stories in two weekly sprints. Live deployment and the earlier six-week pilot stay outside this project.'],
    ['What will count as success?', 'A polished demo alone or measured acceptance evidence.', 'All Must checks, setup and activation timings, a 150 ms one-way delay target, volunteer feedback and zero critical control defects.'],
], [1.5, 2.35, 3.25], font=9.5)
h(d, 'Decisions carried into the charter')
p(d, 'Keep the five-story boundary, 100 student hours and AED 0 incremental cash through reuse. Assign Nurtore to project coordination and Temiko to technical work. Use formal course review as the acceptance gate. These choices form the working plan; they do not establish another person’s availability or the instructor’s approval.')
page(d, 'Work breakdown and dependency brainstorming')
p(d, 'We decomposed the work by tangible output so that each item has an owner and a completion test. Each summary has two leaf outputs, giving 18 WBS elements. The detailed WBS remains in D3.')
table(d, ['Summary output', 'Two leaf outputs', 'Planning owner'], [
    ['1 Project authorization and control', '1.1 Reviewed A2/B2/charter; 1.2 status and change records', 'Nurtore'],
    ['2 Requirements and plan', '2.1 Stakeholder input and PRD; 2.2 integrated D plan', 'Nurtore'],
    ['3 Sprint 1 increment', '3.1 Session access and permissions; 3.2 instructor queue and controls', 'Temiko'],
    ['4 Sprint 2 increment', '4.1 Audio path and recovery; 4.2 acceptance and evaluation', 'Temiko / Nurtore'],
    ['5 Delivery evidence', '5.1 E demonstration; 5.2 updated requirements record', 'Temiko / Nurtore'],
    ['6 Closing', '6.1 Outcomes and lessons; 6.2 presentation and handover', 'Nurtore'],
], [2.05, 3.85, 1.2], font=10)
h(d, 'Dependency reasoning')
table(d, ['Sequence', 'Why it is required'], [
    ['S1 then parallel S2 and S3', 'Review the project direction before requirements work and the device/audio feasibility check. These two activities can run in parallel.'],
    ['Both S2 and S3 then S4', 'The integrated plan needs both user requirements and a credible technical approach.'],
    ['S4 and D review then S5', 'Start the first build sprint with a reviewed scope, backlog and acceptance plan.'],
    ['S5 then S6', 'The audio increment depends on session access, speaking approval and the first review.'],
    ['S6 and E submission then S7', 'Closeout must use actual evaluation evidence and unresolved defects.'],
], [2.2, 4.9], font=10)
h(d, 'Schedule decision')
p(d, 'Plan D review for 19 September. Sprint 1 runs 20–26 September; Sprint 2 runs 27 September–3 October. Check E before its 4 October 00:00 cutoff. Closeout runs 4–9 October, before the F cutoff. The two dependency paths through S2 and S3 have no planned internal float. If D review slips, escalate the schedule instead of silently shortening a sprint.')
p(d, 'This is a typed AI-assisted decomposition. The original hand-drawn or Post-it WBS and dependency images requested by D3 are not recreated or represented as supplied evidence.', size=9.5)
page(d, 'Communication brainstorming and working plan')
p(d, 'The communication choice should keep quick coordination separate from the lasting decision record. Telegram is selected for short team messages, Notion for the PRD and decisions, and LMS messaging or class review for instructor decisions. This selection does not claim an existing group chat or a past conversation.')
table(d, ['Need', 'Selected working practice', 'Owner'], [
    ['Resolve daily blockers', 'Ten-minute check-in on workdays. Post the next action, blocker and owner in Telegram. Urgent microphone-control failures stop the affected test immediately.', 'Both'],
    ['Keep decisions findable', 'Record scope changes, rationale, owner and date in Notion. Link each decision to the relevant requirement or risk.', 'Nurtore'],
    ['Review each increment', 'Thirty-minute review at each sprint boundary. Demonstrate completed stories, list failures and agree on the next backlog.', 'Both'],
    ['Obtain course decisions', 'Use the LMS or the next class review for formal scope, acceptance or deadline questions. Keep the instructor’s actual response.', 'Nurtore'],
    ['Collect user feedback', 'Invite willing reviewers, show a controlled demonstration, and use the anonymous form. Report all valid responses and any missing evidence.', 'Nurtore'],
    ['Preserve technical evidence', 'Keep device/browser combinations, timings, pass/fail checks and defect references. Save no session speech or transcripts.', 'Temiko'],
], [1.5, 4.45, 1.15], font=10)
h(d, 'Assumptions to test during the work')
p(d, 'At least five volunteers will be available; existing phones, a laptop and speaker can support the demo; 100 student hours will cover the scope; and two weekly sprints will be feasible after D review. Check these assumptions early and revise the plan if they fail. They are not claims about resources already secured.')
h(d, 'Original human evidence')
p(d, 'Temiko’s supplied SMART photograph is included unchanged in Human_Input. No original contribution from Nurtore, team charter-discussion image, D3 hand drawing or pre-AI D6 communication notes was supplied. The course’s human-evidence requirements therefore remain distinct from this completed planning supplement. Do not describe this generated text as a photo or a record of a meeting.')
d.save(OUT / 'Supporting_Notes/ClassMic_Brainstorming_and_Decisions.docx')

d = base('ClassMic Evaluation Protocol and Review Form', 'E evaluation preparation', body_size=10.5)
title(d, 'ClassMic Evaluation Protocol and Review Form', 'Prepared for use during execution')
p(d, 'Use this protocol after the prototype exists. It defines the selected acceptance method and blank records; it contains no test results. Nurtore coordinates reviewers and records outcomes. Temiko runs technical checks and fixes defects.')
table(d, ['Measure', 'Method', 'Pass rule'], [
    ['Setup', 'Ten trials. Start when the tester receives the join instruction; stop when the correct session shows microphone-ready status. Record denied permission and other failures.', 'At least 9 of 10 within 120 seconds.'],
    ['Speaking activation', 'Thirty trials with a ready speaker. Start at instructor approval; stop at the first audible speech from the speaker. Keep device and network conditions in the log.', 'At least 27 of 30 within 3 seconds.'],
    ['One-way audio delay', 'Thirty non-speech timing trials. Compare the input signal and speaker output on a shared measurement timebase. Process calibration signals in memory; retain only numeric timings. Never substitute round-trip ping for audio delay.', '95th percentile at most 150 ms. Report median and method. Unmeasured means unverified.'],
    ['Audibility feedback', 'At least five willing reviewers hear a short question through the usual speaking method and through ClassMic. Alternate the order across reviewers. Ask the same comparison question on the form.', 'At least 75% rate easier audibility 4 or 5 out of 5. With five reviewers, at least four must be positive.'],
    ['Control and recovery', 'Test permission denial, expired joining, two simultaneous requests, unapproved speech, release, mute, removal, timeout, disconnect and end session. Retest every repaired defect.', 'All Must checks pass. Zero unauthorized transmission, saved speech or open critical control defect.'],
], [1.25, 4.3, 1.55], font=9.5)
h(d, 'Definitions and data handling')
p(d, 'For 30 delay values, sort ascending and use the 29th value as the nearest-rank 95th percentile; the median is the average of values 15 and 16. Retain all attempts and report exclusions with reasons. Do not replace failed trials with extra successful ones.')
p(d, 'Record anonymous reviewer codes, date, device/browser combination, conditions, timings, ratings and defect IDs. Collect no names, contact details, speech recordings or transcripts in the test record. Keep participant-level records until 30 days after course feedback, then delete them and retain aggregate counts and engineering conclusions. Participants can stop without affecting their course standing.')
p(d, 'The 150 ms threshold is a selected prototype acceptance target, not a claim of measured performance or a universal classroom-audio standard. If it fails, report the failure and its effect on the recommendation.')
page(d, 'Anonymous reviewer form')
p(d, 'Reviewer code: __________     Date: __________     Test configuration: __________')
p(d, 'Participation is optional. This short form asks about a prototype demonstration, not your identity. Please compare the same question heard through the usual speaking method and through ClassMic.')
table(d, ['Question', 'Response'], [
    ['ClassMic made the question easier to hear than the usual method.', '1 Strongly disagree   2 Disagree   3 Neutral   4 Agree   5 Strongly agree'],
    ['The delay or echo disrupted the question.', '1 Strongly disagree   2 Disagree   3 Neutral   4 Agree   5 Strongly agree'],
    ['I understood how to request a turn and when the microphone was active.', '1 Strongly disagree   2 Disagree   3 Neutral   4 Agree   5 Strongly agree'],
    ['Could you participate through the intended route?', 'Yes / No / Used the alternative route'],
    ['What made listening or speaking difficult?', '________________________________________________\n________________________________________________'],
    ['What one change would help most?', '________________________________________________\n________________________________________________'],
], [3.1, 4.0], font=10)
h(d, 'Evaluation summary to complete after testing')
table(d, ['Result', 'Recorded value'], [
    ['Setup successes / attempts', '________ / 10'],
    ['Speaking-start successes / attempts', '________ / 30'],
    ['Delay median / 95th percentile / method', '________ ms / ________ ms / __________________'],
    ['Positive audibility responses / valid responses', '________ / ________ = ________ %'],
    ['Must checks passed / total checks', '________ / ________'],
    ['Open critical defects', '________'],
    ['Conclusion and important limitations', '________________________________________________'],
], [3.4, 3.7], font=10)
p(d, 'Complete these fields only from actual evidence. A small convenience sample supports a course evaluation; it does not establish campus-wide demand or effectiveness.', size=9.5)
d.save(OUT / 'D_Develop_Plans/ClassMic_Evaluation_Protocol.docx')

# Empty structured records for real testing, not invented results.
with (OUT / 'D_Develop_Plans/ClassMic_Test_Records.csv').open('w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Trial ID','Measure','Date','Device and browser','Conditions','Measured value','Unit','Pass or fail','Defect ID or notes'])
    for prefix, measure, count, unit in [('SET','Setup',10,'seconds'),('ACT','Speaking activation',30,'seconds'),('DEL','One-way audio delay',30,'milliseconds')]:
        for i in range(1,count+1): w.writerow([f'{prefix}{i:02}',measure,'','','','',unit,'',''])
with (OUT / 'D_Develop_Plans/ClassMic_Reviewer_Responses.csv').open('w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Anonymous code','Date','Configuration','Presentation order','Easier audibility 1-5','Disruptive delay 1-5','Control clarity 1-5','Participation route','Difficulty','Suggested change'])

# Microsoft Project XML exchange file. Dates and dependency logic are verified below.
NS = 'http://schemas.microsoft.com/project'
ET.register_namespace('', NS)
def tag(name): return '{'+NS+'}'+name
def add(parent, name, value):
    node = ET.SubElement(parent, tag(name)); node.text = str(value); return node
project = ET.Element(tag('Project'))
for k,v in [
    ('SaveVersion',12),('UID','CLASSMIC2026'),('Name','ClassMic Course Prototype'),
    ('Title','ClassMic Course Prototype Schedule'),('Subject','Two weekly construction sprints'),
    ('Manager','Nurtore Arynuruly'),('Author',TEAM),('CreationDate','2026-09-10T08:00:00'),
    ('ScheduleFromStart',1),('StartDate','2026-09-10T08:00:00'),('FinishDate','2026-10-09T17:00:00'),
    ('CriticalSlackLimit',0),('CurrencyDigits',2),('CurrencySymbol','AED'),('CurrencyCode','AED'),
    ('CalendarUID',1),('DefaultStartTime','08:00:00'),('DefaultFinishTime','17:00:00'),
    ('MinutesPerDay',480),('MinutesPerWeek',3360),('DaysPerMonth',30),('DefaultTaskType',1),
    ('DurationFormat',7),('WorkFormat',2),
]: add(project,k,v)
calendars = ET.SubElement(project, tag('Calendars')); cal = ET.SubElement(calendars, tag('Calendar'))
for k,v in [('UID',1),('Name','Seven-day planning windows'),('IsBaseCalendar',1),('BaseCalendarUID',-1)]: add(cal,k,v)
week = ET.SubElement(cal,tag('WeekDays'))
for day in range(1,8):
    wd=ET.SubElement(week,tag('WeekDay'));add(wd,'DayType',day);add(wd,'DayWorking',1)
    times=ET.SubElement(wd,tag('WorkingTimes'))
    for start,finish in [('08:00:00','12:00:00'),('13:00:00','17:00:00')]:
        wt=ET.SubElement(times,tag('WorkingTime'));add(wt,'FromTime',start);add(wt,'ToTime',finish)
tasks=ET.SubElement(project,tag('Tasks'))
idmap={'S1':1,'S2':2,'S3':3,'S4':4,'S5':6,'S6':8,'S7':10}
hours={'S1':10,'S2':10,'S3':8,'S4':12,'S5':24,'S6':24,'S7':12}
entries=[]
for row in schedule:
    sid,name,start,finish,days,preds,owner,critical=row
    pred_ids=[idmap[x] for x in preds.split(';') if x]
    if sid=='S5': pred_ids=[5]
    if sid=='S6': pred_ids=[7]
    if sid=='S7': pred_ids=[9]
    entries.append(dict(uid=idmap[sid],name=sid+' '+name,start=start+'T08:00:00',finish=finish+'T17:00:00',days=int(days),preds=pred_ids,owner=owner,hours=hours[sid],milestone=False,deadline=None))
for uid,name,finish,pred,deadline in [
    (5,'M1 D review','2026-09-19T17:00:00',4,'2026-09-22T00:00:00'),
    (7,'M2 Sprint 1 review','2026-09-26T17:00:00',6,None),
    (9,'M3 E ready for submission','2026-10-03T17:00:00',8,'2026-10-04T00:00:00'),
    (11,'M4 F ready for submission','2026-10-09T17:00:00',10,'2026-10-10T00:00:00'),
]: entries.append(dict(uid=uid,name=name,start=finish,finish=finish,days=0,preds=[pred],owner='Nurtore',hours=0,milestone=True,deadline=deadline))
for e in sorted(entries,key=lambda x:x['uid']):
    t=ET.SubElement(tasks,tag('Task'))
    for k,v in [('UID',e['uid']),('ID',e['uid']),('Name',e['name']),('Type',1),('IsNull',0),('Contact',e['owner']),('OutlineNumber',e['uid']),('OutlineLevel',1),('Start',e['start']),('Finish',e['finish']),('Duration',f"PT{e['days']*8}H0M0S"),('DurationFormat',7),('Work',f"PT{e['hours']}H0M0S"),('EffortDriven',0),('Estimated',1),('Milestone',int(e['milestone'])),('Summary',0),('Critical',1),('PercentComplete',0),('ConstraintType',0),('CalendarUID',1)]: add(t,k,v)
    if e['deadline']: add(t,'Deadline',e['deadline'])
    add(t,'Notes','Planning estimate. The seven-day calendar preserves calendar-date windows; task Work is the separate student-effort allowance. Formal review and resource availability are not asserted.')
    for pred in e['preds']:
        linknode=ET.SubElement(t,tag('PredecessorLink'))
        for k,v in [('PredecessorUID',pred),('Type',1),('CrossProject',0),('LinkLag',0),('LagFormat',7)]: add(linknode,k,v)
ET.indent(project,space='  ')
xml_path=OUT/'D_Develop_Plans/ClassMic_MS_Project_Schedule.xml'
ET.ElementTree(project).write(xml_path,encoding='utf-8',xml_declaration=True)
by_id={e['uid']:e for e in entries}
assert sum(e['hours'] for e in entries)==100
assert len(by_id)==11
for e in entries:
    a=datetime.fromisoformat(e['start']);b=datetime.fromisoformat(e['finish'])
    assert a<=b
    if not e['milestone']: assert (b.date()-a.date()).days+1==e['days']
    for pred in e['preds']: assert datetime.fromisoformat(by_id[pred]['finish'])<=a
    if e['deadline']: assert b<datetime.fromisoformat(e['deadline'])
assert [e['days'] for e in entries if e['name'].startswith(('S5 ','S6 '))]==[7,7]
assert ET.parse(xml_path).getroot().tag==tag('Project')

(OUT/'D_Develop_Plans/Schedule_File_Guide.md').write_text('''# ClassMic editable schedule

ClassMic_MS_Project_Schedule.xml contains seven work activities and four review or submission milestones, with finish-to-start dependencies. It includes 100 student hours, the selected dates and the published D/E/F deadline times. ClassMic_Schedule.csv supplies the same seven main activities in a simple table.

The seven-day scheduling calendar preserves the calendar-day windows in D3. Each scheduled day represents an eight-hour planning window; the separate Work field contains the estimated student effort. It does not assign either student eight hours of work every day.

Open the XML as a new project in Microsoft Project, choose Gantt Chart view, and show Name, Duration, Start, Finish, Predecessors and Work. Check the two seven-day sprint windows before exporting a chart. The file was generated in Microsoft's exchange format and checked for dates, dependencies and effort arithmetic. Microsoft Project itself is not installed on this Mac, so a native import or chart export has not been verified here.

The D3 brief asks for a chart from MS Project. The Word plan includes a readable Gantt view, and this XML supplies the editable source for a native chart. That chart-export requirement remains open until the file is opened there or the instructor accepts the supplied representation.

Format references: [Microsoft Project XML data introduction](https://learn.microsoft.com/en-us/office-project/xml-data-interchange/introduction-to-project-xml-data?view=project-client-2016), [task elements](https://github.com/MicrosoftDocs/office-developer-msproject-xml-docs/blob/main/project-xml-data-interchange/task-elements-and-xml-structure.md), and [dependency types](https://github.com/MicrosoftDocs/office-developer-msproject-xml-docs/blob/main/project-xml-data-interchange/type-element-multiple-parents.md).
''')
print('Created original input, three-page brainstorming supplement, two-page evaluation protocol, blank test records and Microsoft Project XML schedule.')
