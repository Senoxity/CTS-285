"""Tests for the Memory Bank (MemoryBank in dataman/logic.py).

Run from the folder that contains app.py:
    python -m pytest -v -s test_memory_bank.py
(-v lists each test by name; -s lets the print() lines below show up.)
"""
import json

import pytest

from dataman.logic import MAX_SET_SIZE, MemoryBank, SetFull
from dataman.store import JsonFileStore, MemoryStore


@pytest.fixture
def bank():
    """An empty Memory Bank set on an in-memory store (a fresh one per test)."""
    return MemoryBank(MemoryStore(), "set-1")


def fill(bank, count):
    """Helper: add `count` different problems (P0, P1, P2, ...)."""
    for i in range(count):
        bank.add_problem(f"P{i}")


def test_new_set_is_empty(bank):
    print(f"\n  members={bank.members()}")
    assert bank.members() == []


def test_add_problem_puts_it_in_the_set(bank):
    bank.add_problem("P11")
    print(f"\n  members={bank.members()}")
    assert bank.members() == ["P11"]


def test_members_keep_the_order_they_were_added(bank):
    for pid in ["P3", "P1", "P2"]:
        bank.add_problem(pid)
    print(f"\n  members={bank.members()}")
    assert bank.members() == ["P3", "P1", "P2"]


def test_adding_the_same_problem_twice_is_ignored(bank):
    bank.add_problem("P1")
    bank.add_problem("P1")
    print(f"\n  members={bank.members()}")
    assert bank.members() == ["P1"]


def test_ten_problems_fit(bank):
    fill(bank, MAX_SET_SIZE)
    print(f"\n  set holds {len(bank.members())} (limit {MAX_SET_SIZE})")
    assert len(bank.members()) == 10


def test_eleventh_problem_is_refused(bank):
    fill(bank, MAX_SET_SIZE)
    with pytest.raises(SetFull, match="already holds 10") as err:
        bank.add_problem("P10")
    print(f"\n  refused with: {err.value}")
    assert len(bank.members()) == 10
    assert "P10" not in bank.members()


def test_re_adding_a_member_of_a_full_set_is_not_an_error(bank):
    fill(bank, MAX_SET_SIZE)
    bank.add_problem("P0")              # already in the set, so no SetFull
    print(f"\n  set still holds {len(bank.members())}")
    assert len(bank.members()) == 10


def test_two_sets_do_not_share_members():
    store = MemoryStore()
    set_a = MemoryBank(store, "set-a")
    set_b = MemoryBank(store, "set-b")
    fill(set_a, MAX_SET_SIZE)
    set_b.add_problem("P99")            # set-b has room even though set-a is full
    print(f"\n  set-a holds {len(set_a.members())}, set-b holds {set_b.members()}")
    assert len(set_a.members()) == 10
    assert set_b.members() == ["P99"]


def test_changing_the_returned_list_does_not_change_the_set(bank):
    bank.add_problem("P1")
    copy = bank.members()
    copy.append("P2")
    print(f"\n  edited copy={copy}, real members={bank.members()}")
    assert bank.members() == ["P1"]


def test_set_survives_a_restart_with_the_json_store(tmp_path):
    path = tmp_path / "store.json"      # tmp_path is a throwaway folder
    first_run = MemoryBank(JsonFileStore(path), "set-1")
    first_run.add_problem("P1")
    first_run.add_problem("P2")

    # A brand-new store object reading the same file acts like a restart.
    second_run = MemoryBank(JsonFileStore(path), "set-1")
    print(f"\n  after 'restart': members={second_run.members()}")
    assert second_run.members() == ["P1", "P2"]

    saved = json.loads(path.read_text())
    assert saved["sets"] == {"set-1": ["P1", "P2"]}
