<h1 align="center">IMDb Top Movies Scraper</h1>

<div align="center">
  <strong>Scrape and extract data from IMDb's top 250 movies chart with ease!</strong>
</div>

<br>

<div align="center">
  <!-- Add badges here -->
  <img alt="GitHub last commit" src="https://img.shields.io/github/last-commit/HossamMohamed12/imdb-top-movies-scraper">
  <img alt="GitHub license" src="https://img.shields.io/github/license/HossamMohamed12/imdb-top-movies-scraper">
</div>

<br>
## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Introduction
This Scrapy project is designed to scrape the top 250 movies from IMDb, extracting key details such as title, genres, release date, age rating, duration, rating, and reviews count. The project includes a Spider (`movies`) to crawl IMDb's top movies chart page and parse individual movie pages, an Item class (`TopMoviesItem`) for defining scraped data fields, and a Pipeline (`SaveToDatabasePipeline`) to save the scraped data to a SQLite database.

## Features
- Scrape and extract data from IMDb's top 250 movies chart.
- Extract details including title, genres, release date, age rating, duration, rating, and reviews count.
- Utilize Scrapy's powerful features for efficient web scraping.
- Save scraped data to a SQLite database for further analysis and visualization.
- Customize data processing and output using ItemLoaders and Pipelines.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/imdb-top-movies-scraper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd imdb-top-movies-scraper
   ```
3. Install project dependencies:
   ```bash
   pip install -r requirements.txt
   ```
## Usage
1.Run the spider:
```bash
scrapy crawl movies
```
2.Sit back and relax while the spider scrapes IMDb's top movies data.
3.Once scraping is complete, the data will be saved to a SQLite database (movies.db) in the project directory.
## Contribution
Contributions are welcome! If you have suggestions or want to add features, feel free to open an issue or submit a pull request.
## License
This project is licensed under the MIT License.
