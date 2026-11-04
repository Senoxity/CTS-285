# M4 Design Investigation Record

## Product Slice
US-03 — Mid-Practice Pause Functionality

## Initial Question
What state has to persist within a practice session in order for practice data to be stored, and where in the program would that state live in order to be recalled upon unpausing?

## Planned Evidence
Field or state table

## Evidence Actually Used
- Use-case boundary / actor-goal framing
- Behavior/state flow and two-attempt simulation
- Data-model/schema and Memory Bank constraint stress tests
- Interface/wireframe comparison and state audit
- Design complication and critique

## Findings
### Use-Case Boundary / Question Framing
Learner: Presses a button that pauses the active session.

Question: Exactly what data from the active session is stored, and where within the program is the data stored?

### Behavior / State
The implementation sharpened how exactly the state function works within the program, which can provide a basis for creating the pause functionality outlined earlier.

### Data / Persistence
The model showed exactly how the memory bank system works by giving visuals to help with understanding the system's function, while also updating in real time as data is modified. This allows conclusions to be made regarding implementation much easier than it would be otherwise.

### Memory Bank Constraint
The failure of the 11th addition to the set proves that the model's structure within the business logic layer is a functional design. For future implementation, the logic for rejecting the 11th problem must lie in the business logic layer in order to prevent an invalid set from occurring in the data.

**Constraint boundary selected:** both

### Interaction
The interaction helped clarify that greater detail may not be required, but it is necessary if the program is meant to retain a consistent program state (and to also prevent confusing learners)

## Layer Boundary Notes
**Business behavior that should remain outside the interface:**
The state-based structure should live outside of the text interface, since it is the main part of the program that would need to be reused for other parts of the program.

**Data that can be stubbed now:**
The problem data for each of the problems in the set can be stored in memory now, and the 11th problem rule will be preserved in order to keep storage consistent.

## New Complication
**Response:** Revise state boundary

Keeping the session state outside of the interface and in memory ensures that the session is properly restored if the program were to close/end mid-session. It also ensures accurate reporting if a curator were to look at the learner's progress data.

## Build-Readiness Decision
**Disposition:** Revise

**Design decision:**
Revising the current slice is the optimal path to ensure that implementation goes smoothly due to the problems that surfaced earlier regarding session restoration.

## Revision From Initial Thinking
Nothing really changed from my initial thinking, since I had already identified the fact that the program lacked a way to restore progress if the session is interrupted.

## Tradeoff Accepted
Losing implementation time in exchange for clarifying and refining a missing feature.

## Unresolved Uncertainty
How exactly the session restoration system should be implemented.

## Next Question
How should the implementation team design and store the user's session, and how should it be restored?

## Three-Layer Prototype Bridge
Interface: input/output feedback and display, number of attempts display

Business logic: attempts logic, answer verification, and memory bank rules

Data: learner progress, previous session data, and memory bank data.

## Trace Back to Product Work
The acceptance criteria describes the functionality as returning the user to "the exact question and state where they paused" as central to the story's functionality. Additionally, the story relies on the Identity/Session approach to function, which is a very common dependency.
