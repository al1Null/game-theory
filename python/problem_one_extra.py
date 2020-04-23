import numpy as np
from random import randint

def calculate_experimental_payoff(trials=100_000):
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


def calculate_payoff(A_matrix, game_matrix, B_matrix):
    # payoff = E(A, B) = A_matrix * game_matrix * B_matrix
    # first A_matrix * game_matrix
    A_game_matrix = np.matmul(A_matrix, game_matrix)
    # now take that matrix and multiple by B_matrix
    expected_payoff = np.matmul(A_game_matrix, B_matrix)[0][0]

    return expected_payoff


if __name__ == '__main__':
    # main driving code
    print("1.")

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

    ### 1a)
    print("\ta)")
    ### Theoretical calculation

    # E(A, B) = A_matrix * game_matrix * B_matrix
    expected_payoff = calculate_payoff(A_matrix, game_matrix, B_matrix)
    print(f"\t\tThe theoretical expected payoff is {expected_payoff}.")

    ### Experimental calculation

    # finding the expected payoff
    number_of_trials = 1_000_000 # increase the number of trials to achieve more precision
    print(f"\t\tCalculating experimental payoff... (decrease number of trials if it's taking too long)")
    expected_payoff = calculate_experimental_payoff(number_of_trials)
    print(f"\t\tThe experimental expected payoff with {number_of_trials} trials is: {expected_payoff}.")


    ### 1b)
    print("\tb)")
    # Finding player A's best strategy knowing player B's strategy

    # each pure strategy for player A
    i_strategy   = np.array([
        [1, 0, 0],
    ])
    ii_strategy  = np.array([
        [0, 1, 0],
    ])
    iii_strategy = np.array([
        [0, 0, 1],
    ])

    # calculating the expected payoff for each of the strategies
    i_payoff   = calculate_payoff(i_strategy,   game_matrix, B_matrix)
    ii_payoff  = calculate_payoff(ii_strategy,  game_matrix, B_matrix)
    iii_payoff = calculate_payoff(iii_strategy, game_matrix, B_matrix)

    # maximum payoff for player A
    maximum_payoff = max((i_payoff, ii_payoff, iii_payoff))

    # the optimal strategy is the one with the largest payoff
    optimal_strategy = None
    if maximum_payoff == i_payoff:
        optimal_strategy = i_strategy
    elif maximum_payoff == ii_payoff:
        optimal_strategy = ii_strategy
    elif maximum_payoff == iii_payoff:
        optimal_strategy = iii_strategy

    print(f"\t\t{optimal_strategy[0]} is the most optimal strategy for player A with of a payoff of {maximum_payoff}.")


    ### 1c)
    print("\tc)")
    # Finding player B's best strategy knowing player A's strategy

    # each pure strategy for player B
    i_strategy   = np.array([
        [1],
        [0],
        [0],
        [0],
    ])
    ii_strategy = np.array([
        [0],
        [1],
        [0],
        [0],
    ])
    iii_strategy = np.array([
        [0],
        [0],
        [1],
        [0],
    ])
    iv_strategy = np.array([
        [0],
        [0],
        [0],
        [1],
    ])

    # calculating the expected payoff for each of the strategies
    i_payoff   = calculate_payoff(A_matrix, game_matrix, i_strategy)
    ii_payoff  = calculate_payoff(A_matrix, game_matrix, ii_strategy)
    iii_payoff = calculate_payoff(A_matrix, game_matrix, iii_strategy)
    iv_payoff  = calculate_payoff(A_matrix, game_matrix, iv_strategy)

    # maximum payoff for player B (this more negative the better it is for player B)
    maximum_payoff = min((i_payoff, ii_payoff, iii_payoff, iv_payoff))

    # the optimal strategy is the one with the largest (most negative) payoff
    optimal_strategy = None
    if maximum_payoff == i_payoff:
        optimal_strategy = i_strategy
    elif maximum_payoff == ii_payoff:
        optimal_strategy = ii_strategy
    elif maximum_payoff == iii_payoff:
        optimal_strategy = iii_strategy
    elif maximum_payoff == iv_payoff:
        optimal_strategy = iv_strategy

    print(f"\t\t{i_strategy.transpose()[0]} is the most optimal strategy for player B with of a payoff of {maximum_payoff}.")



