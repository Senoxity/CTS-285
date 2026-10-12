# DataMan Product Backlog
## Sources
This backlog uses these files from my repository:
- `docs/requirements.md`
- `docs/decisions/m3-backlog-triage-record.md`
- `docs/decisions/m3-product-owner-decision-record.md`
## Priority Order
List every story ID from highest priority to lowest. The story blocks below must
appear in this same order.
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
- Then the system indicates whether the answer is correct or incorrect.

**Relative Effort:** Small, describes a basic function of the program that would not require much substantial effort.
**Dependency / Constraint:** None  
**Priority:** 1  
**Readiness:** Move Forward  
**Priority Rationale:** The requirement's status as a high-value, low-effort core functionality of the system makes it a top priority. Stakeholders also require this feature for the first public release, and afford the feature very high value, as outlined in E-02.

---
### US-02 — Saved Progress Retention
**Requirement ID:** [FR-01]  
**User Story:** As a learner, I want my progress to be saved between sessions so that I don’t lose my practice progress when I leave and come back later.  
**Acceptance Criteria:**  
- Given that the user is in an authenticated session,
- When the user pauses or exits the session,
- Then the user's progress is saved, and the user's last saved practice state is restored when they return.

**Relative Effort:** Large, relies on an identity/session approach that would require a large amount of additional work/refinement.  
**Dependency / Constraint:** US-03, Q-03, NFR-01, Identity/Session approach  
**Priority:** 4  
**Readiness:** Defer  
**Priority Rationale:** Implementation of this feature requires a very high amount of effort. It's high value for stakeholders and US-03's position as a dependency allows it to hold Priority 4, but the feature cannot continue development until the Identity/Session approach is resolved.

---
### US-03 — Mid-Practice Pause Functionality
**Requirement ID:** [FR-02]  
**User Story:** As a learner, I want to be able to pause mid-practice session so that I can stop partway through and later continue from exactly where I left off.  
**Acceptance Criteria:**  
- Given that a user's practice session is currently in-progress,
- When the user selects the pause option,
- Then the session stops, and when the user resumes, they return to the exact question and state where they paused.

**Relative Effort:** Medium, relies on the identity/session approach, and implementation may cause issues to arise  
**Dependency / Constraint:** Identity/Session approach  
**Priority:** 2  
**Readiness:** Refine  
**Priority Rationale:** Since this feature unlocks development for US-02, as well as having explicit stakeholder need outlined in E-07, the feature holds a high value, but the feature can't be fully completed until this identity/session approach is resolved.

---
### US-04 — Parent/Teacher Progress Summary
**Requirement ID:** [FR-04, NFR-03]  
**User Story:** As a parent or teacher, I want a summary of the learner's progress so that I can see what they practiced, and whether practice is occurring.  
**Acceptance Criteria:**  
- Given that a learner has completed a practice session,
- When a teacher/guardian accesses the learner's account,
- Then a summary of the learner's practice session is displayed.

**Relative Effort:** Medium, requires maintenance of the learner's activity data. This data would then be displayed to the parent/guardian.  
**Dependency / Constraint:** Q-03, E-03, Identity/Session approach, Activity data.  
**Priority:** 5  
**Readiness:** Refine  
**Priority Rationale:** The amount of effort relative to what is being provided is unbalanced, due to it's position as being medium-value, but also medium-risk because of the feature's extra unresolved scope (i.e. usage of activity data, reliance on Q-03, and undefined reporting structure as outlined in E-03). This allows it to sit below US-02, despite being closer to completion.

---
### US-05 — User Attempts Monitoring
**Requirement ID:** [FR-05]  
**User Story:** As a learner, I want the ability to see how many attempts I've made, and how many attempts remain so that I know how many more attempts I can make.  
**Acceptance Criteria:**  
- Given that a learner is completing a practice problem,
- When a learner answers incorrectly,
- Then the system displays how many attempts the user has made, and how many more attempts remain on the problem.

**Relative Effort:** Small, has no dependencies and works in tandem with core features.  
**Dependency / Constraint:** None  
**Priority:** 3  
**Readiness:** Move Forward  
**Priority Rationale:** The feature's relatively low effort required to implement contrasts well with its high value among shareholders, particularly instructors.

## Open Questions Carried Forward
- **[Q-01]:** No story currently waits on this question, since it describes adding whole new features to the program, rather than describing core functionality or basic features. In other words, it currently lies outside the project scope.  
- **[Q-02]:** The behavior of the program across devices and browsers is technically a constraint on every story, but Q-02 does not block any of the stories from continuing development as it stands currently.  
- **[Q-03]:** US-04 and US-02 rely on this question being answered, since the saved progress functionality, as well as the progress summary feature require collection of user data. Knowing which database technology to use would allow developers to begin working on these features.
- **[Identity/Session Approach]:** This is being listed as an open question due to it's position as a dependency on many of the stories listed in this document, but it's undefined nature as outlined in the triage record requires refinement. The I/SA also effects E-06 from the Requirements Register.
## Revisions After Triage and Release Planning
The Backlog Triage Decision Record affected the decision-making process for some of the requirements listed above, since that record detailed a lot of functions that were laid out in the Requirements Register; a document that I used as the basis for the Product Backlog. The specific changes the Backlog Triage Decision Record made to this document are listed below:
- US-02 deferred per triage (identity/session not ready).
- US-01 held as top priority because the instructor requires it for release.
- US-04 kept at Refine.
- S3 and S6 excluded.

The Product Owner Decision Record also played a role in shaping how decisions were made about the user stories, due to the "checklist" that the document provided (the section under "Transfer to DataMan" in that record).
## Additional Notes
- While a specific outline of capacity was not laid out for the DataMan Project, as it stands currently the only requirements listed in the Product Backlog that could form the first usable release would be US-01 and US-05, due to their lack of dependencies, and high-value nature.
- Items S3 and S6 from the Backlog Triage Decision Record were deferred for the purposes of this document. Item S3 was deferred because of it's low value to the project, making it difficult to include with the other features in mind. Item S6 was deferred due to outstanding disagreements between shareholders about how a reporting dashboard would look/function. This disagreement is outlined in E-03.

