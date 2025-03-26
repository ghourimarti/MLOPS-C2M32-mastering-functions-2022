#!/usr/bin/env python
print("Hello World")
from nlplogic.corenlp import get_phrases , search_wikipedia , summarize_wikipedia , get_text_blob
name = "Golden State Warriors"
blob = get_text_blob(name)


print("<------------------------------------- get_phrases ------------------------------------->")
print(get_phrases(name))
print("\n\n<--------------------------------- search_wikipedia -------------------------------------->")
print(search_wikipedia(name))
print("\n\n<---------------------------------- summarize_wikipedia ------------------------------------->")
print(summarize_wikipedia(name))
print("\n\n<---------------------------------- get_text_blob ------------------------------------->")
print(get_text_blob(summarize_wikipedia(name)))
print("\n\n<---------------------------------- blob.noun_phrases -------------------------------------->")
print(blob.noun_phrases)
