class Birds:
    def __init__(self, name, birdtype):
        self.name = name
        self.birdtype = birdtype

    def info(self):
        print(f'{self.name}은/는 {self.birdtype}')
