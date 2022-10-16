stampCount=int(input("Enter the total number of country stamps: "))
uniCountry=set()
for x in range(stampCount):
    uniCountry.add(input())
print(f"The number of Unique Country inputted were {len(uniCountry)}.")