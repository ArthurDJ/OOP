import queue

dirsx = [1, 0, 0, -1]
dirsy = [0, -1, 1, 0]
dir = ['D', 'L', 'R', 'U']
path = []
res = ""


def setupMaze():
    """ Setup an 8x8 max
        0 is  square we can move through, 1 is a rock"""
    return \
        [[0, 1, 0, 0, 1, 1, 0, 1], \
         [0, 1, 1, 0, 0, 1, 0, 1], \
         [0, 0, 0, 0, 0, 1, 0, 1], \
         [0, 0, 1, 0, 0, 1, 0, 1], \
         [1, 0, 1, 0, 0, 0, 0, 0], \
         [1, 0, 0, 0, 0, 1, 1, 0], \
         [0, 0, 1, 0, 0, 1, 0, 0], \
         [1, 1, 1, 1, 0, 0, 0, 0], \
         ]


def markVis(maze, pos):
    maze[pos[0]][pos[1]] = -1


def judgeMark(maze, pos):
    return maze[pos[0]][pos[1]] == 0


def judgePos(maze, pos):
    if len(maze[0]) > pos[0] >= 0 and len(maze[1]) > pos[1] >= 0:
        return True
    return False


def dfs(maze, pos, end):
    markVis(maze, pos)
    if pos == end:
        path.append(pos)
        return True
    for i in range(4):
        nextpos = (pos[0] + dirsx[i], pos[1] + dirsy[i])
        if judgePos(maze, nextpos) and judgeMark(maze, nextpos) and dfs(maze, nextpos, end):
            path.append(pos)
            global res
            res += dir[i]
            return True
    return False


def print_path(path):
    for i in range(0, len(path)):
        print(path[i][0], dir[path[i][1]])


def maze_huisu(maze, start, end):
    if start == end:
        print(start)
        return
    # path = queue.LifoQueue()
    path = []
    markVis(maze, start)
    path.append((start, 0))
    while len(path) != 0:
        pos, nextdir = path.pop()
        for i in range(nextdir, 4):
            nextpos = (pos[0] + dirsx[i], pos[1] + dirsy[i])
            if nextpos == end:
                print_path(path)
                return
            if judgePos(maze, nextpos) and judgeMark(maze, nextpos):
                path.append((pos, i + 1))
                markVis(maze, nextpos)
                path.append((nextpos, 0))
                break


def main():
    maze = setupMaze()
    # dfs(maze, (0, 0), (len(maze[0]) - 1, len(maze[1]) - 1))
    # print(path[::-1])
    # print(res[::-1])
    maze_huisu(maze, (0, 0), (len(maze[0]) - 1, len(maze[1]) - 1))


if __name__ == '__main__':
    main()
