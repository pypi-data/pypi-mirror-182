# traice

Tiny yet useful tool for consistent model training logs generation.

# Installation

To install through pip use the following command:

```sh
pip install traicer
```

The tool requires only `pandas` package to be installed. However, there is `environment.yml` file which can be used for the same environment which is used for developing the tool:

```sh
conda env create -f environment.yml
```

# Usage

The tool may be used as follows (see `examples/dummy.py`):

```py
from random import seed, uniform
from time import time, sleep

from traice import Traicer

traicer = Traicer()


def train_step():
    sleep(uniform(0, 1))


seed(17)

init_timestamp = time()

for i in range(1, 5):
    start_timestamp = time()
    train_step()
    traicer.push(i, uniform(0, 1 / i), (time_ := time()) - start_timestamp, time_ - init_timestamp)

print(traicer.df)
```

Essentially, it accumulates all `push` arguments in a list which is then converted to a dataframe. The example produces the following log (the last two columns may differ a bit):

```sh
   epoch      loss      time  cumulative_time
0      1  0.806691  0.522609         0.522609
1      2  0.144813  0.961565         1.484184
2      3  0.234740  0.767061         2.251254
3      4  0.027541  0.661659         2.912921
```

# Testing

To run test execute the following statement in your terminal:

```sh
python -m unittest discover test
```
