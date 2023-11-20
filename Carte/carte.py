import pygal_maps_fr
from pygal.style import LightColorizedStyle
fr_chart = pygal_maps_fr.Regions()
fr_chart.title = 'Some regions'
fr_chart.add('Métropole', ['82', '11', '93'])
fr_chart.add('Corse', ['94'])
fr_chart.add('DOM COM', ['01', '02', '03', '04'])
fr_chart.render()
