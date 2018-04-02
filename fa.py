import goody


def read_fa(file : open) -> {str:{str:str}}:
    d={}
    for line in file:
        r=line.strip('\n').split(';')
        d.update({r[0]:{r[num]:r[num+1] for num in range(len(r[1:])) if num%2==1}})
    return d

def fa_as_str(fa : {str:{str:str}}) -> str:
    return ''.join(sorted(['  '+item+' transitions: '+str(sorted([(item2,fa[item][item2]) for item2 in fa[item].keys()]))+'\n' for item in fa.keys()]))

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    l=[state]
    current_state=state
    for item in inputs:
        try:
            current_state=fa[current_state][item]
            l.append((item,current_state))
        except KeyError:
            l.append((item,None))
            break
    return l

def interpret(fa_result : [None]) -> str:
    s= 'Start state = '+fa_result[0]+'\n'+''.join(['  Input = '+item[0]+'; new state = '+item[1]+'\n' for item in fa_result[1:] if item[1]!=None])
    if fa_result[-1][1]==None:
        s+='  Input = '+fa_result[-1][0]+';'+' illegal input: simulation terminated\nStop state = None\n'
    else:
        s+='Stop state = '+fa_result[-1][1]+'\n'
    return s



if __name__ == '__main__':
    # Write script here
    file=input('Enter the name of any file with a finite automaton: ')
    d1=read_fa(open(file))
    print()
    print("Finite Automaton's Description")
    print(fa_as_str(d1))
    print()
    d2=input('Enter the name of any file with the start-state and inputs: ')
    for line in open(d2):
        print()
        print('Starting new simulation')
        temp=line.strip('\n').split(';')
        print(interpret(process(d1, temp[0], temp[1:])))          
    # For running batch self-tests
    print()
    #import driver
