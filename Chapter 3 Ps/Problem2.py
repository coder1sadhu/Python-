letter = '''Dear <|NAME|>,
You are selected!
Date: <|DATE|>'''

print(letter.replace("<|NAME|>", "Hansal").replace("<|DATE|>", "20/06/2024"))