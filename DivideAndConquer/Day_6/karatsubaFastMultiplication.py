
def karatsuba(x,y):
    '''Function to multiply 2 numbers in a more efficient manner'''
    if len(str(x)) == 1 or len(str(y)) ==1:
        return x*y
    else:
        n = max(len(str(x)),len(str(y)))
        nby = n//2
        # extracting 1 and second halves of both
        a = x // 10**(nby)
        b = x % 10**(nby)
        c = y // 10**(nby)
        d = y % 10**(nby)

        ac = karatsuba(a,c)
        bd = karatsuba(b,d)
        ad_plus_bc = karatsuba(a+b,c+d) - ac - bd

        # writing n as 2*nby takes care of both even and odd n
        #
        prod = ac * 10**(2*nby) + (ad_plus_bc * 10**nby) + bd
    
    return prod


def main():
    x = 122131363
    y = 457858585

    print("PRODUCT OF X : {0}\tY:{1}\t is : {2}".format(x,y,karatsuba(x,y)))


if __name__ == "__main__":
    main()


