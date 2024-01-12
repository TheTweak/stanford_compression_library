import numpy as np
from scl.core.data_block import DataBlock

def biased_coin_generator():
    """
    the function returns H with probability prob_H, and T with prob_T
    """
    # NOTE: hard-coding prob_H to 0.8
    prob_H = 0.8
    prob_T = 1 - prob_H
    # generate random coin toss
    rng = np.random.default_rng()
    toss = rng.choice(["H", "T"], p=[prob_H, prob_T])
    return toss


def shubhams_fair_coin_generator():
    """
    TODO:
    use the biased_coin_generator() function above to implement the fair coin generator

    Outputs:
        toss (str): H, T
        num_biased_tosses (int): number of times the biased_coin_generator() was called to generate the output
    """
    toss = None
    num_biased_tosses = 0
    while True:
        t1 = biased_coin_generator()
        t2 = biased_coin_generator()

        num_biased_tosses += 2

        if t1 == t2:
            continue

        if t1 == 'H':
            toss = 'H'
        else:
            toss = 'T'

        break

    return toss, num_biased_tosses


def shubhams_fair_coin_generator_v2():
    toss = None
    num_biased_tosses = 0
    tl = [biased_coin_generator()]
    while True:
        tl.append(biased_coin_generator())

        t1, t2 = tl[-2], tl[-1]

        if t1 == t2:
            continue

        if t1 == 'H':
            toss = 'H'
        else:
            toss = 'T'

        break

    return toss, num_biased_tosses


def test_shubhams_fair_coin_generator():
    """
    TODO:
    write a test to check whether the shubhams_fair_coin_generator() is really generating fair coin tosses

    Also, check if the num_biased_tosses matches the answer which you computed in part 2.
    """

    # perform the experiment
    # feel free to reduce this when you are testing
    num_trials = 10000
    tosses = []
    num_biased_tosses_list = []
    for _ in range(num_trials):
        # toss, num_biased_tosses = shubhams_fair_coin_generator()
        toss, num_biased_tosses = shubhams_fair_coin_generator_v2()

        # check if the output is indeed in H,T
        assert toss in ["H", "T"]
        tosses.append(toss)
        num_biased_tosses_list.append(num_biased_tosses)

    # NOTE: We are using the DataBlock object from SCL.
    # Take a look at `scl/core/data_block.py` to understand more about the class
    # the get_empirical_distribution() outputs a ProbDist class. Take a look at
    # `scl/core/prob_dist.py` to understand this object better
    tosses_db = DataBlock(tosses)
    empirical_dist_tosses = tosses_db.get_empirical_distribution()

    np.testing.assert_almost_equal(empirical_dist_tosses.probability('H'), 0.5, decimal=1)
    np.testing.assert_almost_equal(empirical_dist_tosses.probability('T'), 0.5, decimal=1)
    print(f'num biased tosses: {np.average(num_biased_tosses_list)}')
