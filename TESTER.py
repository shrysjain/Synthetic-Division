from random import randint, choice # For generating coefficients/powers for polynomials
import shreyas as shreyas_evaluate # Local module
import catelyn as catelyn_evaluate # Local module
from pickle import dump, load # For persistence

def normalize(poly): # Convert a list of coefficients to a polynomial
  poly = [str(x) for x in poly]

  for i in range(len(poly)):
    power = str(len(poly) - i - 2)
    if power == "-1": power = "0"
    poly[i] += "x^" + str(int(power)+1)

  for item in poly:
    if item.startswith("0"):
      poly.remove(item)

  for i in range(len(poly)):
    try:
      if poly[i].startswith("0"):
        poly.remove(poly[i])
    except: pass
    try:
      if poly[i].endswith("^1"):
        poly[i] = poly[i][:-2]
    except: pass
    try:
      if poly[i].endswith("^0"):
        poly[i] = poly[i][:-3]
    except: pass
    try: 
      if poly[i].startswith("1x") and len(poly[i]) > 1:
        poly[i] = poly[i][1:]
    except: pass
    try:
      if poly[i].startswith("-1x") and len(poly[i]) > 2:
        poly[i] = "-" + poly[i][2:]
    except: pass
    try:
      if poly[i] == "1x^2": poly[i] = "x^2"
      elif poly[i] == "-1x^2": poly[i] = "-x^2"
    except: pass
    try:
      if poly[i].startswith("1x^"):
        poly[i] = "x^" + poly[i][3:]
    except: pass
    try:
      if poly[i].startswith("-1x^"):
        poly[i] = "-x^" + poly[i][4:]
    except: pass

  for i in range(len(poly)):
    if poly[i].startswith("0"): poly[i] = "1" + poly[i]

  final = " + ".join(poly)

  final = final.replace("+ -", "- ")

  if final[0] == "1" and final[2] == "x":
    final = "-" + final[1:]

  return final[:-1]

def generate(): # Generate a list of coefficients and a root for synthetic division 
  coeff = []
  root = choice([i for i in range(-30, 30) if i not in [0]])

  for i in range(randint(1, 12)):
    coeff.append(randint(-999, 999))

  for j in range(len(coeff)):
    if randint(0, 5) == 0:
      coeff.insert(randint(0, len(coeff)-1), 0)

  while coeff[0] == 0: coeff.pop(0)

  return [coeff, root]

# Pickledump test case count
try:
  with open("./count.pk", "rb") as f:
    count = load(f)
except:
  with open("./count.pk", "wb") as f:
    dump(0, f)
    count = 0

# Generate and evaluate test cases
while True:
  temp = generate()
  coeff, root = temp[0], temp[1]

  FINAL = f"({normalize(coeff)}) / " + f"(x - {root})".replace("- -", "+ ")

  if FINAL.split(" / ")[0].endswith(" + )") or FINAL.split(" / ")[0].endswith(" - )"):
    FINAL = FINAL.split(" / ")
    FINAL[0] = FINAL[0][:-4]
    FINAL = " / ".join(FINAL)

  print(FINAL)
  print()

  shreyas = shreyas_evaluate(FINAL)
  catelyn = catelyn_evaluate(FINAL)

  print(shreyas + "\n" + catelyn + "\n")

  print(shreyas == catelyn)

  if not shreyas == catelyn: break
  else:
    count += 1
    print(f"PASSED ON TEST CASE #{count}\n")

# Pickledump test case count
with open("./count.pk", "wb") as f:
  dump(count + 1, f)

# Failed test case information
print(f"-----------------------\nFAILED ON TEST CASE #{count + 1}:\n\n{FINAL}\n{shreyas}\n{catelyn}\n")

A = set(shreyas.split())
B = set(catelyn.split())

diff = A.symmetric_difference(B)

print(f"DIFFERENCE: {diff}")
