def synth_alg(test, root):
  final = [test[0]]

  for i in range(len(test) - 1):
    final.append((root*final[i]) + test[i + 1])

  for i in range(len(final)-1):
    final[i] = str(final[i]) + "x^" + str(len(test) - 2 - i)

  if (root*-1) > 0:
    final[-1] = str(final[-1]) + " / (x + " + str(root*-1) + ")"
  else:
    final[-1] = str(final[-1]) + " / (x - " + str(root*-1) + ")"
  
  for i in range(len(final)):
    temp = final[i]
    if temp[0] == "0":
      final[i] = ""
    elif "^0" in temp:
      final[i] = temp[0:temp.index("x")]
    elif temp[-2:] == "^1":
      final[i] = temp[0:temp.index("^")]
    elif temp[0:2] == "1x":
      final[i] = temp[1:]
    elif temp[0:3] == "-1x":
      final[i] == "-" + temp[2:]

  while "" in final:
      del final[final.index("")]

  st = final[0]

  for i in range(1, len(final)):
    if (final[i])[0] == "-":
      st += " - "
      final[i] = (final[i])[1:]
    else:
      st += " + "
    st += final[i]

  st = st.replace("+ -","- ")
  st = st.replace("- -","+ ")
  
  return st
