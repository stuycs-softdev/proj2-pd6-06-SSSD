from flask import render_template
import json

DEFAULT_OPTIONS = {
	'div': '#map-canvas',
	'zoom': 11,
	'lat': 40.7143528,
	'lng': -74.0059731,
	'streetViewControl': False,
	'disableDoubleClickZoom': True,
}

# options should be a dict
def map(options={}):
	map_options = DEFAULT_OPTIONS
	map_options.update(options)
	options = json.dumps(map_options)
	return render_template('map.html', map_options=options)
