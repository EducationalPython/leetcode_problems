# LeetCode Problem Scraper

## Overview
This project is a web scraper that extracts problem descriptions from LeetCode and converts them into Markdown format. The script uses **Selenium** for web scraping, **BeautifulSoup** for HTML parsing, and **html2text** for Markdown conversion.

## Features
- Scrapes LeetCode problem descriptions
- Converts the extracted HTML into Markdown
- Saves the formatted description to `problem_description.md`
- Optionally includes the author's name in the output

## Requirements
Ensure you have the following dependencies installed:

```sh
pip install selenium beautifulsoup4 html2text
```

You also need **Google Chrome** installed and the **Chrome WebDriver** that matches your browser version. Download it from:
[ChromeDriver Download](https://sites.google.com/chromium.org/driver/)

## Usage
### Running the Scraper
The main script is `scraper.py`, and it can be run manually using:

```sh
python scraper.py --link "<leetcode_problem_url>" --author "Your Name"
```

Alternatively, you can use the provided `run.sh` script to automate execution:

### Running with `run.sh`

```sh
chmod +x run.sh
./run.sh
```

### Example
Example command:

```sh
python scraper.py --link "https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/" --author "Abubakir Koshek. email: koshek[dot]a[at][phystech default mail]"
```

This will generate `problem_description.md` containing:
- The problem title
- The problem description
- The author's name (if provided)

## File Structure
```
project_root/
│── src/
│   ├── scraper.py  # Main scraping script
│── run.sh          # Script to execute the scraper
│── problem_description.md  # Output Markdown file
│── README.md       # Documentation
```

## Notes
- The scraper waits for 5 seconds to allow dynamic content to load.
- If the scraping fails, a failure message will be displayed.
- The script doesn't run in "headless" mode, I think it is bot detection from leetcode.

## Author
Developed by **Abubakir Koshek**

For any issues, feel free to contact via email: `koshek[dot]a[at][phystech default mail]`
