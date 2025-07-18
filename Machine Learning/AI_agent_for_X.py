import numpy as np
import random
import time

# Setup for the environment
grid_rows = 5      # Vertical positions (agent begins at lowest row)
grid_cols = 5      # Sideways positions
movements = 3      # 0: Move left, 1: Move right, 2: Move up

# Initialize Q-values table (rows x columns x possible moves)
Q_values = np.zeros((grid_rows, grid_cols, movements))

# Learning configuration
training_sessions = 1000      # Total number of learning iterations
alpha = 0.8                  # Learning speed factor
discount = 0.9               # Importance of future rewards
exploration_chance = 0.3     # Probability of random exploration

# Training process
for session in range(training_sessions):
    current_row = grid_rows - 1  # Begin at the bottom
    current_col = random.randint(0, grid_cols - 1)  # Random column start

    completed = False
    while not completed:
        # Choose action: explore or exploit
        if random.random() < exploration_chance:
            chosen_action = random.randint(0, movements - 1)  # Random exploration
        else:
            chosen_action = np.argmax(Q_values[current_row, current_col])  # Best known move

        # Calculate new position
        new_row, new_col = current_row, current_col
        if chosen_action == 0 and new_col > 0:
            new_col -= 1  # Go left
        elif chosen_action == 1 and new_col < grid_cols - 1:
            new_col += 1  # Go right
        elif chosen_action == 2 and new_row > 0:
            new_row -= 1  # Advance upward

        # Determine reward
        if new_row == 0:
            reward = 10  # Successfully reached top
            completed = True
        else:
            reward = -1  # Cost for each step

        # Update Q-value
        current_q = Q_values[current_row, current_col, chosen_action]
        best_future = np.max(Q_values[new_row, new_col])
        Q_values[current_row, current_col, chosen_action] = current_q + alpha * (reward + discount * best_future - current_q)

        # Transition to new state
        current_row, current_col = new_row, new_col

# Evaluate the trained agent starting from middle bottom
current_row, current_col = 4, 2  # Center starting point
step_count = 0

print("\nAgent's navigation path:")

while current_row != 0:
    # Visualize current state
    display_grid = [["." for _ in range(grid_cols)] for _ in range(grid_rows)]
    display_grid[current_row][current_col] = "A"  # Mark agent
    display_grid[0][current_col] = "T"           # Target position

    for r in range(grid_rows):
        print(" ".join(display_grid[r]))
    print("-" * 20)

    # Select optimal action
    chosen_action = np.argmax(Q_values[current_row, current_col])
    if chosen_action == 0 and current_col > 0:
        next_row, next_col = current_row, current_col - 1
    elif chosen_action == 1 and current_col < grid_cols - 1:
        next_row, next_col = current_row, current_col + 1
    elif chosen_action == 2 and current_row > 0:
        next_row, next_col = current_row - 1, current_col
    else:
        next_row, next_col = current_row, current_col  # No movement if invalid

    print(f"Step {step_count}: At ({current_row}, {current_col}) -> Chose {['Left', 'Right', 'Up'][chosen_action]} -> Moves to ({next_row}, {next_col})\n")
    time.sleep(0.5)  # Brief delay for visualization

    current_row, current_col = next_row, next_col
    step_count += 1

# Display final state at target
final_grid = [["." for _ in range(grid_cols)] for _ in range(grid_rows)]
final_grid[current_row][current_col] = "A"
final_grid[0][current_col] = "T"

for r in range(grid_rows):
    print(" ".join(final_grid[r]))

print(f"Achieved target in {step_count} steps.")