import matplotlib.pyplot as plt

Bowler_Height = [160,165,166,168,169,170,174,175,176,177,180,182,183,185,190]
Bowler_Speed = [80,85,90,95,100,105,110,115,120,125,130,135,140,145,150,155]

plt.xlabel("Bowler Height in cm")
plt.ylabel("Bowler Speed in km/hr")

plt.scatter(Bowler_Height, Bowler_Speed)
plt.show()
