from dataman.logic import PracticeSession, Problem, paused_state
from dataman.store import MemoryStore

store = MemoryStore()
session = PracticeSession(store, "maya-1", Problem("P1", "7 x 8", 56))
session.pause()
print(paused_state(store, "maya-1"))