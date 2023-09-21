# 문자열 str이 주어질 때, str을 출력하는 코드를 작성해 보세요.

str = input()
print(str)

# 정수 a와 b가 주어집니다. 각 수를 입력받아 입출력 예와 같은 형식으로 출력하는 코드를 작성해 보세요.

a, b = map(int, input().strip().split(' '))
print("a = %d" %(a))
print("b = %d" %(b))
