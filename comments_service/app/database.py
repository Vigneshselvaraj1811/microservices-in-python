from motor.motor_asyncio import AsyncIOMotorClient
from .models import Post
from fastapi import HTTPException
from bson import ObjectId
MONGO_DETAILS = "mongodb://mongodb:27017"

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.blog
posts_collection = database.get_collection("posts")

async def get_all_posts():
    posts = []
    async for post in posts_collection.find():
        posts.append(Post(**post))
    return posts

async def get_post(post_id: str):
    if (post := await posts_collection.find_one({"_id": ObjectId(post_id)})) is not None:
        return Post(**post)
    raise HTTPException(status_code=404, detail=f"Post {post_id} not found")

async def create_post(post: Post):
    post_dict = post.dict(by_alias=True)
    new_post = await posts_collection.insert_one(post_dict)
    created_post = await posts_collection.find_one({"_id": new_post.inserted_id})
    return Post(**created_post)