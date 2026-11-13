"""Text interface layer. This is the only file that uses input() and print().

Run:  python app.py              (data lives in RAM)
      python app.py --store json (data survives a restart)
"""
import argparse

from dataman.logic import (MemoryBank, PracticeSession, Problem, SetFull,
                           curator_report, paused_state)
from dataman.store import JsonFileStore, MemoryStore

PROBLEM = Problem("P1", "7 x 8", 56)
PROBLEMS = {PROBLEM.id: PROBLEM}   # stub: turns a saved problem id back into a Problem
SESSION = "maya-1"

def run_problem(session):
    """Ask for answers until the problem is finished or the learner pauses."""
    while not session.is_finished():
        try:
            raw = input(f"Try {session.next_try()}: {session.problem.prompt} = ")
        except (KeyboardInterrupt, EOFError):
            raw = "pause"
        raw = raw.strip().lower()
        if raw == "pause":
            session.pause()
            print("\nPaused. Choose 'unpause' to continue.")
            return
        try:
            answer = int(raw)
        except ValueError:
            print("Enter a whole number.")
            continue
        out = session.submit(answer)
        if out.status == "correct":
            print("Correct.")
        elif out.status == "retry":
            print("Not yet. Try again.")
        else:
            print(f"The answer is {out.revealed_answer}.")

def practice(store):
    if paused_state(store, SESSION) is not None:
        print("A session is paused. Choose 'unpause' to continue.")
        return
    session = PracticeSession(store, SESSION, PROBLEM)
    if session.is_finished():
        print("This session is finished. Choose 'report'.")
        return
    print("Type 'pause' at any time to pause.")
    run_problem(session)


def unpause(store):
    state = paused_state(store, SESSION)
    if state is None:
        print("Nothing is paused.")
        return
    session = PracticeSession(store, SESSION, PROBLEMS[state.problem_id])
    session.resume()
    print(f"Resuming {state.problem_id} at try {state.try_number}.")
    run_problem(session)


def report(store):
    rep = curator_report(store, SESSION, PROBLEM.id)
    print(f"Curator report for {SESSION}: {rep['label']}")
    for r in rep["attempts"]:
        print(f"  try {r['try']}: answered {r['answer']} -> "
              f"{'correct' if r['correct'] else 'wrong'}")


def bank(store):
    memory_bank = MemoryBank(store, "set-1")
    pid = input("Problem id to add (for example P11): ").strip()
    try:
        memory_bank.add_problem(pid)
        print(f"Added. Set holds {len(memory_bank.members())}.")
    except SetFull as err:
        print(f"Refused: {err}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--store", choices=["memory", "json"], default="memory")
    args = parser.parse_args()
    store = JsonFileStore() if args.store == "json" else MemoryStore()
    actions = {"practice": practice, "unpause": unpause, "report": report, "bank": bank}
    while True:
        try:
            choice = input("practice / unpause / report / bank / quit > ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print()
            break


if __name__ == "__main__":
    main()
