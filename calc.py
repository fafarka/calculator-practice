def main():
    print("Консольный калькулятор")

    a = input("Введите первое число: ")
    b = input("Введите второе число: ")

    a = int(a)
    b = int(b)

    op = input("Введите операцию (+, -, *, /): ")

    if op == '+':
        x = a + b
        print("Результат:", x)
    elif op == '-':
        x = a + b
        print("Результат:", x )
    elif op == '*':
        x = a + b
        print("Результат:", x )
    elif op == '/':
        x = a + b
        print("Результат:", x )
    else:
        print("Неизвестная операция")

    if op in ['+', '-', '*', '/']:
        print("Результат (повторно):", x )

if __name__ == "__main__":
    main()
