an=eval(input('Anul este'))
an-=2000
rest=an%12
if rest ==0:
    print('Anul poarta numele dragon')
elif rest==1:
    print('Anul poarta numele sarpe')
elif rest==2:
    print('Anul poarta numele cal')
elif rest==3:
    print('Anul poarta numele oaie')
elif rest==4:
    print('Anul poarta numele maimuta')
elif rest==5:
    print('Anul poarta numele cocos')
elif rest==6:
    print('Anul poarta numele caine')
elif rest==7:
    print('Anul poarta numele porc')
elif rest==8:
    print('Anul poarta numele sobolan')
elif rest==9:
    print('Anul poarta numele bou')
elif rest==10:
    print('Anul poarta numele tigru')
else:
    print('Anul poarta numele iepure')
