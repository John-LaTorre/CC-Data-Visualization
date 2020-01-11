import pygal
from die import Die

#Create a d6
die = Die()

#Make some rolls, store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

#Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one d6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('d6', frequencies)
hist.render_to_file('die_visual.svg')


