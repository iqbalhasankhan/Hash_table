hashTable = [[] for _ in range(10)]  # 2d list/dict 10*10


def hash(name):
    name = ord(name[0])  # ASCII
    return name % len(hashTable) #ASCII 73 % 10= 3


def insert(hashTable, name, type):
    hashkey = hash(name)
    keyIs = False
    bucket = hashTable[hashkey]

    for i, nt in enumerate(bucket):
        n, t = nt
        if name == n:
            keyIs = True
            break

    if keyIs:
        bucket.append((name, type))

    else:
        bucket.append((name, type))


def update(hashTable, name, type):
    hashkey = hash(name)
    keiIs = False
    bucket = hashTable[hashkey]

    for i, nt in enumerate(bucket):
        n, t = nt
        if name == n:
            keiIs = True
            break

    if keiIs:
        bucket[i] = ((name, type))

    else:
        bucket.append((name, type))


def show():
    print(hashTable)


def delete(hashTable, name):
    hashkey = hash(name)
    keiIs = False
    bucket = hashTable[hashkey]

    for i, nt in enumerate(bucket):
        n, t = nt
        if name == n:
            keiIs = True
            break

    if keiIs:
        del bucket[i]

    else:
        print("No Such Name")


def search(hashTable, name):
    hashkey = hash(name)
    keiIs = False
    bucket = hashTable[hashkey]

    for i, nt in enumerate(bucket):
        n, t = nt
        if name == n:
            return n, t


show()  # Show 2


insert(hashTable, "Iqbal", "ID")  # insert 1
show()

print(hash("Iqbal"))  # Hash 6



delete(hashTable, "Iqbal")  # delete 3
show()

choice = int(input())
if choice == 1:
    insert(hashTable, str(input()), str(input()))
elif choice == 2:
    update(hashTable, str(input()), str(input()))
elif choice == 3:
    show()







