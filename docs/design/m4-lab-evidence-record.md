# M4 Lab Evidence Record

## Answer Flow Lab
**Initial design decision tested:** Persistence across interruption/reload

**Scenario that exposed the issue:** Interruption or reload between attempts

### Consequence Observed
This may be because I repeatedly pressed the buttons on the calculator interface after the flow had completed, but it would appear that the flow does not properly terminate after revealing the incorrect answer. I kept entering numbers, it would count them wrong, and would reveal the correct answer, even though the flow had completed. This includes when the program is reloaded.

### Revision Made
I changed the interruption protection decision to "Current session only in interface memory" to see if changing how the information is saved upon interruption would fix the issue described above.

### What Changed After Revision
After changing the interruption protection decision, the issue was *technically* solved, since the program now resets when the answer flow is completed, but this change instead created a new issue, that being that after an interruption, the program no longer saves the required evidence that it did before.

---

## Memory Bank & Curator Retrieval Lab
**Initial design decision tested:** Ten-problem limit enforcement

**Scenario that exposed the issue:** Attempt to add an 11th problem

### Consequence Observed
The stress test revealed that the 11th problem rule is properly enforced if more than 1 extra attempt at adding a problem is created, since trying to enter P12 still results in a rejection, instead of letting it in. This was to make sure that the program wasn't specifically blocking out Problem 11, but rather all problems above 10.

### Revision Made
No revision was made to the program since all of the required tests were passed on the first configuration, and the relationship described above does not require revision.

### What Changed After Revision
N/A

---

## Cross-Lab Finding
Both of the tests described above would not have been able to be discovered without actually testing the program, and instead simply reading the requirements for the program, since both describe the direct behavior of the program--one instance of it working properly, and one where some ironing out needs to be done.

## Revised / New Design Question
With the answer flow and memory bank features ironed out, the next main question that requires answering regards the pause functionality that I described in my product backlog. Particularly, how exactly the program state will be saved and restored is extremely important to implementing the feature in the final design.
