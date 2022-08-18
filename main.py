import calendar # calendar is "built in" -- module called sys
# import sys
# import zweeble # import something that doesn't exist - no mod named ___ in any of those paths
# from random import randint
from calendar import isleap

year = 2004

print(sys.path) # outputs list of strings (strings of folder paths) that py looks in for the want-to-be-imported modules

# could do sys.path.append(), but that's bad practice ... add one if you don't have it in that path ANOTHER way (will be covered later)

# print(calendar.isleap(year))

print(isleap(year))

# cmd on mac or alt on pc and hover-click on function from module to see its code
