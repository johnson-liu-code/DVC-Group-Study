from fastapi import APIRouter
from .. import store
from ..schemas import SignupRequest, LoginRequest, User

router = APIRouter()

@router.post("/signup", response_model=User)
def signup(payload: SignupRequest):
    uid = store.new_id()
    user = {
        "id": uid,
        "role": payload.role or "student",
        "first_name": payload.first_name,
        "last_name": payload.last_name,
        "email": payload.email,
    }
    store.users[uid] = user
    return user

@router.post("/login")
def login(payload: LoginRequest):
    for u in store.users.values():
        if u["email"].lower() == payload.email.lower():
            return {"ok": True, "user_id": u["id"]}
    return {"ok": False, "error": "Unknown email. Please sign up."}

@router.post("/logout")
def logout():
    return {"ok": True}
