from agents import function_tool


@function_tool
async def meal_planner(diet_preferences:str)->list[str]:
    """
     Generate a 7-day vegetarian meal plan including breakfast, lunch, and dinner for each day.
    """

    if diet_preferences.lower() != "vegetarian":
        return "Currently, only vegetarian plans are supported."
    
    meal_plan=[]

    meals = [
        ("Oatmeal with berries and almonds", "Grilled veggie wrap with hummus", "Lentil curry with brown rice"),
        ("Greek yogurt with granola", "Chickpea salad sandwich", "Vegetable stir fry with tofu"),
        ("Smoothie bowl with banana and chia", "Quinoa and black bean bowl", "Stuffed bell peppers"),
        ("Whole grain toast with peanut butter", "Zucchini noodles with pesto", "Spinach and paneer curry"),
        ("Muesli with soy milk", "Vegetarian burrito bowl", "Vegetable lasagna"),
        ("Fruit salad and toast", "Mushroom and spinach quesadilla", "Chana masala with naan"),
        ("Chia pudding with mango", "Caprese sandwich", "Falafel with couscous and tahini")
    ]


    for i,(breakfast, lunch, dinner) in enumerate(meals):
        day_plan=(
            f"Day {i+1} - Vegetarian Plan:\n"
            f"  🥣 Breakfast: {breakfast}\n"
            f"  🥗 Lunch: {lunch}\n"
            f"  🍝 Dinner: {dinner}\n"
        )

        meal_plan.append(day_plan)

    return "\n".join(meal_plan)