from fastapi import APIRouter


router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses = {404: {"message": "Not found"}})

products_list = [{"name":"laptop", "price":1000},
          {"name":"mouse", "price":10},
          {"name":"keyboard", "price":20}]

@router.get("/")
async def products():
  return products_list


@router.get("/{id}")
async def products(id: int):
  return products_list[id]