from utils import get_year
from taipy import Gui
# from taipy.gui import Markdown

# year = str(get_year())
years = [(str(y), str(y)) for y in get_year()]
year = years[0]
print(year)
# text = '2014'
base_page = """
    # Getting started with Taipy GUI

My year: <|{year}|>

<|{year}|selector|lov={years}|dropdown|>
"""

Gui(page=base_page).run()
