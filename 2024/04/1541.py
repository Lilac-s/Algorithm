formula = list(input().split('-'))
for i in range(len(formula)):
    new = list(map(int, formula[i].split('+')))
    formula[i] = new
res = 0
for start in formula[0]:
    res += start
for i in range(1, len(formula)):
    summary = 0
    for num in formula[i]:
        if num != '+':
            summary += int(num)
    res -= summary
print(res)