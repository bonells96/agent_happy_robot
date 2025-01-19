from abc import ABC, abstractmethod
from app.load_checker.core.schemas import ShipmentRecord
from typing import List, Optional

from abc import ABC, abstractmethod
from typing import Optional, List
from app.load_checker.core.schemas import ShipmentRecord

class BaseDataAccessor(ABC):
    """Abstract base class defining the interface for data access."""

    @abstractmethod
    def get_by_reference(self, ref_number: str) -> Optional[ShipmentRecord]:
        """Retrieve shipment by reference number."""
        pass

    @abstractmethod
    def get_by_lane_and_equipment(self, origin: str, destination: str, equipment_type: Optional[str] = None) -> List[ShipmentRecord]:
        """Retrieve shipments by origin-destination pair and optionally by equipment type."""
        pass

