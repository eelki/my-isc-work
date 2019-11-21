import numpy.ma as MA
import numpy as np

#marr = MA.masked_array(range(10), fill_value = -999)
#print(marr)

#marr[2] = MA.masked
#print(marr)

#print(marr.mask)

#narr = MA.masked_where(marr > 6, marr)
#print(narr)

#print(MA.filled(narr))

#print(type(MA.filled(narr)))

m1 = MA.masked_array(range(1, 9))
print(m1)

m2 = m1.reshape(2, 4)
print(m2)

m3 = MA.masked_where(m2 > 6, m2)
print(m3)

print(m3*100)

print(m3 - np.ones((2, 4)))

print(type(m3 - np.ones((2, 4))))
