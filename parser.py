import requests
import json
from requests.exceptions import ConnectionError
from copy import deepcopy

INVALID_VALUES = ['N/A', '-', '']

def retrieve():
  """
  Retrieves data
  """
  r = None
  try:
    r = requests.get('https://coderbyte.com/api/challenges/json/json-cleaning')
  except ConnectionError as e:
    print(e)
  return r

def parse_generic(data):
  """
  Dispatches value to dict or list clean 
  """
  if isinstance(data, dict):
    return clean_dict(data)
  elif isinstance(data, list):
    return clean_list(data)
  return data

def clean_dict(data):
  """
  Parses a list to remove terms from INVALID_VALUES
  """
  cleaned_dict = {}
  for key, value in data.items():
    cleaned_data = parse_generic(value)
    if cleaned_data not in INVALID_VALUES:
      cleaned_dict.update({key: cleaned_data})
  return cleaned_dict

def clean_list(data):
  """
  Parses a list to remove terms from INVALID_VALUES
  """
  cleaned_list = []
  for value in data:
    cleaned_data = parse_generic(value)
    if cleaned_data not in INVALID_VALUES:
      cleaned_list.append(value)
  return cleaned_list

def clean_data():
  data = retrieve().json()
  cleaned_data = parse_generic(data)
  return cleaned_data

print(clean_data())
