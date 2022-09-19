class FastHash:
    N = 4
    X = 0
    A = 0
    B = 0

    Ac = 1
    Bc = 1
    Ad = 0
    Bd = 0

    table = [[None, None, None] for i in range(100)]

    def __init__(self):

        for i in range(self.N):
            fir_position_of_x = self.first_hash_func(self.X)
            sec_position_of_x = self.second_hash_func(self.X)

            if self.table[fir_position_of_x][sec_position_of_x] == None:
                self.table[fir_position_of_x][sec_position_of_x] = self.X
                self.A = (self.A + self.Ad) % 10**3
                self.B = (self.B + self.Bd) % 10**15
            else:
                self.A = (self.A + self.Ac) % 10**3
                self.B = (self.B + self.Bc) % 10**15

            self.X = (self.X * self.A + self.B) % 10**15

        print(self.X, self.A, self.B)



    def first_hash_func(self, value):
        return value % 36


    def second_hash_func(self, value):
        return value % 50


a = FastHash()
