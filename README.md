# Nifty 50 Scraper and Dashboard

This project scrapes the "Nifty 50" data from the NSE India website every 5 minutes, stores the data in a Redis instance, and displays the data on a web app built with Angular and Flask.

## Project Structure

- `backend/`: Contains the Flask application that scrapes the data and serves it via an API.
- `web_scraper/`: Contains the Angular application that fetches and displays the data.

## Prerequisites

- Python 3.x
- Node.js and npm
- Redis server
- Angular CLI

## How It Works

### Flask Application

- **Scraper:** The `fetchData` function in `app.py` runs in a background thread and scrapes data from the NSE India website every 5 minutes. The data is parsed using BeautifulSoup, filtered for non-empty tables, and stored in Redis.
- **API Endpoint:** The `/api/getData` endpoint retrieves the stored data from Redis and returns it as a JSON response.

### Angular Application

- **Data Service:** The `DataService` in `src/app/data.service.ts` makes an HTTP GET request to the Flask API endpoint to fetch the data.
- **Component:** The `AppComponent` in `src/app/app.component.ts` uses the `DataService` to get the data and display it in a card layout.

## Running the Applications

1. **Ensure Redis server is running:**
    ```bash
    redis-server
    ```

2. **Run the Flask backend:**
    ```bash
    cd backend
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    python app.py
    ```

3. **Run the Angular frontend:**
    ```bash
    cd web_scraper
    ng serve
    ```

4. **Visit the application in your browser:**
    ```url
    http://localhost:4200
    ```

## Example Data Structure

    The data returned by the backend and displayed by the frontend should have the following structure:
    ```json
    [
    {
        "name": "Table 1",
        "rows": [
        ["Column1", "Column2", "Column3"],
        ["Value1", "Value2", "Value3"]
        ]
    },
    {
        "name": "Table 2",
        "rows": [
        ["Column1", "Column2", "Column3"],
        ["Value1", "Value2", "Value3"]
        ]
    }
    ]

## Troubleshooting

	•	Connection Refused Error:
            Ensure that the Redis server is running before starting the Flask application.
	•	CORS Issues:
            The Flask application uses flask_cors to enable CORS. Ensure this is properly set up to allow requests from the Angular frontend.
