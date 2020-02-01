import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style = LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'awesome-python', 'python']

plot_dicts = [
    {'value': 81884, 'label': 'Description of s-d-p'},
    {'value': 78744, 'label': 'Description of a-p'},
    {'value': 66114, 'label': 'Description of p'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

