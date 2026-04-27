from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    # Version 1.0 (Blue Environment)
    return {"version": "Blue (v1.0)", "pod": hostname}