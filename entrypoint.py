from config import docker_config
import uvicorn

if __name__ == "__main__":
    if docker_config.Mode == "server":
        uvicorn.run("api.app:app", host="0.0.0.0", port=80, reload=True)
    else:
        pass
