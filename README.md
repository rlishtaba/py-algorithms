# Algorithms and Data Structures.

[![Build Status](https://travis-ci.org/rlishtaba/py-algorithms.svg?branch=master)](https://travis-ci.org/rlishtaba/py-algorithms)

Library of Algorithms, Data Structures, variety of solutions to common CS problems.

![Dijkstra’s shrotest path algorithm](https://steemitimages.com/0x0/https://i.imgur.com/dWtprX5.gif)

## Installation

Add this line to your application as managed dependency:

```python
py-algorithms>=0,<1
```

Or install it globally/locally using `pip` package manager:

```bash
$ pip install py-algorithms
```

## What's inside?

    ^ Data Structures
      - Deque
      - Stack (LIFO)
      - Queue (FIFO)
      - Fibonacci Heap (https://en.wikipedia.org/wiki/Fibonacci_heap)
        - Min Heap
        - Max Heap
      - Priority Queue (Fibonacci)
        - Min PQ
        - Max PQ
      - Suffix Array
---

    ^ Search
      - Binary Search
---

    ^ Sort
      - Quick Sort
      - Shell Sort (Shell method)
      - Heap Sort (Fibonacci heap)
      - Merge Sort
      - Comb Sort
      - Bubble Sort
      - Selection Sort
---

    ^ Algorithms
      - Quick Union
      - Union Find
      - Weighted Union Find
      - Weighted Union Find with Path Compression
---

    ^ Challenges
      - TopCoder (www.topcoder.com)
      - HackerRank problems & submissions (https://www.hackerrank.com)
      - CoderByte challenges (https://coderbyte.com)
---

## Usage

Check out unit test in order to take usage examples.

### Sorting Algorithms

Sort algorithms factory methods implementation will follow
functional interface. Old school concrete type disclosure available too as well.


#### *Quick Sort

![quick-sort-media](https://upload.wikimedia.org/wikipedia/commons/6/6a/Sorting_quicksort_anim.gif)

Quicksort (sometimes called partition-exchange sort) is an efficient sorting algorithm,
serving as a systematic method for placing the elements of an array in order.
Developed by Tony Hoare in 1959 and published in 1961, it is still a commonly used algorithm for sorting.
When implemented well, it can be about two or three times faster than its main competitors, merge sort and heapsort.

    Worst case: О(n^2)
    Best case: О(n log n)
    Average: О(n log n)
    Space: O(n) naive

```python
from py_algorithms.sort import new_quick_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_quick_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```


#### *Heap Sort

![heap-sort-media](https://upload.wikimedia.org/wikipedia/commons/1/1b/Sorting_heapsort_anim.gif)

In computer science, heapsort is a comparison-based sorting algorithm.
Heapsort can be thought of as an improved selection sort: like that algorithm,
it divides its input into a sorted and an unsorted region, and it iteratively
shrinks the unsorted region by extracting the largest element and moving
that to the sorted region. The improvement consists of the use of a heap data structure
rather than a linear-time search to find the maximum.

    Worst case: О(n log n)
    Best case: О(n)
    Average: О(n log n)
    Worst case space: O(1)

```python
from py_algorithms.sort import new_heap_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_heap_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```

#### *Shell Sort

![shell-sort-media](https://upload.wikimedia.org/wikipedia/commons/d/d8/Sorting_shellsort_anim.gif)

Shellsort, also known as Shell sort or Shell's method, is an in-place comparison sort.
It can be seen as either a generalization of sorting by exchange (bubble sort) or
sorting by insertion (insertion sort). The method starts by sorting pairs of elements far apart
from each other, then progressively reducing the gap between elements to be compared.
Starting with far apart elements, it can move some out-of-place elements into position faster
than a simple nearest neighbor exchange. Donald Shell published the first version of this sort in 1959
The running time of Shellsort is heavily dependent on the gap sequence it uses. For many practical variants,
determining their time complexity remains an open problem.

    Worst case: О(n^2)
    Best case: О(n log n)
    Average: ~
    Worst case space: O(n)

```python
from py_algorithms.sort import new_shell_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_shell_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```

#### *Bubble Sort

![bubble-sort-media](https://upload.wikimedia.org/wikipedia/commons/5/54/Sorting_bubblesort_anim.gif)

Bubble sort, sometimes referred to as sinking sort, is a simple sorting algorithm that repeatedly
steps through the list to be sorted, compares each pair of adjacent items and swaps them if they are in the wrong order.

    Worst case: O(n^2)
    Best case: O(n) (if already sorted)
    Average: O(n^2)
    Worst case space: O(1)

```python
from py_algorithms.sort import new_bubble_sort

sort = new_bubble_sort() # type: Callable[[List[T]], List[T]]
sort([20,15,0,-1,70,-88])

#=> [-88, -1, 0, 15, 20, 70]
```

#### *Merge Sort

![merge-sort-media](https://upload.wikimedia.org/wikipedia/commons/c/c5/Merge_sort_animation2.gif)

In computer science, merge sort is an efficient, general-purpose,
comparison-based sorting algorithm. Most implementations produce a stable sort,
which means that the implementation preserves the input order of equal elements in the sorted output.
Mergesort is a divide and conquer algorithm that was invented by John von Neumann in 1945.

    Worst case: О(n)
    Best case: О(n log n)
    Average: О(n log n)
    Worst case space: O(n)

```python
from py_algorithms.sort import new_merge_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_merge_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```

#### *Comb Sort

![comb-sort-media](https://upload.wikimedia.org/wikipedia/commons/4/46/Comb_sort_demo.gif)

Comb sort is a relatively simple sorting algorithm originally designed by
Włodzimierz Dobosiewicz in 1980. Later it was rediscovered by Stephen Lacey and Richard Box in 1991.
Comb sort improves on bubble sort. The basic idea is to eliminate turtles,
or small values near the end of the list, since in a bubble sort these slow the sorting down tremendously.
Rabbits, large values around the beginning of the list, do not pose a problem in bubble sort.

    Worst case: О(n^2)
    Best case: О(n log n)
    Average: О(n^2)
    Worst case space: O(1)

```python
from py_algorithms.sort import new_comb_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_comb_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```

#### *Selection Sort

![selection-sort-media](https://upload.wikimedia.org/wikipedia/commons/2/25/Insertion_sort_animation.gif)

In computer science, selection sort is a sorting algorithm,
specifically an in-place comparison sort. It has O(n^2) time complexity,
making it inefficient on large lists, and generally performs worse than the similar insertion sort.
Selection sort is noted for its simplicity, and it has performance
advantages over more complicated algorithms in certain situations,
particularly where auxiliary memory is limited.

    Worst case: О(n^2)
    Best case: О(n^2)
    Average: О(n^2)
    Worst case space: O(n)

```python
from py_algorithms.sort import new_selection_sort

xs = [0, 6, 7, 8, 9, 4, 5, 12, -1]
sorting_algorithm = new_selection_sort()
sorting_algorithm(xs)

#=> [-1, 0, 4, 5, 6, 7, 8, 9, 12]
```

---

### Search Algorithms

#### *Binary Search

In computer science, binary search, also known as half-interval search, logarithmic search, or binary chop,
is a search algorithm that finds the position of a target value within a sorted array.

```python
from py_algorithms.search import new_binary_search, Search

array = [0, 4, 5, 6, 7, 8, 9, 12]
algorithm = new_binary_search() # type: Search

algorithm.search(array, 12) #=> 12
algorithm.search(array, 6)  #=> 6
```

---

### Data Structures

#### *Deque

In computer science, a double-ended queue (dequeue, often abbreviated to deque)
is an abstract data type that generalizes a queue, for which elements can be added to
or removed from either the front (head) or back (tail)

Deque implementation using doubly-linked list underneath. Operations taking
constant time.

```python
from py_algorithms.data_structures import new_deque, Deque

ds = new_deque() # type: Deque
ds.push_back(1)  #=> 1
ds.push_front(2) #=> 2
ds.front         #=> 2
ds.back          #=> 1
ds.pop_front()   #=> 2
ds.size          #=> 1
```

#### *FIFO queue

FIFO is an acronym for first in, first out, a method for organizing and manipulating a data buffer,
where the oldest (first) entry, or 'head' of the queue, is processed first.

```python
from py_algorithms.data_structures import new_queue, Queue

ds = new_queue() # type: Queue
ds.push(1)
ds.push(2)
ds.pop() #=> 1
ds.pop() #=> 2
ds.size  #=> 0
```

#### *LIFO queue. Stack.

In computer science, a stack is an abstract data type that serves as a collection of elements,
with two principal operations: push, which adds an element to the collection, and pop,
which removes the most recently added element that was not yet removed.
The order in which elements come off a stack gives rise to its alternative name, LIFO (for last in, first out).
Additionally, a peek operation may give access to the top without modifying the stack.

```python
from py_algorithms.data_structures import new_stack, Stack

ds = new_stack() # type: Stack
ds.push(1)
ds.push(2)
ds.pop() #=> 2
ds.pop() #=> 1
ds.size  #=> 0
```

#### Heap

In computer science, a Fibonacci heap is a data structure for priority queue operations,
consisting of a collection of heap-ordered trees. It has a better amortized running time
than many other priority queue data structures including the binary heap and binomial heap.
Michael L. Fredman and Robert E. Tarjan developed Fibonacci heaps in 1984 and published
them in a scientific journal in 1987. They named Fibonacci heaps after the Fibonacci numbers,
which are used in their running time analysis.

##### *Generic Heap (https://www.cs.princeton.edu/~wayne/teaching/fibonacci-heap.pdf)

Make a new heap with `Max` property by supplying functor `(a: any, b: any) => c: int`

```python
from py_algorithms.data_structures import new_heap, Heap

heap = new_heap(lambda x, y: (x > y) - (x < y) == 1) # type: Heap
```

Push distinct key value pairs to the heap

```python
heap.push('Kelly', 1)
heap.push('Susan', 8)
heap.push('Ryan', 7)
```

Heap should manage to keep highest key & value on the top

```python
heap.next_key #=> 'Susan'
heap.pop()    #=> 8
```

##### *MAX Heap (https://en.wikipedia.org/wiki/Min-max_heap)

```python
from py_algorithms.data_structures import new_max_heap, Heap

heap = new_max_heap() # type: Heap

heap.push('Kelly', 1)
heap.push('Susan', 8)
heap.push('Ryan', 7)
```

Heap should manage to keep highest key & value on the top

```python
heap.next_key #=> 'Susan'
heap.max      #=> 8
heap.pop()    #=> 8
```

##### *MIN Heap (https://en.wikipedia.org/wiki/Min-max_heap)

```python
from py_algorithms.data_structures import new_min_heap, Heap

heap = new_min_heap() # type: Heap

heap.push('One', 1)
heap.push('Eight', -8)
heap.push('Seven', 7)
```

Heap should manage to keep lowest key & value on the top

```python
heap.next_key #=> 'Eight'
heap.min      #=> -8
heap.pop()    #=> -8
```

#### Priority Queue (https://en.wikipedia.org/wiki/Priority_queue)
In computer science, a priority queue is an abstract data type which is like a
regular queue or stack data structure, but where additionally each element has a "priority"
associated with it. In a priority queue, an element with high priority is served before
an element with low priority. If two elements have the same priority,
they are served according to their order in the queue.

##### Generic Priority Queue

Example of a Max PQ data structure

```python
from py_algorithms.data_structures import new_priority_queue

pq = new_priority_queue(lambda x, y: (x > y) - (x < y) == 1)
pq.push('Important', 10)
pq.push('Not So Important', -2)
pq.pop() #=> 'Important'
```


#### Suffix Array (https://en.wikipedia.org/wiki/Suffix_array)

In computer science, a suffix array is a sorted array of all suffixes of a string.
It is a data structure used, among others, in full text indices,
data compression algorithms and within the field of bibliometrics.
Suffix arrays were introduced by Manber & Myers (1990) as a simple,
space efficient alternative to suffix trees. They have independently been discovered by
Gaston Gonnet in 1987 under the name PAT array (Gonnet, Baeza-Yates & Snider 1992).

```python
from py_algorithms.data_structures import new_suffix_array

ds = new_suffix_array('python')
ds.is_sub_str('py') #=> True
ds.is_sub_str('on') #=> True
ds.is_sub_str('ton') #=> True
ds.is_sub_str('blah') #=> False
```

---

### Algorithms

#### *Weighted Union Find With Path Compression

...

---

### Challenges

Solutions to specific area problems in Computer Science discipline.

#### Coderbyte

Solutions to various challenges published at https://coderbyte.com

#### Hackerrank

Solutions to various challenges published at www.hackerrank.com

* Binary Search Tree LCA
* Shortest Path in Unweighted Graph with cycles


## Contributing

Bug reports and pull requests are welcome on GitHub at https://github.com/rlishtaba/py-algorithms. This project is intended to be a safe, welcoming space for collaboration, and contributors are expected to adhere to the [Contributor Covenant](http://contributor-covenant.org) code of conduct.


## License

The library is available as open source under the terms of the [MIT License](http://opensource.org/licenses/MIT).
