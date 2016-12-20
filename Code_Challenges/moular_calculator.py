# Problem #14
def modular_calculation(num = 0, ops = []):

  for operations in ops:
    operator = operations[0]
    op_value = operations[1]
    if operator == '+':
      num += op_value
    elif operator == '*':
      num *= op_value
    else:
      num %= op_value

  return num

def main():
  f = open('test_modular_calculator.txt', 'r')
  num = int(f.readline())
  li = [line.strip() for line in f]
  operations = []
  for ops in li:
    (x,y) = ops.split()
    operations.append((x,int(y)))
  
  print(modular_calculation(num, operations))


if __name__ == '__main__':
  main()