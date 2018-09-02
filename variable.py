def count(b):
    b = b + 1
if __name__ == '__main__':
    c = 1
    b = 10
    for i in range(10):
        count(c)
        print("c:", c)
        b = b + 1
        print("b:", b)
    print("last c:", c)