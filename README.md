```markdown
# UK OSINT Data Harvester

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Issues](https://img.shields.io/github/issues/freedumbanddumbocracy/UK-OSintbc)](https://github.com/freedumbanddumbocracy/UK-OSintbc/issues)
[![Stars](https://img.shields.io/github/stars/freedumbanddumbocracy/UK-OSintbc)](https://github.com/freedumbanddumbocracy/UK-OSintbc/stargazers)

## Overview

UK OSINT Data Harvester is a professional-grade open-source intelligence (OSINT) tool designed for automated data collection from UK-specific sources. It scrapes and aggregates information from Companies House, 192.com, property listing sites (Rightmove, Zoopla, Land Registry), social media platforms (LinkedIn, GitHub, Twitter/X), and email intelligence services. The tool generates comprehensive reports in JSON, CSV, and text formats, making it ideal for researchers, investigators, and data analysts.

**Note**: This tool is intended for ethical research purposes only. Ensure compliance with all relevant laws, regulations, and platform terms of service. The developers assume no liability for misuse.

### Features

- **Automated Data Collection**: Scrapes real data from multiple UK sources with concurrent processing for efficiency.
- **Sources Supported**:
  - Companies House (company names, numbers, addresses).
  - 192.com (people search, limited by anti-bot measures).
  - Property sites (Rightmove listings, Zoopla and Land Registry notes).
  - Social media (LinkedIn, GitHub profiles, Twitter/X presence).
  - Email intelligence (validation, disposable check, domain info, breach notes).
- **Professional Logging**: Detailed logging with timestamps and file rotation for debugging.
- **Anti-Bot Evasion**: User-agent rotation to avoid detection.
- **Report Generation**: Outputs in JSON, CSV, and human-readable text with summaries of successes and failures.
- **Verbose Mode**: Optional detailed output for troubleshooting.
- **Extensibility**: Easy to extend with additional sources.

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/freedumbanddumbocracy/UK-OSintbc.git
   cd UK-OSintbc
   ```

2. **Install Dependencies**:
   Ensure Python 3.8+ is installed. Run:
   ```
   pip install -r requirements.txt
   ```
   Requirements:
   - requests
   - beautifulsoup4
   - fake-useragent
   - python-dotenv (for API keys, if used)
   - whois (optional for domain info)

3. **Setup Environment**:
   - Create a `.env` file for any API keys (e.g., for breach checking).
   - Example `.env`:
     ```
     HIBP_API_KEY=your_haveibeenpwned_key
     ```

## Usage

Run the tool with command-line arguments. At least one target identifier is required.

### Basic Examples
- Search by name and postcode:
  ```
  python uk_osint_harvester.py --name "John Smith" --postcode "SW1A 1AA"
  ```

- Search by company number:
  ```
  python uk_osint_harvester.py --company-number "12345678" --name "ACME Ltd"
  ```

- Search with email:
  ```
  python uk_osint_harvester.py --name "Jane Doe" --email "jane@example.co.uk"
  ```

- Verbose mode for detailed output:
  ```
  python uk_osint_harvester.py --name "John Smith" --verbose
  ```

### Output
The tool generates three files:
- JSON report (detailed data).
- CSV summary (source status and metrics).
- Text summary (human-readable overview).

Example output directory structure:
```
uk_osint_harvested_data_20250715_123456.json
uk_osint_harvested_data_20250715_123456.csv
uk_osint_harvested_summary_20250715_123456.txt
```

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add YourFeature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by open-source OSINT tools like SpiderFoot and Maltego.
- Uses libraries like BeautifulSoup for parsing and fake_useragent for evasion.

## Contact

For questions or support, open an issue on GitHub or contact [your email or contact info].

--- 
This README is maintained as of July 15, 2025. For the latest updates, visit the GitHub repository.