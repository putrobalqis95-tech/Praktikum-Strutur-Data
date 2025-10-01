class Stack:
    def _init_(self):
        self._data = list()

    def isEmpty(self):
        return len(self) == 0

    def _len_(self):
        return len(self._data)

    def peek(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data top.')
        else:
            return self._data[-1]

    def pop(self):
        if self.isEmpty():
            raise Exception('Stack kosong. Tidak ada data yang dapat di-pop.')
        else:
            return self._data.pop()

    def push(self, data):
        self._data.append(data)

    def printData(self):
        for item in self._data:
            print(item)

    def deleteAll(self):   # perbaikan indentasi di sini
        self._data.clear()

myStack = Stack()
myStack.push(10)
myStack.push(21)
myStack.push(32)

print(f'Total Data = {myStack._len_()}')
print(f'Elemen TOP = {myStack.peek()}')

print()
print('Data dalam Stack: ')
myStack.printData()

print()
print('Hapus Data')
myStack.pop()
print('Data dalam Stack: ')
myStack.printData()

print()
print('Hapus Seluruh Data')
myStack.deleteAll()
if myStack.isEmpty():
    print('Stack Kosong')
else:
    print('Data dalam Stack: ')
    myStack.printData()