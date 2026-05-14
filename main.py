from fastapi import FastAPI, Path
from app.routes import issues
from app.middleware.timer import timing_middleware
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Issue Tracker API",
    version="0.1.0",
    description="A mini production-style API built with FastAPI",
)

app.middleware("http")(timing_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  #
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}

app.include_router(issues.router)

# items = [
#     {"id": 0, "title": "First item", "description": "This is the first item"},
#     {"id": 2, "title": "Second item", "description": "This is the second item"},
#     {"id": 3, "title": "Third item", "description": "This is the third item"},
# ]

# users = [
#     {"id": 1, "name": "John Doe"},
#     {"id": 2, "name": "Jane Do2"},
#     {"id": 3, "name": "Bob Smith"},
# ]

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/health")
# async def health():
#     return {"status": "ok"}

# @app.get("/items")
# def get_items():
#     return items

# @app.get("/items/{item_id}")
# async def get_items_by_id(item_id: int):
#     for item in items:
#         if item['id'] == item_id:
#             return item
#     return {'error': 'item not found'}

# # With validation
# @app.get("/users/{user_id}")
# async def get_user(user_id: int = Path(gt=0 , le=1000, description="the user ID")):
#     for user in users:
#         if user['id'] == user_id:
#             return user
#     return {'error': 'user not found'}

# # post
# @app.post('/items')
# async def create_items(item: dict):
#     items.append(item)
#     return items

