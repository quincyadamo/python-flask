#Create a function that takes in two lists and creates a single dictionary
#where the first list contains keys and the second values

name = ["Samantha", "Thomas", "Taylor", "Jose", "Sky", "Elisa", "Tori"]
favorite_animal = ["zebra", "tiger", "elephant", "giraffe", "gorilla", "dolphins", "llamas"]

new_dict = zip(name,favorite_animal)
print new_dict
