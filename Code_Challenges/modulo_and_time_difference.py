# Problem #12
def time_diff(time1, time2):
  time1_in_sec = (time1[0] * 86400) + (time1[1] * 3600) + (time1[2] * 60) + (time1[3])
  time2_in_sec = (time2[0] * 86400) + (time2[1] * 3600) + (time2[2] * 60) + (time2[3])
  diff_in_sec = time2_in_sec - time1_in_sec

  days = diff_in_sec / (86400)
  diff_in_sec %= 86400
  hours = diff_in_sec / (3600)
  diff_in_sec %= 3600
  mins = diff_in_sec / (60)
  diff_in_sec %= 60
  return '({} {} {} {})'.format(int(days), int(hours), int(mins), int(diff_in_sec))


def main():

  f = open('test_modulo_and_time_difference.txt', 'r')
  f.readline()

  for line in f:
    li = tuple(map(lambda x: int(x), line.strip().split()))
    time1 = li[:4]
    time2 = li[4:]
    print(time_diff(time1, time2))

if __name__ == '__main__':
  main()