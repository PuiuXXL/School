
import random

class SearchProblem:
    def __init__(self, n, x_goal, y_goal):
        self.n = n
        self.x_goal = x_goal
        self.y_goal = y_goal

    def get_initial_state(self):
        return (0, 0)

    def is_goal(self, state):
        return state == (self.x_goal, self.y_goal)

    def get_succesors(self, state):
        x, y = state
        succesors = []

        if x > 0:
            succesors.append(("up", (x - 1, y)))
        if x < self.n - 1:
            succesors.append(("down", (x + 1, y)))
        if y > 0:
            succesors.append(("left", (x, y - 1)))
        if y < self.n - 1:
            succesors.append(("right", (x, y + 1)))

        return succesors

    def do_path(self, path, state):
        for action in path:
            for move, new_state in self.get_succesors(state):
                if action == move:
                    state = new_state
                    break
        print("Final state is:", state)


def make_random_move(problem, state):
    succesors = problem.get_succesors(state)

    if succesors:
        action, new_state = random.choice(succesors)
        return action, new_state


problem = SearchProblem(5, 3, 3)

state = problem.get_initial_state()

while not problem.is_goal(state):
    action, state = make_random_move(problem, state)
    print(action, state)

print("Final")
