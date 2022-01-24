def make_dolcelatte():
    print("1. 얼음을 넣는다.")
    print("2. 연유를 30ml를 넣는다.")
    print("3. 찬 우유를 넣는다.")
    print("4. 에스프레소샷을 넣는다.")

def make_blueberry_smoothie():
    print("1. 블루베리 20g을 넣는다.")
    print("2. 우유 300ml를 넣는다.")
    print("3. 얼음을 넣는다.")
    print("4. 믹서기에 간다.")
    
def make_simple_latte():
    print("1. 커피를 넣는다.")
    print("2. 우유를 넣는다.")
    print("3. 신나게 섞는다.")

total_dictionary = {}

while True:
    question = input("질문을 입력해주세요 : ")
    if (question == "q"):
        break
    else:
        total_dictionary[question] = ""

for i in total_dictionary:
    print(i)
    answer = input("답변을 입력해주세요 : ")
    total_dictionary[i] = answer
    
print(total_dictionary)
