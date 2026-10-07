# M3 Product Owner Decision Record

## Scenario
StudyTrack release planning under constrained capacity.

## Round 1 — Capacity 13
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-05: Weekly progress summary (4 pts)

**Why this release slice was defensible:**
The selected release slice best fits within the effort constraints of the project, without sacrificing core functionality or key features. The selected tasks best represent what StudyTask should be able to do on release.

**One intentional deferral and why:**
Deferred Custom Color Themes (ST-06) due to low value. The effort required to include the task does not accurately reflect the value it would bring to StudyTask.

## Complication
Capacity dropped from 13 to 10 points. Keyboard accessibility testing revealed that task entry cannot reliably be completed with keyboard navigation, so ST-04 became release-critical.

## Revised Release Slice — Capacity 10
- ST-01: Create a study task (3 pts)
- ST-02: Mark a study task complete (2 pts)
- ST-03: Recover a missed task (3 pts)
- ST-04: Keyboard-accessible task entry (2 pts)

### Removed after complication
- ST-05: Weekly progress summary

### Added after complication
- ST-04: Keyboard-accessible task entry

**What changed and why:**
Item ST-05 was deferred and replaced with Item ST-04. The complication revealed that users that require keyboard functionality were being left out, and the new effort budget being lower provided exactly the amount of points to fit in keyboard accessibility.

**Tradeoff accepted:**
Losing the insight that having a weekly summary would give is a viable tradeoff when the other option is alienating users with specific needs. Additionally, the complication described the inclusion of keyboard accessibility features as being paramount to the product's release.

## Transfer to DataMan
Before finalizing your DataMan backlog, review whether any item is high value but not ready, depends on unresolved work, consumes disproportionate effort, or should move because it reduces risk or unlocks other work.

