# HW4 - Customers    Oswaldo Flores
"""
To handle a customer, a list of customers, an address, and a list of addresses.

The Customer class will represent a customer with a list of their addresses. The CustomerList
will represent a list of customers. The Address class will represent an address. The AddressList will
represent a list of addresses.

SQLITE_PROVIDER: To connect to the Sqlite.
IMPORT_FILE_PROVIDER: To connect to the csv.
EXPORT_FILE_PROVIDER: To connect to the csv.
"""
import db as d
from dataclasses import dataclass, field


@dataclass
class Customer:
    SQLITE_PROVIDER = d.SqliteDAO(d.SqliteConnection(d.SqliteDAO.DATABASE))
    __id: int
    __first_name: str
    __last_name: str
    __address: list = field(default_factory=list)
    __dao: d.DAO = SQLITE_PROVIDER

    def __init__(self, first_name: str = '', last_name: str = '', customer_id: int = 0):
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param first_name: A customer first name.
        :type first_name: str
        :param last_name: A customer last name.
        :type last_name: str
        :param customer_id: The id for the customer.
        :type customer_id: int
        """
        self.__id = customer_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = []

    def __getitem__(self) -> int:
        """
        To get a customer's id.

        To get a customer's id.

        :return: The id for the customer.
        """
        return self.__id

    def __str__(self) -> str:
        """
        To set what the object should look.

        To set what the object should look like when called.

        :return: To format what an object should look like to the user.
        """
        address_string = f''
        for address in self.__address:
            address_string = f'{address_string} {address}'
        return f'{self.__first_name}, {self.__last_name}, {address_string}'

    def __eq__(self, rhs: int) -> bool:
        """
        To make sure customer id and rhs id match.

        To match customer id and rhs id.

        :param rhs: The id that might belong to this customer.
        :type rhs: int
        :return: True when IDs match. False when IDs do not match.
        """
        return self.__id == rhs

    def get_id(self) -> int or str:
        """
        To get id.

        To get a customer's id.

        :return: The customer id.
        """
        return self.__id

    def get_first_name(self) -> str:
        """
        To get first name.

        To get a customer's first name.

        :return: Customer's first name.
        """
        return self.__first_name

    def get_last_name(self) -> str:
        """
        To get last name.

        To get a customer's last name.

        :return: Customer's last name.
        """
        return self.__last_name

    def get_address(self) -> list:
        """
        To get the list of addresses.

        To get the list of addresses that belongs to a customer.

        :return: The list of addresses.
        """
        return self.__address

    def append(self, address) -> None:
        """
        To append an address to the address list.

        To append an address to the address list.

        :param address: An address
        """
        self.__address.append(address)

    def new_customer(self) -> None:
        """
        To communicate between the ui and the db module for inserting a new customers.

        To communicate between the ui and the db module. To insert a new customer.
        Any form of the CRUD operations belongs in the db module.
        """
        self.__dao.insert_customer(self.__first_name, self.__last_name)

    def remove_customer(self, customer_id) -> None:
        """
        To communicate between the ui and the db module for removing an existing customer.

        To communicate between the ui and the db module. To remove a customer.
        Any form of the CRUD operations belongs in the db module.
        """
        self.__dao.delete_customer(customer_id)

    def load_first_customer(self) -> None:
        """
        To communicate between the ui and the db module for loading the first customer.

        To communicate between the ui and the db module. To select a customer.
        Any form of the CRUD operations belongs in the db module.
        """
        customer = self.__dao.get_first_customer_address()
        self.__address.clear()
        self.__id = customer.get_id()
        self.__first_name = customer.get_first_name()
        self.__last_name = customer.get_last_name()
        self.__address.extend(customer.get_address())

    def load_last_customer(self) -> None:
        """
        To communicate between the ui and the db module for loading the last customer.

        To communicate between the ui and the db module. To load a customer.
        Any form of the CRUD operations belongs in the db module.
        """
        customer = self.__dao.get_last_customer_address()
        self.__address.clear()
        self.__id = customer.get_id()
        self.__first_name = customer.get_first_name()
        self.__last_name = customer.get_last_name()
        self.__address.extend(customer.get_address())

    @staticmethod
    def set_customer(customer_id: str, first_name: str, last_name: str) -> None:
        """
        To communicate between the ui and the db module for update a customer.

        To communicate between the ui and the db module. To update a customer.
        Any form of the CRUD operations belongs in the db module.
        """
        Customer.__dao.update_customer(int(customer_id), first_name, last_name)


@dataclass
class CustomerList:
    SQLITE_PROVIDER = d.SqliteDAO(d.SqliteConnection(d.SqliteDAO.DATABASE))
    IMPORT_FILE_PROVIDER = d.CsvDAO(d.CsvConnection(d.CsvDAO.IMPORT_FILE_NAME))
    EXPORT_FILE_PROVIDER = d.CsvDAO(d.CsvConnection(d.CsvDAO.EXPORT_FILE_NAME))
    __customer_list: list[Customer] = field(default_factory=list)
    __dao: d.DAO = SQLITE_PROVIDER

    @property
    def dao(self) -> d.DAO:
        """
        To get the dao.

        To get the dao.

        :return: The dao provider.
        """
        return self.__dao

    @dao.setter
    def dao(self, value: d.DAO) -> None:
        """
        To set the dao.

        To set the old dao with the new dao.

        :param value: The new dao
        :type value: d.DAO
        """
        self.__dao = value

    def __len__(self) -> int:
        """
        To get the length of the list.

        To get the length of the list.

        :return: The length of the list.
        """
        return len(self.__customer_list)

    def __iter__(self):
        """
        To iterate over the list.

        To iterate over the list.

        :yield: A customer.
        """
        for customer in self.__customer_list:
            yield customer

    def __str__(self) -> str:
        """
        To set what the object should look.

        To set what the object should look like when called.

        :return: To format what an object should look like to the user.
        """
        return '\n'.join(map(str, self.__customer_list))

    def get_last_customer_id(self) -> int:
        """
        To get the latest customer id.

        To get the last customer id from the list.

        :return: An id for a customer.
        """
        index = len(self.__customer_list) - 1
        customer_id = self.__customer_list[index].get_id()
        return customer_id

    def load_customers(self) -> None:
        """
        To communicate between the ui and the db module for loading customers.

        To communicate between the ui and the db module. To load customers.
        Any form of the CRUD operations belongs in the db module.
        """
        customers = self.__dao.get_customer()
        self.__customer_list.clear()
        self.__customer_list.extend(customers)

    def load_asc_customer_address(self) -> None:
        """
        To communicate between the ui and the db module for loading customers.

        To communicate between the ui and the db module. To load customers in
        ascending order. Any form of the CRUD operations belongs in the db module.
        """
        customers = self.__dao.get_asc_customer_addresses()
        self.__customer_list.clear()
        self.__customer_list.extend(customers)

    def load_desc_customer_address(self) -> None:
        """
        To communicate between the ui and the db module for loading customers.

        To communicate between the ui and the db module. To load customers in
        descending order. Any form of the CRUD operations belongs in the db module.
        """
        customers = self.__dao.get_desc_customer_addresses()
        self.__customer_list.clear()
        self.__customer_list.extend(customers)

    def load_customer_address_id(self, customer_id: int) -> None:
        """
        To communicate between the ui and the db module for loading customers.

        To communicate between the ui and the db module. To load customers from their ids.
        Any form of the CRUD operations belongs in the db module.
        """
        customers = self.__dao.get_customer_address_id(customer_id)
        self.__customer_list.clear()
        self.__customer_list.extend(customers)

    def does_id_exist(self, customer_id: str) -> bool:
        """
        To make a customer id exist within the list.

        To make a customer is existed within the list.

        :param customer_id: A customer id.
        :type customer_id: str
        :return: True when a match is found. False when a match is not found.
        """
        for customer in self.__customer_list:
            matches = customer == int(customer_id)
            if matches:
                return matches
        return False

    def to_different_file(self, customers) -> None:
        """
        To communicate between the ui and the db module for exporting data.

        To communicate between the ui and the db module. To export data.
        Any form of the CRUD operations belongs in the db module.
        """
        self.__dao.export_file(customers)


@dataclass
class Address:
    SQLITE_PROVIDER = d.SqliteDAO(d.SqliteConnection(d.SqliteDAO.DATABASE))
    __id: int
    __customer_id: int
    __street: str
    __city: str
    __state: str
    __zip: str
    __phone_number: str
    __dao: d.DAO = SQLITE_PROVIDER

    def __init__(self, customer_id: int = 0, street: str = '', city: str = '', state: str = '',
                 customer_zip: str = '', phone_number: str = '',  address_id: int = 0):
        """
        To initialize the object's state.

        To gave default values and values to the fields.

        :param customer_id: The id for a customer.
        :type customer_id: int
        :param street: The name of the street.
        :type street: str
        :param city: The name of the city.
        :type city: str
        :param state: The name of the state.
        :type state: str
        :param customer_zip: The address's zip
        :type customer_zip: str
        :param phone_number: The address phone number.
        :type phone_number: str
        :param address_id: The id for an address
        :type address_id: int
        """
        self.__id = address_id
        self.__customer_id = customer_id
        self.__street = street
        self.__city = city
        self.__state = state
        self.__zip = customer_zip
        self.__phone_number = phone_number

    def __iter__(self):
        """
        To get the address id.

        To get the address id.

        :yield: An address id.
        """
        yield self.__id

    def __getitem__(self) -> int:
        """
        To get an id.

        To get an address id.

        :return: ID for address.
        """
        return self.__id

    def __str__(self) -> str:
        """
        To set what the object should look.

        To set what the object should look like when called.

        :return: To format what an object should look like to the user.
        """
        a_string = f'{self.__street}, {self.__city}, {self.__state}'
        return f'{a_string}, {self.__zip}, {self.__phone_number}'

    def __eq__(self, rhs: int) -> bool:
        """
        To match address id with a rhs id.

        To determine if the ids match.
        :param rhs: An id to match with this class id.
        :type rhs: int
        :return: True if ids match. False if ids does not match.
        """
        return self.__id == rhs

    def get_address_id(self) -> int or str:
        """
        To get address id.

        To get address id.

        :return: An address id.
        """
        return self.__id

    def get_street(self) -> str:
        """
        To get the street name

        To get the street name from this class.

        :return: The name of the street.
        """
        return self.__street

    def get_city(self) -> str:
        """
        To get city.

        To get city from this class.

        :return: The name of the city.
        """
        return self.__city

    def get_state(self) -> str:
        """
        To get the state.

        To get the state name from this class.

        :return: The name of the state in two letters.
        """
        return self.__state

    def get_zip(self) -> str:
        """
        To get zip.

        To get zip from this class.

        :return: The zip.
        """
        return self.__zip

    def get_phone_number(self) -> str:
        """
        To get phone number.

        To get phone number from this class.

        :return: The phone number.
        """
        return self.__phone_number

    def new_address(self) -> None:
        """
        To communicate between the ui and the db module for inserting new data.

        To communicate between the ui and the db module. To insert new data.
        Any form of the CRUD operations belongs in the db module.
        """
        self.__dao.insert_an_address(self.__customer_id, self.__street, self.__city,
                                     self.__state, self.__zip, self.__phone_number)

    def remove_address(self, customer_id: int) -> None:
        """
        To communicate between the ui and the db module for removing data.

        To communicate between the ui and the db module. To remove data.
        Any form of the CRUD operations belongs in the db module.
        """
        self.__dao.delete_address(customer_id)

    @staticmethod
    def set_address(address_id: int or str, street: str, city: str, state: str, address_zip: str,
                    phone_number: str) -> None:
        """
        To communicate between the ui and the db module for updating the data.

        To communicate between the ui and the db module. To update data.
        Any form of the CRUD operations belongs in the db module.
        """
        Address.__dao.update_address(int(address_id), street, city, state, address_zip, phone_number)


class AddressList:
    SQLITE_PROVIDER = d.SqliteDAO(d.SqliteConnection(d.SqliteDAO.DATABASE))
    __address_list: list = field(default_factory=list)
    __dao: d.DAO = SQLITE_PROVIDER

    def __init__(self):
        """
        To initialize the object's state.

        To gave default values and values to the fields.
        """
        self.__address_list = []

    def __len__(self) -> int:
        """
        To get the length of the list.

        To get the length of the list.

        :return: The length of the list.
        """
        return len(self.__address_list)

    def __iter__(self):
        """
        To iterate over the list.

        To iterate over the field list.

        :yield: An address
        """
        for address in self.__address_list:
            yield address

    def __str__(self) -> str:
        """
        To set what the object should look.

        To set what the object should look like when called.

        :return: To format what an object should look like to the user.
        """
        return '\n'.join(map(str, self.__address_list))

    def load_address(self) -> None:
        """
        To communicate between the ui and the db module for loading data.

        To communicate between the ui and the db module. To load data.
        Any form of the CRUD operations belongs in the db module.
        :return:
        """
        address = self.__dao.get_address()
        self.__address_list.clear()
        self.__address_list.extend(address)

    def does_address_id_exist(self, address_id: int or str) -> bool:
        """
        To match the given id with the list that has address id.

        To determine if the given id match with any of the address ids in the list.
        :param address_id: The given id to match with in the list.
        :type address_id: int or str
        :return: True if the ids do match. False if the id does not match.
        """
        for address in self.__address_list:
            matches = address == int(address_id)
            if matches:
                return matches
        return False
