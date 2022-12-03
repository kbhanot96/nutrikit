from nutrikit.core.dish.item import ItemList

class Dish:
    pass


class HomemadeDish(Dish):
    def __init__(self):
        self.recipe = Recipe()
        self.ingredients = ItemList()


class MarketDish(Dish):
    pass


class Recipe:
    pass