# Wildfire Visualization Over Time

This project is a real-time and historical wildfire monitoring and analysis application that leverages NASA's FIRMS data. The project displays current wildfire detections on an interactive map and provides historical trends via aggregated charts and maps.

## Overview

- **Real-Time Visualization:**  
  Displays current wildfire hotspots on an interactive map using Leaflet. Markers are color-coded based on confidence levels.

- **Historical Analysis:**  
  Uses aggregated historical data (queried from DynamoDB via an AWS Lambda/API Gateway endpoint) to generate interactive charts showing trends in total fires, average brightness, and average confidence over selected time ranges (past week, month, or year). Additionally, a historical map displays individual fire events from raw data.

## Data Sources

- **NASA FIRMS:**  
  Real-time fire detections are pulled from NASA’s FIRMS CSV API.
- **DynamoDB:**  
  Historical and aggregated wildfire data are stored in a DynamoDB table.
- **AWS Services:**  
  AWS Lambda functions (for data ingestion and aggregation) and API Gateway are used to manage and expose the backend data.

## Technologies Used

- **Frontend:**  
  - HTML, CSS, and JavaScript  
  - [Leaflet](https://leafletjs.com/) for interactive mapping  
  - [Chart.js](https://www.chartjs.org/) for data visualization  
  - [PapaParse](https://www.papaparse.com/) for CSV parsing

- **Backend:**  
  - AWS Lambda (Python)  
  - DynamoDB for data storage  
  - API Gateway for exposing API endpoints

## Future Enhancements

- Enhance the aggregation logic to include more detailed metrics and average geolocation data.
- Improve UI interactivity and add more filters.
- Scale the application to incorporate additional data sources and predictive analytics.

## Setup

1. **Backend Setup:**  
   - Configure AWS Lambda functions to ingest and aggregate wildfire data.
   - Set up a DynamoDB table and API Gateway endpoints for both raw and aggregated data.

2. **Frontend Setup:**  
   - Host the static site (using GitHub Pages or similar) and integrate the maps, charts, and API calls.

3. **Testing and Deployment:**  
   - Verify API responses, map marker rendering, and chart updates.
   - Deploy updates as needed.

---

This project serves as both a portfolio piece and a tool for understanding the spatial and temporal dynamics of wildfires. Enjoy exploring the data!