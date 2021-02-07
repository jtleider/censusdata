"""Functions to faciliate exporting data downloaded from Census API."""

def exportcsv(file, data):
	"""Export Pandas DataFrame where index is composed of `censusgeo` objects. Can be used with return value from `download()`.

	Args:
		file: String or file handler for exporting data.
		data (pandas.DataFrame): Data to export.

	Returns:
		None.
	"""
	geocomponent = [g[0] for g in data.index[0].geo]
	ngeocomponent = len(geocomponent)
	try:
		for gc in geocomponent:
			assert gc not in data
		assert 'NAME' not in data
	except AssertionError:
		raise ValueError('Name conflict between one of geographic components and existing variable')
	for gc in geocomponent:
		data[gc] = [g[1] for i in data.index for g in i.geo if g[0] == gc]
	data['NAME'] = [i.name for i in data.index]
	col = list(data.columns)
	data = data.reindex(columns=col[-(ngeocomponent+1):]+col[:-(ngeocomponent+1)])
	try:
		data.to_csv(file, index=False)
	finally:
		for gc in geocomponent:
			del data[gc]
		del data['NAME']
		return None

