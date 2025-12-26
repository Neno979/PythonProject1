class BasketballPlayer:
    def __init__(self, first_name , last_name, height_cm, weight_kg, points, assists, rebounds ):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

Lebron = BasketballPlayer("Lebron" , "James" , 203 , 113, 30.7 , 9.3 , 6.3)

print(Lebron.first_name)