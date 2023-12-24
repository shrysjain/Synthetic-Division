import sys

# P3
def synth_alg(coeff, root):
  quotients = [coeff[0]]
  del coeff[0]
  
  for index, term in enumerate(coeff):
    quotients.append((quotients[index] * root) + term)

  if not quotients[-1] == 0:
    remainder = True
  else: remainder = False

  quotients = [str(x) for x in quotients]

  for i in range(len(quotients)):
    power = str(len(quotients) - i - 2)
    if power == "-1": power = "0"
    quotients[i] += "x^" + power

  for item in quotients:
    if item.startswith("0"):
      quotients.remove(item)

  for i in range(len(quotients)):
    try:
      if quotients[i].startswith("0"):
        quotients.remove(quotients[i])
    except: pass
    try:
      if quotients[i].endswith("^1"):
        quotients[i] = quotients[i][:-2]
    except: pass
    try:
      if quotients[i].endswith("^0"):
        quotients[i] = quotients[i][:-3]
    except: pass
    try: 
      if quotients[i].startswith("1x") and len(quotients[i]) > 1:
        quotients[i] = quotients[i][1:]
    except: pass
    try:
      if quotients[i].startswith("-1x") and len(quotients[i]) > 2:
        quotients[i] = "-" + quotients[i][2:]
    except: pass
    try:
      if quotients[i] == "1x^2": quotients[i] = "x^2"
      elif quotients[i] == "-1x^2": quotients[i] = "-x^2"
    except: pass
    try:
      if quotients[i].startswith("1x^"):
        quotients[i] = "x^" + quotients[i][3:]
    except: pass
    try:
      if quotients[i].startswith("-1x^"):
        quotients[i] = "-x^" + quotients[i][4:]
    except: pass

  for i in range(len(quotients)):
    if quotients[i].startswith("0"): quotients[i] = "1" + quotients[i]

  final = " + ".join(quotients)
  
  if remainder:
    if root == abs(root):
      final += f" / (x - {root})"
    else:
      final += f" / (x + {root * -1})"

  final = final.replace("+ -", "- ")

  if final[0] == "1" and final[2] == "x":
    final = "-" + final[1:]

  return final

# P4
def evaluate(poly):
  poly = poly.split(" / ")
  coeff = []

  root = int("".join([str(x) for x in poly[1] if x.isnumeric()])) * -1
  if "-" in poly[1]: root *= -1

  _temp = poly[0]
  poly = [*poly[0]]

  if poly[1] == "-":
    temp = True
  else: temp = False

  for i in range(len(poly)):
    if poly[i] == "-" and poly[i+1] == " ": 
      poly.insert(i+2, "?")

  try:
    if _temp[-6] == "-" and _temp[-5] == " ":
      poly.insert(-4, "?")
  except: pass

  try:
    if _temp[-5] == "-" and _temp[-4] == " ":
      poly.insert(-3, "?")
  except: pass

  poly.pop(0)
  poly.pop()

  poly = "".join(poly).replace("-", "+")

  poly = poly.replace("--", "-").split(" + ")

  for i in range(len(poly)):
    poly[i] = poly[i].replace("?", "-")

  for item in poly:
    if item.endswith("x"):
      poly[poly.index(item)] = item + "^1"
    if not "x" in item:
      poly[poly.index(item)] = item + "x^0"
    if item.startswith("x"):
      item = "1" + item
    if item.startswith("-x"):
      poly[poly.index(item)] = "-1" + item[1:]

  for item in poly:
    coeff.append(item.split("x")[0])

  if poly[len(poly)-1].endswith("^0"):
    is_constant = True
  else: is_constant = False

  if not is_constant:
    poly.append("0x^0")

  c = 0

  for i in range(len(poly) - 1):
    diff = int(poly[i].split("^")[1]) - int(poly[i+1].split("^")[1])
    for _ in range(diff-1):
      coeff.insert(i+1+c, 0)
      c += 1

  if not is_constant: coeff.append(0)

  for term in coeff:
    if term == "+": coeff[coeff.index(term)] = "-1"
    if term == "": coeff[coeff.index(term)] = "1"

  for i in range(len(coeff)):
    if str(coeff[i]).startswith("--"):
      coeff[i] = coeff[i][1:]

  coeff = [int(x) for x in coeff]

  if temp == True:
    coeff[0] = -1 * abs(coeff[0])

  return synth_alg(coeff, root)

sys.modules[__name__] = evaluate
