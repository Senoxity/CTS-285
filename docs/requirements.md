# DataMan Requirements Register
> Replace all bracketed prompts with your own project evidence and requirements. Delete the prompts before submitting.
## Project Context
The DataMan Project is intended to bring a modern spin on the legacy calculator by the same name. The project seeks to rebuild the different functions of the original DataMan calculator in order to make practicing simple math concepts more fun and engaging for students. The program is meant to be used by both students and teachers, both for practicing basic math concepts, and tracking the user's progress as they do so.

## Evidence Notes
- **E-01 — Source:** M2 Eliciation Decision Record  
  **Evidence:**  Stakeholders say modern means the experience should work reliably in a browser, be understandable without a printed manual, and avoid making the learner navigate unnecessary screens. They do not specify a visual style or framework.

- **E-02 — Source:** M2 Eliciation Decision Record  
  **Evidence:** Stakeholders identify immediate answer feedback, repeated practice after an incorrect response, and a clear way for learners to see progress as central to the original experience.

- **E-03 — Source:** M2 Eliciation Decision Record  
  **Evidence:** Adults want to understand what the learner practiced and whether progress is occurring, but stakeholders have not yet agreed on a detailed reporting dashboard.

- **E-04 — Source:** Original DataMan Manual
  **Evidence:** The program is intended to focus on practicing basic math concepts; it was not meant for testing purposes.
  
[Add additional evidence notes if needed.]

## Functional Requirements
Write at least four functional requirements. Each requirement should describe a capability or behavior the system must provide.
### FR-01
**Requirement:** The system must preserve a learner's saved practice progress between authenticated sessions.  
**Source/Rationale:** Stakeholder need for a progress-saving system is evident throughout multiple sources. An exact record of this need is, “Students keep losing their practice progress when they leave and return later.”

### FR-02
**Requirement:** The system must be fully compatible with multiple types of viewports for ease of use.   
**Source/Rationale:** Pre-determined stakeholder need for the program to be easily accessible was defined in E-01. 

### FR-03
**Requirement:** The system must give immediate feedback when the user enters a math problem, solution, or number guess.
**Source/Rationale:** Requirement describes the original behavior of the Answer Checker, Memory Bank, and Number Guesser.

### FR-04
**Requirement:** The system must display the learner's progress in an easy-to-read format that is easily accessible by Parents or Instructors.  
**Source/Rationale:** Learner progress tracking was an established Stakeholder need in E-03.

### FR-05
**Requirement:** The system must clearly display the number of attempts the user has made on a problem, as well as how many attempts remain.
**Source/Rationale:** Stakeholder and instructor concern over learners giving up or simply guessing their way through problems has made this requirement tantamount to ensuring learners stay engaged and focused.

## Non-Functional Requirements
Write at least three non-functional requirements. Each requirement should describe a measurable quality, constraint, or condition the system must satisfy.

### NFR-01
**Requirement:** The system must be available to all users from 7:00AM to 7:00PM, Monday through Friday, except for maintainence hours/days.  
**Source/Rationale:** The system must be available during these times in order to be utilized by learners during school hours.

### NFR-02
**Requirement:** The system must maintain a visual style similar in theme to the original DataMan calculator from 1977.
**Source/Rationale:** Brand identity is important to the project if its purpose is to revive an existing program.

### NFR-03
**Requirement:** The system must maintain an intuitive and easy-to-use format for both learners and guardians.
**Source/Rationale:** M2 Elicitation Record cites stakeholder need for a "modern" version of DataMan. Stakeholder's definition of "modern" in this context describes 

[Add additional non-functional requirements if needed.]

## Open Questions / Assumptions
Do not turn an unsupported idea into a confirmed requirement. Record unresolved items here until evidence supports a decision.

- **Q-01:** [What still needs to be clarified or confirmed?]
- **Q-02:** [What still needs to be clarified or confirmed?]

[Add or remove items as appropriate.]
## Final Quality Check

Before submitting, confirm that each requirement is:

- [ ] Clear enough for another team member to interpret consistently.
- [ ] Supported by evidence, a stakeholder need, or a confirmed project constraint.
- [ ] Testable or verifiable later.
- [ ] Solution-neutral enough for this stage of the project.
- [ ] Focused on one main capability or quality.
- [ ] Classified correctly as functional or non-functional.

Also confirm:

- [ ] At least four functional requirements are included.
- [ ] At least three non-functional requirements are included.
- [ ] Every confirmed requirement has a source/rationale.
- [ ] Open questions and assumptions are separated from confirmed requirements.
- [ ] The simulation decision record is saved at `docs/decisions/m2-elicitation-decision-record.md`.
- [ ] This file is saved as `docs/requirements.md`, committed, and synced to GitHub.
