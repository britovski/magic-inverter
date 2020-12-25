import os

for delay in range(900, 1000, 1):
    print(delay)
    plot = "%04d" % delay

    sim = open("simulation.spice").read()
    sim = sim.replace("DELAY", str(delay))
    sim = sim.replace("PLOT", plot)

    sim_name = "spices/%d.spice" % delay
    with open(sim_name, 'w') as fh:
        fh.write(sim)

    os.system("ngspice %s" % sim_name)