# Displays a name and address formatted like a mailing label
def display_mailing_label(name, address, city, state, zip):
    print(name)
    print(address)
    print(f"{city}, {state} {zip}")
    print()


# Adds any number of integers and shows the full equation
def add_numbers(*numbers):
    total = sum(numbers)
    equation = " + ".join(str(n) for n in numbers)
    print(f"{equation} = {total}")


# Shows the total, amount paid and change or remaining balance
def display_receipt(total_due, amount_paid):
    print(f"Total Due: ${total_due:,.2f}")
    print(f"Amount Paid: ${amount_paid:,.2f}")
    print()
    if amount_paid >= total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change:,.2f}")
    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance:,.2f} still needs to be paid.")
    print("-" * 30)


display_mailing_label("Meric Capar", "395 Castro St", "Mountain View", "CA", "94043")
display_mailing_label("Deodat Sharma", "456 University Ave", "Palo Alto", "CA", "94301")

add_numbers(5)
add_numbers(5, 10)
add_numbers(5, 10, 15, 20)

display_receipt(45.50, 50)      # overpay
display_receipt(45.50, 45.50)   # exact
display_receipt(45.50, 30)      # underpay