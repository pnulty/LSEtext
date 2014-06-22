import matplotlib.pyplot as plt
import numpy as np

#ax = plt.subplot() 
#for label in (ax.get_xticklabels() + ax.get_yticklabels()):
#    label.set_fontname('Arial')
#    label.set_fontsize(20)


def get_values(f):
	remove_words=["'veil'", "'jobseek'"]
	lines = open(f).readlines()
	i=4
	words = []
	sims = []
	while(i < len(lines)):
		word = lines[i].split()[-1]
		sim = float(lines[i+1].strip()) 
		if not word in remove_words:
			words.append(word)
			sims.append(sim)
		i+=6
	print len(words)
	print len(sims)
	print
	return(words,sims) 

f = 'results/guardianCompare.txt'
gwords, gsims = get_values(f)

f = 'results/telegraphCompare.txt'
telwords, telsims = get_values(f)

f = 'results/timesCompare.txt'
timwords, timsims = get_values(f)

f = 'results/mailCompare.txt'
mwords, msims = get_values(f)

f = 'results/expressCompare.txt'
ewords, esims = get_values(f)

f = 'results/independentCompare.txt'
iwords, isims = get_values(f)


ind = np.arange(len(ewords)) 
width = 0.2       # the width of the bars

fig, ax = plt.subplots()

rects1 = ax.bar(ind, gsims,  width, color='salmon')
rects2 = ax.bar(ind+width, timsims,  width, color='slategray')
rects3 = ax.bar(ind+width+width, telsims,  width, color='royalblue')



# add some
ax.set_ylabel('Association score')
ax.set_title(' "broadsheet" newspapers ')
ax.set_xticks(range(len(telsims)))
ax.set_xticklabels(ewords)

for label in (ax.get_xticklabels() + ax.get_yticklabels()):
    label.set_fontname('Arial')
    label.set_fontsize(17)

ax.legend( (rects1[0], rects2[0], rects3[0]),('Guardian', 'Times', 'Telegraph') )



plt.show()

plt.show()