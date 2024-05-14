# HW4 - Customers    Oswaldo Flores
"""
Handles the GUI, input, and output.

To design what the GUI program should look like to the user. The GUI determine how the inputs
and outputs should function.

STANDARD_EMTPY_LIST: The list is an empty string.
STANDARD_FIRST_NAME: The customer's first name in a list.
STANDARD_LAST_NAME: The customer's last name in a list.
STANDARD_STREET: The customer's street in a list.
STANDARD_CITY: The customer's city in a list.
STANDARD_STATE: The customer's state in a list.
STANDARD_ZIP: The customer's zip in a list.
STANDARD_PHONE_STATEMENT: The customer's phone number in a list.
STANDARD_STATE_STR_LEN: A string length for a state's abbreviation name.
MINIMUM_PHONE_NUMBER: The minimum of what a phone number can be.
MAXIMUM_PHONE_NUMBER: The maximum of what a phone number can be.
MINIMUM_ZIP: The minimum of what a zip can be.
MAXIMUM_ZIP = The maximum of what a zip can be.
"""

import tkinter as tk
from dataclasses import dataclass
from objects import Customer, CustomerList, Address, AddressList
from tkinter import ttk, messagebox

STANDARD_EMTPY_LIST = 0
STANDARD_FIRST_NAME = 0
STANDARD_LAST_NAME = 1
STANDARD_STREET = 2
STANDARD_CITY = 3
STANDARD_STATE = 4
STANDARD_ZIP = 5
STANDARD_PHONE_STATEMENT = 6
STANDARD_STATE_STR_LEN = 2
MINIMUM_PHONE_NUMBER = 1111111111
MAXIMUM_PHONE_NUMBER = 9999999999
MINIMUM_ZIP = 11111
MAXIMUM_ZIP = 99999


