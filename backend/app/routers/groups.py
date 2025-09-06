from fastapi import APIRouter, HTTPException
from typing import List, Optional
from .. import store
from ..schemas import GroupCreate, Group, InviteResponse, PublicGroupCard

router = APIRouter()

@router.get("", response_model=List[PublicGroupCard])
def list_public_groups(course_id: Optional[str] = None):
    cards = []
    for g in store.groups.values():
        if g["privacy"] != "public":
            continue
        if course_id and g["course_id"] != course_id:
            continue
        sess = next((s for s in store.sessions.values() if s["group_id"] == g["id"]), None)
        initials = []
        for m in store.memberships:
            if m["group_id"] == g["id"]:
                u = store.users.get(m["user_id"])
                if u:
                    initials.append(store.initials(u["first_name"]))
        cards.append(PublicGroupCard(
            id=g["id"],
            title=g["title"],
            course_code=store.courses[g["course_id"]]["code"],
            start_at=sess["start_at"] if sess else None,
            end_at=sess["end_at"] if sess else None,
            location=sess["location"] if sess else None,
            participant_initials=initials,
            tutor_requested=bool(g.get("requires_tutor", False)),
        ))
    return cards

@router.post("", response_model=Group)
def create_group(payload: GroupCreate, creator_id: str):
    if payload.course_id not in store.courses:
        raise HTTPException(400, "Unknown course_id")
    gid = store.new_id()
    group = {
        "id": gid,
        "title": payload.title,
        "course_id": payload.course_id,
        "creator_id": creator_id,
        "privacy": payload.privacy,
        "requires_tutor": payload.requires_tutor,
    }
    store.groups[gid] = group
    store.memberships.append({"user_id": creator_id, "group_id": gid, "role_in_group": "owner"})
    return group

@router.post("/{group_id}/invite", response_model=InviteResponse)
def invite(group_id: str):
    if group_id not in store.groups:
        raise HTTPException(404, "Group not found")
    token = group_id
    link = f"https://example.edu/invite/{token}"
    qr_svg = "<svg viewBox='0 0 10 10' width='128' height='128'><rect width='10' height='10' fill='#000'/></svg>"
    return {"qr_svg": qr_svg, "email_link": link}

@router.post("/{group_id}/join")
def join_public(group_id: str, user_id: str):
    g = store.groups.get(group_id)
    if not g:
        raise HTTPException(404, "Group not found")
    if g["privacy"] != "public":
        raise HTTPException(403, "Group is private")
    store.memberships.append({"user_id": user_id, "group_id": group_id, "role_in_group": "member"})
    return {"ok": True}
