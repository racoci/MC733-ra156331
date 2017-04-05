import numpy as np
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import cm
from itertools import *

gcc = np.array([[[[0.0457, 0.0320],[0.0457, 0.0320],[0.0457, 0.0320]],[[0.0108, 0.0254],[0.0115, 0.0266],[0.0117, 0.0267]],[[0.0044, 0.0235],[0.0054, 0.0252],[0.0054, 0.0253]],[[0.0029, 0.0230],[0.0039, 0.0248],[0.0036, 0.0251]],[[0.0025, 0.0225],[0.0034, 0.0246],[0.0031, 0.0247]]],[[[0.0261, 0.0308],[0.0261, 0.0308],[0.0261, 0.0308]],[[0.0063, 0.0239],[0.0067, 0.0252],[0.0068, 0.0253]],[[0.0026, 0.0220],[0.0032, 0.0237],[0.0032, 0.0239]],[[0.0017, 0.0215],[0.0023, 0.0232],[0.0021, 0.0236]],[[0.0014, 0.0210],[0.0020, 0.0230],[0.0018, 0.0233]]],[[[0.0160, 0.0222],[0.0160, 0.0222],[0.0160, 0.0222]],[[0.0039, 0.0163],[0.0042, 0.0172],[0.0042, 0.0172]],[[0.0017, 0.0150],[0.0021, 0.0161],[0.0021, 0.0162]],[[0.0011, 0.0146],[0.0015, 0.0157],[0.0014, 0.0160]],[[0.0009, 0.0144],[0.0013, 0.0155],[0.0011, 0.0159]]],[[[0.0109, 0.0170],[0.0109, 0.0170],[0.0109, 0.0170]],[[0.0029, 0.0112],[0.0031, 0.0120],[0.0032, 0.0119]],[[0.0014, 0.0101],[0.0017, 0.0110],[0.0017, 0.0110]],[[0.0009, 0.0098],[0.0012, 0.0107],[0.0011, 0.0109]],[[0.0007, 0.0096],[0.0010, 0.0105],[0.0009, 0.0107]]],[[[0.0086, 0.0142],[0.0086, 0.0142],[0.0086, 0.0142]],[[0.0024, 0.0078],[0.0025, 0.0086],[0.0026, 0.0084]],[[0.0013, 0.0068],[0.0015, 0.0076],[0.0016, 0.0075]],[[0.0008, 0.0065],[0.0011, 0.0072],[0.0011, 0.0073]],[[0.0006, 0.0064],[0.0009, 0.0071],[0.0008, 0.0072]]]], dtype = np.float64)
mesa = np.array([[[[0.0459, 0.0022],[0.0459, 0.0022],[0.0459, 0.0022]],[[0.0000, 0.0021],[0.0000, 0.0022],[0.0000, 0.0022]],[[0.0000, 0.0021],[0.0000, 0.0022],[0.0000, 0.0022]],[[0.0000, 0.0021],[0.0000, 0.0022],[0.0000, 0.0022]],[[0.0000, 0.0021],[0.0000, 0.0022],[0.0000, 0.0022]]],[[[0.0255, 0.0017],[0.0255, 0.0017],[0.0255, 0.0017]],[[0.0000, 0.0016],[0.0000, 0.0017],[0.0000, 0.0017]],[[0.0000, 0.0016],[0.0000, 0.0017],[0.0000, 0.0017]],[[0.0000, 0.0016],[0.0000, 0.0017],[0.0000, 0.0017]],[[0.0000, 0.0016],[0.0000, 0.0017],[0.0000, 0.0017]]],[[[0.0151, 0.0009],[0.0151, 0.0009],[0.0151, 0.0009]],[[0.0000, 0.0008],[0.0000, 0.0009],[0.0000, 0.0008]],[[0.0000, 0.0008],[0.0000, 0.0008],[0.0000, 0.0008]],[[0.0000, 0.0008],[0.0000, 0.0008],[0.0000, 0.0008]],[[0.0000, 0.0008],[0.0000, 0.0008],[0.0000, 0.0008]]],[[[0.0092, 0.0005],[0.0092, 0.0005],[0.0092, 0.0005]],[[0.0000, 0.0004],[0.0000, 0.0004],[0.0000, 0.0004]],[[0.0000, 0.0004],[0.0000, 0.0004],[0.0000, 0.0004]],[[0.0000, 0.0004],[0.0000, 0.0004],[0.0000, 0.0004]],[[0.0000, 0.0004],[0.0000, 0.0004],[0.0000, 0.0004]]],[[[0.0059, 0.0073],[0.0059, 0.0073],[0.0059, 0.0073]],[[0.0000, 0.0003],[0.0000, 0.0004],[0.0000, 0.0004]],[[0.0000, 0.0002],[0.0000, 0.0002],[0.0000, 0.0002]],[[0.0000, 0.0002],[0.0000, 0.0002],[0.0000, 0.0002]],[[0.0000, 0.0002],[0.0000, 0.0002],[0.0000, 0.0002]]]], dtype = np.float64)
galgel = np.array([[[[0.0236, 0.2730],[0.0236, 0.2730],[0.0236, 0.2730]],[[0.0001, 0.2104],[0.0001, 0.2341],[0.0001, 0.2285]],[[0.0001, 0.1823],[0.0001, 0.2155],[0.0001, 0.1947]],[[0.0000, 0.1706],[0.0001, 0.2166],[0.0001, 0.1877]],[[0.0000, 0.1619],[0.0001, 0.2182],[0.0001, 0.1867]]],[[[0.0120, 0.2730],[0.0120, 0.2730],[0.0120, 0.2730]],[[0.0000, 0.2104],[0.0000, 0.2341],[0.0000, 0.2285]],[[0.0000, 0.1823],[0.0000, 0.2155],[0.0000, 0.1947]],[[0.0000, 0.1706],[0.0000, 0.2167],[0.0000, 0.1877]],[[0.0000, 0.1619],[0.0000, 0.2182],[0.0000, 0.1867]]],[[[0.0060, 0.1848],[0.0060, 0.1848],[0.0060, 0.1848]],[[0.0000, 0.1450],[0.0000, 0.1596],[0.0000, 0.1573]],[[0.0000, 0.1291],[0.0000, 0.1472],[0.0000, 0.1371]],[[0.0000, 0.1239],[0.0000, 0.1469],[0.0000, 0.1331]],[[0.0000, 0.1217],[0.0000, 0.1473],[0.0000, 0.1338]]],[[[0.0032, 0.1406],[0.0032, 0.1406],[0.0032, 0.1406]],[[0.0000, 0.1154],[0.0000, 0.1243],[0.0000, 0.1253]],[[0.0000, 0.1092],[0.0000, 0.1159],[0.0000, 0.1159]],[[0.0000, 0.1140],[0.0000, 0.1150],[0.0000, 0.1174]],[[0.0000, 0.1276],[0.0000, 0.1147],[0.0000, 0.1250]]],[[[0.0017, 0.1203],[0.0017, 0.1203],[0.0017, 0.1203]],[[0.0000, 0.1064],[0.0000, 0.1115],[0.0000, 0.1135]],[[0.0000, 0.1026],[0.0000, 0.1071],[0.0000, 0.1131]],[[0.0000, 0.1040],[0.0000, 0.1055],[0.0000, 0.1151]],[[0.0000, 0.1050],[0.0000, 0.1055],[0.0000, 0.1182]]]], dtype = np.float64)
art = np.array([[[[0.0004, 0.5575],[0.0004, 0.5575],[0.0004, 0.5575]],[[0.0001, 0.5500],[0.0001, 0.5566],[0.0001, 0.5511]],[[0.0001, 0.5496],[0.0001, 0.5566],[0.0001, 0.5507]],[[0.0001, 0.5495],[0.0001, 0.5696],[0.0001, 0.5507]],[[0.0001, 0.5495],[0.0001, 0.5753],[0.0001, 0.5507]]],[[[0.0002, 0.5579],[0.0002, 0.5579],[0.0002, 0.5579]],[[0.0001, 0.5504],[0.0001, 0.5570],[0.0001, 0.5515]],[[0.0001, 0.5499],[0.0001, 0.5569],[0.0001, 0.5510]],[[0.0001, 0.5499],[0.0001, 0.5700],[0.0001, 0.5510]],[[0.0001, 0.5499],[0.0001, 0.5757],[0.0001, 0.5510]]],[[[0.0002, 0.4674],[0.0002, 0.4674],[0.0002, 0.4674]],[[0.0000, 0.4519],[0.0000, 0.4639],[0.0000, 0.4534]],[[0.0000, 0.4495],[0.0000, 0.4626],[0.0000, 0.4514]],[[0.0000, 0.4494],[0.0000, 0.4755],[0.0000, 0.4513]],[[0.0000, 0.4494],[0.0000, 0.4813],[0.0000, 0.4513]]],[[[0.0001, 0.4216],[0.0001, 0.4216],[0.0001, 0.4216]],[[0.0000, 0.3970],[0.0000, 0.4154],[0.0000, 0.4007]],[[0.0000, 0.3940],[0.0000, 0.4133],[0.0000, 0.3971]],[[0.0000, 0.3939],[0.0000, 0.4258],[0.0000, 0.3969]],[[0.0000, 0.3940],[0.0000, 0.4312],[0.0000, 0.3970]]],[[[0.0001, 0.3923],[0.0001, 0.3923],[0.0001, 0.3923]],[[0.0000, 0.3569],[0.0000, 0.3824],[0.0000, 0.3636]],[[0.0000, 0.3492],[0.0000, 0.3792],[0.0000, 0.3563]],[[0.0000, 0.3483],[0.0000, 0.3909],[0.0000, 0.3562]],[[0.0000, 0.3508],[0.0000, 0.3958],[0.0000, 0.3562]]]], dtype = np.float64)

