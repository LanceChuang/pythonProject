def permute(s):
    out = []
    
    # base case
    if len(s) == 1:
        out = [s]
    else:
    #     for every letter in string
        for i,let in enumerate(s):
            # for every permutation resulting from step 2 and 3
#             print(i,let)
            for perm in permute(s[:i]+s[i+1:]):
#                 print(s[:i])
                
                # print("My current letter is: ",let)
                # print("The perm is: ",perm)
                # add it to the output
                out += [let+perm] 
                # print("the output is: ",out)
    
    return out
ans = permute('abc')
print(ans)

# if input is number , we can use itertools
from itertools import permutations
l = list(permutations(range(1, 4)))
print(l)