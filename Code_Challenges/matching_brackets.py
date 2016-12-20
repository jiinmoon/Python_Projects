# Problem #19

li1 = ('{', '(', '[', '<')
li2 = ('}', ')', ']', '>')
dic = {x:y for x,y in zip(li2, li1)}

def check_match(data):
  stack = []
  for c in list(data):
    if c in li1:
      stack.append(c)
    else:
      tmp = stack.pop()
      if not tmp == dic[c]:
        return 0

  if len(stack) > 0:
    return 0
  else:
    return 1 

def main():
  f = open('test_matching_brackets.txt', 'r')
  f.readline()

  for line in f:
    print(check_match(filter(lambda c: c in li1 or c in li2, list(line.strip()))))

if __name__ == '__main__':
  main()