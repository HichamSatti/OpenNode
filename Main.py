"""  Building module "NEM"..."""
import app.NEM

import os
import json
from datetime import datetime

start  = datetime.now()

xdiv = []
ydiv = []
zdiv = []
xsize = []
ysize = []
zsize = []
zpln = []
assm = []
x_siga = []
x_sigtr = []
x_sigf = []
x_nu_sigf = []
chi = []
x_sigs = []
ds = []
sps = []
xpos = []
ypos = []
zpos = []
nk = 0

PATH    = open(os.getcwd()+'/app/link/script.dir', "r" ).read()
Methods = open(os.getcwd()+'/app/link/script00.py', "r" ).read()

if Methods == 'NEM':
    with open(PATH) as json_data:
        data = json.load(json_data)
        mode = data['Data']['Parameters']['Calculation Mode']
        ng = data['Data']['Parameters']['Number of Energy Groups']
        nmat = data['Data']['Parameters']['Number of Materials']
        order = data['Data']['Parameters']['Polynomial Order']
        nx = data['Data']['Parameters']['Number of X-Assembly']
        ny = data['Data']['Parameters']['Number of Y-Assembly']
        nz = data['Data']['Parameters']['Number of Z-Assembly']
        np = data['Data']['Parameters']['Number of Planar']
        x_east = data['Data']['Boundary Condition']['X_East']
        x_west = data['Data']['Boundary Condition']['X_West']
        y_north = data['Data']['Boundary Condition']['Y_North']
        y_south = data['Data']['Boundary Condition']['Y_South']
        z_top = data['Data']['Boundary Condition']['Z_Top']
        z_bott = data['Data']['Boundary Condition']['Z_Bottom']
        xdiv = data['Data']['Parameters']['X-Assembly Division']
        ydiv = data['Data']['Parameters']['Y-Assembly Division']
        zdiv = data['Data']['Parameters']['Z-Assembly Division']
        xsize = data['Data']['Parameters']['X-Assembly Size']
        ysize = data['Data']['Parameters']['Y-Assembly Size']
        zsize = data['Data']['Parameters']['Z-Assembly Size']
        zpln = data['Data']['Parameters']['Planar Assignement to Z']
        assm = data['Data']['XY_Assembly']
        # assmx = data['Data']['Z_Assembly']
        for i in range(nmat):
            x_siga.append(data['Data']['Materials'][i]['Absorption_XS'])
            x_sigtr.append(data['Data']['Materials'][i]['Transport_XS'])
            x_sigf.append(data['Data']['Materials'][i]['Fission_XS'])
            x_nu_sigf.append(data['Data']['Materials'][i]['Nu*Fission_XS'])
            chi.append(data['Data']['Materials'][i]['Chi'])
            x_sigs.append(data['Data']['Materials'][i]['Scattering_XS'])
        if mode == 'Fixed Source':
            ns = data['Data']['Fixed Source Parameters']['Source Number']
            npor = data['Data']['Fixed Source Parameters']['Radial FS Number']
            npox = data['Data']['Fixed Source Parameters']['Axial FS Number']
            for i in range(ns):
                ds.append(data['Data']['Fixed Source Parameters']['Source Parameters'][i]['Source Density'])
                sps.append(data['Data']['Fixed Source Parameters']['Source Parameters'][i]['Source Energy Spectrum'])
                xpos.append(data['Data']['Fixed Source Parameters']['Source Parameters'][i]['Radial FS Position (x)'])
                ypos.append(data['Data']['Fixed Source Parameters']['Source Parameters'][i]['Radial FS Position (y)'])
                zpos.append(data['Data']['Fixed Source Parameters']['Source Parameters'][i]['Axial FS Position'])

# ns=2
# ds=[10.0,20.0]
# sps = [[1.0,0.0],[1.0,0.0]]
# xpos = [[2, 2, 1, 0],[9, 8, 8, 0]]
# ypos = [[1, 0, 0, 0],[9, 0, 0, 0]]
# zpos = [[10, 1],[10, 1]]
""" Modes """
# mode = 'Forward'
# mode = 'Adjoint'
# mode = 'Fixed Source'

