from classes import (Country, Category, City, Product,Store)


def country_tables():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
        0. Back
            >>> """)

    if services == "1":
        Country.select()
        back = input("""
            0. Back
                >>>> """)
        if back == "0":
            return country_tables()

    elif services == "2":
        name = input("Name: ")
        country = Country(name)
        print(country.insert())
        return country_tables()

    elif services == "3":
        column = input("Column Name: ")
        old_date = input("Old Data: ")
        new_data = input("New Data: ")
        print(Country.update(column, new_data, old_date, "country"))

        return country_tables()

    elif services == "4":
        column = input("Column Name: ")
        data = input("Data: ")
        print(Country.delete(column, data, "country"))
        return country_tables()
    elif services == "0":
        return main()
    else:
        return country_tables()


def category_tables():
    services = input("""
        1. Select
        2. Insert
        3. Update
        4. Delete
        0. Back
            >>> """)

    if services == "1":
        Category.select()
        back = input("""
            0. Back
                >>>> """)
        if back == "0":
            return category_tables()

    elif services == "2":
        name = input("Name: ")
        category = Category(name)
        print(category.insert())
        return category_tables()

    elif services == "3":
        column = input("Column Name: ")
        old_date = input("Old Data: ")
        new_data = input("New Data: ")
        print(Category.update(column, new_data, old_date, "category"))

        return country_tables()

    elif services == "4":
        column = input("Column Name: ")
        data = input("Data: ")
        print(Category.delete(column, data, "category"))
        return category_tables()
    elif services == "0":
        return main()


def city_tables():
    services = input("""
            1. Select
            2. Insert
            3. Update
            4. Delete
            0. Back
                >>> """)

    if services == "1":
        Product.select()
        back = input("""
                0. Back
                    >>>> """)
        if back == "0":
            return city_tables()

    elif services == "2":
        name = input("Name: ")
        country_id = int(input("Country ID: "))
        city = City(name, country_id)
        print(city.insert())
        return city_tables()

    elif services == "3":
        column = input("Column Name: ")
        old_date = input("Old Data: ")
        new_data = input("New Data: ")
        print(City.update(column, new_data, old_date, "city"))

        return city_tables()

    elif services == "4":
        column = input("Column Name: ")
        data = input("Data: ")
        print(City.delete(column, data, "city"))
        return city_tables()
    elif services == "0":
        return main()


def product_table():
    services = input("""
                1. Select
                2. Insert
                3. Update
                4. Delete
                0. Back
                    >>> """)

    if services == "1":
        Product.select()
        back = input("""
                    0. Back
                        >>>> """)
        if back == "0":
            return product_table()

    elif services == "2":
        name = input("Name: ")
        description = input("Description: ")
        price = input("Price: ")
        count = input("Count: ")
        serial_number = int(input("Serial Number: "))
        start_date = input("Start Date: ")
        end_date = input("End Date: ")
        store_id = int(input("Store ID: "))
        category_id = int(input("Category ID: "))
        product = Product(name, description, price, count, serial_number, start_date, end_date, store_id, category_id)
        print(product.insert())
        return product_table()

    elif services == "3":
        column = input("Column Name: ")
        old_date = input("Old Data: ")
        new_data = input("New Data: ")
        print(Product.update(column, new_data, old_date, "product"))

        return product_table()

    elif services == "4":
        column = input("Column Name: ")
        data = input("Data: ")
        print(Product.delete(column, data, "product"))
        return product_table()
    elif services == "0":
        return main()
    else:
        return city_tables()


def store_table():
    services = input("""
                1. Select
                2. Insert
                3. Update
                4. Delete
                0. Back
                    >>> """)

    if services == "1":
        Store.select()
        back = input("""
                    0. Back
                        >>>> """)
        if back == "0":
            return store_table()

    elif services == "2":
        name = input("Name: ")

        store = Store(name)
        print(store.insert())
        return store_table()

    elif services == "3":
        column = input("Column Name: ")
        old_date = input("Old Data: ")
        new_data = input("New Data: ")
        print(Store.update(column, new_data, old_date, "store"))

        return store_table()

    elif services == "4":
        column = input("Column Name: ")
        data = input("Data: ")
        print(Store.delete(column, data, "store"))
        return store_table()
    elif services == "0":
        return main()


def main():
    tables = input("""
        1. Country
        2. City
        3. Category
        4. Store
        5. Produckt
            >>> """)

    if tables == "1":
        return country_tables()

    elif tables == "2":
        return city_tables()

    elif tables == "3":
        return category_tables()

    elif tables == "4":
        return store_table()

    elif tables == "5":
        return product_table()

    else:
        print("Error")
        return main()


if __name__ == "__main__":
    main()
