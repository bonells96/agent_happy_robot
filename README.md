# HappyRobot Challenge

Welcome to the HappyRobot Challenge! We'll implement a real-world carrier sales use case using the HappyRobot platform and develop a custom REST API to support this use case.

## Overview

This project implements a FastAPI-based REST API that provides shipment and carrier verification functionality. The API allows users to query shipment information using reference numbers or lane/equipment criteria, and verify carrier MC numbers.

## Features

- Secure API access with API key authentication
- Shipment lookup by reference number
- Shipment search by lane (origin/destination) and equipment type
- Carrier MC number verification
- CSV data loading and management
- Error handling and logging

## Prerequisites

- Python 3.9+
- Docker (optional)
- FastAPI
- pandas
- uvicorn

## Installation

### Using Docker

1. Clone the repository:
```bash
git clone <repository-url>
cd happy-robot-challenge
```

2. Build and run the Docker container:
```bash
docker build -t happy-robot-api .
docker run -p 8080:8080 happy-robot-api
```

### Manual Installation

1. Clone the repository
2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## API Endpoints


### Shipment Lookup
- `POST /shipment/`
  - Retrieves shipment details by reference number
  - Requires API key authentication
  - Request body:
    ```json
    {
      "ref_number": "REF09460"
    }
    ```
  - Example response:
    ```json
    {
      "shipment": {
        "reference_number": "ref09460",
        "origin": "denver, co",
        "destination": "detroit, mi",
        "equipment_type": "dry van",
        "rate": 868.0,
        "commodity": "automotive parts"
      }
    }
    ```

### Lane and Equipment Search
- `POST /shipment/by_lane_and_equipment/`
  - Searches shipments by origin, destination, and equipment type
  - Requires API key authentication
  - Request body:
    ```json
    {
      "origin": "denver, co",
      "destination": "detroit, mi",
      "equipment_type": "dry van"
    }
    ```

### Carrier Verification
- `POST /verify_carrier/`
  - Verifies carrier MC number
  - Requires API key authentication
  - Request body:
    ```json
    {
      "mc_number": "MC123456"
    }
    ```

## Authentication

All endpoints (except the root endpoint) require API key authentication. Include the API key in the request header:

```bash
X-API-Key: your-api-key-here
```

Example curl request:
```bash
curl -X 'POST' \
  'http://localhost:8000/shipment/' \
  -H 'Content-Type: application/json' \
  -H 'X-API-Key: xxxx' \
  -d '{
  "ref_number": "REF09460"
}'
```

## Project Structure

```
happy-robot-challenge/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── csv_loader.py
│   ├── models/
│   │   └── models.py
│   ├── load_checker/
│   │   └── data_access/
│   │       └── pandas_accessor.py
│   └── validate_carrier/
│       └── carrier_verifier.py
├── Dockerfile
└── requirements.txt
```



## License

[Add your license information here]
