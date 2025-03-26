from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    print("\n\n<--------------------------------- search_wikipedia -------------------------------------->")
    """Search wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    print("\n\n<---------------------------------- summarize_wikipedia ------------------------------------->")
    """Summarize wikipedia"""

    print(f"Finding wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    print("\n\n<---------------------------------- get_text_blob ------------------------------------->")
    """Gets text blob object and returns"""

    blob = TextBlob(text)
    return blob


def get_phrases(name):
    print("<------------------------------------- get_phrases ------------------------------------->")
    """Find wikipedia name and return back phrases"""

    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases
