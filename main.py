from os import curdir
from dbobjects import ProductDatabaseObject, SupplyDatabseObject
from tkinter import *
from tkinter import ttk
import json

productDb = ProductDatabaseObject()
supplyDb = SupplyDatabseObject()

productDb.refresh()
supplyDb.refresh()



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
    

    submitBtn = Button(curPopUp, text="Add Product", width=10, height=1, command=lambda:[productDb.addProduct({
        "NAME":nameFieldEntry.get(),
        "AMO":int(amoFieldEntry.get()),
        "SELLPRICE":float(sellPriceFieldEntry.get()),
        "MAKEPRICE":float(makePriceFieldEntry.get()),
        "DESC":None
    }, n.get()), productDb.updateDb(), makeProductRecord(),  curPopUp.destroy()])
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

    subminBtn = Button(curPopUp, text="Add Category", height=1, width=20, command=lambda:[productDb.addCategory(nameFieldEntry.get()), productDb.updateDb(), makeProductRecord(), curPopUp.destroy()])
    subminBtn.place(x=10, y=110)
    curPopUp.mainloop()

def makeProductRecord():
    with open("products.json", "r") as f:
        jsonData = json.load(f)
    categorys = [*jsonData.items()]
    textData = ""
    for x in categorys:
        tempText = f"CATEGORY: {x[0]}\n"
        for y in x[1]:
            tempText += f' NAME: {y["NAME"]} | AMO: {y["AMO"]} | SELLPRICE: {y["SELLPRICE"]} | MAKEPRICE: {y["MAKEPRICE"]}\n'
        textData += tempText + "\n"
    with open("productInventory.txt", "w") as f:
        f.write(textData)

def makeSupplyRecord():
    with open("supplies.json", "r") as f:
        jsonData = json.load(f)
    categorys = [*jsonData.items()]
    textData = ""
    for x in categorys:
        tempText = f"CATEGORY: {x[0]}\n"
        for y in x[1]:
            tempText += f' NAME: {y["NAME"]} | AMO: {y["AMO"]} | PRICE: {y["PRICE"]}\n'
        textData += tempText + "\n"
    print(textData)
    with open("supplyInventory.txt", "w") as f:
        f.write(textData)

def addSupplyPopup():
    curPopUp = Tk()
    curPopUp.geometry("250x250")
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
    

    submitBtn = Button(curPopUp, text="Add Supply", width=10, height=1, command=lambda:[supplyDb.addSupply({
        "NAME":nameFieldEntry.get(),
        "AMO":int(amoFieldEntry.get()),
        "PRICE":float(PriceFieldEntry.get()),
        "DESC":None
    }, n.get()), supplyDb.updateDb(), makeSupplyRecord(),  curPopUp.destroy()])
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

    subminBtn = Button(curPopUp, text="Add Category", height=1, width=20, command=lambda:[ supplyDb.addCategory(nameFieldEntry.get()), supplyDb.updateDb(), makeSupplyRecord(), curPopUp.destroy()])
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

def changeProductAmo():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("240x200")
    curPopUp.resizable(False, False)

    changeProductAmoTitle = Label(curPopUp, text="Change Product Amo")
    changeProductAmoTitle.place(x=10, y=10)

    productChosenLbl = Label(curPopUp, text="Product:")
    productChosenLbl.place(x=10, y=50)
    product = StringVar(curPopUp)
    
    productChosen = OptionMenu(curPopUp, product, *productDb.getAllProductNames())
    productChosen.place(x=70, y=50)

    n = StringVar(curPopUp)

    amoFieldLbl = Label(curPopUp, text='Amo:')
    amoFieldLbl.place(x=10, y=90)
    amoFieldEntry = Entry(curPopUp, width=5)
    amoFieldEntry.place(x=50, y=90)

    r1 = Radiobutton(curPopUp, text="+", variable=n, value="+")
    r2 = Radiobutton(curPopUp, text="-", variable=n, value="-")
    r3 = Radiobutton(curPopUp, text="=", variable=n, value="=")
    r1.place(x=10, y=130)
    r2.place(x=60, y=130)
    r3.place(x=110, y=130)

    submitBtn = Button(curPopUp, text="Change Item Amo", command=lambda:[
        productDb.changeItemAmo(product.get().split("|")[1], product.get().split("|")[0], n.get(), int(amoFieldEntry.get())),
        productDb.updateDb(), makeProductRecord(), curPopUp.destroy()])
    submitBtn.place(x=10, y=170)

    curPopUp.mainloop() 

def changeSupplyAmo():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("240x200")
    curPopUp.resizable(False, False)

    changeProductAmoTitle = Label(curPopUp, text="Change Supply Amo")
    changeProductAmoTitle.place(x=10, y=10)

    productChosenLbl = Label(curPopUp, text="Supply:")
    productChosenLbl.place(x=10, y=50)
    product = StringVar(curPopUp)
    
    productChosen = OptionMenu(curPopUp, product, *supplyDb.getAllProductNames())
    productChosen.place(x=70, y=50)

    n = StringVar(curPopUp)

    amoFieldLbl = Label(curPopUp, text='Amo:')
    amoFieldLbl.place(x=10, y=90)
    amoFieldEntry = Entry(curPopUp, width=5)
    amoFieldEntry.place(x=50, y=90)

    r1 = Radiobutton(curPopUp, text="+", variable=n, value="+")
    r2 = Radiobutton(curPopUp, text="-", variable=n, value="-")
    r3 = Radiobutton(curPopUp, text="=", variable=n, value="=")
    r1.place(x=10, y=130)
    r2.place(x=60, y=130)
    r3.place(x=110, y=130)

    submitBtn = Button(curPopUp, text="Change Item Amo", command=lambda:[
        supplyDb.changeItemAmo(product.get().split("|")[1], product.get().split("|")[0], n.get(), int(amoFieldEntry.get())),
        supplyDb.updateDb(),
        makeSupplyRecord(),
        curPopUp.destroy()
        
    ])
    submitBtn.place(x=10, y=170)


    curPopUp.mainloop()

