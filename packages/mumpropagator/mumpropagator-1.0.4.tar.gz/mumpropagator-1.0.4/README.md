# mumpropagator
python class interface to MUM -- Muon Propagator developed by Igor Sokalski.

The reference: [Phys. Rev. D64:074015 (2001)](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.64.074015)

## Installation
```
pip install mumpropagator
```
## Usage
```
from mumpropagator import pymum
m = pymum.mum()
```
## Example
### from a python module
```
from mumpropagator import pymum_example
from mumpropagator.pymum_example import *
pymum_example.transport(opts)
```
opts is a namespace like the following
```
namespace(energy=1000.0,
          depth=1.0,
          n=1000,
          type=1,
          savefig=True,
          output='figures',
```
one can change these parameters before calling ``transport`` method.
