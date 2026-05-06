from fastapi import FastAPI
from pydantic import BaseModel

# ---------------------------------------------------------------------------
# Initialize app
# ---------------------------------------------------------------------------
app = FastAPI()

# ---------------------------------------------------------------------------
# Define a Pydantic model for the request body
# ---------------------------------------------------------------------------
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

# ---------------------------------------------------------------------------
# Define API endpoints
# ---------------------------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Web server is available"}
    
@app.get("/health")
async def health():
    return {"status": "ok"}

# POST request with body validation
@app.post("/items/")
async def create_item(item: Item):
    return item

# ---------------------------------------------------------------------------
# Run the app
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000, reload=True)