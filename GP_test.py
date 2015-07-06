cgpaSoFar = float(raw_input("What's your GPA?" ))
unitsSoFar = int(raw_input('How many units have you offered so far? '))
targetCGPA = float(raw_input('What is your target CGPA at the end of this semester? '))
thisSemUnits = int(raw_input('How many units are you offering this semester? '))
cumSoFar = cgpaSoFar * unitsSoFar
totalUnits = unitsSoFar + thisSemUnits
cumCurrent = (targetCGPA * totalUnits) - cumSoFar #cumCurrent is the number we need
if (targetCGPA > 5.0 or cgpaSoFar > 5.0):
    print 'That is unrealistic!'
else:
    thisSemGP = cumCurrent /thisSemUnits
    if (thisSemGP > 5.0):
        print 'That is unattainable'
    else:
        print cumCurrent,thisSemGP
raw_input('Press any key to exit > ')