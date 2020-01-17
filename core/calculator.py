from decorators import cache_decorator

@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b
    elif operation == '**':
        return a ** b
    else:
        raise ValueError


if __name__ == '__main__':
    try:
        print("To exit, press CTRL+C")
        while(True):
            a = int(input('Введите число: '))  # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
            b = int(input('Введите число: '))
            operation = input('Введите операцию: ')

            print('Результат: ', calculator(a, b, operation))

    except ValueError:
        print("Incorrect input.\nUsage:\n"
              "Введите число: [number]\n"
              "Введите число: [number]\n"
              "Введите операцию: [+, -, /, *, **]")
    except ZeroDivisionError:
        print("Division by zero")
    except KeyboardInterrupt:
        print("\nGoodbye")
