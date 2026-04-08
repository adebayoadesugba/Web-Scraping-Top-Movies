# 🎬 Top 100 Movies Web Scraper (Python Web Scraping Project)

A Python web scraping project that **extracts the Top 100 movies list from Empire Online** and saves the results into a text file.

The script sends a request to the Empire Online website, parses the HTML using **BeautifulSoup**, extracts movie titles, organizes them in the correct ranking order, and writes them to a `.txt` file.

This project demonstrates **practical web scraping techniques using Python**, including HTTP requests, HTML parsing, and data extraction.

---

## Features

- 🌐 Scrapes movie data directly from a live website
- 🧠 Parses HTML content using BeautifulSoup
- 📋 Extracts the Top 100 movie titles
- 🔄 Reorders results from **1 → 100**
- 💾 Saves the scraped data to a text file
- 🛡 Uses browser headers to avoid request blocking

---

## Technologies Used

- Python 3
- Requests (HTTP requests)
- BeautifulSoup (HTML parsing)
- File Handling

---

## Project Structure

```bash
100-movies-scraped/
│
├── main.py        # Web scraping script
├── movies.txt     # Output file containing the movie list
│
└── README.md
