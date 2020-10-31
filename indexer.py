import doc2json as dj
import json
import sys

outputs = [] # output strings to print
headingValues = { 'TITLE': 0, 'SUBTITLE': 1, 'HEADING_1': 2,
        'HEADING_2': 3, 'HEADING_3': 4, 'HEADING_4': 5 }

def parseHeadingInfo(doc):
    quantity = doc['body']['content']
    page = 0 # start on 0'th page (will be inc on first break)
    for el in quantity:
        print()
        print(el, "::", type(el))
        if type(el) == dict:
            print("---")
            print(el.keys())
            # check if section, increment page if so
            if 'sectionBreak' in el.keys():
                print("Section found!", end=' ')
                page += 1
            # if not a section, check contents
            else:
                print("Not a section")
                if 'paragraph' not in el.keys():
                    continue # ignore non paragraph types
                text_type = el['paragraph']['paragraphStyle']['namedStyleType']
                elements = el['paragraph']['elements'][0]
                if 'textRun' in elements:
                    text_content = elements['textRun']['content']
                    # some text content here carry a trailing newline; remove it
                    if '\n' in text_content:
                        text_content = text_content[:len(text_content)-1]
                else:
                    print("No text run!", elements.keys())
                    continue
                #text_content = el['paragraph']['elements']['textRun']['content']
                if 'HEADING_' in text_type or 'TITLE' in text_type:
                    hv = headingValues[text_type]
                    tabs = hv * '    '
                    print("Found a heading!", text_type, "on page", page, "content", text_content)
                    outputs.append(str(page) + "~" + tabs + text_content) 
            if 'startIndex' in el:
                print(el['startIndex'])
            if 'endIndex' in el:
                print(el['endIndex'])
            if 'paragraph' in el:
                print(el['paragraph'])
            print("Found on page", page)
    print(type(quantity))


doc = dj.getDocumentContents()
with open('.dump', 'w') as f:
    f.writelines(json.dumps(doc))
    f.close()
parseHeadingInfo(doc)

L = int(sys.argv[1]) if len(sys.argv) > 1 else 80
padChar = '.'
for line in outputs:
        delim = line.index('~')
        pageNumber = line[0:delim]
        l = len(line) - len(pageNumber) - 1
        pad = L - l - len(pageNumber)
        # TODO: include URL's here to bit in code
        print(line[delim+1:len(line)], padChar * pad, str(pageNumber),
                sep='') 
        #print(heading)

