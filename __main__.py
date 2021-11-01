

def categories(cutter_element=" "):
  """Separate the string by the element indicated by removing unnecessary spaces."""
  return list(map(lambda item: item.strip(), self.text_categories.split(cutter_element)))
