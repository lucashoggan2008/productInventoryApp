from json import load, dump
from os import curdir
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
    
    def textExport(self):
        return f' NAME: {self.NAME} | AMO: {self.AMO} | SELLPRICE: {self.SELLPRICE} | MAKEPRICE: {self.MAKEPRICE} \n'
    

class Supply:
    def __init__(self, DATA):
        self.NAME = DATA["NAME"]
        self.AMO = DATA["AMO"]
        self.PRICE = DATA["PRICE"]
        self.DESC = DATA["DESC"]

    def export(self):
        return {
            "NAME":self.NAME,
            "AMO":self.AMO,
            "PRICE":self.PRICE,
            "DESC":self.DESC
        }
    
    def textExport(self):
        return f"NAME: {self.NAME} | AMO: {self.AMO} | PRICE: {self.PRICE} \n"

class SupplyCategory:
    def __init__(self, NAME, DATA):
        self.NAME = NAME
        self.ITEMS = []
        for x in DATA:
            self.ITEMS.append(Supply(DATA=x))

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
    
    def changeItemAmo(self, NAME, MODE, AMO):
        index = self.itemIndex(NAME)
        if index != None:
            if MODE == "+":
                self.ITEMS[index].AMO += AMO
            if MODE == "-":
                self.ITEMS[index].AMO -= AMO
            if MODE == "=":
                self.ITEMS[index].AMO = AMO

    
    def addItem(self, DATA):
        self.ITEMS.append(Supply(DATA))

    def removeItem(self, NAME):
        index = self.itemIndex(NAME)
        if index != None:
            self.ITEMS.pop(index)
    
    def getItemNames(self):
        tempNamesList = []
        for x in self.ITEMS:
            tempNamesList.append(x.NAME)
        return tempNamesList

    def export(self):        
        exportedItems = []
        for x in self.ITEMS:
            exportedItems.append(x.export())
        return {self.NAME:exportedItems}   

    def textExport(self):
        tempText = f"CATEGORY: {self.NAME} \n"
        for x in self.ITEMS:
            tempText += x.textExport()
        tempText += "\n"
        return tempText

class ProductCategory:
    def __init__(self, NAME, DATA):
        self.NAME = NAME
        self.ITEMS  = []
        for x in DATA:
            self.ITEMS.append(Product(DATA=x))
    
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
    
    def changeItemAmo(self, NAME, MODE, AMO):
        index = self.itemIndex(NAME)
        if index != None:
            if MODE == "+":
                self.ITEMS[index].AMO += AMO
            if MODE == "-":
                self.ITEMS[index].AMO -= AMO
            if MODE == "=":
                self.ITEMS[index].AMO = AMO

    def soldItem(self, NAME):
        self.changeItemAmo(NAME, "-", 1)
    
    def addItem(self, DATA):
        self.ITEMS.append(Product(DATA))

    def removeItem(self, NAME):
        index = self.itemIndex(NAME)
        if index != None:
            self.ITEMS.pop(index)
    
    def getItemNames(self):
        tempNamesList = []
        for x in self.ITEMS:
            tempNamesList.append(x.NAME)
        return tempNamesList

    def export(self):
        exportedItems = []
        for x in self.ITEMS:
            exportedItems.append(x.export())
        print(exportedItems)
        return {self.NAME:exportedItems}   

    def textExport(self):
        tempText = f"CATEGORY: {self.NAME} \n"
        for x in self.ITEMS:
            tempText += x.textExport()
        tempText += "\n"
        return tempText

class SupplyDatabseObject:
    def __init__(self):
        self.CATEGORYS = []

    def refresh(self):
        with open("supplies.json", "r") as f:
            CURDATA = load(f)
        CURDATA = [*CURDATA.items()]
        for x in CURDATA:
            self.CATEGORYS.append(SupplyCategory(x[0], x[1]))

    def updateDb(self):
        tempExportedList = {}
        for x in self.CATEGORYS:
            tempExportedList.update(x.export())
        with open("supplies.json", "w") as f:
            dump(tempExportedList, f)
        
        
    def addCategory(self, NAME):
        if not self.categoryExist(NAME):
            self.CATEGORYS.append(SupplyCategory(NAME, {}))

    def categoryExist(self, NAME):
        for x in self.CATEGORYS:
            if x.NAME == NAME:
                return True
        return False
    
    def categoryIndex(self, NAME):
        if self.categoryExist(NAME):
            for count, value in enumerate(self.CATEGORYS):
                if value.NAME == NAME:
                    return count
        return False

    def addSupply(self, supplyData, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            self.CATEGORYS[index].addItem(supplyData)
    
    def deleteCategory(self, name):
        index = self.categoryIndex(name)
        if index != False or index == 0:
            self.CATEGORYS.pop(index)

    def deleteProduct(self, productName, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            self.CATEGORYS[index].removeItem(productName)
    
    def getProductNames(self, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            return self.CATEGORYS[index].getItemNames()
        return False

    def getProduct(self, categoryName, productName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            return self.CATEGORYS[index].getItem(productName)
        return False
    
    def getCategoryNames(self):
        tempNameList = []
        for x in self.CATEGORYS:
            tempNameList.append(x.NAME)
        return tempNameList

    

    def exportText(self):
        tempText = ""
        for x in self.CATEGORYS:
            tempText += x.textExport()
        return tempText

    

class ProductDatabaseObject:
    def __init__(self):
        self.CATEGORYS = []

    def refresh(self):
        with open("products.json", "r") as f:
            CURDATA = load(f)
        CURDATA = [*CURDATA.items()]
        for x in CURDATA:
            self.CATEGORYS.append(ProductCategory(x[0], x[1]))

    def updateDb(self):
        tempExportedList = {}
        for x in self.CATEGORYS:
            tempExportedList.update(x.export())
        with open("products.json", "w") as f:
            dump(tempExportedList, f)
        
        
    def addCategory(self, NAME):
        if not self.categoryExist(NAME):
            self.CATEGORYS.append(ProductCategory(NAME, {}))

    def categoryExist(self, NAME):
        for x in self.CATEGORYS:
            if x.NAME == NAME:
                return True
        return False
    
    def categoryIndex(self, NAME):
        if self.categoryExist(NAME):
            for count, value in enumerate(self.CATEGORYS):
                if value.NAME == NAME:
                    return count
        return False

    def addProduct(self, productData, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            self.CATEGORYS[index].addItem(productData)
    
    def deleteCategory(self, name):
        index = self.categoryIndex(name)
        if index != False:
            self.CATEGORYS.pop(index)

    def deleteProduct(self, productName, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            self.CATEGORYS[index].removeItem(productName)
    
    def getProductNames(self, categoryName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            return self.CATEGORYS[index].getItemNames()
        return False

    def getProduct(self, categoryName, productName):
        index = self.categoryIndex(categoryName)
        if index != False or index == 0:
            return self.CATEGORYS[index].getItem(productName)
        return False
    
    def getCategoryNames(self):
        tempNameList = []
        for x in self.CATEGORYS:
            tempNameList.append(x.NAME)
        return tempNameList

    def exportText(self):
        tempText = ""
        for x in self.CATEGORYS:
            tempText += x.textExport()
        return tempText


        



        
        

        

    
