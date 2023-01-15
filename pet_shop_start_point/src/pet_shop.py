# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop['name']

def get_total_cash(pet_shop):
    return pet_shop['admin']['total_cash']

def add_or_remove_cash(pet_shop,cash_change):
    pet_shop['admin']['total_cash'] += cash_change

def get_pets_sold(pet_shop):
    return pet_shop['admin']['pets_sold']
    
def increase_pets_sold(pet_shop,change):
    pet_shop['admin']['pets_sold'] += change
    return pet_shop['admin']['pets_sold']

def get_stock_count(pet_shop):
   return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop,pet):
    list_of_pets = []
    for pets in pet_shop['pets']:
        if pets['breed'] == pet:
            list_of_pets.append(pets['breed'])
    return list_of_pets

def find_pet_by_name(pet_shop,name):
    for pets in pet_shop['pets']:
        if pets['name'] == name:
            return pets
    return None

def remove_pet_by_name(pet_shop,name):
    for pets in pet_shop['pets']:
        if pets['name'] == name:
             pet_shop['pets'].remove(pets)


def add_pet_to_stock(pet_shop,new_pet):
    pet_shop['pets'].append(new_pet)


def get_customer_cash(customer):
    return customer['cash']

def remove_customer_cash(customer,cash):
    customer['cash'] -= cash

def get_customer_pet_count(customer):
    return len(customer['pets'])


def add_pet_to_customer(customer,new_pet):
    customer['pets'].append(new_pet)

def customer_can_afford_pet(customer,new_pet):
    if customer['cash'] >= new_pet['price']:
        return True
    else: 
        return False

