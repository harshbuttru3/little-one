import random

class Baby:
    def __init__(self, Dhruvi, Harsh):
        self.name = self.generate_name()
        self.traits = self.inherit_traits(Dhruvi, Harsh)
    
    def generate_name(self):
        # Randomly choose a name to make it fun!
        names = ["Dharsh", "Darshvi", "Little One", "Tiny Tot"]
        return random.choice(names)
    
    def inherit_traits(self, Dhruvi, Harsh):
        # Mix and match traits from Mom and Dad
        combined_traits = {}
        for trait in set(Dhruvi.keys()).union(Harsh.keys()):
            combined_traits[trait] = random.choice(
                [Dhruvi.get(trait, "Unknown"), Harsh.get(trait, "Unknown")]
            )
        return combined_traits
    
    def show_traits(self):
        print(f"Meet {self.name}!")
        print("Here are the inherited traits:")
        for trait, value in self.traits.items():
            print(f"{trait}: {value}")

# Define Dhruvi (Mom) and Harsh (Dad) traits
Dhruvi = {
    "hair_color": "brown",
    "eye_color": "black",
    "height": "average",
    "intelligence": "high",
}

Harsh = {
    "hair_color": "brown",
    "eye_color": "black",
    "height": "tall",
    "intelligence": "average",
}

# "Creating" a baby
baby = Baby(Dhruvi, Harsh)
baby.show_traits()
