class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        seen = set()
        dic = {0:(-1, 0), 1:(0, 1), 2:(1, 0), 3:(0, -1)}
        def dfs(x, y, direction):
            robot.clean()
            seen.add((x, y))
            for i in range(4):
                dir1 = (direction + i) % 4
                if (x+dic[dir1][0], y+dic[dir1][1]) in seen:
                    robot.turnRight()
                    continue
                if not robot.move():
                    robot.turnRight()
                    continue
                dfs(x+dic[dir1][0], y+dic[dir1][1], dir1)
                robot.turnRight()
                robot.turnRight()
                robot.move()
                robot.turnRight()
                robot.turnRight()
                robot.turnRight()
        dfs(0, 0, 0)