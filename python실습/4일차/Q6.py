"""
사용자로부터 다음과 같은 숫자를 입력받아 입력받은 숫자의 총합을 구하는 프로그램을 작성하시오.
(단 숫자는 콤마로 구분하여 입력한다.)
65,45,2,3,45,8
"""

str1 = input("숫자를 ,로 구분하여 입력하시오")

# print(type(str1), " :", str1)

s = 0
for n in str1.split(","):
    # print(type(n), ":", n)
    s += int(n)

print("답 :", s)