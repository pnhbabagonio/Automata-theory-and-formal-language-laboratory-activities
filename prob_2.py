def run_dfa(transitions, start, accept, string):
    state = start
    for ch in string:
        if (state, ch) in transitions:
            state = transitions[(state, ch)]
        else:
            return False
    return state in accept

# ---------- Problem 2 ----------
trans2 = {
    ('q0', 'a'): 'q1',
    ('q0', 'b'): 'q2',
    ('q1', 'a'): 'q0',
    ('q1', 'b'): 'q3',
    ('q2', 'a'): 'q3',
    ('q2', 'b'): 'q0',
    ('q3', 'a'): 'q2',
    ('q3', 'b'): 'q1',
}

start2 = 'q0'
accept2 = {'q0', 'q3'}

strings2 = ["", "ab", "bb", "ababb", "abbabbb", "aab"]
print("\nProblem 2 Results:")
for s in strings2:
    print(s, "=>", "ACCEPTED" if run_dfa(trans2, start2, accept2, s) else "REJECTED")

# Problem 2 Results:
#  => ACCEPTED
# ab => ACCEPTED
# bb => ACCEPTED
# ababb => REJECTED
# abbabbb => REJECTED
# aab => REJECTED