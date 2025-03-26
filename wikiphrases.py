#!/usr/bin/env python
import fire
from nlplogic.corenlp import get_phrases


if __name__ == "__main__":
    """Run the fire cli"""
    fire.Fire(get_phrases)
