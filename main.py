

class Teste(object):

    def __init__(self, animal):
        if animal == "gato":
            self.miar()
        if animal == "cachorro":
            self.latir()



    def miar(self):
        print("miaaau")

    def latir(self):
        print("auau")


def main():
    t = Teste("cachorro")
    

if __name__ == '__main__':
    main()