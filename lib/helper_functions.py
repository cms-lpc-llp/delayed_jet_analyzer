import numpy as np

def getRecoTime(algorithm,rechit_cut, rechit_time,rechit_energy):
    # 0 is energy weighted, 1 is energy squared weighted, 2 is median
    rechit_energy = rechit_energy[np.logical_not(rechit_time == -666)]
    rechit_time = rechit_time[np.logical_not(rechit_time == -666)]
    rechit_time = rechit_time[rechit_energy > rechit_cut]
    rechit_energy = rechit_energy[rechit_energy > rechit_cut]
    assert(len(rechit_time) == len(rechit_energy))
    if np.sum(rechit_energy) > 0.0 and len(rechit_time) > 0:
        if algorithm == 0:
            return np.sum(np.multiply(rechit_time,rechit_energy)/np.sum(rechit_energy))
        elif algorithm == 1:
            return np.sum(np.multiply(rechit_time,rechit_energy*rechit_energy)/np.sum(rechit_energy*rechit_energy))
        elif algorithm == 2:
            return np.median(rechit_time)
    else:
        return None
