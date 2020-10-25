import doc2json as dj

outputs = []

def parseHeadingInfo(body_content, verbose):
    for i in range(len(body_content)):
        content = str(body_content[i])
        prefix = content.find("'namedStyleType': '")
        if prefix != -1:
            prefix += 18 # add len of search string
            headingType = content[prefix+1:content.index("'", prefix+1)]
            contentPrefix = content.find("'content': '") + 11
            headingText = content[contentPrefix+1:content.index("'", contentPrefix+1)-2]
            if verbose:
                print(headingType)
                print(headingText)
            if headingType.find("TITLE") != -1 or headingType.find("HEADING_") != -1: 
                outputs.append(headingType + " " + headingText) 
        if verbose:
            print(body_content[i])
            print()

result = dj.getDocumentContents()
result = result['body']['content']
parseHeadingInfo(result, True)

for heading in outputs:
    print(heading)
