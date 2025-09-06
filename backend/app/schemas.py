from pydantic import BaseModel, EmailStr
from typing import Optional, List, Literal
from datetime import datetime

Role = Literal["student", "tutor", "staff"]
Privacy = Literal["public", "private"]

class SignupRequest(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    role: Role | None = "student"

class LoginRequest(BaseModel):
    email: EmailStr
    code: Optional[str] = None

class User(BaseModel):
    id: str
    role: Role
    first_name: str
    last_name: str
    email: EmailStr

class Course(BaseModel):
    id: str
    code: str
    name: str
    department: str = "MATH"

class GroupCreate(BaseModel):
    title: str
    course_id: str
    privacy: Privacy = "public"
    requires_tutor: bool = False

class Group(BaseModel):
    id: str
    title: str
    course_id: str
    creator_id: str
    privacy: Privacy
    requires_tutor: bool

class InviteResponse(BaseModel):
    qr_svg: str
    email_link: str

class SessionCreate(BaseModel):
    group_id: str
    start_at: datetime
    end_at: datetime
    location: str = "Tutoring Center"
    room_id: Optional[str] = None

class Session(BaseModel):
    id: str
    group_id: str
    start_at: datetime
    end_at: datetime
    location: str
    room_id: Optional[str] = None
    status: Literal["pending","approved","cancelled"] = "pending"

class TutorAssignment(BaseModel):
    id: str
    session_id: str
    tutor_id: str
    status: Literal["requested","assigned","declined","completed"] = "requested"

class PublicGroupCard(BaseModel):
    id: str
    title: str
    course_code: str
    start_at: Optional[datetime] = None
    end_at: Optional[datetime] = None
    location: Optional[str] = None
    participant_initials: List[str] = []
    tutor_requested: bool = False
