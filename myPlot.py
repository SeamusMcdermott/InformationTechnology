import matplotlib.pyplot as plt

xlist = [1,1,2,5,3,7,2,1,10,10]
ylist = ['ed', 'roxy', 'danielle', 'jake', 'donnie', 'armanie', 'reidun', 'alice', 'daemon', 'max diamond']

plt.xlabel("Friends")
plt.ylabel("People")

plt.title("My Plot!!!")

plt.plot(xlist,ylist,'bd')

plt.show()