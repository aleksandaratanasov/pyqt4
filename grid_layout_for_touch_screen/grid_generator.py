#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:44:35 2015

@author: Aleksandar Vladimirov Atanasov
@author: 
"""

'''
Newton's method for computing integer square root
@return: largest integer X for which x*x does not exceed n
'''
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x
    
    
def get_dim(list_len):
    col = isqrt(list_len)

    # special cases
    # 1x1 for a list with a single element
    if list_len == 1:
        return (1, 1)
    # empty list
    if list_len == 0:
        return (0, 0)
    # perfect sqrt numbers produce a square matrix without empty cells
    if col**2 == list_len:
        return (col, col)
    # all the rest
    # following is suitable for displays with height < width
    # it can easily be reversed so that it can handle height > width
    elif col**2 < list_len <= col*(col+1):
        return (col, col+1)
    elif col*(col+1) < list_len <= (col+1)**2:
        return (col+1, col+1)

def main():
    # Sample data generator
    names = []
    num_of_items = 11
    for i in range(0, num_of_items):
        names.append(str(i))
    
    n = len(names)
    
    (rows, cols) = get_dim(n)
    print 'grid (rows x cols): ' + str(rows) + 'x' + str(cols)
    
    num_empty_cells = abs(len(names) - rows*cols)
    num_full_cells = rows*cols - num_empty_cells
    print 'num of empty cells:', num_empty_cells
    print 'num of full cells:', num_full_cells
    nameIdx = 0
    for r in range(0, rows):
        print '\t'
        for c in range(0, cols):
            print '',
            if nameIdx < len(names):
                print '[' + str(r) + '][' + str(c) + '] : ' + names[nameIdx] + '\t',
                nameIdx = nameIdx + 1
            else:
                print '[' + str(r) + '][' + str(c) + '] : ' + '@\t',

if __name__ == '__main__':
    main()