def soldProduct():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("200x120")
    curPopUp.resizable(False, False)

    soldProductTitle = Label(curPopUp, text="Sold Product")
    soldProductTitle.place(x=10, y=10)

    productChosenLbl = Label(curPopUp, text="Product:")
    productChosenLbl.place(x=10, y=50)
    product = StringVar(curPopUp)
    
    productChosen = OptionMenu(curPopUp, product, *productDb.getAllProductNames())
    productChosen.place(x=70, y=50)

    submitBtn = Button(curPopUp, text="Change Item Amo", command=lambda:[
        productDb.changeItemAmo(product.get().split("|")[1], product.get().split("|")[0], "-", 1),
        productDb.updateDb(), makeProductRecord(), curPopUp.destroy()])
    submitBtn.place(x=10, y=90)

    curPopUp.mainloop()
    

def usedSupply():
    curPopUp = Tk()
    curPopUp.title("App")
    curPopUp.geometry("200x200")
    curPopUp.resizable(False, False)

    usedSupplyTitle = Label(curPopUp, text="Used Supply")
    usedSupplyTitle.place(x=10, y=10 )

    productChosenLbl = Label(curPopUp, text="Supply:")
    productChosenLbl.place(x=10, y=50)
    product = StringVar(curPopUp)
    
    productChosen = OptionMenu(curPopUp, product, *supplyDb.getAllProductNames())
    productChosen.place(x=70, y=50)

    submitBtn = Button(curPopUp, text="Submit", command=lambda:[
        supplyDb.changeItemAmo(product.get().split("|")[1], product.get().split("|")[0], "-", 1),
        supplyDb.updateDb(),
        makeSupplyRecord(),
        curPopUp.destroy()
    ])

    


    curPopUp.mainloop()


#starting template   
#curPopUp = Tk()
#curPopUp.title()
#curPopUp.geometry("")
#curPopUp.resizable(False, False)
#curPopUp.mainloop()

COL1X = 10
COL2X = 110
COL3X = 210
COL4X = 310
MAXX = COL4X + 100

ROW1Y=100
ROW2Y=200
ROW3Y=300
ROW4Y=400 
MAXY = ROW3Y + 100


window = Tk()

window.geometry(f"{MAXX}x{MAXY}")
window.resizable(False, False)

mainTitleLabel = Label(window, text="Product Inventory App", font=("Lucida Sans Unicode", 25))
mainTitleLabel.place(x=10, y=10)
window.title("App")
BTNWIDTH = 10
BTNHEIGHT= 5


#column 1

addProductBtn = Button(window, text="Add\nProduct", command=addProductPopup, height=BTNHEIGHT, width=BTNWIDTH)
addProductBtn.place(x=COL1X, y=ROW1Y)

addProductCategoryBtn = Button(window, text="Add\nProduct\nCategory", command=addProductCategoryPopup, height=BTNHEIGHT, width=BTNWIDTH)
addProductCategoryBtn.place(x=COL1X, y=ROW2Y)

delProductBtn = Button(window, text="Delete\nProduct", command=delProductPopup, height=BTNHEIGHT, width=BTNWIDTH)
delProductBtn.place(x=COL1X, y=ROW3Y)



#column 2

delProductCategoryBtn = Button(window, text="Delete\nProduct\nCategory", height=BTNHEIGHT, width=BTNWIDTH, command=delProductCategory)
delProductCategoryBtn.place(x=COL2X, y=ROW1Y)

changeProductAmoBtn = Button(window, text="Change\nProduct\nAmount", height=BTNHEIGHT, width=BTNWIDTH, command=changeProductAmo)
changeProductAmoBtn.place(x=COL2X, y=ROW2Y)

soldProductBtn = Button(window, text="Sold\nItem", height=BTNHEIGHT, width=BTNWIDTH, command=soldProduct)
soldProductBtn.place(x=COL2X, y=ROW3Y)

#column 3

addSupplybtn = Button(window, text="Add\nSupply", command=addSupplyPopup, height=BTNHEIGHT, width=BTNWIDTH)
addSupplybtn.place(x=COL3X, y=ROW1Y)

addSupplyCategoryBtn = Button(window, text="Add\nSupply\nCategory", command=addSupplyCategory, height=BTNHEIGHT, width=BTNWIDTH)
addSupplyCategoryBtn.place(x=COL3X, y=ROW2Y)

delSupplyBtn = Button(window, text="Delete\nSupply", command=delSupplyPopup, height=BTNHEIGHT, width=BTNWIDTH)
delSupplyBtn.place(x=COL3X, y=ROW3Y)



#column 4

delSupplyCategoryBtn = Button(window, text="Delete\nSupply\nCategory", height=BTNHEIGHT, width=BTNWIDTH, command=delSupplyCategory)
delSupplyCategoryBtn.place(x=COL4X, y=ROW1Y)

changeSupplyAmoBtn = Button(window, text="Change\nSupply\nAmount", height=BTNHEIGHT, width=BTNWIDTH, command=changeSupplyAmo)
changeSupplyAmoBtn.place(x=COL4X, y=ROW2Y)

usedSupplyBtn = Button(window, text="Used\nSupply", height=BTNHEIGHT, width=BTNWIDTH, command=usedSupply)
usedSupplyBtn.place(x=COL4X, y=ROW3Y)

window.mainloop()
