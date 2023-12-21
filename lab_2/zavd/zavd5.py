# Перевірка числа на парність
number = 7

if number % 2 == 0:
    print(number, "є парним числом.")
else:
    print(number, "є непарним числом.")

# Оцінка оцінки студента
grade = 85

if grade >= 90:
    print("Оцінка A")
elif grade >= 80:
    print("Оцінка B")
elif grade >= 70:
    print("Оцінка C")
elif grade >= 60:
    print("Оцінка D")
else:
    print("Оцінка F")

# Перевірка числа на діленість на 2 і 3 одночасно
number = 15

if number % 2 == 0:
    if number % 3 == 0:
        print(number, "ділиться як на 2, так і на 3.")
    else:
        print(number, "ділиться на 2, але не ділиться на 3.")
else:
    if number % 3 == 0:
        print(number, "ділиться на 3, але не ділиться на 2.")
    else:
        print(number, "не ділиться ані на 2, ані на 3.")
