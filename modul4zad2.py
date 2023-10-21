import logging

operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

a = float(input("Podaj składnik 1: "))
b = float(input("Podaj składnik 2: "))

result = 0

if operation == '1':
    result = a + b
    logging.info(f"Dodaję {a} i {b}")

if operation == '2':
    result = a - b
    logging.info(f"Odejmuję {a} i {b}")

if operation == '3':
    result = a * b
    logging.info(f"Mnożę {a} i {b}")


