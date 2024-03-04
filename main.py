from utils import get_year, get_data_line_chart, get_data_summary_line
from taipy import Gui
# from taipy.gui import Markdown

# year = str(get_year())
years = [(str(y), str(y)) for y in get_year()]
year = years[0]
print(year)
data = get_data_line_chart()
total_devisa = get_data_summary_line()
# Name of the three sets to trace
items = sorted([d for d in data.keys() if d not in ['Tahun', 'Jumlah']])

options = [
    {"stackgroup": "one", "groupnorm": "percent"},
    {"stackgroup": "one"},
    {"stackgroup": "one"},
    {"stackgroup": "one"},
    {"stackgroup": "one"},
    {"stackgroup": "one"}
]
layout = {
    # Show all values when hovering on a data point
    "hovermode": "x unified"
}

print(data)
current_devisa = total_devisa['Total'][-1]
last_devisa = total_devisa['Total'][-2]
first_devisa = total_devisa['Total'][0]
# text = '2014'
base_page = """
<|1 1 1|layout|
<current_devisa|
## **Current Devisa**{: .color-primary}:
## US $ <|{current_devisa}|text|raw|>
|current_devisa>

<two_year_increment|
## **2022-2023 Increment**{: .color-primary}:
## <|{round(((current_devisa - last_devisa) / last_devisa * 100), 2)}|text|raw|> %
|two_year_increment>

<all_time_increment|
## **2005-2023 Increment**{: .color-primary}:
## <|{round(((current_devisa - first_devisa) / first_devisa * 100), 2)}|text|raw|> %
|all_time_increment>
|>

<|1 1|layout|
<|{total_devisa}|chart|mode=lines|x=Tahun|y[1]=Total|title=Total Devisa Indonesia (dalam Juta USD)|>

<|{data}|chart|x=Tahun|y={items}|title=Detail Cadangan Devisa (dalam Juta USD)|>
|>
<|{data}|chart|x=Tahun|y={items}|options={options}|layout={layout}|title=Komposisi Cadangan Devisa (dalam persen)|>

"""

Gui(page=base_page).run(use_reloader=True, port=8080)
