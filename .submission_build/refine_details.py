from pathlib import Path
import json

ROOT = Path('/Users/gravitycodez/Desktop/Project managment')
path = ROOT / '.submission_build/build_submission.py'
s = path.read_text()

changes = {
    'Confirm these role assignments.': 'These are the selected planning roles.',
    'Name and approval remain to be confirmed.': 'Formal course acceptance remains open.',
    'The team must confirm these estimates.': 'Use these as the planning baseline and check actual capacity before each sprint.',
    'Confirm device access and an acceptable audio-delay threshold before testing.': 'Check device access before testing. The selected one-way audio-delay target is a 95th percentile of no more than 150 milliseconds.',
    'Confirm the revised aspiration with the team and course instructor, gather local examples of the audibility problem, and agree on volunteer testing.': 'Use the revised aspiration as the working direction. Gather local audibility examples and request the course review before development.',
    'The acceptable delay threshold requires AV or instructor confirmation.': 'The selected prototype target is a 95th percentile one-way delay of no more than 150 milliseconds.',
    'The proposed sequence requires early D review and permission to start E work before its upload area opens.': 'The plan schedules D review by 19 September. The E upload opening date does not state a restriction on starting work.',
    'Proposed course sponsor and acceptance authority: the course instructor, whose name and acceptance of this role require confirmation.': 'Course acceptance authority: the BUS 2010 instructor. Formal charter approval and the named sponsor record remain open.',
    'Proposed project manager: Nurtore Arynuruly. Proposed technical lead: Temiko Machavariani.': 'Planning roles: Nurtore Arynuruly is project manager. Temiko Machavariani is technical lead.',
    '2. Confirm early D review, sprint dates, available effort, equipment, volunteers, audio-delay threshold and the test-data handling plan.': '2. Confirm formal D review by 19 September, equipment access and volunteer availability. The plan defines the test protocol, delay target and data handling.',
    '3. Provide the required genuine charter brainstorming images or confirm that the instructor accepts the separately submitted evidence. Individual student inputs are handled separately at the team’s request.': '3. Add genuine team discussion images and any missing individual input. Temiko’s supplied SMART note and an AI-assisted brainstorming proposal accompany this charter; neither claims a completed group meeting.',
    'Confirm permission to begin construction before the E upload area opens on 26 September.': 'The E upload area opens on 26 September; its opening date does not prohibit earlier work.',
    'Report median and 95th percentile transport delay separately.': 'Report median and 95th percentile one-way audio delay separately. The 95th percentile must not exceed 150 milliseconds.',
    'Report median and 95th percentile transport delay separately. Test for intelligibility and sustained feedback. Obtain an agreed delay threshold before acceptance.': 'Measure 30 one-way delay trials; report median and 95th percentile, with the latter at most 150 ms. Speech must remain intelligible without sustained feedback.',
    'Obtain an agreed delay threshold before acceptance.': 'Apply the 150 ms target and record any failure.',
    'Team-chosen channel to confirm. Nurtore keeps the action log.': 'Telegram for daily coordination; Notion for decisions. Nurtore keeps the action log.',
    'Course-approved channel to confirm. Nurtore prepares the decision request.': 'LMS messaging or the next class review. Nurtore prepares the decision request.',
    'Brief check-in on workdays and a weekly plan review.': 'Ten-minute check-in on workdays; a 30-minute review at each sprint boundary.',
    'Short review and anonymous response form. Nurtore records results.': 'Use the supplied anonymous review form after a controlled demonstration. Nurtore records results.',
    'Review ratings and agree on the audio-delay threshold.': 'Track the risk triggers and apply the selected 150 ms delay target.',
    'Team and instructor confirm the rescope.': 'Use the course prototype as the working scope; obtain formal course acceptance.',
    'Confirm early start and each person’s availability.': 'Complete D review by 19 September and check available effort at sprint planning.',
    'agree on the audio-delay threshold and handling of minimal test data': 'apply the selected delay target and test-data protocol',
    'Agree on the audio-delay threshold and handling of minimal test data.': 'Use the selected 150 ms delay target and the supplied test-data protocol.',
    'Confirm the revised course scope, reviewer, 100-hour effort assumption and proposed sprint dates.': 'The selected baseline is five stories, 100 student hours and the two listed sprint dates. Formal course review and actual resource availability remain open.',
    'Confirm the revised A2/B2/C1 and the course instructor’s role. Confirm early D review and sprint dates. Validate the audibility problem and instructor workflow. Confirm devices, room access if needed, volunteer reviewers, acceptable transport delay and minimal test-data handling. Confirm team capacity and the Notion page’s access settings. Supply genuine human evidence required by C1, D3 and D6.': 'Obtain formal course acceptance of A2/B2/C1 and D review by 19 September. Validate the audibility problem and instructor workflow. Check devices, any room access and volunteer availability. The selected test target is 95th percentile one-way delay of no more than 150 milliseconds; retain only the minimal records specified in the evaluation protocol. Add the Notion link and genuine human evidence required by C1, D3 and D6.',
    'The D6 brief asks for communication brainstorming written before AI prompting. That original human input is still required. The plan above is a proposal for the team to review, not a record of a completed brainstorming session.': 'The companion brainstorming supplement explains the selected communication plan. It is AI-assisted planning prepared now. The D6 request for original pre-AI human notes remains open; this supplement does not claim to recreate those notes.',
    'The prototype saves no audio or transcripts and retains only agreed test results.': 'The prototype saves no audio or transcripts. Keep anonymous test counts, timings and defect records until 30 days after course feedback, then delete participant-level records.',
}
for old, new in changes.items():
    if old not in s:
        print('No exact match:', old[:85])
    else:
        s = s.replace(old, new)

