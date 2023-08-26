import json
import numpy 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patches as mpatch
from matplotlib.patches import Ellipse, Arc
import mpl_toolkits.mplot3d.art3d as art3d
import math 
import matplotlib.pyplot
from pathlib import Path
import os

xsize = []
ysize = []
zsize = []

Drct    = open(os.getcwd()+'/app/link/script.dir', "r" ).read()
Methods = open(os.getcwd()+'/app/link/script00.py', "r" ).read()

FileName = (Path(Drct).stem)


if Methods == 'NEM':
    with open(Drct) as json_data:
        data = json.load(json_data)
        xsize = data['Data']['Parameters']['X-Assembly Size']
        ysize = data['Data']['Parameters']['Y-Assembly Size']
        zsize = data['Data']['Parameters']['Z-Assembly Size']

def add_one_by_one_gen(l):
    cumsum = 0
    for i in l:
        cumsum += i
        yield cumsum

xs = list(add_one_by_one_gen(xsize))
zs = list(add_one_by_one_gen(zsize))
if ysize != xsize:
    ysize.reverse()
ys = list(add_one_by_one_gen(ysize))

def RdPower(self):
    data = np.loadtxt('app/Output/RadialPower.out')
    max_columns = len(data[0]) - 1
    max_rows = len(data) -1
    x = [data[rownum+1][0] for rownum in range(max_rows)] 
    y = [data[0][colnum + 1] for colnum in range(max_columns)]
    z = [[data[rownum+1][colnum + 1] for rownum in range(max_rows)] for colnum in range(max_columns)]
    x = np.array(x)
    y = np.array(y)
    z = np.array(z)
    x,y = np.meshgrid(x, y)
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_xlabel('X [cm]')                         
    ax.set_ylabel('Y [cm]') 
    im = ax.imshow(z, interpolation='bilinear', cmap='jet', 
             origin='lower', extent=[0, abs(x).max(), 0,abs(y).max()])
    clb = fig.colorbar(im)
    #ax.set_xticklabels([])
    #ax.set_yticklabels([])
    #clb.ax.set_title('Peaking Factor Distribution ', loc='left', fontsize=9)
    #plt.xticks(rotation=45)
    #plt.yticks(rotation=45)
    #ax.xaxis.tick_top()
    clb.set_label('Power Density')
    plt.xticks(xs)
    plt.yticks(ys)
    plt.title("Radial Power Distribution")
    plt.show()

def AxPower1(self):
    data = np.loadtxt('app/Output/AxialPower.out')
    max_columns = len(data[0]) - 1
    max_rows = len(data) - 1
    x = [data[0][colnum + 1] for colnum in range(max_columns)]
    y = [data[rownum+1][0] for rownum in range(max_rows)] 
    z = [[data[rownum+1][colnum + 1] for rownum in range(max_rows)] for colnum in range(max_columns)]
    x = np.array(x).T
    y = np.array(y).T
    z = np.array(z).T
    x,y = np.meshgrid(x, y)
    fig = matplotlib.pyplot.figure()
    ax = fig.add_subplot(111)
    ax.set_ylabel('Core Height(cm)') 
    im = ax.imshow(z, interpolation='bilinear', cmap='jet', 
             origin='lower', extent=[0, abs(x).max(), 0,abs(y).max()])
    clb = fig.colorbar(im)
    clb.set_label('Power Density')
    plt.title("Axial Power Distribution")

    # Show the plot.
    plt.show()

def AxPower2(self):
    data = np.loadtxt('app/Output/AxialPower.out')
    max_columns = len(data[0]) - 1
    max_rows = len(data) - 1
    x = [data[rownum+1][0] for rownum in range(max_rows)] 
    y = [data[rownum+1][1] for rownum in range(max_rows)] 
    x = np.array(x)
    y = np.array(y)
    plt.hexbin(y,x, gridsize=30, cmap='Blues')
    plt.xlabel('Power')
    plt.ylabel('Core Height(cm)')
    plt.title('Axial Power Distribution')
    plt.show()

