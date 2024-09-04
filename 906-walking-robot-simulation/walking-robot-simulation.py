class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Directions represented as (dx, dy): North, East, South, West
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        d, x, y, res = 0, 0, 0, 0
        s = set(map(tuple, obstacles))  # Set for obstacle positions
        
        for command in commands:
            if command == -1:  # Turn right
                d = (d + 1) % 4
            elif command == -2:  # Turn left
                d = (d - 1) % 4
            else:
                dx, dy = directions[d]  # Current direction vector
                for _ in range(command):
                    if (x + dx, y + dy) in s:  # Check if next step is an obstacle
                        break
                    x += dx
                    y += dy
                res = max(res, x**2 + y**2)  # Update maximum distance squared
        
        return res