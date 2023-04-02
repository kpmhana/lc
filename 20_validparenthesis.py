p = []
last = ""
str = "}{([}]){}"
result = False
for i, val in enumerate(str):
    if val in "({[":
        p.append(val)
        continue
    
    if(len(p) != 0):
        last = p[-1]
    if val == ")" and last == "(":
        p.pop()
    elif val == "}" and last == "{":
        p.pop()
    elif val == "]" and last == "[":
        p.pop()
    else:
        break
    
if len(p) == 0 and last != "":
    result = True

print(result)

