# Calculate customer acquisition cost based on marketing expenses and number of new customers
def calculate_customer_acquisition_cost(marketing_expenses, num_new_customers):
    return marketing_expenses / num_new_customers if num_new_customers > 0 else 0

# Example usage:
marketing_expenses = 10000  # Total marketing expenses
num_new_customers = 200  # Number of new customers acquired
customer_acquisition_cost = calculate_customer_acquisition_cost(marketing_expenses, num_new_customers)
print("Customer acquisition cost:", customer_acquisition_cost)
