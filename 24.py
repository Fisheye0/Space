for x in ('0123456789ABCDEF'):
    w1 = int('2'+ x + 'BAD', 16)
    w2 = int('3C'+ x + 'FE', 16)
    if ((w1+w2)%15) == 0:
        print(x)
        x = int(x)
        print((w1+w2)/15)
