def solution(n):
    answer = 0
    for i in range(1, n+1):
        sum = 0
        j = i
        while sum < n:
            sum += j
            if sum == n:
                answer += 1
                break
            j += 1
            
        
    return answer