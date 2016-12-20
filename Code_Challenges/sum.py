def sum(A=0, B=0):
    return A+B

def main():
    (A,B) = map(lambda x: int(x), input().split(' '))
    print(sum(A,B))

if __name__ == "__main__":
    main()