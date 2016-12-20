# Problem #20

def main():
  vowels = ['a','e','i','o','u','y']

  f = open('test_vowel_count.txt', 'r')
  f.readline()

  for line in f:
      print(len(list(filter(lambda x: x in vowels, list(line.strip())))))


if __name__ == "__main__":
  main()