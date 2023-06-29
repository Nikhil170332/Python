import re
date = input("enter the date in (YYYY-MM-DD):")
result = re.sub("(\d{4})-(\d{2})-(\d{2})",r"\3-\2-\1",date)
print(f"before changing {date}, after changing {result}")