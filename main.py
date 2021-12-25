import requests, json
import tkinter as tk
from PIL import Image, ImageTk
import io

window = tk.Tk()

api_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = input("Enter The Pokemon Number: ")

response = requests.get(api_url + str(pokemon))
data = response.json()

print("Name: ", end= "")
name = data["forms"][0]["name"]
abilities = data["abilities"]
types = data["types"]
stats = data["stats"]
print(name)

str_ability = "Abilities: \n"
for a in range(len(abilities)):
  str_ability += abilities[a]["ability"]["name"] +  ", "
print(str_ability)


str_type = "Type: \n"
for t in range(len(types)):
  str_type += types[t]["type"]["name"] + ", "
print(str_type)

str_stat = "Stats: \n"
for s in range(len(stats)):
  str_stat = stat_name = stats[s]["stat"]["name"]
  str_stat = stat_value = (stats[s]["base_stat"])
  print(stat_name + ": " + str(stat_value))

#Labels
lbl_name = tk.Label(text = name)
lbl_name.grid(row = 0, column = 1)


lbl_abilities = tk.Label(text = str_ability)
lbl_abilities.grid(row = 1, column = 0)

lbl_type = tk.Label(text = str_type)
lbl_type.grid(row = 2, column = 0)



image1 = Image.open(io.BytesIO(requests.get(data["sprites"]["front_default"]).content))
image1 = image1.resize((200,200),Image.ANTIALIAS)
sprite = ImageTk.PhotoImage(image1)

lbl_img = tk.Label(image = sprite)
lbl_img.grid(row = 5, column = 1)



window.mainloop()
