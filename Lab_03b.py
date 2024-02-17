"""
    CSC 309 SFSU Spring 2023
    Lab #3b
    Created on Wed Feb 12 02:27:49 2024
    Last updated on Feb 16 01:55
    @author: scottquashen
    
    Description: 
        This program implements a function that sorts any list of numbers.

    Inputs: 
        List 

    Outputs: 
        incremental sorting of our List

    Dependencies: time

    Assumptions: developed and tested using Spyder 5.4.3, Python version 3.11.5 on macOS 14.2.1
"""


# Import all of your modules needed for this project.
import time

# Print your name and current time in a single line of python code.
print("Scott Quashen... ", time.asctime())
# Create a Python list L=[4, 2, 5, 3, 1]

L = [4, 2, 5, 3, 1]

# Replace one item at a time 
def customSort( someList ):
    """
    
    Description
    ----------Loop that sorts items in list from left to right handling last item independently
    Parameters
    ----------someList : List  
    Returns
    -------None.
    Usage
    -------customSort( L ).

    """
    for i in range(0, len( someList ) - 1):
            # customSort last element
            if i + 1 >= len( someList ):
                
                # customSort if the last item needs to be swapped
                if ( someList[ i  ] > someList[ i - 1 ]):
                   c = someList [ i  ]
                   someList [ i  ] = someList [ i - 1 ]
                   someList [ i - 1] = c
                   print( someList )
                   # customSort middle elements       
            elif someList[ i + 1 ] < someList[ i ]:
                    # swap items 
                    c = someList [ i ]
                    someList [ i ] = someList [ i + 1 ]
                    someList [ i + 1 ] = c
                    # perform prints() to show incremental processing 
                    print( someList )
            
                    
# Repeat this process until all items are in correct order               
def callSortUntillFinishedLoop( someList ):
    """
    
    Description
    ----------Loop that calls custom sort func untill customSort 'finished' passes
    Parameters
    ----------someList : List  
    Returns
    -------None.
    Usage
    -------callSortUntillFinishedLoop( L ).

    """
    finished = False
    while not finished:
        for i in range(len(someList)):
            if i > 0:
                if someList[i - 1] > someList[i]:
                    customSort( someList )
                    
                else:
                    # all previous items are sorted, now we customSort for completion
                    # including the final item in our list
                    for i in range(len( someList )):
                        if i > 0:
                            if someList[ i - 1 ] > someList[ i ]:
                                customSort( someList )
                            if i == len( someList ) - 1:
                                # all done, end the loop to stop sorting
                                finished = True 
                                
""" FUNCTION CALLS BELOW"""
# sort the list
callSortUntillFinishedLoop( L )


















