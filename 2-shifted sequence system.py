import ast

def replace_all_entries(s,n):
    for i in range(len(s)):
        if s[i] < n:
            s[i] = n-1
    return s

def expand(s,n):
    last = s[len(s)-1]
    if last == 0:
        s.pop()
        return s
    else:
        for i in range(len(s)-2,-1,-1):
            if s[i] < last:
                t = replace_all_entries(s[i:],last)
                for j in range(i-1,-1,-1):
                    if s[j] <= last-1:
                        u = replace_all_entries(s[j:],last)
                        if u < t:
                            possible_bad_parts = []
                            for k in range(j+1,len(s)):
                                if s[k] < last :
                                    possible_bad_parts.append(replace_all_entries(s[k:len(s)-1],last))
                            bad_part = max(possible_bad_parts)
                            for l in range(len(bad_part)):
                                if bad_part[l] < last:
                                    bad_part[l] = last-1
                            s.pop()
                            for l in range(n):
                                s.extend(bad_part)
                            return s
def large_number():
    n = 100
    for i in range(100):
        a = [0,0,n]
        while (a != []):
            expand(a,n)
            n += 1
    return n

a = ast.literal_eval(input("What do you expand? Example: [0,0,2,1,2]\n"))
b = int(input("Expansion factor? Example: 3\n"))
c = int(input("How many times do you expand? Example: 10\n"))
d = input("Max length of the sequence after expansion? (leave it blank for no limit) Example: 20\n")
if d != "":
    d = int(d)
for i in range(c):
    print(a)
    if a == []:
        break
    expand(a,b)
    if d != "":
        a = a[:d]