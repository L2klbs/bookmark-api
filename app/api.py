from fastapi import APIRouter, Depends, Form, File, UploadFile
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List, Optional

from .models import Entry, EntryDB
from .db import get_db

router = APIRouter()

# Health Check
@router.get("/health")
def health_check():
    return { "status": "ok" }

@router.get("/entries", response_model=List[Entry])
async def list_entries(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(EntryDB))
    entries = result.scalars().all()
    return [Entry.model_validate(e) for e in entries]


@router.post("/entry", response_model=Entry)
async def create_entry(
    title: str = Form(...),
    bookmark: Optional[str] = Form(None),
    media_type: Optional[str] = Form(None),
    genre: Optional[str] = Form(None),
    content_url: Optional[str] = Form(None),
    thumbnail: Optional[UploadFile] = File(None),
    db: AsyncSession = Depends(get_db)
):
    # TODO: save thumbnail to disk and generate URL
    thumbnail_url = None

    new_entry = EntryDB(
        title=title,
        bookmark=bookmark,
        media_type=media_type,
        genre=genre,
        content_url=content_url,
        thumbnail_url=thumbnail_url
    )

    db.add(new_entry)
    await db.commit()
    await db.refresh(new_entry)

    return Entry.model_validate(new_entry)


@router.put("/entry/{entry_id}", response_model=Entry)
async def update_entry(
    entry_id: int,
    title: str = Form(...),
    bookmark: Optional[str] = Form(None),
    media_type: Optional[str] = Form(None),
    genre: Optional[str] = Form(None),
    content_url: Optional[str] = Form(None),
    thumbnail: Optional[UploadFile] = File(None),
    db: AsyncSession = Depends(get_db)
):
    # 1. Fetch the existing entry
    result = await db.execute(select(EntryDB).where(EntryDB.id == entry_id))
    entry = result.scalar_one_or_none()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    # 2. Apply updates
    entry.title = title
    entry.bookmark = bookmark
    entry.media_type = media_type
    entry.genre = genre
    entry.content_url = content_url
    entry.thumbnail_url = None  # TODO: handle file upload later

    # 3. Commit changes
    await db.commit()
    await db.refresh(entry)

    return Entry.model_validate(entry)


@router.delete("/entry/{entry_id}")
async def delete_entry(entry_id: int, db: AsyncSession = Depends(get_db)):
    # 1. Fetch the existing entry
    result = await db.execute(select(EntryDB).where(EntryDB.id == entry_id))
    entry = result.scalar_one_or_none()

    if not entry:
        raise HTTPException(status_code=404, detail="Entry not found")

    await db.delete(entry)
    await db.commit()

    return {"message": f"Entry {entry_id} deleted."}
