# Study Group App (MVP)

## Overview

A study group coordination platform that connects students, tutors, and staff for academic collaboration. The application allows students to discover and join study groups, request tutoring assistance, and enables staff to manage scheduling and room assignments. Built as an MVP with a FastAPI backend and React frontend, currently using in-memory storage with plans to migrate to a persistent database.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: React 18 with TypeScript for type safety and modern development practices
- **Build Tool**: Vite for fast development and optimized production builds
- **Architecture Pattern**: Component-based architecture with role-specific pages (Student, Tutor, Staff)
- **State Management**: React hooks for local component state management
- **Styling**: Inline styles for rapid prototyping (suitable for MVP phase)

### Backend Architecture
- **Framework**: FastAPI for modern Python API development with automatic OpenAPI documentation
- **Architecture Pattern**: Router-based modular structure separating concerns by feature (auth, groups, sessions, tutors, admin)
- **Data Layer**: In-memory storage using Python dictionaries for MVP rapid development
- **API Design**: RESTful endpoints with Pydantic models for request/response validation
- **Authentication**: Placeholder email-based system designed for future magic link implementation

### Data Storage Strategy
- **Current**: In-memory Python dictionaries for rapid MVP development and testing
- **Planned Migration**: PostgreSQL with SQLAlchemy ORM and Alembic migrations for production persistence
- **Data Models**: User roles (student/tutor/staff), study groups with privacy controls, tutoring sessions, and tutor assignments

### Containerization
- **Docker Compose**: Multi-service development environment with separate containers for frontend and backend
- **Development Setup**: Hot-reload enabled for both React and FastAPI during development
- **Port Configuration**: Backend on 8000, frontend on 5173 for standard development workflow

## External Dependencies

### Core Technologies
- **FastAPI**: Modern Python web framework with automatic API documentation
- **React + TypeScript**: Frontend framework with static typing for enhanced developer experience
- **Vite**: Fast build tool and development server for modern web applications
- **Uvicorn**: ASGI server for running FastAPI applications
- **Pydantic**: Data validation and serialization for API models

### Planned Integrations
- **PostgreSQL**: Production database for persistent data storage
- **SQLAlchemy**: Python SQL toolkit and ORM for database operations
- **Alembic**: Database migration tool for schema management
- **Email Service**: Magic link authentication system (service provider TBD)
- **QR Code Generation**: For group invitation links and easy mobile access

### Development Tools
- **Docker**: Containerization for consistent development and deployment environments
- **TypeScript**: Static typing for improved code quality and developer experience
- **Python Multipart**: File upload handling for FastAPI