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
  all_contacts: ContactList = []
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
  c = ContactList()