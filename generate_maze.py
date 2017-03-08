import maze
import random


# Create maze using Pre-Order DFS maze creation algorithm
def create_dfs(m):
    stack = []
    cur_cell = random.randint(0, m.total_cells - 1)
    visted_cells = 1

    while visted_cells < m.total_cells:
        print(stack)
        unvisited_neighbors = m.cell_neighbors(cur_cell)
        if unvisited_neighbors:
            rand_index = random.randint(0, len(unvisited_neighbors)-1)
            new_cell = unvisited_neighbors[rand_index]
            new_cell_index = new_cell[0]
            new_cell_dir = new_cell[1]
            m.connect_cells(cur_cell, new_cell_index, new_cell_dir)
            stack.append(cur_cell)
            cur_cell = new_cell_index
            visted_cells += 1
        else:
            cur_cell = stack.pop()
        m.refresh_maze_view()
    m.state = 'solve'




def main():
    current_maze = maze.Maze('create')
    create_dfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    main()
