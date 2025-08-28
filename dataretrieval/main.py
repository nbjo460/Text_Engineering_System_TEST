import routes
import uvicorn

app = routes.app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8111)
