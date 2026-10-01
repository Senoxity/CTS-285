# DataMan Requirements Register

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

- **E-05 — Source:** M2.3 DataMan Elicitation Case  
  **Evidence:** Instructors and Stakeholder cite concerns over user engagement, saying that learners are prone to guessing or giving up after repeated attempts on the same problem.

- **E-06 — Source:** M2 Elicitation Decision Record  
  **Evidence:** A complication arose in which Stakeholders raised concern over students being logged out prematurely when using the program on a mobile device.

- **E-07 — Source:** M2 Simulation  
  **Evidence:** Teachers report that students may pause practice and return later. They want a learner’s saved practice state to remain available after leaving and returning to the application.

- **E-08 — Source:** customer_vn.html (AKA Elicitation VN Scene)  
  **Evidence:** Stakeholders report that DataMan would be used in a classroom setting, with other learners present and actively using the program as well. This information is provided by the learner present in the scene.
  

## Functional Requirements

### FR-01
**Requirement:** The system must preserve a learner's saved practice progress between authenticated sessions.    
**Source/Rationale:** Stakeholder need for a progress-saving system is evident throughout multiple sources. An exact record of this need is, “Students keep losing their practice progress when they leave and return later.”

### FR-02
**Requirement:** The system must give users the option to pause the program mid-practice, and return to the practice session at the exact point they paused at.  
**Source/Rationale:** Pausing the program and returning in the same state was an established stakeholder need in E-07.

### FR-03
**Requirement:** The system must give immediate feedback when the user enters a math problem, solution, or number guess.  
**Source/Rationale:** Requirement describes the original behavior of the Answer Checker, Memory Bank, and Number Guesser.

### FR-04
**Requirement:** The system must display the learner's progress in a format that can be accessed by Parents or Instructors.    
**Source/Rationale:** Learner progress tracking was an established Stakeholder need in E-03.

### FR-05
**Requirement:** The system must clearly display the number of attempts the user has made on a problem, as well as how many attempts remain.  
**Source/Rationale:** Stakeholder and instructor concern over learners giving up or simply guessing their way through problems has made this requirement tantamount to ensuring learners stay engaged and focused.

## Non-Functional Requirements

### NFR-01
**Requirement:** The system must remain functional on multiple types of devices.  
**Source/Rationale:** This requirement is meant to rectify the complication that arose in the Decision Record, as outlined in E-06.

### NFR-02
**Requirement:** The system must support at least 100 simultaneous users without noticeable performance degradation.  
**Source/Rationale:** M2 Simulation (E-08) describes the usage of the DataMan program in a classroom setting, where excessive internet traffic is expected. The program must be functional under these conditions.

### NFR-03
**Requirement:** The system must maintain a clearly labeled and consistent interface for both learners and guardians to access core functions, and review progress.  
**Source/Rationale:** M2 Elicitation Record cites stakeholder need for a "modern" version of DataMan. Stakeholder's definition of "modern" in this context describes the need for the program to be "understandable without a manual". 


## Open Questions / Assumptions

- **Q-01:** Stakeholders have not identified whether or not other features of the original calculator (i.e. Electro Flash, Wipe Out, Force Out, etc.) are also meant to be preserved.
- **Q-02:** Compatibility of the program between operating systems (i.e. Windows, Chrome OS, Linux, etc.) is not directly listed as a requirement, but it is implied.
- **Q-03:** Preferred database technology for saving user progress was never outlined by stakeholders. "DataMan Requirement Repair Lab" implies the usage of SQLite, but this is inconclusive.
