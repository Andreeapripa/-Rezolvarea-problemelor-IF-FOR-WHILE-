n=int(input('n='))
if n==28 or n==29:
    print('februarie')
if n==30:
    print('aprilie','iunie','septembrie','noiembrie')
if n==31:
    print('ianuarie','martie','mai','iule','august','octombrie','decembrie')
if n<28 or n>31:
    print('numar de zile invalid')