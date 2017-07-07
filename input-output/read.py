import os
import sys
# print(sys.version)

# print os.getcwd() # /Users/damienshaw/Dev/Tutorials/Udemy/Python
# print os.path.basename(__file__) # input.py
# print os.path.abspath(__file__) # /Users/damienshaw/Dev/Tutorials/Udemy/Python/input-output/input.py
# print os.path.dirname(__file__) # /Users/damienshaw/Dev/Tutorials/Udemy/Python/input-output

# quotes = open("/Users/damienshaw/Dev/Tutorials/Udemy/Python/short_quotes.txt", "r")

# using a relative path
QUOTES_PATH = os.path.join(os.getcwd(), 'short_quotes.txt')
quotes = open(QUOTES_PATH, "r", encoding='utf-8')

for line in quotes:
    print(line, end='')

quotes.close()
