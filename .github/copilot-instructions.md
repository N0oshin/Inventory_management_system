# Copilot Instructions for Product Management API

## Architecture Overview

This is a **FastAPI-based product management system** with async SQLAlchemy ORM. The architecture follows a modular structure:

- **`app/core/`**: Core infrastructure (config, database, migrations)
- **`app/modules/`**: Feature modules (product, category) - each module is self-contained

**Key architectural decision**: All database models inherit from `Base` in `database.py` which enforces UUID primary keys with auto-generation and indexing.

## Database & ORM Patterns

### Database Setup (`app/core/database.py`)
- Uses **SQLAlchemy 2.0+ async engine** with `postgresql+asyncpg://` connection
- Session management via `async_sessionmaker` with `expire_on_commit=False` (preserves objects after commit)
- Dependency injection pattern: `get_db()` yields sessions for FastAPI route handlers

### Model Creation Pattern
All models must:
1. Inherit from `Base` (automatic UUID primary key)
2. Use `Mapped` type hints with `mapped_column()` for all fields
3. Example structure to follow:
```python
from app.core.database import Base
from sqlalchemy.orm import Mapped, mapped_column

class Product(Base):
    __tablename__ = "products"
    name: Mapped[str] = mapped_column(String(255))
    description: Mapped[str | None]
```

### Configuration (`app/core/config.py`)
- Uses **Pydantic v2 BaseSettings** with `.env` file support
- Database URL format: `postgresql+asyncpg://user:password@host:port/dbname`
- Settings are loaded once at startup via `settings` singleton

## Module Development Pattern

Each feature module (`app/modules/{feature}/`) should contain:
- `models.py`: SQLAlchemy ORM models
- `schemas.py`: Pydantic request/response schemas
- `crud.py`: Database operations
- `routes.py`: FastAPI endpoints (use `get_db` dependency)
- `__init__.py`: Export key classes/functions

## Development Workflow

**Running the API**:
```bash
# Ensure .env is configured with valid database_url
uvicorn app.main:app --reload
```

**Database connection**:
- PostgreSQL with asyncpg driver (required for async operations)
- `.env` file must exist with `database_url` variable
- Connection string includes URL-encoded password (e.g., `%40` for `@`)

## Common Patterns & Conventions

1. **Async-first**: All database operations use `async def`, all routes are async
2. **UUID everywhere**: All model IDs are UUIDs, never use integer PKs
3. **Type hints required**: Use `Mapped[]` in models, Pydantic types in schemas
4. **Session cleanup automatic**: FastAPI's dependency injection + `async with` handles session lifecycle
