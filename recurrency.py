def show(n):
    if n<=0:
        return
    print(n)
    show(n/2)
    show(n/2)
n=8
show(n)
    