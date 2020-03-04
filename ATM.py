pin=int(input('enter your 4 digit pin :-'))
pin2=[0,1,2,3,4,'yes','no']
print(pin)
if pin==9430:
    print('select your transection type')
    print('1 for balance enquery')
    print('2 for change pin')
    print('3 for money withdraw ')
    print('4 for money transfer')
    bank=int(input('transection type:-'))
    
    
        #balance enquery
    if bank==(pin2[1]):
        print('balance enquery :-')
        print('account balance is 10000')
        s=input('do you want a balance slip :-')
        if s==(pin2[5]):
            print(pin2[5])
            print('here is your account slip')
        else:
            print(pin2[6])
            print('exit')
            
            
            #changing pin
    elif bank==(pin2[2]):
        print('change pin :-')
        pin3=int(input('enter your current pin :-'))
        print(pin3)
        if pin3==pin:
            pin4=int(input('enyer the new pin :-'))
            print(pin4)
            if pin4>=1000 and pin4<10000:
                pin=pin4
                print(pin,'your pin is successfully changed')
            else:
                print('plz enter the valid 4 digit pin')
        else:
            print('plz enter the correct pin')
            
            
            #money withdraw
    elif bank==(pin2[3]):
        print('money withdraw :-')
        type=['saving account','current account']
        print('1. saving account')
        print('2. current account')
        type1=int(input('select the account type :-'))
        print('ypur account type :-')
        if type1==1:
            print(type[0])
            amount=int(input('enter the amount :-'))
            print(amount)
            pin1=int(input('enter the pin :'))
            print(pin1)
            if pin1==pin:
                print('your transection is successfully complete')
            else:
                print('wrong pin')
        elif type1==2:
            print(type[1])
            print('enter the amount :-')
            pin0=int(input('enter the pin :'))
            print(pin0)
            if pin0==pin:
                print('youe money withdraw is successfully complete')
            else:
                print('wrong pin')
        else:
            print('plz select the account type')
            
            
            #money transfer
    elif bank==(pin2[4]):
        print('money transfer :-')
        bankname=input('anter the bank name :-')
        print(bankname)
        ac=input('enter the account number :')
        print(ac)
        ac1=input('conferm the accoint number :')
        print(ac1)
        if ac==ac1:
            amount1=int(input('enter the amount :-'))
            p=int(input('enter the pin :'))
            print(p)
            if p==pin:
                print('your money transfer is successful')
            else:
                print('invalid pin')
        else:
            print('account number is not match')
    else:
        print('try again')
else:
    print('wrong pin')
                
