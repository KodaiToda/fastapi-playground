# import requests

# url = 'https://jsonplaceholder.typicode.com/posts'

# res = requests.get(url)

# print(res.status_code)
# print(res.json())

# datum = res.json()[0]
# print(datum)

from typing import List, Dict

sample_list: List[int] = [1, 2, 3, 4]
sample_dict: Dict[str, str] = {'username': 'abcd'}

price: int = 100
tax: float = 1.1

def calc_price_including_tax(price: int, tax: float) -> int:
  return int(price*tax)

if __name__ == '__main__':
  print(f'{calc_price_including_tax(price=price, tax=tax)}円')


