import random

class 老查:
    def 唐():
        n = random.randrange(3,10)
        print(n * "阿巴")

    def 回答(ques):
        state1 = "这是一个本体论问题，所以我们无法得出任何答案。"
        state2 = "这个问题的答案不用进行严谨讨论就能得出，所以我们不用讨论它。"
        lst = [state1,state2]
        print(random.choice(lst))

    def 评价(noun):
        print("哈哈，勾-八"+noun+"，芜————")

if __name__ == "__main__":
    老查.唐()
