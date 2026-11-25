# README_tests.md

### !!! PUT ALL TESTS IN THE SAME FOLDER AS APP.PY FOR THEM TO WORK !!!

Info about other tests included below, as written by Claude.

## How to run them and see the output

From that folder, run:

python -m pytest -v -s test_answer_checker.py test_memory_bank.py

-v lists every test by name with PASSED or FAILED. -s lets the print() lines inside the tests show, so each test also displays what actually happened. For example:

test_answer_checker.py::test_two_wrong_answers_reveal_the_answer
  submit(50), submit(51) -> Outcome(status='reveal', try_number=2, revealed_answer=56)
PASSED

The run ends with 25 passed.

## What the tests cover

### test_answer_checker.py (15 tests):

- A new session starts with no attempts.
- A correct answer on the first try, and on the second.
- A wrong first answer allows a retry.
- Two wrong answers reveal the answer.
- No third try after two wrong answers, and no more answers after a correct one.
- Every attempt is recorded.
- The five curator labels: not attempted, first-try success, second-try success, two misses and in progress.
- Two sessions don’t share attempts.
- Attempts survive a restart with the JSON store.

### test_memory_bank.py (10 tests):

- A new set is empty.
- Adding a problem, and members keeping the order they were added.
- Adding the same problem twice is ignored.
- Ten problems fit and the eleventh is refused with SetFull.
- Re-adding an existing member of a full set is not an error.
- Two sets don’t share members.
- Changing the returned list doesn’t change the set.
- The set survives a restart with the JSON store, including a check of what’s written in the file.

The tests that use the JSON store write to a throwaway folder, so they never touch your real dataman_store.json.

## Don’t run plain pytest

Typing just pytest also collects exercise/test_bank.py, which is a separate template exercise with its own MemoryBank. That test fails on purpose until its missing rule is added. It isn’t related to your code or my tests. Naming the two files, as in the command above, avoids it.