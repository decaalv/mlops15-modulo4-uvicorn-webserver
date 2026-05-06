import pandas as pd
from joblib import load
from fastapi import FastAPI
from pydantic import BaseModel
from Houses import House

classifier = load("./models/linear_regression.joblib")

# ---------------------------------------------------------------------------
# Initialize app
# ---------------------------------------------------------------------------
app = FastAPI()

@app.post("/predict")
async def predict_price(house: House):
    house_data = pd.DataFrame([house.dict()])
    prediction = classifier.predict(house_data)
    return {
        'sale_price': prediction.tolist()
    }


# ---------------------------------------------------------------------------
# Define a Pydantic model for the request body
# ---------------------------------------------------------------------------
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

items_db = [] # Add this at the top

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
    items_db.append(item)
    return item


# Add this endpoint at the end of app_v1.py
@app.get("/items/")
async def read_items():
    return items_db

# ---------------------------------------------------------------------------
# Run the app
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)