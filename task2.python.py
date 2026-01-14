
import math
def display_me():
    print("\n----- Calculator -----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power (x^y)")
    print("6. Square Root")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("10. Logarithm")

def get_ch():
    try:
        return int(input("Enter choice (1-10): "))
    except ValueError:
        return None

def main():
    while True:
        display_me()
        cho = get_ch()
        if cho not in range(1, 11):
            print("Invalid option. Exiting calculator.")
            break
        if cho in [1, 2, 3, 4, 5]:
            try:
                n1 = float(input("Enter first number: "))
                n2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers.")
                continue

            if cho == 1:
                print("Result =", n1 + n2)
            elif cho == 2:
                print("Result =", n1 - n2)
            elif cho == 3:
                print("Result =", n1 * n2)
            elif cho == 4:
                if n2 != 0:
                    print("Result =", n1 / n2)
                else:
                    print("Error: Cannot divide by zero!")
            elif cho == 5:
                print("Result =", math.pow(n1, n2))

       
        else:
            try:
                n = float(input("Enter number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if cho == 6:
                print("Result =", math.sqrt(n))
            elif cho == 7:
                print("Result =", math.sin(math.radians(n)))
            elif cho == 8:
                print("Result =", math.cos(math.radians(n)))
            elif cho == 9:
                print("Result =", math.tan(math.radians(n)))
            elif cho == 10:
                if n > 0:
                    print("Result =", math.log(n))
                else:
                    print("Error: Logarithm undefined for non-positive numbers.")

    print("Calculator closed.")
if __name__ == "__main__":
    main()
