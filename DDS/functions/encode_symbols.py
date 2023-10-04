# Функція для кодування символу
def encode(symbol, symbols_table):
    if symbol in symbols_table:
        return symbols_table[symbol]
    else:
        return None
