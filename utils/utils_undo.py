def update_undo(l, u):
    if(u != l):
        u.append(l[:])


def undol(l, u):
    u.pop()
    l[:] = u[-1]
