import numpy as np

# matrix representation of the game pay offs table
game_matrix = np.array([[-4, 6, -4, 1], [5, -7, 3, 8], [-8, 0, 6, -2]])
A_matrix = np.array([[0.5, 0, .5],]) # player A's strategy matrix
B_matrix = np.array([[0.25],[0.25],[0.25],[0.25],]) # player B's strategy matrix

### 1a) ###
# payoff = E(A, B) = A_matrix * game_matrix * B_matrix
expected_payoff = np.matmul(np.matmul(A_matrix, game_matrix), B_matrix)[0][0]
print(f"The theoretical expected payoff is {expected_payoff}.")


### b) ###
# Finding player A's best strategy knowing player B's strategy
# each pure strategy for player A
i_strategy   = np.array([[1, 0, 0],])
ii_strategy  = np.array([[0, 1, 0],])
iii_strategy = np.array([[0, 0, 1],])

# calculating the expected payoff for each of the strategies
i_payoff   = np.matmul(np.matmul(i_strategy,   game_matrix), B_matrix)[0][0]
ii_payoff  = np.matmul(np.matmul(ii_strategy,  game_matrix), B_matrix)[0][0]
iii_payoff = np.matmul(np.matmul(iii_strategy, game_matrix), B_matrix)[0][0]

# maximum payoff for player A
maximum_payoff = max((i_payoff, ii_payoff, iii_payoff))

# the optimal strategy is the one with the largest payoff
optimal_strategy = None
if maximum_payoff == i_payoff: optimal_strategy = i_strategy
elif maximum_payoff == ii_payoff: optimal_strategy = ii_strategy
elif maximum_payoff == iii_payoff: optimal_strategy = iii_strategy

print(f"{optimal_strategy[0]} is the most optimal strategy "
      f"for player A with of a payoff of {maximum_payoff}.")


### c) ###
# Finding player B's best strategy knowing player A's strategy
# each pure strategy for player B
i_strategy   = np.array([[1],[0],[0],[0],])
ii_strategy  = np.array([[0],[1],[0],[0],])
iii_strategy = np.array([[0],[0],[1],[0],])
iv_strategy  = np.array([[0],[0],[0],[1],])

# calculating the expected payoff for each of the strategies
i_payoff   = np.matmul(np.matmul(A_matrix, game_matrix), i_strategy)[0][0]
ii_payoff  = np.matmul(np.matmul(A_matrix, game_matrix), ii_strategy)[0][0]
iii_payoff = np.matmul(np.matmul(A_matrix, game_matrix), iii_strategy)[0][0]
iv_payoff  = np.matmul(np.matmul(A_matrix, game_matrix), iv_strategy)[0][0]

# maximum payoff for player B (this more negative the better it is for player B)
maximum_payoff = min((i_payoff, ii_payoff, iii_payoff, iv_payoff))

# the optimal strategy is the one with the largest (most negative) payoff
optimal_strategy = None
if maximum_payoff   == i_payoff:   optimal_strategy = i_strategy
elif maximum_payoff == ii_payoff:  optimal_strategy = ii_strategy
elif maximum_payoff == iii_payoff: optimal_strategy = iii_strategy
elif maximum_payoff == iv_payoff:  optimal_strategy = iv_strategy

print(f"{i_strategy.transpose()[0]} is the most optimal strategy for player "
      f"B with of a payoff of {maximum_payoff}.")
