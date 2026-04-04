class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temperature_tracker = [0] * len(temperatures)
        stack = []
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, index = stack.pop()
                temperature_tracker[index] = i - index
            stack.append((temperatures[i], i))
        return temperature_tracker
