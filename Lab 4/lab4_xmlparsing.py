# XML Parsing
import pickle
import csv
import xml.etree.ElementTree
import urllib.request


# Download XML file from URL
URL = "http://mlg.ucd.ie/modules/COMP30760/contacts.xml"
response = urllib.request.urlopen(URL)
raw_xml = response.read().decode()
print(raw_xml)

# Parse the XML Data
tree = xml.etree.ElementTree.fromstring(raw_xml)

# Store contacts from XML File in a list of dictionaries
contacts = []
for entry in tree.findall("contact"):
    contact = {}
    contact["name"] = entry.find("name").text
    contact["email"] = entry.find("email").text
    contact["phone"] = entry.find("phone").text
    contacts.append(contact)
print("Parsed %d contacts" % len(contacts))

for contact in contacts:
    print("%s:\temail=%s\tphone=%s" %
          (contact["name"], contact["email"], contact["phone"]))

# Export to CSV
f_out = open("contacts.csv", "w")

fields = ["name", "email", "phone"]
writer = csv.DictWriter(f_out, fieldnames=fields)

writer.writeheader()

for contact in contacts:
    writer.writerow(contact)
f_out.close()


# Serialise Data With Pickle File
f_out = open("contacts.pkl", "wb")
pickle.dump(contacts, f_out)
f_out.close()

f_in = open("contacts.pkl", "rb")
backup = pickle.load(f_in)
f_in.close()

# Un-Pickling File
print("Read %d contacts" % len(backup))
for contact in backup:
    print("%s:\temail=%s\tphone=%s" %
          (contact["name"], contact["email"], contact["phone"]))
