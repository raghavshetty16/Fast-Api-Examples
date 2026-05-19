# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>FastAPI HTML Page</title>
    </head>
    <body>
        <h1>Hello from Raghav!</h1>
        <p>This HTML page is returned directly from a FastAPI route.</p>
    </body>
    </html>
    """