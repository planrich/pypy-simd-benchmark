#! /usr/bin/env python2
import subprocess
import re
import sys
import numpy as np

class Config(object):
    def __init__(self, name, exe, params):
        self.name = name
        self.exe = exe
        self.params = params
        self.fd = None
        self.time_matcher = re.compile("^time: (\d+\.\d+)$")
        self.times = {}

    def setup(self, suffix):
        pass
        #self.baseline = baseline is None
        #if baseline is not None:
        #    self.fd = open('%s%s.dat' % (self.name,suffix), 'wb')
        #    self.fd.write("x\ty\tstd\n")
        #    self.baselines = baseline.baselines

    def teardown(self):
        pass

    def benchname(self):
        return self.benchname

    def log(self, output, run, arg):
        benchname = '%s-%s' % (run.name, '-'.join(unfold_args(arg)))
        for line in output.splitlines():
            match = self.time_matcher.match(line)
            if match:
                self.times.setdefault(benchname,[]).append(float(match.group(1)))

    def runkey(self, name, arg):
        return '%s-%s' % (name,arg)

    def mean_log(self, key):
        t = [float(x[1]) for x in self.times]
        mean = np.mean(t)
        std = np.std(t)
        if self.baseline:
            self.baselines[key] = (key, mean, std)
        else:
            baseline = self.baselines[key]
            assert baseline is not None
            m = baseline[1] / mean
            v = std
            self.fd.write("%s\t%s\t%s\n" % (key, m, v))

def unfold_args(args):
    if isinstance(args, tuple):
        return [str(s) for s in args]
    return [str(args)]

class Run(object):
    def __init__(self, name, args, exclude=None):
        self.name = name
        self.args = args
        self.exclude = exclude or []

    def benchmark(self, config):
        for arg in self.args.params:
            cmd = [config.exe] + config.params + ['%s.py' % self.name] + unfold_args(arg)
            for i in range(TIMES):
                print "run) config %s run %s arg %s\n cmd) %s" % (config.name, self.name, arg, ' '.join(cmd))
                proc = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
                stdout, stderr = proc.communicate()
                config.log(stdout,self,arg)
                print stderr

class Args(object):
    def __init__(self, params):
        self.params = params

to_run = [
    #Run('add', Args([2000,3000])),
    Run('dot', Args([1000,2000,3000])),
    Run('som', Args([32,386,512])),
]

FAST = "--fast" in sys.argv
try:
    idx = sys.argv.index("--times")
    TIMES = int(sys.argv[idx+1])
except ValueError:
    TIMES = 1

if FAST:
    del sys.argv[sys.argv.index('--fast')]
    to_run = [
        #Run('np/dot', Args([500])),
        #Run('np/som', Args([32])),
        Run('user/array_add', Args([(1000,10000),(1500,10000),(2500,10000)]), exclude=['python']),
        Run('user/array_sum', Args([(1000,10000),(1500,10000),(2500,10000)]), exclude=['python']),
        Run('user/fir', Args([(100,10000),(150,20000),(200,3000)]), exclude=['python']),
    ]

configs = [
    Config('python', '/home/rich/.virtualenvs/python/bin/python', []),
    Config('pypy', '/home/rich/.virtualenvs/portpypy/bin/python', []),
    Config('pypy-vec', '/home/rich/src/pypy/pypy-c', ['--jit','vec_all=1,vec=1'])
]

try:
    suffix = sys.argv[1]
except IndexError:
    suffix = ''
for config in configs:
    for run in to_run:
        if config.name in run.exclude:
            continue
        run.benchmark(config)

def cn(name):
    name = name.replace("np/", "")
    name = name.replace("user/", "")
    name = name.replace("_", "-")
    return name

for config in configs:
    print config.name
    for name, times in config.times.items():
        print " ", cn(name), ", mean:", np.mean(times), "std:", np.std(times), "|", times

