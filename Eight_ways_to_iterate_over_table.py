DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1,5)

class Table:
    def __init__(self,data):
        self.data = data
    def walk(self,dir0,dir1):
        res = []
        if dir0 == 4 and dir1 == 3: #вправо-вниз
            [res.extend(i) for i in self.data]
        elif dir0 == 3 and dir1 == 4: #вниз-вправо
            for j in range(len(self.data[0])):
                for i in self.data:
                    res.append(i[j])
        elif dir0 == 2 and dir1 == 3: #вліво-вниз
            for i in self.data:
                i.reverse()
                res.extend(i)
                i.reverse()
        elif dir0 == 3 and dir1 == 2: #вниз-вліво
            for j in range(len(self.data[0])):
                for i in self.data:
                    i.reverse()
                    res.append(i[j])
                    i.reverse()
        elif dir0 == 4 and dir1 == 1: #вправо-вверх
            self.data.reverse()
            for i in self.data:
                res.extend(i)
            self.data.reverse()
        elif dir0 == 1 and dir1 == 4: #вверх-вправо
            self.data.reverse()
            for j in range(len(self.data[0])):
                for i in self.data:
                    res.append(i[j])
            self.data.reverse()
        elif dir0 == 2 and dir1 == 1: #вліво-вверх
            self.data.reverse()
            for i in self.data:
                i.reverse()
                res.extend(i)
                i.reverse()
            self.data.reverse()
        elif dir0 == 1 and dir1 == 2: #вверх-вліво
            self.data.reverse()
            for j in range(len(self.data[0])):
                for i in self.data:
                    i.reverse()
                    res.append(i[j])
                    i.reverse()
            self.data.reverse()
        return res
