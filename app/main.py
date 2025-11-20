from fastapi import Depends, FastAPI, HTTPException

from app.auth import get_current_user
from .routers.users import router as users_router
from .routers.payment import router as payment_router
from .routers.projects import router as project_router
from fastapi.middleware.cors import CORSMiddleware

origins = ["http://localhost:3000", "http://localhost:5173"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users")
app.include_router(payment_router, prefix="/access")
app.include_router(project_router, prefix="/home")


@app.get("/me")
def read_me(current_user_id: str = Depends(get_current_user)):
    # current_user_id ya contiene el valor de payload["sub"]
    return {"user_id": current_user_id}


def main():
    print("Hello from frog-blast!")


if __name__ == "__main__":
    main()
