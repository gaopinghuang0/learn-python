"""
Learn python interpreter from 
https://github.com/aosabook/500lines/blob/master/interpreter/interpreter.markdown
"""


class Interpreter(object):
	def __init__(self):
		self.stack = []

	def LOAD_VALUE(self, number):
		self.stack.append(number)

	def PRINT_ANSWER(self):
		answer = self.stack.pop()
		print answer

	def ADD_TWO_VALUES(self):
		num1 = self.stack.pop()
		num2 = self.stack.pop()
		total = num1 + num2
		self.stack.append(total)

	def run_code(self, what_to_execute):
		instructions = what_to_execute['instructions']
		numbers = what_to_execute['numbers']
		for each_step in instructions:
			instruction, argument = each_step
			if instruction == "LOAD_VALUE":
				number = numbers[argument]
				self.LOAD_VALUE(number)
			elif instruction == "ADD_TWO_VALUES":
				self.ADD_TWO_VALUES()
			elif instruction == "PRINT_ANSWER":
				self.PRINT_ANSWER()



def main():
	what_to_execute = {
	'instructions': [("LOAD_VALUE", 0),
					("LOAD_VALUE", 1),
					("ADD_TWO_VALUES", None),
					("LOAD_VALUE", 2),
					("ADD_TWO_VALUES", None),
					("PRINT_ANSWER", None)],
	"numbers": [7, 5, 8]}

	interpreter = Interpreter()
	interpreter.run_code(what_to_execute)

if __name__ == "__main__":
	main()
