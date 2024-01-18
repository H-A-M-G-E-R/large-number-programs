# I think that [1,1,1...] corresponds to ε_0 and [2,2,2...] corresponds to ψ_0(Ω_ω).
def step_down(sequence, Type, index):
    if index == 0:
        return
    else:
        if Type == 0:
            return index-1
        else:
            i = index
            level = 0
            while level != -1:
                i = step_down(sequence, Type-1, i)
                if i == None:
                    return
                if sequence[i] < Type:
                    level += 1
                else:
                    level -= 1
            return i
def expand(sequence, n):
    if sequence == []:
        return []
    else:
        for m in range(sequence[len(sequence)-1],0,-1):
            i = step_down(sequence, m, len(sequence)-1)
            if i != None:
                sequence[len(sequence)-1] = m-1
                sequence += sequence[i:] * n
                return sequence
        sequence.pop()
        return sequence
