import os
import urllib.request as urllib2
import json
import csv
from datetime import datetime

def get_ip_info(ip):
    url = "http://ip-api.com/json/"
    try:
        response = urllib2.urlopen(url + ip)
        data = response.read()
        values = json.loads(data)
        return values
    except urllib2.URLError as e:
        print(f"Network error: {e}")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON response")
        return None

def save_to_csv(data, filename='ip_info.csv'):
    file_exists = os.path.isfile(filename)
    with open(filename, mode='a', newline='') as file:
        fieldnames = ['query', 'city', 'isp', 'country', 'region', 'timezone', 'date']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if not file_exists:
            writer.writeheader()  # Write the header only if the file didn't exist before

        writer.writerow({
            'query': data['query'],
            'city': data['city'],
            'isp': data['isp'],
            'country': data['country'],
            'region': data['region'],
            'timezone': data['timezone'],
            'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Add current date and time
        })

while True:
    ip = input("What is your target IP: ")

    if not ip:
        print("Please enter a valid IP address.")
        continue

    values = get_ip_info(ip)

    if values:
        if values["status"] == "fail":
            print(f"Error: {values['message']}")
        else:
            print(f"ISP: {values['isp']}")
            save_to_csv(values)  # Save the data to CSV
            print("Data saved to ip_info.csv.")
            break
    else:
        print("Failed to retrieve IP information. Please try again.")

