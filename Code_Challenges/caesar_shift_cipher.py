# Problem #47

li1 = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
li2 = [i for i in range(1, 27)]
dic = {x:y for x, y in zip(li1, li2)}

def decypher(c, K):
  if c.isalpha():
    return li1[(dic[c] - K - 1) % 26]
  else:
    return c

def main():
  f = open('test_caesar_shift_cipher.txt', 'r')
  K = int(f.readline().strip().split()[1])

  for line in f:
    print(''.join([decypher(c, K) for c in line.strip()]))


if __name__ == '__main__':
  main()