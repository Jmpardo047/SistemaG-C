def validint()->int:
    try:
        num = int(input((':)_ ')))
    except ValueError:
        print('invalid value')
        os.system('pause')
        validint()
    else:
        return num

def validtext()->str:
    try:
        text = str(input(':)_'))
    except ValueError:
        print('invalid value')
        os.system('pause')
        validtext()
    else:
        return text
def validfloat():
    pass