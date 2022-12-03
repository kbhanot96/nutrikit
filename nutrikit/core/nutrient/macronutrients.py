class Macronutrient:
    pass


class Protein(Macronutrient):
    def __init__(self, value):
        self.value = value


class Fat(Macronutrient):
    def __init__(self, value):
        self.value = value


class Carbohydrate(Macronutrient):
    def __init__(self, value):
        self.value = value


class MacronutrientProfile:

    def __init__(self, protein, fat, carbohydrate):

        self.protein = Protein(value=protein)
        self.fat = Fat(value=fat)
        self.carbohydrate = Carbohydrate(value=carbohydrate)
