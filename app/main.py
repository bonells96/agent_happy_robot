from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader
import pandas as pd
from app.load_checker.data_access.pandas_accessor import PandasAccessor
from typing import Optional
from app.validate_carrier.carrier_verifier import CarrierVerifier  # Import the class
from app.config import config  # Import the Config instance
from app.models.models import ReferenceRequest, LaneAndEquipmentRequest, CarrierRequest
from app.csv_loader import CSVLoader  # Import the CSV loader

# Initialize FastAPI app
app = FastAPI()


# Define API Key Header
API_KEY_NAME = "X-API-Key"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=True)


def verify_api_key(api_key: str = Depends(api_key_header)):
    """
    Verifies the API key passed in the request header.
    Raises an HTTPException if the API key is invalid.
    """
    if api_key != config.api_key:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return True



# Initialize the PandasAccessor with a sample DataFrame (adjust the file path as needed)
# Create an instance of CSVLoader to load the data
loader = CSVLoader()
accessor = loader.get_accessor()


@app.get("/")
def read_root():
    return {"message": "Welcome to the HRO API"}

@app.post("/shipment/")
def get_shipment_by_reference(request: ReferenceRequest):
    try:
        shipment = accessor.get_by_reference(request.ref_number)
        if shipment:
            return {"shipment": shipment.dict()}
        return {"error": "Shipment not found"}
    except Exception as e:
        accessor.handle_exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/shipment/by_lane_and_equipment/")
def get_shipments_by_lane_and_equipment(request: LaneAndEquipmentRequest):
    """
    Retrieve shipments by lane (origin and destination) and optionally by equipment type.
    """
    try:
        shipments = accessor.get_by_lane_and_equipment(
            origin=request.origin, destination=request.destination, equipment_type=request.equipment_type
        )
        if shipments:
            return {"shipments": [shipment.dict() for shipment in shipments]}
        return {"error": "No shipments found for the specified criteria"}
    except Exception as e:
        accessor.handle_exception(e)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    

@app.post("/verify_carrier/")
def verify_carrier(request: CarrierRequest):
    """
    Endpoint to verify a carrier's MC number.
    """
    try:
        verifier = CarrierVerifier()
        carrier_details = verifier.verify(request.mc_number)
        return carrier_details
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))