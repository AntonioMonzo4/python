from fastapi import APIRouter

router = APIRouter(prefix="/products", tags=["products"], responses={404: {"message": "Not found"}})

products_list = ["Producto 1", "Producto 2", "Producto 3"]

@router.get("/")
async def product():
    return products_list

@router.get("/{id}")
async def product(id: int):
    try:
        return products_list[id]
    except:
        return {"error": "Product not found"}