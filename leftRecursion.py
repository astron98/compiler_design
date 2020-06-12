#Left-recursion removal
# Note: currently its used for only Direct-recursion grammar.

g = list()   
'''
example inputs:
i)
E->E+T | T
T->T*F | F
F->(E) | i

ii)
x->x + t | t
t->t*f | f
f->~f | (x) | true
'''

#step 1: Reading the input
#Note: For epsilon or lambda we are using 'null'
while(1):
    x = input("production rules: ")
    if(x==""):
        break
    else:
        g.append(x.strip())
print("\nprinting the user-input: ",g)

#step 2: Splitting the RHS values at " | " and storing in a Dictionary.
store  = {}
mp = {}     # for mapping the LHS with the LHS' values eg: mp[A] = A' 
for i in g:
    mp[i[0]] = str(i[0]) + "\'"
    # for j in i:
    store[i[0:3]] = i[3: len(i)].split(' | ')

#step 3: check for left-recursion and eliminate it.
result = []		

for lhs in store:
    recurr = ""
    non_recurr = ""
    for rhs in store[lhs]:
        if(lhs[0] == rhs[0]):
            # append the recurring part to "recurr" string
            recurr += str(rhs[1:]) + mp[lhs[0]] + " | "
        else:
			#append the non recurring part to "non_recurr" string
            if(rhs=="null" and len(store[lhs])>1):
                non_recurr += mp[lhs[0]] + " | "
            else:    
                non_recurr += mp[lhs[0]] + rhs + " | "
    
    recurr += "null"    # adding (null = lambda/epsilon) in the end of the LHS' part.
    if(non_recurr!=""):
            non_recurr = non_recurr[0:-3]
    ans=""    
    if(recurr!="null"): 
        # left-recursion "found", thus eliminate it.   
        result.append(lhs + non_recurr)
        result.append(mp[lhs[0]] + "->" + recurr)
    else:
        # left-recursion "not found", so just append the production rule as it is.
        ans = " ".join(str(elem + " | ") for elem in store[lhs])
        ans = str(ans[:-3])
        result.append(lhs + ans)


#step 4: printing the resulted grammar.
print("\nPrinting the resulted-grammar...\n")
for rules in result:
    print(rules)

print("\n\n...the program has ended here...")

