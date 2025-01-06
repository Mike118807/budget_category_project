import budget_category

# Create an instance of BudgetCategory
food_category = budget_category.BudgetCategory("Food", 500)

# Display initial budget details
food_category.display_category_summary()

# Add an expense and display updated budget details
food_category.add_expense(100)
food_category.display_category_summary()

# Change the category name and allocated budget
food_category.set_category_name("Groceries")
food_category.set_allocated_budget(600)

# Display updated budget details
food_category.display_category_summary()
