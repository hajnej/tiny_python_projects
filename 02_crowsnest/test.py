#!/usr/bin/env python3
"""tests for crowsnest.py"""

import os
from subprocess import getstatusoutput, getoutput

prg = './crowsnest.py'
consonant_words = [
    'brigantine', 'clipper', 'dreadnought', 'frigate', 'galleon', 'haddock',
    'junk', 'ketch', 'longboat', 'mullet', 'narwhal', 'porpoise', 'quay',
    'regatta', 'submarine', 'tanker', 'vessel', 'whale', 'xebec', 'yatch',
    'zebrafish'
]
vowel_words = ['aviso', 'eel', 'iceberg', 'octopus', 'upbound']
invalid_words = ['4sharks', 'cam3l', 'sea!gul']
template = 'Ahoy, Captain, {} {} off the larboard bow!'


# --------------------------------------------------
def test_exists():
    """exists"""

    assert os.path.isfile(prg)


# --------------------------------------------------
def test_usage():
    """usage"""

    for flag in ['-h', '--help']:
        rv, out = getstatusoutput(f'{prg} {flag}')
        assert rv == 0
        assert out.lower().startswith('usage')


# --------------------------------------------------
def test_consonant():
    """brigantine -> a brigantine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('a', word)


# --------------------------------------------------
def test_consonant_upper():
    """brigantine -> A Brigatine"""

    for word in consonant_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('A', word.title())


# --------------------------------------------------
def test_vowel():
    """octopus -> an octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word}')
        assert out.strip() == template.format('an', word)


# --------------------------------------------------
def test_vowel_upper():
    """octopus -> An Octopus"""

    for word in vowel_words:
        out = getoutput(f'{prg} {word.title()}')
        assert out.strip() == template.format('An', word.title())

def test_boat_larboard():
    """side is larboard"""
    side = "larboard"
    for word in consonant_words:
        out = getoutput(f"{prg} --side {side} {word}")
        assert out.strip() == f'Ahoy, Captain, a {word} off the {side} bow!'

def test_boat_starboard():
    """side is starboard"""
    side = "starboard"
    for word in consonant_words:
        out = getoutput(f"{prg} --side {side} {word}")
        assert out.strip() == f'Ahoy, Captain, a {word} off the {side} bow!'

def test_invalid_input():
    """Test input word is valid alpha"""

    for word in invalid_words:
        out = getoutput(f"{prg} {word}")
        assert out.strip() == f"FAIL: {word} is not valid alphabetic string"
