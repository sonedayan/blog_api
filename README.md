# Blog API Documentation

| Resource | Description       |
| -------- | ----------------- |
| Users    | Authors of posts  |
| Posts    | Blog posts        |
| Comments | Feedback on posts |


| Method | URL                     | Description         |
| ------ | ----------------------- | ------------------- |
| GET    | `/api/posts`            | Get all posts       |
| GET    | `/api/posts/{id}`       | Get a specific post |
| POST   | `/api/posts`            | Create a new post   |
| PUT    | `/api/posts/{id}`       | Update a post       |
| DELETE | `/api/posts/{id}`       | Delete a post       |
| GET    | `/api/users/{id}/posts` | Get posts by user   |
