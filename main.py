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
window.geometry("200x500")
window.resizable(False, False)

def addProductPopup():
    curPopUp = Tk()
    curPopUp.geometry("250x250")
    curPopUp.title("Add Product")
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
    }, n.get()), productDb.updateDb(), curPopUp.destroy()])
    submitBtn.place(x=10, y=210)


    curPopUp.mainloop()

def addProductCategoryPopup():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.title("App")
    curPopUp.resizable(False, False)

    addCategoryTitle = Label(curPopUp, text="Add Product Category")
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
    curPopUp.geometry("250x200")
    curPopUp.title("Add Supply")
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
    categoryChosenLbl.place(x=10, y=150)
    n = StringVar(curPopUp)
    n.set(" select ")
    
    categoryChosen = OptionMenu(curPopUp, n, *supplyDb.getCategoryNames())
    categoryChosen.place(x=80, y=150)
    

    submitBtn = Button(curPopUp, text="Add Product", width=10, height=1, command=lambda:[makeSupplyRecord(), supplyDb.addSupply({
        "NAME":nameFieldEntry.get(),
        "AMO":int(amoFieldEntry.get()),
        "PRICE":float(PriceFieldEntry.get()),
        "DESC":None
    }, n.get()), supplyDb.updateDb(), curPopUp.destroy()])
    submitBtn.place(x=10, y=210)


    curPopUp.mainloop()

def addSupplyCategory():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.title("App")
    curPopUp.resizable(False, False)

    addCategoryTitle = Label(curPopUp, text="Add Supply Category")
    addCategoryTitle.place(x=10, y=10)

    nameFieldLbl = Label(curPopUp, text="Name:")
    nameFieldLbl.place(x=10, y=60)
    nameFieldEntry = Entry(curPopUp, width=20)
    nameFieldEntry.place(x=60, y=60)

    subminBtn = Button(curPopUp, text="Add Category", height=1, width=20, command=lambda:[makeSupplyRecord(), supplyDb.addCategory(nameFieldEntry.get()), supplyDb.updateDb(), curPopUp.destroy()])
    subminBtn.place(x=10, y=110)
    curPopUp.mainloop()  

def delProductPopup():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.title("App")
    curPopUp.resizable(False, False) 

    delProductTitle = Label(curPopUp, text="Del Product")
    delProductTitle.place(x=10, y=10)

    categoryChosenLbl = Label(curPopUp, text="Product:")
    categoryChosenLbl.place(x=10, y=50)
    n = StringVar(curPopUp)
    n.set(" select ")
    
    categoryChosen = OptionMenu(curPopUp, n, *productDb.getAllProductNames())
    categoryChosen.place(x=70, y=50)

    submitBtn = Button(curPopUp, text="Del Product", command=lambda:[productDb.deleteProduct(n.get().split("|")[0], n.get().split("|")[1]), productDb.updateDb(), makeProductRecord(), curPopUp.destroy()])
    submitBtn.place(x=10, y=90)

    curPopUp.mainloop()

def delSupplyPopup():
    curPopUp = Tk()
    curPopUp.geometry("200x150")
    curPopUp.title("App")
    curPopUp.resizable(False, False) 

    delProductTitle = Label(curPopUp, text="Del Supply")
    delProductTitle.place(x=10, y=10)

    categoryChosenLbl = Label(curPopUp, text="Supply:")
    categoryChosenLbl.place(x=10, y=50)
    n = StringVar(curPopUp)
    n.set(" select ")
    
    categoryChosen = OptionMenu(curPopUp, n, *supplyDb.getAllProductNames())

    submitBtn = Button(curPopUp, text="Del Supply", command=lambda:[supplyDb.deleteSupply(n.get().split("|")[0], n.get().split("|")[1]), supplyDb.updateDb(), makeSupplyRecord(), curPopUp.destroy()])
    submitBtn.place(x=10, y=90)

    categoryChosen.place(x=70, y=50)      

