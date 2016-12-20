# Problem #33
from collections import Counter

def main():
  f = open('test_parity_control.txt', 'r')

  li = list(map(lambda x: int(x), f.readline().strip().split()))
  decoded_message = []
  for c in li:
    if len(bin(c)[2:]) <= 7 and Counter(bin(c))['1'] % 2 == 0:
      decoded_message.append(chr(c))
    else:
      if len(bin(c)[2:]) >= 8 and not Counter(bin(c-128))['1'] % 2 == 0:
        decoded_message.append(chr(c-128))
  print(''.join(decoded_message))



if __name__ == '__main__':
  main()