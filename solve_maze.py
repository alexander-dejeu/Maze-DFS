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
    # TODO: Implement solve_bfs
    pass


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