def delProductCategory():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("200x150")
    curPopUp.resizable(False, False)

    delCategoryTitle = Label(curPopUp, text="Delete Product Category")
    delCategoryTitle.place(x=10, y=10)

    categoryChosenLbl = Label(curPopUp, text="Category:")
    categoryChosenLbl.place(x=10, y=50)
    n = StringVar(curPopUp)
    n.set(" select ")
    if productDb.getCategoryNames() != []:
        categoryChosen = OptionMenu(curPopUp, n, *productDb.getCategoryNames())
        categoryChosen.place(x=70, y=45)

        subminBtn = Button(curPopUp, text="Del Product Category", command=lambda:[productDb.deleteCategory(n.get()), productDb.updateDb(), makeProductRecord(), curPopUp.destroy()])
        subminBtn.place(x=10, y=90)

        curPopUp.mainloop()    
    else:
        noneLbl = Label(curPopUp, text="No Categorys")
        noneLbl.place(x=70, y=50)
        curPopUp.mainloop()
        
    

def delSupplyCategory():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("200x150")
    curPopUp.resizable(False, False)

    delCategoryTitle = Label(curPopUp, text="Delete Supply Category")
    delCategoryTitle.place(x=10, y=10)

    categoryChosenLbl = Label(curPopUp, text="Category:")
    categoryChosenLbl.place(x=10, y=50)
    n = StringVar(curPopUp)
    n.set(" select ")
    if productDb.getCategoryNames() != []:
        categoryChosen = OptionMenu(curPopUp, n, *supplyDb.getCategoryNames())
        categoryChosen.place(x=70, y=45)

        subminBtn = Button(curPopUp, text="Del Product Category", command=lambda:[supplyDb.deleteCategory(n.get()), supplyDb.updateDb(), makeSupplyRecord(), curPopUp.destroy()])
        subminBtn.place(x=10, y=90)

    else:
        noneLbl = Label(curPopUp, text="No Categorys")
        noneLbl.place(x=70, y=50)
        curPopUp.mainloop()

    curPopUp.mainloop()

#starting template   
#curPopUp = Tk()
#curPopUp.title()
#curPopUp.geometry("")
#curPopUp.resizable(False, False)
#curPopUp.mainloop()


mainTitleLabel = Label(window, text="Product Inventory App")
mainTitleLabel.place(x=10, y=10)
window.title("App")
BTNWIDTH = 10
BTNHEIGHT= 5

COL1X = 10
COL2X = 110

ROW1Y=100
ROW2Y=200
ROW3Y=300
ROW4Y=400

#column 1

addProductBtn = Button(window, text="Add\nProduct", command=addProductPopup, height=BTNHEIGHT, width=BTNWIDTH)
addProductBtn.place(x=COL1X, y=ROW1Y)

addProductCategoryBtn = Button(window, text="Add\nProduct\nCategory", command=addProductCategoryPopup, height=BTNHEIGHT, width=BTNWIDTH)
addProductCategoryBtn.place(x=COL1X, y=ROW2Y)

delProductBtn = Button(window, text="Delete\nProduct", command=delProductPopup, height=BTNHEIGHT, width=BTNWIDTH)
delProductBtn.place(x=COL1X, y=ROW3Y)

delProductCategoryBtn = Button(window, text="Delete\nProduct\nCategory", height=BTNHEIGHT, width=BTNWIDTH, command=delProductCategory)
delProductCategoryBtn.place(x=COL1X, y=ROW4Y)

#column 2

addSupplybtn = Button(window, text="Add\nSupply", command=addSupplyPopup, height=BTNHEIGHT, width=BTNWIDTH)
addSupplybtn.place(x=COL2X, y=ROW1Y)

addSupplyCategoryBtn = Button(window, text="Add\nSupply\nCategory", command=addSupplyCategory, height=BTNHEIGHT, width=BTNWIDTH)
addSupplyCategoryBtn.place(x=COL2X, y=ROW2Y)

delSupplyBtn = Button(window, text="Delete\nSupply", command=delSupplyPopup, height=BTNHEIGHT, width=BTNWIDTH)
delSupplyBtn.place(x=COL2X, y=ROW3Y)

delSupplyCategoryBtn = Button(window, text="Delete\nSupply\nCategory", height=BTNHEIGHT, width=BTNWIDTH, command=delSupplyCategory)
delSupplyCategoryBtn.place(x=COL2X, y=ROW4Y)


window.mainloop()
