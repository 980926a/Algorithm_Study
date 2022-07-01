# 정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지 이다. 
# 5로 나누어떨어지면 5로 나눈다. 
# 3으로 나눠떨어지면 3으로 나눈다. 2로 하면 2로 나누고 마지막은 1을 뺀ㄷ.

# 최종 1로 만들 때 연산 최솟 값 .

# 나눌 수 있는 경우의 수 를 구하기?
# N/5= 5. N/3=. N/2=13 이것의 크기를 비교하기 제일 작은 5선택?

n = int(input())

d = [0] * 30001

for i in range(2,n+1):
    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1
    # 현재의 수가 2로 나누어 떨아지는 경우
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2]+1)
    # 현재의 수가 3으로 나누어 떨어지는 경우
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3]+1)
    # 현재의 수가 5으로 나누어 떨어지는 경우
    if i % 5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])
    
