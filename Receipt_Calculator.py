from fpdf import FPDF

class ReceiptCalculator:
    def __init__(self):
        self.items = []

    def add_item(self, name, price, quantity):
        """Add an item to the list."""
        self.items.append({"name": name, "price": price, "quantity": quantity})

    def calculate_totals(self, tax_rate=0.05, discount_rate=0.1):
        """Calculate subtotal, tax, discount, and final total."""
        subtotal = sum(item["price"] * item["quantity"] for item in self.items)
        tax = subtotal * tax_rate
        discount = subtotal * discount_rate
        total = subtotal + tax - discount
        return subtotal, tax, discount, total

    def generate_receipt(self, subtotal, tax, discount, total):
        """Display the receipt on the console."""
        print("\n====== Receipt ======")
        for item in self.items:
            print(f"{item['name']} (x{item['quantity']}): ${item['price'] * item['quantity']:.2f}")
        print(f"\nSubtotal: ${subtotal:.2f}")
        print(f"Tax: ${tax:.2f}")
        print(f"Discount: ${discount:.2f}")
        print(f"Total: ${total:.2f}")

    def save_receipt_as_text(self, subtotal, tax, discount, total):
        """Save the receipt as a text file."""
        with open("receipt.txt", "w") as file:
            file.write("====== Receipt ======\n")
            for item in self.items:
                file.write(f"{item['name']} (x{item['quantity']}): ${item['price'] * item['quantity']:.2f}\n")
            file.write(f"\nSubtotal: ${subtotal:.2f}\n")
            file.write(f"Tax: ${tax:.2f}\n")
            file.write(f"Discount: ${discount:.2f}\n")
            file.write(f"Total: ${total:.2f}\n")
        print("\nReceipt saved as 'receipt.txt'.")

    def save_receipt_as_pdf(self, subtotal, tax, discount, total):
        """Save the receipt as a PDF file."""
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, txt="====== Receipt ======", ln=True, align='C')

        for item in self.items:
            pdf.cell(200, 10, txt=f"{item['name']} (x{item['quantity']}): ${item['price'] * item['quantity']:.2f}", ln=True)

        pdf.cell(200, 10, txt=f"\nSubtotal: ${subtotal:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Tax: ${tax:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Discount: ${discount:.2f}", ln=True)
        pdf.cell(200, 10, txt=f"Total: ${total:.2f}", ln=True)

        pdf.output("receipt.pdf")
        print("\nReceipt saved as 'receipt.pdf'.")

# Main program
if __name__ == "__main__":
    calculator = ReceiptCalculator()

    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        price = float(input(f"Enter price for {name}: "))
        quantity = int(input(f"Enter quantity for {name}: "))
        calculator.add_item(name, price, quantity)

    subtotal, tax, discount, total = calculator.calculate_totals()

    calculator.generate_receipt(subtotal, tax, discount, total)

    save_option = input("\nSave receipt as (1) Text or (2) PDF? Enter 1 or 2: ")
    if save_option == "1":
        calculator.save_receipt_as_text(subtotal, tax, discount, total)
    elif save_option == "2":
        calculator.save_receipt_as_pdf(subtotal, tax, discount, total)
    else:
        print("Invalid option. Receipt not saved.")
