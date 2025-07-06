pet = input("What is the animal species: ")
age_pet = int(input("Enter pet's age: "))

# Default food
recommended_food = "Regular pet food"

if pet == "Dog" and age_pet < 2:
    recommended_food = "Puppy Food"
elif pet == "Cat" and age_pet > 5:
    recommended_food = "Senior cat food"

print("Animal species is", pet, "and age is", age_pet, "so recommended food is", recommended_food)
