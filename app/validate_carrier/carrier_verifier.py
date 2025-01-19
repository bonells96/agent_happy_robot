class CarrierVerifier:
    """A class to handle carrier verification logic."""

    @staticmethod
    def verify(mc_number: str) -> dict:
        """Simulate verification of a carrier's MC number."""
        mc_number = mc_number.strip()

        # Synthetic verification logic
        if mc_number.isdigit() and len(mc_number) == 6:
            # Simulating valid carrier data
            return {
                "mc_number": mc_number,
                "status": "Valid",
                "carrier_name": "Mock Carrier Inc.",
                "address": "123 Mock Street, Mocksville, MS",
                "operational_status": "Active",
                "safety_rating": "Satisfactory"
            }
        else:
            raise ValueError("Invalid MC number format or not found.")
