# I think that [2] corresponds to ε_0 and [3] corresponds to ψ_0(Ω_ω).
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
        if sequence[len(sequence)-1] > 0:
            i = step_down(sequence, sequence[len(sequence)-1], len(sequence)-1)
            if i == None:
                i = len(sequence)-1
            sequence[len(sequence)-1] -= 1
            sequence += sequence[i:] * n
        else:
            sequence.pop()
        return sequence
def repeatedly_expand(sequence, n, limit, printparents=False):
    if printparents:
        print(str(sequence) + str(parents(sequence)))
    else:
        print(sequence)
    while sequence != []:
        expand(sequence, n)
        sequence = sequence[:limit]
        if printparents:
            print(str(sequence) + str(parents(sequence)))
        else:
            print(sequence)
def parents(sequence):
    if sequence == []:
        return []
    else:
        parents = [0]*len(sequence)
        for i in range(1, sequence[len(sequence)-1]+1):
            j = len(sequence)-1
            while j != None:
                parents[j] = i
                j = step_down(sequence, i, j)
        return parents
