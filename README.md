# Geocoding ETL Pipeline

A robust and scalable ETL pipeline built with **Apache Airflow** to enrich address data using the **LocationIQ API**. This project demonstrates best practices in data engineering, including modular code structure, efficient memory management using Python generators, and resilient API integration.

## Features
- **Scalable Extraction**: Reads multiple JSON files from a directory using Python generators to maintain a low memory footprint.
- **Resilient Transformation**: Integrated with LocationIQ API with built-in retry logic and smart error handling (skips invalid addresses to save API quota).
- **Atomic Loading**: Consolidates processed data into a single, clean JSON output.
- **Containerized Environment**: Fully dockerized setup for consistent deployment across different machines.



## Project Structure

```bash 
.
├── dags/
│   └── etl_geocode.py         # Main Airflow DAG definition
├── src/
│   ├── integrations/
│   │   └── geocode_util.py    # LocationIQ API integration logic
│   ├── transformers/
│   │   └── address_transformer.py # Data enrichment & transformation
│   └── utils/
│       ├── reader.py          # File extraction utility
│       └── writer.py          # Data loading utility
├── data/
│   ├── int_test_input/        # Raw JSON input files
│   └── int_test_output/       # Enriched JSON output
├── .env                       # API Credentials (ignored by git)
├── docker-compose.yaml        # Infrastructure as code
└── requirements.txt           # Python dependencies
```

##  Setup & Installation
### 1. Prerequisites
Docker & Docker Compose installed.

A LocationIQ API Key (Get one at locationiq.com).

### 2. Configuration
Create a .env file in the root directory and add your API key without quotes:

```bash
LOCATIONIQ_API_KEY=your_api_access_token_here
```

### 3. Deployment
Launch the Airflow environment:

```bash
docker-compose up -d
```

### 4. Running the Pipeline
Access the Airflow UI at http://localhost:8080 (Default: admin/admin).

Unpause the DAG named etl_geocode.

Trigger the DAG manually to start the ETL process.


## Technical Decisions
### API Resilience
Retry Logic: Implements exponential backoff for network/server errors.

### 404 Handling 
The system intelligently identifies invalid addresses and skips them immediately without retrying, preserving API rate limits.
