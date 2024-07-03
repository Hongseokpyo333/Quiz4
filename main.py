import foo import add_func # 푸야.. foo.py파일 만들고, 더하기 기능 완성해줘. 함수는 add_func()로 하고 리턴은 정수, 파라미터는 정수 2개.
import master import sub_func # 마스터야. master.py만들고, 빼기 기능 완성해 줘.

## 변수부
num1,num2,res = 100,200,0
## 메인 코드
res = add_func(num1, num2)
print(res)
res = sub_func(num1, num2)
print(res)