""" Forward """
# nx = 9
# ny = 9
# nz = 19
# ng = 2
# nmat = 5
# np=4
# xdiv = [1]*9
# ydiv = [1]*9
# zdiv = [1]*19
# xsize=[20]*8
# xsize.insert(0,10)
# ysize=[20]*8
# ysize.insert(8,10)
# zsize = [20]*19
# zpln=[1]
# zpln.extend([2]*13)
# zpln.extend([3]*4)
# zpln.extend([4])
# assm=[[[4,4,4,4,0,0,0,0,0],[4,4,4,4,4,4,0,0,0],[4,4,4,4,4,4,4,0,0],[4,4,4,4,4,4,4,4,0],[4,4,4,4,4,4,4,4,0],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4]],[[4,4,4,4,0,0,0,0,0],[1,1,1,4,4,4,0,0,0],[2,2,1,1,1,4,4,0,0],[2,2,2,2,1,1,4,4,0],[3,2,2,2,3,1,1,4,0],[2,2,2,2,2,2,1,4,4],[2,2,2,2,2,2,1,1,4],[2,2,2,2,2,2,2,1,4],[3,2,2,2,3,2,2,1,4]],[[4,4,4,4,0,0,0,0,0],[1,1,1,4,4,4,0,0,0],[2,2,1,1,1,4,4,0,0],[2,2,2,2,1,1,4,4,0],[3,2,2,2,3,1,1,4,0],[2,2,2,2,2,2,1,4,4],[2,2,3,2,2,2,1,1,4],[2,2,2,2,2,2,2,1,4],[3,2,2,2,3,2,2,1,4]],[[4,4,4,4,0,0,0,0,0],[4,4,4,4,4,4,0,0,0],[4,4,4,4,4,4,4,0,0],[4,4,4,4,4,4,4,4,0],[5,4,4,4,5,4,4,4,0],[4,4,4,4,4,4,4,4,4],[4,4,5,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[5,4,4,4,5,4,4,4,4]]]
# """# assm=[[[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,0],[4,4,4,4,4,4,4,4,0],[4,4,4,4,4,4,4,0,0],[4,4,4,4,4,4,0,0,0],[4,4,4,4,0,0,0,0,0]],[[3,2,2,2,3,2,2,1,4],[2,2,2,2,2,2,2,1,4],[2,2,2,2,2,2,1,1,4],[2,2,2,2,2,2,1,4,4],[3,2,2,2,3,1,1,4,0],[2,2,2,2,1,1,4,4,0],[2,2,1,1,1,4,4,0,0],[1,1,1,4,4,4,0,0,0],[4,4,4,4,0,0,0,0,0]],[[3,2,2,2,3,2,2,1,4],[2,2,2,2,2,2,2,1,4],[2,2,2,2,2,2,1,1,4],[2,2,2,2,2,2,1,4,4],[3,2,2,2,3,1,1,4,0],[2,2,2,2,1,1,4,4,0],[2,2,1,1,1,4,4,0,0],[1,1,1,4,4,4,0,0,0],[4,4,4,4,0,0,0,0,0]],[[5,4,4,4,5,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,5,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[5,4,4,4,5,4,4,4,0],[4,4,4,4,4,4,4,4,0],[4,4,4,4,4,4,4,0,0],[4,4,4,4,4,4,0,0,0],[4,4,4,4,0,0,0,0,0]]]"""
# """# assm=[[[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,4,4,4],[0,4,4,4,4,4,4,4,4],[0,4,4,4,4,4,4,4,4],[0,0,4,4,4,4,4,4,4],[0,0,0,4,4,4,4,4,4],[0,0,0,0,0,4,4,4,4]],[[4,1,2,2,3,2,2,2,3],[4,1,2,2,2,2,2,2,2],[4,1,1,2,2,2,2,2,2],[4,4,1,2,2,2,2,2,2],[0,4,1,1,3,2,2,2,3],[0,4,4,1,1,2,2,2,2],[0,0,4,4,1,1,1,2,2],[0,0,0,4,4,4,1,1,1],[0,0,0,0,0,4,4,4,4]],[[4,1,2,2,3,2,2,2,3],[4,1,2,2,2,2,2,2,2],[4,1,1,2,2,2,2,2,2],[4,4,1,2,2,2,2,2,2],[0,4,1,1,3,2,2,2,3],[0,4,4,1,1,2,2,2,2],[0,0,4,4,1,1,1,2,2],[0,0,0,4,4,4,1,1,1],[0,0,0,0,0,4,4,4,4]],[[4,4,4,4,5,4,4,4,5],[4,4,4,4,4,4,4,4,4],[4,4,4,4,4,4,5,4,4],[4,4,4,4,4,4,4,4,4],[0,4,4,4,5,4,4,4,5],[0,4,4,4,4,4,4,4,4],[0,0,4,4,4,4,4,4,4],[0,0,0,4,4,4,4,4,4],[0,0,0,0,0,4,4,4,4]]]"""
# x_sigtr=[[0.222222,0.833333],[0.222222,0.833333],[0.222222,0.833333],[0.166667,1.111111],[0.166667,1.111111]]
# x_siga=[[0.010,0.080],[0.010,0.085],[0.0100,0.1300],[0.000,0.010],[0.000,0.055]]
# x_nu_sigf=[[0.000,0.135],[0.000,0.135],[0.000,0.135],[0.000,0.000],[0.000,0.000]]
# x_sigf =[[0.000,0.135],[0.000,0.135],[0.000,0.135],[0.000,0.000],[0.000,0.000]]
# chi =[[1.0,0.0],[1.0,0.0],[1.0,0.0],[0.0,0.0],[0.0,0.0]]
# x_sigs =[[[0.1922,0.020],[0.000,0.7533]],[[0.1922,0.020],[0.000,0.7483]],[[0.1922,0.020],[0.000,0.7033]],[[0.1267,0.040],[0.000,1.1011]],[[0.000,0.040],[0.000,0.000]]]
# x_east = 1
# x_west = 2
# y_north = 2
# y_south = 1
# z_top = 1
# z_bott = 1
# order = 4




