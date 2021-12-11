from os import curdir
from dbobjects import ProductDatabaseObject, SupplyDatabseObject
from tkinter import *
from tkinter import ttk
from datetime import datetime

productDb = ProductDatabaseObject()
supplyDb = SupplyDatabseObject()

productDb.refresh()
supplyDb.refresh()

window = Tk()
window.geometry("400x400")
window.resizable(False, False)

def addProductPopup():
    curPopUp = Tk()
    curPopUp.geometry("250x350")
    curPopUp.resizable(False, False)

    addProductTitle = Label(curPopUp, text="Add Product")
    addProductTitle.place(x=10, y=10)

    nameFieldLbl = Label(curPopUp, text="Name:")
    nameFieldLbl.place(x=10, y=60)
    nameFieldEntry = Entry(curPopUp, width=20)
    nameFieldEntry.place(x=80, y=60)

    amoFieldLbl = Label(curPopUp, text="Amo:")
    amoFieldLbl.place(x=10, y=90)
    amoFieldEntry = Entry(curPopUp, width=5)
    amoFieldEntry.place(x=80, y=90)

    sellPriceFieldLbl = Label(curPopUp, text="Sell price:")
    sellPriceFieldLbl.place(x=10, y=120)
    sellPriceFieldEntry = Entry(curPopUp, width=5)
    sellPriceFieldEntry.place(x=80, y=120)

    makePriceFieldLbl = Label(curPopUp, text="Make price:")
    makePriceFieldLbl.place(x=10, y=150)
    makePriceFieldEntry = Entry(curPopUp, width=5)
    makePriceFieldEntry.place(x=80, y=150)

    categoryChosenLbl = Label(curPopUp, text="Category:")
    categoryChosenLbl.place(x=10, y=180)
    n = StringVar(curPopUp)
    n.set(" select ")
    
    categoryChosen = OptionMenu(curPopUp, n, *productDb.getCategoryNames())
    categoryChosen.place(x=80, y=180)
    

    submitBtn = Button(curPopUp, text="Add Product", width=10, height=1, command=lambda:[makeProductRecord, productDb.addProduct({
        "NAME":nameFieldEntry.get(),
        "AMO":int(amoFieldEntry.get()),
        "SELLPRICE":float(sellPriceFieldEntry.get()),
        "MAKEPRICE":float(makePriceFieldEntry.get()),
        "DESC":None
    }, n.get()), productDb.updateDb(), print(n.get()), curPopUp.destroy()])
    submitBtn.place(x=10, y=210)


    curPopUp.mainloop()

def addProductCategoryPopup():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.resizable(False, False)

    addCategoryTitle = Label(curPopUp, text="Add Category")
    addCategoryTitle.place(x=10, y=10)

    nameFieldLbl = Label(curPopUp, text="Name:")
    nameFieldLbl.place(x=10, y=60)
    nameFieldEntry = Entry(curPopUp, width=20)
    nameFieldEntry.place(x=60, y=60)

    subminBtn = Button(curPopUp, text="Add Category", height=1, width=20, command=lambda:[makeProductRecord(), productDb.addCategory(nameFieldEntry.get()), productDb.updateDb(), curPopUp.destroy()])
    subminBtn.place(x=10, y=110)
    curPopUp.mainloop()

def makeProductRecord():
    textData = productDb.exportText()
    with open("productInventory.txt", "w") as f:
        f.write(textData)

def makeSupplyRecord():
    textData = supplyDb.exportText()
    with open("supplyInventory.txt", "w") as f:
        f.write(textData)

def addSupplyPopup():
    curPopUp = Tk()
    curPopUp.geometry("250x350")
    curPopUp.resizable(False, False)

    addProductTitle = Label(curPopUp, text="Add Supply")
    addProductTitle.place(x=10, y=10)

    nameFieldLbl = Label(curPopUp, text="Name:")
    nameFieldLbl.place(x=10, y=60)
    nameFieldEntry = Entry(curPopUp, width=20)
    nameFieldEntry.place(x=80, y=60)

    amoFieldLbl = Label(curPopUp, text="Amo:")
    amoFieldLbl.place(x=10, y=90)
    amoFieldEntry = Entry(curPopUp, width=5)
    amoFieldEntry.place(x=80, y=90)

    PriceFieldLbl = Label(curPopUp, text="Price:")
    PriceFieldLbl.place(x=10, y=120)
    PriceFieldEntry = Entry(curPopUp, width=5)
    PriceFieldEntry.place(x=80, y=120)


    categoryChosenLbl = Label(curPopUp, text="Category:")
    categoryChosenLbl.place(x=10, y=180)
    n = StringVar(curPopUp)
    n.set(" select ")
    
    categoryChosen = OptionMenu(curPopUp, n, *supplyDb.getCategoryNames())
    categoryChosen.place(x=80, y=180)
    

    submitBtn = Button(curPopUp, text="Add Product", width=10, height=1, command=lambda:[makeSupplyRecord(), supplyDb.addSupply({
        "NAME":nameFieldEntry.get(),
        "AMO":int(amoFieldEntry.get()),
        "PRICE":float(PriceFieldEntry.get()),
        "DESC":None
    }, n.get()), supplyDb.updateDb(), print(n.get()), curPopUp.destroy()])
    submitBtn.place(x=10, y=210)


    curPopUp.mainloop()

def addSupplyCategory():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.resizable(False, False)

    addCategoryTitle = Label(curPopUp, text="Add Category")
    addCategoryTitle.place(x=10, y=10)

    nameFieldLbl = Label(curPopUp, text="Name:")
    nameFieldLbl.place(x=10, y=60)
    nameFieldEntry = Entry(curPopUp, width=20)
    nameFieldEntry.place(x=60, y=60)

    subminBtn = Button(curPopUp, text="Add Category", height=1, width=20, command=lambda:[makeSupplyRecord(), supplyDb.addCategory(nameFieldEntry.get()), supplyDb.updateDb(), curPopUp.destroy()])
    subminBtn.place(x=10, y=110)
    curPopUp.mainloop()  

    

    



mainTitleLabel = Label(window, text="Product Inventory App")
mainTitleLabel.place(x=10, y=10)

addProductBtn = Button(window, text="Add\nProduct", command=addProductPopup)
addProductBtn.place(x=10, y=100)

addProductCategoryBtn = Button(window, text="Add\nProduct\nCategory", command=addProductCategoryPopup)
addProductCategoryBtn.place(x=10, y=190)




addSupplybtn = Button(window, text="Add\nSupply", command=addSupplyPopup)
addSupplybtn.place(x=110, y=100)

addSupplyCategoryBtn = Button(window, text="Add\nSupply\nCategory", command=addSupplyCategory)
addSupplyCategoryBtn.place(x=110, y=190)


window.mainloop()
