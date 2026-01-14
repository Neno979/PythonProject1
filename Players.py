class Player():
    def __init__( self, first_name , last_name , height_cm , weight_kg ):
        self.first_name = first_name
        self.last_name = last_name
        self.height_cm = height_cm
        self.weight_kg = weight_kg

    def weight_lbs(self):
        pounds = self.weight_kg * 2.20
        return pounds







class BasketballPlayer(Player):
    def __init__(self, first_name , last_name, height_cm, weight_kg, points, assists, rebounds ):
        super().__init__( first_name, last_name, height_cm, weight_kg )
        self.points = points
        self.assists = assists
        self.rebounds = rebounds

class FootballPlayer(Player):
    def __init__(self, first_name, last_name, height_cm, weight_kg, goals, assists, yellow_cards):
        super().__init__( first_name, last_name, height_cm, weight_kg)
        self.goals = goals
        self.assists = assists
        self.yellow_cards = yellow_cards



Lebron = BasketballPlayer("Lebron" , "James" , 203 , 113 , 30.7 , 9.3 , 6.3 )
Durant = BasketballPlayer("Kevin" , "Durant" , 210 , 100 , 27.2 , 7.1 , 5.1 )

Ronaldo = FootballPlayer( "Cristiano" , "Ronaldo" , 187 , 85 , 25, 6, 7)
Messi = FootballPlayer( "Leo" , "Messi" , 170 , 67 , 25, 6, 7)
print ( Lebron.first_name + " weight in lbs is : " + str(Lebron.weight_lbs()))

print ( Durant.first_name + " weight is " + str(Durant.weight_kg))

print (Messi.first_name + " scored " + str(Messi.goals) + " goals!")

