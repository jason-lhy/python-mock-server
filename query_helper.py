def dict_to_query(dictionary: dict) -> str:
  conditions = [f"AND JSON_EXTRACT(arguments, '$.{k}') = '{v}'" for k, v in dictionary.items()]
  return " ".join(conditions)