@dataclass
class CustomerForm:
    __customer_id_entry: ttk.Entry
    __first_name_entry: ttk.Entry
    __last_name_entry: ttk.Entry
    __address_id_entry: ttk.Entry
    __street_entry: ttk.Entry
    __city_entry: ttk.Entry
    __state_entry: ttk.Entry
    __zip_entry: ttk.Entry
    __phone_number_entry: ttk.Entry

    def __init__(self):
        """
        To run an operation when the program runs.

        What the GUI should look like when the program runs. To assign values to the object fields.
        To wire the buttons to its event handlers.
        """
        root = tk.Tk()
        root.title('Customer Form')
        root.geometry('380x340')

        ttk.Label(root, text='Customer ID').grid(row=1, column=1, pady=2)
        self.__customer_id_entry = ttk.Entry(root)
        self.__customer_id_entry.grid(row=1, column=2)

        ttk.Label(root, text='First Name').grid(row=2, column=1, pady=10)
        self.__first_name_entry = ttk.Entry(root)
        self.__first_name_entry.grid(row=2, column=2)

        ttk.Label(root, text='Last Name').grid(row=3, column=1)
        self.__last_name_entry = ttk.Entry(root)
        self.__last_name_entry.grid(row=3, column=2)

        ttk.Label(root, text='Address ID').grid(row=4, column=1, pady=10)
        self.__address_id_entry = ttk.Entry(root)
        self.__address_id_entry.grid(row=4, column=2)

        ttk.Label(root, text='Street').grid(row=5, column=1)
        self.__street_entry = ttk.Entry(root)
        self.__street_entry.grid(row=5, column=2)

        ttk.Label(root, text='City').grid(row=6, column=1, pady=10)
        self.__city_entry = ttk.Entry(root)
        self.__city_entry.grid(row=6, column=2)

        ttk.Label(root, text='State').grid(row=7, column=1)
        self.__state_entry = ttk.Entry(root)
        self.__state_entry.grid(row=7, column=2)

        ttk.Label(root, text='ZIP').grid(row=8, column=1, pady=10)
        self.__zip_entry = ttk.Entry(root)
        self.__zip_entry.grid(row=8, column=2)

        ttk.Label(root, text='Phone Number').grid(row=9, column=1)
        self.__phone_number_entry = ttk.Entry(root)
        self.__phone_number_entry.grid(row=9, column=2)

        first_customer = ttk.Button(root, text='First Customer', command=self.first_customer_button_handler)
        first_customer.grid(row=10, column=1, pady=10)

        last_customer = ttk.Button(root, text='Last Customer', command=self.last_customer_button_handler)
        last_customer.grid(row=10, column=2)

        add = ttk.Button(root, text='Add', command=self.add_button_handler)
        add.grid(row=10, column=3, padx=5)

        delete = ttk.Button(root, text='Delete', command=self.delete_button_handler)
        delete.grid(row=10, column=4)

        previous = ttk.Button(root, text='Previous', command=self.previous_button_handler)
        previous.grid(row=11, column=1)

        next_customer = ttk.Button(root, text='Next', command=self.next_button_handler)
        next_customer.grid(row=11, column=2)

        update = ttk.Button(root, text='Update', command=self.update_button_handler)
        update.grid(row=9, column=4)

        import_customers = ttk.Button(root, text='Import', command=self.import_button_handler)
        import_customers.grid(row=11, column=3)

        export_customers = ttk.Button(root, text='Export', command=self.export_button_handler)
        export_customers.grid(row=11, column=4)

        root.mainloop()

    def export_button_handler(self) -> None:
        """
        When the user presses the export button.

        If the user does not give a value to customer id, all the data in the Sqlite
        will be export to csv file. If the user give a customer id, export the customer and all of their
        address to a csv file. If a customer id does not have data, do not export anything. Display to the
        that nothing happen. If a customer id is a string or a character, do not export anything.
        Display to the user that nothing happen. Exporting data should not happen here, it should happen in
        the db module.
        """
        customer_id = self.__customer_id_entry.get()
        if customer_id == '':
            self.export_all()
        elif self.is_an_integer(customer_id):
            customers = CustomerList()
            customers.load_customer_address_id(int(customer_id))
            if len(customers) == STANDARD_EMTPY_LIST:
                messagebox.showerror('Error', 'Nothing was Exported')
            else:
                self.export_a_customer_data(customers)
        else:
            messagebox.showerror('Error', 'Nothing was Exported')

    def import_button_handler(self) -> None:
        """
        When the user presses the import button.

        To get data from a csv file and import the data to Sqlite. I assume every customer
        is unique. I assume that every customer will have an address assign to them. I assume
        the customer information is correct. Importing data should not happen here. It should
        happen in the db module.
        """
        customers = CustomerList()
        customers.dao = customers.IMPORT_FILE_PROVIDER
        customers.load_asc_customer_address()
        for new_customer in customers:
            customer_data = str(new_customer).split(',')
            self.new_customer_and_address(customer_data[STANDARD_FIRST_NAME].upper(),
                                          customer_data[STANDARD_LAST_NAME].upper().strip(),
                                          customer_data[STANDARD_STREET].upper().strip(),
                                          customer_data[STANDARD_CITY].upper().strip(),
                                          customer_data[STANDARD_STATE].upper().strip(),
                                          customer_data[STANDARD_ZIP].strip(),
                                          customer_data[STANDARD_PHONE_STATEMENT].strip())

    def update_button_handler(self) -> None:
        """
        When the user presses the update button.

        To update a customer and their address. Validate the all user entries. Validate
        if customer id and address id exist. If customer id and address id does not exist,
        display the user that the data they enter is incorrect. After every successful update,
        the form should be clear.
        """
        customer_id = self.__customer_id_entry.get()
        first_name = self.__first_name_entry.get()
        last_name = self.__last_name_entry.get()
        address_id = self.__address_id_entry.get()
        street = self.__street_entry.get()
        city = self.__city_entry.get()
        state = self.__state_entry.get()
        address_zip = self.__zip_entry.get()
        phone_number = self.__phone_number_entry.get()
        if self.is_an_integer(customer_id) and self.is_characters_only(first_name) and \
                self.is_characters_only(last_name) and self.is_an_integer(address_id) and \
                self.is_street(street) and self.is_characters_only(city) and self.is_state(state) \
                and self.is_zip(address_zip) and self.is_phone_number(phone_number):
            customer_address_exist = self.does_customer_address_exist(customer_id, address_id)
            if customer_address_exist:
                Customer.set_customer(customer_id, first_name.upper(), last_name.upper())
                Address.set_address(address_id, street.upper(), city.upper(), state.upper(),
                                    address_zip, phone_number)
                self.clear_the_form()
                messagebox.showinfo('Update', 'Update Successfully')
            else:
                messagebox.showerror('Error', 'Invalid IDs')

        else:
            messagebox.showerror('Error', 'Invalid Data')

    def previous_button_handler(self) -> None:
        """
        When the user presses the previous button.

        Move back by one customer in descending order. Customer id and address id
        should be validated. If a customer has more than one address, iterator through
        their addresses as well. I assume every customer has at least one address.
        """
        customer_id = self.__customer_id_entry.get()
        address_id = self.__address_id_entry.get()
        customers = CustomerList()
        customers.load_desc_customer_address()
        on_customer_address = False
        on_previous_customer = False
        if self.is_an_integer(customer_id) and self.is_an_integer(address_id):
            for customer in customers:
                for address in customer.get_address():
                    if on_customer_address and on_previous_customer:
                        self.insert_to_entry(customer, address)
                        on_customer_address = False
                        on_previous_customer = False
                    if int(customer_id) in customers and int(address_id) in address:
                        on_previous_customer = True
                        on_customer_address = True
        else:
            messagebox.showerror('Error', 'Invalid IDs')

    def next_button_handler(self) -> None:
        """
        When the user presses the next button.

        Move forward customer by one in ascending order. Customer id and address id should
        be validated. If a customer has more than one address, iterator through their addresses
        as well. I assume every customer has at least one address.
        """
        customer_id = self.__customer_id_entry.get()
        address_id = self.__address_id_entry.get()
        customers = CustomerList()
        customers.load_asc_customer_address()
        on_customer_address = False
        on_next_customer = False
        if self.is_an_integer(customer_id) and self.is_an_integer(address_id):
            for customer in customers:
                for address in customer.get_address():
                    if on_customer_address and on_next_customer:
                        self.insert_to_entry(customer, address)
                        on_customer_address = False
                        on_next_customer = False
                    if int(customer_id) in customers and int(address_id) in address:
                        on_next_customer = True
                        on_customer_address = True
        else:
            messagebox.showerror('Error', 'Invalid IDs')

    def first_customer_button_handler(self) -> None:
        """
        When the user presses the first customer button.

        To display the first customer information to the user. At least one
        customer must exist to display data. If no customer exist, display to the user
        that no customer was found. Before outputting the first customer, the form must be clear
        of data.
        """
        self.clear_the_form()
        first_customer = Customer()
        try:
            first_customer.load_first_customer()
            self.__customer_id_entry.insert(0, first_customer.get_id())
            self.__first_name_entry.insert(0, first_customer.get_first_name())
            self.__last_name_entry.insert(0, first_customer.get_last_name())
            for address in first_customer.get_address():
                self.__address_id_entry.insert(0, address.get_address_id())
                self.__street_entry.insert(0, address.get_street())
                self.__city_entry.insert(0, address.get_city())
                self.__state_entry.insert(0, address.get_state())
                self.__zip_entry.insert(0, address.get_zip())
                self.__phone_number_entry.insert(0, address.get_phone_number())
        except:
            messagebox.showerror('Error', 'No customer found')

    def last_customer_button_handler(self) -> None:
        """
        When the user presses the last customer button.

        To display the last customer information to the user. At least one
        customer must exist to display data. If no customer exist, display to the user
        that no customer was found. Before outputting the last customer, the form must be clear
        of data.
        """
        self.clear_the_form()
        last_customer = Customer()
        try:
            last_customer.load_last_customer()
            self.__customer_id_entry.insert(0, last_customer.get_id())
            self.__first_name_entry.insert(0, last_customer.get_first_name())
            self.__last_name_entry.insert(0, last_customer.get_last_name())
            for address in last_customer.get_address():
                self.__address_id_entry.insert(0, address.get_address_id())
                self.__street_entry.insert(0, address.get_street())
                self.__city_entry.insert(0, address.get_city())
                self.__state_entry.insert(0, address.get_state())
                self.__zip_entry.insert(0, address.get_zip())
                self.__phone_number_entry.insert(0, address.get_phone_number())
        except:
            messagebox.showerror('Error', 'No customer found')

    def add_button_handler(self) -> None:
        """
        When the user presses the add button.

        Validate all entries. If a customer and address does not exist, add all data to
        sqlite database. If a customer exist and address does not exist, add the address
        to the sqlite database. If a customer and address already exist, do not add anything
        to the database. Adding data to sqlite should be handled by the db module.
        """
        customer_id = self.__customer_id_entry.get()
        first_name = self.__first_name_entry.get()
        last_name = self.__last_name_entry.get()
        address_id = self.__address_id_entry.get()
        street = self.__street_entry.get()
        city = self.__city_entry.get()
        state = self.__state_entry.get()
        address_zip = self.__zip_entry.get()
        phone_number = self.__phone_number_entry.get()
        if self.is_an_integer(customer_id) and self.is_characters_only(first_name) and \
                self.is_characters_only(last_name) and self.is_an_integer(address_id) and \
                self.is_street(street) and self.is_characters_only(city) and self.is_state(state) \
                and self.is_zip(address_zip) and self.is_phone_number(phone_number):
            customers = CustomerList()
            customers.load_customers()
            is_customer_id_match = customers.does_id_exist(customer_id)
            if is_customer_id_match:
                self.new_address(address_id, customer_id, street, city, state, address_zip, phone_number)
            else:
                self.new_customer_and_address(first_name, last_name, street, city, state, address_zip,
                                              phone_number)
        else:
            messagebox.showerror('Error', 'Invalid Data')

    def delete_button_handler(self) -> None:
        """
        When the user presses the delete button.

        Delete a customer with their address using their customer id.
        Validate customer id. If the customer id is validated delete a customer
        and their addresses. If the delete button was not successful, display it to the user.
        Once a customer is successfully deleted, clear the form.
        """
        customer_id = self.__customer_id_entry.get()
        if self.is_an_integer(customer_id):
            customers = CustomerList()
            customers.load_customers()
            does_customer_exist = customers.does_id_exist(customer_id)
            if does_customer_exist:
                a_customer = Customer()
                a_customer.remove_customer(int(customer_id))
                a_address = Address()
                a_address.remove_address(int(customer_id))
                messagebox.showinfo('Success', 'Customer was Deleted')
                self.clear_the_form()
            else:
                messagebox.showerror('Error', 'Enter a valid customer id')
                self.clear_the_form()
        else:
            messagebox.showerror('Error', 'Enter a valid customer id')
            self.clear_the_form()

    def new_customer_and_address(self, first_name: str, last_name: str, street: str, city: str, state: str,
                                 address_zip: str, phone_number: str) -> None:
        """
        For adding a new customer and a new address.

        To shorten the code in the add_button_handler. To add a new customer and a new address.
        Adding data in the database will be in the db module. Clear the form after adding the data.

        :param first_name: A customer's first name.
        :type first_name: str
        :param last_name: A customer's last name.
        :type last_name: str
        :param street: The street name for a customer.
        :type street: str
        :param city: The city name for a customer.
        :type city: str
        :param state: The state name for a customer.
        :type state: str
        :param address_zip: An address zip for a customer.
        :type address_zip: str
        :param phone_number: The phone number for a customer.
        :type phone_number: str
        """
        a_customer = Customer(first_name.upper(), last_name.upper())
        a_customer.new_customer()
        customers = CustomerList()
        customers.load_customers()
        last_customer = customers.get_last_customer_id()
        a_address = Address(last_customer, street.upper(), city.upper(),
                            state.upper(), address_zip, phone_number)
        a_address.new_address()
        messagebox.showinfo('Added', 'Customer and Address was Added')
        self.clear_the_form()

    def new_address(self, address_id: str, customer_id: str, street: str, city: str,
                    state: str, address_zip: str, phone_number: str) -> None:
        """
        For adding a new address.

        To shorten the code in the add_button_handler. To add a new address from an already
        existing customer. Adding the data will happen in the db module. If an address already
        exist, display it to the user.

        :param address_id: The id for address.
        :type address_id: str
        :param customer_id: The id for a customer.
        :type customer_id: str
        :param street: The street name for a customer.
        :type street: str
        :param city: The city name for a customer.
        :type city: str
        :param state: The state name for a customer.
        :type state: str
        :param address_zip: An address zip for a customer.
        :type address_zip: str
        :param phone_number: The phone number for a customer.
        :type phone_number: str
        """
        addresses = AddressList()
        addresses.load_address()
        is_address_id_match = addresses.does_address_id_exist(address_id)
        if is_address_id_match:
            messagebox.showinfo('Exist', 'Customer and Address Already Exist')
        else:
            a_address = Address(int(customer_id), street.upper(), city.upper(),
                                state.upper(), address_zip, phone_number)
            a_address.new_address()
            messagebox.showinfo('Half Exist', 'Customer Already Exist Address was Added')
            self.clear_the_form()

    def clear_the_form(self) -> None:
        """
        To clear the form.

        To clear the form from any data. The labels in the form should not be deleted
        only the entries of the form.
        """
        self.__customer_id_entry.delete(0, tk.END)
        self.__first_name_entry.delete(0, tk.END)
        self.__last_name_entry.delete(0, tk.END)
        self.__address_id_entry.delete(0, tk.END)
        self.__street_entry.delete(0, tk.END)
        self.__city_entry.delete(0, tk.END)
        self.__state_entry.delete(0, tk.END)
        self.__zip_entry.delete(0, tk.END)
        self.__phone_number_entry.delete(0, tk.END)

    def is_zip(self, invalid_number: str) -> bool:
        """
        To validate zip.

        Zip must be a number. Zip must be within the minimum and maximum of zip.

        :param invalid_number: Invalid value of zip.
        :type invalid_number: str
        :return: True if zip is a number and within the limits. False if it is not a number or within
        the limits.
        """
        if invalid_number.isdigit():
            if MINIMUM_ZIP <= int(invalid_number) <= MAXIMUM_ZIP:
                return True
        return False

    def is_state(self, invalid_string: str) -> bool:
        """
        To validate state.

        State must contain characters only. State must only contain two characters.

        :param invalid_string: Invalid name of a state.
        :type invalid_string: str
        :return: True when it contains two characters. False when it does not contain characters or
        if the character count is more than two.
        """
        if self.is_characters_only(invalid_string):
            if len(invalid_string) == STANDARD_STATE_STR_LEN:
                return True
        return False

    def is_phone_number(self, invalid_number: str) -> bool:
        """
        To validate phone number.

        Make should the invalid number contains numbers only and the number is within the minimum
        and maximum of phone number.
        :param invalid_number: The unvalidated phone number.
        :type invalid_number: str
        :return: True if the invalid number is a number and is within the limits. False
        if the invalid number contains characters and is not within the limits.
        """
        if invalid_number.isdigit():
            if MINIMUM_PHONE_NUMBER <= int(invalid_number) <= MAXIMUM_PHONE_NUMBER:
                return True
        return False

    def is_street(self, invalid_string: str) -> bool:
        """
        To validate street.

        Street must not be emtpy. Street can contain numbers and characters.
        :param invalid_string: The unvalidated street.
        :type invalid_string: str
        :return: True if the string is not empty. False if the string is empty.
        """
        if invalid_string == '':
            return False
        return True

    def is_an_integer(self, invalid_number: str) -> bool:
        """
        To validate if a value is an integer.

        To validate that a string or number is an integer.
        :param invalid_number: The unvalidated integer.
        :type invalid_number: str
        :return: True if the value is an integer. False if the value is
        anything else.
        """
        try:
            an_integer = int(invalid_number)
        except:
            return False
        return True

    def is_characters_only(self, invalid_string: str) -> bool:
        """
        To validate a string.

        To make sure a string contains characters only. To make sure the
        string is not empty.
        :param invalid_string: The unvalidated string.
        :type invalid_string: str
        :return: True if it contains characters only. False if it does not contain characters only.
        """
        if invalid_string == '':
            return False
        for character in invalid_string:
            if character.isdigit():
                return False
        return True

    def insert_to_entry(self, customer: Customer, address: Address) -> None:
        """
        To insert data into the form.

        The form must be clear first to enter any data. Then enter the data into
        the form.
        :param customer: Holds a customer data.
        :type customer: Customer
        :param address: Holds an address data.
        :type address: Address
        """
        self.clear_the_form()
        self.__customer_id_entry.insert(0, customer.get_id())
        self.__first_name_entry.insert(0, customer.get_first_name())
        self.__last_name_entry.insert(0, customer.get_last_name())
        self.__address_id_entry.insert(0, address.get_address_id())
        self.__street_entry.insert(0, address.get_street())
        self.__city_entry.insert(0, address.get_city())
        self.__state_entry.insert(0, address.get_state())
        self.__zip_entry.insert(0, address.get_zip())
        self.__phone_number_entry.insert(0, address.get_phone_number())

    def does_customer_address_exist(self, customer_id: str, address_id: str) -> bool:
        """
        To validated customer and address id.

        To make sure that both customer id and address id exist within the data.
        :param customer_id: The id for a customer.
        :type customer_id: str
        :param address_id: The id for an address.
        :type address_id: str
        :return: True if both IDs exist. False if either IDs does not exist.
        """
        customers = CustomerList()
        customers.load_customers()
        is_customer_id_match = customers.does_id_exist(customer_id)
        addresses = AddressList()
        addresses.load_address()
        is_address_id_match = addresses.does_address_id_exist(address_id)
        if is_customer_id_match and is_address_id_match:
            return True
        return False

    def export_all(self) -> None:
        """
        To export all data.

        To shorten the code in the export_button_handler. To export all the data from the sqlite
        into a csv file. To exporting data should be handled in the db module. If no data exist,
        display it to the user.
        """
        customers = CustomerList()
        customers.load_asc_customer_address()
        customer_list = []
        if len(customers) != STANDARD_EMTPY_LIST:
            for customer in customers:
                customer_string = str(customer)
                customer_list.append(customer_string)
            customers.dao = customers.EXPORT_FILE_PROVIDER
            customers.to_different_file(customer_list)
        else:
            messagebox.showinfo('No Export', 'Nothing was Exported')

    def export_a_customer_data(self, customers: CustomerList) -> None:
        """
        To export a customer with their addresses.

        To shorten the code in export_button_handler. To export a customer with their addresses.
        Exporting the file will get handled by the db module.

        :param customers: Customer with their addresses.
        :type customers: CustomerList
        """
        customer_list = []
        for customer in customers:
            customer_string = str(customer)
            customer_list.append(customer_string)
        customers.dao = customers.EXPORT_FILE_PROVIDER
        customers.to_different_file(customer_list)
