import numpy as np
import math
import math
@np.vectorize
def msq2(px1, py1, pz1, px2, py2, pz2, m1, m2):
    p1_sq = px1 ** 2 + py1 ** 2 + pz1 ** 2
    p2_sq = px2 ** 2 + py2 ** 2 + pz2 ** 2
    m1_sq = m1 ** 2
    m2_sq = m2 ** 2
    x1 = m1_sq / p1_sq
    x2 = m2_sq / p2_sq
    x = x1 + x2 + x1 * x2
    a = angle(px1, py1, pz1, px2, py2, pz2)
    cos_a = np.cos(a)
    if cos_a >= 0:
        y1 = (x + np.sin(a) ** 2) / (np.sqrt(x + 1) + cos_a) 
    else:
        y1 = -cos_a + np.sqrt(x + 1) 
    y2 = 2 * np.sqrt(p1_sq * p2_sq)
    return m1_sq + m2_sq + y1 * y2

# numerically stable calculation of angle
def angle(x1, y1, z1, x2, y2, z2):
    # cross product
    cx = y1 * z2 - y2 * z1
    cy = x1 * z2 - x2 * z1
    cz = x1 * y2 - x2 * y1
    
    # norm of cross product
    c = np.sqrt(cx * cx + cy * cy + cz * cz)
    
    # dot product
    d = x1 * x2 + y1 * y2 + z1 * z2
    
    return np.arctan2(c, d)
# naive implementation
def msq1(px1, py1, pz1, px2, py2, pz2, m1, m2):
    p1_sq = px1 ** 2 + py1 ** 2 + pz1 ** 2
    p2_sq = px2 ** 2 + py2 ** 2 + pz2 ** 2
    m1_sq = m1 ** 2
    m2_sq = m2 ** 2
    
    # energies of particles 1 and 2
    e1 = np.sqrt(p1_sq + m1_sq)
    e2 = np.sqrt(p2_sq + m2_sq)

    # dangerous cancelation in third term
    return m1_sq + m2_sq + 2 * (e1 * e2 - (px1 * px2 + py1 * py2 + pz1 * pz2))


def deltaPhi( phi1,  phi2):
    dphi = phi1-phi2
    while np.count_nonzero(dphi > math.pi)>0:
        dphi[dphi > math.pi] -= 2*math.pi
    while np.count_nonzero(dphi< -math.pi)>0:
        dphi[dphi < -math.pi] += 2*math.pi
    return dphi
def deltaR(eta1, phi1, eta2, phi2):
    dphi = deltaPhi(phi1,phi2)
    deta = eta1 - eta2
    return (dphi*dphi + deta*deta)**0.5

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
