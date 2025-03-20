def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
      discounted_price = price - (price * discount_percent / 100)
      return discounted_price
    else:
        return price
    
price = int(input("Enter   the price :"))
discount = int(input("Enter the discount :"))
final_price = calculate_discount(price,discount)
print(f'The final price is:{final_price}')