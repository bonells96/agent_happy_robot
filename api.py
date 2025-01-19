from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from app.load_checker.data_access.pandas_accessor import PandasAccessor


# Initialize FastAPI app
app = FastAPI()

# Create a Pydantic model for the input data
class ReferenceRequest(BaseModel):
    ref_number: str

# Initialize the PandasAccessor with a sample DataFrame (adjust the file path as needed)
df = pd.read_csv('example_load_data.csv')
accessor = PandasAccessor(df)

@app.get("/")
def read_root():
    return {"message": "Welcome to the HRO API"}

@app.post("/shipment/")
def get_shipment_by_reference(request: ReferenceRequest):
    shipment = accessor.get_by_reference(request.ref_number)
    if shipment:
        return {"shipment": shipment.dict()}
    return {"error": "Shipment not found"}