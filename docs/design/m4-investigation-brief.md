# M4 Investigation Brief

## Product Slice
US-03 — Mid-Practice Pause Functionality

## Trace to Product Work
The acceptance criteria describes the functionality as returning the user to "the exact question and state where they paused" as central to the story's functionality. Additionally, the story relies on the Identity/Session approach to function, which is a very common dependency.

## Initial Design Question
**Question type:** Data / State

What state has to persist within a practice session in order for practice data to be stored, and where in the program would that state live in order to be recalled upon unpausing?

## Why This Question Matters
Blindly coding the feature in without answering this question first would make implementation nearly impossible to complete, since how the pause functionality would be handled and where it would be handled at remains unanswered.

## Planned Evidence
- Field or state table

## Why This Evidence Is a Reasonable Starting Point
Creating a state table to model the program's practice session would help answer the questions regarding what exact state of the program is meant to be saved, and how it would be restored upon returning. However, it could not answer where the data would be stored within the program.

## Studio Check
During the DataMan Design Studio, record whether the evidence actually answered the question, whether you needed different evidence, and what new question emerged.
