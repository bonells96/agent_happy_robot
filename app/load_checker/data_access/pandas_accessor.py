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
        self.df = df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

    def get_by_reference(self, ref_number: str) -> Optional[ShipmentRecord]:
        try:
            ref_number = ref_number.lower()
            result = self.df[self.df['reference_number'] == ref_number]
            return self._to_shipment_record(result.iloc[0]) if not result.empty else None
        except Exception as e:
            logger.error(f"Error retrieving shipment by reference: {e}")
            raise DataAccessError(f"Failed to retrieve shipment: {e}")

    def get_by_lane_and_equipment(self, origin: str, destination: str, equipment_type: Optional[str] = None) -> List[ShipmentRecord]:
        try:
            origin = origin.lower()
            destination = destination.lower()
            mask = self.df['origin'].str.contains(origin, case=False, na=False) & self.df['destination'].str.contains(destination, case=False, na=False)
            filtered_df = self.df[mask]

            if equipment_type:
                equipment_type = equipment_type.lower()
                filtered_df = filtered_df[filtered_df['equipment_type'].str.contains(equipment_type, case=False, na=False)]

            return [self._to_shipment_record(row) for _, row in filtered_df.iterrows()]
        except Exception as e:
            logger.error(f"Error retrieving shipments by lane and equipment: {e}")
            raise DataAccessError(f"Failed to retrieve shipments: {e}")

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
