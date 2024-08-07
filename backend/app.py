from flask import Flask, jsonify
from flask_cors import CORS
import threading
import time
import redis
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def fetchData():
    url = "https://www.nseindia.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    while True:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all tables
        tables = soup.find_all('table')
        all_tables_data = []
        
        for idx, table in enumerate(tables):
            table_data = {}
            # table_data['name'] = f'Table {idx + 1}'
            rows = table.find_all('tr')
            table_data['rows'] = []
            
            for row in rows:
                cols = row.find_all('td')
                cols_text = []
                for ele in cols:
                    cols_text.append(ele.text.strip())
                filtered_cols = []
                for ele in cols_text:
                    if ele:
                        filtered_cols.append(ele)
                if filtered_cols:  # Only add non-empty rows
                    table_data['rows'].append(filtered_cols)

            if table_data['rows']:  # Only add non-empty tables
                all_tables_data.append(table_data)
        
        # Store data in Redis
        redis_client.set('all_tables_data', str(all_tables_data))
        
        # Wait for 5 minutes before fetching the data again
        time.sleep(300)

# Start the background thread
thread = threading.Thread(target=fetchData)
thread.daemon = True
thread.start()

@app.route('/api/getData', methods=['GET'])
def getScrappedData():
    # Fetch data from Redis
    data = redis_client.get('all_tables_data')
    if data:
        all_tables_data = eval(data)  # Convert string back to list
    else:
        all_tables_data = []
    return jsonify(all_tables_data)

if __name__ == '__main__':
    app.run(debug=True)