"""Constructing wrapper function "nodxyz"..."""
nxx,nyy,nzz = app.NEM.nodxyz(xdiv,ydiv,zdiv,[nx,ny,nz])

"""Constructing wrapper function "asmblg_delta"..."""
node,mnum,delx,dely,delz = app.NEM.asmblg_delta(nmat,nxx,nyy,nzz,xsize,ysize,zsize,xdiv,ydiv,zdiv,zpln,assm,[np,nx,ny,nz])

"""Constructing wrapper function "stagg"..."""
y_smax,y_smin,x_smax,x_smin = app.NEM.stagg(mnum,[nxx,nyy,nzz])

"""Constructing wrapper function "nod"..."""
nk = app.NEM.nod(nzz,y_smax,y_smin,[nyy])
print('nk=',nk)

"""Constructing wrapper function "posinod"..."""
ix,iy,iz,xyz,mat = app.NEM.posinod(y_smax,y_smin,nk,mnum,[nxx,nyy,nzz])

"""Constructing wrapper function "deltv"..."""
delv = app.NEM.deltv(delx,dely,delz,ix,iy,iz,[nk,nxx,nyy,nzz])
print('delv=',delv)

""" Constructing wrapper function "xd_xsigr"..."""
xd,x_sigr = app.NEM.xd_xsigr(x_siga,x_sigs,x_sigtr,[ng,nk])
# for g in range(ng):
    # print ('g=', g, ' x_sigr=', x_sigr[0][g])

"""Constructing wrapper function "title1"..."""
app.NEM.title1()

"""Constructing wrapper function "timestamp"..."""
app.NEM.timestamp()

