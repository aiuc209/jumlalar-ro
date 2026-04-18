import pytest

def capitalize_first_last(sentence):
    words = sentence.split()
    if len(words) > 1:
        return words[0].capitalize() + ' ' + ' '.join(words[1:-1]) + ' ' + words[-1].capitalize()
    else:
        return words[0].upper()

def test_capitalize_first_last():
    assert capitalize_first_last("hello world") == "Hello world World"
    assert capitalize_first_last("python is fun") == "Python is Fun"
    assert capitalize_first_last("i am a programmer") == "I am A Programmer"
    assert capitalize_first_last("single") == "SINGLE"

def test_capitalize_first_last_empty_string():
    assert capitalize_first_last("") == ""

def test_capitalize_first_last_single_word():
    assert capitalize_first_last("test") == "TEST"
