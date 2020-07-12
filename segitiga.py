class Segitiga():
    def __init__(self, a, t):
        self.a = a
        self.t = t

    def info(self):
        return f'Ini rumus menghitung luas segitiga dengan Alas = {self.a} dan Tinggi = {self.t}'
    def luas_segitiga(self):
        return self.a * self.t / 2