def wrapper(f):
    def fun(l):
        # complete the function
        k = []
        for i in l:
            if len(i)==13:
                a = "+91 "+i[3:8]+" "+i[8:]
                k.append(a)
            elif len(i)==12:
                a = "+91 "+i[2:7]+" "+i[7:]
                k.append(a)
            elif len(i)==11:
                a = "+91 "+i[1:6]+" "+i[6:]
                k.append(a)
            else:
                a = "+91 "+i[:5]+" "+i[5:]
                k.append(a)
        f(k)
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
