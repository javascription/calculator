# Calculator #

def main()
    while True
        print(Hello! Welcome To The Calculator)
        print(Enter )
        print(+ To add)
        print(- To subtract)
        print( To multiply)
        print( To divide)
        print(Type 'exit' to stop)

        inpt = input(What operation would you like to perform )

        try
            inpt1 = float(input(First Number ))
            inpt2 = float(input(Second Number ))
        except ValueError
            print(Invalid input. Please enter numeric values.)
            continue

        if inpt == +
            print(add(inpt1, inpt2))
        elif inpt == -
            print(subtract(inpt1, inpt2))
        elif inpt == 
            print(multiply(inpt1, inpt2))
        elif inpt == 
            if inpt2 == 0
                print(Error Cannot divide by zero.)
                continue
            else
                print(divide(inpt1, inpt2))
        else
            print(Wrong Value!)


def add(x, y)
    return x + y
def subtract(x, y)
    return x - y
def multiply(x, y)
    return x  y
def divide(x, y)
    return x  y

main()