def Flux(self):
    with open(Drct) as json_data:
         datas = json.load(json_data)
         ng = datas['Data']['Parameters']['Number of Energy Groups']         
    data = []
    # M00 = open('app/link/script00.py', "r" ).read()
    # if M00 == 'NEM':
        # data = np.loadtxt('app/Output/FluxGr1.out')
    # else:
        # QMessageBox.warning(self, "Warning", "select the calculation method.")

    for i in range(ng):   
        data = np.loadtxt('app/Output/FluxGr '+str(i+1))
        max_columns = len(data[0]) - 1
        max_rows = len(data) -1
        x = [data[rownum+1][0] for rownum in range(max_rows)] 
        y = [data[0][colnum + 1] for colnum in range(max_columns)]
        z = [[data[rownum+1][colnum + 1] for rownum in range(max_rows)] for colnum in range(max_columns)]
        x = np.array(x)
        y = np.array(y)
        z = np.array(z)
        x,y = np.meshgrid(x, y)
        fig = matplotlib.pyplot.figure()
        ax = fig.add_subplot(111)
        ax.set_xlabel('X [cm]')                         
        ax.set_ylabel('Y [cm]') 
        ax.set_title('Energy Group '+str(i+1),  loc='right', fontsize=10)
        im = ax.imshow(z, interpolation='bilinear', cmap='jet', 
                 origin='lower', extent=[0, abs(x).max(), 0,abs(y).max()])
        clb = fig.colorbar(im, format='%.1E')
        #ax.set_xticklabels([])
        #ax.set_yticklabels([])
        #clb.ax.set_title('Peaking Factor Distribution ', loc='left', fontsize=9)
        #plt.xticks(rotation=45)
        #plt.yticks(rotation=45)
        #ax.xaxis.tick_top()
        clb.set_label('Flux Density')
        plt.xticks(xs)
        plt.yticks(ys)
        plt.title('Radial Flux Distribution', loc='left')
        plt.show()
        
def Visualization2D(self):
    assm =[[]]
    plannar = []
    pin = []
    regmat = []
    nom    = []
    width_x = []
    width_y = []
    with open(Drct) as json_data:
        data = json.load(json_data)
        nmat = data['Data']['Parameters']['Number of Materials']
        nx = data['Data']['Parameters']['Number of X-Assembly']  # Number of Pin Cell
        ny = data['Data']['Parameters']['Number of Y-Assembly']  # Number of Pin Cell
        np  = data['Data']['Parameters']['Number of Planar'] 
        # xsize = data['Data']['Parameters']['X-Assembly Size']
        # ysize = data['Data']['Parameters']['Y-Assembly Size']
        plannar = data['Data']['XY_Assembly']

        # if FileName == ('IAEA_2D' or 'Ad_IAEA_2D'):
            # plannar[0].reverse()

        # for i in range(np):
            # plannar.append(data['Data']['Assemblies'][i]['Assembly'])
        # for p in range(np):
        # for i in range(npc):
            # pin.append(data['data']['PinCells'][i]['mat_fill'])
        for p in range(np) :
            Height = len(plannar[p])
            width = len(plannar[p])
            assm =numpy.zeros(((Height),(width)),dtype='i')

            i1=0
            # for j in range(len(core[0])):
            for k in range(len(plannar[p])):
                    # for m in range(len(pin[0])):
                i2=0
                        # for i in range(len(core[0])):
                for l in range(len(plannar[p])):
                                # for n in range(len(pin[0])):
                    assm[i1][i2] = plannar[p][k][l]
                    i2+=1
                i1+=1
            # nx = len(np.amax(data['Data']['Core'],axis=0))
            # ny = len(np.amax(data['Data']['Core'],axis=1))
                
            nxx = len(plannar[p])
            nyy = len(plannar[p])
            NX = nxx
            NY = nyy
            width_x.append(data['Data']['Parameters']['X-Assembly Size'])
            width_y.append(data['Data']['Parameters']['Y-Assembly Size'])
            # nx =  len(width_x[0])*NX
            # ny =  len(width_y[0])*NY
            xcm  = width_x[0]*NX
            ycm  = width_x[0]*NY
            for j in range(nmat):
                nom.append(data['Data']['Materials'][j]['Name'])
            # for i in range(npc):
                # regmat.append(data['data']['PinCells'][i]['mat_fill'])
            fig, ax = plt.subplots()
            widthx = [0]
            widthy = [0]
            somx = [0]
            somy = [0]
            for i in range(nx):
                widthx.append(xcm[i])
                somx.append(sum(widthx))
            for j in range(ny):
                widthy.append(ycm[j])
                somy.append(sum(widthy))
            rectangles = []
            red_patch = []
            mx = somx[0]
            my = somy[0]

            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.72, box.height])
            for i in range(nx):
                for j in range(ny):
                    rectangles.append(mpatch.Rectangle((somx[i],somy[j]), xcm[i], ycm[j],linewidth=0.0,edgecolor='k'))
            colr = ['#33A1C9','#DC143C','#00C78C','#FFEC8B','#00FFFF','#FA8072', 
                    '#FFC1C1','#ACFFC7','Black', '#c2c2f0', '#ffb3e6', 
                    '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6','White']
            for i in range(nmat):
                red_patch.append(mpatches.Patch(color=colr[i], label=nom[i]))
            n=nx-1
            m=0
            for r in rectangles:
                ax.add_artist(r) 
                if assm[n][m]== 0 :
                    r.set_facecolor(color='white')
                else :
                    r.set_facecolor(color=colr[int(assm[n][m])-1])

                rx, ry = r.get_xy()
                cx = rx + r.get_width()/2.0
                cy = ry + r.get_height()/2.0
                n-=1
                if (n<0):
                    n=nx-1
                    m+=1
            ax.set_ylim((min(somy), max(somy)))
            ax.set_xlim((min(somx), max(somx)))
            #ax.set_xticklabels([])
            #ax.set_yticklabels([]) 
            ax.set_xlabel('X [cm]')
            ax.set_ylabel('Y [cm]')
            ax.set_title('Planar '+str(p+1),  loc='left', fontsize=10)
            ax.set_title('Radial Geometry',  loc='center')
            clb = plt.legend(handles=red_patch, loc='center left', title="Materials", fontsize='small', bbox_to_anchor=(1, 0.5))
            plt.xticks(xs, rotation=90)
            plt.yticks(ys)
            plt.show()

