from lxml import etree as ET

#Get the XML file data
stream = open ("sample.xml", "r")

#Parse the data into an ElementTree object
xml = ET.parse(stream)

#Get the "root" Element object from the ElementTree
root = xml.getroot()

#Itera through eachchild of the root Element
for e in root:
    #Print the stringfield version of the element
    print(ET.tostring(e))
    print("")

    #Print the "id" attribute of the Element object
    print(e.get("id"))
