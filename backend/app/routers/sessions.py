from fastapi import APIRouter, HTTPException
from .. import store
from ..schemas import SessionCreate, Session

router = APIRouter()

@router.post("", response_model=Session)
def create_session(payload: SessionCreate):
    if payload.group_id not in store.groups:
        raise HTTPException(400, "Unknown group_id")
    sid = store.new_id()
    sess = {
        "id": sid,
        "group_id": payload.group_id,
        "start_at": payload.start_at,
        "end_at": payload.end_at,
        "location": payload.location,
        "room_id": payload.room_id,
        "status": "pending",
    }
    store.sessions[sid] = sess
    return sess

@router.post("/{session_id}/request-tutor")
def request_tutor(session_id: str):
    s = store.sessions.get(session_id)
    if not s:
        raise HTTPException(404, "Session not found")
    g = store.groups.get(s["group_id"])
    if g:
        g["requires_tutor"] = True
    return {"ok": True}
