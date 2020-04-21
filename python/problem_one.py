import numpy as np
from random import randint

# matrix representation of the game pay offs table
game_matrix = np.array([
    [-4, 6, -4, 1],
    [5, -7, 3, 8],
    [-8, 0, 6, -2]
])
# player A's strategy matrix
A_matrix = np.array([
    [0.5, 0, .5],
])
# player B's strategy matrix
B_matrix = np.array([
    [0.25],
    [0.25],
    [0.25],
    [0.25],
])

def calculate_payoff(trials=100_000):
    def get_random_A_strategy():
        """
        player A uses strategy i half of the time,
        strategy iii half of the time, and
        strategy ii none of the time
        """

        # i   will correspond to 0
        # iii will correspond to 1
        random_int = randint(0, 1)

        # return the appropriate row index
        # 0 is 0; 1 is 2
        return 0 if random_int == 0 else 2

    def get_random_B_strategy():
        """player B uses each of the four strategies one fourth of the time."""

        # i   will correspond to 0
        # ii  will correspond to 1
        # iii will correspond to 2
        # iv  will correspond to 3
        random_int = randint(0, 3)

        # return the appropriate column index
        return random_int



    expected_payoff = 0

    # average over the number of trials
    for i in range(trials):
        # get the random strategy for each player
        A_strategy = get_random_A_strategy()
        B_strategy = get_random_B_strategy()

        # get the score from the game matrix
        payoff = game_matrix[A_strategy][B_strategy]

        # add trial to total expected payoff
        expected_payoff += payoff

    # divide out by number of trials
    expected_payoff /= trials

    return expected_payoff



if __name__ == '__main__':
    # main driving code

    ### 1a)
    # Experimental calculations for expected pay off

    number_of_trials = 5_000_000 # increase the number of trials to achieve more precision
    expected_payoff = calculate_payoff(number_of_trials)
    print(f"The experimental expected payoff with {number_of_trials} trials is: {expected_payoff}")

    # Theoretical calculations
    # E(A, B) = A_matrix * game_matrix * B_matrix

    # first A_matrix * game_matrix
    A_game_matrix = np.matmul(A_matrix, game_matrix)
    # now take that matrix and multiple by B_matrix
    expected_payoff = np.matmul(A_game_matrix, B_matrix)[0][0]
    print(f"The theoretical expected payoff is {expected_payoff}.")

    ### 1b)

