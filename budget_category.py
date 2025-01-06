class BudgetCategory:
    def __init__(self, category_name, allocated_budget):
        self.__category_name = category_name
        self.__allocated_budget = allocated_budget
        self.__remaining_budget = allocated_budget  # Initialize remaining budget to allocated budget

    # Getter for category_name
    def get_category_name(self):
        return self.__category_name

    # Setter for category_name
    def set_category_name(self, category_name):
        self.__category_name = category_name

    # Getter for allocated_budget
    def get_allocated_budget(self):
        return self.__allocated_budget

    # Setter for allocated_budget with validation
    def set_allocated_budget(self, allocated_budget):
        if allocated_budget > 0:
            self.__allocated_budget = allocated_budget
            self.__remaining_budget = allocated_budget  # Reset remaining budget
        else:
            print("Budget should be a positive number")

    # Method to add an expense to the category
    def add_expense(self, amount):
        if amount > 0 and amount <= self.__remaining_budget:
            self.__remaining_budget -= amount
            print(f"Expense of {amount} added. Remaining budget: {self.__remaining_budget}")
        else:
            print("Invalid expense amount")

    # Method to display the budget category details
    def display_category_summary(self):
        print(f"Category: {self.__category_name}")
        print(f"Allocated Budget: {self.__allocated_budget}")
        print(f"Remaining Budget: {self.__remaining_budget}")
