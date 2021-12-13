# A simple contacts class
import unittest


class ContactsBook:

    def __init__(self):
        self.contacts = self.setupContacts()

    def setupContacts(self):
        """The key is a person's name. The value in each case is
           a 3-tuple with (email,position,extension)"""
        return \
            {'jane': ('jane@acme.com', 'manager', 1546), \
             'rod': ('rod@acme.com', 'programmer', 8724), \
             'freddy': ('freddy@acme.com', 'support', 8524)}

    def listAllContacts(self):
        """Iterate through the dictionary to show all contacts"""
        for k, v in self.contacts.items():
            email, position, extension = v
            print(f'{k}: email: {email}, position: {position}, ext: {extension}')

    def getNumberOfContacts(self) -> object:
        """Returns the number of contacts in this book"""
        return len(self.contacts.keys())

    def addNewContact(self, name, email, position, extension):
        """Add a new key/value pairing to the dictionary
           Returns True if this is a new contact and can be added
           False otherwise"""
        if name not in self.contacts.keys():
            self.contacts[name] = (email, position, extension)
            return True
        else:
            return False

    def updateEmail(self, name, newEmail):
        """Updates an email address for the named person
           Returns True if can be updated, false otherwise """
        if name in self.contacts.keys():
            v = self.contacts[name]
            email, position, extension = v
            self.contacts[name] = (newEmail, position, extension)
            return True
        else:
            return False

    def getEmail(self, name):
        """Fetches an email address for a named person. Returns
        None if the named person is not in the contacts list"""
        if name in self.contacts.keys():
            v = self.contacts[name]
            email, position, extension = v
            return email
        else:
            return None

    def searchByName(self, name):
        """Search for person by name and display contact details"""
        if name not in self.contacts.keys():
            print(f'Sorry, {name} not in the contacts list')
            return False
        else:
            v = self.contacts[name]
            email, position, extension = v
            print(f'{name}: email: {email}, position: {position}, ext: {extension}')
            return True

    def printAllKeys(self):
        """Print all keys in the dictionary """
        for k in self.contacts.keys():
            print(k)


class TestContactsBook(unittest.TestCase):

    def setUp(self):
        self.test = ContactsBook()

    def tearDown(self):
        self.test.contacts.clear()

    def test_1(self):
        # Adds a new contact ‘william’
        self.test.addNewContact('william', 'will@acme.com', 'junior', 1234)

        #  checks that the contact has been added successfully.
        # print(self.test.searchByName('william'))
        self.assertTrue(self.test.searchByName('william'))

        # Verifies that the number of contacts in the book is now 4
        # print(self.test.getNumberOfContacts())
        self.assertEqual(4, self.test.getNumberOfContacts(),
                         'Verifies that the number of contacts in the book is now 4')

        # Attempts to add ‘william’ again and then checks that it was not added
        self.assertFalse(self.test.addNewContact('william', 'will@acme.com', 'junior',
                                                 1234),
                         "Attempts to add ‘william’ again and then checks that it was not added")
        # Verifies that the number of contacts in the book is still 4.
        # print(self.test.getNumberOfContacts())
        self.assertEqual(4, self.test.getNumberOfContacts(),
                         "Verifies that the number of contacts in the book is still 4")

    def test_2(self):
        # Verifies that rod’s email address is ‘rod@acme.com’.
        # print(self.test.getEmail('rod') == 'rod@acme.com')
        self.assertEqual(self.test.getEmail('rod'), 'rod@acme.com',
                         "Verifies that rod’s email address is ‘rod@acme.com’")

        # Updates rod’s email address to ‘roddy@acme.com’
        self.test.updateEmail('rod', 'roddy@acme.com')

        # Verifies that rod’s email address is now ‘roddy@acme.com’
        # self.test.getEmail('rod')
        self.assertEqual(self.test.getEmail('rod'), 'roddy@acme.com',
                         "Verifies that rod’s email address is now ‘roddy@acme.com’")

        # Verifies that rod can be looked up by name
        # self.test.searchByName('rod')
        self.assertTrue(self.test.searchByName('rod'), "Verifies that rod can be looked up by name")

        # Check that if we try to look up a person whose name is not in the contact
        # book that searchByName() returns False.
        # print(self.test.searchByName('pika'))
        self.assertFalse(self.test.searchByName('pika'))


if __name__ == '__main__':
    unittest.main()
