# DataMan Product Backlog
## Sources
This backlog uses these files from my repository:
- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`
## Priority Order
1. [US-01]
2. [US-03]
3. [US-05]
4. [US-02]
5. [US-04]
## Stories
### US-01 — Immediate User Feedback
**Requirement ID:** [FR-03]  
**User Story:** As a learner, I want immediate answer feedback upon entering an input so that I know whether to continue or try again.  
**Acceptance Criteria:**
- Given that the user is answering a problem,
- When the user enters an input into the program (i.e. problem, solution, number guess),
- Then the system indicates correct or incorrect immediately, without further action from the user.

**Relative Effort:** Small, describes a basic function of the program that would only require input-checking and a displayed result.  
**Dependency / Constraint:** None  
**Priority:** 1  
**Readiness:** Move Forward  
**Priority Rationale:** The requirement's status as a high-value, low-effort, low risk core functionality of the system makes it a top priority. Stakeholders also require this feature for the first public release, and afford the feature very high value, as outlined in the Backlog Triage Decision Record.

---
### US-03 — Mid-Practice Pause Functionality
**Requirement ID:** [FR-02]  
**User Story:** As a learner, I want to be able to pause mid-practice session so that I can stop partway through and later continue from exactly where I left off.  
**Acceptance Criteria:**  
- Given that a user's practice session is currently in-progress,
- When the user selects the pause option,
- Then the session stops, and when the user resumes, they return to the exact question and state where they paused.

**Relative Effort:** Medium, must capture and restore the exact question state; restoring after exit also needs the identity/session approach.  
**Dependency / Constraint:** Identity/Session approach  
**Priority:** 2  
**Readiness:** Refine  
**Priority Rationale:** Since this feature unlocks development for US-02, operates on a medium risk level, and has explicit stakeholder need outlined in E-07, the feature holds a high value, but the feature can't be fully completed until this identity/session approach is resolved. US-03 maintains it's position over US-05 in the priority list due to the aforementioned stakeholder need, as well as unlocking development on US-02.

---
### US-05 — User Attempts Monitoring
**Requirement ID:** [FR-05]  
**User Story:** As a learner, I want the ability to see how many attempts I’ve used and how many remain so that I stay focused on each problem instead of guessing or giving up.  
**Acceptance Criteria:**  
- Given that a learner is in a practice session,
- When the problem is presented and after each incorrect attempt,
- Then the system displays how many attempts used, and how many remain, visible on the problem screen without navigating elsewhere.

**Relative Effort:** Small, counts attempts and displays two numbers, building on US-01’s correct/incorrect result.  
**Dependency / Constraint:** US-01  
**Priority:** 3  
**Readiness:** Move Forward  
**Priority Rationale:** The feature's relatively low risk and low effort required to implement contrasts well with its high value among stakeholders, particularly instructors.

---
### US-02 — Saved Progress Retention
**Requirement ID:** [FR-01]  
**User Story:** As a learner, I want my progress to be saved between sessions so that I don’t lose my practice progress when I leave and come back later.  
**Acceptance Criteria:**  
- Given that the user has exited an authenticated session,
- When the user returns in a new authenticated session,
- Then the user's last saved practice session progress is available.

**Relative Effort:** Large, relies on an identity/session approach that would require a large amount of additional work/refinement.  
**Dependency / Constraint:** US-03, Q-03, NFR-01, Identity/Session approach  
**Priority:** 4  
**Readiness:** Defer  
**Priority Rationale:** Large effort and Medium risk, with a Deferred readiness because the identity approach is unresolved and US-03 must come first. It still ranks above US-04 because its value is High (triage S2) versus Medium for US-04. Risk level is Medium, since the dependence on other requirements makes rework potential noticeable.

---
### US-04 — Parent/Teacher Progress Summary
**Requirement ID:** [FR-04, NFR-03]  
**User Story:** As a parent or teacher, I want a summary of the learner's progress so that I can see what they practiced, and whether progress is occurring.  
**Acceptance Criteria:**  
- Given that a learner has completed a practice session,
- When a parent/teacher selects the progress option,
- Then the system displays a summary of what the learner practiced and whether progress is occurring, reachable from a clearly labeled location.

**Relative Effort:** Medium, requires maintenance of the learner's activity data. This data would then be displayed to the parent/teacher.  
**Dependency / Constraint:** Q-03, E-03, Identity/Session approach, Activity data.  
**Priority:** 5  
**Readiness:** Refine  
**Priority Rationale:** Medium value, Medium effort, Medium risk, plus extra unresolved scope: activity data, Q-03, and undefined reporting (E-03). Refinement is required if US-04 is to move forward.

## Open Questions Carried Forward
- **[Q-01]:** No story currently waits on this question, since it describes adding whole new features to the program, rather than describing core functionality or basic features.
- **[Q-02]:** The behavior of the program across operating systems is technically a constraint on every story, but Q-02 does not block any of the stories from continuing development as it stands currently.  
- **[Q-03]:** US-04 and US-02 rely on this question being answered, since the saved progress functionality, as well as the progress summary feature require collection of user data. Knowing which database technology to use would allow developers to begin working on these features.
- **[Identity/Session Approach]:** Originating from the Backlog Triage Decision Record, this is being listed as an open question due to its position as a dependency on US-02, US-03, and US-04, but it's undefined nature as outlined in the triage record requires refinement. The Identity/Session Approach also affects E-06 and NFR-01 from the Requirements Register.
## Revisions After Triage and Release Planning
The Backlog Triage Decision Record affected the decision-making process for some of the requirements listed above, since that record detailed a lot of functions that were laid out in the Requirements Register; a document that I used as the basis for the Product Backlog. The specific changes the Backlog Triage Decision Record made to this document are listed below:
- US-02 deferred per triage (identity/session not ready).
- US-01 held as top priority because the instructor requires it for release.
- US-04 kept at Refine.
- S3 and S6 excluded.

The Product Owner Decision Record also played a role in shaping how decisions were made about the user stories, due to the "checklist" that the document provided (the section under "Transfer to DataMan" in that record). Specific examples include:
- High Value but Not Ready: US-02, US-03
- Depends on Unresolved Work: US-02, US-03, US-04
- Disproportionate Effort: US-02
- Unlocks Other Work: US-03

## Additional Notes
- Triage Numbers Resolution:
  - S1 = US-01
  - S2 = US-02
  - S4 = US-04
- US-03 and US-05 have no triage counterpart.
- While a specific outline of capacity was not laid out for the DataMan Project, as it stands currently the only requirements listed in the Product Backlog that could form the first usable release would be US-01 (no dependencies) and US-05 (depends only on US-01).
- Items S3 and S6 from the Backlog Triage Decision Record were excluded for the purposes of this document. Item S3 was deferred because of its low value to the project, and E-01 stating that stakeholders gave no visual style for the DataMan Project. Item S6 was excluded from this backlog due to outstanding disagreements between stakeholders about how a reporting dashboard would look/function. This disagreement is outlined in E-03.
- The functionality for repeated practice after an incorrect answer is described by item S5 in the Backlog Triage Decision Record, and by E-02 in the Requirements Register. This behavior is being covered by US-01.
- E-06 describes an issue regarding premature logout for mobile users. This will be treated as a potential risk for US-02.
- US-03 is set to "refine" due to the identity dependency, which according to the Backlog Triage Decision Record, is not yet complete.

