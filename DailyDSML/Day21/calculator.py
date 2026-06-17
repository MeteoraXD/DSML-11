class Calculator:
    def __init__(self, num1, num2, operator):
        self.num1 = num1
        self.num2 = num2
        self.operator = operator

    def calc(self):
        if self.operator == '+':
            return self.num1 + self.num2
        elif self.operator == '-':
            return self.num1 - self.num2
        elif self.operator == '*':
            return self.num1 * self.num2
        elif self.operator == '/':
            if self.num2 == 0:
                return 'Cannot be divisible by 0'
            return self.num1 / self.num2
        else:
            return 'Invalid Operator'