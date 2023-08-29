print('WELCOME')
print("press 'a' to calculate acceleration")
print("press 'v' to calculate velocity")
print("press 't' to calculate time")
print("press 's' to calculate speed")
X=input('>')
#ACCELERATION
if X=='a' :
    print("press's'to calculate acceleration when 'DISPLACEMENT IS UNKNOWN'")
    print("press't'to calculate acceleration when 'TIME IS UNKNOWN'")
    print("press'v'to calculate acceleration when 'FINAL VELOCITY IS UNKNOWN'")
    print("press'f'to calculate acceleration when 'FORCE and MASS are KNOWN'")
    h=input('>')
    if h=='s' :
        a=print('ok, calculating Acceleration')
        b=input('enter initial velocity (in m/s): ')
        c=input('enter final velocity (in m/s): ')
        d=input('enter Time taken (in second): ')
        e=float(c)-float(b)
        f=e/float(d)
        print('ACCELERATION is',f ,'m/s.sq')
    elif h=='v' :
        aaaa=print('ok, calculating Acceleration')
        bbbb=input('enter initial velocity(in m/s): ')
        cccc=input('enter displacement(in meters): ')
        dddd=input('enter time(in seconds): ')
        eeee=float(cccc)*2 - float(bbbb)*float(dddd)*2
        ffff=eeee/float(dddd)**2
        print('ACCELERATION is',ffff ,'m/s.sq')
    elif h=='t' :
        aa=print('ok, calculating Acceleration')
        bb=input('enter initial velocity (in m/s): ')
        cc=input('enter final velocity (in m/s): ')
        dd=input('enter Displacement (in meters): ')
        ee=float(cc)**2 - float(bb)**2
        ff=float(dd)*2
        g=ee/ff
        print('ACCELERATION is',g ,'m/s.sq')
    elif h=='f' :
        aaa=print('ok, calculating Acceleration')
        bbb=input('enter force applied:')
        ccc=input('enter mass:')
        ddd=float(bbb)/float(ccc)
        print('ACCELERATION is',ddd ,'m/s.sq')
    else :
        print('invalid letter')
        quit()
#VELOCITY
elif X=='v' :
    print("press 'v' to calculate 'FINAL VELOCITY'")
    print("press 'u' to calculate 'INITIAL VELOCITY'")
    print("press 'a' to calculate 'AVERAGE VELOCITY'")
    l=input('>')
    if l=='v' :
        print("press 't' to calculate velocity when 'TIME IS UNKNOWN'")
        print("press 's'to calculate velocity when 'DISPLACEMENT IS UNKNOWN'")
        print("press 'a'to calculate velocity when 'ACCELERATION IS UNKNOWN'")
        print("press 'u'to calculate velocity when 'INITIAL VELOCITY IS UNKNOWN'")
        j=input('>')
        if j=='t' :
            print('ok, calculating velocity')
            gg=input('enter initial velocity(in m/s): ')
            hh=input('enter acceleration(in m/s.sq): ')
            ii=input('enter displacement(in meters): ')
            jj=float(gg)**2
            jjj= 2*float(hh)*float(ii)
            jjjj=jj+jjj
            kk=(jjjj)**0.5
            print('VELOCITY is',kk ,'m/s')
        elif j=='s' :
            print('ok, calculating velocity')
            ii=input('enter initial velocity(in m/s): ')
            iii=input('enter acceleration(in m/s.sq): ')
            iiii=input('enter time(in seconds): ')
            kkk=float(ii) + float(iii)*float(iiii)
            print('VELOCITY is',kkk ,'m/s')
        elif j=='a' :
            print('ok, calculating velocity')
            m=input('enter initial velocity(in m/s): ')
            mm=input('enter displacement(in meters): ')
            mmm=input('enter time(in seconds): ')
            mmmm=2*float(mm) / float(mmm)
            n=mmmm - float(m)
            print('VELOCITY is',n ,'m/s')
        elif j=='u' :
            print('ok, calculating velocity')
            nn=input('enter displacement(in meters): ')
            nnn=input('enter time(in seconds): ')
            nnnn=input('enter acceleration(in m/s.sq): ')
            o=2*float(nn) + float(nnnn) * float(nnn)**2
            oo=2*float(nnn)
            print('VELOCITY is',o/oo ,'m/s')
        else :
            print('invalid letter!')
            quit()
    elif l=='u' :
        print("press 't' to calculate initial velocity when 'TIME IS UNKNOWN'")
        print("press 'v'to calculate initial velocity when 'FINAL VELOCITY IS UNKNOWN'")
        print("press 's'to calculate initial velocity when 'DISPLACEMENT IS UNKNOWN'")
        print("press 'a'to calculate initial velocity when 'ACCELERATION IS UNKNOWN'")
        y=input('>')
        if y=='t' :
            print('ok, calculating initial velocity')
            p=input('enter final velocity(in m/s): ')
            pp=input('enter acceleration(in m/s.sq): ')
            ppp=input('enter displacement(in meters): ')
            q=float(p)**2 - 2*float(pp)*float(ppp)
            print('INITIAL VELOCITY is',q ,'m/s')
        elif y=='v' :
            print('ok, calculating initial velocity')
            mm=input('enter acceleration(in m/s.sq): ')
            mmm=input('enter displacement(in meters): ')
            mmmm=input('enter time(in seconds): ')
            r=2*float(mmm) - float(mm) * float(mmmm)**2
            rr=2*float(mmmm)
            print('INITIAL VELOCITY is',r/rr ,'m/s')
        elif y=='s' :
            print('ok, calculating initial velocity')
            t=input('enter final velocity(in m/s): ')
            tt=input('enter acceleration(in m/s.sq): ')
            ttt=input('enter time(in seconds): ')
            tttt=float(t) - float(tt)*float(ttt)
            print('INITIAL VELOCITY is',tttt ,'m/s')
        elif y=='a' :
            print('ok, calculating initial velocity')
            uu=input('enter displacement(in meters): ')
            uuu=input('enter time(in seconds): ')
            u=input('enter final velocity(in m/s): ')
            ab=2*float(uu) - float(uuu)*float(u)
            ac=ab/float(uuu)
            print('INITIAL VELOCITY is',ac ,'m/s')
        else :
            print('invalid letter')
            quit()
    elif l=='a' :
        print('ok, calculating Average velocity')
        w=input('enter total Displacement(in metres): ')
        ww=input('enter total Time(in seconds): ')
        www=float(w)/float(ww)
        print('AVERAGE VELOCITY',WWW ,'m/s')
    else :
        print('invalid letter')
        quit()

