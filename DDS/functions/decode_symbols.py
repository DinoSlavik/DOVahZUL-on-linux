# Функція для декодування коду в символ
def decode(code, symbols_table):
    for symbol, symbol_code in symbols_table.items():
        if code == symbol_code:
            return symbol
    return None

