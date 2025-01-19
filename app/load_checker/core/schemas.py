# Example using schemas.py:
from dataclasses import dataclass, asdict
from typing import Optional

@dataclass
class ShipmentRecord:  # You might also rename the class to match the file
    """Schema defining the structure of a shipment record."""
    reference_number: str
    origin: str
    destination: str
    equipment_type: str
    rate: float
    commodity: str

    def dict(self):
        return asdict(self)