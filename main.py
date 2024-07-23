from name import Name
from phone import Phone
from address_book import AddressBook
from record import Record

if __name__ == "__main__":

    # Test the Field, Name, and Phone classes
    # Creating instances of Name and Phone
    name = Name("John Doe")
    print(name)  # Output: John Doe

    try:
        phone = Phone("1234567890")
        print(phone)  # Output: 1234567890
    except ValueError as e:
        print(e)

    try:
        phone = Phone("1234567")
        print(phone)
    except ValueError as e:
        print(e)  # Output: Invalid phone number format

    # Test the Phone class
    try:
        phone = Phone("1234567890")
        print(phone)  # Output: 1234567890
    except ValueError as e:
        print(e)

    try:
        phone = Phone("1234567")
        print(phone)
    except ValueError as e:
        print(e)  # Output: Invalid phone number format

    # Test the Record class
    # Creating a record for John
    record = Record("John")
    record.add_phone("1234567890")
    record.add_phone("5555555555")
    print(record)  # Output: Contact name: John, phones: 1234567890; 5555555555

    # Editing phone number
    record.edit_phone("1234567890", "1112223333")
    print(record)  # Output: Contact name: John, phones: 1112223333; 5555555555

    # Finding a phone number
    phone = record.find_phone("5555555555")
    print(phone)  # Output: 5555555555

    # Removing a phone number
    record.remove_phone("1112223333")
    print(record)  # Output: Contact name: John, phones: 5555555555

    # Test the AddressBook class
    # Creating an address book
    book = AddressBook()

    # Adding records
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Listing all contacts
    for name, record in book.items():
        print(record)
    # Output:
    # Contact name: John, phones: 1234567890; 5555555555
    # Contact name: Jane, phones: 9876543210

    # Finding and editing a record
    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print(john)
    # Output: Contact name: John, phones: 1112223333; 5555555555

    # Deleting a record
    book.delete("Jane")
    for name, record in book.items():
        print(record)
    # Output: Contact name: John, phones: 1112223333; 5555555555
