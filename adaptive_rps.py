import random

hist=[[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

def main():
    last_i=None
    while True:
        m=markov(last_i)
        i=input("your move: ")
        if i=="q":
            break
        print(f"{winning(m, i)} wins")
        if last_i!=None:
            hist[last_i][indx_of(i)]+=1
        last_i=indx_of(i)

def markov(last_i):
    if last_i==None:
        return random.choice(['r', 'p', 's'])
    row=hist[last_i]
    max_val=max(row)#6
    candidates=[]
    for k, v in enumerate(row):
        if v==max_val:
            candidates.append(k)
    predict=random.choice(candidates)
    if predict==0:#rock
        return 'p'
    elif predict==1:#paper
        return 's'
    elif predict==2:#scissors
        return 'r'
    
def indx_of(key):
    move_map = {"r": 0, "p": 1, "s": 2}
    return move_map[key]

def winning(m, i):
    if m==i:
        return 'tie'
    if (m == 'r' and i == 's') or (m == 'p' and i == 'r') or (m == 's' and i == 'p'):
        return m
    else:
        return i

if __name__ == "__main__":
    main()

