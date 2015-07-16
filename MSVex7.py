# Calculate the total charge for an online store in Canada
# Check if person lives in Canada and if so what province they are from
# Apply taxes appropriately and return the total.

class CanadaPay(object):
    def __init__(self, response=input, display=print, total=0, 
                    generalSalesTax=5, harmonizedSalesTax=13, provinceTax=6 ):
        self.response = response
        self.display = display
        self.final_total = total
        self.gst = generalSalesTax
        self.hst = harmonizedSalesTax
        self.pt = provinceTax
    def final_sales(self):
        country = self.response("What Country are you from? ").lower()
        order_total = float(self.response("What was your total? "))
        if country == "canada":
            province = self.response("What Province? ").lower()
            if province == "alberta":
                taxes = order_total * (self.gst / 100)# Gets the decimal form of the percent.
                total = order_total + taxes
                self.display("Your final total is: $%.2f" % total) # Note %.2f will limit the float to two decimal points.
            elif province == "ontario" or province == "new brunswick" or \
                province == "nova scotia":
                taxes = order_total * (self.hst / 100)
                total = order_total + taxes
                self.display("Your final total is: $%.2f" % total)
            else:
                taxes = order_total * ((self.pt / 100) + (self.gst / 100))
                total = order_total + taxes
                self.display("Your final total is: $%.2f" % total)
        else:
            self.display("Your total is: $%.2f" % order_total )
            
run = CanadaPay()
run.final_sales()