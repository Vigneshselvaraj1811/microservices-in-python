from motor.motor_asyncio import AsyncIOMotorClient
from .models import Comment
from fastapi import HTTPException
from bson import ObjectId

MONGO_DETAILS = "mongodb://mongodb:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.blog
comments_collection = database.get_collection("comments")

async def get_comments_for_post(post_id: str):
    comments = []
    async for comment in comments_collection.find({"post_id": post_id}):
        comments.append(Comment(**comment))
    return comments

async def get_comment(comment_id: str):
    if (comment := await comments_collection.find_one({"_id": ObjectId(comment_id)})) is not None:
        return Comment(**comment)
    raise HTTPException(status_code=404, detail=f"Comment {comment_id} not found")

async def create_comment(comment: Comment):
    comment_dict = comment.dict(by_alias=True)
    new_comment = await comments_collection.insert_one(comment_dict)
    created_comment = await comments_collection.find_one({"_id": new_comment.inserted_id})
    return Comment(**created_comment)