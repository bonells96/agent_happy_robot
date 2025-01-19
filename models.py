from pydantic import BaseModel
from typing import Optional

class ReferenceRequest(BaseModel):
    ref_number: str

class LaneAndEquipmentRequest(BaseModel):
    origin: str
    destination: str
    equipment_type: Optional[str] = None

class CarrierRequest(BaseModel):
    mc_number: str

