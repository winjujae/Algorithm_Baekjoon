N = int(input())  # 시험 본 과목의 개수 N을 입력받습니다.
scores = list(map(int, input().split()))  # 세준이의 현재 성적을 입력받아 리스트 scores에 저장합니다.
total = sum(scores)
max_score = max(scores)
new_average = total / N * 100 / max_score
print(new_average)