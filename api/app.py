from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import resources.constants


def get_application() -> FastAPI:
    application = FastAPI(title=resources.constants.PROJECT_NAME, debug=resources.constants.DEBUG,
                          version=resources.constants.VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # application.add_event_handler("startup", create_start_app_handler(application))
    # application.add_event_handler("shutdown", create_stop_app_handler(application))
    # application.include_router(api.router, prefix="/api")

    return application


app = get_application()
