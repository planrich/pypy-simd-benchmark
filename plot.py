
import sys
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def show(configs, cn):
    sorting = {'python': 3, 'pypy-vec': 1, 'pypy': 2}
    names = {'python': 'CPython', 'pypy-vec': 'PyPy VecOpt', 'pypy': 'PyPy'}
    means = {'python': [], 'pypy-vec': [], 'pypy': []}
    stds = {'python': [], 'pypy-vec': [], 'pypy': []}
    sorting_benchmark = {
        'dot': 1,
        'add': 1,
        'sum': 1,
        'fir': 1,
        'rgb-to-yuv': 1,
    }
    all_benchmark_names = set()
    for config in configs:
        for name in config.times:
            all_benchmark_names.add(name)
    all_benchmark_names = sorted(all_benchmark_names)
    for config in configs:
        for benchmark_name in all_benchmark_names:
            times = config.times.get(benchmark_name, [])
            if not times:
                means[config.name].append(0)
                stds[config.name].append(0)
            else:
                means[config.name].append(numpy.mean(times))
                stds[config.name].append(numpy.std(times))

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

    all_benchmark_names_show = [cn(n).split('-')[0] for n in all_benchmark_names]
    plt.xlabel('')
    plt.ylabel('Time in seconds (Less is better)')
    plt.title('NumPy/Python programs')
    plt.yticks(numpy.arange(0,1.5,step=0.5))
    plt.xticks(index + ((bar_width*4)/2.0), all_benchmark_names_show, rotation=60)
    plt.legend()

    for line in ax.get_xticklines() + ax.get_yticklines():
        line.set_markersize(0)

    plt.tight_layout()
    plt.savefig('test.pdf')
    plt.show()
