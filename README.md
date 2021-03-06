# Aim
Create a list module containing several common Python list methods and built-in
functions.

Working on this project helps build a strong understanding of **lists** in
Python. It also indicates my ability to understand how each list method and
built-in function works; and to implement them in my program.

# Implementation
The program *list_function.py* solely contains functions that have been defined,
whereas the program *tester.py* is a test driver that is able to be run to check
the successful usage of each pre-defined function in the program
*list_function.py*.

The following functions are defined:
1. size(my_list)
2. to_string(my_list , sep=', ')
3. count_item(value, my_list)
4. search(value, my_list)
5. insert_item(value, insert_position. my_list)
6. remove_index(remove_position, my_list)
7. get_unique(my_list)

# Usage
1. size() processes a list and return its length.
2. to_string() processes a list and return the string version of it.
3. count_item() receives a value and return the occurrences of that value in the
   given list.
4. search() receives a value and return the location of that value in the given
   list.
5. insert_item() receives a list and return a copy with a value inserted into
   the list at the specified index.
6. remove_index() receives a list and return a copy with the item at the
   specified index removed from the list.
7. get_unique() receives a list and return a copy which contains only the unique
   items from the original list.

# Restrictions
In order to keep the idea of the project pure, the followings are restricted to
use:
* Built-in functions such as len(), list(), slice(), sum(), min(), max().
* List methods such as index(), pop(), count(), insert().
* String methods such as join(), split(), count(), index().

# Sample Output
```
-----------------
| START TESTING |
-----------------

SIZE
Expected: 7
     Got: 7
        PASSED 1/26 (+1)
Expected: 0
     Got: 0
        PASSED 2/26 (+1)
Expected: 6
     Got: 6
        PASSED 3/26 (+1)

TO_STRING
Expected: r, i, n, g, i, n, g
     Got: r, i, n, g, i, n, g
        PASSED 4.5/26 (+1.5)
Expected: r-i-n-g-i-n-g
     Got: r-i-n-g-i-n-g
        PASSED 6/26 (+1.5)
Expected: 1, 7, 2, 3, 7, 7
     Got: 1, 7, 2, 3, 7, 7
        PASSED 6.5/26 (+0.5)
Expected: 1 - 7 - 2 - 3 - 7 - 7
     Got: 1 - 7 - 2 - 3 - 7 - 7
        PASSED 7/26 (+0.5)

COUNT_ITEM
Expected: 2
     Got: 2
        PASSED 8/26 (+1)
Expected: 0
     Got: 0
        PASSED 9/26 (+1)
Expected: 3
     Got: 3
        PASSED 10/26 (+1)

SEARCH
Expected: 3
     Got: 3
        PASSED 11/26 (+1)
Expected: None
     Got: None
        PASSED 12/26 (+1)
Expected: 1
     Got: 1
        PASSED 13/26 (+1)

INSERT_ITEM
Expected: ['one', 'two', 'three', 'four', 'five', 'six']
     Got: ['one', 'two', 'three', 'four', 'five', 'six']
        PASSED 14/26 (+1)
Expected: ['i', 't', 's']
     Got: ['i', 't', 's']
        PASSED 15/26 (+1)
Expected: ['s', 'i', 't']
     Got: ['s', 'i', 't']
        PASSED 16/26 (+1)
Expected: ['p', 'i', 't']
     Got: ['p', 'i', 't']
        PASSED 17/26 (+1)
Expected: [1, 2, 3, 4, 5, 6]
     Got: [1, 2, 3, 4, 5, 6]
        PASSED 18/26 (+1)

REMOVE_INDEX
Expected: ['r', 'i', 'g']
     Got: ['r', 'i', 'g']
        PASSED 19/26 (+1)
Expected: ['i', 'n', 'g']
     Got: ['i', 'n', 'g']
        PASSED 20/26 (+1)
Expected: ['r', 'i', 'n']
     Got: ['r', 'i', 'n']
        PASSED 21/26 (+1)
Expected: []
     Got: []
        PASSED 22/26 (+1)
Expected: [1, 4, 5, 6]
     Got: [1, 4, 5, 6]
        PASSED 23/26 (+1)

GET_UNIQUE
Expected: ['a', 'b', 'c', 'd']
     Got: ['a', 'b', 'c', 'd']
        PASSED 25/26 (+2)
Expected: [1, 3, 2, 4]
     Got: [1, 3, 2, 4]
        PASSED 26/26 (+1)

---------------
| END TESTING |
---------------

Final Result: [26/26]

Well done 'list' master!
```
