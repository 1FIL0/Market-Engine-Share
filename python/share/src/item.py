class MarketItem:
    def __init__(self):
        self.tempID: int = -1
        self.permID: int = -1
        self.weaponName: str = ""
        self.skinName: str = ""
        self.fullName: str = ""
        self.grade: int = -1
        self.category: int = -1
        self.wear: int = -1
        self.useModifiedState: bool = False # FIELD IS SET MANUALLY BASED ON modified_items.json
        self.price: float = -1.0 # FIELD IS SET MANUALLY BASED ON modified_items.json
        self.priceSteamTax: float = -1.0 # FIELD IS BASED ON PRICE
        self.modifiedPrice: float = 0.0 # FIELD IS SET MANUALLY BASED ON modified_items.json
        self.marketPrice: float = -1.0
        self.tradeupable: bool = False
        self.collection: int = -1
        self.minFloat: float = -1.0
        self.maxFloat: float = -1.0
        self.imageUrl: str = ""
        self.imageName: str = ""
        self.steamMarketUrl: str = ""

