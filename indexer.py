import doc2json as dj
import json

outputs = [] # output strings to print

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
                    print("Found a heading!", text_type, "on page", page, "content", text_content)
                    outputs.append(text_type + " " + text_content + " " + str(page))
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

for heading in outputs:
    print(heading)

# TODO: impl func below
"""
need to:
    1. assign correct "id" to heading according to nested, etc
    2. "tab" = nested heading level
    3. impl pad with \. (or any other char)
"""
