 def calculator(num1, operator, num2):
	
	if operator == "+":
		return num1 + num2
		
	if operator == "-":
		return num1 - num2	
		
	if operator == "x" or operator == "*":
		return num1 * num2
		
	if operator == "÷" or operator == "/":
		if num2 == 0:
			return "can't divide by 0"
		return num1 / num2
