mylist = list("abc")
print(mylist[len(mylist)-1])

new_list = mylist[0:2]
print(new_list)

list2 = ['hello']*5
print(list2)

list3 = [i for i in range(0,8,2)]
print(list3)

list4 = [["Frog", "a green animal"], ["Candle", "an object that lights up"]]
print(list4)

for x in list4:
    print(x)

class DictionaryEntry:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

    def __add__(self, rhs):
        return(self.word + str(rhs))
    

list5 = [DictionaryEntry("Frog", "green animal"), DictionaryEntry("Bowl", "Something I eat out of")]

for x in list5:
    print( x.word, x.definition)


foo = 'hello'
bar = DictionaryEntry('frog', 'green animal')
bar2 = DictionaryEntry('toad', 'another green animal')
print(type(list5))
print(type(bar))
print(type(foo))
print(list3.count(2))

#print(bar + bar2)
#bar.__add__(bar2)


#print(bar + 5)
x = 5
print(x.__add__(3))
5 + 3

a = {'frog':[0,2,3,4], 'toad':'another green animal'}
print(a['frog'])



dictionary2 = {'apple':'red thing', 'banana':'yellow thing'}
for i in dictionary2:
    print(i)