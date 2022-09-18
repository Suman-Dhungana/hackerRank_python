def swap_case(string):
    swapped = ""
    for st in string:
        if st.islower():
            swapped += st.upper()
        else:
            swapped += st.lower()
    return swapped


s = input("Enter the String: ")
result = swap_case(s)
print(f"Result: {result}")