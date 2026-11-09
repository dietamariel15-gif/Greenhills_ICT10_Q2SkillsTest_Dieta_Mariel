
from pyscript import display, document


non_metals = {
    'H': {'name': 'Hydrogen', 'number': 1, 'mass': 1.008},
    'C': {'name': 'Carbon', 'number': 6, 'mass': 12.011},
    'N': {'name': 'Nitrogen', 'number': 7, 'mass': 14.007},
    'O': {'name': 'Oxygen', 'number': 8, 'mass': 15.999},
    'F': {'name': 'Fluorine', 'number': 9, 'mass': 18.998},
    'P': {'name': 'Phosphorus', 'number': 15, 'mass': 30.974},
    'S': {'name': 'Sulfur', 'number': 16, 'mass': 32.06},
    'Cl': {'name': 'Chlorine', 'number': 17, 'mass': 35.45},
    'Se': {'name': 'Selenium', 'number': 34, 'mass': 78.971},
    'Br': {'name': 'Bromine', 'number': 35, 'mass': 79.904},
    'I': {'name': 'Iodine', 'number': 53, 'mass': 126.90},
    'He': {'name': 'Helium', 'number': 2, 'mass': 4.0026},
    'Ne': {'name': 'Neon', 'number': 10, 'mass': 20.180},
    'Ar': {'name': 'Argon', 'number': 18, 'mass': 39.948},
    'Kr': {'name': 'Krypton', 'number': 36, 'mass': 83.798},
    'Xe': {'name': 'Xenon', 'number': 54, 'mass': 131.29},
    'Rn': {'name': 'Radon', 'number': 86, 'mass': 222}
}


def search_element(e):
    document.getElementById('div1').innerHTML = ' '

    element_symbol = document.getElementById('symbol').value.strip().capitalize()

    element_check = element_symbol in non_metals

    if element_symbol == '':
        display('Please enter an element symbol!', target='div1')

    elif element_check:
        element = non_metals[element_symbol]

        display(
            f"Element Symbol: {element_symbol}\n"
            f"Element Name: {element['name']}\n"
            f"Atomic Number: {element['number']}\n"
            f"Atomic Mass: {element['mass']}",
            target='div1'
        )

    else:
        display(
            f"Sorry, {element_symbol} does not exist in the non-metals list!",
            target='div1'
        )

