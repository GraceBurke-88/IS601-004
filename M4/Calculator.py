class Calculator:
    ans = 0

    def _is_float(self, val):
        try:
            val = float(val)
            return True
        except:
            return False

    def _is_int(self, val):
        try:
            val = int(val)
            return True
        except:
            return False

    def _as_number(self, val):
        if self._is_int(val):
            return int(val)
        elif self._is_float(val):
            return float(val)
        else:
            raise Exception("Not a number")

    def add(self, num1, num2):
        if num1 == "ans":
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1+num2
        return self.ans

    def sub(self, num1, num2):
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    def mult(self, num1, num2):
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans

    def div(self, num1, num2):
        if num1 == "ans":
            return self.div(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            if num2 == 0:
                print("Can't divide by zero, sorry")
            else:
                self.ans = num1/num2
        return self.ans



if __name__ == '__main__':
    is_running = True
    user_input = input("Are you ready?")
    calc = Calculator()
    print(calc)
    if user_input == "yes":
        while is_running:
            user_input = input("Input your equation:")
            if user_input == "quit" or user_input == "q":
                is_running = False
            else:
                print("Your eq was " + str(user_input))
                if "+" in user_input:
                    nums = user_input.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    print("Result is " + str(r))
                # must be done before - check to hanlde negative values
                elif "/" in user_input:
                    nums = user_input.split("/")
                    r = calc.div(nums[0].strip(), nums[1].strip())
                    print("Result is " + str(r))

                elif "*" in user_input or "x" in user_input:
                    nums = user_input.split("*") if "*" in user_input else user_input.split("x")
                    r = calc.mult(nums[0].strip(), nums[1].strip())
                    print("Result is " + str(r))
                # must be done last so negative numbers work
                elif "-" in user_input:
                    nums = user_input.split("-")
                    r = calc.sub(nums[0].strip(), nums[1].strip())
                    print("Result is " + str(r))




    else:
        print("Good bye")
        is_running = False
