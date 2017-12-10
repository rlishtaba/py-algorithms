#!/usr/bin/env python
import sys

from setuptools import find_packages
from setuptools import setup

import versioneer

if sys.version_info < (3, 5, 0):
    raise RuntimeError("Py Algorithms library requires Python 3.5.0+")

setup(
    name="py-algorithms",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Roman Lishtaba",
    author_email="roman@lishtaba.com",
    keywords=['algorithm', 'algorithms', 'data structure', 'data structures',
              'data structures python', 'containers', 'heaps', 'heap sort',
              'sorting algorithms', 'graphs', 'graph algorithms', 'hashing',
              'python', 'selection sort', 'selectionsort', 'merge sort',
              'mergesort',
              'bubble sort', 'bubblesort', 'quick sort', 'quick-sort',
              'quicksort', 'qsort',
              'binary search', 'heap', 'fibonacci heap', 'max heap', 'min heap',
              'priority queue',
              'fibonacci priority queue', 'max priority queue',
              'min priority queue',
              'dynamic connectivity', 'union find', 'quick union',
              'weighted quick union',
              'weighted quick union with path compression',
              'fibonacci heap sort', 'heapsort',
              'heap sort', 'shell-sort', 'shell sort', 'shellsort', 'comb sort',
              'comb-sort',
              'combsort', 'coderbyte', 'hackerrank', 'coderbyte challenges',
              'hackerrank challenges', 'boyer-moore',
              'boyer-moore-string-search', 'primality-tes',
              'miller-rabin', 'miller-rabin-primality-test',
              'simple-primality-test', 'topological-sort', 'directed-graph',
              'DAG', 'directed-acyclic-graph', 'simple-graph',
              'undirected-graph', 'depth-first-search', 'DFS',
              'breadth-first-search', 'BFS', 'Levenshtein Distance',
              'levenshtein-distance'],
    description="Library of Algorithms, Data Structures, "
                "variety of solutions to common "
                "CS problems.",
    long_description="Library of Algorithms, Data Structures, "
                     "variety of solutions to common "
                     "CS problems. Algorithms and Data Structures "
                     "implemented using pure awesome "
                     "Python.",
    license="MIT",
    url='https://github.com/rlishtaba/py-algorithms',
    scripts=[],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
    ],
    install_requires=[
        'packaging>=16',
        'PyYAML>=3,<4',
        'six>=1,<2',
    ],
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
)
