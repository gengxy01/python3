import json
from pygal_maps_world.i18n import COUNTRIES

import pygal_maps_world.maps as m
from pygal.style import RotateStyle, LightenStyle, DefaultStyle
import country_code as cc


filename = "population_data.json"

with open(filename) as f:
    pop_data = json.load(f)

cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = cc.get_country_code(country_name)
        if code:
            cc_populations[code] = population

#根据人口数量分为三组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}

for code, population in cc_populations.items():
    if population < 10000000:
        cc_pops_1[code] = population
    elif population < 1000000000:
        cc_pops_2[code] = population
    else:
        cc_pops_3[code] = population

wm_style = RotateStyle('#c7f4f3')
wm = m.World(style=wm_style)
# wm.add('2010', cc_populations)
wm.add('0-10m', cc_pops_1)
wm.add('10m-1bn', cc_pops_2)
wm.add('>1bn', cc_pops_3)
wm.render_to_file('world_population.svg')




