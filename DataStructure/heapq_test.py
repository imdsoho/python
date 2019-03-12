# -*- coding: utf-8 -*-

# 데이터를 정렬된 상태로 저장하기 위해서 사용
# heapq 모듈은 이진 트리(binary tree) 기반의 최소 힙(min heap) 자료구조를 제공
# min heap을 사용하면 원소들이 항상 정렬된 상태로 추가되고 삭제되며, min heap에서 가장 작은값은 언제나 인덱스 0, 즉, 이진 트리의 루트에 위치합니다.
# heapq 모듈에은 파이썬의 보통 리스트를 마치 최소 힙처럼 다룰 수 있도록 도와줍니다.
# 그냥 빈 리스트를 생성해놓은 다음 heapq 모듈의 함수를 호출할 때 마다 이 리스트를 인자로 넘겨야 합니다.
# 파이썬에서는 heapq 모듈을 통해서 원소를 추가하거나 삭제한 리스트가 그냥 최소 힙입니다.

# 힙에 원소를 추가 - heappush()
import heapq

heap = []
heapq.heappush(heap, 4)
heapq.heappush(heap, 1)
heapq.heappush(heap, 7)
heapq.heappush(heap, 3)

print(heap)

# 힙에서 원소를 삭제 - heappop()
print(heapq.heappop(heap))
print(heap)

# 최소값 삭제하지 않고 얻기
print(heap[0])

# 주의사항은 인덱스 0에 가장 작은 원소가 있다고 해서, 인덱스 1에 두번째 작은 원소, 인덱스 2에 세번째 작은 원소가 있다는 보장은 없다는 것입니다.
# 왜냐하면 힙은 heappop() 함수를 호출하여 원소를 삭제할 때마다 이진 트리의 재배치를 통해 매번 새로운 최소값을 인덱스 0에 위치시키기 때문입니다.

# 기존 리스트를 힙으로 변환 - heapify()
# 원소가 들어있는 리스트 힙으로 만든다.
# heapify() 함수에 리스트를 인자로 넘기면 리스트 내부의 원소들의 위에서 다룬 힙 구조에 맞게 재배치되며 최소값이 0번째 인덱스에 위치됩니다.
# 즉, 비어있는 리스트를 생성한 후 heappush() 함수로 원소를 하나씩 추가한 효과가 납니다.
# heapify() 함수의 성능은 인자로 넘기는 리스트의 원소수에 비례합니다.
# 즉 O(N)의 시간 복잡도를 가집니다.

heap = [4, 1, 7, 3, 8, 5]
heapq.heapify(heap)

print(heap)

# 최대 힙
# 힙에 튜플(tuple)를 원소로 추가하거나 삭제하면, 튜플 내에서 맨 앞에 있는 값을 기준으로 최소 힙이 구성되는 원리를 이용하는 것입니다.
# 따라서, 최대 힙을 만들려면 각 값에 대한 우선 순위를 구한 후, (우선 순위, 값) 구조의 튜플(tuple)을 힙에 추가하거나 삭제하면 됩니다.
# 그리고 힙에서 값을 읽어올 때는 각 튜플에서 인덱스 1에 있는 값을 취하면 됩니다. (우선 순위에는 관심이 없으므로)

nums = [4, 1, 7, 3, 8, 5]
heap = []

for num in nums:
    heapq.heappush(heap, (-num, num))  # (우선 순위, 값)

    while heap:
        print(heapq.heappop(heap)[1])  # index 1


# K번째 최소값/최대값
# 최소 힙이나 최대 힙을 사용하면 K번째 최소값이나 최대값을 효츌적으로 구할 수 있습니다.
# K번째 최소값을 구하기 위해서는 주어진 배열로 힙을 만든 후, heappop() 함수를 K번 호출하면 됩니다.

def kth_smallest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)

        kth_min = None

        for _ in range(k):
            kth_min = heapq.heappop(heap)

    return kth_min

print(kth_smallest([4, 1, 7, 3, 8, 5], 3))


# 힙 정렬
# 힙 정렬(heap sort)은 위에서 설명드린 힙 자료구조의 성질을 이용한 대표적인 정렬 알고리즘입니다.

def heap_sort(nums):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        sorted_nums = []

        while heap:
            sorted_nums.append(heapq.heappop(heap))

    return sorted_nums

    print(heap_sort([4, 1, 7, 3, 8, 5]))

# 가장 큰 n개의 원소 - heapq.nlargest(n, iterable, key=None)

# 가장 작은 n개의 원소 - heapq.nsmallest(n, iterable, key=None)

# 리스트 합치기 - heapq.merge(*iterables, key=None, reverse=False)

# heapq.merge(L1, L2)는 L1, L2가 정렬되어 있다고 가정하고 이 둘을 정렬된 채로 합치는 generator를 만듭니다.
# 정렬된 iterator를 반환한다.
# 비슷한 함수로 sorted(itertools.chain(*iterables)) 가 있는데, iterable을 반환한다.

# [참조]http://www.daleseo.com/python-heapq/
