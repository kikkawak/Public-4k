import numpy as np
import matplotlib.pyplot as plt
import scipy

"""sample data"""

z0     = np.exp(np.linspace(-10.,1.,111)) / np.exp(1.) * 4.
# print(np.linspace(-10.,1.,111))
value0 = np.sin(2.*np.pi*z0)
# print(z0)

"""interpolation"""

f1     = scipy.interpolate.interp1d(z0, value0, kind="linear",     bounds_error=False, fill_value=np.nan)
f2     = scipy.interpolate.interp1d(z0, value0, kind="quadratic",  bounds_error=False, fill_value=np.nan)
f3     = scipy.interpolate.interp1d(z0, value0, kind="cubic",      bounds_error=False, fill_value=np.nan)

z      = np.linspace(0.,4.,41)
value1 = f1(z)
value2 = f2(z)
value3 = f3(z)

"""plot"""

fig = plt.figure(figsize=(8,6),constrained_layout=True)
ax1 = fig.add_subplot(111)

ax1.plot(value0,z0, color='k', alpha=0.75, label='original')
ax1.scatter(np.zeros_like(z0), z0, marker='x', color='gray')

ax1.plot(value1,z, color='b', linestyle='dashed',   label='linear'   )
ax1.plot(value2,z, color='r', linestyle='dotted',   label='quadratic')
ax1.plot(value3,z, color='g', linestyle='dashdot',  label='cubic'    )
ax1.scatter(np.ones_like(z)*0.1, z, marker='x', color='lightgray')

"""detail"""

xtick      = np.linspace(-1.,1.,9)
xticklabel = ["{:.2f}".format(x) for x in xtick]
ax1.set_xlim(-1.,1.)
ax1.set_xticks(xtick)
ax1.set_xticklabels(xticklabel, fontsize=12)
ax1.set_xlabel('value', fontsize=18)
# ax1.set_xlabel('value',fontsize=8)

ytick      = np.linspace(0.,4.,9)
yticklabel = ["{:.2f}".format(y) for y in ytick]
ax1.set_ylim(0.,4.)
ax1.set_yticks(ytick)
ax1.set_yticklabels(yticklabel, fontsize=12)
ax1.set_ylabel('depth', fontsize=18)

# ax1.set_title('vertical profiles')
ax1.legend(loc='lower left', fontsize=12)
# ax1.legend()
ax1.grid()


"""show"""

plt.show()

"""save"""

# plt.savefig('./exmple_interpolate.png',dpi=300)
# plt.savefig('./exmple_interpolate.eps')
# plt.savefig('./exmple_interpolate.pdf')
