N = int(input())
scores = list(map(int, input().split()))
total = sum(scores)
max_score = max(scores)
new_average = total / N * 100 / max_score
print(new_average)