# Required source images remain evidence, and the supplement has a separate provenance label.
s = s.replace("'A2 B2 and charter review'", "'A2, B2 and charter review'")
s = s.replace("'Requirements used for this revision'", "'Requirements used for this revision'")
path.write_text(s)

sp = ROOT / '.submission_build/build_slides.mjs'
t = sp.read_text()
slide_changes = {
    'The team must confirm capacity and responsibilities.': 'Use these planning roles and check capacity at sprint planning.',
    'Role assignments and reviewer participation require confirmation.': 'Planning roles are selected. Reviewer participation and course acceptance remain open.',
    'Measure transport delay separately. Confirm an acceptable threshold before audio acceptance.': 'Separate one-way audio-delay target: 95th percentile at most 150 ms.',
    'Confirm early D review and permission to start construction before the E upload area opens.': 'D review is planned for 19 September. The E opening date controls uploads.',
    'Targets and approvals require confirmation. Report transport delay separately from speaking activation.': 'Selected one-way delay target: 95th percentile at most 150 ms. Formal course acceptance remains open.',
    'Two weekly construction sprints. The proposed early start needs instructor confirmation.': 'Two weekly construction sprints, after the planned D review on 19 September.',
    'Proposed responsibilities': 'Planning responsibilities',
    'A2/B2/C1 approval, roles, dates, audio threshold and genuine brainstorming evidence. Individual inputs are handled separately.': 'Formal course approval and genuine team evidence. Temiko’s original note and an AI-assisted brainstorming proposal are included.',
    'an acceptance threshold requiring confirmation': 'a selected 95th percentile target of 150 milliseconds',
    'a threshold awaiting confirmation': 'a selected 95th percentile target of 150 milliseconds',
    'Proposed early D review and construction dates require instructor confirmation.': 'D review is scheduled for 19 September. The upload opening date does not state a restriction on earlier work.',
    'and instructor permission to start E construction before the upload area opens on 26 September': 'before the two build sprints; the E upload area opens on 26 September',
    'Individual input is handled separately at the user request.': 'The package includes Temiko’s original SMART note and a separately labelled AI-assisted brainstorming proposal. No group meeting or another student’s input is invented.',
    'Role assignments, named instructor and technical reviewer participation require confirmation.': 'Planning roles are selected. Formal course acceptance and technical reviewer participation remain open.',
}
for old, new in slide_changes.items():
    if old not in t: print('Slide no exact match:', old[:85])
    else: t = t.replace(old, new)
t = t.replace("const finalPath=path.join(root,'ClassMic_Submission',item.folder,`ClassMic_${item.key}_Three_Slides.pptx`);", "const finalPath=path.join(build,`ClassMic_${item.key}_Three_Slides_revised.pptx`);")
sp.write_text(t)
print('Updated document and slide authoring sources.')