"""Constructing wrapper function "output"..."""
app.NEM.output(nx,ny,delx,dely,delz,xd,x_sigr,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,zdiv,node,zpln,x_east,x_west,y_north,y_south,z_top,z_bott,mode,[ng,np,nmat,nz,nxx,nyy,nzz])

"""Constructing wrapper function "init"..."""
# keff,jo,ji,l0,al,f0,fx1,fy1,fz1,fx2,fy2,fz2 = NEM.init(ng,nk)
                  
"""Constructing wrapper function "xs_updt"..."""
# sigs,siga,sigtr,sigf,nu_sigf,d,sigr = NEM.xs_updt(mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,[ng,nk,nmat])

"""Constructing wrapper function "d_sigr"..."""
# d,sigr = NEM.d_sigr(siga,sigs,sigtr,[ng,nk])

"""Constructing wrapper function "nodal_coup4"..."""
# p4,r4 = NEM.nodal_coup4(delx,dely,delz,d,sigr,ix,iy,iz,[ng,nk,nxx,nyy,nzz])

"""Constructing wrapper function "nodal_coup2"..."""
# p2,r2 = NEM.nodal_coup2(delx,dely,delz,d,sigr,ix,iy,iz,[ng,nk,nxx,nyy,nzz])

"""Constructing wrapper function "outer"..."""
# NEM.outer(keff,f0,fx1,fy1,fz1,fx2,fy2,fz2,order,r2,p2,r4,p4,mat,al,jo,ji,l0,d,sigr,chi,sigs,nu_sigf,ix,iy,iz,delx,dely,delz,delv,xyz,x_smax,x_smin,y_smax,y_smin,x_east,x_west,y_north,y_south,z_top,z_bott,[ng,nk,nmat,nxx,nyy,nzz])

# if mode == 'Forward':
"""Constructing wrapper function "forward"..."""
    # app.NEM.forward(order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,[ng,nk,nx,ny,nz,nmat,nxx,nyy,nzz])

# if mode == 'Adjoint':
"""Constructing wrapper function "adjoint"..."""
    # app.NEM.adjoint(order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,[ng,nk,nx,ny,nz,nmat,nxx,nyy,nzz])

# if mode == 'Fixed Source':
"""Constructing wrapper function "fixedsrc"..."""
    # app.NEM.fixedsrc(order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,y_smax,y_smin,xdiv,ydiv,zdiv,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,ds,sps,zpos,xpos,ypos,mode,[ng,nk,nx,ny,nz,nmat,nxx,nyy,nzz,ns,npor,npox])

#######################   Print Extra Sources   #######################
"""Constructing wrapper function "exsrc"..."""
if mode == 'Fixed Source':
    esrc = app.NEM.exsrc(nk,ds,sps,xyz,xdiv,ydiv,zdiv,xpos,ypos,zpos,[ng,nx,ny,nz,nxx,nyy,nzz,ns,npox,npor])
    app.NEM.fixedsrc(order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,y_smax,y_smin,xdiv,ydiv,zdiv,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,esrc,[ng,nk,nx,ny,nz,nmat,nxx,nyy,nzz])
else: 
    """Constructing wrapper function "modes"..."""
    app.NEM.modes(order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,[ng,nk,nx,ny,nz,nmat,nxx,nyy,nzz])

"""Constructing wrapper function "outer4fx"..."""
# f0,fx1,fy1,fz1,fx2,fy2,fz2 = NEM.outerfx(order,r2,p2,r4,p4,chi,mat,d,sigr,sigs,siga,nu_sigf,ix,iy,iz,delx,dely,delz,delv,exsrc,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,[ng,nk,nmat,nxx,nyy,nzz])

"""Constructing wrapper function "outeradj"..."""
# f0,fx1,fy1,fz1,fx2,fy2,fz2 = NEM.outeradj(order,r2,p2,r4,p4,chi,mat,d,sigr,sigs,nu_sigf,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,[ng,nk,nmat,nxx,nyy,nzz])

"""Constructing wrapper function "title2"..."""
app.NEM.title2()
