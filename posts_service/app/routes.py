from fastapi import APIRouter, HTTPException
from .models import Comment, CommentCreate
from .database import get_comments_for_post, get_comment, create_comment
from bson import ObjectId
from typing import List

router = APIRouter()

@router.post("/", response_model=Comment)
async def create_new_comment(comment: CommentCreate):
    return await create_comment(Comment(**comment.dict()))

@router.get("/post/{post_id}", response_model=List[Comment])
async def read_comments_for_post(post_id: str):
    return await get_comments_for_post(post_id)

@router.get("/{comment_id}", response_model=Comment)
async def read_comment(comment_id: str):
    try:
        return await get_comment(comment_id)
    except HTTPException as e:
        raise e
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid comment ID format")