def split_removing_spaces(text, cutter_element=" "):
    """Separate the string by the element indicated by removing unnecessary spaces."""
    return list(map(lambda item: item.strip(), text.split(cutter_element)))


def get_random_token_int(length=6):
    """Get random number. Example: 123456"""
    import uuid
    return str(uuid.uuid4().int)[:length]

  
def transform_to_snake_case(text):
    """Example: hello world -> hello_world"""
    return text.strip().lower().replace(' ', '_'))
    
  
def transform_to_kebab_case(text):
  """Example: hello world -> hello-world"""
  return text.strip().lower().replace(' ', '-'))

  
def transform_to_camel_case(text):
  """Example: hello world -> helloWorld"""
  return ''.join(map(lambda word: word.capitalize(), text.strip().split(' '))))

    
def convert_to_two_decimals(number: float):
    return float("{:.2f}".format(number))


def convert_to_two_decimals_string(number: str):
    return "{:.2f}".format(number)


def remove_accents(raw_text):
    """Removes common accent characters."""
    import re
    import functools
    sustitutions = {
        "[àáâãäå]": "a",
        "[ÀÁÂÃÄÅ]": "A",
        "[èéêë]": "e",
        "[ÈÉÊË]": "E",
        "[ìíîï]": "i",
        "[ÌÍÎÏ]": "I",
        "[òóôõö]": "o",
        "[ÒÓÔÕÖ]": "O",
        "[ùúûü]": "u",
        "[ÙÚÛÜ]": "U",
        "[ýÿ]": "y",
        "[ÝŸ]": "Y",
        "[ß]": "ss",
        "[ñ]": "n",
        "[Ñ]": "N",
    }
    return functools.reduce(
        lambda text, key: re.sub(key, sustitutions[key], text),
        sustitutions.keys(),
        raw_text,
    )
