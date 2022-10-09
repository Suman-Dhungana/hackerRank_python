from itertools import permutations

ls=input("Enter String and length of sub string to be permutated:").split()

string= ls[0]
r = int(ls[1])
lsl = list(permutations(string,r))
for x in sorted(lsl):
    print("".join(x))