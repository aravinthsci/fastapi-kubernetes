from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware

from app.api.errors.http_error import http_error_handler
from app.api.routes.api import router as api_router
from app.api.db.database import create_tables


def get_application() -> FastAPI:
    application = FastAPI(title='fastapi-kubernetes', version='1.0', docs_url='/fastapi',
                          openapi_url='/fastapi/openapi.json', redoc_url='/fastapi/redoc')

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.add_exception_handler(HTTPException, http_error_handler)

    application.include_router(api_router, prefix='/fastapi/api')
    create_tables()
    return application


app = get_application()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)
