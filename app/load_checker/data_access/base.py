from abc import ABC, abstractmethod
from app.load_checker.core.schemas import ShipmentRecord
from typing import List, Optional

class BaseDataAccessor(ABC):
    """Abstract base class defining the interface for data access."""
    
    @abstractmethod
    def get_by_reference(self, ref_number: str) -> Optional[ShipmentRecord]:
        """Retrieve shipment by reference number."""
        pass

    @abstractmethod
    def get_by_lane(self, origin: str, destination: str) -> List[ShipmentRecord]:
        """Retrieve shipments by origin-destination pair."""
        pass

    @abstractmethod
    def get_by_equipment(self, equipment_type: str) -> List[ShipmentRecord]:
        """Retrieve shipments by equipment type."""
        pass

    @abstractmethod
    def get_average_rate_by_lane(self, origin: str, destination: str) -> Optional[float]:
        """Calculate average rate for a lane."""
        pass

