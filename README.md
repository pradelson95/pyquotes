# PyQuotes

PyQuotes is a Python library designed to help you manage and retrieve quotes from famous authors. It allows you to fetch random quotes, search for quotes by a specific author, count quotes per author, and more. The library is simple to use and comes with custom error handling.

## Features

- **Get Random Quote**: Retrieve a random quote from a collection.
- **Get Quotes by Author**: Fetch all quotes from a specified author.
- **Count Quotes by Author**: Count how many quotes are available for a specific author.
- **Custom Error Handling**: Includes handling for invalid types and limits on the number of quotes requested.

## Installation

To use PyQuotes, you can either install it directly from the GitHub repository or create your own project that includes it.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/PyQuotes.git


2. **Get a random quote**

   ```bash
   from PyQuotes import PyQuotes
   
   quote = PyQuotes.get_random_quote()
   print(quote)  # Prints a random quote with author

3. **Get Quotes by Author**
   
   
   ```bash
   from PyQuotes import PyQuotes

   quotes = PyQuotes.get_quote_by_author("Albert Einstein")
   for quote in quotes:
    print(quote["quote"])


3. **Get a Specific Number of Random Quotes**
   
   
   ```bash
   from PyQuotes import PyQuotes
    
   PyQuotes.get_amount_radom_authors(5)  # Prints 5 random quotes



4. **Count Quotes by Author**
   
   
   ```bash
   from PyQuotes import PyQuotes

    count = PyQuotes.count_quotes_by_author("Albert Einstein")
    print(f"Albert Einstein has {count} quotes")