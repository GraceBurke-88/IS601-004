class Calculator:
    """
    gnb5 implemented on 2/26/23
    A simple calculator that performs basic arithmetic operations (add, subtract, multiply, divide)

    Note:
    - If the input string contains "ans" instead of a number, the previous answer
        will be used instead (or zero if no value has been provided).
    - Division by zero will result in an error message.
    """
        
    ans = 0

    def _is_float(self, val):
        """
        gnb5 implemented on 2/26/23
        Check if the given value is a float.
        Args: val (str): The value to be checked.
        Returns: bool: True if the value is a float, False otherwise.
        """
        try:
            val = float(val)
            #print('is_float', val)
            return True
        except:
            #print("not a float")
            return False

    def _is_int(self, val):
        """
        gnb5 implemented on 2/26/23
        Check if the given value is an integer.
        Args: val (str): The value to be checked.
        Returns: bool: True if the value is an integer, False otherwise.
        """
        try:
            val = int(val)
            print('is_int', val)
            return True
        except:
            return False
        
    #https://processing.org/examples/integersfloats.html
    #had to move float first because it was changing the precision of float values
    def _as_number(self, val):
        """
        gnb5 implemented on 2/26/23
        Checks to see if the given value is an integer or float (calls previous helper methods)
        Convert the given string value to either an integer or float
        Args: val (str): The value to be converted.
        Returns: int or float: The converted value.
        Raises: Exception: If the value cannot be converted to a number.
        """
        
        if self._is_float(val):
            return float(val)
        elif self._is_int(val):
            return int(val)
        else:
            raise Exception("Not a number")


    def add(self, num1, num2):
        """
        gnb5 implemented on 2/26/23
        Adds two numbers and stores the result as the new answer.
        Returns: float: The sum of the two numbers.
        """
                
        #print(num1)
        if num1 == "ans":
            #added str
            return self.add(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            #print(num1)
            num2 = self._as_number(num2)
            #print(num2)
            self.ans = num1+num2
        return self.ans
        #return float(self.ans)
        

    def sub(self, num1, num2):
        """
        gnb5 implemented on 2/26/23
        Subtracts the second number from the first and stores the result as the new answer.
        """
                
        if num1 == "ans":
            return self.sub(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1-num2
        return self.ans

    def mult(self, num1, num2):
        """
        gnb5 implemented on 2/26/23
        Multiplies two numbers and stores the result as the new answer.
        """
                
        if num1 == "ans":
            return self.mult(self.ans, num2)
        else:
            num1 = self._as_number(num1)
            num2 = self._as_number(num2)
            self.ans = num1*num2
        return self.ans

    def div(self, num1, num2):
        """
        gnb5 implemented on 2/26/23
        Divides the first number by the second number and stores the result as the new answer.
        If the second number is 0, prints an error message and does not update the answer.
        """
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
    """ gnb5 implemented on 2/26/23 """
    # Set up the calculator and ask the user if they're ready
    is_running = True
    user_input = input("Are you ready to begin?")
    calc = Calculator()
    print(calc)
    # If the user is ready, start the main loop
    if user_input == "yes":
        while is_running:
            # Get the user's input equation
            user_input = input("Input your equation:")
            # If the user wants to quit, exit the loop
            if user_input == "quit" or user_input == "q":
                is_running = False
            else:
                # Parse the equation and perform the appropriate calculation
                # Print the result of the calculation
                print("Your eq was " + str(user_input))
                if "+" in user_input:
                    nums = user_input.split("+")
                    r = calc.add(nums[0].strip(), nums[1].strip())
                    #print("Result is " + str(r))
                    print("Result is {:.2f}".format(r))
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
