# def gen(n):
#     for i in range (n):
#         yield i
#         gen(i)


# for i in gen(10):
#     print(i)
a=iter("123")

while True:
    try:
        print(next(a))
    except StopIteration:
        break

print("*******")
def my_(start,end):
    curretnt=start
    while curretnt<end:
        yield curretnt
        curretnt+=1
x=my_(1,101)
for i in x:
    print(i)


print("######")
class Sentence:
    def __init__(self,sentence):
        self.sentence=sentence
        self.list=self.sentence.split()
        self.index=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.list):
            raise StopIteration
        index=self.index
        self.index+=1
        return self.sentence[index]


y_sentence=Sentence("This is a sentence")
for i in y_sentence:
    print(i)


#Generator

print("#**********************#")
def sentence(Sentence):
    for i in Sentence.split():
        yield i


y_sentence=sentence("This is a sentence")
print(type(y_sentence))
for i in y_sentence:
    print(i)
