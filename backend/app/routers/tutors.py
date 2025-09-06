from fastapi import APIRouter, HTTPException
from .. import store
from ..schemas import TutorAssignment

router = APIRouter()

@router.get("/requests")
def tutor_requests():
    results = []
    for s in store.sessions.values():
        g = store.groups.get(s["group_id"])
        if g and g.get("requires_tutor", False):
            results.append(s)
    return results

@router.post("/assignments", response_model=TutorAssignment)
def accept_assignment(session_id: str, tutor_id: str):
    if session_id not in store.sessions:
        raise HTTPException(404, "Session not found")
    aid = store.new_id()
    ta = {"id": aid, "session_id": session_id, "tutor_id": tutor_id, "status": "assigned"}
    store.tutor_assignments[aid] = ta
    return ta

@router.get("/assignments")
def my_assignments(tutor_id: str):
    return [a for a in store.tutor_assignments.values() if a["tutor_id"] == tutor_id]
