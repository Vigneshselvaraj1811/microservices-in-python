from fastapi import APIRouter, HTTPException
from .models import Post, PostCreate
from .database import get_all_posts, get_post, create_post
from bson import ObjectId
from typing import List

router = APIRouter()

# Allow both /posts and /posts/
@router.post("", response_model=Post, include_in_schema=False)
@router.post("/", response_model=Post)  # Handles /posts/
async def create_new_post(post: PostCreate):
    return await create_post(Post(**post.dict()))

@router.get("/", response_model=List[Post])
async def read_posts():
    return await get_all_posts()

@router.get("/{post_id}", response_model=Post)
async def read_post(post_id: str):
    try:
        return await get_post(post_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid post ID format")