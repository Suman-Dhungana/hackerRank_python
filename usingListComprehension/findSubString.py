def count_substring(string, sub_string):
    sub_len = len(sub_string)
    new = [n for n in range(len(string)) if string[n:n+sub_len] == sub_string and len(string[n:n+sub_len]) == sub_len]
    return (len(new))


string = input("Enter Test String: ").strip()
sub_string = input("Enter Sub String: ").strip()
count = count_substring(string, sub_string)
print(f"Occurence of \"{sub_string}\" substring: {count}")