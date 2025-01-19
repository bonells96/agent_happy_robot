from .base import BaseDataAccessor
from app.load_checker.core.schemas import ShipmentRecord
from app.load_checker.core.exceptions import DataAccessError
from typing import Optional, List
import pandas as pd
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PandasAccessor(BaseDataAccessor):
    """Pandas implementation of data accessor for smaller datasets."""
    
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def get_by_reference(self, ref_number: str) -> Optional[ShipmentRecord]:
        try:
            result = self.df[self.df['reference_number'] == ref_number]
            return self._to_shipment_record(result.iloc[0]) if not result.empty else None
        except Exception as e:
            logger.error(f"Error retrieving shipment by reference: {e}")
            raise DataAccessError(f"Failed to retrieve shipment: {e}")

    def get_by_lane(self, origin: str, destination: str) -> List[ShipmentRecord]:
        try:
            mask = (self.df['origin'] == origin) & (self.df['destination'] == destination)
            return [self._to_shipment_record(row) for _, row in self.df[mask].iterrows()]
        except Exception as e:
            logger.error(f"Error retrieving shipments by lane: {e}")
            raise DataAccessError(f"Failed to retrieve shipments: {e}")

    def get_by_equipment(self, equipment_type: str) -> List[ShipmentRecord]:
        try:
            return [
                self._to_shipment_record(row)
                for _, row in self.df[self.df['equipment_type'].str.contains(equipment_type)].iterrows()
            ]
        except Exception as e:
            logger.error(f"Error retrieving shipments by equipment: {e}")
            raise DataAccessError(f"Failed to retrieve shipments: {e}")

    def get_average_rate_by_lane(self, origin: str, destination: str) -> Optional[float]:
        try:
            mask = (self.df['origin'] == origin) & (self.df['destination'] == destination)
            rates = self.df[mask]['rate']
            return float(rates.mean()) if not rates.empty else None
        except Exception as e:
            logger.error(f"Error calculating average rate: {e}")
            raise DataAccessError(f"Failed to calculate average rate: {e}")

    @staticmethod
    def _to_shipment_record(row: pd.Series) -> ShipmentRecord:
        """Convert a pandas Series to a ShipmentRecord."""
        return ShipmentRecord(
            reference_number=str(row['reference_number']),
            origin=str(row['origin']),
            destination=str(row['destination']),
            equipment_type=str(row['equipment_type']),
            rate=float(row['rate']),
            commodity=str(row['commodity'])
        )



