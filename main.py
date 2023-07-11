from core.Simulation import Simulation

simulation = Simulation()
simulation.simulate_in_real_time(call_back=lambda x: print("HA"))
