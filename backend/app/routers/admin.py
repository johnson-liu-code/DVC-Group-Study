from fastapi import APIRouter, HTTPException
from .. import store

router = APIRouter()

@router.get("/schedule")
def schedule(from_iso: str | None = None, to_iso: str | None = None):
    return list(store.sessions.values())

@router.post("/sessions/{session_id}/approve-room")
def approve_room(session_id: str, room_id: str):
    s = store.sessions.get(session_id)
    if not s:
        raise HTTPException(404, "Session not found")
    s["room_id"] = room_id
    s["status"] = "approved"
    return {"ok": True, "session_id": session_id, "room_id": room_id}

@router.post("/sessions/{session_id}/assign-tutor")
def assign_tutor(session_id: str, tutor_id: str):
    if session_id not in store.sessions:
        raise HTTPException(404, "Session not found")
    aid = __import__('uuid').uuid4().hex
    store.tutor_assignments[aid] = {"id": aid, "session_id": session_id, "tutor_id": tutor_id, "status": "assigned"}
    return {"ok": True, "assignment_id": aid}

@router.post("/announcements")
def announcements(message: str):
    return {"ok": True, "sent_to": len(store.users), "message": message}

@router.get("/reports")
def reports():
    return {
        "groups": len(store.groups),
        "sessions": len(store.sessions),
        "tutor_assignments": len(store.tutor_assignments),
    }
