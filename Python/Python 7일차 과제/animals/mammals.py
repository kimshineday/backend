class Dogs:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def info(self):
        print(f'{self.name}은/는 {self.breed}')
