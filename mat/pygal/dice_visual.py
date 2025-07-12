from die import Die
import pygal

die = Die()
die2 = Die()
results = []
for roll_num in range(1000):
    result = die.roll()+die2.roll()
    results.append(result)

frequencies = []
max_result = die.sides + die2.sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6','7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')
# hist.render()
