months = ['January', 'Febuary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

numBday = input("When's your birthday in mm/dd/yyyy format?\n")

wordBday = numBday.split('/')

validMonth = False
if int(wordBday[0]) <= 12:
  validMonth = True

if validMonth != True:
  print('Invalid Birthdate\nError 2: Month not in appropriate range')
else:
  numMonth = wordBday[0]

  if numMonth[0] == '0':
    numMonth = numMonth[1]

  wordMonth = months[(int(numMonth) - 1)]
  wordBday.pop(0)
  wordBday.insert(0, wordMonth)  # type: ignore


  numDay = wordBday[1]

  if int(numDay[0]) == 0:
    numDay = numDay[1]
  wordBday.pop(1)
  wordBday.insert(1, numDay)  # type: ignore



  if int(numDay) != 11 and int(numDay) != 12 and int(numDay) != 13:

    numSuf = ''
    char = len(numDay) - 1

    if int(numDay[char]) == 1:
      numSuf = 'st'
    elif int(numDay[char]) == 2:
      numSuf = 'nd'
    elif int(numDay[char]) == 3:
      numSuf = 'rd'
    else:
      numSuf = 'th'

  else:
    numSuf = 'th'


  a, b, c = wordBday
  sentence = f'{a} {b}{numSuf}, {c}'

  if int(b) >= 31 or int(b) <= 0:
    print('Invalid Birthdate\nError 1: Day number not in appropriate range')
  else:
    print(sentence)