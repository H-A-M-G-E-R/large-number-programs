# I think that [0,1,2] corresponds to ε_0 and [0,1,2,3] corresponds to ψ_0(Ω_ω). Limit of this notation is [0,ω].
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
        last_entry = sequence[len(sequence)-1]
        if last_entry > 0:
            i = step_down(sequence, last_entry, len(sequence)-1)
            if i == None:
                i = len(sequence)-1
            while sequence[i] >= last_entry:
                i -= 1
            sequence.pop()
            bad_part = sequence[i:]
            for j in range(n):
                for k in range(len(bad_part)):
                    bad_part[k] += last_entry - sequence[i] - 1
                sequence += bad_part
        else:
            sequence.pop()
        return sequence
def repeatedly_expand(sequence, n, limit):
    print(sequence)
    while sequence != []:
        expand(sequence, n)
        sequence = sequence[:limit]
        print(sequence)
