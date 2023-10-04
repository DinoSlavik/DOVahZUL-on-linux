import functions.encode_symbols as encode_symbols
import functions.decode_symbols as decode_symbols
import json

symbols_table_path = "./symbols_table.json"

if __name__ == "__main__":
    with open(symbols_table_path, "r") as f:
        symbols_table = json.loads(f.read())

    test_text = "DOVah VaaK ALDUIN"

    # Кодування тексту
    encoded_text = [encode_symbols.encode(char, symbols_table) for char in test_text]

    # Виведення результату
    print("Текст після кодування:", encoded_text)

    # Декодування тексту
    decoded_text = [decode_symbols.decode(code, symbols_table) for code in encoded_text]

    # Виведення результату
    print("Текст після декодування:", "".join(decoded_text))
