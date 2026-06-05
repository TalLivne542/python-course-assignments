from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from core.polymer_logic import calculate_crystallinity

app = FastAPI(title="Polymer Crystallinity Web API")

# Define the expected JSON data structure from the client
class CrystallinityInput(BaseModel):
    polymer_name: str
    delta_hm_measured: float
    moisture_content: float = 0.0

@app.get("/")
def home():
    return {"message": "Welcome to the Polymer Crystallinity API. Use the /calculate endpoint to POST data."}

@app.post("/calculate")
def calculate_endpoint(input_data: CrystallinityInput):
    """
    Web Endpoint: Receives polymer parameters, invokes Day 04 business logic, and returns the result.
    """
    try:
        # Call the isolated business logic function from Day 04
        result = calculate_crystallinity(
            polymer_name=input_data.polymer_name,
            delta_hm_measured=input_data.delta_hm_measured,
            moisture_content=input_data.moisture_content
        )
        return {
            "status": "success",
            "polymer": input_data.polymer_name,
            "crystallinity_percentage": round(result, 2)
        }
    except ValueError as e:
        # Map validation errors from core logic to HTTP 400 Bad Request
        raise HTTPException(status_code=400, detail=str(e))
