from calculator import Calculator


def main():
    number1=5
    number2=7
    sum=Calculator.Sum(number1,number2)
    sub=Calculator.subtract(number1,number2)
    mul=Calculator.mulltiply(number1,number2)

    print(f"the summary is :{sum}")
    print(f"the subtract is :{sub}")
    print(f"the mulltiply is :{mul}")
    print("add stam line")

main()