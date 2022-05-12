#  Basic Functions of time module in python

import time
#  Important functions of the module:-ctime, time, strftime, strptime, localtime, gmtime, asctime, mktime

#  ctime converts time in secs from epoch into string
time_ctime = time.ctime()      # not providing any argument to ctime will take input from time.time() function
print(time_ctime)       

print(time.time())             # gives time( in secs ) from epoch until today
print(time.ctime(time.time())) # converts the time(in secs) given by time.time() to readable string

local_time = time.localtime()  # gives local time in struct_time
print(type(local_time))
print(local_time)

gmt_time = time.gmtime()       # gives GMT or UTC time in struct_time
print(type(gmt_time))
print(gmt_time)

#  To convert time_struct to string we would make use of time.strftime()
str_time = time.strftime(" %c ", gmt_time) # For more formatting options refer the official python docs
print(str_time)
str_time2 = time.strftime(" %c", local_time)
#  print(type(str_time2))
print(str_time2)

#  To convert string back into time_struct we make use of time.strptime()
struct_time = time.strptime(str_time2, " %c")   # Formatting is similar to time.strftime()
print(struct_time)

#  To convert time in tuples or time.struct_time to string of format "%c"( as represented in time.strftime() ) we make use of time.asctime()
time_tuple = (2022, 11, 4, 20, 16, 0, 0, 0, 0) # (year, month, day, hour, minutes, secs, #day of the week, #day of the year, #dst) #dst has value -1 or 0
print(time.asctime(time_tuple))

#  To convert struct_time into seconds since epoch we make use of time.mktime()
print(time.mktime(struct_time))
