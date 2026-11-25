class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        pos_to_speed = [(pos, speed) for pos, speed in zip(position, speed)]
        pos_to_speed.sort(key = lambda x : x[0], reverse=True)

        for pos, speed in pos_to_speed:
            time = (target-pos)/speed
            if stack and time <= stack[-1]:
                continue
            else:
                stack.append(time)
        return len(stack)