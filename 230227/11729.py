N = int(input())

def hanoi(N, From, To):
    if N > 1:
        hanoi(N-1, From, 6-From-To)
    
    print(From, To)
    
    if N > 1:
        hanoi(N-1, 6-From-To, To)
        
print(2**N - 1)
hanoi(N,1,3)