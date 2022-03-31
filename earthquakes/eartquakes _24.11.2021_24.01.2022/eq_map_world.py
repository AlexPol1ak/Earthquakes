import json
from plotly.graph_objs import Scattergeo , Layout
from plotly import offline

file = 'data/month_earthquakes_v2.json'
with open(file) as f:
	month_eq = json.load(f)
	
month_eq_dicts = month_eq['features']

mags, lons, lats, hover_texts = [], [], [], []
for m_eq_dict in month_eq_dicts:
		mags.append(m_eq_dict['properties']['mag'])
		lons.append(m_eq_dict['geometry']['coordinates'][0])
		lats.append(m_eq_dict['geometry']['coordinates'][1])
		hover_texts.append(m_eq_dict['properties']['title'])

data = [{
	'type': 'scattergeo',
	'lon': lons,
	'lat': lats,
	'text': hover_texts,
	'marker':{
	    'size': [4*mag for mag in mags],
	    'color': mags,
	    'colorscale':'inferno',
	    'reversescale': True,
	    'colorbar': {'title': 'Magnitude 1.0+', 'bgcolor': 'gray'},
	}
}]
ca_layout = Layout(title='Magnitude 1.0+ Earthquakes, Past Month, World')
fig = {'data': data, 'layout': ca_layout }
offline.plot(fig, filename='Magnitude_1_0+_Earthquakes_Past_Month_world.html')
