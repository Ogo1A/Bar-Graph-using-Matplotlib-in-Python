import matplotlib.pyplot as pyplot
labels=('Python','Java','Scala','PHP')
index=(1,2,3,4)
sizes=[25,25,25,25]

pyplot.bar(index,sizes,tick_label=labels)   
pyplot.ylabel('usage')
pyplot.xlabel('Programming Language')

pyplot.show()   
