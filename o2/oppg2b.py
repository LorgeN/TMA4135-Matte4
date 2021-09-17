from oppg2a import p, scp


if __name__ == "__main__":
    a = -2
    b = 1
    
    for i in range(2, 4):
        for j in range(1, i):
            print(scp(p(j, a, b), p(i, a, b), a, b))
