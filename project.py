from myparser import MyParser
from word2number import w2n

if __name__ == "__main__":
    parser = MyParser()
    while True:
        try:
            s = input('Input Exp >>>> ')
            op=['+','-','/','*']
            operator=''
            for o in op:
                if o in s:
                    operator=o
                    break
            splitted = s.split(operator)
            exp1=splitted[0].strip()
            exp2=splitted[1].strip()
            try:
                if not exp1.isnumeric():
                    exp1=w2n.word_to_num(exp1)
                if not exp2.isnumeric():
                    exp2=w2n.word_to_num(exp2)
                s=str(exp1)+operator+str(exp2)
            except Exception as e:
                pass
        except EOFError:
            break
        if not s:
            continue
        result = parser.parse(s)

        print(f"Result Is -> {result}\n")
