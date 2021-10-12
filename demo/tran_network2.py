# import SpicePy modules
import sys
sys.path.insert(1, "../")
import netlist as ntl
from netsolve import net_solve
import matplotlib.pyplot as plt
plt.ion()

# read netlist
net = ntl.Network('tran_network2.net')

# compute the circuit solution
net_solve(net)

# plot results
net.plot()