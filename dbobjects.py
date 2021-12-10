class Product:
    def __init__(self, DATA):
        self.NAME = DATA["NAME"]
        self.AMO = DATA["AMO"]
        self.SELLPRICE = DATA["SELLPRICE"]
        self.MAKEPRICE = DATA["MAKEPRICE"]
        self.DESC = DATA["DESC"]
    
    def export(self):
        return {
            "NAME":self.NAME,
            "AMO":self.AMO,
            "SELLPRICE":self.SELLPRICE,
            "MAKEPRICE":self.MAKEPRICE,
            "DESC":self.DESC
        }

class ProductCategory:
    def __init__(self, NAME, DATA):
        self.NAME = NAME
        self.ITEMS  = []
        for x in DATA:
            self.ITEMS.append(Product(DATA=DATA))
    
    def itemExist(self, NAME):
        for x in self.ITEMS:
            if x.NAME == NAME:
                return True
        return False
    
    def itemIndex(self, NAME):
        if self.itemExist(NAME):
            for count, value in enumerate(self.ITEMS):
                if value.NAME == NAME:
                    return count

    def getItem(self, NAME):
        index = self.itemIndex(NAME)
        if index != None:
            return self.ITEMS[index]
    
    def changeItemAmo(self, NAME):
        

