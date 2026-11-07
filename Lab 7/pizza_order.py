
TOPPINGS = {
    "cheese": 40,
    "olives": 30,
    "onion": 20,
    "paneer": 50
}

SIZES = {
    "S": 8,
    "M": 10,
    "L": 12
}


def toppings_price(toppings_csv):
    if not isinstance(toppings_csv, str):
        return None

    toppings = toppings_csv.split(',')

    if not toppings or any(not t.strip() for t in toppings):
        return None

    total = 0

    for t in toppings:
        topping = t.strip().lower()

        if topping not in TOPPINGS:
            return None

        total += TOPPINGS[topping]

    return total


def pizza_inches(size):
    if not isinstance(size, str):
        return None

    size = size.strip().upper()

    if size not in SIZES:
        return None

    return SIZES[size]


def split_bill(text):
    if not isinstance(text, str):
        return None

    try:
        parts = text.split('/')

        if len(parts) != 2:
            return None

        total = int(parts[0].strip())
        people = int(parts[1].strip())

        if total < 0 or people <= 0:
            return None

        return round(total / people, 2)

    except ValueError:
        return None


def main():
    print("==== Running toppings_price ====")
    user_input = input("Enter toppings as CSV (e.g. cheese,olives): ")
    result = toppings_price(user_input)

    if result is None:
        print("Invalid toppings entered!")
    else:
        print("Toppings Price:", result)

    print("\n==== Running pizza_inches ====")
    user_input = input("Enter pizza size (S/M/L): ")
    result = pizza_inches(user_input)

    if result is None:
        print("Invalid pizza size!")
    else:
        print("Size in Inches:", result)

    print("\n==== Running split_bill ====")
    user_input = input("Enter total and people (e.g. 900/3): ")
    result = split_bill(user_input)

    if result is None:
        print("Invalid bill details!")
    else:
        print("Per Person:", result)


if __name__ == "__main__":
    main()
