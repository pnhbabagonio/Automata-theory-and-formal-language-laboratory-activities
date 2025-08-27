def run_dfa(trans, start, accept, data):
    state = start
    for ch in data:
        if (state, ch) in trans:
            state = trans[(state, ch)]
        else:
            return False
    return state in accept

# ---------- Problem #1 ----------
trans1 = {
    ('a', '0'): 'a',
    ('a', '1'): 'b',
    ('b', '0'): '1',
    ('b', '1'): 'a',
    ('1', '1'): '1'
}

start1 = 'a'
accept1 = {'1'}
strings1 = ["1110", "10", "11010", "1001", "0", "11"]
print("\nProblem 1 Results:")
for s in strings1:
    print(s, "=>", "ACCEPTED" if run_dfa(trans1, start1, accept1, s) else "REJECTED")


# Problem 1 Results:
# 1110 => ACCEPTED
# 10 => ACCEPTED
# 11010 => ACCEPTED
# 1001 => REJECTED
# 0 => REJECTED
# 11 => REJECTED