from __future__ import annotations

class SingletonMeta(type):
  _instances = {}

  def __call__(cls, *args, **kwargs) -> "SingletonMeta":
    """
    Possible changes to the value of the `__init__` argument do not affect
    the returned instance.
    """
    if cls not in cls._instances:
      instance = super().__call__(*args, **kwargs)
      cls._instances[cls] = instance
    return cls._instances[cls]

class ContactList(list["Contact"], metaclass=SingletonMeta):
  def search(self, name: str) -> list["Contact"]:
    matching_contacts: list["Contact"] = []
    for contact in self:
      if name in contact.name:
        matching_contacts.append(contact)
    return matching_contacts

class Contact:
  all_contacts: ContactList = ContactList()
  def __init__(self, name: str, email: str) -> None:
    self.name = name
    self.email = email
    Contact.all_contacts.append(self)
  
  def __repr__(self) -> str:
    return (
      f"{self.__class__.__name__}("
      f"{self.name!r}, {self.email!r}"
      f")"
    )
  

if __name__ == "__main__":
  c = Contact("John Doe", "johndoe@gmail.com")
  d = Contact("Mary Jane", "mary_jane@outlook.de")
  print("Contact.all_contacts:")
  print(Contact.all_contacts)

  print("\nc.all_contacts:")
  print(c.all_contacts)
  print(f"id of Contact.all_contacts {id(Contact.all_contacts)}" +
        f" - id of c.all_contacts {id(c.all_contacts)}")
  
  print("\nCreating new ContactList contact_list")
  contact_list = ContactList()
  print(f"id of new ContactList: {id(contact_list)}")

  print("\nAppend non-contact 'abcdef' to contact list")
  c.all_contacts.append("abcdef") # we append a non-contact
  print("\nc.all_contacts:")
  print(c.all_contacts)
  print("\ncontact_list:")
  print(contact_list)
