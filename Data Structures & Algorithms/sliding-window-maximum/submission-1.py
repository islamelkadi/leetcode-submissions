import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # First attempt
        max_elements = []
        nums = [-x for x in nums]
        for i in range(0, len(nums) - k + 1):
            heap = nums[i : i + k]
            heapq.heapify(heap)
            max_elements.append(-heap[0])
        return max_elements

        # # Step 1
        # # 1.1 Create a heapified empty list
        # # 1.2 Create the fixed sized window in that heap
        # # 1.3 Get max
        # heap = []
        # max_elements = []
        # heapq.heapify(heap)
        # for i in range(k):
        #     heapq.heappush(heap, -nums[i])
        # max_elements.append(heap[0])

        # # # Step 2
        # # for i in range(1, len(nums)):
