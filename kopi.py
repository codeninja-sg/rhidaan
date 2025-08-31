drink = ''#empty string

choice=input('Do you want kopi (1)or Teh (2) Select: ')
if choice== '1':
    drink = drink + 'kopi'

elif choice== '2':
    drink = drink + 'Teh'

else:
    print ('not a choice - press 1 or 2.' )

print (' Your order is ' + drink)
