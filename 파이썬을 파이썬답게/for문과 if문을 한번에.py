def solution(mylist):
    answer = [i**2 for i in mylist if i%2==0]
    return answer