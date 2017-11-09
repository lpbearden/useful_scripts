import re

p = re.compile(r'(?:\{!case\.)(.*)(?:\})')
f = open('testfile', 'w')

with open("test.xml") as old_file:
    for line in old_file:
        m = p.search(line)
        if m:
            field_name = m.group(1)
            f.write('<apex:pageBlockSectionItem>\n' 
                + '<apex:outputLabel value="{!$ObjectType.case.fields.' + field_name +'.Label}" />\n' 
                + '<apex:outputField value="{!case.' + field_name +'}" />\n'
                + '</apex:pageBlockSectionItem>')
        else:
            f.write(line)