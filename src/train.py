states = ["C", "N"]
nucleotides = ["A", "T", "G", "C"]


# emission
def est_emission(nucleotides, annotations):

    emission_counts = {
        "C": {"A": 0, "T": 0, "G": 0, "C": 0},
        "N": {"A": 0, "T": 0, "G": 0, "C": 0}
    }

    for nucleotide, state in zip(nucleotides, annotations):
        emission_counts[state][nucleotide] += 1

    emission_probs = {
        # inner dicts programatically generated; whereas for counts, increment operator wouldn't work
        "C": {},
        "N": {}
    }
    
    for state in states:
        total = sum(emission_counts[state].values())

        for nucleotide in nucleotides:
            emission_probs[state][nucleotide] = emission_counts[state][nucleotide] / total

    return emission_probs


# transition
def est_transition(annotations):
    
    transition_counts = {
        "C": {"C": 0, "N": 0},
        "N": {"C": 0, "N": 0}
    }

    for i in range(len(annotations) - 1):
        transition_counts[annotations[i]][annotations[i + 1]] += 1

    transition_probs = {
        "C": {},
        "N": {}
    }

    for state1 in states:
        total = sum(transition_counts[state1].values())
        for state2 in states:
            transition_probs[state1][state2] = transition_counts[state1][state2] / total

    return transition_probs
