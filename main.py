# C0772827
# Jeison Guerrero
from pymongo import MongoClient
from tkinter import *

client = MongoClient("mongodb+srv://pythonJ:python123@cluster0.c1vms.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db=client.business

root = Tk()
root.title("Tech Invetory Mananger")
root.geometry("450x300")
root.option_add( "*font", "lucida 14 bold italic" )

def add_product():
    label_type = Label(root, text="Type")
    label_type.grid(row=3, column=0)
    product_type = Entry(root, width=20, borderwidth=5)
    product_type.grid(row=3, column=1)

    label_brand = Label(root, text="brand")
    label_brand.grid(row=4, column=0 )
    product_brand = Entry(root, width=20, borderwidth=5)
    product_brand.grid(row=4, column=1) 

    label_stock = Label(root, text="Stock")
    label_stock.grid(row=5, column=0)
    product_stock = Entry(root, width=20, borderwidth=5)
    product_stock.grid(row=5, column=1)

    confirm_product = Button(root, text="Enter", height=2, width=15, command=lambda: add_product_button())
    confirm_product.grid(row=6, column=0, columnspan=3)

    def add_product_button():
        product = {
            'type': product_type.get(),
            'brand': product_brand.get(),
            'stock': product_stock.get()
        }
        result=db.inventory.insert_one(product)
        
def delete_product():
    del_product = Entry(root, width=20, borderwidth=5)
    del_product.grid(row=3, column=0)
   
    del_button = Button(root, text="Enter", height=2, width=15, command=lambda: del_product_button())
    del_button.grid(row=3, column=1)

    def del_product_button():
        result = db.inventory.delete_many({'type':del_product.get()})

def update_product():
    updt_prod = Entry(root, width=20, borderwidth=5)
    updt_prod.grid(row=3, column=0)
   
    current_button = Button(root, text="Enter", height=2, width=15, command=lambda: change_product_info())
    current_button.grid(row=3, column=1)

    def change_product_info():
        current_product = db.inventory.find_one({'type':updt_prod.get()})
        current_product_info = "Type: " + str(current_product.get('type')) + "\nBrand: " + str(current_product.get('brand')) + "\nStock: " + str(current_product.get('stock'))
        query_label_type = Label(root, text=current_product_info)
        query_label_type.grid(row=4, column=0, columnspan=3)

        update_label_type = Label(root, text="Type")
        update_label_type.grid(row=5, column=0)
        update_product_type = Entry(root, width=20, borderwidth=5)
        update_product_type.grid(row=5, column=1)

        update_label_brand = Label(root, text="Brand")
        update_label_brand.grid(row=6, column=0 )
        update_product_brand = Entry(root, width=20, borderwidth=5)
        update_product_brand.grid(row=6, column=1) 

        update_label_stock = Label(root, text="Stock")
        update_label_stock.grid(row=7, column=0)
        update_product_stock = Entry(root, width=20, borderwidth=5)
        update_product_stock.grid(row=7, column=1)

        confirm_button = Button(root, text="Enter", height=2, width=10, command=lambda: update_product_button())
        confirm_button.grid(row=8, column=0, columnspan=3)

        def update_product_button():
            ASingleReview = db.inventory.find_one({'type':updt_prod.get()})
            
            newvalues = {   
                    '$set' : {
                        'type': update_product_type.get(),
                        'brand': update_product_brand.get(),
                        'stock': update_product_stock.get()
                        }
                    }

            update = db.inventory.update_many(
                {'_id':ASingleReview.get('id')},newvalues)

            UpdatedDocument = db.inventory.find_one({'_id':ASingleReview.get('_id')})
            print('The updated document:')
            print(UpdatedDocument)

def list_products():
    e = Entry(root, width=20, borderwidth=5)
    e.grid(row=3, column=0)
    button_e = Button(root, text="Enter", height=1, width=10, command=lambda: list_products_button())
    button_e.grid(row=3, column=1)

    def list_products_button():
        product = db.inventory.find_one({ 'type': e.get()})

        product_info = "Type: " + str(product.get('type')) + "\nBrand: " + str(product.get('brand')) + "\nStock: " + str(product.get('stock'))

        query_label = Label(root, text=product_info)
        query_label.grid(row=4, column=0, columnspan=3)

button_1 = Button(root, text="Add product", height=2, width=15, command=lambda: add_product())
button_2 = Button(root, text="Update product", height=2, width=15, command=lambda: update_product())
button_3 = Button(root, text="Delete product", height=2, width=15, command=lambda: delete_product())
button_4 = Button(root, text="View products", height=2, width=15, command=lambda: list_products())

button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=2, column=0)
button_4.grid(row=2, column=1)

root.mainloop()
