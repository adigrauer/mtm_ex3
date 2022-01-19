# addProduct
# add product to the storage if does not exit already, and amount and price is not negativ.
def addProduct(warehouse, product_name, price, amount):
    if not product_name in warehouse or price < 0 or amount < 0:
        return
    warehouse[product_name] = [price, amount, 0] #value[2] = quantitiy of units sold

# changeProductAmount
# change product amount in storage if already exit.
# amount of item can be negativ
def changeProductAmount(warehouse, product_name, amount_to_update):
    if not product_name in warehouse:
        return
    warehouse[product_name][1] += amount_to_update

# shipOrder
# ship order if item exit in storage and amount of quantaties is not lower than ordered
# update the counter of selling of the item
def shipOrder(warehouse, orders):
    for product in range(2,len(orders),2):
        if orders[product] == "-": 
            continue
        if not product in warehouse:
            continue
        if warehouse[product][1] < orders[product+1]:
            continue
        warehouse[product][1] - orders[product+1]
        warehouse[product][2] += 1

# createWarehouse
# create warehouse due to commands in given file text
def createWarehouse(file_name):
    warehouse = {}
    for line in file_name:
        read_line = line.split()
        if read_line[0] == "add":
            addProduct (warehouse, *read_line[2:])
        elif read_line[0] == "change":
            changeProductAmount(warehouse, *read_line[2:])
        else:
            shipOrder(warehouse, read_line)

# find_best_selling_product
# return taple of best product name and his profits
def find_best_selling_product(file_name):
    warehouse = createWarehouse(file_name)
    sorted_warehouse = sorted(warehouse.items(), key=lambda tup: tup[1][2], reverse= True)
    key, val = sorted_warehouse[0]
    return (key, val[0]*val[2])

# find_k_most_expensive_products
# return list of k most expensive items orderd vy price.
# items with the same price will be orderd lexicography
def find_k_most_expensive_products(file_name, k):
    warehouse = createWarehouse(file_name)
    sorted_warehouse = sorted(warehouse.items(), key=lambda tup: (-tup[1][0], tup[0]))
    return [item[0] for item in sorted_warehouse[:k]]