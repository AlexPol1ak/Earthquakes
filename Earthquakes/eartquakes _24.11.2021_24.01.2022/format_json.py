import json

file = 'data/month_earthquakes.json'

with open(file, encoding='utf-8') as f:
	moth_eq_data = json.load(f)

frmt_data = 'data/month_earthquakes_v2.json'
with open(frmt_data, 'w') as f:
	json.dump(moth_eq_data,f , indent=4)