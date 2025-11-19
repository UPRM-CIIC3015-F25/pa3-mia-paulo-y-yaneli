class PlanetCard:
    def __init__(self, name, description, price=6, chips=0, mult=0, image=None, isActive=False):
        self.name = name
        self.description = description
        self.price = price
        self.chips = chips
        self.mult = mult
        self.image = image
        self.isActive = isActive

    def __str__(self):
        return f"{self.name}: {self.description}"

    def sellPrice(self):
        return int(self.price * 0.6)

# TODO (TASK 6.1): Implement the Planet Card system for Balatro.
#   Create a dictionary called PLANETS that stores all available PlanetCard objects.
#   Each entry should use the planet's name as the key and a PlanetCard instance as the value.
#   Each PlanetCard must include:
#       - name: the planet's name (e.g., "Mars")
#       - description: the hand it levels up or affects
#       - price: how much it costs to purchase
#       - chips: the chip bonus it provides
#       - mult: the multiplier it applies
#   Example structure:
#       "Gusty Garden": PlanetCard("Gusty Garden", "levels up galaxy", 6, 15, 7)
#   Include all planets up to "Sun" to complete the set.
#   These cards will be used in the shop and gameplay systems to upgrade specific poker hands.

PLANETS = {
    "Mercury": PlanetCard(
        name="Mercury",
        description="levels up High Card",
        price=2,
        chips=10,
        mult=1
    ),
    "Venus": PlanetCard(
        name="Venus",
        description="levels up One Pair",
        price=2,
        chips=15,
        mult=1
    ),
    "Earth": PlanetCard(
        name="Earth",
        description="levels up Two Pair",
        price=2,
        chips=15,
        mult=2
    ),
    "Mars": PlanetCard(
        name="Mars",
        description="levels up Three of a Kind",
        price=2,
        chips=25,
        mult=2
    ),
    "Jupiter": PlanetCard(
        name="Jupiter",
        description="levels up Straight",
        price=3,
        chips=25,
        mult=3
    ),
    "Saturn": PlanetCard(
        name="Saturn",
        description="levels up Flush",
        price=3,
        chips=30,
        mult=3
    ),
    "Uranus": PlanetCard(
        name="Uranus",
        description="levels up Full House",
        price=3,
        chips=35,
        mult=3
    ),
    "Neptune": PlanetCard(
        name="Neptune",
        description="levels up Four of a Kind",
        price=3,
        chips=40,
        mult=4
    ),
    "Sun": PlanetCard(
        name="Sun",
        description="levels up all hands",
        price=12,
        chips=30,
        mult=2
    )


}
