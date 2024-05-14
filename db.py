# HW4 - Customers    Oswaldo Flores
"""
To handle the database.

Each database will have a class and each database will have a class for connection.

STANDARD_FIRST_NAME: The customer's first name in a list.
STANDARD_LAST_NAME: The customer's last name in a list.
STANDARD_STREET: The customer's street in a list.
STANDARD_CITY: The customer's city in a list.
STANDARD_STATE: The customer's state in a list.
STANDARD_ZIP: The customer's zip in a list.
STANDARD_PHONE_STATEMENT: The customer's phone number in a list.
IMPORT_FILE_NAME: File to import.
EXPORT_FILE_NAME: File to export.
DATABASE: Sqlite database
INSERT_A_CUSTOMER: To insert a customer.
INSERT_A_ADDRESS: To insert an address.
GET_CUSTOMERS:To get customers.
GET_CUSTOMER_BY_ID: To get customer by id.
GET_ADDRESSES: To addresses.
GET_FIRST_CUSTOMER_ADDRESS: To get first customer.
GET_LAST_CUSTOMER_ADDRESS: To get last customer.
GET_ASC_CUSTOMER_ADDRESSES: To get customers with their addresses in ascending order.
GET_DESC_CUSTOMER_ADDRESSES: To get customers with their addresses in descending order.
DELETE_A_CUSTOMER: To delete a customer.
DELETE_AN_ADDRESS: To delete address(es).
UPDATE_CUSTOMER: To update a customer.
UPDATE_ADDRESS: To update an address.
"""
import csv
import objects
import os.path
import sqlite3
from abc import ABC, abstractmethod
from contextlib import closing


class Connection(ABC):
    @abstractmethod
    def get_connection(self):
        """
        To get a connection.

        To get a connection. Is-A class must have this method because it is abstract.
        :return:
        """
        pass


class SqliteConnection(Connection):
    __database_file: str = ''

    def __init__(self, database_file) -> None:
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param database_file: The name of the database file.
        """
        self.__database_file = database_file

    def get_connection(self):
        """
        To get a connection in the sqlite database.

        To get a connection in the sqlite database.

        :return: A connection to sqlite.
        """
        conn = sqlite3.connect(self.__database_file)
        conn.row_factory = sqlite3.Row
        return conn


class CsvConnection(Connection):
    __file_name: str = ''

    def __init__(self, file_name: str):
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param file_name: The name of the file for csv.
        :type file_name: str
        """
        self.__file_name = file_name

    def get_connection(self):
        """
        To get a connection to the csv file.

        To get a connection to the csv file. If a file does not exist, it creates the file.

        :return: The connection to the file.
        """
        if not os.path.exists(self.__file_name):
            with open(self.__file_name, 'w'):
                pass
        return open(self.__file_name, mode='r+', newline='')


class DAO(ABC):
    @abstractmethod
    def insert_customer(self, first_name, last_name):
        """
        To insert a customer to a database.

        To insert a customer to a database. Is-A class must have this method because it is abstract.

        :param first_name: The first name of a customer.
        :param last_name: The last name of a customer.
        """
        pass

    @abstractmethod
    def insert_an_address(self, customer_id, street, city, state, address_zip, phone_number):
        """
        To insert an address.

        To insert an address to a database. Is-A class must have this method because it is abstract.

        :param customer_id: The id for a customer.
        :param street: The name of the street.
        :param city: The name of the city
        :param state: The name of the state.
        :param address_zip: The zip.
        :param phone_number: A customer's phone number.
        :return:
        """
        pass

    @abstractmethod
    def delete_customer(self, customer_id):
        """
        To delete a customer.

        To delete a customer with a given customer id. Is-A class must have this method
        because it is abstract.

        :param customer_id: The id of a customer.
        """
        pass

    @abstractmethod
    def delete_address(self, customer_id):
        """
        To delete address(es).

        To delete address(es) with a given customer id. Is-A class must have this
        method because it is abstract.

        :param customer_id:  The id of a customer.
        """
        pass

    @abstractmethod
    def get_customer(self):
        """
        To get customers only.

        To get customers. Is-A class must have this method because it is abstract.
        """
        pass

    @abstractmethod
    def get_address(self):
        """
        To get addresses only.

        To get addresses only. Is-A class must have this method because it is abstract.
        """
        pass

    @abstractmethod
    def get_first_customer_address(self):
        """
        To get the first customer with their first address.

        To get the first customer with their first address. Is-A class must have
        this method because it is abstract.
        """
        pass

    @abstractmethod
    def get_last_customer_address(self):
        """
        To get the last customer with their last address.

        To get the last customer with their last address. Is-A class must have
        this method because it is abstract.
        """
        pass

    @abstractmethod
    def get_asc_customer_addresses(self):
        """
        To get customer addresses in ascending order.

        To get customer addresses in ascending order. Is-A class must have this
        method because it is abstract.
        """
        pass

    @abstractmethod
    def get_desc_customer_addresses(self):
        """
        To get customer addresses in descending order.

        To get customer addresses in descending order. Is-A class must have this method
        because it is abstract.
        """
        pass

    @abstractmethod
    def update_customer(self, customer_id, first_name, last_name):
        """
        To update a customer.

        To update a customer data. Is-A class must have this method because it is abstract.

        :param customer_id: The id for a customer.
        :param first_name: The customer's first name.
        :param last_name: The customer's last name.
        """
        pass

    @abstractmethod
    def export_file(self, customers):
        """
        To export data.

        To export data. Is-A class must have this method because it is abstract.

        :param customers: A list of customers with their addresses.
        """
        pass

    @abstractmethod
    def update_address(self, address_id, street, city, state, address_zip, phone_number):
        """
        To update an address.

        To update an address. Is-A class must have this method because it is abstract.

        :param address_id: The id for an address.
        :param street: The name of the street.
        :param city: The name of the city.
        :param state: The name of the state.
        :param address_zip: The zip.
        :param phone_number: Customer's phone number.
        """
        pass

    @abstractmethod
    def get_customer_address_id(self, customer_id):
        """
        To get a customer with their address(es).

        To get a customer with their address(es) with a given customer id.
        Is-A class must have this method because it is abstract.
        :param customer_id: The id for a customer.
        """
        pass


