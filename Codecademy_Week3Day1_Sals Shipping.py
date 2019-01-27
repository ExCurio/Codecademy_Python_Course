#Week 3, Day 1 - Project: Sal's Shipping

def cost_of_ground_shipping(weight):
  if weight <= 2:
    price_per_pound = 1.50
  elif weight <= 6:
    price_per_pound = 3.00
  elif weight <= 10:
    price_per_pound = 4.00
  else:
    price_per_pound = 4.75
  return 20 + (price_per_pound * weight)

cost_of_premium_ground_shipping = 125.00

def cost_of_drone_shipping(weight):
  if weight <= 2:
    price_per_pound = 4.50
  elif weight <= 6:
    price_per_pound = 9.00
  elif weight <= 10:
    price_per_pound = 12.00
  else:
    price_per_pound = 14.25
  return price_per_pound * weight

def print_cheapest_shipping(weight):
  
  ground = cost_of_ground_shipping(weight)
  premium = cost_of_premium_ground_shipping
  drone = cost_of_drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "Ground shipping"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium shipping"
    cost = premium
  else:
    method = "Drone shipping"
    cost = drone

  print("The cheapest shipping rate available is $%.2f with %s." % (cost, method))
    

print_cheapest_shipping(4.8)
print_cheapest_shipping(41.5)