def AxiGeo2D(self):
    assm =[[]]
    plannar = []
    pin = []
    regmat = []
    nom    = []
    width_x = []
    width_y = []
    with open(Drct) as json_data:
        data = json.load(json_data)
        nmat = data['Data']['Parameters']['Number of Materials']
        nx = data['Data']['Parameters']['Number of X-Assembly']  # Number of Pin Cell
        nz = data['Data']['Parameters']['Number of Z-Assembly']  # Number of Pin Cell
        np  = data['Data']['Parameters']['Number of Planar'] 
        # xsize = data['Data']['Parameters']['X-Assembly Size']
        # ysize = data['Data']['Parameters']['Y-Assembly Size']
        # plannar = data['Data']['Core2']

        plannar.append(data['Data']['Z_Assembly'])
        width  = nx
        Height = nz
        assm =numpy.zeros(((Height),(width)),dtype='i')

        i1=0
        for k in range(nz):
            i2=0
            for l in range(nx):
                assm[i1][i2] = plannar[0][k][l]
                i2+=1
            i1+=1                

        width_x.append(data['Data']['Parameters']['X-Assembly Size'])
        width_y.append(data['Data']['Parameters']['Z-Assembly Size'])
        xcm  = width_x[0]*nx
        ycm  = width_y[0]*nz
        for j in range(nmat):
            nom.append(data['Data']['Materials'][j]['Name'])
        fig, ax = plt.subplots()
        widthx = [0]
        widthy = [0]
        somx = [0]
        somy = [0]
        for i in range(nx):
            widthx.append(xcm[i])
            somx.append(sum(widthx))
        for j in range(nz):
            widthy.append(ycm[j])
            somy.append(sum(widthy))
        rectangles = []
        red_patch = []
        mx = somx[0]
        my = somy[0]

        box = ax.get_position()
        ax.set_position([box.x0, box.y0, box.width * 0.75, box.height])
        for i in range(nx):    
            for j in range(nz):

                rectangles.append(mpatch.Rectangle((somx[i],somy[j]), xcm[i], ycm[j],linewidth=0.0,edgecolor='k'))
        colr = ['#33A1C9','#DC143C','#00C78C','#FFEC8B','#00FFFF','#FA8072', 
                    '#FFC1C1','#ACFFC7','Black', '#c2c2f0', '#ffb3e6',
                        '#ffb3e6', '#c2c2f0','#ffb3e6', '#c2c2f0','#ffb3e6']
        for i in range(nmat):
            red_patch.append(mpatches.Patch(color=colr[i], label=nom[i]))
        n=nz-1
        m=0
        for r in rectangles:
            ax.add_artist(r) 
            if assm[n][m]== 0 :
                r.set_facecolor(color='white')
            else :
                r.set_facecolor(color=colr[int(assm[n][m])-1])

            rx, ry = r.get_xy()
            cx = rx + r.get_width()/2.0
            cy = ry + r.get_height()/2.0
            n-=1
            if (n<0):
                n=nz-1
                m+=1
        ax.set_ylim((min(somy), max(somy)))
        ax.set_xlim((min(somx), max(somx)))
                #ax.set_xticklabels([])
                #ax.set_yticklabels([]) 
        ax.set_xlabel('X [cm]')
        ax.set_ylabel('Z [cm]')
        ax.set_title('Axial Geometry ',  loc='center')
        clb = plt.legend(handles=red_patch, loc='center left', title="Materials", fontsize='small', bbox_to_anchor=(1, 0.5))
        plt.xticks(xs, rotation=90)
        plt.yticks(zs)
        plt.show()


