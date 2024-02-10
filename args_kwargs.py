def add(a, *args, **kwargs):
    print(a)
    print(args)
    print(kwargs)

add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, b=11, c=12, d=13, e=14, f=15, g=16, h=17, i=18, j=19, k=20)