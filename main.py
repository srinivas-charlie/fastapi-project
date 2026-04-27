""" from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates





app = FastAPI(debug=True)

# Point to templates folder
templates = Jinja2Templates(directory="templates")


""" 
""" @app.get("/")
def homepage():
    return ["name", "srinivas"]


@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html",{"request": request}) """ """


@app.get("/dashboard")
def get_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request}) """







from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)

templates = Jinja2Templates(directory="templates")

@app.get("/dashboard")
def get_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})

@app.get("/login")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})










