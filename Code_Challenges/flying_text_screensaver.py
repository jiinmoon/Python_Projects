# Problem #134

def compute_coord(lim):
  while True:
    for i in range(0,lim):
      yield i
    for i in range(lim-2,0,-1):
      yield i


def main():
  f = open('test_flying_text_screensaver.txt', 'r')
  w, h, l = map(lambda x: int(x), f.readline().strip().split())
  print(w, h, l)

  w = w - l
  x, y = 0, 0

  x_gen = compute_coord(w+1)
  y_gen = compute_coord(h)
  
  result = []
  for _ in range(101):
    result.append(str(next(x_gen)))
    result.append(str(next(y_gen)))

  print(' '.join(result))

if __name__ == '__main__':
  main()