class CsvDAO(DAO):
    IMPORT_FILE_NAME = 'customers.csv'
    EXPORT_FILE_NAME = 'export.csv'
    STANDARD_FIRST_NAME = 0
    STANDARD_LAST_NAME = 1
    STANDARD_STREET = 2
    STANDARD_CITY = 3
    STANDARD_STATE = 4
    STANDARD_ZIP = 5
    STANDARD_PHONE_STATEMENT = 6

    __connection = None

    def __init__(self, connection):
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param connection: A connection.
        """
        self.__connection = connection

    def export_file(self, customers):
        """
        To export data.

        To export data to a csv file. I assume I should not delete any data that is in the
        csv file.
        :param customers: A list of customers.
        """
        with self.__connection.get_connection() as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            for _ in reader:
                pass
            writer = csv.writer(csv_file, delimiter=',')
            for customer in customers:
                a_customer = customer.split(',')
                writer.writerow([f'{a_customer[self.STANDARD_FIRST_NAME]}'] +
                                [f'{a_customer[self.STANDARD_LAST_NAME]}'] +
                                [f'{a_customer[self.STANDARD_STREET]}'] +
                                [f'{a_customer[self.STANDARD_CITY]}'] +
                                [f'{a_customer[self.STANDARD_STATE]}'] +
                                [f'{a_customer[self.STANDARD_ZIP]}'] +
                                [f'{a_customer[self.STANDARD_PHONE_STATEMENT]}'])

    def get_asc_customer_addresses(self):
        """
        To get data from the csv file.

        To get data from the csv file. I assume the csv is already in ascending order.
        I assume the csv file is formatted correctly. I assume every customer is unique.
        :return:
        """
        with self.__connection.get_connection() as csv_file:
            reader = csv.reader(csv_file, delimiter='\t')
            customers = []
            for row in reader:
                customer = objects.Customer(row[self.STANDARD_FIRST_NAME], row[self.STANDARD_LAST_NAME])
                address = objects.Address(0, row[self.STANDARD_STREET], row[self.STANDARD_CITY],
                                          row[self.STANDARD_STATE], row[self.STANDARD_ZIP],
                                          row[self.STANDARD_PHONE_STATEMENT])
                customer.append(address)
                customers.append(customer)
            return customers

    def insert_customer(self, first_name, last_name):
        """
        To insert a customer.

        To insert a customer to the csv file. I assume I should not delete anything
        in the file.

        :param first_name: The first name of the customer.
        :param last_name: The last name of the customer.
        """
        pass

    def insert_an_address(self, customer_id, street, city, state, address_zip, phone_number):
        """
        To insert an address.

        To insert an address to the csv file. I assume I should not delete anything
        in the file.

        :param customer_id: The customer id.
        :param street: The name of the street.
        :param city: The name of the city.
        :param state: The name of the state.
        :param address_zip: The address's zip.
        :param phone_number: The customer's phone number.
        """
        pass

    def delete_customer(self, customer_id):
        """
        To delete a customer.

        To delete a customer. I should only delete one customer in the csv file.

        :param customer_id: The customer's id.
        """
        pass

    def delete_address(self, customer_id):
        """
        To delete an address.

        To delete an address.

        :param customer_id: The customer's id.
        """
        pass

    def get_customer(self):
        """
        To get customers.

        To get customers from the csv file.
        """
        pass

    def get_address(self):
        """
        To get an address.

        To get an address.
        """
        pass

    def get_first_customer_address(self):
        """
        To get the first customer with their first address.

        To get the first customer with their first address.
        """
        pass

    def get_last_customer_address(self):
        """
        To get the last customer with their last address.

        To get the last customer with their last address.
        """
        pass

    def get_desc_customer_addresses(self):
        """
        To get the customer with their addresses in descending order.

        To get the customer with their addresses in descending order.
        """
        pass

    def update_customer(self, customer_id, first_name, last_name):
        """
        To update a customer's data.

        To update a customer's data.

        :param customer_id: The id for the customer.
        :param first_name: The customer's first name.
        :param last_name: The customer last name.
        """
        pass

    def update_address(self, address_id, street, city, state, address_zip, phone_number):
        """
        To update an address.

        To update an address.

        :param address_id: The id for an address.
        :param street: The name of the street.
        :param city: The name of the city.
        :param state: The name of the state.
        :param address_zip: The address's zip.
        :param phone_number: The customer's phone number.
        """
        pass

    def get_customer_address_id(self, customer_id):
        """
        To get a customer with its address.

        To get a customer with its address based on its given id.

        :param customer_id: The id for a customer.
        """
        pass


class SqliteDAO(DAO):
    DATABASE = 'customers.sqlite'

    INSERT_A_CUSTOMER = '''INSERT INTO customers(first_name, last_name)
                          VALUES (?, ?)'''

    INSERT_A_ADDRESS = '''INSERT INTO addresses(customer_id, street, city, state, zip, phone_number)
                        VALUES (?, ?, ?, ?, ?, ?)'''

    GET_CUSTOMERS = '''SELECT id, first_name, last_name
                        FROM customers'''

    GET_CUSTOMER_BY_ID = '''SELECT c.id, c.first_name, c.last_name, a.id as 'address_id', a.customer_id,
                            a.street, a.city, a.state, a.zip, a.phone_number
                            FROM customers as c JOIN addresses as a
                            WHERE c.id = a.customer_id AND c.id = ?
                            ORDER BY c.id ASC, address_id ASC'''

    GET_ADDRESSES = '''SELECT id, customer_id, street, city, state, zip, phone_number
                      FROM addresses'''

    GET_FIRST_CUSTOMER_ADDRESS = '''SELECT c.id, c.first_name, c.last_name, a.id as 'address_id', 
                                    a.customer_id, a.street, a.city, a.state, a.zip, a.phone_number
                                    FROM customers as c JOIN addresses as a
                                    WHERE c.id = a.customer_id
                                    ORDER BY c.id ASC, address_id ASC
                                    LIMIT 1'''

    GET_LAST_CUSTOMER_ADDRESS = '''SELECT c.id, c.first_name, c.last_name, a.id as 'address_id', 
                                   a.customer_id, a.street, a.city, a.state, a.zip, a.phone_number
                                   FROM customers as c JOIN addresses as a
                                   WHERE c.id = a.customer_id
                                   ORDER BY c.id DESC, address_id DESC
                                   LIMIT 1'''

    GET_ASC_CUSTOMER_ADDRESSES = '''SELECT c.id, c.first_name, c.last_name, a.id as 'address_id', a.customer_id,
                                a.street, a.city, a.state, a.zip, a.phone_number
                                FROM customers as c JOIN addresses as a
                                WHERE c.id = a.customer_id
                                ORDER BY c.id ASC, address_id ASC'''

    GET_DESC_CUSTOMER_ADDRESSES = '''SELECT c.id, c.first_name, c.last_name, a.id as 'address_id', a.customer_id,
                                    a.street, a.city, a.state, a.zip, a.phone_number
                                    FROM customers as c JOIN addresses as a
                                    WHERE c.id = a.customer_id
                                    ORDER BY c.id DESC, address_id DESC'''

    DELETE_A_CUSTOMER = '''DELETE FROM customers
                          WHERE id = ?'''

    DELETE_AN_ADDRESS = '''DELETE FROM addresses
                              WHERE customer_id = ?'''

    UPDATE_CUSTOMER = '''UPDATE customers
                         SET first_name = ?, last_name = ?
                         WHERE id = ?'''

    UPDATE_ADDRESS = '''UPDATE addresses
                        SET street = ?, city = ?, state = ?, zip = ?, phone_number = ?
                        WHERE id = ?'''

    __connection: Connection = None

    def __init__(self, connection):
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param connection: To get a connection to sqlite.
        """
        self.__connection = connection

    def insert_customer(self, first_name, last_name):
        """
        To insert a customer.

        To insert a customer. I assume the customer id will auto increment.

        :param first_name: The customer's first name.
        :param last_name: The customer's last name.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.INSERT_A_CUSTOMER, (first_name, last_name))
                conn.commit()

    def insert_an_address(self, customer_id, street, city, state, address_zip, phone_number):
        """
        To insert an address.

        To insert an address. I assume address id will auto increment.

        :param customer_id: The customer's id.
        :param street: The name of a street.
        :param city: The name of a city.
        :param state: The name of a state.
        :param address_zip: The address's zip.
        :param phone_number: The customer's phone number.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.INSERT_A_ADDRESS, (customer_id, street, city, state, address_zip, phone_number))
                conn.commit()

    def delete_customer(self, customer_id):
        """
        To delete a customer.

        To delete a customer with a given customer id.

        :param customer_id: The id for a customer.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.DELETE_A_CUSTOMER, (customer_id,))
                conn.commit()

    def delete_address(self, customer_id):
        """
        To delete address(es).

        To delete address(es) with a given customer id.

        :param customer_id:The id for a customer.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.DELETE_AN_ADDRESS, (customer_id,))
                conn.commit()

    def get_customer(self):
        """
        To get customers.

        To get customers. Each customer will be put into as a Customer object.

        :return: A list of Customers.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_CUSTOMERS)
                results = c.fetchall()
        customers = []
        for row in results:
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customers.append(customer)
        return customers

    def get_first_customer_address(self):
        """
        To get the first customer with their first address.

        To get the first customer with their first address. A customer will have a Customer object.
        An address will have an Address object.

        :return: Customer with a list of address.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_FIRST_CUSTOMER_ADDRESS)
                results = c.fetchall()
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["address_id"])
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customer.append(address)
            return customer

    def get_last_customer_address(self):
        """
        To get the last customer with their last address.

        To get the last customer with their last address. A customer will have a Customer object.
        An address will have an Address object.

        :return: Customer with a list of address.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_LAST_CUSTOMER_ADDRESS)
                results = c.fetchall()
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["address_id"])
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customer.append(address)
            return customer

    def get_address(self):
        """
        To get addresses.

        To get addresses. Each address will have an Address object.

        :return: A list of Address.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_ADDRESSES)
                results = c.fetchall()
        addresses = []
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["id"])
            addresses.append(address)
        return addresses

    def get_asc_customer_addresses(self):
        """
        To get the ascending order of customer address.

        To get the ascending order of customer address. Each address will have an Address object.
        Each customer will have a Customer object.

        :return: A list of customers.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_ASC_CUSTOMER_ADDRESSES)
                results = c.fetchall()
        customers = []
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["address_id"])
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customer.append(address)
            customers.append(customer)
        return customers

    def get_desc_customer_addresses(self):
        """
        To get the descending order of customer addresses.

        To get the descending order of customer addresses. Each address will have an Address object.
        Each customer will have a Customer object.
        :return: A list of customers.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_DESC_CUSTOMER_ADDRESSES)
                results = c.fetchall()
        customers = []
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["address_id"])
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customer.append(address)
            customers.append(customer)
        return customers

    def update_customer(self, customer_id, first_name, last_name) -> None:
        """
        To update a customer data.

        To update a customer data. Customer id is use for to found the customer.
        Their first and last name may change.

        :param customer_id: The id for a customer.
        :param first_name: The first name of a customer.
        :param last_name: The last name of a customer.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.UPDATE_CUSTOMER, (first_name, last_name, customer_id))
                conn.commit()

    def update_address(self, address_id, street, city, state, address_zip, phone_number) -> None:
        """
        To update an address.

        To update an address. Address id is use for to find the address in the sqlite database.
        Any given data beside address id may change.

        :param address_id: The id for an address.
        :param street: The name of a street.
        :param city: The name of a city.
        :param state: The name of a state.
        :param address_zip: The address's zip.
        :param phone_number: The customer's phone number.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.UPDATE_ADDRESS, (street, city, state, address_zip, phone_number, address_id))
                conn.commit()

    def export_file(self, customers):
        """
        To export a file.

        To export a file.

        :param customers: A list of customers.
        """
        pass

    def get_customer_address_id(self, customer_id):
        """
        To get a customer with their addresses.

        To get a customer with their addresses with the given customer id.

        :param customer_id: An id for a customer
        :return: A list of customer.
        """
        with self.__connection.get_connection() as conn:
            with closing(conn.cursor()) as c:
                c.execute(self.GET_CUSTOMER_BY_ID, (customer_id,))
                results = c.fetchall()
        customers = []
        for row in results:
            address = objects.Address(row["customer_id"], row["street"], row["city"], row["state"],
                                      row["zip"], row["phone_number"], row["address_id"])
            customer = objects.Customer(row["first_name"], row["last_name"], row["id"])
            customer.append(address)
            customers.append(customer)
        return customers
