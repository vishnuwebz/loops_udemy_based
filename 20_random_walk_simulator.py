# 3 random walk simulator

import random
position = 0
steps = []
for _ in range(10):
    step = random.choice([-1, 1])  # Move left or right
    position += step
    steps.append(position)
print(f"Random Walk: {steps}")

# Random Walk: [-1, 0, 1, 0, -1, 0, -1, 0, -1, -2]