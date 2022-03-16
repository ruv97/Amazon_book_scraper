# Amazon_goodreads_book_scraper

I have build a personal price tracker automation, which can scrape our favorite books from goodreads,keep track of it’s prices on amazon.in daily and notifies us if there are huge drops in the prices.

To scrape goodreads.com and amazon.in to build a price-change / price tracker script. If we login to goodreads and go to My book > Want to Read.

## For running this program you will need to install the following libraries

- selenium
- webdriver
- pandas
- beautifulSoup

I have created 3 files.

**1.goodreads_scraper.py**

- Download ALL “Want to read” books from goodreads.
- Place it in the csv file, with as much metadata I can collect (eg: bookname, editor, avg rating etc).

**2.amazon_scraper.py**

- This takes “books_goodreads.csv” and scrapes amazon.in for the name of the book.
- Selenium will type on the search screen the book name one by one.

**3. price_diff.py**

- append today’s date (fetched from constants.py for simulation purposes) to books_amazon_goodreads.csv so that it becomes `books_amazon_goodreads_dd_mm_yyyy.csv`
- execute the second script again by incrementing the constant date by 1 resulting in another books_amazon_goodreads_dd_mm_yyyy.csv.
- third script will picks same date from constants, and reads currentday, currentday-1 files
- then go to the latest day’s file and row by row (pandas dataframes), go over it. We compare today’s price for kindle, amazon, paperback with previous day prices, and if any of these prices are lower by a certain amount (eg: 5% drop, defined in constants again), we move that row to a new dataframe. This time, we store the current day’s price + the previous day’s price in that category in another column in the csv. We do this for all the categories.

