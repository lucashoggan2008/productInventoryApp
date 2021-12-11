from dbobjects import ProductDatabaseObject

pdb = ProductDatabaseObject()

pdb.refresh()

pdb.addProduct({
    "NAME":"TEST",
    "AMO":5,
    "SELLPRICE":20,
    "MAKEPRICE":10,
    "DECS":None
}, "Candles")

pdb.updateDb()
