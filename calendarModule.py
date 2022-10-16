import calendar

# ls = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
mon,day,yr = input("Enter Date (mm dd yyy): ").split()
# print(ls[calendar.weekday(int(yr), int(mon), int(day))].upper())
print(calendar.day_name[calendar.weekday(int(yr), int(mon), int(day))].upper())