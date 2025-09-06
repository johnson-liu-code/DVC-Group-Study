from typing import Dict, List
import uuid

users: Dict[str, dict] = {}
courses: Dict[str, dict] = {}
groups: Dict[str, dict] = {}
memberships: List[dict] = []
sessions: Dict[str, dict] = {}
tutor_assignments: Dict[str, dict] = {}

def seed():
    for code, name in [("MATH-192", "Calculus I"), ("MATH-194", "Linear Algebra")]:
        cid = str(uuid.uuid4())
        courses[cid] = {"id": cid, "code": code, "name": name, "department": "MATH"}
seed()

def new_id():
    return str(uuid.uuid4())

def initials(first_name: str) -> str:
    return (first_name[:1] if first_name else "?") + "•"
