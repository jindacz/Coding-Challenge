def rle(s):
  l = len(s)

  result = ''
  if l == 0: return result

  i = 0
  while i < l:
    char = s[i]
    result += char

    count = 1
    while i + count < l and s[i + count] == char:
      count += 1

    result += str(count)

    i += count

  return result

def main():
  tests = [
    { 'input': '',                'output': '' },
    { 'input': 'a',               'output': 'a1' },
    { 'input': 'abc',             'output': 'a1b1c1' },
    { 'input': 'aa',              'output': 'a2' },
    { 'input': 'aab',             'output': 'a2b1' },
    { 'input': 'aabbcc',          'output': 'a2b2c2' },
    { 'input': 'aabaccccdexdx',   'output': 'a2b1a1c4d1e1x1d1x1' },
    { 'input': 'wwwwaaadexxxxxx', 'output': 'w4a3d1e1x6' },
  ]

  for i in range(len(tests)):
    print(f'Test {i+1}:', rle(tests[i]['input']) == tests[i]['output'])

main()
