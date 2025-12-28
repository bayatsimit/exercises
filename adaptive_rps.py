import random

hist=[[[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
      [[0, 0, 0], [0, 0, 0], [0, 0, 0]]]

def main():
    last2_i=None
    last_i=None
    total=0
    wins=0
    tie=0
    while True:
        m=markov(last2_i, last_i)
        i=input("your move: ")
        if i=="q":
            break
        total+=1
        print(f"markov's move: {m}")
        winner=winning(m, i)
        if winner=='tie':
            tie+=1
            print('tie')
        else:
            print(f"{winner} won")
        if winner=='you':
            wins+=1
        print(f'{wins} wins, {tie} ties out of {total}')
        if last2_i!=None:
            hist[last2_i][last_i][indx_of(i)]+=1
        last2_i=last_i
        last_i=indx_of(i)

def markov(last2, last):
    if last2==None:
        if last==None:
            return random.choice(['r', 'p', 's'])
        else:
            return counter_move(last)
    row=hist[last2][last]
    max_val=max(row)
    candidates=[]
    for k, v in enumerate(row):
        if v==max_val:
            candidates.append(k)
    predict=random.choice(candidates)
    return counter_move(predict)
    
def indx_of(key):
    move_map = {"r": 0, "p": 1, "s": 2}
    return move_map[key]

def counter_move(i):
    if i==0:#rock
        return 'p'
    elif i==1:#paper
        return 's'
    elif i==2:#scissors
        return 'r'

def winning(m, i):
    if m==i:
        return 'tie'
    if (m == 'r' and i == 's') or (m == 'p' and i == 'r') or (m == 's' and i == 'p'):
        return 'markov'
    else:
        return 'you'

if __name__ == "__main__":
    main()

