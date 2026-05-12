import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # # First attempt
        # max_elements = []
        # nums = [-x for x in nums]
        # for i in range(0, len(nums) - k + 1):
        #     heap = nums[i : i + k]
        #     heapq.heapify(heap)
        #     max_elements.append(-heap[0])
        # return max_elements

        # Second attempt - more optimized
        # Step 1
        # 1.1 Create a heapified empty list
        # 1.2 Create the fixed sized window in that heap
        if k == 1:
            return nums

        heap = []
        heapq.heapify(heap)
        for i in range(k):
            heapq.heappush(heap, (-nums[i], -i))

        # Add max element
        max_elements = [-heap[0][0]]

        # Step 2
        for i in range(k, len(nums)):
            heapq.heappush(heap, (-nums[i], -i))

            # This means that the left most boundary's index
            # is still greater than that of the current heap
            # max. This means the heap is no longer within
            # bounds
            while i - k >= -heap[0][1]:
                heapq.heappop(heap)

            max_elements.append(-heap[0][0])
        return max_elements
