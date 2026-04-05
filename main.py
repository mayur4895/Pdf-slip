import random
from sorting.heap_sort import heap_sort
from sorting.selection_sort import selection_sort
from graph.bfs import bfs
from matrix.strassen import strassen
from utils.timer import measure_time

arr = [random.randint(1, 100) for _ in range(10)]
print("Heap Sort Before:", arr)
print("Heap Sort After:", measure_time(heap_sort, arr.copy()))

print("\nSelection Sort Before:", arr)
print("Selection Sort After:", measure_time(selection_sort, arr.copy()))

graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}
print("\nBFS Traversal:", bfs(graph, 0))

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
print("\nStrassen Result:", strassen(A, B))
