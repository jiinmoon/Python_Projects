# Problem75
from collections import Counter

def check_score(values):
    #print(values)
    
    c = Counter(values).values()
    
    if 6 in set(values) and len(set(values)) == 5:
        print('big-straight')
    elif 1 in set(values) and len(set(values)) == 5:
        print('small-straight')
    else:
        if 2 in c and 3 in c:
            print('full-house')
        elif 5 in c:
            print('yacht')
        elif 4 in c:
            print('four')
        elif 3 in c:
            print('three')
        elif 2 in c and len(c) == 3:
            print('two-pairs')
        elif 2 in c:
            print('pair')
        else:
            print('none')

def main():
    f = open('test_yacht_or_dice_poker.txt', 'r')
    f.readline()
    
    for line in f:
        check_score(list(map(lambda x: int(x), line.strip().split())))
        
    
    


if __name__ == '__main__':
    main()