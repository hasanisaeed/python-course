from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

def get_content():
    # file_path = "assets/simple.html"
    file_path = "assets/nice-looking-page.html"

    with open(file_path, 'r') as f:
        content = f.read() 

    return content

v = app.get("/", response_class=HTMLResponse)

v(get_content)
