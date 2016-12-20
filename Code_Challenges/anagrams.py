# Problem #127

def main():
  f_dic = open('words_dict.txt', 'r')
  f_test = open('test_anagrams.py', 'r')

  f_test.readline()

  words_dic = {}

  for word in f_dic:
    w = word.strip()
    sorted_w = ''.join(sorted(list(w)))
    if sorted_w not in words_dic:
      words_dic[sorted_w] = [w]
    else:
      words_dic[sorted_w] = words_dic[sorted_w] + [w]

  for line in f_test:
    print(len(words_dic[''.join(sorted(list(line.strip())))]) - 1)


if __name__ == '__main__':
  main()