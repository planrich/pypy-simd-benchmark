
import sys
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show(filename,means,stds,
        all_benchmark_names,all_benchmark_names_show,
        speedup=None, sorting=None):
    if not sorting:
        sorting = {'python': 3, 'pypy-vec': 1, 'pypy': 2}
    names = {'python': 'CPython', 'pypy-vec': 'PyPy VecOpt', 'pypy': 'PyPy'}
    fig, ax = plt.subplots(figsize=(10,5))

    index = numpy.arange(len(all_benchmark_names))
    bar_width = 0.15

    opacity = 1
    error_config = {'ecolor': '0.3'}

    colors = ['#c25b56','#525564','#96c0Ce']
    for i,name in enumerate(sorted(means.keys(), key=lambda x: sorting[x])):
        mean = means[name]
        std = stds[name]
        label = names[name]
        print mean
        print std
        print label
        plt.bar(index + (i+1) * bar_width, mean,
                bar_width, alpha=opacity,
                color=colors[i], yerr=std,
                error_kw=error_config, label=label,)

    plt.xlabel('')
    plt.ylabel('Time in seconds (Less is better)')
    plt.title('NumPy/Python programs')
    plt.yticks(numpy.arange(0,1.5,step=0.5))
    plt.xticks(index + ((bar_width*4)/2.0), all_benchmark_names_show, rotation=60)
    plt.legend()

    for line in ax.get_xticklines() + ax.get_yticklines():
        line.set_markersize(0)

    plt.tight_layout()
    plt.savefig(filename)
    plt.show()
