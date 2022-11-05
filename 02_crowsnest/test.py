#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = "./crowsnest.py"
consonant_words = [
    "brigantine",
    "clipper",
    "dreadnought",
    "frigate",
    "galleon",
    "haddock",
    "junk",
    "ketch",
    "longboat",
    "mullet",
    "narwhal",
    "porpoise",
    "quay",
    "regatta",
    "submarine",
    "tanker",
    "vessel",
    "whale",
    "xebec",
    "yatch",
    "zebrafish",
]
vowel_words = ["aviso", "eel", "iceberg", "octopus", "upbound"]
template = "Ahoy, Captain, {} {} off the larboard bow!"
starboard_template = "Ahoy, Captain, {} {} off the starboard bow!"


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ["-h", "--help"]:
        rv, out = getstatusoutput(f"{prg} {flag}")
        assert rv == 0
        assert out.lower().startswith("usage")


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("a", word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> a Brigatine"""

    for word in consonant_words:
        out = getoutput(f"{prg} {word.title()}")
        assert out.strip() == template.format("A", word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == template.format("an", word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> an Octopus"""

    for word in vowel_words:
        out = getoutput(f"{prg} {word.upper()}")
        assert out.strip() == template.format("An", word.upper())


def test_matching_case():
    """Checks if the article matches the word"""
    for word in vowel_words:
        out_upper = getoutput(f"{prg} {word.title()}")
        assert out_upper.strip() == template.format("An", word.title())


def test_starbaord():
    """Checks if the --side switch outputs the word starboard"""
    for word in vowel_words:
        output = getoutput(f"{prg} {word} --side starboard")
        assert output.strip() == starboard_template.format("an", word)

def test_error_message():
    """Checks that a helpful message is displayed when garbage is fed to the program"""
    output = getoutput(f"{prg} 12324354")
    assert output.strip() == "Your word must start with an alphabetical character"