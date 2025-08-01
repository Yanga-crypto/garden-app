# Using input to get `season` and `plant_type`.
season = input(
    "Please select the season (spring, summer, autum, winter)"
).lower()
plant_type = input(
    "Please select the plant type (flower, vegatable, fruit)"
).lower()

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season

if season == "spring":
    advice += "Plant your seeds"
elif season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "autum":
    advice += "Focus on mulching and planting cool-season vegetables."
# Add more seasons like Spring and Autum
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "fruit":
    advice += ("Water regularly, especially during dry periods "
               "and the flowering and fruiting stages. ")
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
