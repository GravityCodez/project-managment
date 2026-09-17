# ClassMic Product Requirements Document

Status: proposed for team and instructor review. No approval or test result is implied.

## Context and objective

ClassMic tests whether a student phone can make a question easier to hear through a room speaker while the instructor controls speaking turns. The course project covers five user stories in two weekly sprints, followed by evaluation and closing. A live classroom pilot needs a separate decision.

## Target users

- Student speaker: wants to request a turn and be heard without installing a new app.
- Student listener: wants to hear the question clearly.
- Instructor: wants to approve, mute and end speaking without losing control of the class.
- Project manager: needs acceptance results and feedback to support a recommendation.

These are provisional role descriptions, not interview-based personas.

## Requirements and user stories

Import ClassMic_Notion_Requirements.csv as a Notion database. It has the eight fields required by the lab. Keep the requirement ID at the start of Feature/Requirement. Add links to actual evidence and test results after import. Keep Status as Proposed until the appropriate review occurs.

### R1 Temporary browser session and QR or code join

As a student, I want to join a temporary room session without installing an app so that I can participate quickly.

Priority: Must. Charter objectives: O1; O2; O4. Planned sprint: 1.

Acceptance criteria: A valid code joins the correct session. An expired or ended session rejects joining. Denying microphone permission leaves the interface usable. At least 9 of 10 timed setup trials finish within 2 minutes.

Evidence basis: ClassMic in-class SMART note; prior ClassMic charter.

### R2 Speaking queue with approval, mute, removal and end controls

As an instructor, I want to choose and stop speakers so that I can manage classroom discussion.

Priority: Must. Charter objectives: O1; O4. Planned sprint: 1 and 2.

Acceptance criteria: One request appears once in the queue. Only the approved student may transmit. Mute, removal, timeout and end session stop transmission. Concurrent requests never create two active speakers. All control and misuse checks pass.

Evidence basis: ClassMic in-class SMART note; prior ClassMic charter.

### R3 One approved phone transmits to a laptop and connected speaker

As a student, I want to speak through my phone after approval so that other people in the room can hear my question.

Priority: Must. Charter objectives: O1; O2; O3; O4. Planned sprint: 2.

Acceptance criteria: Microphone notice and permission precede capture. Audio transmits only during approved push to talk and stops on release or revocation. At least 27 of 30 scripted trials become audible within 3 seconds of approval when the tester is ready to speak. Report median and 95th percentile transport delay separately. No sustained feedback is acceptable.

Evidence basis: ClassMic SMART note; prior charter; technical feasibility still untested.

### R4 Clear permission, connection and alternative participation paths

As a participant who cannot use a phone microphone, I want another way to contribute so that I am not excluded.

Priority: Must. Charter objectives: O1; O4. Planned sprint: 1 and 2.

Acceptance criteria: Permission denial and disconnection show a clear next step. The instructor can repeat a question or provide an available physical microphone. Keyboard navigation and readable control labels pass the agreed review. Rejoining never restores a previous speaking approval.

Evidence basis: Prior ClassMic charter and plan; user validation pending.

### R5 Test record and anonymous feedback without stored speech

As the project manager, I want a record of test outcomes and feedback so that I can recommend whether further testing is worthwhile.

Priority: Must. Charter objectives: O1; O2; O3; O4. Planned sprint: 2.

Acceptance criteria: The report covers every Must check, 10 setup trials, 30 speaking trials and feedback from at least 5 volunteers. At least 75% report easier audibility. Save results and minimal test metadata only. Report failures, sample limits and open defects. No audio or transcript is saved.

Evidence basis: ClassMic SMART note and prior charter; sample sizes proposed for course feasibility.

## Priorities and exclusions

R1–R5 are Must. Simple connection checks and a short guide are Should refinements. Visual polish is Could. Recording, saved transcripts, permanent profiles, grading, attendance, captions, polling, simultaneous speakers, remote participation and live campus deployment are excluded.

## Charter objectives

O1: five priority stories and all Must checks, with no open critical defect.
O2: 9/10 setup trials within two minutes and 27/30 ready-speaker activation trials audible within three seconds of approval.
O3: at least 75% positive audibility feedback from at least five willing reviewers, with counts and sample limitations.
O4: no unauthorized transmission in misuse tests, no saved speech and an alternative speaking route.

## Open questions

Confirm the revised A2/B2/C1 and the course instructor’s role. Confirm early D review and sprint dates. Validate the audibility problem and instructor workflow. Confirm devices, room access if needed, volunteer reviewers, acceptable transport delay and minimal test-data handling. Confirm team capacity and the Notion page’s access settings. Supply genuine human evidence required by C1, D3 and D6.

## Review and maintenance

Nurtore maintains priorities and decisions. Temiko maintains implementation status and technical evidence. The team reviews the PRD at each sprint review. Material scope or schedule changes go to the course instructor. Record approval only when the review actually occurs. Save an export at each milestone.
