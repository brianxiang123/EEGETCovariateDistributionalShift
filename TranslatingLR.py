import numpy as np
import math

def main():
    dminh = np.load('./Tasks/Direction_task_with_dots_synchronised_min_hilbert.npz')
    dmin = np.load('./Tasks/Direction_task_with_dots_synchronised_min.npz')
    dmaxh = np.load('./Tasks/Direction_task_with_dots_synchronised_max_hilbert.npz')
    dmax = np.load('./Tasks/Direction_task_with_dots_synchronised_max.npz')

    ldminh = dminh['labels']
    ldmin = dmin['labels']
    ldmaxh = dmaxh['labels']
    ldmax = dmax['labels']

    print("cdminh")
    cdminh = leftrighttrans1(ldminh[:,2])
    print("cdmin")
    cdmin = leftrighttrans1(ldmin[:,2])
    print("cdmaxh")
    cdmaxh = leftrighttrans1(ldmaxh[:,2])
    print("cdmax")
    cdmax = leftrighttrans1(ldmax[:,2])

    ndminh = np.vstack((ldminh[:,0], cdminh)).T
    ndmin = np.vstack((ldmin[:,0], cdmin)).T
    ndmaxh = np.vstack((ldmaxh[:,0], cdmaxh)).T
    ndmax = np.vstack((ldmax[:,0], cdmax)).T

    np.savez('./Tasks/LR_task_with_dots_synchronised_min_hilbert.npz', EEG = dminh['EEG'], labels = ndminh)
    np.savez('./Tasks/LR_task_with_dots_synchronised_min.npz', EEG = dmin['EEG'], labels = ndmin)
    np.savez('./Tasks/LR_task_with_dots_synchronised_max_hilbert.npz', EEG = dmaxh['EEG'], labels = ndmaxh)
    np.savez('./Tasks/LR_task_with_dots_synchronised_max.npz', EEG = dmax['EEG'], labels = ndmax)


def leftrighttrans1(rarr):
    narr = []
    cnt1 = 0
    cnt2 = 0
    for i in range(len(rarr)):
        if abs(rarr[i]) < math.pi/2:
            narr.append(1)
            cnt1+=1
        else:
            narr.append(0)
            cnt2+=1
    print("Right: " + str(cnt1))
    print("Left: " + str(cnt2))
    return narr

main()
