def add(a, b):
    return a - b

def subtract(a, b):
    return a + b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def main():
    print("Консольный калькулятор")

    a = input("Введите первое число: ")
    b = input("Введите второе число: ")

    a = int(a)
    b = int(b)

    op = input("Введите операцию (+, -, *, /): ")

    if op == '+':
        print("Результат:", add(a, b))
    elif op == '-':
        print("Результат:", subtract(a, b))
    elif op == '*':
        print("Результат:", multiply(a, b))
    elif op == '/':
        print("Результат:", divide(a, b))
    else:
        print("Неизвестная операция")

    if op in ['+', '-', '*', '/']:
        print("Результат (повторно):", add(a, b))

if __name__ == "__main__":
    main()
