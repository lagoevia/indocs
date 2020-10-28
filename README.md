# Google Docs Indexer

Simple indexer for Google Docs, as an addon via Google Script.
For the current document, use all headings info to generate an index.
Each line in the index has the format:
id. description(padding)pagenum, ie
1. Some title...........10

Technical:

Get JSON dump, formulate index from that, then insert back into document?

1. Get JSON dump
Done by google,
    https://developers.google.com/docs/api/samples/output-json#python
as doc2json.py

2. Parse Heading Info separately
Done, need to apply some minor extra formatting

3. Add link functionality to headers

Note: as of now, approach requires an user to insert section breaks where
pages end. This is impractical as these would move around upon later changes.
A possible future solution is to allow functionality to remove section breaks.
Then, user would need to manually insert the new ones, then generate index.
