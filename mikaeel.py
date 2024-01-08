root = 0
def synth_alg(coeff):
    ls = [coeff[0]]
    cur = coeff[0] * root * -1
    for i in range(1, len(coeff)):
        ls.append(cur + coeff[i])
        cur = (cur + coeff[i]) * root * -1
    return ls 
def compiler(coeff):
    global root 
    root1 = root
    string = ""
    for i, chr in enumerate(coeff):
        exponent = len(coeff)-i-2
        if i == 0:
            if exponent > 0:
                if chr == 1:
                    string += "x^" + str(exponent)
                elif chr == -1:
                    string += "-x^" + str(exponent)
                elif chr == 0:
                    continue 
                else:
                    string += str(chr) + "x^" + str(exponent)
        else:
            if exponent > 0:
                if chr == 1:
                    string += " + " + "x^" + str(exponent)
                elif chr == -1:
                    string += " - " + "x^" + str(exponent)
                elif chr == 0: 
                    continue
                else:
                    if chr < 0: 
                        string += " - " + str(abs(chr)) + "x^" + str(exponent)
                    else:
                        string += " + " + str(abs(chr)) + "x^" + str(exponent)
            elif exponent == 0:
                if chr < 0: 
                    string += " - " + str(abs(chr))
                elif chr == 0:
                    continue
                else:
                    string += " + " + str(abs(chr))
        if "^1 " in string:
            string = string.replace("^1 ", ' ')
        if "x^0" in string:
            string = string.replace("x^0", '')
    if coeff[-1] != 0:
        if coeff[-1] < 0:
            if root1 < 0:
                string = string + " - " + str(abs(coeff[-1])) +  " / " + "(x" + " - " + str(abs(root1)) + ")"
            else:
                string = string + " - " + str(abs(coeff[-1])) +  " / " + "(x" + " + " + str(root1) + ")"
        else:
            if root1 < 0:
                string = string + " + " + str(abs(coeff[-1])) +  " / " + "(x" + " - " + str(abs(root1)) + ")"
            else:
                string = string + " + " + str(coeff[-1]) +  " / " + "(x" + " + " + str(root1) + ")"
    if "^1 " in string:
        string = string.replace("^1 ", ' ')
    if "^1" in string[-2:]:
        string = string.replace("^1", '')
    return string
def evaluate(string):
    subfinal = []
    final = []
    numerator, denominator = string.split(" / ")
    num = numerator.split()
    den = denominator.split()
    numfix = [chr.replace('(', '').replace(')', '') for chr in num]
    denfix = [chr.replace('(', '').replace(')', '') for chr in den]
    expo = numfix[0].split("^")[1]

    for index, chr in enumerate(numfix):
        cur = chr.split("^")
        if chr == '+' or chr == '-':
            continue
        elif len(cur) < 2:
            if "x" in cur[0]: 
                numfix[index] = numfix[index] + "^1 "
            else:
                numfix[index] = numfix[index] + "x^0"
    for i in range(int(expo) + 1):
        final.append(0)
    for i in range(0, len(numfix), 2):
        cur = int(numfix[i].split("^")[1])
        if numfix[i-1] == '-':
            final[len(final)-cur-1] = ("-" + numfix[i].split("x")[0])
        else:
            final[len(final)-cur-1] = (numfix[i].split("x")[0])
    for i in range(len(final)):
        if final[i] == '': 
            final[i] = 1
    global root 
    if denfix[-2] == "-":
        root = int("-" + denfix[-1])
    else:
        root = int(denfix[-1])
    for i in final:
        subfinal.append(str(i))
    for i in range(len(subfinal)):
        if subfinal[i] == "-":
            subfinal[i] = subfinal[i].replace("-", "-1")
    subfinal = [int(i) for i in subfinal]
    return subfinal 
#print(compiler(synth_alg(evaluate("(2x^2 + 11x + 15) / (x + 3)"))))
#print(compiler(synth_alg(evaluate("(2x^4 + 6x^3 + 5x^2 - 44) / (x + 3)"))))
#print(compiler(synth_alg(evaluate("(6x^3 + 5x^2 - 44) / (x + 3)"))))
#print(compiler(synth_alg(evaluate("(-x^6 + 6x^3 + 5x^2 - 44) / (x + 3)")))) 
#print(compiler(synth_alg(evaluate("(2x^10 + 11x + 15) / (x + 3)")))) 
#print(compiler(synth_alg(evaluate("(x^6 + 11x + 15) / (x + 10)")))) 
#print(compiler(synth_alg(evaluate("(x^6 + x + 15) / (x + 1)"))))
#print(compiler(synth_alg(evaluate("(x^2 + x) / (x + 1)"))))
#print(compiler(synth_alg(evaluate("(x^2 + x) / (x - 1)"))))
#print(compiler(synth_alg(evaluate("(x^2 + x) / (x - 10)"))))
#print(compiler(synth_alg(evaluate("(-69x^2) / (x + 1)"))))
#print(compiler(synth_alg((evaluate("(-20x^11 - x^6 + x^3 - 200) / (x - 2)")))))
#print(compiler(synth_alg(evaluate("(-x^11 - x^6 + x^3 - 200) / (x - 2)"))))
#print(compiler(synth_alg(evaluate("(x^6 + x + 15) / (x + 1)"))))
#print(compiler(synth_alg(evaluate("(111x^13 - 7x^3 - 10) / (x - 100)"))))
#print(compiler(synth_alg(evaluate("(-50x^5 + 447x^4 - 551x^3 + 172x^2 - 835) / (x + 12)"))))
print(compiler(synth_alg(evaluate("(2x^3 + 10x^2 + 7x + 2) / (x + 4)"))))
