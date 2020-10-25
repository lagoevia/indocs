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

3. Add indexing to heading data
4. Add page numbers to heading data
5. Print formatted
