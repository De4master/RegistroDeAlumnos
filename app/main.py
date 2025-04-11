from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.routers import alumno

app = FastAPI()

# ✅ Archivos estáticos (CSS, JS, imágenes, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ✅ Plantillas (Jinja2) desde la carpeta "templates"
templates = Jinja2Templates(directory="templates")

# ✅ Ruta de inicio: Usar Jinja2 para renderizar el archivo HTML
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# ✅ Incluir las rutas del router de alumnos
app.include_router(alumno.router, prefix="/alumnos", tags=["Alumnos"])
