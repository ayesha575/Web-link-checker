# Web Link Checker

A lightweight Python utility designed to scan and verify the operational status of multiple web links automatically. This tool helps web administrators and SEO professionals identify broken URLs (404 errors) and ensure website health.

## Features

- **Automated Scanning:** Reads a list of URLs from a local text file (`urls.txt`).
- **HTTP Status Check:** Sends requests to check each URL's HTTP response status code (e.g., `200 OK`).
- **Error Handling:** Gracefully handles invalid URLs, network timeouts, and broken links with standard error logging.
- **Timeout Management:** Uses a 5-second timeout limit to prevent hanging on unresponsive servers.

## Tech Stack

- **Language:** Python 3
- **Libraries:** `requests`

## Getting Started

### Prerequisites

Ensure you have Python installed on your system along with the `requests` library:

```bash
pip install requests
