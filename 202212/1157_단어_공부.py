word = list(input())
wordDict = {}
for i in range(len(word)):
    largeWord = word[i].upper()
    # if largeWord in list(wordDict.keys()):
    #     break
    if largeWord not in list(wordDict.keys()):
        smallWord = word[i].lower()
        cnt = 0
        cnt += word.count(largeWord)
        cnt += word.count(smallWord)
        wordDict[largeWord] = cnt

maxnum = max(list(wordDict.values()))
if list(wordDict.values()).count(maxnum) > 1:
    print('?')
else:
    print(max(wordDict, key=wordDict.get))
