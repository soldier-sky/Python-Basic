def parse_xml(xml_string):
    stack = []
    elements = {}

    i = 0
    while i < len(xml_string):
        if xml_string[i] == '<':
            j = i + 1
            while j < len(xml_string) and xml_string[j] != '>':
                j += 1

            if j < len(xml_string) and xml_string[i + 1] == '/':
                # Closing tag
                tag = xml_string[i + 2:j].strip()
                if stack:
                    parent = stack.pop()
                    parent_name = parent[0]
                    parent_content = parent[1]

                    if parent_name not in elements:
                        elements[parent_name] = []

                    if parent_content:
                        elements[parent_name].append({tag: parent_content})

                    current_element = (parent_name, elements[parent_name])
                else:
                    current_element = (tag, elements[tag] if tag in elements else [])
            else:
                # Opening tag
                tag = xml_string[i + 1:j].strip()
                stack.append((tag, []))

            i = j + 1
        else:
            # Text content
            j = i
            while j < len(xml_string) and xml_string[j] != '<':
                j += 1

            # Text content
            content = xml_string[i:j].strip()
            if content:
                stack[-1][1].append(content)

            i = j

    return elements


# Example XML string
xml_string = """
<root>
    <person>
        <name>John</name>
        <age>30</age>
    </person>
    <person>
        <name>Jane</name>
        <age>25</age>
    </person>
</root>
"""


arxml_string = """
<ARXML>
    <AUTOSAR xmlns="http://autosar.org/schema/r4.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://autosar.org/schema/r4.0 AUTOSAR_4-2-2.xsd">
        <ECU-Instance>
            <ECU-Id>ECU1</ECU-Id>
            <Short-Name>EngineECU</Short-Name>
            <!-- Other ECU properties go here -->
        </ECU-Instance>
        <ECU-Instance>
            <ECU-Id>ECU2</ECU-Id>
            <Short-Name>BrakeECU</Short-Name>
            <!-- Other ECU properties go here -->
        </ECU-Instance>
    </AUTOSAR>
</ARXML>
"""

# Parsing the XML string
parsed_data = parse_xml(xml_string)
print(parsed_data)


parsed_data2 = parse_xml(arxml_string)
print(parsed_data2)
