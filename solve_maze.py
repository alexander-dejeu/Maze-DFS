import maze
import generate_maze
import sys
import random

# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # Going to need a stack for backtracking
    stack = []
    cur_cell = 0
    visted_cells = 0

    goal = m.total_cells-1
    while cur_cell != goal:
        unvisited_neighbors = m.cell_neighbors(cur_cell)
        if unvisited_neighbors:
            rand_index = random.randint(0, len(unvisited_neighbors)-1)
            rand_neighbor = unvisited_neighbors[rand_index]
            m.visit_cell(cur_cell, rand_neighbor[0], rand_neighbor[1])
            stack.append(cur_cell)
            cur_cell = rand_neighbor[0]
            visted_cells += 1
        else:
            m.backtrack(cur_cell)
            cur_cell = stack.pop()
        m.refresh_maze_view()
    m.state = 'idle'




# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    queue = []
    cur_cell = 0
    direction = 0b0000
    visited_cells = 0
    queue.append((cur_cell, direction))

    goal = m.total_cells-1
    while cur_cell != goal and queue is not []:
        cell = queue.pop(0)
        cur_cell = cell[0]
        cur_dir = cell[1]

        m.bfs_visit_cell(cur_cell, cur_dir)
        visited_cells += 1
        m.refresh_maze_view()

        unvisited_neighbors = m.cell_neighbors(cur_cell)
        for cell in unvisited_neighbors:
            queue.append((cell[0], cell[1]))
    m.reconstruct_solution(cur_cell)
    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
