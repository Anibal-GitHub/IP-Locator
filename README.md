# IP-Locator

## IP Info Finder

This project is a Python tool to obtain detailed information about an IP address using the [ip-api.com](http://ip-api.com/) API. The tool also saves the collected data, including the date of the query, in a CSV file.

## Description

The tool allows you to enter an IP address and obtain relevant information such as the Internet Service Provider (ISP), city, country, region, and timezone. Additionally, it saves this data along with the date of the query in a CSV file.

## Requirements

- Python 3.x
- Standard Python modules (`os`, `urllib.request`, `json`, `csv`, `datetime`)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Anibal-GitHub/IP-Locator.git
    cd IP-Info-Finder
    ```

2. Make sure you have Python 3.x installed on your system.

## Usage

Run the `ip_info_finder.py` script from your terminal or command line:

```bash
python ip_info_finder.py



The script will prompt you to enter an IP address and then display the related information. The data will also be saved in the ip_info.csv file in the same directory.

Example
Here's an example of how to use the tool:
What is your target IP: 8.8.8.8
ISP: Google LLC
Data saved to ip_info.csv.


The ip_info.csv file will have content similar to this:
query,city,isp,country,region,timezone,date
8.8.8.8,Mountain View,Google LLC,United States,CA,America/Los_Angeles,2025-02-01 19:54:00


Notes
Make sure you have an internet connection so the tool can access the ip-api.com API.

The ip-api.com API has a limit on free queries. For more queries, consider subscribing to a paid plan.

Contributions
Contributions are welcome! If you have suggestions or find any issues, please open an issue or send a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.