# Problem #28

answer = ['under', 'normal', 'over', 'obese']

def calc_bmi(weight = 0.0, height = 0.0):
    bmi = float(weight) / float(height ** 2)
    if bmi < 18.5:
      print(answer[0])
    elif 18.5 <= bmi < 25.0:
      print(answer[1])
    elif 25.0 <= bmi < 30.0:
      print(answer[2])
    else:
      print(answer[3])

def main():
  f = open('test_body_mass_index.txt', 'r')
  f.readline()
  for line in f:
    (weight, height) = line.strip().split()
    calc_bmi(float(weight), float(height))


if __name__ == '__main__':
  main()