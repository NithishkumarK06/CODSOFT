class MyContact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class MyContactBook:
    def __init__(self):
        self.contacts = []

    def add_To_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact for {contact.name} added to My contact book.")

    def view_My_contacts(self):
        if not self.contacts:
            print("Here My contact list is empty.")
        else:
            print("MyContact List:")
            for contact in self.contacts:
                print(f"Name: {contact.name}, Phone_no: {contact.phone_number}")

    def search_My_contact(self, search_term):
        results = []
        for contact in self.contacts:
            if (
                search_term.lower() in contact.name.lower()
                or search_term in contact.phone_number
            ):
                results.append(contact)
        if results:
            print("Searched Contacts:")
            for contact in results:
                print(f"Name: {contact.name}, Phone_no: {contact.phone_number}")
        else:
            print("Sorry . There is no Contact You Mentiond")

    def update_My_contact(self, name, new_contact):
        for contact in self.contacts:
            if contact.name == name:
                contact.name = new_contact.name
                contact.phone_number = new_contact.phone_number
                contact.email = new_contact.email
                contact.address = new_contact.address
                print(f"Contact for {name} It's updated.")
                return
        print(f"Sorry . No contact found in mentioned name {name}.")

    def delete_My_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact for {name} It's deleted.")
                return
        print(f"Sorry . No contact found in mentioned name {name}.")

def main():
    contact_book = MyContactBook()

    while True:
        print("\nYour PhoneBook :)")
        print("1. Add MyContact")
        print("2. View MyContacts")
        print("3. Search MyContact")
        print("4. Update My New Contact")
        print("5. Delete MyContact")
        print("6. Exit")

        choice = input("Mention your choice: ")

        if choice == "1":
            name = input("Mention His/Her name: ")
            phone_number = input("Mention His/Her phone number: ")
            email = input("Mention His/Her email * (optional): ")
            address = input("Mention His/Her address * (optional): ")
            contact = MyContact(name, phone_number, email, address)
            contact_book.add_To_contact(contact)
        elif choice == "2":
            contact_book.view_My_contacts()
        elif choice == "3":
            search_term = input("Mention The name or phone number to search for: ")
            contact_book.search_My_contact(search_term)
        elif choice == "4":
            name = input("Mention His/Her name to Update in Contact: ")
            new_name = input("Mention His/Her new name (leave empty to keep the same): ")
            new_phone = input("Mention His/Her new phone number (leave empty to keep the same): ")
            new_email = input("Mention His/Her new email (leave empty to keep the same): ")
            new_address = input("Mention His/Her new address (leave empty to keep the same): ")
            new_contact = MyContact(new_name, new_phone, new_email, new_address)
            contact_book.update_My_contact(name, new_contact)
        elif choice == "5":
            name = input("Mention His/Her name to Delete : ")
            contact_book.delete_My_contact(name)
        elif choice == "6":
            print("See You Soon With New Friendly Contast's")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
