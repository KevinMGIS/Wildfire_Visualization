import requests
import csv
import boto3
import io
import time
from decimal import Decimal

# Configure your DynamoDB resource (adjust region if necessary)
dynamodb = boto3.resource('dynamodb', region_name='us-east-2')
table = dynamodb.Table('WildfireData')  # Replace with your table name

# URL for the historical CSV file from FIRMS
url = "https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_USA_contiguous_and_Hawaii_7d.csv"

# Download the CSV file
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to download CSV file. Status code: {response.status_code}")
    exit(1)

csv_text = response.text
csv_file = io.StringIO(csv_text)

# Use csv.DictReader to parse the CSV file
reader = csv.DictReader(csv_file)

# Process each record and insert into DynamoDB
count = 0
for record in reader:
    try:
        # Example: Convert latitude and longitude to floats (you might have different field names)
        latitude = float(record.get('latitude', ''))
        longitude = float(record.get('longitude', ''))
    except (ValueError, TypeError):
        continue  # Skip records without valid coordinates

    # Create a unique RecordID (for example, combining date, time, and coordinates)
    acq_date = record.get('acq_date', '')
    acq_time = record.get('acq_time', '')
    record_id = f"{acq_date}_{acq_time}_{latitude:.2f}_{longitude:.2f}"

    # Build the item. Convert numeric values to Decimal (DynamoDB requires Decimal for numbers)
    item = {
        'RecordID': record_id,
        'Timestamp': int(time.time()),  # Or use a field from the record if available
        'latitude': Decimal(str(latitude)),
        'longitude': Decimal(str(longitude)),
        'brightness': Decimal(str(record.get('brightness', '0'))),
        'confidence': Decimal(str(record.get('confidence', '0'))),
        'acq_date': acq_date,
        'acq_time': acq_time
    }

    try:
        table.put_item(Item=item)
        count += 1
    except Exception as e:
        print(f"Error inserting record {record_id}: {e}")

print(f"Successfully imported {count} records into DynamoDB.")