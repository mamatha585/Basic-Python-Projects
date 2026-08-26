class Details:
    def __init__(self,Product_name,Original_price,Discount_Percentage):
        self.Product_name = Product_name
        self.Original_price = Original_price
        self.Discount_Percentage = Discount_Percentage
 
    def disCal(self):
        if not (0 <= self.Discount_Percentage <= 100):
            print("Invalid Discount Percentage")
            return
        self.Discount_Amt = (self.Original_price * self.Discount_Percentage)/100

        self.Final_Price = self.Original_price - self.Discount_Amt
        
    def display(self):
        print("\n\n--------------- Discount Details ---------------")
        print(f"Product Name: {self.Product_name}")
        print(f"Original Price: ₹{self.Original_price:.2f}")
        print(f"Discount Percentage: {self.Discount_Percentage}%")
        print(f"Discount Amount: ₹{self.Discount_Amt:.2f}")
        print(f"Final Price: ₹{self.Final_Price:.2f}")

product_name = str(input("Enter Product Name: "))
original_price = float(input("Enter Original Price: "))
discount_percentage = float(input("Enter Discount Percentage: "))
dress = Details(product_name,original_price,discount_percentage)
dress.disCal()
dress.display()