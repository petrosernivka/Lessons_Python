DIRECTION_UP, DIRECTION_LEFT, DIRECTION_DOWN, DIRECTION_RIGHT = range(1,5)

class Table:
    def __init__(self,data):
        self.data = data
    def walk(self,dir0,dir1):
        
        #вправо-вниз
        if dir0 == 4 and dir1 == 3: #вправо-вниз
            for j in range(len(self.data)):
                for i in range(len(self.data[0])):
                    yield self.data[j][i]
        
        #вниз-вправо
        elif dir0 == 3 and dir1 == 4: 
            for j in range(len(self.data[0])):
                for i in range(len(self.data)):
                    yield self.data[i][j]
        
        #вліво-вниз
        elif dir0 == 2 and dir1 == 3: 
            for j in range(len(self.data)):
                for i in range(len(self.data[0])-1, -1, -1):
                    yield self.data[j][i]
            
        #вниз-вліво
        elif dir0 == 3 and dir1 == 2: 
            for j in range(len(self.data[0])-1, -1, -1):
                for i in range(len(self.data)):
                    yield self.data[i][j]
                    
        #вправо-вверх
        elif dir0 == 4 and dir1 == 1: 
            for j in range(len(self.data)-1, -1, -1):
                for i in range(len(self.data[0])):
                    yield self.data[j][i]
            
        #вверх-вправо    
        elif dir0 == 1 and dir1 == 4: 
            for j in range(len(self.data[0])):
                for i in range(len(self.data)-1, -1, -1):
                    yield self.data[i][j]
                    
        #вліво-вверх            
        elif dir0 == 2 and dir1 == 1: 
            for j in range(len(self.data)-1, -1, -1):
                for i in range(len(self.data[0])-1, -1, -1):
                    yield self.data[j][i]
            
        #вверх-вліво    
        elif dir0 == 1 and dir1 == 2: 
            for j in range(len(self.data[0])-1, -1, -1):
                for i in range(len(self.data)-1, -1, -1):
                    yield self.data[i][j]
