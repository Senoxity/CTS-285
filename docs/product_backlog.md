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
3. [US-02]
4. [US-04]
## Stories
<!-- Copy one story block for each story. Do not change the field labels. -->
### US-01 — Immediate User Feedback
**Requirement ID:** [FR-03]
**User Story:** As a learner, I want immediate answer feedback upon entering an input so that I know whether to continue or try again.
**Acceptance Criteria:**
- Given that the user is answering a problem,
- When the user enters an input into the program,
- Then the system provides immediate answer feedback to the user.
**Relative Effort:** Small, describes basic core functionality of the system.
**Dependency / Constraint:** None
**Priority:** 1
**Readiness:** Move Forward
**Priority Rationale:** The requirement's status as a high-value, low-effort core functionality of the system makes it a top priority for developers.
---
### US-02 — Saved Progress Retention
**Requirement ID:** [FR-01]
**User Story:** As a learner, I want my progress to be saved between sessions so that I can easily pause or resume working.
**Acceptance Criteria:**
- Given that the user is in an authenticated session,
- When the user pauses or exits the session,
- Then the user's progress is saved, and restored when they return.
**Relative Effort:** Large, relies on an identity/session approach that would require a large amount of additional work/refinement.
**Dependency / Constraint:** US-03, Identity/Session approach
**Priority:** 3
**Readiness:** Move Forward
**Priority Rationale:** Despite the very high amount of effort required to supplement the feature, overwhelming stakeholder need and incredibly high value has made the feature's inclusion a high-priority one.
---
### US-03 — Mid-Practice Pause Functionality
**Requirement ID:** [FR-02]
**User Story:** As a learner, I want to be able to pause mid-practice session so that I can save my practice progress for later.
**Acceptance Criteria:**
- Given that a user's practice session is currently in-progress,
- When the user presses the pause button,
- Then the practice session is stopped, and is resumed when the user returns, or after the session is exited.
**Relative Effort:** Medium, relies on the identity/session approach, but implementation would not require much effort.
**Dependency / Constraint:** Identity/Session approach
**Priority:** 2
**Readiness:** Move Forward
**Priority Rationale:** Stakeholder need establishes this feature as a high-priority feature. The feature's middling required effort and status as a dependency for US-02 makes rolling the feature out important for core functionality.
---
### US-04 — Parent/Teacher Progress Summary
**Requirement ID:** [FR-04, NFR-03]
**User Story:** As a guardian, I want a summary of the learner's progress so that I can help them with practice and monitor their activity.
**Acceptance Criteria:**
- Given that a learner has completed a practice session,
- When a teacher/guardian accesses the learner's account,
- Then a summary of the learner's practice session is displayed.
**Relative Effort:** Medium, requires maintenance of the learner's activity data. This data would then be displayed to the parent/guardian.
**Dependency / Constraint:** Identity/Session approach, Activity data, as well as stakeholder uncertainty
**Priority:** 4
**Readiness:** Refine
**Priority Rationale:** The amount of effort relative to what is being provided is relatively unbalanced, due to the number of constraints and dependencies. Stakeholder uncertainty about exactly what data to display also plays a role in this requirement's low priority rating.

## Open Questions Carried Forward
List each open question or assumption from `docs/requirements.md` that affects this
backlog. Do not turn an unresolved question into a confirmed story.
- **[Q-01]:** No story current waits on this question, since it describes adding whole new features to the program, rather than describing core functionality or basic features. In other words, it currently lies outside the project scope.
- **[Q-02]:** No story current waits on this question, due to the fact that stakeholders have not yet confirmed whether or not the program is intended to be used on different operating systems.
- **[Q-03]:** US-04 relies on this question being answered, since the progress summary requires collection of user data. Knowing which database technology to use would allow developers to begin working on creating the progress summary.
## Revisions After Triage and Release Planning
The Backlog Triage Decision Record greatly effected the decision-making process for some of the requirements listed above, since that record detailed a lot of functions that were laid out in the Requirements Register; a document that I used as the basis for the Product Backlog. No revisions based on the Backlog Triage Decision Record and the Product Owner Decision Record were made, since this document was created after the completion of those two records.

