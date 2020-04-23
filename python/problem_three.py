import numpy as np

game_matrix = np.array([[0.7, 0.4], [0.5, 0.6],])

# D = (a + d) - (b + c)
D = (0.7 + 0.6) - (0.4 + 0.5)

# Optimal kicker strategy
# = [(d-c)/D  (a-b)/D]
kicker_strategy = np.array([(0.6 - 0.5) / D, (0.7 - 0.4)/ D])

print(f"The Kicker should kick high {round(kicker_strategy[0] * 100, 0)} percent of the time")
print(f"The Kicker should kick low  {round(kicker_strategy[1] * 100, 0)} percent of the time")

# Optimal goalie strategy
# = [(d-b)/D  (a-c)/D]
goalie_strategy = np.array([(0.6 - 0.4) / D, (0.7 - 0.5)/ D])

print(f"The goalie should block high {round(goalie_strategy[0] * 100, 0)} percent of the time")
print(f"The goalie should block low  {round(goalie_strategy[0] * 100, 0)} percent of the time")