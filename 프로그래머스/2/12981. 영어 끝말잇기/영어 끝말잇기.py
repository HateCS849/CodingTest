def solution(n, words):
    used = [words[0]]
    
    for i in range(1, len(words)):
        prev_word = words[i-1]
        cur_word = words[i]
        
        #끝말잇기 규칙 틀리거나 or 중복단어
        if prev_word[-1] != cur_word[0] or cur_word in used:
            person = i % n + 1
            turn = i // n + 1
            return [person, turn]
            
        used.append(cur_word)

    return [0, 0]