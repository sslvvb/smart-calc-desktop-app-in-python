from sys import argv
from calculator.simple import SimpleCalculator

def calc(text):
	
	try:
		c = SimpleCalculator()
		c.run(text)
		return c.log[-1]
	except Exception as e:
		print(e)
		return 0.0

if __name__ == '__main__':
    print(calc(argv[1]))
