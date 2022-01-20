dagen = ['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag']

print('Alle dagen van de week: ')
print(dagen)

print(' Alle Werkdagen:')
print(dagen[0:5])

print('Weekenddagen: ')
print(dagen[5:7])

print('Alle dagen van de week in omgekeerde: ')
dagen.reverse()
print(dagen)

print('De werkdagen in omgekeerde: ')
print(dagen[-5:])


print('De weekenddagen in omgekeerde:')
print(dagen[:2])
