checklist = list()
# checklist.append("Hello")
print(checklist)
# checklist.append("World")
print(checklist)

def create(item):   checklist.append(item)
def read(index):    return checklist[index]
# checklist = ['Hello', 'World']
# checklist[1] = "Cats"
print(checklist)

def update(index, item):    checklist[index] = item
# checklist = ['Hello', 'World']
# checklist.pop(1)
# print(checklist)

def destroy(index):     checklist.pop(index)

def list_all_items():   index = 0
index = 0
for list_item in checklist:
    # print(str(index) + list_item)
    print("{} {}".format(index, list_item))
index += 1







def test():
    create("purple sox")
create("purple sox")
create("red cloak")
    # Add your testing code here
print(read(0))
print(read(1))
update(0, "purple socks")
destroy(1)
print(read(0))

list_all_items()

test()