d = {'gcc': gcc,'mesa': mesa,'galgel': galgel,'art': art}

def plot3d(X, Y, Z, nome):
	X = np.log2(X)
	Y = np.log2(Y)
	X,Y = np.meshgrid(X,Y)

	fig = plt.figure()
	ax = fig.gca(projection='3d')

	for i, c, cmap_name in zip((0,1,2),('r', 'g', 'b'),('Reds', 'Greens', 'Blues')):
		ax.plot_surface(X, Y, Z[...,i], color = c, alpha=0.3)
		
		cset = ax.contour(X, Y, Z[...,i], zdir='z',  cmap=plt.get_cmap(cmap_name))
		cset = ax.contour(X, Y, Z[...,i], zdir='x',  cmap=plt.get_cmap(cmap_name))
		cset = ax.contour(X, Y, Z[...,i], zdir='y',  cmap=plt.get_cmap(cmap_name))

	'''
	cset = ax.contour(X, Y, Z, zdir='z', offset=-100, cmap=cm.coolwarm)
	cset = ax.contour(X, Y, Z, zdir='x', offset=-40, cmap=cm.coolwarm)
	cset = ax.contour(X, Y, Z, zdir='y', offset=40, cmap=cm.coolwarm)
	'''
	ax.set_xlabel('lg(Block Size)')
	#ax.set_xlim(4, 64)
	ax.set_ylabel('lg(Associativity)')
	#ax.set_ylim(1, 16)
	ax.set_zlabel('Demand miss rate')
	#ax.set_zlim(0, 1)
	ax.set_title(nome)

	plt.show()



x = np.array([4, 8, 16, 32, 64])
y = np.array([1, 2, 4, 8, 16])

for nome in d:
	plot3d(x, y, d[nome][...,0], nome+"_i")
	plot3d(x, y, d[nome][...,1], nome+"_d")