#TIME
elif X=='t' :
    print("press 's' to calculate TIME when 'DISPLACEMENT IS UNKNOWN' ")
    print("press 'v' to calculate TIME when 'FINAL VELOCITY IS UNKNOWN' ")
    print("press 'u' to calculate TIME when 'INITIAL VELOCITY IS UNKNOWN' ")
    print("press 'a' to calculate TIME when 'ACCELERATION IS UNKNOWN' ")
    print("press 'd' to calculate TIME when 'DISTANCE AND SPEED ARE KNOWN' ")
    print("press 'd' to calculate TIME when 'DISPLACEMENT AND VELOCITY ARE KNOWN' ")
    print("press 'vv' to calculate TIME when 'UNIFORM ACCELERATION AND VELOCITY ARE KNOWN' ")
    abc=input('>')
    if abc=='s' :
        print('ok, calculating time')
        abd=input('enter initial velocity(in m/s): ')
        abe=input('enter final velocity(in m/s): ')
        abf=input('enter acceleration(in m/s.sq): ')
        abg=float(abe) - float(abd)
        abz=abg/float(abf)
        print('TIME is',abz ,'seconds')
    elif abc=='v' :
        print('ok, calculating time')
        abi=input('enter initial velocity(in m/s): ')
        abj=input('enter displacement(in meters): ')
        abk=input('enter acceleration(in m/s.sq): ')
        abl= -float(abi)
        abo=float(abi)**2 + 2*float(abk)*float(abj)
        abx=abo**0.5
        abp=abl+abx
        abn=abp/float(abk)
        print('TIME is',abn ,'seconds')
    elif abc=='u' :
        print('ok, calculating time')
        ijk=input('enter final velocity(in m/s): ')
        ijl=input('enter acceleration(in m/s.sq): ')
        ijm=input('enter displacement(in meters): ')
        ijn=float(ijk)**2 - 2*float(ijm)*float(ijl)
        ijo=ijn**0.5
        ijp=float(ijk) + ijo
        ijq=ijp/float(ijl)
        print('TIME is',ijq ,'seconds')
    elif abc=='a' :
        print('ok, calculating time')
        abu=input('enter initial velocity(in m/s): ')
        abx=input('enter final velocity(in m/s): ')
        abw=input('enter displacement(in meters): ')
        aby=float(abw) * 2
        abz=float(abu) + float(abx)
        baa=aby/abz
        print('TIME is',baa ,'seconds')
    elif abc=='d' :
        print('ok, calculating time')
        bab=input('enter velocity/speed (in m/s): ')
        bac=input('enter displacement/distance (in meters): ')
        bad=float(bac)/float(bab)
        print('TIME is',bad ,'seconds')
    elif abc=='vv' :
        print('ok, calculating time')
        bae=input('enter acceleration(in m/s.sq): ')
        baf=input('enter velocity(in m/s): ')
        bag=float(baf) / float(bae)
        print('TIME is',bag ,'seconds')
    else :
        print('invalid letter')
        quit()

#speed
elif X=='s' :
    print('ok, calculating speed')
    bah=input('enter distance (in meters): ')
    bai=input('enter time(in seconds): ')
    baj=float(bah) / float(bai)
    print('speed is',bag ,'m/s')


else :
    print('invalid letter')
    quit()

input('THANKYOU')

#thankyou
