import unittest
import io
from contextlib import redirect_stdout

# Import functions from student assignment.
# Instead of 'assignment8_1', use the student's Python filename without the .py.
from loadable_contact_list_class import ContactList

EXAMPLE_FILE = "sample_contact_list.txt"

class TestExample(unittest.TestCase):
    '''Example Suite'''

    def test_example_display(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            input = EXAMPLE_FILE
            ContactList(input).display()
            actual = buf.getvalue()
            expected = "Sandy Cheeks\tcheeks@ucsc.edu\t831-507-8282\t157 Dome Drive\n\
Perry Platypus\tnotaplatypus@ucsc.edu\t510-339-2102\t7211 Tristate Alley\n\
Ino Yamanaka\ttelekineticflower@ucsc.edu\t415-988-2341\t98 Konoha Lane\n\
Ash Ketchum\tpikapika@ucsc.edu\t626-876-2212\t2 Pallet Town Road\n\
Finn and Jake\tfinnjakeinc@ucsc.edu\t954-878-0909\t1001 Ooo Street\n\
Eren Jaeger\tboywithtitanheart@ucsc.edu\t808-243-1234\t892 Mi Casa Court\n\
Jeon Jung-kook\tjungkook@ucsc.edu\t408-797-2210\t65400 BTS Parkway\n\
Ariana Grande\tkat@ucsc.edu\t626-771-2214\t1126 Mariah Avenue\n\
Avatar Aang\taang@ucsc.edu\t915-122-1912\t1 Northern Air Temple\n\
Lee Chae-lin\tcl@ucsc.edu\t510-822-5453\t4321 Hello Boulevard\n"
            self.assertEqual(actual, expected, \
                f"example/load_contact_list :: Function failed with input {input}. Found {actual}, expected {expected}.")
            # buf.flush()
            # buf.close()

    def test_example_get_email_1(self):
        input = "Eren Jaeger"
        actual = ContactList(EXAMPLE_FILE).get_email(input)
        expected = 'boywithtitanheart@ucsc.edu'
        self.assertEqual(actual, expected, \
            f"example/get_email :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_email_2(self):
        input = "Sasuke Uchiha"
        actual = ContactList(EXAMPLE_FILE).get_phone(input)
        expected = None
        self.assertEqual(actual, expected, \
            f"example/get_email :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_phone(self):
        input = "Lee Chae-lin"
        actual = ContactList(EXAMPLE_FILE).get_phone(input)
        expected = '510-822-5453'
        self.assertEqual(actual, expected, \
            f"example/get_phone :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_address(self):
        input = "Sandy Cheeks"
        actual = ContactList(EXAMPLE_FILE).get_address(input)
        expected = '157 Dome Drive'
        self.assertEqual(actual, expected, \
            f"example/get_address :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_email_list(self):
        input = ["Ino Yamanaka", "Ash Ketchum", "Ariana Grande"]
        actual = ContactList(EXAMPLE_FILE).get_email_list(input)
        expected = ['telekineticflower@ucsc.edu', 'pikapika@ucsc.edu', 'kat@ucsc.edu']
        self.assertCountEqual(actual, expected, \
            f"example/get_email_list :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_phone_list(self):
        input = ["Finn and Jake", "Lee Chae-lin", "Avatar Aang", "Perry Platypus"]
        actual = ContactList(EXAMPLE_FILE).get_phone_list(input)
        expected = ['954-878-0909', '510-822-5453', '915-122-1912', '510-339-2102']
        self.assertCountEqual(actual, expected, \
            f"example/get_phone_list :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_phone_list_2(self):
        input = ['Jeon Jung-kook', "Gaara of the Sand", "Lee Chae-lin", "Green Skin Donkey Kong"]
        actual = ContactList(EXAMPLE_FILE).get_phone_list(input)
        expected = ['408-797-2210', '510-822-5453']
        self.assertCountEqual(actual, expected, \
            f"example/get_phone_list :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_address_list(self):
        input = ["Finn and Jake", "Lee Chae-lin", "Avatar Aang", "Perry Platypus"]
        actual = ContactList(EXAMPLE_FILE).get_address_list(input)
        expected = ['1001 Ooo Street', '4321 Hello Boulevard', '1 Northern Air Temple', '7211 Tristate Alley']
        self.assertCountEqual(actual, expected, \
            f"example/get_address_list :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_example_get_address_list_2(self):
        input = ['Jeon Jung-kook', "Gaara of the Sand", "Lee Chae-lin", "Green Skin Donkey Kong"]
        actual = ContactList(EXAMPLE_FILE).get_address_list(input)
        expected = ['65400 BTS Parkway', '4321 Hello Boulevard']
        self.assertCountEqual(actual, expected, \
            f"example/get_address_list :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_get_all_names(self):
        input = EXAMPLE_FILE
        actual = ContactList(EXAMPLE_FILE).get_all_names()
        expected = ['Sandy Cheeks', 'Perry Platypus', 'Ino Yamanaka', 'Ash Ketchum', 'Finn and Jake', 'Eren Jaeger', 'Jeon Jung-kook', 'Ariana Grande', 'Avatar Aang', 'Lee Chae-lin']
        self.assertCountEqual(actual, expected, \
            f"example/get_all_names :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_get_all_emails(self):
        input = EXAMPLE_FILE
        actual = ContactList(EXAMPLE_FILE).get_all_emails()
        expected = ['cheeks@ucsc.edu', 'notaplatypus@ucsc.edu', 'telekineticflower@ucsc.edu', 'pikapika@ucsc.edu', 'finnjakeinc@ucsc.edu', 'boywithtitanheart@ucsc.edu', 'jungkook@ucsc.edu', 'kat@ucsc.edu', 'aang@ucsc.edu', 'cl@ucsc.edu']
        self.assertCountEqual(actual, expected, \
            f"example/get_all_names :: Function failed with input {input}. Found {actual}, expected {expected}.")


    def test_get_all_phones(self):
        input = EXAMPLE_FILE
        actual = ContactList(EXAMPLE_FILE).get_all_phones()
        expected = ['831-507-8282', '510-339-2102', '415-988-2341', '626-876-2212', '954-878-0909', '808-243-1234', '408-797-2210', '626-771-2214', '915-122-1912', '510-822-5453']
        self.assertCountEqual(actual, expected, \
            f"example/get_all_phones :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_get_all_addresses(self):
        input = EXAMPLE_FILE
        actual = ContactList(EXAMPLE_FILE).get_all_addresses()
        expected = ['157 Dome Drive', '7211 Tristate Alley', '98 Konoha Lane', '2 Pallet Town Road', '1001 Ooo Street', '892 Mi Casa Court', '65400 BTS Parkway', '1126 Mariah Avenue', '1 Northern Air Temple', '4321 Hello Boulevard']
        self.assertCountEqual(actual, expected, \
            f"example/get_all_addresses :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_str(self):
        input = EXAMPLE_FILE
        actual = ContactList(EXAMPLE_FILE).__str__()
        expected = "Contacts (10): Sandy Cheeks, Perry Platypus, Ino Yamanaka, Ash Ketchum, Finn and Jake, Eren Jaeger, Jeon Jung-kook, Ariana Grande, Avatar Aang, Lee Chae-lin."
        self.assertCountEqual(actual, expected, \
            f"example/get_all_addresses :: Function failed with input {input}. Found {actual}, expected {expected}.")

    def test_add_contact(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            input = ("Jonathan Joestar", "jjoestar@ucsc.edu", "333-333-3333", "1 Joestar Mansion, Britian")
            actual = ContactList(EXAMPLE_FILE)
            actual.add_contact(("Jonathan Joestar", "jjoestar@ucsc.edu", "333-333-3333", "1 Joestar Mansion, Britian"))
            actual.display()
            actual = buf.getvalue()
            expected = "Sandy Cheeks\tcheeks@ucsc.edu\t831-507-8282\t157 Dome Drive\n\
Perry Platypus\tnotaplatypus@ucsc.edu\t510-339-2102\t7211 Tristate Alley\n\
Ino Yamanaka\ttelekineticflower@ucsc.edu\t415-988-2341\t98 Konoha Lane\n\
Ash Ketchum\tpikapika@ucsc.edu\t626-876-2212\t2 Pallet Town Road\n\
Finn and Jake\tfinnjakeinc@ucsc.edu\t954-878-0909\t1001 Ooo Street\n\
Eren Jaeger\tboywithtitanheart@ucsc.edu\t808-243-1234\t892 Mi Casa Court\n\
Jeon Jung-kook\tjungkook@ucsc.edu\t408-797-2210\t65400 BTS Parkway\n\
Ariana Grande\tkat@ucsc.edu\t626-771-2214\t1126 Mariah Avenue\n\
Avatar Aang\taang@ucsc.edu\t915-122-1912\t1 Northern Air Temple\n\
Lee Chae-lin\tcl@ucsc.edu\t510-822-5453\t4321 Hello Boulevard\n\
Jonathan Joestar\tjjoestar@ucsc.edu\t333-333-3333\t1 Joestar Mansion, Britian\n"
            self.assertCountEqual(actual, expected, \
            f"example/add_contact :: Function failed with input {input}. Found {actual}, expected {expected}.")
            # buf.flush()
            # buf.close()

    def test_remove_contact(self):
        with io.StringIO() as buf, redirect_stdout(buf):
            input = "Sandy Cheeks"
            actual = ContactList(EXAMPLE_FILE)
            actual.remove_contact("Sandy Cheeks")
            actual.display()
            actual = buf.getvalue()
            expected = "Perry Platypus\tnotaplatypus@ucsc.edu\t510-339-2102\t7211 Tristate Alley\n\
Ino Yamanaka\ttelekineticflower@ucsc.edu\t415-988-2341\t98 Konoha Lane\n\
Ash Ketchum\tpikapika@ucsc.edu\t626-876-2212\t2 Pallet Town Road\n\
Finn and Jake\tfinnjakeinc@ucsc.edu\t954-878-0909\t1001 Ooo Street\n\
Eren Jaeger\tboywithtitanheart@ucsc.edu\t808-243-1234\t892 Mi Casa Court\n\
Jeon Jung-kook\tjungkook@ucsc.edu\t408-797-2210\t65400 BTS Parkway\n\
Ariana Grande\tkat@ucsc.edu\t626-771-2214\t1126 Mariah Avenue\n\
Avatar Aang\taang@ucsc.edu\t915-122-1912\t1 Northern Air Temple\n\
Lee Chae-lin\tcl@ucsc.edu\t510-822-5453\t4321 Hello Boulevard\n"
            self.assertCountEqual(actual, expected, \
            f"example/remove_contact :: Function failed with input {input}. Found {actual}, expected {expected}.")
            # buf.flush()
            # buf.close()

if __name__ == "__main__":

    unittest.main()