# Study Group App (MVP Scaffold)

This repository is a **starter codebase** aligned with the agreed MVP plan and API contract. It includes a lightweight FastAPI backend (in-memory store) and a Vite + React + TypeScript frontend. No database yet—this is to unblock UI + API iteration.

## Quick Start (Dev)
- Install Docker + Docker Compose
- Copy `.env.example` to `.env`
- Run:
```bash
docker compose up --build
```
- Backend: http://localhost:8000 (FastAPI docs: http://localhost:8000/docs)
- Frontend: http://localhost:5173

## What’s Implemented
- Auth endpoints (email-only placeholder; magic link TBD).
- Public/private groups (private joining simulated via token).
- Sessions creation + tutor request flags.
- Tutor queue & assignments (in-memory).
- Staff schedule read + basic admin actions.
- Basic React pages for Student, Tutor, Staff and a simple schedule component.

## Next
- Replace in-memory store with Postgres (SQLAlchemy + Alembic).
- Implement real email (magic links) + QR code invites.
- Add role-based guards in frontend routes.
- Expand schedule UI, accessibility, and notifications.
