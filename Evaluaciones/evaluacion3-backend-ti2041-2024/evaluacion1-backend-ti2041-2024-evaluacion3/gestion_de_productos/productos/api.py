from ninja import NinjaAPI

api = NinjaAPI()

@api.get("/status")
def status(request):
    return {"message": "API is working"}

@api.get("/products")
def list_products(request):
    return [{"id": 1, "name": "Product A"}, {"id": 2, "name": "Product B"}]

@api.post("/add-product")
def add_product(request, name: str):
    return {"message": f"Product {name} added successfully!"}
