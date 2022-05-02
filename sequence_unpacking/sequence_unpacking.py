#  Sequence unpacking involves extracting values from sequences in python( eg:- list, tuples, dictionary.. ) into variables

#  Most basic sequence unpacking
splits_data = ("10/2/2022", 60, 10, 10)
date, pace, time, miles = splits_data
import sys
print("Date :", date, "Pace :", pace, "Time :", time, "Miles :", miles, sep=' ', end='\n', file=sys.stdout, flush=False)

#  Sequences can also be present inside sequences themselves
new_splits_data = ("10/2/2022", 60, 10, (10, 20, 30, 40, 50))
date, pace, time, splits_mile = new_splits_data
print(splits_mile)

#  Extracting values form splits_mile
date, pace, time, (mile_1, mile_2, mile_3, mile_4, mile_5) = new_splits_data
print("Mile 1:", mile_1, "Mile_2 :", mile_2, "Mile_3 :", mile_3, "Mile_4 :", mile_4, "Mile_5 :", mile_5, sep=' ', end='\n', file=sys.stdout, flush=False)

#  Extracting only select values from sequences by making use of '_' operator in python 
new_split_data = ("10/12/2001", 40, 10, (1, 2, 3, 4, 5))
_, pace, _, mile = new_split_data
print("Pace :", pace, "Mile :", mile, sep=' ', end='\n', file=sys.stdout, flush=False)

#  Sequence unpacking using python * operator (here we are storing the middle values in a list)
date, pace, time, ( first, *middle, last ) = new_splits_data
print( "First :", first, "Middle :", middle, "Last :", last )

#  Sequence extracting using dictionary
new_split_dict = ("10/2/2022", 60, 10, {'Mile_1':10, 'Mile_2':20, 'Mile_3':30, 'Mile_4':40, 'Mile_5':50})
_, _, _, split_withdict = new_split_dict
print(split_withdict)
print(split_withdict['Mile_3'])     #Accessing values from tuple new_split_dict
