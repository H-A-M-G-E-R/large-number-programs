# I think that [0,1,2] corresponds to ε_0, [0,1,2,3] corresponds to ψ_0(Ω_ω), and [0,2] corresponds to lim(BMS). Limit of this notation is [0,ω].
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
    elif sequence[len(sequence)-1] > 0:
        i = step_down(sequence, sequence[len(sequence)-1], len(sequence)-1)
        if i == None:
            i = len(sequence)-1
        else:
            while sequence[i] > sequence[len(sequence)-1]:
                i = step_down(sequence, sequence[len(sequence)-1], i)
                if i == None:
                    i = len(sequence)-1
                    break
        sequence[len(sequence)-1] -= 1
        difference = 0
        j = i-1
        while sequence[j] > sequence[len(sequence)-1]:
            j -= 1
        if sequence[len(sequence)-1] > sequence[j]:
            difference = sequence[len(sequence)-1] - sequence[j]
        bad_part = sequence[i:]
        for j in range(n):
            for k in range(len(bad_part)):
                bad_part[k] += difference
            sequence += bad_part
    else:
        sequence.pop()
    return sequence
def repeatedly_expand(sequence, n, limit):
    print(sequence)
    while sequence != []:
        expand(sequence, n)
        print(sequence)
        sequence = sequence[:limit]
