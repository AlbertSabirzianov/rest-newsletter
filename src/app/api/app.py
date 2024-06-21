from fastapi import FastAPI


def create_app():
    app = FastAPI()
    from ..api.api_router import api_router
    app.include_router(api_router, prefix="/api")
    return app


app = create_app()
