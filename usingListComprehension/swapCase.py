def swapCase(string):
    listl = [(st.upper() if st.islower() else st.lower()) for st in string]
    return "".join(listl)

s = input("Enter the String: ")
result = swapCase(s)
print(f"Result: {result}")