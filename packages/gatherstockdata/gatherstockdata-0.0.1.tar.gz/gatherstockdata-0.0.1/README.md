
# Gather Stock Data

This project is primarily for personal use and education and can be used to gather simple stock data from yahoo finance. It
provides a simple way of gathering stock data without all the hard work.


## Authors

- [Lucas Rimfrost](https://www.github.com/octokatherine)


## Installation

Install gatherstockdata with pip
Use the following command in cmd:

```python
  pip install gatherstockdata
```
    
## Usage

```python
from gatherstockdata import *

def main():
    # Ticker of stock as parameter
    data = gather_funda_info("AAPL")
    return data['pps']

show_data = main()
print(show_data)
```

