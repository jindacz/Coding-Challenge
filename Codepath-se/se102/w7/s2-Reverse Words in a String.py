# Write a method to convert a string representation of an integer into its equivalent integer number.

# Assumes the input string only has characters including 0-9 and -, no empty string
def a_to_i(s):

  sign = 1
  if s[0] == '-':
    sign = -1
    s = s[1:] # Throw away the first char
  
  output = 0

  for i in range(len(s)):
    output = (output * 10) + int(s[i])

  return sign * output
  

def main():
  tests = [
    { 'input': '1',     'output': 1 },
    { 'input': '-1',    'output': -1 },
    { 'input': '12',    'output': 12 },
    { 'input': '-12',   'output': -12 },
    { 'input': '1234',  'output': 1234 },
    { 'input': '-1234', 'output': -1234 },
    { 'input': '0',     'output': 0 },
    { 'input': '-0',    'output': 0 },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', a_to_i(tests[i]['input']) == tests[i]['output'])

main()