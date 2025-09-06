from fastapi import FastAPI
from .routers import auth, groups, sessions, tutors, admin

app = FastAPI(title="Study Group App API", version="0.0.1")

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(sessions.router, prefix="/sessions", tags=["sessions"])
app.include_router(tutors.router, prefix="/tutor", tags=["tutor"])
app.include_router(admin.router, prefix="/admin", tags=["admin"])

@app.get("/health")
def health():
    return {"ok": True}
