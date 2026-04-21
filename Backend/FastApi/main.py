#Previamente se ha instalado FastApi con el comando pip install "fastapi[all]"
from fastapi import FastAPI
from routers import products
from fastapi.staticfiles import StaticFiles



app = FastAPI()


# Routers
app.include_router(products.router)
app.mount("/static", StaticFiles(directory="static"), name="static")#Para montar archivos estáticos como imágenes,
#CSS o JavaScript en la ruta /static. El directorio "static" es donde se encuentran estos archivos en el proyecto. 
# El nombre "static" es un alias para esta ruta, que se puede usar para referenciar los archivos estáticos en otras partes de la aplicación.


@app.get("/")# @app(decorador) sirve para un objeto web en este caso define la ruta del get  en este caso el localhost 

async def root():
    return "Hello FastAPI"

#Levantamos el servidor con el comando uvicorn main:app --reload

#Otra operación 

@app.get("/url")
async def root():
    return {"url_curso":"https://mouredev.com/python"}

#Si no encuentra la dirección manda este mensaje en forma de JSON {"detail":"Not Found"}

#Para que la documentación se haga automática tenemos que Swagger o Redocly  /docs /redoc


#AMBAS SON DE TESTEO PARA PROBAR APIS
#PostMan --> para interactuar con la Api 
#Thunder Client --> desde VScode