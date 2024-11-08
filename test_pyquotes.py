import pytest

from pyquotes import PyQuotes, LimitQuoteError


#Verifica que el método get_random_quote devuelve un diccionario 
# con las claves "author" y "quote".
def test_get_random_quote():
    quote = PyQuotes.get_random_quote()
    assert isinstance(quote, dict)
    assert "author" in quote
    assert "quote" in quote


#test_get_quote_by_author_valid: Prueba get_quote_by_author 
#con un autor conocido y verifica que las citas devueltas corresponden al autor.
def test_get_quote_by_author_valid():
    quotes = PyQuotes.get_quote_by_author("Pradelson Francois")
    assert isinstance(quotes, list)
    for quote in quotes:
        assert quote["author"].lower() == "Pradelson Francois".lower()


#test_get_quote_by_author_invalid: Prueba get_quote_by_author con un autor 
# desconocido y verifica que devuelve una lista vacía.
def test_get_quote_by_author_invalid():
    quotes = PyQuotes.get_quote_by_author("Unknown Author")
    assert quotes == []


#test_get_quote_by_author_type_error: Verifica 
#que el método lanza un ValueError cuando se pasa un tipo incorrecto.
def test_Value_Error():
    with pytest.raises(TypeError):
        PyQuotes.get_random_quote(1)


#test_get_amount_radom_authors_valid: Llama al método get_amount_radom_authors 
#con una cantidad válida y no espera errores.
def test_get_amount_radom_authors_valid():
    PyQuotes.get_amount_radom_authors(4)


#test_get_amount_radom_authors_invalid_type: Verifica que el método 
#lanza un ValueError cuando se pasa un tipo incorrecto.
def test_get_amount_radom_authors_invalid_type():
    with pytest.raises(ValueError):
        PyQuotes.get_amount_radom_authors("five")


#test_get_amount_radom_authors_limit_error: Verifica que el método lanza un 
# LimitQuoteError cuando se solicita más citas de las disponibles.
def test_get_amount_radom_authors_limit_error():
    with pytest.raises(LimitQuoteError):
        PyQuotes.get_amount_radom_authors(1000) 



#test_count_quotes_by_author: Verifica que el método count_quotes_by_author 
# devuelve un número entero mayor o igual a cero.
def test_count_quotes_by_author():
    count = PyQuotes.count_quotes_by_author("Albert Einstein")
    assert isinstance(count, int)
    assert count >= 0