# work in log space to prevent underflow
import math

def viterbi(sequence, iprobs, tprobs, eprobs):

    states = ["C", "N"]

    # Viterbi table - highest odds of ending up at certain state
    vtable = []

    # Backpointers - most likely path to each state
    backpointers = []

    # --------------------------------
    # FIRST NUCLEOTIDE
    # --------------------------------

    first_nucleotide = sequence[0]

    first_probs = {}
    # backpointers will both be blank, but storing in variable means it's programatically generated -> no chance of error
    first_backpointers = {}

    for state in states:
        first_probs[state] = math.log(iprobs[state]) * math.log(eprobs[state][first_nucleotide])
        first_backpointers[state] = None

    vtable.append(first_probs)
    backpointers.append(first_backpointers)

    # --------------------------------
    # SUBSEQUENT NUCLEOTIDES
    # --------------------------------

    for nucleotide in sequence[1:]:

        # init here so new probs/backpointers for each nucleotide, but constant WITHIN each nucleotide ready for appending
        current_probs = {}
        current_backpointers = {}

        for current_state in states:
            
            # init here so that they aren't reset with each loop through PREVIOUS states, but are reset before considering new CURRENT state
            best_prob = 0
            best_prev_state = None

            for prev_state in states:

                prob = vtable[-1][prev_state] * math.log(tprobs[prev_state][current_state]) * math.log(eprobs[current_state][nucleotide])

                if prob > best_prob:
                    best_prob = prob
                    best_prev_state = prev_state

            current_probs[current_state] = best_prob
            current_backpointers[current_state] = best_prev_state

        vtable.append(current_probs)
        backpointers.append(current_backpointers)

    # --------------------------------
    # BEST FINAL STATE
    # --------------------------------

    final_probs = vtable[-1]

    best_final_state = max(states, key=lambda state: final_probs[state])

    # --------------------------------
    # TRACEBACK
    # --------------------------------

    path = [best_final_state]

    for position in range(len(sequence) - 1, 0, -1):
        prev_state = backpointers[position][path[-1]]
        path.append(prev_state)

    path.reverse()

    return "".join(path)
