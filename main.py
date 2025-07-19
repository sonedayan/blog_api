from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# --------------------------
# Models
# --------------------------
class PostCreate(BaseModel):
    user_id: int
    title: str
    content: str

class Post(PostCreate):
    id: int

# --------------------------
# In-memory storage
# --------------------------
posts = []
next_post_id = 1  # This will increment with each new post

# --------------------------
# Routes
# --------------------------

@app.get("/api/posts", response_model=List[Post])
def get_all_posts():
    return posts

@app.get("/api/posts/{id}", response_model=Post)
def get_post(id: int):
    for post in posts:
        if post.id == id:
            return post
    raise HTTPException(status_code=404, detail="Post not found")

@app.post("/api/posts", response_model=Post)
def create_post(post_data: PostCreate):
    global next_post_id
    new_post = Post(id=next_post_id, **post_data.dict())
    posts.append(new_post)
    next_post_id += 1
    return new_post

@app.put("/api/posts/{id}", response_model=Post)
def update_post(id: int, updated_data: PostCreate):
    for index, post in enumerate(posts):
        if post.id == id:
            updated_post = Post(id=id, **updated_data.dict())
            posts[index] = updated_post
            return updated_post
    raise HTTPException(status_code=404, detail="Post not found")

@app.delete("/api/posts/{id}")
def delete_post(id: int):
    for index, post in enumerate(posts):
        if post.id == id:
            posts.pop(index)
            return {"message": "Post deleted"}
    raise HTTPException(status_code=404, detail="Post not found")

@app.get("/api/users/{user_id}/posts", response_model=List[Post])
def get_user_posts(user_id: int):
    return [post for post in posts if post.user_id == user_id]
