from modules.manager import ManagerSqlite
from modules.pizza import Pizza


def main():
    # Inicializa el administrador de la base de datos
    manager = ManagerSqlite("pizza.db") 

    # Crea instancias de Pizza
    pizza = Pizza("Mozzarella","Individual",2000)
    pizza_dos = Pizza("Jamon","Chica",5000)
    pizza_tres = Pizza("JamonYMorrones","Grande",9000)
    pizza_cuatro = Pizza("Fugazzeta","Chica",3000)
    
    # Inserta las pizzas en la base de datos
    manager.insert_one_pizza(pizza)
    manager.insert_one_pizza(pizza_dos)
    manager.insert_one_pizza(pizza_tres)
    manager.insert_one_pizza(pizza_cuatro)

    # Obtiene y muestra todas las pizzas en la base de datos
    for pizza in manager.get_all_pizza():
        print(pizza)

    # Obtiene y muestra una pizza específica
    pizza_jamon = manager.get_one_pizza("Jamon")
    if pizza_jamon:
        print(pizza_jamon)
    else:
        print("No se encontró la pizza 'Jamon'.")


if __name__ == "__main__":
    main()