

class unionfind:


    def __init__(self,l):
        self.l = l
        self.sz = [0]*len(l)



    def union_qf(self,c1,c2):

        if not self.find_qf(c1,c2):
            self.l[c2]=self.l[c1]
            self.l = [c1 if x == c2 else x for x in self.l ]
            return True
        else:
            return False


    def find_qf(self,c1,c2):
        if self.l[c1] == self.l[c2]:
            return True
        return False


    def union_qu(self,c1,c2):
        if not self.find_qu(c1,c2):
            self.l[self.find_root(c1)] = self.find_root(c2)

    def find_qu(self,c1,c2):
        if self.find_root(c1) == self.find_root(c2):
            return True
        return False

    def find_root(self,c):
        while c != self.l[c]:
            c = self.l[c]
        return c



    def union_wqu(self,c1,c2):


        pass

    def find_wqu(self,c1,c2):


        pass

    def union_wqupc(self,c1,c2):
        pass

    def find_wqupc(self,c1,c2):
        pass








def getList(n):
    l = []
    for i in range(n):
        l.append(i)
    return l

if __name__=="__main__":
    n = 10


    u1 = unionfind(getList(10))
    u2 = unionfind(getList(5))

    print("u1:",u1.l)
    # u1.union_qf(4,5)
    # u1.union_qf(5,10)

    u1.union_qu(4,3)
    u1.union_qu(3,8)
    u1.union_qu(6,5)
    u1.union_qu(9,4)

    print(u1.find_qu(8,9))
    print(u1.find_qu(5,4))



    print("Result",u1.l)


