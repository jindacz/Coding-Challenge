# Write a method that takes an integer as input and returns its string representation.

def i_to_s(n):
  if not(n): return '0'

  l = []
  sign = '-' if n < 0 else ''
  n = abs(n)

  while n:
    d = str(n % 10)
    l.append(d)
    n = n // 10

  l.append(sign)
  l.reverse()

  return ''.join(l)
  
# test with smallest possible first
def main():
  tests = [
    { 'input': 1,    'output': '1' },
    { 'input': -1,   'output': '-1' },
    { 'input': 0,    'output': '0' },
    { 'input': 12,   'output': '12' },
    { 'input': -12,  'output': '-12' },
    { 'input': 123,  'output': '123' },
    { 'input': -123, 'output': '-123' },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', i_to_s(tests[i]['input']) == tests[i]['output'])

main()
