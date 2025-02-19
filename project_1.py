import requests
from openpyxl import Workbook

def fetch_api_data(url):
    """Fetch data from the given API URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def process_and_combine_data(api1_data, api2_data):
    """Process and combine data from two APIs in a meaningful way."""
    combined_data = []

    # Example: Combine country details (API1) with weather data (API2)
    for country in api1_data.get('countries', []):
        country_name = country.get('name')
        weather_info = next((info for info in api2_data.get('weather', []) if info.get('country') == country_name), None)

        if weather_info:
            combined_data.append({
                'Country': country.get('name'),
                'Capital': country.get('capital'),
                'Region': country.get('region'),
                'Weather': weather_info.get('description'),
                'Temperature': weather_info.get('temperature')
            })
    
    return combined_data

def write_to_excel(data, filename="output.xlsx"):
    """Write combined data to an Excel file using Openpyxl."""
    wb = Workbook()
    ws = wb.active
    ws.title = "Combined Data"

    # Write headers
    headers = ["Country", "Capital", "Region", "Weather", "Temperature"]
    ws.append(headers)

    # Write data rows
    for entry in data:
        ws.append([entry.get(header, "") for header in headers])

    # Save workbook
    wb.save(filename)
    print(f"Data written to {filename}")

if __name__ == "__main__":
    # API endpoints (replace with actual API URLs)
    api1_url = "https://restcountries.com/v3.1/all"
    api2_url = "https://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q=London&aqi=no"

    # Fetch data from APIs
    api1_data = fetch_api_data(api1_url)
    api2_data = fetch_api_data(api2_url)

    if api1_data and api2_data:
        # Process and combine data
        combined_data = process_and_combine_data(api1_data, api2_data)

        # Write combined data to Excel
        write_to_excel(combined_data)
    else:
        print("Failed to fetch data from one or both APIs.")
 