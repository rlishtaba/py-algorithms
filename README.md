# Python Algorithms

[![Build Status](https://travis-ci.org/rlishtaba/py-algorithms-playground.svg?branch=master)](https://travis-ci.org/rlishtaba/py-algorithms)


## Installation

Add this line to your application as managed dependency:

```python
py-algorithms>=0,<1
```

Or install it using `pip` package manager:

    $ pip install py-algorithms

## What's inside?

    ^ Data Structures
      - Deque
      - Stack (LIFO)
      - Queue (FIFO)
      - Priority Queue

    ^ Search
      - Binary Search

    ^ Sorting
      - Bubble Sort

    ^ Agorithms
      - Quick Union
      - Union Find
      - Weighted Union Find
      - Weighted Union Find with Path Compression

## Usage

### Sorting

Sort algorithms factory methods implementation will follow
functional interface. Old school concrete type disclosure available too as well

    from py_algorithms.sort import new_bubble_sort

    bubble_sort = new_bubble_sort() # returns function of a Sort interface to apply

    bubble_sort([20,15,0,-1,70,-88])

    # => [-88, -1, 0, 15, 20, 70]

Same as

    from py_algorithms.sort import BubbleSort, Sort

    bubble_sort = BubbleSort() # type: Sort

    bubble_sort.sort([20,15,0,-1,70,-88])

    # => [-88, -1, 0, 15, 20, 70]


### Search

    from py_algorithms.search import binary_search, Search

    algorithm = binary_search() # type: Sesrch

    algorithm.search([0, 6, 7, 8, 9, 4, 5, 12], 1)

    # => 12


### Data Structures

#### Deque

Deque implementation using doubly-linked list underneath. Operations taking
constant time.

    from py_algorithms.data_structures import new_deque

    ds = new_deque()
    ds.push_back(1)  #=> 1
    ds.push_front(2) #=> 2
    ds.front         #=> 2
    ds.back          #=> 1
    ds.pop_front()   #=> 2
    ds.size          #=> 1


#### FIFO queue

    from py_algorithms.data_structures import new_queue

    ds = new_queue()
    ds.push(1)
    ds.push(2)
    ds.pop() #=> 1
    ds.pop() #=> 2
    ds.size  #=> 0


#### LIFO queue. Stack.

    from py_algorithms.data_structures import new_stack

    ds = new_stack()
    ds.push(1)
    ds.push(2)
    ds.pop() #=> 2
    ds.pop() #=> 1
    ds.size  #=> 0

### Algorithms


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rlishtaba/py-algorithms. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The library is available as open source under the terms of the [LGPL v3 License](http://opensource.org/licenses/LGPLv3).
