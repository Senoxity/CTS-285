"""Tests for the answer checker (PracticeSession in dataman/logic.py).

Run from the folder that contains app.py:
    python -m pytest -v -s test_answer_checker.py
(-v lists each test by name; -s lets the print() lines below show up.)
"""
import pytest

from dataman.logic import (AttemptsExhausted, PracticeSession, Problem,
                           result_label)
from dataman.store import JsonFileStore, MemoryStore

PROBLEM = Problem("P1", "7 x 8", 56)   # right answer: 56
SESSION_ID = "test-learner"


@pytest.fixture
def session():
    """A brand-new session on an empty in-memory store (a fresh one per test)."""
    return PracticeSession(MemoryStore(), SESSION_ID, PROBLEM)


def test_new_session_starts_empty(session):
    print(f"\n  attempts={session.attempts()} finished={session.is_finished()} "
          f"next_try={session.next_try()}")
    assert session.attempts() == []
    assert not session.is_finished()
    assert session.next_try() == 1


def test_correct_answer_on_first_try(session):
    out = session.submit(56)
    print(f"\n  submit(56) -> {out}")
    assert out.status == "correct"
    assert out.try_number == 1
    assert out.revealed_answer is None
    assert session.is_finished()


def test_wrong_first_answer_allows_a_retry(session):
    out = session.submit(50)
    print(f"\n  submit(50) -> {out}")
    assert out.status == "retry"
    assert out.try_number == 1
    assert out.revealed_answer is None
    assert not session.is_finished()
    assert session.next_try() == 2


def test_correct_answer_on_second_try(session):
    session.submit(50)
    out = session.submit(56)
    print(f"\n  submit(50), submit(56) -> {out}")
    assert out.status == "correct"
    assert out.try_number == 2
    assert session.is_finished()


def test_two_wrong_answers_reveal_the_answer(session):
    session.submit(50)
    out = session.submit(51)
    print(f"\n  submit(50), submit(51) -> {out}")
    assert out.status == "reveal"
    assert out.try_number == 2
    assert out.revealed_answer == 56
    assert session.is_finished()


def test_no_third_try_after_two_wrong_answers(session):
    session.submit(50)
    session.submit(51)
    with pytest.raises(AttemptsExhausted):
        session.submit(56)
    print(f"\n  third submit refused; attempts kept = {len(session.attempts())}")
    assert len(session.attempts()) == 2     # the refused answer was not saved


def test_no_more_answers_after_a_correct_one(session):
    session.submit(56)
    with pytest.raises(AttemptsExhausted):
        session.submit(56)
    print(f"\n  extra submit refused; attempts kept = {len(session.attempts())}")
    assert len(session.attempts()) == 1


def test_every_attempt_is_recorded(session):
    session.submit(50)
    session.submit(56)
    rows = session.attempts()
    print(f"\n  recorded attempts: {rows}")
    assert [r["try"] for r in rows] == [1, 2]
    assert [r["answer"] for r in rows] == [50, 56]
    assert [r["correct"] for r in rows] == [False, True]


@pytest.mark.parametrize("answers, expected_label", [
    ([], "not attempted"),
    ([56], "first-try success"),
    ([50, 56], "second-try success"),
    ([50, 51], "two misses"),
    ([50], "in progress"),
])
def test_result_label_tells_the_outcomes_apart(session, answers, expected_label):
    for a in answers:
        session.submit(a)
    label = result_label(session.attempts())
    print(f"\n  answers={answers} -> label={label!r}")
    assert label == expected_label


def test_two_sessions_do_not_share_attempts():
    store = MemoryStore()
    one = PracticeSession(store, "learner-1", PROBLEM)
    two = PracticeSession(store, "learner-2", PROBLEM)
    one.submit(56)
    print(f"\n  learner-1 finished={one.is_finished()}, "
          f"learner-2 finished={two.is_finished()}")
    assert one.is_finished()
    assert not two.is_finished()
    assert two.next_try() == 1


def test_attempts_survive_a_restart_with_the_json_store(tmp_path):
    path = tmp_path / "store.json"      # tmp_path is a throwaway folder
    first_run = PracticeSession(JsonFileStore(path), SESSION_ID, PROBLEM)
    first_run.submit(50)

    # A brand-new store object reading the same file acts like a restart.
    second_run = PracticeSession(JsonFileStore(path), SESSION_ID, PROBLEM)
    print(f"\n  after 'restart': attempts={second_run.attempts()} "
          f"next_try={second_run.next_try()}")
    assert second_run.next_try() == 2
    assert not second_run.is_finished()
