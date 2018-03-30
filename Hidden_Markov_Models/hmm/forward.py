#!/usr/bin/env python3


#9.1 Implement the Forward algorithm and run it with the HMM in Fig. 9.3 to compute
#the probability of the observation sequences 331122313 and 331123312.
#Which is more likely?
#to compute the probability of the observation sequences 331122313 and 331123312

#According to Figure 9.3
# A hidden Markov model for relating numbers of ice creams eaten by Jason (the
#observations) to the weather (H or C, the hidden variables).
states = ["hot", "cold"]
transition_matrix = {"hot": {"cold": 0.4, "hot": 0.6}, "cold": {"hot": 0.4, "cold": 0.5}}
pi = {"start": {"hot": 0.8, "cold": 0.2}, "end": {"hot": 0.1, "cold": 0.1}}
emitting = {"hot": {1: 0.2, 2: 0.4, 3: 0.4}, "cold": {1: 0.5, 2: 0.4, 3: 0.1}}

observations0 = [int(x) for x in "313"]
observations1 = [int(x) for x in "331122313"]
observations2 = [int(x) for x in "331123312"]

def forward(cur_obs):
    T = len(cur_obs)

    N = len(states)

    #Create a probability matrix forward[N+2,T]
    state = [{} for _ in range(0,T)]

    #Init
    for y in states:
        state[0][y] = pi["start"][y] * emitting[y][cur_obs[0]]

    #Recursion step
    for t in range(1, T):
        for y in states:
            state[t][y] = sum(state[t-1][y] * transition_matrix[y_prev][y] * emitting[y][cur_obs[t]] for y_prev in states)

    #Termination step

    prob = sum(state[T-1][y] for y in states)
    return prob

print(forward(observations1))
print(forward(observations2))
