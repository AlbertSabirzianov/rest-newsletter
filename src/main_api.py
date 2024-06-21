import uvicorn

from fastapi import FastAPI


def create_app():
    app = FastAPI()
    from app.api.api_router import api_router
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
