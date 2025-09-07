drink = ''#empty string

choice=input('Do you want kopi (1)or Teh (2) Select: ')
if choice== '1':
    drink = drink + 'kopi'

elif choice== '2':
    drink = drink + 'Teh'

else:
    print ('not a choice - press 1 or 2.' )

choice = input ('Do you want milk (1) or no milk (2) ')
if choice == '1':
        drink = drink
elif choice == '2':
     drink = drink + '-o'

else:
     print ("not a choice - pres 1 or 2.")
print (' Your order is ' + drink)
