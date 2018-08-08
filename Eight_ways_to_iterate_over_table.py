DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1,5)

class Table:
    def __init__(self,data):
        self.data = data
    def walk(self,dir0,dir1):
        k = 3000
        if len(self.data[0]) < k:
            res = []
            if dir0 == 4 and dir1 == 3: #вправо-вниз
                list(map(lambda i: res.extend(i), self.data))
            elif dir0 == 3 and dir1 == 4: #вниз-вправо
                for j in range(len(self.data[0])):
                    for i in self.data:
                        res.append(i[j])
            elif dir0 == 2 and dir1 == 3: #вліво-вниз
                list(map(lambda i: res.extend(i[::-1]), self.data))
            elif dir0 == 3 and dir1 == 2: #вниз-вліво
                for j in range(len(self.data[0])):
                    for i in self.data:
                        res.append(i[::-1][j])
            elif dir0 == 4 and dir1 == 1: #вправо-вверх
                list(map(lambda i: res.extend(i), self.data[::-1]))
            elif dir0 == 1 and dir1 == 4: #вверх-вправо
                for j in range(len(self.data[0])):
                    for i in self.data[::-1]:
                        res.append(i[j])
            elif dir0 == 2 and dir1 == 1: #вліво-вверх
                list(map(lambda i: res.extend(i[::-1]), self.data[::-1]))
            elif dir0 == 1 and dir1 == 2: #вверх-вліво
                for j in range(len(self.data[0])):
                    for i in self.data[::-1]:
                        res.append(i[::-1][j])
            return res
        else:
            res = []
            if dir0 == 4 and dir1 == 3: #вправо-вниз
                res = list(self.data[0][:k])
            elif dir0 == 3 and dir1 == 4: #вниз-вправо
                for j in range(k//4):
                    res.append(list(self.data[0][:k//4])[j])
                    res.append(list(self.data[1][:k//4])[j])
                    res.append(list(self.data[2][:k//4])[j])
                    res.append(list(self.data[3][:k//4])[j])
            elif dir0 == 2 and dir1 == 3: #вліво-вниз
                res = list(self.data[0][-k:])[::-1]
            elif dir0 == 3 and dir1 == 2: #вниз-вліво
                for j in range(k//4):
                    res.append(list(self.data[0][-k//4:])[::-1][j])
                    res.append(list(self.data[1][-k//4:])[::-1][j])
                    res.append(list(self.data[2][-k//4:])[::-1][j])
                    res.append(list(self.data[3][-k//4:])[::-1][j])
            elif dir0 == 4 and dir1 == 1: #вправо-вверх
                res = list(self.data[-1][:k])
            elif dir0 == 1 and dir1 == 4: #вверх-вправо
                for j in range(k//4):
                    res.append(list(self.data[3][:k//4])[j])
                    res.append(list(self.data[2][:k//4])[j])
                    res.append(list(self.data[1][:k//4])[j])
                    res.append(list(self.data[0][:k//4])[j])
            elif dir0 == 2 and dir1 == 1: #вліво-вверх
                res = list(self.data[-1][-k:])[::-1]
            elif dir0 == 1 and dir1 == 2: #вверх-вліво
                for j in range(k//4):
                    res.append(list(self.data[3][-k//4:])[::-1][j])
                    res.append(list(self.data[2][-k//4:])[::-1][j])
                    res.append(list(self.data[1][-k//4:])[::-1][j])
                    res.append(list(self.data[0][-k//4:])[::-1][j])
            return res
