from easygui import *

msg = "Informations clients"
fields = ('Prénom','Nom','Téléphone','Email')
customer = multenterbox(msg,msg,fields)

pizza_count = integerbox('Combien de pizza ?')
pizzas_list = {
    "Reine": ['a'],
    "Diavola": ['b'],
}
ingredients = ['tomate','mozzarella','jambon','champignons','salami piquant','basilic']
pizzas = []

for p in range(pizza_count):
    if boolbox('Type','Type de pizza',('Choisir', 'Creer')):
        choice = choicebox('Choisir une pizza','Choisir dans la liste :',pizzas_list)
        pizzas.append(choice)
    else:
        choice = multchoicebox('Choisir les ingrédients','Choisir les ingrédients :',ingredients)
        custom = ['Custom', choice]
        pizzas.append(choice)

text = "Pizzas : " + str(len(pizzas)) + "\n"
for piz in pizzas:
    if len(piz) == 1:
        text = text + piz + "\n"
    else:
        text = text + 'Custom : ' + str(piz) + "\n"

text = text + 'Total : ' + str(len(pizzas)*10) + '€'

msgbox(text,'Récapitulatif','Valider')
print(pizzas)