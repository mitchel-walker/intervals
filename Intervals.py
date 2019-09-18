#  File: Intervals.py

#  Description: This program combines given intervals and prints a series of non-intersecting intervals

#  Date Created: 2/3/2019

#  Date Last Modified: 2/3/2019

def create_list(filename):
    #this function uses input text file to create a list of tuples
    lst = []
    file = open(filename, 'r')
    for line in file:
        try:
            space = line.index(' ')
            tup = (eval(line[0:space]),eval(line[space + 1:]))
            lst.append(tup)
        except ValueError:
            pass
    return lst

def combine_intervals(lst):
    #this function combines intersecting intervals from a list of tuples
    lst.sort()
    for i in range(len(lst)-1):
        if lst[i][1] >= lst[i+1][0]:
            maximum = max(max(lst[i]),max(lst[i+1]))
            lst[i+1] = (lst[i][0],maximum)
            #tuples that are combined are replaced with '0' to be removed later
            lst[i] = 0
    #remove '0'
    while 0 in lst:
        lst.remove(0)
    return lst

def sort_intervals(lst):
    #sorts list of intervals by size of the intervals
    for i in range(1,len(lst)):
        length = lst[i][1]-lst[i][0]
        place = i
        #insertion sort
        while (length < lst[place-1][1]-lst[place-1][0]) and place > 0:
            place -= 1
        lst.insert(place, lst.pop(i))
    return lst

def main():
    #this function calls the previously defined functions and prints the
    #intervals, both sorted and unsorted
    lst = create_list('intervals.txt')
    lst = combine_intervals(lst)
    print("Non-intersecting Intervals:")
    for tup in lst:
        print(tup)
    lst = sort_intervals(lst)
    print("\nNon-intersecting Intervals in order of size:")
    for tup in lst:
        print(tup)
    
    return

main()


