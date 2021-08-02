def shipstation_order_create(order_data, product_data):
    #code
    for product in product_data:
       print(product['total_amount'])
       print(product['product'].id)


class Test:
    def __init__(self, id):
        self.id = id
# everything from here is in another file
product1 =  Test(1)
product2 =  Test(2)
product3 =  Test(3)
order ={}
cart =[
    {
        'total_amount': 30,
        'product': product1
        }, 
    {'total_amount': 31,
        'product': product2


    }, 
    {'total_amount': 32,
        'product': product3
    }
    ]


shipstation_order_create(order, cart)