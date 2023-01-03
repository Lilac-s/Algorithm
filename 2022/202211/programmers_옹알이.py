def solution(babbling):
    babble = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for text in babbling:
        for bab in babble:
            text = text.replace(bab, "0")
        text = text.replace("0", "")
        if len(text) == 0:
            cnt += 1
        
    answer = cnt
    return answer