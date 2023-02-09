# Find a path from the start to the end in given mazz

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x,y: (x+1, y),
    lambda x,y: (x-1, y),
    lambda x,y: (x, y+1),
    lambda x,y: (x, y-1),
]

def maze_path(x1, y1, x2, y2):
    # (x1,y1) is the start and (x2, y2) is the end pf the maze
    stack = []
    stack.append((x1, y1))
    while len(stack) > 0:
        cur_node = stack[-1] #Current node

        if cur_node[0] == x2 and cur_node[1] == y2:
            for location in stack:
                print(location)
            return True

        for dir in dirs:
            next_node = dir(cur_node[0], cur_node[1])
            if maze[next_node[0]][next_node[1]] == 0:
                # If there is a direction to go, append next node to the stack
                stack.append(next_node)
                # change the maze to indicate next_code is included in the path
                maze[next_node[0]][next_node[1]] = 2
                break

        else:
            # If there's no available path, return to the previous path
            maze[next_node[0]][next_node[1]] = 2
            stack.pop()

    # If ends up with empty stack
    print('No path')
    return False

maze_path(1, 1, 7, 9)
