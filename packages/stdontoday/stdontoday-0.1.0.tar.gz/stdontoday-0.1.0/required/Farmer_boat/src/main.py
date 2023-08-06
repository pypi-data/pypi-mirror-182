def condition(p_w, p_g, p_c,p_f):
    if p_f:
        return p_f
    if p_w and p_g and not p_f:
        return False
    if p_g and p_c and not p_f:
        return False
    else:
        return True


def goat(state):
    return state[1]


def wolf(l):
    return l[0]


def cabbage(l):
    return l[2]


def farmer(l):
    return l[3]


def actions(state):
    if state == goal_state:
        return
    sol = []
    new_state = state[::]
    if farmer(state):
        new_state[3] = False 
        
t = True
f = False
init_state = ([t, t, t, t], [f, f, f, f], [f, f, f, f])
goal_state = ([f, f, f, f], [f, f, f, f], [t, t, t, t])

