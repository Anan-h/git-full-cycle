class Calculator:
    @staticmethod
    def Sum(number1,number2):
        return number1+number2

    @staticmethod
    def subtract(number1,number2):
        return (max(number1,number2)-min(number1,number2))

    @staticmethod
    def mulltiply(number1,number2):
        return number1*number2