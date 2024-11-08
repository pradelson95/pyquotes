import random as rd
from quotesData import quotes
from colorama import Fore


class LimitQuoteError(Exception):
    pass 


class PyQuotes:
    quotes = quotes

    @classmethod
    def get_random_quote(cls):
        return rd.choice(cls.quotes)
    
    
    @classmethod
    def get_quote_by_author(cls, author_name):
        if not isinstance(author_name, str):
            raise ValueError(Fore.LIGHTRED_EX + f"El nombre del autor debe ser una cadena de texto.")
        quotes_by_author = [q for q in cls.quotes if q["author"].lower() == author_name.lower()]
        
        if not quotes_by_author:
            print(f"No se encontraron citas para el author {author_name}")

        return quotes_by_author
    
    
    @classmethod
    def get_amount_radom_authors(cls, amount):
        if not isinstance(amount, int):
            raise ValueError(Fore.LIGHTRED_EX + f" El tipo de dato debe ser entero")
        
        if amount > len(cls.quotes):
            raise LimitQuoteError(Fore.LIGHTRED_EX + f" La cantidad solicitada es mayor al número de citas disponibles")

        amount_authors = rd.sample(cls.quotes, amount)
        for quote in amount_authors:
            print(Fore.LIGHTYELLOW_EX + quote["author"] + " ----- " + Fore.LIGHTCYAN_EX + quote["quote"])
            
    
    @classmethod
    def count_quotes_by_author(cls, author_name):
        quotes_by_author =  [q for q in cls.quotes if q["author"].lower() == author_name.lower()]
        count = len(quotes_by_author)
        print(f"The author {author_name} has {count} amount of phrases")
        return count
    
    