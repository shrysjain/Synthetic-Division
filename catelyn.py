import sys

def synth_alg(test, root):
    list = [test[0], ]
    sub = 0
    string = ""
    power = len(test) - 2
    for i in range(1, len(test)):
        sub = root * list[-1]
        list.append(test[i] + sub)
    for j in range(len(list)):
        if list[j] == 0:
            power -= 1
        elif list[j] == 1 and power != -1:
            if power == 0:
                string += str(list[j]) + " + "
                power -= 1
            elif power == 1:
                string += "x + "
                power -= 1
            else:
                string += "x^" + str(power) + " + "
                power -= 1
        elif list[j] == -1 and power != -1:
            if power == 0:
                string += str(list[j]) + " + "
                power -= 1
            elif power == 1:
                string += "-x + "
                power -= 1
            else:
                string += "-x^" + str(power) + " + "
                power -= 1
        elif power != 0 and power != 1 and power != -1:
            string += str(list[j]) + "x^" + str(power) + " + "
            power -= 1
        elif power == 0:
            string += str(list[j]) + " + "
            power -= 1
        elif power == 1:
            string += str(list[j]) + "x + "
            power -= 1
        elif power == -1 and list[j] != 0:
            string += str(list[j]) + " / (x - " + str(root) + ")"
    while "+ -" in string:
        string = string[0:string.index("+ -")] + string[string.index("+ -") + 2:string.index("+ -") + 3] + " " + string[string.index("+ -") + 3:]
    while " - -" in string:
        string = string[0:string.index(" - -")] + " + " + string[string.index(" - -") + 4:]
    if string[-2:] == "+ ":
        return string[0:len(string) - 2]
    return string[0:len(string)]

def evaluate(poly):
    coefficients = []
    powers = []
    string = poly[1:]
    number = ""
    boo = True
    root = 0
    if string[0] == "x":
        coefficients.append(1)
    elif string[0:2] == "-x":
        coefficients.append(-1)
    elif "x" in string[0:string.index("/")]:
        coefficients.append(int(poly[1:poly.index("x")]))
    if "^" in string:
        string = string[(string.index("^")) + 1:]
        for i in range(len(string)):
            if string[i].isnumeric():
                number += string[i]
            if string[i].isnumeric() == False:
                break
        powers.append(int(number))
        string = string[string.index(" ") + 1:]
    else:
        if "x" in string[1:string.index("/")]:
            string = string[1:]
            if "+" in string[0:string.index("/")]:
                string = string[string.index("+") + 2:]
                coefficients.append(int(string[0:string.index(")")]))
            elif "-" in string[string.index("x"):string.index("/")]:
                string = string[string.index("-") + 2:]
                coefficients.append(int(string[0:string.index(")")]) * -1)
            else:
                powers.append(1)
                coefficients.append(0)
            string = string[string.index("/") + 5:]
            if string[0] == "-":
                boo = False
            string = string[string.index(" ") + 1:]
            for i in range(len(string)):
                if string[i].isnumeric():
                    number += string[i]
                if string[i].isnumeric() == False:
                    break
            if boo == True:
                root = (int(number) * -1)
            elif boo == False:
                root = (int(number))
            return synth_alg(coefficients, root)
        else:
            return string[0:string.index(")")] + " " + string[string.index("/"):]
    while "^" in string:
        boo = True
        number = ""
        if string[0] == "-":
            boo = False
        string = string[string.index(" ") + 1:]
        if string[0] == "x":
            if boo == True:
                coefficients.append(1)
            elif boo == False:
                coefficients.append(-1)
        else:
            for j in range(len(string)):
                if string[j].isnumeric():
                    number += string[j]
                elif string[j].isnumeric() == False:
                    break
            if boo == True:
                coefficients.append(int(number))
            elif boo == False:
                coefficients.append(int(number) * - 1)
        string = string[string.index("^") + 1:]
        number = ""
        for k in range(len(string)):
            if string[k].isnumeric():
                number += string[k]
            if string[k].isnumeric() == False:
                break
        powers.append(int(number))
        string = string[string.index(" ") + 1:]
    boo = True
    number = ""
    if "x" in string[0:string.index("/")]:
        if string[0] == "-":
            boo = False
        string = string[string.index(" ") + 1:]
        if string[0] == "x":
            if boo == True:
                coefficients.append(1)
            elif boo == False:
                coefficients.append(-1)
        else:
            for i in range(len(string)):
                if string[i].isnumeric():
                    number += string[i]
                if string[i].isnumeric() == False:
                    break
            if boo == True:
                coefficients.append(int(number))
            elif boo == False:
                coefficients.append(int(number) * -1)
        powers.append(1)
        string = string[string.index("x") + 1:]
    boo = True
    number = ""
    if "+" in string[0:string.index("/")] or "-" in string[0:string.index("/")]:
        if string[0] != "+" and string[0] != "-":
            string = string[string.index(" ") + 1:]
        if string[0] == "-":
            boo = False
        string = string[string.index(" ") + 1:]
        for i in range(len(string)):
            if string[i].isnumeric():
                number += string[i]
            if string[i].isnumeric() == False:
                break
        if boo == True:
            coefficients.append(int(number))
        elif boo == False:
            coefficients.append(int(number) * -1)
        powers.append(0)
    boo = True
    number = ""
    string = string[string.index("/") + 5:]
    if string[0] == "-":
        boo = False
    string = string[string.index(" ") + 1:]
    for i in range(len(string)):
        if string[i].isnumeric():
            number += string[i]
        if string[i].isnumeric() == False:
            break
    if boo == True:
        root = int(number) * -1
    elif boo == False:
        root = int(number)
    for index in range(powers[0] - powers[-1] - 1):
        if powers[index] - 1 == powers[index + 1]:
            continue
        else:
            powers.insert(index + 1, powers[index] - 1)
            coefficients.insert(index + 1, 0)
    while powers[-1] != 0:
        powers.append(powers[-1] - 1)
        coefficients.append(0)
    return (synth_alg(coefficients, root))

sys.modules[__name__] = evaluate