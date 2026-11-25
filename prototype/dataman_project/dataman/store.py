"""Stubbed data layer.

Two stand-ins for a database. Both give the logic layer the same four methods.
Swap one for the other and logic.py does not change.
"""
import json
from pathlib import Path


class MemoryStore:
    """Lives in RAM. Gone when the program ends."""

    def __init__(self):
        self._attempts: list[dict] = []
        self._sets: dict[str, list[str]] = {}
        self._paused: dict[str, dict] = {}

    def save_attempt(self, session_id, problem_id, try_number, answer, correct):
        self._attempts.append({
            "session_id": session_id, "problem_id": problem_id,
            "try": try_number, "answer": answer, "correct": correct,
        })

    def attempts_for(self, session_id, problem_id):
        return [a for a in self._attempts
                if a["session_id"] == session_id and a["problem_id"] == problem_id]

    def members(self, set_id):
        return list(self._sets.get(set_id, []))

    def add_member(self, set_id, problem_id):
        self._sets.setdefault(set_id, []).append(problem_id)

    def save_pause(self, session_id, problem_id, try_number):
        self._paused[session_id] = {"problem_id": problem_id, "try": try_number}
    def load_pause(self, session_id):
        # return the dict, or None if not paused
        record = self._paused.get(session_id)
        return dict(record) if record else None
    
    def clear_pause(self, session_id):
        # use .pop(session_id, None) so clearing twice is safe
        self._paused.pop(session_id, None)

class JsonFileStore(MemoryStore):
    """Same methods. Writes to a file, so evidence survives a restart."""

    def __init__(self, path="dataman_store.json"):
        super().__init__()
        self.path = Path(path)
        if self.path.exists():
            raw = json.loads(self.path.read_text())
            self._attempts = raw.get("attempts", [])
            self._sets = raw.get("sets", {})
            self._paused = raw.get("paused", {})

    def _flush(self):
        self.path.write_text(json.dumps(
            {"attempts": self._attempts, "sets": self._sets, "paused":self._paused}, indent=2))

    def save_attempt(self, *args):
        super().save_attempt(*args)
        self._flush()

    def add_member(self, *args):
        super().add_member(*args)
        self._flush()

    def save_pause(self, *args):
        super().save_pause(*args)
        self._flush()

    def clear_pause(self, *args):
        super().clear_pause(*args)
        self._flush()
