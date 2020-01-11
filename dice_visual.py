import pygal
from die import Die

#Create 4 d6
die_1 = Die()
die_2 = Die()
die_3 = Die()
die_4 = Die()

#Make some rolls, store results in a list
results = []

for roll_num in range(10000):
    rolls = []
    rolls.append(die_1.roll())
    rolls.append(die_2.roll())
    rolls.append(die_3.roll())
    rolls.append(die_4.roll())
    rolls.remove(min(rolls))

    result = sum(rolls)
    results.append(result)

#Analyze the results
frequencies = []
max_result = 18

for value in range(3, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling 4d6 and subtracting the lowest value 1000 times"
hist.x_labels = ['3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('stat roll', frequencies)
hist.render_to_file('dice_visual3.svg')


