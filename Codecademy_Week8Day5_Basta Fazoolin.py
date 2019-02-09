class Business:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises
    
  def __repr__(self):
    return "We own the business {business}. {address}".format(business = self.name, address = self.franchises)

class Franchise:
  def __init__(self, address, menus):
    self.address = address
    self.menus = menus
    
  def __repr__(self):
    return "The address is {address}.".format(address = self.address)
  
  def available_menus(self, time):
    available_menus = []
    for menu in self.menus:
      if time >= menu.start_time and time <= menu.end_time:
        available_menus.append(menu)
    return available_menus

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time
    
  def __repr__(self):
    return "The {menu} menu is available from {start} to {end}.".format(menu = self.name, start = self.start_time, end = self.end_time)
  
  def calculate_bill(self, purchased_items):
    bill = 0
    for purchased_item in purchased_items:
      if purchased_item in self.items:
        bill += self.items[purchased_item]
    return bill
  

# Basta Fazoolin' with my Heart Menus:  
# Brunch Menu
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}

brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)

print(brunch_menu)  # Results in "The Brunch menu is available from 1100 to 1600."

print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))  # Results in "13.5"

# Early Bird Menu
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}

early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)

print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))  # Results in "21.5"

# Dinner Menu
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
    
# Kids Menu
kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('Kids', kids_items, 1100, 2100)


# Basta Fazoolin' with my Heart Franchises:
menus = [brunch_menu, early_bird_menu, dinner_menu, kids_menu]

flagship_store = Franchise('1232 West End Road', menus)

new_installment = Franchise('12 East Mulberry Street', menus)

print(flagship_store)  # Results in "The address is 1232 West End Road."

print(flagship_store.available_menus(1200))  # Results in "[The Brunch menu is available from 1100 to 1600., The Kids menu is available from 1100 to 2100.]"

print(flagship_store.available_menus(1700))  # Results in "[The Early Bird menu is available from 1500 to 1800., The Dinner menu is available from 1700 to 2300., The Kids menu is available from 1100 to 2100.]"


# Take a'Arepa Menus:  
# Arepas Menu
arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}

arepas_menu = Menu('Arepas', arepas_items, 1000, 2000)

# Take a'Arepa Franchises:
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)

# Businesses
basta_fazoolin = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

take_arepa = Business('Take a\' Arepa', arepas_place)

print(basta_fazoolin)  # Results in "We own the business Basta Fazoolin' with my Heart. [The address is 1232 West End Road., The address is 12 East Mulberry Street.]"
print(take_arepa)  # Results in "We own the business Take a' Arepa. The address is 189 Fitzgerald Avenue."


