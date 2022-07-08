def valid_brackets(tokens):
      mapping = { ')': '(', ']': '[', '}': '{' }

  stack = []

  for token in tokens:
    if token not in mapping.keys():
      stack.append(token)
    else:
      # Here we encountered one of the closing brackets,
      # so the previous on the stack better match!
      # If it doesn't match, then we don't have a valid list 
      # of matching brackets so we return false.
      top_element = stack.pop() if stack else None
      if mapping[token] != top_element:
        return False

  # If we reach here, then the entire stack was processed,
  # so not(stack) should be True, meaning the expression was good.
  # If for some reason the stack still has remaining tokens, clearly
  # there's something wrong so False is a good return value in that case.
  return not stack

def main():
  tests = [
    { 'inputs': ['(',')'],                 'results': True },
    { 'inputs': ['(',']'],                 'results': False },
    { 'inputs': ['{','(','[',']',')','}'], 'results': True },
    { 'inputs': ['(',')','[',']','{','}'], 'results': True },
    { 'inputs': ['('],                     'results': False },
    { 'inputs': [')','['],                 'results': False },
  ]

  for i in range(len(tests)):
    print(f'Test {i}:', valid_brackets(tests[i]['inputs']) == tests[i]['results'])

main()