

import sys
import numpy

sorted_by_name = {}
with open(sys.argv[1], "rb") as fd:
    text = fd.read()
    for entry in text.split("\n---"):
        times = []
        lines = entry.splitlines()
        lines = filter(lambda x: x.strip() != "", lines)
        if len(lines) == 0:
            continue # last entry
        name, times = lines[0].split(' raw: ')
        times = [float(f) for f in times.split(' ')]
        #
        unique_name = name.split(" ")[0].strip()
        if "python" in name:
            sorted_by_name.setdefault(unique_name,[]).append((3,'python', times))
        elif "pypyv" in name:
            sorted_by_name.setdefault(unique_name,[]).append((1,'pypy-vec', times))
        else:
            sorted_by_name.setdefault(unique_name,[]).append((2,'pypy', times))


import numpy as np
import matplotlib.pyplot as plt


n_groups = 5

means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)

means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

sorting = {'python': 1, 'pypy-vec': 3, 'pypy': 2}
names = {'python': 'Python', 'pypy-vec': 'PyPy VecOpt', 'pypy': 'PyPy'}
means = {'python': [], 'pypy-vec': [], 'pypy': []}
stds = {'python': [], 'pypy-vec': [], 'pypy': []}
labels = []
for benchmark, runs in sorted(sorted_by_name.items(), key=lambda x: x[0]):
    if len(runs) != 3:
        print "skipping", benchmark, "available:", [r for k,r,_ in runs]
        continue
    labels.append(benchmark)
    for _, runner, times in sorted(runs, key=lambda x: x[0]):
        means[runner].append(numpy.mean(times))
        stds[runner].append(numpy.std(times))

fig, ax = plt.subplots()

index = np.arange(len(labels))
bar_width = 0.35

opacity = 1
error_config = {'ecolor': '0.3'}

print means, len(means['python'])
print stds, len(stds['python'])
print len(labels)
colors = ['#ff00ff','#bbbb00','#00bbcc']
for i,name in enumerate(sorted(means.keys(), key=lambda x: sorting[x])):
    plt.bar(index + (i+1) * bar_width, means[name],
            bar_width, alpha=opacity,
            color=colors[i], yerr=stds[name],
            error_kw=error_config, label=names[name],)

plt.xlabel('Name')
plt.ylabel('Time in seconds')
plt.title('NumPy benchmarks')
plt.yticks(numpy.arange(0,4.5, step=0.5))
plt.xticks(index + bar_width, labels, rotation=60)
plt.legend()

plt.tight_layout()
plt.show()

#fd = open("numpy-benchmark.dat", "wb")
#for benchmark, runs in sorted(sorted_by_name.items(), key=lambda x: x[0]):
#    if len(runs) != 3:
#        print "skipping", benchmark, "available:", [r for k,r,_ in runs]
#        continue
#    fd.write('"%s" ' % benchmark)
#    for _, runner, times in sorted(runs, key=lambda x: x[0]):
#        mean = numpy.mean(times)
#        std = numpy.std(times)
#        fd.write('%f %f ' % (mean, std))
#    fd.write('\n')
#fd.close()
#print "written to files"
