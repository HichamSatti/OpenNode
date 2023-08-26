! #######################   Main Subroutines   #######################
Subroutine Modes(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                 nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,&
                 y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode)
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10, 15)
! #######################   User Input Paramaters   #######################
Integer, Intent(in) :: ng                             ! Number of Groups
Integer, Intent(in) :: nk                             ! Number of Nodes
Integer, Intent(in) :: order                          ! Order Polynomial NEM
Integer, Intent(in) :: nx, ny, nz                     ! Number of Assemblies in x, y & z Directions
Integer, Intent(in) :: nxx, nyy, nzz                  ! Number of Nodes in x, y, & z Directions
Integer, Intent(in) :: nmat                           ! Number of Materials
Integer, Dimension(nx), Intent(in) :: xdiv            ! Assembly Division
Integer, Dimension(ny), Intent(in) :: ydiv            ! Assembly Division
Integer, Dimension(nz), Intent(in) :: zdiv            ! Assembly Division
Integer, Dimension(nk), Intent(in) :: mat             ! Materials
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin ! imax and imin along x Direction for Staggered Nodes
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin ! imax and imin along y Direction for Staggered Nodes
Integer, Intent(in) :: x_east, x_west, y_north        ! Boundary Conditions
Integer, Intent(in) :: y_south, z_top, z_bott         ! Boundary Conditions
Real(dp), Dimension(nxx), Intent(in) :: delx          ! Delta_x Volume in cm3
Real(dp), Dimension(nyy), Intent(in) :: dely          ! Delta_y Volume in cm3
Real(dp), Dimension(nzz), Intent(in) :: delz          ! Delta_z Volume in cm3
Real(dp), Dimension(nk), Intent(in) :: delv           ! Nod's Volume in cm3
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz     ! x-Position, y-Position and z-Position of the Node
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz   ! xyz-Position of the Node
Character(Len=100), intent(in) :: mode
! Fixed Source Paramaters
! Real(dp), Dimension(nk,ng), Intent(in) ::  eSrc         ! External Source
! Integer, Intent(in) :: nS                             ! Sources Number
! Real(dp), Dimension(nS), Intent(in) :: dS             ! Source Density
! Real(dp), Dimension(nS,ng), Intent(in) :: spS         ! Source Spectrum
! Integer, Intent(in) :: npor                           ! Number of Radial Fixed Sources Position
! Integer, Intent(in) :: npox                           ! Number of Axial Fixed Sources Position
! Integer, Dimension(nS,npox), Intent(in) :: zpos       ! Axial Position of Extra Sources
! Integer, Dimension(nS,npor), Intent(in) :: xpos, ypos ! Radial Position of Extra Sources
! CXs Assigned to Materials
Real(dp), Dimension(nmat,ng), Intent(in) :: chi       ! Neutron Fission Spectrum
Real(dp), Dimension(nmat,ng), Intent(in) :: x_siga    ! Absorption Macroscopic CX
Real(dp), Dimension(nmat,ng), Intent(in) :: x_sigtr   ! Transport Macroscopic CX
Real(dp), Dimension(nmat,ng), Intent(in) :: x_sigf    ! Fission Macroscopic CX
Real(dp), Dimension(nmat,ng), Intent(in) :: x_nu_sigf ! nu * Fission Macroscopic CX
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs ! Scattering Macroscopic CX
! ##########################################################################

Select Case(mode)
    ! Case('Fixed Source')
        ! Call FixedSrc(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                      ! nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,y_smax,y_smin,xdiv,ydiv,zdiv,&
                      ! xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,eSrc)
    Case('Adjoint')
        Call Adjoint(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                     nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,&
                     y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode)
    Case('Forward')
        Call Forward(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                     nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,&
                     y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode)
End Select

End Subroutine

    Subroutine Forward(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                       nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,&
                       y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode) ! To Solve Forward (Normal) Problems
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15)
! #######################   User Input Paramaters   #######################
Integer, Intent(in) :: ng, nk, order, nx, ny, nz, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nz), Intent(in) :: zdiv
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Character(Len=100), intent(in) :: mode
! CXs Assigned to Materials
Real(dp), Dimension(nmat,ng), Intent(in) :: chi, x_siga, x_sigtr, x_sigf, x_nu_sigf
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs

!##########################################################################
! Local Variables
Real(dp) :: Keff   ! Effectif Multiplication Factor
Real(dp), Dimension(nk,ng) :: f0, fx1, fy1, fz1, fx2, fy2, fz2      ! Flux and Flux Moments
Real(dp), Dimension(nk,ng,6) :: jo   ! Nodals' Outgoing Currents (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,6) :: ji   ! Nodals' Ingoing Currents  (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,3) :: L0   ! Zeroth Transverse Leakages (Lx,Ly,Lz)
Real(dp), Dimension(nk,ng,6) :: al   ! Assembly Discontinuity Factor
Real(dp), Dimension(nk,ng,6,6) :: R4, R2, P2    ! Response Matrix
Real(dp), Dimension(nk,ng,6,7) :: P4            ! Response Matrix
! Real(dp), Dimension(nk,ng,7) :: Q      ! Nodal's Source and Source Moments (0,x1,y1,z1,x2,y2,z2)
! CXs Assigned to Nodes
Real(dp), Dimension(nk,ng,ng) :: sigs  ! Scattering Macroscopic CX
Real(dp), Dimension(nk,ng) :: siga     ! Absorption Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigtr    ! Transport Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigf     ! Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: nu_sigf  ! nu * Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: D        ! Diffusion Coefficient
Real(dp), Dimension(nk,ng) :: sigr     ! Scattering Macroscopic CX
Real(dp), Dimension(nk) :: power
Real(kind=4) :: st, fn
Integer, Parameter :: Ounit = 100      ! Output

Open (Unit=ounit, File='app/Output/NEM.out')
Write(ounit,*)
Write(ounit,*)
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*) &
'                                       Calculation Results'
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*)
Write(ounit,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(ounit,*) ' ----------------------------------------------------'
Write(*,*)
Write(*,*)
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*) &
'                         Calculation Results'
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*)
Write(*,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(*,*) ' ---------------------------------------------------------'

Call CPU_TIME(st)

! #######################   Initialiaze Guess Values   #######################
    Call Init(keff,jo,ji,L0,al,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk)

! #######################   Update XSec   #######################
    Call XS_updt(sigs,siga,sigtr,sigf,nu_sigf,D,sigr,ng,nk,nmat,&
                 mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf)

! #######################   Update Diffusion Coefficient and Removal XS   #######################
    Call D_sigr(D,sigr,siga,sigs,sigtr,ng,nk)

! #######################   Calculate Nodal Coupling Matrices   #######################
    Call Nodal_Coup4(P4,R4,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
    Call Nodal_Coup2(P2,R2,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)

! #######################   Call Outer Iteration   #######################
    Call Outer(Keff,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,mat,al,jo,ji,L0,&
               D,sigr,chi,sigs,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,xyz,&
               x_smax,x_smin,y_smax,y_smin,x_east,x_west,y_north,y_south,z_top,z_bott)

! #######################   Flux & Power Distribution Output   #######################
    Call PowDis(power,f0,sigf,delv,ng,nk,mode)
! Radial Power Distribution
    Call AsmPow(nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,power)
! Axial Power Distribution
    Call AxiPow(nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,power)
! Radial Flux Distribution
    Call AsmFlux(ng,nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,f0,1.e0_DP)
! Axial Flux Distribution
    ! Call AxiFlux(ng,nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,f0) 

Call CPU_TIME(fn)
Write(ounit,*)
Write(*,*)
Write(ounit,*) "Total Time : ", fn-st, "Seconds"
Write(*,*) "Total Time : ", fn-st, "Seconds"

End Subroutine

    Subroutine Adjoint(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                       nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,xdiv,ydiv,zdiv,&
                       y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode) ! To Solve Adjoint Problems
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15)
! #######################   User Input Paramaters   #######################
Integer, Intent(in) :: ng, nk, order, nx, ny, nz, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nz), Intent(in) :: zdiv
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Character(Len=100), intent(in) :: mode
! CXs Assigned to Materials
Real(dp), Dimension(nmat,ng), Intent(in) :: chi, x_siga, x_sigtr, x_sigf, x_nu_sigf
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs
!##########################################################################
! Local Variables
Real(dp) :: Keff   ! Effectif Multiplication Factor
Real(dp), Dimension(nk,ng) :: f0, fx1, fy1, fz1, fx2, fy2, fz2      ! Flux and Flux Moments
Real(dp), Dimension(nk,ng,6) :: jo   ! Nodals' Outgoing Currents (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,6) :: ji   ! Nodals' Ingoing Currents  (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,3) :: L0   ! Zeroth Transverse Leakages (Lx,Ly,Lz)
Real(dp), Dimension(nk,ng,6) :: al   ! Assembly Discontinuity Factor
Real(dp), Dimension(nk,ng,6,6) :: R4, R2, P2    ! Response Matrix
Real(dp), Dimension(nk,ng,6,7) :: P4            ! Response Matrix
! Real(dp), Dimension(nk,ng,7) :: Q      ! Nodal's Source and Source Moments (0,x1,y1,z1,x2,y2,z2)
! CXs Assigned to Nodes
Real(dp), Dimension(nk,ng,ng) :: sigs  ! Scattering Macroscopic CX
Real(dp), Dimension(nk,ng) :: siga     ! Absorption Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigtr    ! Transport Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigf     ! Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: nu_sigf  ! nu * Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: D        ! Diffusion Coefficient
Real(dp), Dimension(nk,ng) :: sigr     ! Scattering Macroscopic CX
Real(dp), Dimension(nk) :: power
Real(dp) :: st, fn
Integer, Parameter :: Ounit = 100      ! Output

Open (Unit=ounit, File='app/Output/NEM.out')
Write(ounit,*)
Write(ounit,*)
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*) &
'                                       Calculation Results'
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*)
Write(ounit,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(ounit,*) ' ----------------------------------------------------'
Write(*,*)
Write(*,*)
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*) &
'                         Calculation Results'
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*)
Write(*,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(*,*) ' ---------------------------------------------------------'

Call CPU_TIME(st)

! #######################   Initialiaze Guess Values   #######################
    Call Init(keff,jo,ji,L0,al,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk)

! #######################   Update XSec   #######################
    Call XS_updt(sigs,siga,sigtr,sigf,nu_sigf,D,sigr,ng,nk,nmat,&
                 mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf)

! #######################   Update Diffusion Coefficient and Removal XS   #######################
    Call D_sigr(D,sigr,siga,sigs,sigtr,ng,nk)

! #######################   Calculate Nodal Coupling Matrices   #######################
    Call Nodal_Coup4(P4,R4,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
    Call Nodal_Coup2(P2,R2,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)

! #######################   Call Outer Iteration   #######################
    Call OuterAdj(Keff,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,chi,mat,al,jo,ji,L0,&
                  D,sigr,sigs,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,&
                  x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)

! #######################   Flux & Power Distribution Output   #######################
    Call PowDis(power,f0,sigf,delv,ng,nk,mode)
! Radial Power Distribution
    Call AsmPow(nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,power)
! Axial Power Distribution
    Call AxiPow(nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,power)
! Radial Flux Distribution
    Call AsmFlux(ng,nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,f0,1.e0_DP)
Call CPU_TIME(fn)
Write(ounit,*) "Total Time : ", fn-st, " Seconds"

End Subroutine

    Subroutine FixedSrc(ng,nk,nx,ny,nz,nmat,order,mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,&
                        nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,x_smax,x_smin,y_smax,y_smin,xdiv,ydiv,zdiv,&
                        xyz,x_east,x_west,y_north,y_south,z_top,z_bott,mode,eSrc) ! To Solve Fixed Sources Problems
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15)
! #######################   User Input Paramaters   #######################
Integer, Intent(in) :: ng, nk, order, nx, ny, nz, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nz), Intent(in) :: zdiv
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng), Intent(in) :: eSrc
! Integer, Intent(in) :: nS
! Real(dp), Dimension(nS), Intent(in) :: dS
! Real(dp), Dimension(nS,ng), Intent(in) :: spS
! Integer, Dimension(nS,npox), Intent(in) :: zpos
! Integer, Dimension(nS,npor), Intent(in) :: xpos, ypos
Character(Len=100), intent(in) :: mode
! CXs Assigned to Materials
Real(dp), Dimension(nmat,ng), Intent(in) :: chi, x_siga, x_sigtr, x_sigf, x_nu_sigf
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs
!##########################################################################
! Local Variables
Real(dp) :: Keff   ! Effectif Multiplication Factor
Real(dp), Dimension(nk,ng) :: f0, fx1, fy1, fz1, fx2, fy2, fz2      ! Flux and Flux Moments
Real(dp), Dimension(nk,ng,6) :: jo   ! Nodals' Outgoing Currents (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,6) :: ji   ! Nodals' Ingoing Currents  (X+,X-,Y+,Y-,Z+,Z-)
Real(dp), Dimension(nk,ng,3) :: L0   ! Zeroth Transverse Leakages (Lx,Ly,Lz)
Real(dp), Dimension(nk,ng,6) :: al   ! Assembly Discontinuity Factor
Real(dp), Dimension(nk,ng,6,6) :: R4, R2, P2    ! Response Matrix
Real(dp), Dimension(nk,ng,6,7) :: P4            ! Response Matrix
! Real(dp), Dimension(nk,ng,7) :: Q      ! Nodal's Source and Source Moments (0,x1,y1,z1,x2,y2,z2)
! CXs Assigned to Nodes
Real(dp), Dimension(nk,ng,ng) :: sigs  ! Scattering Macroscopic CX
Real(dp), Dimension(nk,ng) :: siga     ! Absorption Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigtr    ! Transport Macroscopic CX
Real(dp), Dimension(nk,ng) :: sigf     ! Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: nu_sigf  ! nu * Fission Macroscopic CX
Real(dp), Dimension(nk,ng) :: D        ! Diffusion Coefficient
Real(dp), Dimension(nk,ng) :: sigr     ! Scattering Macroscopic CX
Real(dp), Dimension(nk) :: power
Real(dp) :: st, fn
Integer, Parameter :: Ounit = 100      ! Output

Open (Unit=ounit, File='app/Output/NEM.out')

! #######################   Print Extra Sources   #######################
    ! Call ExSrc(eSrc,nk,ng,nx,ny,nz,nxx,nyy,nzz,nS,dS,spS,&
               ! xyz,xdiv,ydiv,zdiv,xpos,ypos,zpos,npox,npor)

Write(ounit,*)
Write(ounit,*)
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*) &
'                                       Calculation Results'
Write(ounit,*) ' ==============================================' &
// '=================================================='
Write(ounit,*)
Write(ounit,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(ounit,*) ' ----------------------------------------------------'
Write(*,*)
Write(*,*)
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*) &
'                         Calculation Results'
Write(*,*) ' ==============================================' &
// '===================='
Write(*,*)
Write(*,*) '  Iteration    Keff     FissSrc Error   Inner Error'
Write(*,*) ' ---------------------------------------------------------'

Call CPU_TIME(st)

! #######################   Initialiaze Guess Values   #######################
    Call Init(keff,jo,ji,L0,al,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk)

! #######################   Update XSec   #######################
    Call XS_updt(sigs,siga,sigtr,sigf,nu_sigf,D,sigr,ng,nk,nmat,&
                 mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf)

! #######################   Update Diffusion Coefficient and Removal XS   #######################
    Call D_sigr(D,sigr,siga,sigs,sigtr,ng,nk)

! #######################   Calculate Nodal Coupling Matrices   #######################
    Call Nodal_Coup4(P4,R4,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
    Call Nodal_Coup2(P2,R2,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)

! #######################   Call Outer Iteration   #######################
    Call OuterFx(f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,chi,mat,al,jo,ji,L0,&
                 D,sigr,sigs,siga,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,eSrc,&
                 x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)

! #######################   Flux & Power Distribution Output   #######################
    Call PowDis(power,f0,sigf,delv,ng,nk,mode)
! Radial Power Distribution
    Call AsmPow(nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,power)
! Axial Power Distribution
    Call AxiPow(nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,power)
! Radial Flux Distribution
    Call AsmFlux(ng,nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,f0)
    
Call CPU_TIME(fn)
Write(ounit,*) "Total Time : ", fn-st, " Seconds"

End Subroutine

        Subroutine Outer(Keff,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,mat,al,jo,ji,L0,&
                         D,sigr,chi,sigs,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,xyz,&
                         x_smax,x_smin,y_smax,y_smin,x_east,x_west,y_north,y_south,z_top,z_bott)    ! To Perform Outer Iterations
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15), Ounit = 100
Integer, Intent(in) :: ng, nk, order, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin 
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: nu_sigf, D, sigr
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng,6), Intent(in):: al, jo, ji
Real(dp), Dimension(nk,ng,3), Intent(in) :: L0
Real(dp), Dimension(nk,ng,6,6),Intent(in) :: R2, P2, R4
Real(dp), Dimension(nk,ng,6,7),Intent(in) :: P4
Real(dp), Dimension(nk,ng), intent(inout) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Intent(inout) :: Keff
! Local Variables
Integer :: nout = 500                ! Maximum Outer Iteration
Integer :: nac = 5                   ! Number of Outer Iteration Before Next Source Extrapolation
Real(dp) :: ferc = 1.e-5             ! Flux Error Criteria
Real(dp) :: fserc = 1.e-5            ! Fission Source Error Criteria
Real(dp) :: fer, fser                ! Flux and Fission Source Error in BCSEARCH calcs.
Real(dp), Dimension(nk) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2     ! Fission Source & Fission Source Moments
Real(dp) :: Keo                      ! Old Multiplication Factor (Keff)
Real(dp), Dimension(nk) :: fs0d      ! Old Fission Source
Real(dp), Dimension(nk,ng) :: f0d    ! Old Flux
Real(dp) :: fsd                      ! Old Integrated Fission Sources
Real(dp) :: fs                       ! New Integrated Fission Sources
Real(dp) :: domiR, e1, e2
Integer :: g, o, npos
Real(dp), Dimension(nk,ng,7) :: Q
Real(dp), Dimension(nk) :: errn, erro

!#####################    Initialize Fission Source    ####################
    Call FSrc(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,&
              f0,fx1,fy1,fz1,fx2,fy2,fz2,nu_sigf,ng,nk)

errn = 1._dp          ! Variable Fission Source Error
    Call Integrate(fs,fs0,delv,nk)
    Call Integrate(e1,errn,delv,nk)

!#######################    Start Outer Iteration   #######################
    Do o=1, nout
        f0d = f0          ! Save Old Fluxes
        fsd = fs          ! Save Old Integrated Fission Source
        fs0d  = fs0       ! Save Old Fission Source
        Keo = Keff        ! Save Old Multiplication Fctor
        erro = errn       ! Save Old Fission Source Error/Difference
 
        Do g = 1, ng
!#######################   Calculate Total Source   #######################
            Call TSrc(Q,g,Keo,ng,nmat,nk,chi,mat,sigs,f0,fx1,fy1,fz1,&
                      fx2,fy2,fz2,fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2)
!#######################    Start Inner Iteration   #######################
            Call Inner(f0,fx1,fy1,fz1,fx2,fy2,fz2,g,ng,nk,order,jo,ji,L0,Q,R2,P2,R4,P4,al,D,sigr,nxx,nyy,nzz,ix,iy,iz,delx,&
                       dely,delz,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)
        End Do

!########################   Update Fission Source   #######################
        Call FSrc(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,&
                  f0,fx1,fy1,fz1,fx2,fy2,fz2,nu_sigf,ng,nk)
        errn = fs0 - fs0d
        Call Integrate(e2,ABS(errn),delv,nk)    ! Variable Integrated Fission Source Error

!####################   Fission Source Extrapolation   ####################
        if (MOD(o,nac) == 0) Then
            domiR = e2 / e1
            npos = MAXLOC(ABS(erro),1)
            if (erro(npos) * errn(npos) < 0.0) domiR = -domiR
            fs0 = fs0 + domiR / (1._dp - domiR) * errn
            Write(ounit,*) '    ...Fission Source Extrapolated...'
            Write(*,*) '    ...Fission Source Extrapolated...'
        End if
        e1 = e2                         ! Save Integrated Fission Source Error

!############################    Update Keff    ###########################
        Call Integrate(fs,fs0,delv,nk)  ! Integrate Fission Source
        Keff = Keo * fs / fsd           ! Update Keff

!##################   Write Outer Iteration Evolution   ###################
        Call RelE(fs0,fs0d,fser,nk)     ! Search Maximum Point Wise Fission Source Relative Error
        Call RelEg(f0,f0d,fer,nk,ng)    ! Search Maximum Point Wise Flux Error
        if (.TRUE.) Then
            Write(ounit,'(3X,I5,2X,F13.6,2ES15.5)') o, Keff, fser, fer
            Write(*,'(3X,I5,2X,F13.6,2ES15.5)') o, Keff, fser, fer
        End if
        if ((fser < fserc) .AND. (fer < ferc)) Exit  ! if converge, exit.
    End Do

    if (o-1 == nout) Then
        Write(ounit,*)
        Write(ounit,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(ounit,*) '  Iteration May Not Converge.'
        Write(ounit,*) '  Check Problem Specification or Change Iteration Control.'
        Write(ounit,*) '  Code is Stoping...'
        Write(*,*)
        Write(*,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(*,*) '  Iteration May Not Converge.'
        Write(*,*) '  Check Problem Specification or Change Iteration Control.'
        Write(*,*) '  Code is Stoping...'
        Stop
    End if

    if (.TRUE.) Write(ounit,*)
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(ounit,   '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(*,*)
    if (.TRUE.) Write(*,*) '***********************************************'
    if (.TRUE.) Write(*, '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(*,*) '***********************************************'

End Subroutine

        Subroutine OuterAdj(Keff,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,chi,mat,al,jo,ji,L0,&
                            D,sigr,sigs,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,&
                            x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)    !    To Perform Adjoint Outer Iteration
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15), Ounit = 100
Integer, Intent(in) :: ng, nk, order, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin 
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: nu_sigf, D, sigr
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng,6), Intent(in) :: al, jo, ji
Real(dp), Dimension(nk,ng,3), Intent(in) :: L0
Real(dp), Dimension(nk,ng,6,6),Intent(in) :: R2, P2, R4
Real(dp), Dimension(nk,ng,6,7),Intent(in) :: P4
Real(dp), Dimension(nk,ng), intent(inout) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Intent(inout) :: Keff
! Local Variables
Integer :: nout = 500               ! Maximum Outer Iteration
Integer :: nac = 5                  ! Number of Outer Iteration Before Next Source EXTRAPOLATION
Real(dp) :: ferc = 1.e-5            ! Flux Error Criteria
Real(dp) :: fserc = 1.e-5           ! Fission Source Error Criteria
Real(dp) :: fer, fser               ! Flux and Fission Source Error in BCSEARCH calcs.
Real(dp), Dimension(nk) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2     ! Fission Source and Fission Source Moments
Real(dp) :: Keo                     ! Old Multiplication Factor (Keff)
Real(dp), Dimension(nk) :: fs0d     ! Old Fission Source
Real(dp), Dimension(nk,ng) :: f0d   ! Old Flux
Real(dp) :: fsd                     ! Old Integrated Fission Sources
Real(dp) :: fs                      ! New Integrated Fission Sources
Real(dp) :: domiR, e1, e2
Integer :: g, o, npos
Real(dp), Dimension(nk,ng,7) :: Q
Real(dp), Dimension(nk) :: errn, erro

Open (Unit=ounit, File='app/Output/NEM.out')

!#####################    Initialize Fission Source    ####################
    Call FSrcAdj(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,mat,&
                 chi,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,nmat)
errn = 1._dp          ! Variable Fission Source Error
    Call Integrate(fs,fs0,delv,nk)
    Call Integrate(e1,errn,delv,nk)

!#######################    Start Outer Iteration   #######################
    Do o=1, nout
        f0d = f0          ! Save Old Fluxes
        fsd = fs          ! Save Old Integrated Fission Source
        fs0d  = fs0       ! Save Old Fission Source
        Keo = Keff        ! Save Old Multiplication Fctor
        erro = errn       ! Save Old Fission Source Error/Difference

        Do g = ng, 1, -1
!#######################   Calculate Total Source   #######################
            Call TSrcAdj(Q,Keo,sigs,nu_sigf,f0,fx1,fy1,fz1,fx2,fy2,fz2,&
                         fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,g,ng,nk)
!#######################    Start Inner Iteration   #######################
            Call Inner(f0,fx1,fy1,fz1,fx2,fy2,fz2,g,ng,nk,order,jo,ji,L0,Q,R2,P2,R4,P4,al,D,sigr,nxx,nyy,nzz,ix,iy,iz,delx,&
                       dely,delz,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)
        End Do

!########################   Update Fission Source   #######################
        Call FSrcAdj(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,mat,&
                     chi,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,nmat)
        errn = fs0 - fs0d
        Call Integrate(e2,ABS(errn),delv,nk)    ! Variable Integrated Fission Source Error

!####################   Fission Source Extrapolation   ####################
        if (MOD(o,nac) == 0) Then
            domiR = e2 / e1
            npos = MAXLOC(ABS(erro),1)
            if (erro(npos) * errn(npos) < 0.0) domiR = -domiR
            fs0 = fs0 + domiR / (1._dp - domiR) * errn
            Write(ounit,*) '    ...Fission Source Extrapolated...'
        End if
        e1 = e2                         ! Save Integrated Fission Source Error

!############################    Update Keff    ###########################
        Call Integrate(fs,fs0,delv,nk)  ! Integrate Fission Source
        Keff = Keo * fs / fsd

!##################   Write Outer Iteration Evolution   ###################
        Call RelE(fs0,fs0d,fser,nk)     ! Search Maximum Point Wise Fission Source Relative Error
        Call RelEg(f0,f0d,fer,nk,ng)    ! Search Maximum Point Wise Flux Error
        if (.TRUE.) Write(ounit,'(I5,F13.6,2ES15.5)') o, Keff, fser, fer
        if (.TRUE.) Write(*,'(I5,F13.6,2ES15.5)') o, Keff, fser, fer
        if ((fser < fserc) .AND. (fer < ferc)) Exit  ! if converge, exit.
    End Do

    if (o-1 == nout) Then
        Write(ounit,*)
        Write(ounit,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(ounit,*) '  Iteration May Not Converge.'
        Write(ounit,*) '  Check Problem Specification or Change Iteration Control.'
        Write(ounit,*) '  Code is Stoping...'
        Write(*,*)
        Write(*,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(*,*) '  Iteration May Not Converge.'
        Write(*,*) '  Check Problem Specification or Change Iteration Control.'
        Write(*,*) '  Code is Stoping...'
        Stop
    End if

    if (.TRUE.) Write(ounit,*)
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(ounit, '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(*,*)
    if (.TRUE.) Write(*,*) '***********************************************'
    if (.TRUE.) Write(*, '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(*,*) '***********************************************'

End Subroutine

        Subroutine OuterFx(f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,order,R2,P2,R4,P4,nmat,chi,mat,al,jo,ji,L0,&
                           D,sigr,sigs,siga,nu_sigf,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,delv,eSrc,&
                           x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)    !To perform fixed-source outer iteration
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15), Ounit = 100
Integer, Intent(in) :: ng, nk, order, nmat, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nk), Intent(in) :: mat
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin 
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: delv, ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: siga, nu_sigf, D, sigr, eSrc
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng,6), Intent(in):: al, jo, ji
Real(dp), Dimension(nk,ng,3), Intent(in) :: L0
Real(dp), Dimension(nk,ng,6,6),Intent(in) :: R2, P2, R4
Real(dp), Dimension(nk,ng,6,7),Intent(in) :: P4
Real(dp), Dimension(nk,ng), intent(inout) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp) :: Keff
! Local Variables
Integer :: nout = 500               ! Maximum Outer Iteration
Integer :: nac = 5                  ! Number of Outer Iteration Before Next Source Extrapolation
Real(dp) :: ferc = 1.e-5            ! Flux Error Criteria
Real(dp) :: fserc = 1.e-5           ! Fission Source Error Criteria
Real(dp) :: fer, fser               ! Flux and Fission Source Error in BCSEARCH calcs.
Real(dp), Dimension(nk) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2     ! Fission Source & Fission Source Moments
Real(dp), Dimension(nk) :: fs0d     ! Old Fission Source
Real(dp), Dimension(nk,ng) :: f0d   ! Old Flux
Real(dp) :: domiR, e1, e2
Integer :: g, o, npos
Real(dp), Dimension(nk,ng,7) :: Q
Real(dp), Dimension(nk) :: errn, erro

Open (Unit=ounit, File='app/Output/NEM.out')

!#####################    Initialize Fission Source    ####################
    Call FSrc(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,&
              f0,fx1,fy1,fz1,fx2,fy2,fz2,nu_sigf,ng,nk)

errn = 1._dp          ! Variable Fission Source Error
    Call Integrate(e1,errn,delv,nk)

!#######################    Start Outer Iteration   #######################
    Do o=1, nout
        f0d = f0          ! Save Old Fluxes
        fs0d  = fs0       ! Save Old Fission Source
        erro = errn       ! Save Old Fission Source Error/Difference

        Do g = 1, ng
!#######################   Calculate Total Source   #######################
            Call TSrcFx(Q,g,ng,nmat,nk,chi,mat,sigs,f0,fx1,fy1,fz1,&
                        fx2,fy2,fz2,fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,eSrc)
!#######################    Start Inner Iteration   #######################
            Call Inner(f0,fx1,fy1,fz1,fx2,fy2,fz2,g,ng,nk,order,jo,ji,L0,Q,R2,P2,R4,P4,al,D,sigr,nxx,nyy,nzz,ix,iy,iz,delx,&
                       dely,delz,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)
        End Do

!########################   Update Fission Source   #######################
        Call FSrc(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,&
                  f0,fx1,fy1,fz1,fx2,fy2,fz2,nu_sigf,ng,nk)

        errn = fs0 - fs0d
        Call Integrate(e2,ABS(errn),delv,nk)    ! Variable Integrated Fission Source Error

!####################   Fission Source Extrapolation   ####################
        if (Mod(o,nac) == 0) Then
            domiR = e2 / e1
            npos = MAXLOC(ABS(erro),1)
            if (erro(npos) * errn(npos) < 0.0) domiR = -domiR
            fs0 = fs0 + domiR / (1._dp - domiR) * errn
            Write(ounit,*) '    ...Fission Source Extrapolated...'
        End if
        e1 = e2                         ! Save Integrated Fission Source Error

!##################   Write Outer Iteration Evolution   ###################
        Call RelE(fs0,fs0d,fser,nk)     ! Search Maximum Point Wise Fission Source Relative Error
        Call RelEg(f0,f0d,fer,nk,ng)    ! Search Maximum Point Wise Flux Error
        Write(ounit,'(I5,2ES15.5)') o, fser, fer  ! Write Outer Iteration Evolution
        Write(*,'(I5,2ES15.5)') o, fser, fer  ! Write Outer Iteration Evolution
        if ((fser < fserc) .AND. (fer < ferc)) Exit  ! if converge, exit.
    End Do
    if (o-1 == nout) Then
        Write(ounit,*)
        Write(ounit,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(ounit,*) '  Iteration May Not Converge.'
        Write(ounit,*) '  Check Problem Specification or Change Iteration Control.'
        Write(ounit,*) '  Code is Stoping...'
        Stop
    End if

!#########################     Calculate Keff     #########################
    Call MultF(Keff,ng,nk,siga,nu_sigf,f0,jo,ji,nxx,nyy,nzz,ix,iy,iz,&
               delx,dely,delz,x_smax,x_smin,y_smax,y_smin)

    if (o-1 == nout) Then
        Write(ounit,*)
        Write(ounit,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(ounit,*) '  Iteration May Not Converge.'
        Write(ounit,*) '  Check Problem Specification or Change Iteration Control.'
        Write(ounit,*) '  Code is Stoping...'
        Write(*,*)
        Write(*,*) '  Maximum Number of Outer Iteration is Reached.'
        Write(*,*) '  Iteration May Not Converge.'
        Write(*,*) '  Check Problem Specification or Change Iteration Control.'
        Write(*,*) '  Code is Stoping...'
        Stop
    End if

    if (.TRUE.) Write(ounit,*)
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(ounit, '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(ounit,*) '***********************************************'
    if (.TRUE.) Write(*,*)
    if (.TRUE.) Write(*,*) '***********************************************'
    if (.TRUE.) Write(*, '(A40,F9.6)') 'Effective Factor Multiplication & 
    : Keff = ', Keff
    if (.TRUE.) Write(*,*) '***********************************************'

End Subroutine

            Subroutine Inner(f0,fx1,fy1,fz1,fx2,fy2,fz2,g,ng,nk,order,jo,ji,L0,Q,R2,P2,R4,P4,al,D,sigr,nxx,nyy,nzz,ix,iy,iz,delx,&
                             dely,delz,x_smax,x_smin,y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott) ! To Perform Inner Iterations
Implicit None
Integer, Parameter :: dp = Selected_Real_Kind(10,15)
Integer, Intent(in) :: g, ng, nk, order, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz 
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng), Intent(in) :: D, sigr
Real(dp), Dimension(nk,ng,7), Intent(in) :: Q
Real(dp), Dimension(nk,ng,6,6),Intent(in) :: R2, P2, R4
Real(dp), Dimension(nk,ng,6,7),Intent(in) :: P4
Real(dp), Dimension(nk,ng,6), Intent(in) :: al
Real(dp), Dimension(nk,ng,3), Intent(in) :: L0
Real(dp), Dimension(nk,ng,6), Intent(inout) :: jo, ji
Real(dp), Dimension(nk,ng), Intent(inout) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
! Local Variables
Real(dp), Dimension(6) :: MulJin, MulMom
Real(dp), Dimension(nk,ng,7) :: L      ! Transverse Leakage Moments(0, Lx1, Ly1, Lz1, Lx2, Ly2, Lz2)
Integer :: nin = 2      ! Maximum Inner Iteration
Integer :: n, k

! Jout Nodals' outgoing currents+flux  (X+, X-, Y+, Y-, Z+, Z-)
! Jin  Nodals' ingoing currents+source (X+, X-, Y+, Y-, Z+, Z-)

! Start Inner Iteration
Do n = 1, nin
    Do k = 1, nk ! Loop on k for Jin & QTL

!#######################   Calculate Ingoing Partial Currents   #######################
        Call Jin(ji,g,k,jo,al,ng,nk,nxx,nyy,nzz,ix,iy,iz,x_smax,x_smin,&
                 y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)

!#######################   Update Transverse Leakage Moments   #######################
        Call QTL(L(k,g,:),g,k,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xyz,x_smax,x_smin,&
                 y_smax,y_smin,L0,x_east,x_west,y_north,y_south,z_top,z_bott)
   End Do
    Do k = 1, nk
        if      (order == 2) Then
            ! Call MatVec2(MulJin,MulMom,R,P,ji(k,g,:),Q(k,g,:),ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,D,sigr)        Call Nodal_Coup2(P,R,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
            Call MatVec2(MulJin,MulMom,R2(k,g,:,:),P2(k,g,:,:),ji(k,g,:),Q(k,g,:))
        Else if (order == 4) Then
            ! Call MatVec4(MulJin,MulMom,R,P,ji(k,g,:),Q(k,g,:),L(k,g,:),ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,D,sigr)        Call Nodal_Coup2(P,R,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
            Call MatVec4(MulJin,MulMom,R4(k,g,:,:),P4(k,g,:,:),ji(k,g,:),Q(k,g,:),L(k,g,:))
        End if
        ! Call MatVec(R,ji,MulJin,ng,nk,g,k,6,6,6)
        ! Call MatVec(P,Q,MulMom,ng,nk,g,k,6,7,7)

!#######################   Update Outgoing Partial Currents   #######################
       jo(k,g,:) = MulJin + MulMom     !nod(xyz(ix(1),iy(1),iz(3)),2)jo(3) : Jout(y+) 2grp (1x,1y,3z)'node
    ! Update Ingoing Partial Currents in Adjacent Nodes
        ! Call Jin(ji,g,k,jo,al,ng,nk,nxx,nyy,nzz,ix,iy,iz,x_smax,x_smin,&
                 ! y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)    ! Update Zeroth Transverse Leakages

!#######################   Update Zeroth Transverse Leakages   #######################
        Call Lxyz(L0,k,g,ng,nk,jo,ji)

!#######################   Update Flux and Flux Moments   #######################
        if      (order == 2) Then
            Call Flux2(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,sigr,Q,L0)
        Else if (order == 4) Then
            Call Flux4(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,&
                       D,sigr,delx,dely,delz,ix,iy,iz,jo,ji,L0,Q,L)
        End if
    End Do
    Do k = nk, 1, -1 ! Loop on k for Jin & QTL
    ! To Calculate Ingoing Partial Currents from Neighborhod Nodes    
        Call Jin(ji,g,k,jo,al,ng,nk,nxx,nyy,nzz,ix,iy,iz,x_smax,x_smin,&
                 y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)
    ! Update Transverse Leakage Moments
        Call QTL(L(k,g,:),g,k,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xyz,x_smax,x_smin,&
                 y_smax,y_smin,L0,x_east,x_west,y_north,y_south,z_top,z_bott)
    End Do
    Do k = nk, 1, -1
        if (order == 2) Then
            ! Call MatVec2(MulJin,MulMom,R,P,ji(k,g,:),Q(k,g,:),ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,D,sigr)        Call Nodal_Coup2(P,R,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
            Call MatVec2(MulJin,MulMom,R2(k,g,:,:),P2(k,g,:,:),ji(k,g,:),Q(k,g,:))
        Else if (order == 4) Then
            ! Call MatVec4(MulJin,MulMom,R,P,ji(k,g,:),Q(k,g,:),L(k,g,:),ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,D,sigr)        Call Nodal_Coup2(P,R,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz)
            Call MatVec4(MulJin,MulMom,R4(k,g,:,:),P4(k,g,:,:),ji(k,g,:),Q(k,g,:),L(k,g,:))
        End if
        ! Call MatVec(R,ji,MulJin,ng,nk,g,k,6,6,6)
        ! Call MatVec(P,Q,MulMom,ng,nk,g,k,6,7,7)
    ! Update Outgoing Partial Currents
       jo(k,g,:) = MulJin+MulMom     !nod(xyz(ix(1),iy(1),iz(3)),2)jo(3) : Jout(y+) 2grp (1x,1y,3z)'node
    ! Update Ingoing Partial Currents in Adjacent Nodes
        ! Call Jin(ji,g,k,jo,al,ng,nk,nxx,nyy,nzz,ix,iy,iz,x_smax,x_smin,&
                 ! y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott)    ! Update Zeroth Transverse Leakages
    ! Update Zeroth Transverse Leakages
        Call Lxyz(L0,k,g,ng,nk,jo,ji)
    ! Update Flux and Flux Moments
        if (order == 2) Then
            Call Flux2(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,sigr,Q,L0)
        Else if (order == 4) Then
            Call Flux4(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,&
                       D,sigr,delx,dely,delz,ix,iy,iz,jo,ji,L0,Q,L)
        End if
    End Do
End Do

End Subroutine

Subroutine Output(ng,np,nmat,nx,ny,nz,nxx,nyy,nzz,delx,dely,delz,xD,x_sigr,&
                  x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf,chi,zdiv,node,zpln,&
                  x_east,x_west,y_north,y_south,z_top,z_bott,mode)
implicit none
Integer, Parameter :: dp = Selected_Real_Kind(10,15), Ounit = 100, gm = 36
Integer, Intent(in) :: ng, np, nmat, nx, ny, nz, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nz), Intent(in) :: zpln, zdiv
Integer, Dimension(np,nxx,nyy), Intent(in) :: node
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs
Real(dp), Dimension(nmat,ng), Intent(in) :: x_siga, x_sigtr, x_sigf, x_nu_sigf, chi, xD, x_sigr
! Local Variables
Character(Len=2), Dimension(nxx, nyy) :: mmap
Character(Len=100), intent(in) :: mode
Integer, Dimension(ng) :: group
Integer :: i, j, k, g, h, lz, ztot, ip, ipr, kp, xs, xf

Open (Unit=Ounit, File='app/Output/NEM.out')

! #######################           Calculation Mode            #######################
Select Case(mode)
    Case('Fixed Source')
        Write(Ounit,*)    '                       =========================='
        Write(Ounit,*)    '  Calculation Mode :    Fixed Source Calculation '
        Write(Ounit,*)    '  ----------------     =========================='
        Write(*,*)        '                       =========================='
        Write(*,*)        '  Calculation Mode :    Fixed Source Calculation '
        Write(*,*)        '  -----------------    =========================='
    Case('Adjoint')
        Write(Ounit,*)    '                       ====================='
        Write(Ounit,*)    '  Calculation Mode :    Adjoint Calculation '
        Write(Ounit,*)    '  ----------------     ====================='
        Write(*,*)        '                       ====================='
        Write(*,*)        '  Calculation Mode :    Adjoint Calculation '
        Write(*,*)        '  ----------------     ====================='
    Case('Forward')
        Write(Ounit,*)    '                       ====================='
        Write(Ounit,*)    '  Calculation Mode :    Forward Calculation '
        Write(Ounit,*)    '  ----------------     ====================='
        Write(*,*)        '                       ====================='
        Write(*,*)        '  Calculation Mode :    Forward Calculation '
        Write(*,*)        '  ----------------     ====================='
End Select
Write(ounit,*)
Write(ounit,*) '           --------------------------------------------'
Write(*,*)
Write(*,*) '           --------------------------------------------'

Do g=1,ng
    group(g)=g
End Do

! #######################   Macroscopic Cross Sections Output   #######################

Write(Ounit,*) '           >>>> Writing Macroscopic Cross Sections <<<<'
Write(Ounit,*) '           --------------------------------------------'
Write(*,*)     '           >>>> Writing Macroscopic Cross Sections <<<<'
Write(*,*)     '           --------------------------------------------'
    Do k= 1, nmat
        Write(Ounit,1009) k
        Write(Ounit,1011)'Group', 'Transport', 'Diffusion', 'Absorption', &
        'Removal', 'Nu*Fiss', 'Kap*Fis','Fiss. Spctr'
        Write(*,1009) k
        Write(*,1011)'Group', 'Transport', 'Diffusion', 'Absorption', &
        'Removal', 'Nu*Fiss', 'Kap*Fis','Fiss. Spctr'
        Do g= 1, ng
            Write(Ounit,1010) g, x_sigtr(k,g), xD(k,g), x_siga(k,g), &
            x_sigr(k,g), x_nu_sigf (k,g), x_sigf(k,g), chi(k,g)
            Write(*,1010) g, x_sigtr(k,g), xD(k,g), x_siga(k,g), &
            x_sigr(k,g), x_nu_sigf (k,g), x_sigf(k,g), chi(k,g)
        End Do
        Write(Ounit,*)'        --Scattering Matrix--'
        Write(Ounit,'(10X, A5, 20I11)') "G/G'", (group(g), g=1,ng)
        Write(*,*)'        --Scattering Matrix--'
        Write(*,'(10X, A5, 20I11)') "G/G'", (group(g), g=1,ng)
        Do g= 1, ng
            Write(ounit,1015) g, (x_sigs(k,g,h), h=1,ng)
            Write(*,1015) g, (x_sigs(k,g,h), h=1,ng)
        End Do
    End Do
! #######################   Core Geometry Output   #######################
Write(Ounit,*)
Write(ounit,*) '           -------------------------------'
Write(ounit,*) '           >>>>>Wrting Core Geometry<<<<<'
Write(ounit,*) '           -------------------------------'
Write(ounit,*)' Number of Assembly in x, y and z Directions Respectively :'
Write(ounit,*) nx, ny, nz
Write(ounit,*)' Number of Nodes in x, y and z Directions Respectively :'
Write(ounit,*) nxx, nyy, nzz
Write(ounit,*)
Write(ounit,1016) 'x','x'
Write(ounit,'(2X,10F7.2)')(delx(i), i=1,nxx)
Write(ounit,1016) 'y','y'
Write(ounit,'(2X,10F7.2)')(dely(j), j=1,nyy)
Write(*,*)
Write(*,*) '           -------------------------------'
Write(*,*) '           >>>>>Wrting Core Geometry<<<<<'
Write(*,*) '           -------------------------------'
Write(*,*)' Number of Assembly in x, y and z Directions Respectively :'
Write(*,*) nx, ny, nz
Write(*,*)' Number of Nodes in x, y and z Directions Respectively :'
Write(*,*) nxx, nyy, nzz
Write(*,*)
Write(*,1016) 'x','x'
Write(*,'(2X,10F7.2)')(delx(i), i=1,nxx)
Write(*,1016) 'y','y'
Write(*,'(2X,10F7.2)')(dely(j), j=1,nyy)
Write(*,*)
    ip = nxx/gm
    ipr = MOD(nxx,gm) - 1
    Do k= 1,np
        Do j = 1, nyy
            Do i = 1, nxx
                if (node(zpln(k),i,j) == 0) Then
                    mmap(i,j) = '  '
                Else
                    Write (mmap(i,j),'(I2)') node(zpln(k),i,j)
                    mmap(i,j) = TRIM(ADJUSTL(mmap(i,j)))
                End if
            End Do
        End Do

        Write(ounit,1017) k
        Write(*,1017) k
        xs = 1; xf = gm
        Do kp = 1, ip
            Write(ounit,'(6X,100I3)') (i, i = xs, xf)
            Write(*,'(6X,100I3)') (i, i = xs, xf)
            Do j= nyy, 1, -1
                Write(ounit,'(2X,I4,1X,100A3)') j, (mmap(i,j), i=xs, xf)
                Write(*,'(2X,I4,1X,100A3)') j, (mmap(i,j), i=xs, xf)
            End Do
            xs = xs + gm
            xf = xf + gm
        End Do

        Write(ounit,'(6X,100I3)') (i, i = xs, xs+ipr)
        Write(*,'(6X,100I3)') (i, i = xs, xs+ipr)
        if (xs+ipr > xs) Then
            Do j= nyy, 1, -1
                Write(ounit,'(2X,I4,1X,100A3)') j, (mmap(i,j), i=xs, xs+ipr)
                Write(*,'(2X,I4,1X,100A3)') j, (mmap(i,j), i=xs, xs+ipr)
            End Do
        End if
    End Do
    
    Write(ounit,*)
    Write(ounit,1018)
    Write(ounit,*) '-------------------------------------'
    Write(ounit,*) '  Plane Number     Planar Region    Delta-z'
    Write(*,*)
    Write(*,1018)
    Write(*,*) '-------------------------------------'
    Write(*,*) '  Plane Number     Planar Region    Delta-z'
    ztot = nzz
    Do k= nz, 1, -1
        Do lz= 1, zdiv(k)
            If (ztot == nzz) Then
                Write(ounit,'(I9, A6, I13, F15.2)') ztot, ' (Top)', zpln(k), delz(ztot)
                Write(*,'(I9, A6, I13, F15.2)') ztot, ' (Top)', zpln(k), delz(ztot)
            Else if (ztot == 1) Then
                 Write(ounit,'(I9, A9, I10, F15.2)') ztot, ' (Bottom)', zpln(k), delz(ztot)
                 Write(*,'(I9, A9, I10, F15.2)') ztot, ' (Bottom)', zpln(k), delz(ztot)
            Else
                Write(ounit,'(I9, I19, F15.2)') ztot, zpln(k), delz(ztot)
                Write(*,'(I9, I19, F15.2)') ztot, zpln(k), delz(ztot)
            End if
            ztot = ztot - 1
        End Do
    End Do

    Write(ounit,*)
    Write(ounit,*) '  Boundary Conditions'
    Write(ounit,*) '  -------------------'
    Write(*,*)
    Write(*,*) '  Boundary Conditions'
    Write(*,*) '  -------------------'
    if (x_west == 0) Then
        Write(ounit,*)' X-Directed West   : Zero Flux'
        Write(*,*)' X-Directed West   : Zero Flux'
    Else if (x_west == 1) Then
        Write(ounit,*)' X-Directed West   : Zero Incoming Current'
        Write(*,*)' X-Directed West   : Zero Incoming Current'
    Else
        Write(ounit,*)' X-Directed West   : Reflective'
        Write(*,*)' X-Directed West   : Reflective'
    End if

    if (x_east == 0) Then
        Write(ounit,*)' X-Directed East   : Zero Flux'
        Write(*,*)' X-Directed East   : Zero Flux'
    Else if (x_east == 1) Then
        Write(ounit,*)' X-Directed East   : Zero Incoming Current'
        Write(*,*)' X-Directed East   : Zero Incoming Current'
    Else
        Write(ounit,*)' X-Directed East   : Reflective'
        Write(*,*)' X-Directed East   : Reflective'
    End if

    if (y_north == 0) Then
        Write(ounit,*)' Y-Directed North  : Zero Flux'
        Write(*,*)' Y-Directed North  : Zero Flux'
    Else if (y_north == 1) Then
        Write(ounit,*)' Y-Directed North  : Zero Incoming Current'
        Write(*,*)' Y-Directed North  : Zero Incoming Current'
    Else
        Write(ounit,*)' Y-Directed North  : Reflective'
        Write(*,*)' Y-Directed North  : Reflective'
    End if

    if (y_south == 0) Then
        Write(ounit,*)' Y-Directed South  : Zero Flux'
        Write(*,*)' Y-Directed South  : Zero Flux'
    Else if (y_south == 1) Then
        Write(ounit,*)' Y-Directed South  : Zero Incoming Current'
        Write(*,*)' Y-Directed South  : Zero Incoming Current'
    Else
        Write(ounit,*)' Y-Directed South  : Reflective'
        Write(*,*)' Y-Directed South  : Reflective'
    End if

    if (z_bott == 0) Then
        Write(ounit,*)' Z-Directed Bottom : Zero Flux'
        Write(*,*)' Z-Directed Bottom : Zero Flux'
    Else if (z_bott == 1) Then
        Write(ounit,*)' Z-Directed Bottom : Zero Incoming Current'
        Write(*,*)' Z-Directed Bottom : Zero Incoming Current'
    Else
        Write(ounit,*)' Z-Directed Bottom : Reflective'
        Write(*,*)' Z-Directed Bottom : Reflective'
    End if

    if (z_top == 0) Then
        Write(ounit,*)' Z-Directed Top    : Zero Flux'
        Write(*,*)' Z-Directed Top    : Zero Flux'
    Else if (z_top == 1) Then
        Write(ounit,*)' Z-Directed Top    : Zero Incoming Current'
        Write(*,*)' Z-Directed Top    : Zero Incoming Current'
    Else
        Write(ounit,*)' Z-Directed Top    : Reflective'
        Write(*,*)' Z-Directed Top    : Reflective'
    End if

! 1031 Format(2X, 'Calculation Mode : ', A40)
1009 Format(5X, 'Material', I3)
1010 Format(2X, I6, F13.6, 3F12.6, 3F13.6)
1011 Format(2X, A7, A12, A13, A12, A11, 2A13, A15)
1015 Format(10X, I3, F16.6, 20F12.6)
1016 Format(2X,A,'-Directed Nodes Divison (Delta-',A,')')
1017 Format(2X, 'Planar Region : ', I2)
1018 Format(2X, 'Planar Region Assignment to Planes.')

Write(ounit,*)
Write(ounit,*) ' ...Core Geometry is Sucessfully Read...'
Write(ounit,*) '    ---------------------------------'
Write(*,*)
Write(*,*) ' ...Core Geometry is Sucessfully Read...'
Write(*,*) '    ---------------------------------'

end subroutine
! ####################################################################

! #######################   Geometry Subroutines   #######################
Subroutine Nodxyz(nxx,nyy,nzz,nx,ny,nz,xdiv,ydiv,zdiv) ! To Calculate Number of Nodes in x,y & z Directions
Implicit None
Integer, Intent(in) :: nx, ny, nz
Integer, Dimension(nx), Intent(in) ::  xdiv            ! Assembly Size & Division
Integer, Dimension(ny), Intent(in) ::  ydiv            ! Assembly Size & Division
Integer, Dimension(nz), Intent(in) ::  zdiv            ! Assembly Size & Division

Integer, Intent(out) :: nxx, nyy, nzz
! Local Variables
Integer :: i, j, k

! x-direction
nxx=0
Do i= 1,nx
    nxx = nxx+xdiv(i)
End Do
! y-direction
nyy=0
Do j= 1,ny
    nyy = nyy+ydiv(j)
End Do
! z-direction
nzz=0
Do k= 1,nz
    nzz = nzz+zdiv(k)
End Do

End Subroutine

Subroutine Asmblg_delta(node,mnum,delx,dely,delz,nmat,np,nx,ny,nz,nxx,nyy,nzz,&
                        xsize,ysize,zsize,xdiv,ydiv,zdiv,zpln,assm) ! To assign Material into nodes & Calculate Delta x,y & z (node sizes)
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: np                              ! Number of planars
Integer, Intent(in) :: nmat, nx, ny, nz, nxx, nyy, nzz
Integer, Dimension(nx), Intent(in) ::  xdiv            ! Assembly Size & Division
Integer, Dimension(ny), Intent(in) ::  ydiv            ! Assembly Size & Division
Integer, Dimension(nz), Intent(in) ::  zdiv            ! Assembly Size & Division
Real(dp), Dimension(nx), Intent(in) :: xsize           ! Assembly Size & Division
Real(dp), Dimension(ny), Intent(in) :: ysize           ! Assembly Size & Division
Real(dp), Dimension(nz), Intent(in) :: zsize           ! Assembly Size & Division
Integer, Dimension(nz), Intent(in) :: zpln             ! Planar Assignment to Z Direction
Integer, Dimension(np,nx,ny), Intent(in) :: assm       ! Material Assignment into Assembly
Integer, Dimension(nxx,nyy,nzz), Intent(out) :: mnum
Integer, Dimension(np,nxx,nyy), Intent(out) :: node    ! Material Assignment into Nodes
Real(dp), Dimension(nxx), Intent(out) :: delx
Real(dp), Dimension(nyy), Intent(out) :: dely
Real(dp), Dimension(nzz), Intent(out) :: delz
! Local Variables
Integer :: i, j, k, lx, ly, lz, xtot, ytot, ztot
Real(dp) :: div
Integer, Parameter :: Ounit = 100   !output

Do k = 1, nz
    if (zpln(k) > np) Then
        Write(Ounit,'(2X,A15,I3,A35)') 'Error: Planar ', &
        zpln(k), ' is Greater than Number of Planar'
        Write(*,'(2X,A15,I3,A35)') 'Error: Planar ', &
        zpln(k), ' is Greater than Number of Planar'
        Stop
    End if
    if (zpln(k) < 1) Then
        Write(Ounit,'(2X,A)') 'Error: Planar Should Be at Least Equal 1'
        Write(*,'(2X,A)') 'Error: Planar Should Be at Least Equal 1'
        Stop
    End if
End Do

ztot = 0
Do k= 1, nz
    Do lz= 1, zdiv(k)
        ztot = ztot+1
        ytot = 0
        Do j= 1, ny
            Do ly= 1, ydiv(j)
                ytot = ytot+1
                xtot = 0
                Do i= 1, nx
                    Do lx= 1, xdiv(i)
                        xtot = xtot+1
                        mnum(xtot,ytot,ztot) = assm(zpln(k),j,i)
                        if (mnum(xtot,ytot,ztot) > nmat) Then
                            Write(ounit,'(2X,A17,I3,A37)') 'Error: Material ', &
                            mnum(xtot,ytot,ztot), ' is Greater than Number of Materials'
                            Write(*,'(2X,A17,I3,A37)') 'Error: Material ', &
                            mnum(xtot,ytot,ztot), ' is Greater than Number of Materials'
                            Stop
                        End if
                        if (mnum(xtot, ytot, ztot) < 0) Then
                            Write(ounit,'(2X,A)') 'Error: Negative Material Found'
                            Write(*,'(2X,A)') 'Error: Negative Material Found'
                            Stop
                        End if
                        node(zpln(k),xtot,ytot) = assm(zpln(k),j,i)
                    End Do
                End Do
            End Do
        End Do
    End Do
End Do

!Delta x
xtot=0
Do i= 1,nx
    div = xsize(i)/Real(xdiv(i))
    Do lx= 1, xdiv(i)
    xtot = xtot+1
    delx(xtot) = div
    End Do
End Do
!Delta y
ytot=0
Do j= 1,ny
    div = ysize(j)/Real(ydiv(j))
    Do ly= 1, ydiv(j)
    ytot = ytot+1
    dely(ytot) = div
    End Do
End Do
!Delta z
ztot=0
Do k= 1,nz
    div = zsize(k)/Real(zdiv(k))
    Do lz= 1, zdiv(k)
    ztot = ztot+1
    delz(ztot) = div
    End Do
End Do

End Subroutine

Subroutine Stagg(y_smax,y_smin,x_smax,x_smin,nxx,nyy,nzz,mnum) ! To Index non zero material for staggered mesh
Implicit None
Integer, Intent(in) :: nxx, nyy, nzz
Integer, Dimension(nxx,nyy,nzz), Intent(in) :: mnum
Integer, Dimension(nxx), Intent(out) :: x_smax, x_smin ! imax and imin along x Direction for Staggered Nodes
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin ! imax and imin along y Direction for Staggered Nodes
! Local Variables
Integer :: i, j

! Along y Direction
Do j= 1, nyy
    y_smin(j) = nxx
    Do i = 1, nxx
        if (mnum(i,j,1) /= 0) Then
            y_smin(j) = i
            Exit
        End if
    End Do
End Do
Do j= 1, nyy
    y_smax(j) = 0
    Do i = nxx, 1, -1
        if (mnum(i,j,1) /= 0) Then
            y_smax(j) = i
            Exit
        End if
    End Do
End Do
! Along x Direction
Do i= 1, nxx
    x_smin(i) = nyy
    Do j = 1, nyy
        if (mnum(i,j,1) /= 0) Then
            x_smin(i) = j
            Exit
        End if
    End Do
End Do
Do i= 1, nxx
    x_smax(i) = 0
    Do j = nyy, 1, -1
        if (mnum(i,j,1) /= 0) Then
            x_smax(i) = j
            Exit
        End if
    End Do
End Do

End Subroutine

Subroutine Nod(nk,nyy,nzz,y_smax,y_smin) ! To Set Number of Nodes
Implicit None
Integer, Intent(in) :: nyy, nzz
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Integer, Intent(out):: nk
! Local Variables
Integer :: i, j, k

nk = 0
Do k = 1, nzz
    Do j = 1, nyy
        Do i = y_smin(j), y_smax(j)
            nk = nk + 1
        End Do
    End Do
End Do

End Subroutine

Subroutine PosiNod(ix,iy,iz,xyz,mat,y_smax,y_smin,nk,nxx,nyy,nzz,mnum) ! To Set ix,iy,iz & xyz
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk
Integer, Intent(in) :: nxx, nyy, nzz
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Integer, Dimension(nxx,nyy,nzz), Intent(in) :: mnum
Real(dp), Dimension(nxx,nyy,nzz), Intent(out) :: xyz
Real(dp), Dimension(nk), Intent(out) :: ix, iy, iz
Integer, Dimension(nk), Intent(out) :: mat
! Local Variables
Integer :: i, j, k, n

n = 0
Do k = 1, nzz      ! Don't change the order as it would affect th_upd and th_trans
    Do j = nyy, 1, -1
        Do i = y_smin(j), y_smax(j)
            n = n + 1
            ix(n) = i
            iy(n) = j
            iz(n) = k
            xyz(i,j,k) = n
            mat(n) = mnum(i,j,k)
        End Do
    End Do
End Do

End Subroutine

Subroutine Deltv(delv,nk,nxx,nyy,nzz,delx,dely,delz,ix,iy,iz) ! To Calculate Nodes' Volume
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk, nxx, nyy, nzz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk), Intent(out) :: delv
! Local Variables
Integer :: i

Do i = 1, nk
    delv(i) = delx(ix(i)) * dely(iy(i)) * delz(iz(i))
End Do

End Subroutine
! #########################################################################

Subroutine xD_xsigr(xD,x_sigr,x_siga,x_sigs,x_sigtr,ng,nk) ! To Update Diffusion Coefficient and Removal XS
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk
Real(dp), Dimension(nk,ng,ng), Intent(in) :: x_sigs
Real(dp), Dimension(nk,ng), Intent(in) :: x_sigtr, x_siga
Real(dp), Dimension(nk,ng), Intent(out):: x_sigr, xD
! Local Variables
Integer :: k, g, h
Real(dp) :: som

Do k = 1, nk
    Do g = 1, ng
        xD(k,g) = 1./(3.*x_sigtr(k,g))
        som = 0.0
        Do h= 1, ng
            if (g/=h) som = som + x_sigs(k,g,h)
        End Do
        x_sigr(k,g) =  x_siga(k,g) + som
    End Do
End Do  

End Subroutine

Subroutine Init(keff,jo,ji,L0,al,f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk) ! To provide Initial Guess Values for Keff, Jin, Jout, Flux & Flux Moments
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk
Real(dp), Intent(out):: Keff
Real(dp), Dimension(nk,ng,6), Intent(out) :: jo, ji, al
Real(dp), Dimension(nk,ng,3), Intent(out) :: L0
Real(dp), Dimension(nk,ng), Intent(out) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
! Local Variables
Integer :: g, k

Keff = 1._dp
Do g= 1, ng
    Do k = 1, nk
        jo(k,g,:) = 1._dp
        ji(k,g,:) = 1._dp
        al(k,g,:) = 0.0     ! Default alpha
        Call Lxyz(L0,k,g,ng,nk,jo,ji)
        f0(k,g)  = 1._dp
        fx1(k,g) = 1._dp
        fy1(k,g) = 1._dp
        fz1(k,g) = 1._dp
        fx2(k,g) = 1._dp
        fy2(k,g) = 1._dp
        fz2(k,g) = 1._dp
    End Do
End Do

End Subroutine

Subroutine XS_updt(sigs,siga,sigtr,sigf,nu_sigf,D,sigr,ng,nk,nmat,&
                       mat,x_sigs,x_siga,x_sigtr,x_sigf,x_nu_sigf) ! To Update Current XS to Base XS
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nmat
!! CXs Assigned to Materials
Integer,  Dimension(nk), Intent(in) :: mat    ! Materials
Real(dp), Dimension(nmat,ng,ng), Intent(in) :: x_sigs
Real(dp), Dimension(nmat,ng), Intent(in) :: x_siga, x_sigtr, x_sigf, x_nu_sigf
!! CXs Assigned to Nodes
Real(dp), Dimension(nk,ng,ng), Intent(out) :: sigs
Real(dp), Dimension(nk,ng), Intent(out) :: siga, sigtr, sigf, nu_sigf, sigr, D
Integer :: k

Do k = 1, nk
    sigs (k,1:,1:) = x_sigs (mat(k),1:,1:)
    siga (k,1:)    = x_siga (mat(k),1:)
    sigtr (k,1:)   = x_sigtr(mat(k),1:)
    sigf (k,1:)    = x_sigf (mat(k),1:)
    nu_sigf (k,1:) = x_nu_sigf (mat(k),1:)
End Do
 
    Call D_sigr(D,sigr,siga,sigs,sigtr,ng,nk)

End Subroutine

Subroutine D_sigr(D,sigr,siga,sigs,sigtr,ng,nk) ! To Update Diffusion Coefficient and Removal XS
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: sigtr, siga
Real(dp), Dimension(nk,ng), Intent(out):: sigr, D
! Local Variables
Integer :: k, g, h
Real(dp) :: som

Do k = 1, nk
    Do g = 1, ng
        D(k,g) = 1./(3.*sigtr(k,g))
        som = 0.
        Do h= 1, ng
            if (g/=h) som = som + sigs(k,g,h)
        End Do
        sigr(k,g) = siga(k,g) + som
    End Do
End Do

End Subroutine

Subroutine Nodal_Coup4(P4,R4,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz) ! To Calculate Response Matrices R & P
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nxx, nyy, nzz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk),  Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng), Intent(in) :: D, sigr
Real(dp), Dimension(nk,ng,6,6),Intent(out) :: R4
Real(dp), Dimension(nk,ng,6,7),Intent(out) :: P4
! Local Variables
Real(dp), Dimension(6,6) :: A, B
Real(dp), Dimension(6,7) :: C
Integer :: k, g
Real(dp) :: dx, dy, dz, lx, ly, lz
Real(dp) :: ax, ay, az, ax1, ay1, az1, xy, xz, yx
Real(dp) :: bx, by, bz, bx1, by1, bz1, yz, zx, zy

Do g= 1, ng
    Do k = 1, nk
        dx = D(k,g) / delx(ix(k))
        dy = D(k,g) / dely(iy(k))
        dz = D(k,g) / delz(iz(k))
        lx = 1._dp / sigr(k,g) / delx(ix(k))
        ly = 1._dp / sigr(k,g) / dely(iy(k))
        lz = 1._dp / sigr(k,g) / delz(iz(k))
    ! Matrix A
        ax = 1._dp+32.0*dx+120.0*dx*lx+960.0*dx*dx*lx+840.0*dx*dx*lx*lx
        ay = 1._dp+32.0*dy+120.0*dy*ly+960.0*dy*dy*ly+840.0*dy*dy*ly*ly
        az = 1._dp+32.0*dz+120.0*dz*lz+960.0*dz*dz*lz+840.0*dz*dz*lz*lz
         A(1,1) = ax; A(2,2) = ax
         A(3,3) = ay; A(4,4) = ay
         A(5,5) = az; A(6,6) = az
        ax1 = 8.0*dx+60.0*dx*lx+720.0*dx*dx*lx+840.0*dx*dx*lx*lx
        ay1 = 8.0*dy+60.0*dy*ly+720.0*dy*dy*ly+840.0*dy*dy*ly*ly
        az1 = 8.0*dz+60.0*dz*lz+720.0*dz*dz*lz+840.0*dz*dz*lz*lz
         A(1,2) = ax1; A(2,1) = ax1
         A(3,4) = ay1; A(4,3) = ay1
         A(5,6) = az1; A(6,5) = az1
        xy = 20.*dx*ly+840.0*dx*dx*lx*ly
        xz = 20.*dx*lz+840.0*dx*dx*lx*lz
        yx = 20.*dy*lx+840.0*dy*dy*ly*lx
        yz = 20.*dy*lz+840.0*dy*dy*ly*lz
        zx = 20.*dz*lx+840.0*dz*dz*lz*lx
        zy = 20.*dz*ly+840.0*dz*dz*lz*ly
         A(1,3) = xy; A(1,4) = xy
         A(2,3) = xy; A(2,4) = xy
         A(1,5) = xz; A(1,6) = xz
         A(2,5) = xz; A(2,6) = xz

         A(3,1) = yx; A(3,2) = yx
         A(4,1) = yx; A(4,2) = yx
         A(3,5) = yz; A(3,6) = yz
         A(4,5) = yz; A(4,6) = yz

         A(5,1) = zx; A(5,2) = zx
         A(6,1) = zx; A(6,2) = zx
         A(5,3) = zy; A(5,4) = zy
         A(6,3) = zy; A(6,4) = zy
    ! Matrix B
         B = A
        bx = 1._dp-32.0*dx+120.0*dx*lx-960.0*dx*dx*lx+840.0*dx*dx*lx*lx
        by = 1._dp-32.0*dy+120.0*dy*ly-960.0*dy*dy*ly+840.0*dy*dy*ly*ly
        bz = 1._dp-32.0*dz+120.0*dz*lz-960.0*dz*dz*lz+840.0*dz*dz*lz*lz
        bx1 = -8.0*dx+60.0*dx*lx-720.0*dx*dx*lx+840.0*dx*dx*lx*lx
        by1 = -8.0*dy+60.0*dy*ly-720.0*dy*dy*ly+840.0*dy*dy*ly*ly
        bz1 = -8.0*dz+60.0*dz*lz-720.0*dz*dz*lz+840.0*dz*dz*lz*lz
         B(1,1) = bx; B(2,2) = bx    !Replace..
         B(3,3) = by; B(4,4) = by
         B(5,5) = bz; B(6,6) = bz

         B(1,2) = bx1; B(2,1) = bx1
         B(3,4) = by1; B(4,3) = by1
         B(5,6) = bz1; B(6,5) = bz1
    ! Matrix C
         C = 0.0
        ax = 20.*dx*lx*delx(ix(k))+840.0*dx*dx*lx*lx*delx(ix(k))
        ay = 20.*dy*ly*dely(iy(k))+840.0*dy*dy*ly*ly*dely(iy(k))
        az = 20.*dz*lz*delz(iz(k))+840.0*dz*dz*lz*lz*delz(iz(k))
         C(1,1) = ax; C(2,1) = ax
         C(3,1) = ay; C(4,1) = ay
         C(5,1) = az; C(6,1) = az
        ax1 = 60.0*dx*lx*delx(ix(k))
        ay1 = 60.0*dy*ly*dely(iy(k))
        az1 = 60.0*dz*lz*delz(iz(k))
         C(1,2) =  ax1; C(2,2) = -ax1 
         C(3,3) =  ay1; C(4,3) = -ay1
         C(5,4) =  az1; C(6,4) = -az1
        ax1 = 140.0*dx*lx*delx(ix(k))
        ay1 = 140.0*dy*ly*dely(iy(k))
        az1 = 140.0*dz*lz*delz(iz(k))
         C(1,5) = ax1; C(2,5) = ax1
         C(3,6) = ay1; C(4,6) = ay1
         C(5,7) = az1; C(6,7) = az1

        Call Inverse(A,g,k,nk,ix,iy,iz)

        R4(k,g,:,:) = MATMUL(A,B)
        P4(k,g,:,:) = MATMUL(A,C)
    End Do
End Do

End Subroutine

Subroutine Nodal_Coup2(P2,R2,delx,dely,delz,D,sigr,ix,iy,iz,ng,nk,nxx,nyy,nzz) ! To Calculate Response Matrices R & P
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nxx, nyy, nzz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk),  Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng), Intent(in) :: D, sigr
Real(dp), Dimension(nk,ng,6,6),Intent(out) :: R2, P2
! Local Variables
Real(dp), Dimension(6,6) :: A, B, C
Integer :: k, g
Real(dp) :: dx, dy, dz, lx, ly, lz
Real(dp) :: ax, ay, az, ax1, ay1, az1, xy, xz, yx
Real(dp) :: bx, by, bz, bx1, by1, bz1, yz, zx, zy

Do g= 1, ng
    Do k = 1, nk
        dx = D(k,g) / delx(ix(k))
        dy = D(k,g) / dely(iy(k))
        dz = D(k,g) / delz(iz(k))
        lx = 1._dp / sigr(k,g) / delx(ix(k))
        ly = 1._dp / sigr(k,g) / dely(iy(k))
        lz = 1._dp / sigr(k,g) / delz(iz(k))
    ! Matrix A
        ax = 1._dp+8.0*dx+6.0*dx*lx
        ay = 1._dp+8.0*dy+6.0*dy*ly
        az = 1._dp+8.0*dz+6.0*dz*lz
         A(1,1) = ax; A(2,2) = ax
         A(3,3) = ay; A(4,4) = ay
         A(5,5) = az; A(6,6) = az
        ax1 = 4.0*dx+6.0*dx*lx
        ay1 = 4.0*dy+6.0*dy*ly
        az1 = 4.0*dz+6.0*dz*lz
         A(1,2) = ax1; A(2,1) = ax1
         A(3,4) = ay1; A(4,3) = ay1
         A(5,6) = az1; A(6,5) = az1
        xy = 6.*dx*ly
        xz = 6.*dx*lz
        yx = 6.*dy*lx
        yz = 6.*dy*lz
        zx = 6.*dz*lx
        zy = 6.*dz*ly
         A(1,3) = xy; A(1,4) = xy
         A(2,3) = xy; A(2,4) = xy
         A(1,5) = xz; A(1,6) = xz
         A(2,5) = xz; A(2,6) = xz

         A(3,1) = yx; A(3,2) = yx
         A(4,1) = yx; A(4,2) = yx
         A(3,5) = yz; A(3,6) = yz
         A(4,5) = yz; A(4,6) = yz

         A(5,1) = zx; A(5,2) = zx
         A(6,1) = zx; A(6,2) = zx
         A(5,3) = zy; A(5,4) = zy
         A(6,3) = zy; A(6,4) = zy
    ! Matrix B
         B = A
        bx = 1._dp-8.0*dx+6.0*dx*lx
        by = 1._dp-8.0*dy+6.0*dy*ly
        bz = 1._dp-8.0*dz+6.0*dz*lz
        bx1 = -4.0*dx+6.0*dx*lx
        by1 = -4.0*dy+6.0*dy*ly
        bz1 = -4.0*dz+6.0*dz*lz
         B(1,1) = bx; B(2,2) = bx    !Replace..
         B(3,3) = by; B(4,4) = by
         B(5,5) = bz; B(6,6) = bz

         B(1,2) = bx1; B(2,1) = bx1
         B(3,4) = by1; B(4,3) = by1
         B(5,6) = bz1; B(6,5) = bz1
    ! Matrix C
         C = 0.0
        ax1 = 6.0*dx*lx*delx(ix(k))
        ay1 = 6.0*dy*ly*dely(iy(k))
        az1 = 6.0*dz*lz*delz(iz(k))
         C(1,1) =  ax1; C(2,1) = ax1 
         C(3,1) =  ay1; C(4,1) = ay1
         C(5,1) =  az1; C(6,1) = az1

        Call Inverse(A,g,k,nk,ix,iy,iz)
        R2(k,g,:,:) = MATMUL(A,B)
        P2(k,g,:,:) = MATMUL(A,C)

    End Do
End Do

End Subroutine

    Subroutine Inverse(Mtx,g,n,nk,ix,iy,iz) ! To Perform Matrix Inverse by LU Decomposition 
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk, g, n
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz  ! x-position, y-position and z-position of the Node
Real(dp), Dimension(6,6), Intent(inout) :: Mtx
! Local Variables
Integer, Parameter :: Ounit = 100   !output
Real(dp), Dimension(6,6) :: L, U, imat, pmat
Real(dp), Dimension(6) :: y
Real(dp) :: piv, isum
Integer :: i, j, k

pmat = Mtx
U = Mtx
L = 0.0
! Start Matrix Decomposition
Do i= 1, 6
    if (ABS(Mtx(i,i)) < 10e-3) Then
      Write(ounit,*) 'Error in Matrix Decomposition: Diagonal Elements Close to Zero'
      Write(ounit,2001) g, ix(n), iy(n), iz(n)
      Write(*,*) 'Error in Matrix Decomposition: Diagonal Elements Close to Zero'
      Write(*,2001) g, ix(n), iy(n), iz(n)
      Stop
    End if
    L(i,i) = 1._dp
    Do j= i+1, 6
        piv = U(j,i)/U(i,i)
        L(j,i) = piv
        Do k= i, 6
            U(j,k) = U(j,k) - piv*U(i,k)
        End Do
        U(j,i) = 0.0
    End Do
End Do
! Check matrix decomposition
Do i = 1,6
    Do j = 1,6
        isum = 0.0
        Do k = 1,6
            isum = isum+L(i,k)*U(k,j)
        End Do
        if (ABS(Mtx(i,j)-isum)/ABS(Mtx(i,j)) > 1.e-3_dp) Then
            Write(ounit,*) 'Error in Matrix Decomposition: Decomposition Failed'
            Write(ounit,2001) g, ix(n), iy(n), iz(n)
            Write(*,*) 'Error in Matrix Decomposition: Decomposition Failed'
            Write(*,2001) g, ix(n), iy(n), iz(n)
            Stop
        End if
    End Do
End Do
!Initialiaze Identity matrix
imat = 0.0
Do i= 1, 6
    imat(i,i) = 1._dp
End Do
! Calculate matrix inverse
! Ref: https://www.gamedev.net/resources/_/technical/math-and-physics/matrix-inversion-using-lu-decomposition-r3637
Do j=1,6   ! For each column
    !Solve y in Ly = b (Forward substitution)
    y(1) = imat(1,j)
    Do i=2,6
        isum = 0.0
        Do k =1, i-1
            isum = isum + L(i,k)*y(k)
        End Do
        y(i) = imat(i,j)-isum
    End Do
    ! Solve x in Ux=y(Backward substitution) and store inverse matrix to input matrix 'mat'
    Mtx(6,j) = y(6)/U(6,6)
    Do i = 5,1,-1
        isum = 0.0
        Do k =i+1,6
            isum = isum + U(i,k)*Mtx(k,j)
        End Do
        Mtx(i,j) = (y(i)-isum) / U(i,i)
    End Do
End Do
!Check Matrix Inverse
Do i = 1,6
    Do j = 1,6
        isum = 0.0
        Do k = 1,6
            isum = isum+pmat(i,k)*Mtx(k,j)
        End Do
        if (ABS(imat(i,j)-isum) > 1.e-4_dp) Then
            Write(ounit,*) 'Error in Matrix Inversion'
            Write(ounit,2001) g, ix(n), iy(n), iz(n)
            Write(*,*) 'Error in Matrix Inversion'
            Write(*,2001) g, ix(n), iy(n), iz(n)
            Stop
        End if
    End Do
End Do

2001 Format(2X, 'Group = ', I2, ', I = ', I2, ', J = ', I2, ', K = ', I2)

End Subroutine

Subroutine FSrc(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,&
                f0,fx1,fy1,fz1,fx2,fy2,fz2,nu_sigf,ng,nk) ! To Calculate Fission Source & Fission Source Moments
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk
Real(dp), Dimension(nk,ng), Intent(in) :: nu_sigf, f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Dimension(nk), Intent(out) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2
! Local Variables
Integer :: g, k

fs0 = 0.; fsx1 = 0.; fsy1 = 0.; fsz1 = 0.; fsx2 = 0.; fsy2 = 0.; fsz2 = 0.
Do g = 1, ng
    Do k = 1, nk
       fs0(k)  = fs0(k)  + nu_sigf(k,g) * f0 (k,g)
       fsx1(k) = fsx1(k) + nu_sigf(k,g) * fx1(k,g) 
       fsy1(k) = fsy1(k) + nu_sigf(k,g) * fy1(k,g) 
       fsz1(k) = fsz1(k) + nu_sigf(k,g) * fz1(k,g)
       fsx2(k) = fsx2(k) + nu_sigf(k,g) * fx2(k,g) 
       fsy2(k) = fsy2(k) + nu_sigf(k,g) * fy2(k,g) 
       fsz2(k) = fsz2(k) + nu_sigf(k,g) * fz2(k,g)
    End Do 
End Do

End Subroutine

Subroutine FSrcAdj(fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,mat,chi,&
                   f0,fx1,fy1,fz1,fx2,fy2,fz2,ng,nk,nmat)    ! To Calculate Adjoint Fission Source & Fission Source Moments
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nmat
Integer, Dimension(nk), Intent(in) :: mat
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng), Intent(in) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Dimension(nk), Intent(out) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2
! Local Variables
Integer :: g, k

fs0 = 0.; fsx1 = 0.; fsy1 = 0.; fsz1 = 0.; fsx2 = 0.; fsy2 = 0.; fsz2 = 0.
Do g = 1, ng
    Do k = 1, nk
      fs0(k)  = fs0(k)  + f0 (k,g) * chi(mat(k),g)
      fsx1(k) = fsx1(k) + fx1(k,g) * chi(mat(k),g)
      fsy1(k) = fsy1(k) + fy1(k,g) * chi(mat(k),g)
      fsz1(k) = fsz1(k) + fz1(k,g) * chi(mat(k),g)
      fsx2(k) = fsx2(k) + fx2(k,g) * chi(mat(k),g)
      fsy2(k) = fsy2(k) + fy2(k,g) * chi(mat(k),g)
      fsz2(k) = fsz2(k) + fz2(k,g) * chi(mat(k),g)
    End Do
End Do

End Subroutine 

Subroutine Integrate(ss,s,delv,nk) ! To Perform Fs Volume Integration
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk
Real(dp), Dimension(nk), Intent(in) :: delv, s
Real(dp), Intent(out) :: ss
! Local Variables
Integer:: k

ss = 0.
Do k = 1, nk
    ss = ss + delv(k) * s(k)
End Do

End Subroutine

Subroutine TSrc(Q,g,Keff,ng,nmat,nk,chi,mat,sigs,f0,fx1,fy1,fz1,&
                        fx2,fy2,fz2,fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2) ! To Update Total Source
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, ng, nk, nmat
Integer,  Dimension(nk), Intent(in) :: mat
Real(dp), Intent(in) :: Keff
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Dimension(nk), Intent(in) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2
Real(dp), Dimension(nk,ng,7),Intent(out) :: Q
! Local Variables
Real(dp), Dimension(nk) :: s0, sx1, sy1, sz1, sx2, sy2, sz2     ! Scattering Source and Scattering Source Moments
Integer :: h, k

s0 = 0.; sx1 = 0.; sy1 = 0.; sz1 = 0.; sx2 = 0.; sy2 = 0.; sz2 = 0.
Do h = 1, ng
    Do k = 1, nk
        if (g /= h) Then
            s0(k)  = s0(k)  + sigs(k,h,g) * f0(k,h)
            sx1(k) = sx1(k) + sigs(k,h,g) * fx1(k,h)
            sy1(k) = sy1(k) + sigs(k,h,g) * fy1(k,h)
            sz1(k) = sz1(k) + sigs(k,h,g) * fz1(k,h)
            sx2(k) = sx2(k) + sigs(k,h,g) * fx2(k,h)
            sy2(k) = sy2(k) + sigs(k,h,g) * fy2(k,h)
            sz2(k) = sz2(k) + sigs(k,h,g) * fz2(k,h)
        End if
    End Do
End Do
Do k = 1, nk
    Q(k,g,1) = chi(mat(k),g) * fs0(k)/Keff  + s0(k)
    Q(k,g,2) = chi(mat(k),g) * fsx1(k)/Keff + sx1(k)
    Q(k,g,3) = chi(mat(k),g) * fsy1(k)/Keff + sy1(k)
    Q(k,g,4) = chi(mat(k),g) * fsz1(k)/Keff + sz1(k)
    Q(k,g,5) = chi(mat(k),g) * fsx2(k)/Keff + sx2(k)
    Q(k,g,6) = chi(mat(k),g) * fsy2(k)/Keff + sy2(k)
    Q(k,g,7) = chi(mat(k),g) * fsz2(k)/Keff + sz2(k)
End Do

End Subroutine

Subroutine TSrcAdj(Q,Keff,sigs,nu_sigf,f0,fx1,fy1,fz1,fx2,fy2,fz2,&
                   fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,g,ng,nk)      ! To Update Adjoint Total Source
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, ng, nk
Real(dp), Intent(in) :: Keff
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: nu_sigf, f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Dimension(nk), Intent(in) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2
Real(dp), Dimension(nk,ng,7),Intent(out) :: Q
! Local Variables
Real(dp), Dimension(nk) :: s0, sx1, sy1, sz1, sx2, sy2, sz2     ! Scattering Source and Scattering Source Moments
Integer :: h, k

s0 = 0.; sx1 = 0.; sy1 = 0.; sz1 = 0.; sx2 = 0.; sy2 = 0.; sz2 = 0.
Do h = 1, ng
    Do k = 1, nk
        if (g /= h) Then
            s0(k)  = s0(k)  + sigs(k,g,h) * f0(k,h)
            sx1(k) = sx1(k) + sigs(k,g,h) * fx1(k,h)
            sy1(k) = sy1(k) + sigs(k,g,h) * fy1(k,h)
            sz1(k) = sz1(k) + sigs(k,g,h) * fz1(k,h)
            sx2(k) = sx2(k) + sigs(k,g,h) * fx2(k,h)
            sy2(k) = sy2(k) + sigs(k,g,h) * fy2(k,h)
            sz2(k) = sz2(k) + sigs(k,g,h) * fz2(k,h)
        End if
    End Do
End Do
Do k = 1, nk
    Q(k,g,1) = nu_sigf(k,g) * fs0(k)/Keff  + s0(k)
    Q(k,g,2) = nu_sigf(k,g) * fsx1(k)/Keff + sx1(k)
    Q(k,g,3) = nu_sigf(k,g) * fsy1(k)/Keff + sy1(k)
    Q(k,g,4) = nu_sigf(k,g) * fsz1(k)/Keff + sz1(k)
    Q(k,g,5) = nu_sigf(k,g) * fsx2(k)/Keff + sx2(k)
    Q(k,g,6) = nu_sigf(k,g) * fsy2(k)/Keff + sy2(k)
    Q(k,g,7) = nu_sigf(k,g) * fsz2(k)/Keff + sz2(k)
End Do

End Subroutine

Subroutine TSrcFx(Q,g,ng,nmat,nk,chi,mat,sigs,f0,fx1,fy1,fz1,&
                  fx2,fy2,fz2,fs0,fsx1,fsy1,fsz1,fsx2,fsy2,fsz2,eSrc) ! To Update Total Source
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, ng, nk, nmat
Integer,  Dimension(nk), Intent(in) :: mat
Real(dp), Dimension(nmat,ng), Intent(in) :: chi
Real(dp), Dimension(nk,ng), Intent(in) :: eSrc
Real(dp), Dimension(nk,ng,ng), Intent(in) :: sigs
Real(dp), Dimension(nk,ng), Intent(in) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
Real(dp), Dimension(nk), Intent(in) :: fs0, fsx1, fsy1, fsz1, fsx2, fsy2, fsz2
Real(dp), Dimension(nk,ng,7),Intent(out) :: Q
! Local Variables
Real(dp), Dimension(nk) :: s0, sx1, sy1, sz1, sx2, sy2, sz2     ! Scattering Source and Scattering Source Moments
Integer :: h, k

s0 = 0.; sx1 = 0.; sy1 = 0.; sz1 = 0.; sx2 = 0.; sy2 = 0.; sz2 = 0.
Do h = 1, ng
    Do k = 1, nk
        if (g /= h) Then
            s0(k)  = s0(k)  + sigs(k,h,g) * f0(k,h)
            sx1(k) = sx1(k) + sigs(k,h,g) * fx1(k,h)
            sy1(k) = sy1(k) + sigs(k,h,g) * fy1(k,h)
            sz1(k) = sz1(k) + sigs(k,h,g) * fz1(k,h)
            sx2(k) = sx2(k) + sigs(k,h,g) * fx2(k,h)
            sy2(k) = sy2(k) + sigs(k,h,g) * fy2(k,h)
            sz2(k) = sz2(k) + sigs(k,h,g) * fz2(k,h)
        End if
    End Do
End Do
Do k = 1, nk
    Q(k,g,1) = chi(mat(k),g) * fs0(k)  + s0(k) + eSrc(k,g)
    Q(k,g,2) = chi(mat(k),g) * fsx1(k) + sx1(k)
    Q(k,g,3) = chi(mat(k),g) * fsy1(k) + sy1(k)
    Q(k,g,4) = chi(mat(k),g) * fsz1(k) + sz1(k)
    Q(k,g,5) = chi(mat(k),g) * fsx2(k) + sx2(k)
    Q(k,g,6) = chi(mat(k),g) * fsy2(k) + sy2(k)
    Q(k,g,7) = chi(mat(k),g) * fsz2(k) + sz2(k)
End Do

End Subroutine

Subroutine Jin(ji,g,k,jo,al,ng,nk,nxx,nyy,nzz,ix,iy,iz,x_smax,x_smin,&
                           y_smax,y_smin,xyz,x_east,x_west,y_north,y_south,z_top,z_bott) ! To Calculate Ingoing Partial Currents from Neighborhod Nodes
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng,6), Intent(in) :: al, jo
Real(dp), Dimension(nk,ng,6), Intent(out):: ji

! g : Group, k : Nod, (Nmbr): Direction of Axes (+) or (-)         
    if (ix(k) == y_smax(iy(k))) Then    ! East (X+) BC
        Call BCond(ji,x_east,k,g,1,jo,ng,nk)
    Else
        ji(k,g,1) = (jo(xyz(ix(k)+1,iy(k),iz(k)),g,2) + &  
                    al(k,g,1)*jo(k,g,1)) / (1._dp-al(k,g,1))
    End if
    if (ix(k) == y_smin(iy(k))) Then    ! West (X-) BC
        Call BCond(ji,x_west,k,g,2,jo,ng,nk)
    Else
        ji(k,g,2) = (jo(xyz(ix(k)-1,iy(k),iz(k)),g,1) + &  
                    al(k,g,2)*jo(k,g,2)) / (1._dp-al(k,g,2))
    End if
    if (iy(k) == x_smax(ix(k))) Then    ! North (Y+) BC
        Call BCond(ji,y_north,k,g,3,jo,ng,nk)
    Else
        ji(k,g,3) = (jo(xyz(ix(k),iy(k)+1,iz(k)),g,4) + &  
                    al(k,g,3)*jo(k,g,3)) / (1._dp-al(k,g,3))
    End if
    if (iy(k) == x_smin(ix(k))) Then    ! South (Y-) BC
        Call BCond(ji,y_south,k,g,4,jo,ng,nk)
    Else
        ji(k,g,4) = (jo(xyz(ix(k),iy(k)-1,iz(k)),g,3) + &  
                    al(k,g,4)*jo(k,g,4)) / (1._dp-al(k,g,4))
    End if
    If (iz(k) == nzz) Then              ! Top (Z+) BC
        Call BCond(ji,z_top,k,g,5,jo,ng,nk)
    Else
        ji(k,g,5) = (jo(xyz(ix(k),iy(k),iz(k)+1),g,6) + &
                    al(k,g,5)*jo(k,g,5)) / (1._dp-al(k,g,5))
    End if
    If (iz(k) == 1) Then                ! Bottom (Z-)BC
        Call BCond(ji,z_bott,k,g,6,jo,ng,nk)
    Else
        ji(k,g,6) = (jo(xyz(ix(k),iy(k),iz(k)-1),g,5) + &
                    al(k,g,6)*jo(k,g,6)) / (1._dp-al(k,g,6))
    End if

End Subroutine

    Subroutine BCond(ji,bc,k,g,side,jo,ng,nk) ! To Provide proper Boundary Conditions
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk, bc, side
Real(dp), Dimension(nk,ng,6),Intent(in) :: jo
Real(dp), Dimension(nk,ng,6),Intent(out):: ji

    if (bc == 0) Then
        ji(k,g,side) = -jo(k,g,side)
    Else if (bc == 1) Then                    ! Vacuum Boundary
        ji(k,g,side) = 0.0
    Else                                      ! Reflective Boundary
        ji(k,g,side) = jo(k,g,side)
    End if

End Subroutine

Subroutine QTL(L,g,k,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xyz,x_smax,x_smin,&
                           y_smax,y_smin,L0,x_east,x_west,y_north,y_south,z_top,z_bott) ! To Calculate Transverse Leakage Moments using Quadratic Transverse Leakage Approximation
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk, nxx, nyy, nzz, x_east, x_west, y_north, y_south, z_top, z_bott
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Real(dp), Dimension(nk,ng,3), Intent(in) :: L0
Real(dp), Dimension(7), Intent(out) :: L     ! Transverse Leakage Moments(0, Lx1, Ly1, Lz1, Lx2, Ly2, Lz2)
!Local Variables
Real(dp) :: xm, xp, ym, yp, zm, zp
Real(dp) :: p1m, p2m, p1p, p2p, mm, pp, p1, p2, p3
Real(dp) :: p1xy, p2xy, p1xz, p2xz
Real(dp) :: p1yx, p2yx, p1yz, p2yz
Real(dp) :: p1zx, p2zx, p1zy, p2zy
         
! Set Paramaters for X_Direction Transverse Leakage
if (ix(k) == y_smax(iy(k))) Then                ! X+ Plan
    if (x_east == 0 .OR. x_east == 1) Then         ! Vacuum Boundary Conditions
        xm = delx(ix(k)-1)/delx(ix(k))
        p1m = xm+1._dp
        
        p1xy = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,2)   &
                  - L0(xyz(ix(k)-1,iy(k),iz(k)),g,2) &
                  ) / p1m
        p2xy = 0.0
        p1xz = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,3)   &
                  - L0(xyz(ix(k)-1,iy(k),iz(k)),g,3) &
                  ) / p1m
        p2xz = 0.0
    Else                                           ! Reflective Boundary Conditions
        xm = delx(ix(k)-1)/delx(ix(k))
        xp = 1._dp
        p1m = xm+1._dp; p2m = 2.*xm+1._dp; mm = p1m*p2m; p2 = xm+xp+2.;
        p1p = xp+1._dp; p2p = 2.*xp+1._dp; pp = p1p*p2p; p1 = pp-mm;
        p3 = p1m*p1p*(xm+xp+1._dp)
               
        P1xy = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,2)      &
               - pp * L0(xyz(ix(k)-1,iy(k),iz(k)),g,2)    &
               + p1 * L0(k,g,2)                           &
               ) / p3
        P2xy = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,2)     &
               + p1p * L0(xyz(ix(k)-1,iy(k),iz(k)),g,2)   &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)     &
               ) / p3
        P1xz = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,3)      &
               - pp * L0(xyz(ix(k)-1,iy(k),iz(k)),g,3)    &
               + p1 * L0(k,g,3)                           &
               ) / p3
        P2xz = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,3)     &
               + p1p * L0(xyz(ix(k)-1,iy(k),iz(k)),g,3)   &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,3)     &
               ) / p3
    End if
Else if (ix(k) == y_smin(iy(k))) Then           ! X- Plan                       
    if (x_west == 0 .OR. x_west == 1) Then         ! Vacuum Boundary Conditions
        xp = delx(ix(k)+1)/delx(ix(k))
        p1p = xp+1._dp
        
        p1xy = 2.*( L0(xyz(ix(k)+1,iy(k),iz(k)),g,2) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,2)   &
                  ) / p1p
        p2xy = 0.0
        p1xz = 2.*( L0(xyz(ix(k)+1,iy(k),iz(k)),g,3) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,3)   &
                  ) / p1p
        p2xz = 0.0
    Else                                           ! Reflective Boundary Conditions
        xm = 1._dp
        xp = delx(ix(k)+1)/delx(ix(k))
        p1m = xm+1._dp; p2m = 2.*xm+1._dp; mm = p1m*p2m; p2 = xm+xp+2.;
        p1p = xp+1._dp; p2p = 2.*xp+1._dp; pp = p1p*p2p; p1 = pp-mm;
        p3 = p1m*p1p*(xm+xp+1._dp)
         
        P1xy = ( mm * L0(xyz(ix(k)+1,iy(k),iz(k)),g,2)   &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,2)     &
               + p1 * L0(k,g,2)                          &
               ) / p3
        P2xy = ( p1m * L0(xyz(ix(k)+1,iy(k),iz(k)),g,2)  &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
               ) / p3
        P1xz = ( mm * L0(xyz(ix(k)+1,iy(k),iz(k)),g,3)   &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,3)     &
               + p1 * L0(k,g,3)                          &
               ) / p3
        P2xz = ( p1m * L0(xyz(ix(k)+1,iy(k),iz(k)),g,3)  &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,3)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,3)    &
               ) / p3
    End if
Else
    xm = delx(ix(k)-1)/delx(ix(k))
    xp = delx(ix(k)+1)/delx(ix(k))     
    p1m = xm+1._dp; p2m = 2.*xm+1._dp; mm = p1m*p2m; p2 = xm+xp+2.    
    p1p = xp+1._dp; p2p = 2.*xp+1._dp; pp = p1p*p2p; p1 = pp-mm;
    p3 = p1m*p1p*(xm+xp+1._dp)
    
    P1xy = ( mm * L0(xyz(ix(k)+1,iy(k),iz(k)),g,2)   &
           - pp * L0(xyz(ix(k)-1,iy(k),iz(k)),g,2)   &
           + p1 * L0(k,g,2)                          &
           ) / p3
    P2xy = ( p1m * L0(xyz(ix(k)+1,iy(k),iz(k)),g,2)  &
           + p1p * L0(xyz(ix(k)-1,iy(k),iz(k)),g,2)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
           ) / p3
    P1xz = ( mm * L0(xyz(ix(k)+1,iy(k),iz(k)),g,3)   &
           - pp * L0(xyz(ix(k)-1,iy(k),iz(k)),g,3)   &
           + p1 * L0(k,g,3)                          &
           ) / p3
    P2xz = ( p1m * L0(xyz(ix(k)+1,iy(k),iz(k)),g,3)  &
           + p1p * L0(xyz(ix(k)-1,iy(k),iz(k)),g,3)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,3)    &
           ) / p3
End if

! Set Paramaters for Y_Direction Transverse Leakage
if (iy(k) == x_smax(ix(k))) Then                ! Y+ Plan
    if (y_north == 0 .OR. y_north == 1) Then       ! Vacuum Boundary Conditions
        ym = dely(iy(k)-1)/dely(iy(k))
        p1m = ym+1._dp
        
        p1yx = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,1)   &
                  - L0(xyz(ix(k),iy(k)-1,iz(k)),g,1) &
                  ) / p1m
        p2yx = 0.0
        p1yz = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,3)   &
                  - L0(xyz(ix(k),iy(k)-1,iz(k)),g,3) &
                  ) / p1m
        p2yz = 0.0 
     Else                                          ! Reflective Boundary Conditions
        yp = 1._dp
        ym = dely(iy(k)-1)/dely(iy(k))
        p1m = ym+1._dp; p2m = 2.*ym+1._dp; mm = p1m*p2m; p2 = ym+yp+2.;
        p1p = yp+1._dp; p2p = 2.*yp+1._dp; pp = p1p*p2p; p1 = pp-mm;
        p3 = p1m*p1p*(ym+yp+1._dp)
               
        P1yx = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,1)      &
               - pp * L0(xyz(ix(k),iy(k)-1,iz(k)),g,1)    &
               + p1 * L0(k,g,1)                           &
               ) / p3
        P2yx = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,1)     &
               + p1p * L0(xyz(ix(k),iy(k)-1,iz(k)),g,1)   &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)     &
               ) / p3
        P1yz = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,3)      &
               - pp * L0(xyz(ix(k),iy(k)-1,iz(k)),g,3)    &
               + p1 * L0(k,g,3)                           &
               ) / p3
        P2yz = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,3)     &
               + p1p * L0(xyz(ix(k),iy(k)-1,iz(k)),g,3)   &
               - p2  * l0(xyz(ix(k),iy(k),iz(k)),g,3)     &
               ) / p3
    End If
Else if (iy(k) == x_smin(ix(k))) Then           ! Y- Plan
    if (y_south == 0 .OR. y_south == 1) Then       ! Vacuum Boundary Conditions
        yp = dely(iy(k)+1)/dely(iy(k))
        p1p = yp+1._dp
        
        p1yx = 2.*( L0(xyz(ix(k),iy(k)+1,iz(k)),g,1) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,1)   &
                  ) / p1p
        p2yx = 0.0
        p1yz = 2.*( L0(xyz(ix(k),iy(k)+1,iz(k)),g,3) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,3)   &
                  ) / p1p
        p2yz = 0.0 
     Else                                          ! Reflective Boundary Conditions
        ym = 1._dp
        yp = dely(iy(k)+1)/dely(iy(k))
        p1m = ym+1._dp; p2m = 2.*ym+1._dp; mm = p1m*p2m; p2 = ym+yp+2.;
        p1p = yp+1._dp; p2p = 2.*yp+1._dp; pp = p1p*p2p; p1 = pp-mm;
        p3 = p1m*p1p*(ym+yp+1._dp)
               
        P1yx = ( mm * L0(xyz(ix(k),iy(k)+1,iz(k)),g,1)      &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,1)        &
               + p1 * L0(k,g,1)                             &
               ) / p3
        P2yx = ( p1m * L0(xyz(ix(k),iy(k)+1,iz(k)),g,1)     &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,1)       &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)       &
               ) / p3
        P1yz = ( mm * L0(xyz(ix(k),iy(k)+1,iz(k)),g,3)      &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,3)        &
               + p1 * L0(k,g,3)                             &
               ) / p3
        P2yz = ( p1m * L0(xyz(ix(k),iy(k)+1,iz(k)),g,3)     &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,3)       &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,3)       &
               ) / p3
    End if
Else
    ym = dely(iy(k)-1)/dely(iy(k))
    yp = dely(iy(k)+1)/dely(iy(k))     
    p1m = ym+1._dp; p2m = 2.*ym+1._dp; mm = p1m*p2m; p2 = ym+yp+2.    
    p1p = yp+1._dp; p2p = 2.*yp+1._dp; pp = p1p*p2p; p1 = pp-mm;
    p3 = p1m*p1p*(ym+yp+1._dp)
    
    P1yx = ( mm * L0(xyz(ix(k),iy(k)+1,iz(k)),g,1)   &
           - pp * L0(xyz(ix(k),iy(k)-1,iz(k)),g,1)   &
           + p1 * L0(k,g,1)                          &
           ) / p3
    P2yx = ( p1m * L0(xyz(ix(k),iy(k)+1,iz(k)),g,1)  &
           + p1p * L0(xyz(ix(k),iy(k)-1,iz(k)),g,1)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)    &
           ) / p3
    P1yz = ( mm * L0(xyz(ix(k),iy(k)+1,iz(k)),g,3)   &
           - pp * L0(xyz(ix(k),iy(k)-1,iz(k)),g,3)   &
           + p1 * L0(k,g,3)                          &
           ) / p3
    P2yz = ( p1m * L0(xyz(ix(k),iy(k)+1,iz(k)),g,3)  &
           + p1p * L0(xyz(ix(k),iy(k)-1,iz(k)),g,3)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,3)    &
           ) / p3
End if

! Set Paramaters for Z_Direction Transverse Leakage
if (iz(k) == 1) Then                            ! Z- Plan
    if (z_bott == 0 .OR. z_bott == 1) Then         ! Vacuum Boundary Conditions
        zp = delz(iz(k)+1)/delz(iz(k))
        p1p = zp+1._dp
        
        p1zx = 2.*( L0(xyz(ix(k),iy(k),iz(k)+1),g,1) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,1)   &
                  ) / p1p
        p2zx = 0.0
        p1zy = 2.*( L0(xyz(ix(k),iy(k),iz(k)+1),g,2) &
                  - L0(xyz(ix(k),iy(k),iz(k)),g,2)   &
                  ) / p1p
        p2zy = 0.0
    Else                                           ! Reflective Boundary Conditions
        zm = 1._dp
        zp = delz(iz(k)+1)/delz(iz(k))
        p1m = zm+1._dp; p2m = 2.*zm+1._dp; mm = p1m*p2m; p2 = zm+zp+2.
        p1p = zp+1._dp; p2p = 2.*zp+1._dp; pp = p1p*p2p; p1 = pp-mm
        p3 = p1m*p1p*(zm+zp+1._dp)
        
        P1zx = ( mm * L0(xyz(ix(k),iy(k),iz(k)+1),g,1)   &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,1)     &
               + p1 * L0(k,g,1)                          &
               ) / p3
        P2zx = ( p1m * L0(xyz(ix(k),iy(k),iz(k)+1),g,1)  &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,1)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)    &
               ) / p3
        P1zy = ( mm * L0(xyz(ix(k),iy(k),iz(k)+1),g,2)   &
               - pp * L0(xyz(ix(k),iy(k),iz(k)),g,2)     &
               + p1 * L0(k,g,2)                          &
               ) / p3
        P2zy = ( p1m * L0(xyz(ix(k),iy(k),iz(k)+1),g,2)  &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
               ) / p3
    End if
Else if (iz(k) == nzz) Then                     ! Z+ Plan
    if (z_top == 0 .OR. z_top == 1) Then           ! Vacuum Boundary Conditions
        zm = delz(iz(k)-1)/delz(iz(k))
        p1m = zm+1._dp
        
        p1zx = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,1)   &
                  - L0(xyz(ix(k),iy(k),iz(k)-1),g,1) &
                  ) / p1m
        p2zx = 0.0
        p1zy = 2.*( L0(xyz(ix(k),iy(k),iz(k)),g,2)   &
                  - L0(xyz(ix(k),iy(k),iz(k)-1),g,2) &
                  ) / p1m
        p2zy = 0.0
    Else                                           ! Reflective Boundary Conditions
        zp = 1._dp
        zm = delz(iz(k)-1)/delz(iz(k))
        p1m = zm+1._dp; p2m = 2.*zm+1._dp; mm = p1m*p2m; p2 = zm+zp+2.
        p1p = zp+1._dp; p2p = 2.*zp+1._dp; pp = p1p*p2p; p1 = pp-mm
        p3 = p1m*p1p*(zm+zp+1._dp)
        
        P1zx = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,1)       &
               - pp * L0(xyz(ix(k),iy(k),iz(k)-1),g,1)     &
               + p1 * L0(k,g,1)                            &
               ) / p3
        P2zx = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,1)      &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)-1),g,1)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)      &
               ) / p3
        P1zy = ( mm * L0(xyz(ix(k),iy(k),iz(k)),g,2)       &
               - pp * L0(xyz(ix(k),iy(k),iz(k)-1),g,2)     &
               + p1 * L0(k,g,2)                            &
               ) / p3
        P2zy = ( p1m * L0(xyz(ix(k),iy(k),iz(k)),g,2)      &
               + p1p * L0(xyz(ix(k),iy(k),iz(k)-1),g,2)    &
               - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)      &
               ) / p3
    End if
Else
    zm = delz(iz(k)-1)/delz(iz(k))
    zp = delz(iz(k)+1)/delz(iz(k))     
    p1m = zm+1._dp; p2m = 2.*zm+1._dp; mm = p1m*p2m; p2 = zm+zp+2.    
    p1p = zp+1._dp; p2p = 2.*zp+1._dp; pp = p1p*p2p; p1 = pp-mm;
    p3 = p1m*p1p*(zm+zp+1._dp)
    
    P1zx = ( mm * L0(xyz(ix(k),iy(k),iz(k)+1),g,1)   &
           - pp * L0(xyz(ix(k),iy(k),iz(k)-1),g,1)   &
           + p1 * L0(k,g,1)                          &
           ) / p3
    P2zx = ( p1m * L0(xyz(ix(k),iy(k),iz(k)+1),g,1)  &
           + p1p * L0(xyz(ix(k),iy(k),iz(k)-1),g,1)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,1)    &
           ) / p3
    P1zy = ( mm * L0(xyz(ix(k),iy(k),iz(k)+1),g,2)   &
           - pp * L0(xyz(ix(k),iy(k),iz(k)-1),g,2)   &
           + p1 * L0(k,g,2)                          &
           ) / p3
    P2zy = ( p1m * L0(xyz(ix(k),iy(k),iz(k)+1),g,2)  &
           + p1p * L0(xyz(ix(k),iy(k),iz(k)-1),g,2)  &
           - p2  * L0(xyz(ix(k),iy(k),iz(k)),g,2)    &
           ) / p3
End if

! Set Transverse Leakage Moments
L(1) = 0.0
L(2) = ( p1xy/dely(iy(k))+p1xz/delz(iz(k)) ) / 12. ! Lx1
L(3) = ( p1yx/delx(ix(k))+p1yz/delz(iz(k)) ) / 12. ! Ly1
L(4) = ( p1zx/delx(ix(k))+p1zy/dely(iy(k)) ) / 12. ! Lz1
L(5) = ( p2xy/dely(iy(k))+p2xz/delz(iz(k)) ) / 20. ! Lx2
L(6) = ( p2yx/delx(ix(k))+p2yz/delz(iz(k)) ) / 20. ! Ly2
L(7) = ( p2zx/delx(ix(k))+p2zy/dely(iy(k)) ) / 20. ! Lz2

End Subroutine

Subroutine MatVec2(MulJin,MulMom,R2,P2,ji,Q) ! To Perform Matrix vector Multiplication
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Real(dp), Dimension(6,6),Intent(in) :: P2, R2
Real(dp), Dimension(6),Intent(in) :: ji
Real(dp), Dimension(7),Intent(in) :: Q
Real(dp), Dimension(6), Intent(out) :: MulJin, MulMom    
!Local Variables
Integer :: i, j, m, n, v, w
Real(dp) :: isum6,isum7
Real(dp), Dimension(6) :: Q_L

Q_L(:) = Q(1)

m = Size(R2,1)
v = Size(ji,1)
Do i= 1, m
    isum6 = 0.
    Do j = 1, v
        isum6 = isum6 + R2(i,j) * ji(j)
    End Do
    MulJin(i) = isum6
End Do

n = Size(P2,1)
w = Size(Q_L,1)
Do i= 1, n
    isum7 = 0.
    Do j = 1, w
        isum7 = isum7 + P2(i,j) * Q_L(j)
    End Do
    MulMom(i) = isum7
End Do

End Subroutine    

Subroutine MatVec4(MulJin,MulMom,R4,P4,ji,Q,L) ! To Perform Matrix vector Multiplication
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Real(dp), Dimension(6,6),Intent(in) :: R4
Real(dp), Dimension(6,7),Intent(in) :: P4
Real(dp), Dimension(6),Intent(in) :: ji
Real(dp), Dimension(7),Intent(in) :: Q, L
Real(dp), Dimension(6), Intent(out) :: MulJin, MulMom    
!Local Variables
Integer :: i, j, m, n, v, w
Real(dp) :: isum6,isum7
Real(dp), Dimension(7) :: Q_L

Q_L(:) = Q(:) - L(:) 

m = Size(R4,1)
v = Size(ji,1)
Do i= 1, m
    isum6 = 0.
    Do j = 1, v
        isum6 = isum6 + R4(i,j) * ji(j)
    End Do
    MulJin(i) = isum6
End Do

n = Size(P4,1)
w = Size(Q_L,1)
Do i= 1, n
    isum7 = 0.
    Do j = 1, w
        isum7 = isum7 + P4(i,j) * Q_L(j)
    End Do
    MulMom(i) = isum7
End Do

End Subroutine    

Subroutine Lxyz(L0,k,g,ng,nk,jo,ji) ! To Update Transverse Leakages for g Group and n Nod
            ! Flat Leakage Approximation   L = J(+) - J(-)
            ! J(+) = Jout - Jin  &  -J(-) = Jout - Jin  (Net Currents)
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk
Real(dp), Dimension(nk,ng,6),Intent(in) :: jo, ji
Real(dp), Dimension(nk,ng,3),Intent(out):: L0

! 1:x+, 2:x-, 3:y+, 4:y-, 5:z+, 6:z-
L0(k,g,1) = jo(k,g,1) - ji(k,g,1) & 
          + jo(k,g,2) - ji(k,g,2) ! Lx
L0(k,g,2) = jo(k,g,3) - ji(k,g,3) &
          + jo(k,g,4) - ji(k,g,4) ! Ly
L0(k,g,3) = jo(k,g,5) - ji(k,g,5) &
          + jo(k,g,6) - ji(k,g,6) ! Lz

End Subroutine

Subroutine Flux4(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,&
                             D,sigr,delx,dely,delz,ix,iy,iz,jo,ji,L0,Q,L) ! To Update Nod Averaged Flux & Flux Moments
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk, nxx, nyy, nzz
Real(dp), Dimension(nk,ng), Intent(in) :: D, sigr
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng,6),Intent(in) :: jo, ji
Real(dp), Dimension(nk,ng,7),Intent(in) :: Q
Real(dp), Dimension(nk,ng,3),Intent(in) :: L0
Real(dp), Dimension(nk,ng,7), Intent(in) :: L
Real(dp), Dimension(nk,ng), Intent(out) :: f0, fx1, fy1, fz1, fx2, fy2, fz2
! Local Variables
Real(dp) :: Tx, Ty, Tz

! Update Zeroth Flux (Nod Averaged Flux)
    Call Flux2(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,sigr,Q,L0)
if (f0(k,g) < 0.) f0(k,g) = 0.

! Set Parameters Tx, Ty & Tz   [ T = (J+) + (J-) ]
Tx = jo(k,g,1) - ji(k,g,1) - jo(k,g,2) + ji(k,g,2)
Ty = jo(k,g,3) - ji(k,g,3) - jo(k,g,4) + ji(k,g,4)
Tz = jo(k,g,5) - ji(k,g,5) - jo(k,g,6) + ji(k,g,6)
   
! Calculate Flux moments
fx1(k,g) = ( Q(k,g,2) - L(k,g,2) - 0.5*Tx/delx(ix(k))             &
           - 2.*(D(k,g)/delx(ix(k))**2)                       &
           *(jo(k,g,1) + ji(k,g,1) - jo(k,g,2) - ji(k,g,2)) ) &
           / sigr(k,g)

fy1(k,g) = ( Q(k,g,3) - L(k,g,3) - 0.5*Ty/dely(iy(k))             &
           - 2.*(D(k,g)/dely(iy(k))**2)                       &
           *(jo(k,g,3) + ji(k,g,3) - jo(k,g,4) - ji(k,g,4)) ) &
           / sigr(k,g)

fz1(k,g) = ( Q(k,g,4) - L(k,g,4) - 0.5*Tz/delz(iz(k))             &
           - 2.*(D(k,g)/delz(iz(k))**2)                       &
           *(jo(k,g,5) + ji(k,g,5) - jo(k,g,6) - ji(k,g,6)) ) &
           / sigr(k,g)

fx2(k,g) = ( Q(k,g,5) - L(k,g,5) - 0.5*L0(k,g,1)/delx(ix(k))      &
           - 6.*(D(k,g)/delx(ix(k))**2)                       &
           * (jo(k,g,1) + ji(k,g,1) + jo(k,g,2) + ji(k,g,2)   &
           - f0(k,g)) ) / sigr(k,g)

fy2(k,g) = ( Q(k,g,6) - L(k,g,6) - 0.5*L0(k,g,2)/dely(iy(k))      &
           - 6.*(D(k,g)/dely(iy(k))**2)                       &
           * (jo(k,g,3) + ji(k,g,3) + jo(k,g,4) + ji(k,g,4)   &
           - f0(k,g)) ) / sigr(k,g)

fz2(k,g) = ( Q(k,g,7) - L(k,g,7) - 0.5*L0(k,g,3)/delz(iz(k))      &
           - 6.*(D(k,g)/delz(iz(k))**2)                       &
           * (jo(k,g,5) + ji(k,g,5) + jo(k,g,6) + ji(k,g,6)   &
           - f0(k,g)) ) / sigr(k,g)

End Subroutine

Subroutine Flux2(f0,fx1,fy1,fz1,fx2,fy2,fz2,k,g,ng,nk,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,sigr,Q,L0) ! To Update Nod Averaged Flux 
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: g, k, ng, nk, nxx, nyy, nzz
Real(dp), Dimension(nk,ng), Intent(in) :: sigr
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng,7),Intent(in) :: Q
Real(dp), Dimension(nk,ng,3),Intent(in) :: L0
Real(dp), Dimension(nk,ng), Intent(out) :: f0, fx1, fy1, fz1, fx2, fy2, fz2

! Calculate Zeroth Flux
f0(k,g)  = ( Q(k,g,1)             &
         - L0(k,g,1)/delx(ix(k))   &
         - L0(k,g,2)/dely(iy(k))   &
         - L0(k,g,3)/delz(iz(k)) ) &
         / sigr(k,g)
fx1(k,g) = 0.0
fy1(k,g) = 0.0
fz1(k,g) = 0.0
fx2(k,g) = 0.0
fy2(k,g) = 0.0
fz2(k,g) = 0.0

End Subroutine

Subroutine RelE(newF,oldF,rel,nk) ! To Calculate Max Relative Error for FS
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk
Real(dp), Dimension(nk),Intent(in) :: newF, oldF
Real(dp), Intent(out) :: rel
!Local Variables
Real(dp) :: error
Integer :: k

rel = 0.
Do k= 1, nk
    if (ABS(newF(k)) > 1.e-10_dp) Then
        error = ABS(newF(k) - oldF(k)) / ABS(newF(k))
        if (error > rel) rel = error
    End if
End Do

End Subroutine

Subroutine RelEg(newF,oldF,rel,nk,ng) ! To Calculate Max Relative error for Flux
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk     ! Number of Groups
Real(dp), Dimension(nk,ng),Intent(in) :: newF, oldF
Real(dp), Intent(out) :: rel
!Local Variables
Real(dp) :: error
Integer :: g, k

rel = 0.
Do k= 1, nk
    Do g= 1, ng
        if (ABS(newF(k,g)) > 1.d-10) Then
            error = ABS(newF(k,g) - oldF(k,g)) / ABS(newF(k,g))
            if (error > rel) rel = error
        End if
    End Do
End Do

End Subroutine

Subroutine MultF(Keff,ng,nk,siga,nu_sigf,f0,jo,ji,nxx,nyy,nzz,ix,iy,iz,&
                 delx,dely,delz,x_smax,x_smin,y_smax,y_smin)     ! To Calculate Keff for Fixed Source Problem
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nxx, nyy, nzz
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk),  Intent(in) :: ix, iy, iz
Integer, Dimension(nxx), Intent(in) :: x_smax, x_smin
Integer, Dimension(nyy), Intent(in) :: y_smax, y_smin 
Real(dp), Dimension(nk,ng), Intent(in) :: siga, nu_sigf
Real(dp), Dimension(nk,ng), Intent(in) :: f0
Real(dp), Dimension(nk,ng,6),Intent(in) :: jo, ji
Real(dp), Intent(out) :: Keff
! Local Variables
Integer :: g, k
Real(dp) :: leak, absp, fiss
!! Jot Nodals' outgoing currents  (X+, X-, Y+, Y-, Z+, Z-)
!! Jin Nodals' ingoing currents   (X+, X-, Y+, Y-, Z+, Z-)
leak = 0.0
absp = 0.0
fiss = 0.0
Do g = 1, ng
    Do k = 1, nk
        !! Get leakages
        if (ix(k) == y_smax(iy(k))) leak = leak+(jo(k,g,1)-ji(k,g,1))*dely(iy(k))*delz(iz(k))
        if (ix(k) == y_smin(iy(k))) leak = leak+(jo(k,g,2)-ji(k,g,2))*dely(iy(k))*delz(iz(k))
        if (iy(k) == x_smax(ix(k))) leak = leak+(jo(k,g,3)-ji(k,g,3))*delx(ix(k))*delz(iz(k))
        if (iy(k) == x_smin(ix(k))) leak = leak+(jo(k,g,4)-ji(k,g,4))*delx(ix(k))*delz(iz(k))
        if (iz(k) == nzz) leak = leak+(jo(k,g,5)-ji(k,g,5))*delx(ix(k))*dely(iy(k))
        if (iz(k) == 1)   leak = leak+(jo(k,g,6)-ji(k,g,6))*delx(ix(k))*dely(iy(k))
        
        absp = absp + siga(k,g) * f0(k,g) * delx(ix(k)) * dely(iy(k)) * delz(iz(k))
        fiss = fiss + nu_sigf(k,g) * f0(k,g) * delx(ix(k)) * dely(iy(k)) * delz(iz(k))

    End Do
End Do

    Keff = fiss / (leak + absp)

End Subroutine

Subroutine PowDis(p,f0,sigf,delv,ng,nk,mode) ! To Calculate Power Distribution
Implicit None
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk
Real(dp), Dimension(nk), Intent(in) :: delv
Real(dp), Dimension(nk,ng), Intent(in) :: sigf, f0
Real(dp), Dimension(nk), Intent(out) :: p        ! Power
Character(Len=100), intent(in) :: mode
! Local Variables
Integer :: g, k
Integer, Parameter :: Ounit = 100   !output
Real(dp) :: pow, tpow

Open (Unit=ounit, File='app/Output/NEM.out')
p = 0.0
Do g= 1, ng
    Do k= 1, nk
        pow = sigf(k,g)*f0(k,g)*delv(k)
        if (pow < 0.) pow = 0.
        p(k) = p(k)+pow
    End Do
End Do

! Normalize to 1._dp
tpow = 0.
Do k = 1, nk
    tpow = tpow + p(k)
End Do

if (tpow <= 0 .AND. mode /= 'Fixed Source') Then
   Write(ounit, *) '   ERROR: TOTAL NODES POWER IS ZERO OR LESS'
   Write(ounit, *) '   STOP IN SUBROUTINE POWDIS'
   Write(*, *) '   ERROR: TOTAL NODES POWER IS ZERO OR LESS'
   Write(*, *) '   STOP IN SUBROUTINE POWDIS'
   Stop
End if

Do k = 1, nk
    p(k) = p(k) / tpow
End Do

End Subroutine

Subroutine AsmPow(nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,p)   !   To Print Radially Averaged Power Distribution
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk, nx, ny, nxx, nyy, nzz
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz, p
! Local Variables
Real*4, Dimension(100) :: sdelx
Real*4, Dimension(100) :: sdely
Real*4 :: sx, sy
Real(dp) :: som, vsom, totp, fmax
Real(dp), Dimension(nx,ny) :: fasm
Real(dp), Dimension(nxx,nyy) :: fnode
Real(dp), Dimension(nxx,nyy,nzz) :: fx
Integer, Parameter :: xm = 12, Ounit = 100
Integer :: i, j, k, n, lx, ly, ip, ipr, xs, xf, ys, yf, nfuel, xmax, ymax, m
Character(Len=6), Dimension(nx,ny) :: cpow

fx = 0._dp
Do n = 1, nk
    fx(ix(n),iy(n),iz(n)) = p(n)
End Do

!Calculate Axially Averaged Node-Wise Distribution
fnode = 0._dp
Do j = 1, nyy
    Do i = y_smin(j), y_smax(j)
        som = 0._dp
        vsom = 0._dp
        Do k = 1, nzz
            som = som + fx(i,j,k)*delz(k)
            vsom = vsom + delz(k)
        End Do
        fnode(i,j)= som/vsom
    End Do
End Do

!Calculate Assembly Power
nfuel = 0
totp  = 0._dp
ys = 1
yf = 0
Do j= 1, ny
    yf = yf + ydiv(j)
    xf = 0
    xs = 1
    Do i= 1, nx
        xf = xf + xdiv(i)
        som = 0._dp
        vsom = 0._dp
        Do ly= ys, yf
            Do lx= xs, xf
                som = som + fnode(lx,ly)*delx(lx)*dely(ly)
                vsom = vsom + delx(lx)*dely(ly)
            End Do
        End Do
        fasm(i,j) = som / vsom
        xs = xs + xdiv(i)
        if (fasm(i,j) > 0._dp) nfuel = nfuel + 1
        if (fasm(i,j) > 0._dp) totp  = totp + fasm(i,j)
    End Do
    ys = ys + ydiv(j)
End Do

! Normalize Assembly Power to 1.0
xmax = 1; ymax = 1
fmax = 0._dp
Do j = 1, ny
    Do i = 1, nx
        if (totp > 0.) fasm(i,j) = Real(nfuel) / totp * fasm(i,j)
        if (fasm(i,j) > fmax) Then     ! Get max position
            xmax = i
            ymax = j
            fmax = fasm(i,j)
        End if
! If Power = 0 ==> Blank Spaces
   !   if ((fasm(i,j) - 0.) < 1.e-5_dp) Then
            ! cpow(i,j) = '     '
        ! Else
            Write (cpow(i,j),'(F6.3)') fasm(i,j)
            cpow(i,j) = TRIM(cpow(i,j))
        ! End if
    End Do
End Do

! Print Assembly Power Distribution
Write(ounit,*)
Write(ounit,*)
Write(ounit,*) '    Radial Power Distribution'
Write(ounit,*) '  =============================='
Write(*,*)
Write(*,*)
Write(*,*) '    Radial Power Distribution'
Write(*,*) '  =============================='
Open (unit=10, File='app/Output/RadialPower.out')
ip = nx/xm
ipr = MOD(nx,xm) - 1
xs = 1; xf = xm
sx = 0.0
sy = 0.0

Do m = 1,xm
    sdelx(m) = sx+delx(m)*xdiv(m)
    sx = sdelx(m)
End Do
Do m = xm, 1, -1
    sdely(m) = sy+dely(m)*ydiv(m)
    sy = sdely(m)
End Do

Do k = 1, ip
    Write(ounit,'(4X,100I8)') (i, i = xs, xf)
    Write(*,'(4X,100I8)') (i, i = xs, xf)
    Write(10,'(F9.3,100F9.3)') 0.000, ( sdelx(i) , i = xs, xf)
    Do j= ny, 1, -1
        Write(ounit,'(2X,I4,100A8)') j, (cpow(i,j), i=xs, xf)
        Write(*,'(2X,I4,100A8)') j, (cpow(i,j), i=xs, xf)
        Write(10,'(2X,F9.3,2X,100A8)') sdely(j), (cpow(i,j), i=xs, xf)
    End Do
    Write(ounit,*)
    xs = xs + xm
    xf = xf + xm
End Do

Write(ounit,'(4X,100I8)') (i, i = xs, xs+ipr)
Write(*,'(4X,100I8)') (i, i = xs, xs+ipr)
Write(10,'(F9.3,100F9.3)') 0.000, (sdelx(i), i = xs, xs+ipr)

if (xs+ipr > xs) Then
    Do j= ny, 1, -1
        Write(ounit,'(2X,I4,100A8)') j, (cpow(i,j), i=xs, xs+ipr)
        Write(*,'(2X,I4,100A8)') j, (cpow(i,j), i=xs, xs+ipr)
        Write(10,'(2X,F9.3,2X,100A8)') sdely(j), (cpow(i,j), i=xs, xs+ipr)
    End Do
End if
close(10)
Write(ounit,*)
Write(ounit,*) '  MAX POS.       Maximum Value'
Write(ounit,1101) ymax, xmax, fasm(xmax, ymax)
Write(*,*)
Write(*,*) '  MAX POS.       Maximum Value'
Write(*,1101) ymax, xmax, fasm(xmax, ymax)

1101 Format(2X, '(' , I3, ',', I3,')', F15.3)
End Subroutine

Subroutine AxiPow(nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,p)    !   To print Axially Averaged Assembly-Wise Power Distribution
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk, nz, nxx, nyy, nzz
Integer, Dimension(nz), Intent(in) :: zdiv
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin
Real(dp), Dimension(nk), Intent(in) :: delv
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz, p
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
! Local Variables
Real(dp) :: coreh       ! Core Height
Real(dp) :: som, vsom, totp, fmax
Real(dp), Dimension(nz) :: faxi
Real(dp), Dimension(nxx,nyy,nzz) :: fx
Integer, Parameter :: Ounit = 100
Integer :: i, j, k, n, ztot, lz, nfuel, amax

fx = 0._dp
Do n = 1, nk
    fx(ix(n),iy(n),iz(n)) = p(n)
End Do

! Calculate Axial Power
nfuel = 0
totp  = 0._dp
ztot = 0
Do k= 1, nz
    som = 0._dp
    vsom = 0._dp
    Do lz= 1, zdiv(k)
        ztot = ztot + 1
        Do j = 1, nyy
            Do i = y_smin(j), y_smax(j)
                som = som + fx(i,j,ztot)
                vsom = vsom + delv(xyz(i,j,ztot))
            End Do
        End Do
    End Do
    faxi(k) = som/vsom
    if (faxi(k) > 0._dp) nfuel = nfuel + 1
    if (faxi(k) > 0._dp) totp  = totp + faxi(k)
End Do

! Normalize Axial Power to 1.0
fmax = 0._dp
amax = 1
Do k = 1, nz
    faxi(k) = Real(nfuel) / totp * faxi(k)
    if (faxi(k) > fmax) Then
        amax = k   ! Get Max Position
        fmax = faxi(k)
    End if
End Do

! Calculate Core Height
coreh = 0._dp
Do k = 1, nzz
    coreh = coreh + delz(k)
End Do

! Print Axial power distribution
Write(ounit,*)
Write(ounit,*)
Write(ounit,*) '    Axial Power Density Distribution'
Write(ounit,*) '  ===================================='
Write(ounit,*)
Write(ounit,*) '    Plane Number        Power      Height'
Write(ounit,*) '   -----------------------------------------'
Write(*,*)
Write(*,*)
Write(*,*) '    Axial Power Density Distribution'
Write(*,*) '  ===================================='
Write(*,*)
Write(*,*) '    Plane Number        Power      Height'
Write(*,*) '   -----------------------------------------'
Open (unit=20, File='app/Output/AxialPower.out')
som = 0.
ztot = nzz
        Write(20,*)  0, 100

Do k= nz, 1, -1
    if (k == nz) Then
        Write(ounit,'(2X,I8,A7,F13.3, F12.2)') k, ' (Top)', faxi(k), coreh-som
        Write(*,'(2X,I8,A7,F13.3, F12.2)') k, ' (Top)', faxi(k), coreh-som
        Write(20,'(2X, F12.2, F10.3)')  coreh-som, faxi(k)
    Else if (k == 1) Then
        Write(ounit,'(2X,I8,A10,F10.3, F12.2)') k, ' (Bottom)', faxi(k), coreh-som
        Write(*,'(2X,I8,A10,F10.3, F12.2)') k, ' (Bottom)', faxi(k), coreh-som
        Write(20,'(2X, F12.2, F10.3)')  coreh-som, faxi(k)
    Else
        Write(ounit,'(2X,I8,F20.3, F12.2)') k, faxi(k), coreh-som
        Write(*,'(2X,I8,F20.3, F12.2)') k, faxi(k), coreh-som
        Write(20,'(2X, F12.2, F10.3)')  coreh-som, faxi(k)
    End if
    Do lz = 1, zdiv(k)
        som = som + delz(ztot)
        ztot = ztot - 1
    End Do
End Do
close(20)
Write(ounit,*)
Write(ounit,*) '  MAX POS.       Maximum Value'
Write(ounit,1102)  amax, faxi(amax)
Write(*,*)
Write(*,*) '  MAX POS.       Maximum Value'
Write(*,1102)  amax, faxi(amax)

1102 Format(4X, '(' , I3, ')', F18.3)

End Subroutine
Subroutine AxiFlux(ng,nk,nz,nxx,nyy,nzz,ix,iy,iz,xyz,delz,delv,zdiv,y_smax,y_smin,p)    !   To print Axially Averaged Assembly-Wise Power Distribution
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nz, nxx, nyy, nzz
Integer, Dimension(nz), Intent(in) :: zdiv
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin
Real(dp), Dimension(nk), Intent(in) :: delv
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng), Intent(in) :: p
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
! Local Variables
Real(dp) :: coreh       ! Core Height
Real(dp) :: som, vsom, totp, fmax
Real(dp), Dimension(nz,ng) :: faxi
Real(dp), Dimension(ng) :: amax
Real(dp), Dimension(nxx,nyy,nzz,ng) :: fx
Integer, Parameter :: Ounit = 100
Integer :: i, j, k, n, f, g, ztot, lz, nfuel
Character(Len=20), Dimension(ng) :: Filename ! Name of the Complete File

fx = 0._dp
Do g = 1, ng
    Do n = 1, nk
        fx(ix(n),iy(n),iz(n),g) = p(n,g)
    End Do
End Do

! Calculate Axial Power
nfuel = 0
totp  = 0._dp
ztot = 0
Do g = 1, ng
    Do k= 1, nz
        som = 0._dp
        vsom = 0._dp
        Do lz= 1, zdiv(k)
            ztot = ztot + 1
            Do j = 1, nyy
                Do i = y_smin(j), y_smax(j)
                    som = som + fx(i,j,ztot,g)
                    vsom = vsom + delv(xyz(i,j,ztot))
                End Do
            End Do
        End Do
        faxi(k,g) = som/vsom
        if (faxi(k,g) > 0._dp) nfuel = nfuel + 1
        if (faxi(k,g) > 0._dp) totp  = totp + faxi(k,g)
    End Do
End Do

! Normalize Axial Power to 1.0
fmax = 0._dp
amax = 1
Do g = 1, ng
    Do k = 1, nz
        faxi(k,g) = Real(nfuel) / totp * faxi(k,g)
        if (faxi(k,g) > fmax) Then
            amax(g) = k   ! Get Max Position
            fmax = faxi(k,g)
        End if
    End Do
End Do

! Calculate Core Height
coreh = 0._dp
Do k = 1, nzz
    coreh = coreh + delz(k)
End Do

Do f=1,ng ! Loop through all Files
    Write(Filename(f),'(A17,I2)') 'app\Output\AxiFluxGr',f
End Do

Do g = 1, ng
    Write(ounit,'(A,I3)') '    Group : ', g
    Write(*,'(A,I3)')     '    Group : ', g
    ! Print Axial Flux Distribution
    Write(ounit,*)
    Write(ounit,*)
    Write(ounit,*) '    Axial Flux Density Distribution'
    Write(ounit,*) '  ===================================='
    Write(ounit,*)
    Write(ounit,*) '    Plane Number        Flux      Height'
    Write(ounit,*) '   -----------------------------------------'
    Write(*,*)
    Write(*,*)
    Write(*,*) '    Axial Flux Density Distribution'
    Write(*,*) '  ===================================='
    Write(*,*)
    Write(*,*) '    Plane Number        Flux      Height'
    Write(*,*) '   -----------------------------------------'
    Open (g,File=Filename(g))
    som = 0.
    ztot = nzz
    Write(Filename(g),*)  0, 100
    Do k= nz, 1, -1
        if (k == nz) Then
            Write(ounit,'(2X,I8,A7,F13.3, F12.2)') k, ' (Top)', faxi(k,g), coreh-som
            Write(*,'(2X,I8,A7,F13.3, F12.2)') k, ' (Top)', faxi(k,g), coreh-som
            Write(Filename(g),'(2X, F12.2, F10.3)')  coreh-som, faxi(k,g)
        Else if (k == 1) Then
            Write(ounit,'(2X,I8,A10,F10.3, F12.2)') k, ' (Bottom)', faxi(k,g), coreh-som
            Write(*,'(2X,I8,A10,F10.3, F12.2)') k, ' (Bottom)', faxi(k,g), coreh-som
            Write(Filename(g),'(2X, F12.2, F10.3)')  coreh-som, faxi(k,g)
        Else
            Write(ounit,'(2X,I8,F20.3, F12.2)') k, faxi(k,g), coreh-som
            Write(*,'(2X,I8,F20.3, F12.2)') k, faxi(k,g), coreh-som
            Write(Filename(g),'(2X, F12.2, F10.3)')  coreh-som, faxi(k,g)
        End if
        Do lz = 1, zdiv(k)
            som = som + delz(ztot)
            ztot = ztot - 1
        End Do
    End Do
End Do

close(20)
Do g = 1, ng
    Write(ounit,'(A,I3)') '    Group : ', g
    Write(*,'(A,I3)')     '    Group : ', g
    Write(ounit,*)
    Write(ounit,*) '  MAX POS.       Maximum Value'
    Write(ounit,1102)  amax(g), faxi(amax(g),g)
    Write(*,*)
    Write(*,*) '  MAX POS.       Maximum Value'
    Write(*,1102)  amax(g), faxi(amax(g),g)
End Do

1102 Format(4X, '(' , I3, ')', F18.3)

End Subroutine

Subroutine AsmFlux(ng,nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,p,norm)   !   To Print Radially Averaged Flux Distribution
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nx, ny, nxx, nyy, nzz
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng), Intent(in) :: p
Real(dp), Intent(in) :: norm
! Local Variables
Real(dp) :: som, vsom
Real*4, Dimension(100) :: sdelx
Real*4, Dimension(100) :: sdely
Real*4 :: sx, sy
Real(dp), Dimension(ng) :: totf
Real(dp), Dimension(nx,ny,ng) :: fasm
Real(dp), Dimension(nxx,nyy,ng) :: fnode
Real(dp), Dimension(nxx,nyy,nzz,ng) :: fx
Integer, Parameter :: xm = 12, Ounit = 100
Integer :: i, j, k, n, g, lx, ly, ip, ipr, xs, xf, ys, yf, negF, m, f
Character(Len=10), Dimension(nx,ny) :: cflx
Character(Len=20), Dimension(ng) :: Filename ! Name of the Complete File

fx = 0._dp
Do g = 1, ng
    Do n = 1, nk
        fx(ix(n),iy(n),iz(n),g) = p(n,g)
    End Do
End Do

!Calculate Axially Averaged Node-Wise Distribution
fnode = 0._dp
Do g = 1, ng
    Do j = 1, nyy
        Do i = y_smin(j), y_smax(j)
            som = 0._dp
            vsom = 0._dp
            Do k = 1, nzz
                som = som + fx(i,j,k,g)*delx(i)*dely(j)*delz(k)
                vsom = vsom + delx(i)*dely(j)*delz(k)
            End Do
            fnode(i,j,g)= som/vsom
        End Do
    End Do
End Do

!Calculate Radial Flux (Assembly Wise)
negF = 0
Do g = 1, ng
    totf(g)  = 0._dp
    ys = 1
    yf = 0
    Do j= 1, ny
        yf = yf + ydiv(j)
        xf = 0
        xs = 1
        Do i= 1, nx
            xf = xf + xdiv(i)
            som = 0._dp
            vsom = 0._dp
            Do ly= ys, yf
                Do lx= xs, xf
                    som = som + fnode(lx,ly,g)*delx(lx)*dely(ly)
                    vsom = vsom + delx(lx)*dely(ly)
                End Do
            End Do
            fasm(i,j,g) = som / vsom
            xs = xs + xdiv(i)
            if (fasm(i,j,g) > 0._dp) totf(g) = totf(g) + fasm(i,j,g)
            if (fasm(i,j,g) < 0._dp) negF = 1   ! Check if there is Negative Flux
        End Do
        ys = ys + ydiv(j)
    End Do
End Do

! Normalize Flux to Norm
Do g = 1, ng
    Do j = 1, ny
        Do i = 1, nx
            fasm(i,j,g) = norm / totf(g) * fasm(i,j,g) * norm
        End Do
    End Do
End Do

! Print Assembly Flux Distribution

Write(ounit,*)
Write(*,*)
if (negf > 0) Then
    Write(ounit,*) '    ....Warning: Negative Flux Encountered....'
    Write(*,*)     '    ....Warning: Negative Flux Encountered....'
End if

Write(ounit,*) '    Radial Flux Distribution'
Write(ounit,*) '  =============================='
Write(*,*)     '    Radial Flux Distribution'
Write(*,*)     '  =============================='

ip = nx/xm
ipr = Mod(nx,xm) - 1
sx = 0.0
sy = 0.0

Do m = 1, xm
    sdelx(m) = sx+delx(m)*xdiv(m)
    sx = sdelx(m)
End Do
Do m = xm, 1, -1
    sdely(m) = sy+dely(m)*ydiv(m)
    sy = sdely(m)
End Do

Do f=1,ng ! Loop through all Files
    Write(Filename(f),'(A17,I2)') 'app\Output\FluxGr',f
End Do

Do g = 1, ng
    Write(ounit,'(A,I3)') '    Group : ', g
    Write(*,'(A,I3)')     '    Group : ', g
    ! If Flux = 0 ==> Blank Spaces
    Do j = 1, ny
        Do i = 1, nx
            ! if ((fasm(i,j,g) - 0.) < 1.e-5_dp) Then
                ! cflx(i,j) = '         '
            ! Else
                Write (cflx(i,j),'(ES10.3)') fasm(i,j,g)
                cflx(i,j) = TRIM(ADJUSTL(cflx(i,j)))
            ! End if
        End Do
    End Do

    xs = 1; xf = xm
    ! Do f=1,ng
        Open (g,File=Filename(g))
        Do k = 1, ip
            Write(ounit,'(2X,100I11)') (i, i = xs, xf)
            Write(*,'(2X,100I11)') (i, i = xs, xf)
            Write(g,'(F9.3,100F9.3)') 0.000, ( sdelx(i) , i = xs, xf)

            Do j= ny, 1, -1
                Write(ounit,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xf)
                Write(*,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xf)
                Write(g,'(2X,F9.3,2X,100A11)') sdely(j), (cflx(i,j), i=xs, xf)
            End Do
            Write(ounit,*)
            Write(*,*)
            xs = xs + xm
            xf = xf + xm
        End Do

    Write(ounit,'(3X,100I11)') (i, i = xs, xs+ipr)
    Write(*,'(3X,100I11)') (i, i = xs, xs+ipr)
    Write(g,'(F9.3,100F9.3)') 0.000, ( sdelx(i), i = xs, xs+ipr)
    if (xs+ipr > xs) Then
        Do j= ny, 1, -1
            Write(ounit,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xs+ipr)
            Write(*,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xs+ipr)
            Write(g,'(2X,F9.3,2X,100A11)') sdely(j), (cflx(i,j), i=xs, xs+ipr)
        End Do
    End if
    Write(ounit,*)
    Write(*,*)
    Close(f)
End Do

1101 Format(2X, '(' , I3, ',', I3,')', F15.3)

End Subroutine

Subroutine AsmFlux_FxS(ng,nk,nx,ny,nxx,nyy,nzz,ix,iy,iz,delx,dely,delz,xdiv,ydiv,y_smax,y_smin,p)   !   To Print Radially Averaged Flux Distribution for Fixed Sources
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: ng, nk, nx, ny, nxx, nyy, nzz
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nyy), Intent(out) :: y_smax, y_smin
Real(dp), Dimension(nxx), Intent(in) :: delx
Real(dp), Dimension(nyy), Intent(in) :: dely
Real(dp), Dimension(nzz), Intent(in) :: delz
Real(dp), Dimension(nk), Intent(in) :: ix, iy, iz
Real(dp), Dimension(nk,ng), Intent(in) :: p
! Local Variables
Real(dp) :: som, vsom
Real(dp), Dimension(ng) :: totf
Real(dp), Dimension(nx,ny,ng) :: fasm
Real(dp), Dimension(nxx,nyy,ng) :: fnode
Real(dp), Dimension(nxx,nyy,nzz,ng) :: fx
Integer, Parameter :: xm = 12, Ounit = 100
Integer :: i, j, k, n, g, lx, ly, ip, ipr, xs, xf, ys, yf, negF 
Character(Len=10), Dimension(nx,ny) :: cflx

fx = 0._dp
Do g = 1, ng
    Do n = 1, nk
        fx(ix(n),iy(n),iz(n),g) = p(n,g)
    End Do
End Do

!Calculate Axially Averaged Node-Wise Distribution
fnode = 0._dp
Do g = 1, ng
    Do j = 1, nyy
        Do i = y_smin(j), y_smax(j)
            som = 0._dp
            vsom = 0._dp
            Do k = 1, nzz
                som = som + fx(i,j,k,g)*delx(i)*dely(j)*delz(k)
                vsom = vsom + delx(i)*dely(j)*delz(k)
            End Do
            fnode(i,j,g)= som/vsom
        End Do
    End Do
End Do

!Calculate Radial Flux (Assembly Wise)
negF = 0
Do g = 1, ng
    totf(g)  = 0._dp
    ys = 1
    yf = 0
    Do j= 1, ny
        yf = yf + ydiv(j)
        xf = 0
        xs = 1
        Do i= 1, nx
            xf = xf + xdiv(i)
            som = 0._dp
            vsom = 0._dp
            Do ly= ys, yf
                Do lx= xs, xf
                    som = som + fnode(lx,ly,g)*delx(lx)*dely(ly)
                    vsom = vsom + delx(lx)*dely(ly)
                End Do
            End Do
            fasm(i,j,g) = som / vsom
            xs = xs + xdiv(i)
            if (fasm(i,j,g) > 0._dp) totf(g) = totf(g) + fasm(i,j,g)
            if (fasm(i,j,g) < 0._dp) negF = 1   ! Check if there is Negative Flux
        End Do
        ys = ys + ydiv(j)
    End Do
End Do

! Print Assembly Flux Distribution
Write(ounit,*)
if (negf > 0) Write(ounit,*) '    ....Warning: Negative Flux Encountered....'
Write(ounit,*) '    Radial Flux Distribution'
Write(ounit,*) '  =============================='

ip = nx/xm
ipr = Mod(nx,xm) - 1
Do g = 1, ng
    Write(ounit,'(A,I3)') '    Group : ', g
    ! If Flux = 0 ==> Blank Spaces
    Do j = 1, ny
        Do i = 1, nx
            if ((fasm(i,j,g) - 0.) < 1.e-5_dp) THEN
                cflx(i,j) = '         '
            Else
                Write (cflx(i,j),'(ES10.3)') fasm(i,j,g)
                cflx(i,j) = TRIM(ADJUSTL(cflx(i,j)))
            End if
        End Do
    End Do
    
    xs = 1; xf = xm
    Do k = 1, ip
        Write(ounit,'(2X,100I11)') (i, i = xs, xf)
        Do j= ny, 1, -1
            Write(ounit,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xf)
        End Do
        Write(ounit,*)
        xs = xs + xm
        xf = xf + xm
    End Do

    Write(ounit,'(3X,100I11)') (i, i = xs, xs+ipr)
    if (xs+ipr > xs) Then
        Do j= ny, 1, -1
            Write(ounit,'(2X,I4,2X,100A11)') j, (cflx(i,j), i=xs, xs+ipr)
        End Do
    End if
    Write(ounit,*)
End Do

1101 Format(2X, '(' , I3, ',', I3,')', F15.3)

End Subroutine

Subroutine ExSrc(eSrc,nk,ng,nx,ny,nz,nxx,nyy,nzz,nS,dS,spS,&
                 xyz,xdiv,ydiv,zdiv,xpos,ypos,zpos,npox,npor) !   To Read Extra Sources if any
implicit none
Integer, Parameter :: dp = SELECTED_REAL_KIND(10, 15)
Integer, Intent(in) :: nk, ng, nx, ny, nz, nxx, nyy, nzz, npox, npor
Integer, Dimension(nx), Intent(in) :: xdiv
Integer, Dimension(ny), Intent(in) :: ydiv
Integer, Dimension(nz), Intent(in) :: zdiv
Real(dp), Dimension(nxx,nyy,nzz), Intent(in) :: xyz
Integer, Intent(in) :: nS
Real(dp), Dimension(nS), Intent(in) :: dS
Real(dp), Dimension(nS,ng), Intent(in) :: spS
Integer, Dimension(nS,npox), Intent(in) :: zpos
Integer, Dimension(nS,npor), Intent(in) :: xpos, ypos
Real(dp), Dimension(nk,ng), Intent(out) :: eSrc
! Local Variables
Character(Len=1), Dimension(nx,ny) :: posS         ! Source position
! Character(Len=2), Dimension(nxx, nyy) :: mmap
Integer, Parameter :: xm = 36, Ounit = 100
Integer :: i, j, k, g, h, n, xt, yt, zt, it, jt, kt, r, z
Real(dp) :: som

Open (Unit=Ounit, File='app/Output/NEM.out') 
Write(Ounit,*)
Write(Ounit,*)
Write(Ounit,*) '           >>>>> Reading Extra Sources <<<<<'
Write(Ounit,*) '           -------------------------------'
eSrc = 0._dp
Do n = 1, nS
    if (dS(n) <= 0.0) Then
        Write(ounit,*) '  Error: Source Density Shall Be Greater Than Zero'
        Stop
    End if

    ! Is Total Spectrum = 1.0?
    som = 0._dp
    Do g = 1, ng
        som = som + spS(n,g)
    End Do
    ! Check Total Spectrum
    if (ABS(som - 1._dp) > 1.e-5_dp) Then
        Write(ounit,*) 'Total Source Spectrum Is Not Equal To 1.0'
        Stop
    End if

    ! Write Output
    Write(Ounit,'(A12,I3)') '     Source ', n
    Write(Ounit,*)         '-----------------'
    Write(Ounit,'(A20,ES10.3, A11)') '  Source Density  : ', dS(n), '  n/(m^3*s)'
    Write(Ounit,'(A19,100F6.2)') '  Source Spectrum : ', (spS(n,g), g = 1, ng)
    Write(Ounit,*) ' Source Position '
    ! Read Source Position
! v = size(zpos,1)
! w = size(xpos,1)
    Do z = 1, npox
            if (zpos(n,z) < 1) Exit
            if (zpos(n,z) > nz) Then
                Write(Ounit,* ) '  Error: Wrong Extra Sources Position (ZPOS)'
                Write(Ounit, 2033) zpos(n,z)
                Stop
            End if
            posS = '0'
            Do r = 1, npor
                if (xpos(n,r) < 1 .OR. ypos(n,r) < 1) Exit
                if (xpos(n,r) > nx) Then
                    Write(ounit,* ) '  Error: Wrong Extra Sources Position (XPos)'
                    Write(ounit, 2033) xpos(n,r), ypos(n,r)
                    Stop
                End if
                if (ypos(n,r) > ny) Then
                    Write(ounit,* ) '  Error: Wrong Extra Sources Position (YPos)'
                    Write(ounit, 2033) xpos(n,r), ypos(n,r)
                    Stop
                End if
                posS(xpos(n,r),ypos(n,r)) = 'X'
                zt = 0
                kt = 1
                Do k = 1, zpos(n,z)
                    if (k > 1) kt = zt + 1
                    zt = zt + zdiv(k)
                End Do
                yt = 0
                jt = 1
                Do j = 1, ypos(n,r)
                    if (j > 1) jt = yt + 1
                    yt = yt + ydiv(j)
                End Do
                xt = 0
                it = 1
                Do i = 1, xpos(n,r)
                    if (i > 1) it = xt + 1
                    xt = xt + xdiv(i)
                End Do
                Do k = kt, zt
                    Do j = jt, yt
                        Do i = it, xt
                            Do h = 1, ng
                                eSrc(xyz(i,j,k),h) = eSrc(xyz(i,j,k),h) + dS(n) * spS(n,h)
                            End Do
                        End Do
                    End Do
                End Do
            End Do
            Write(Ounit,'(A18,I3)') '   Plane Number : ', zpos(n,z)
            Write(Ounit,'(7X,100I3)') (i, i = 1, nx)
            Do j = ny, 1, -1
                Write(Ounit,'(4X,I3, 100A3 )') j, (posS(i,j), i=1, nx)
            End Do
            Write(Ounit,*)
        End Do
    End Do

2033 Format(2X, I3, I3)

End Subroutine

Subroutine timestamp()
!      ------------------------------------------------------------------------
!      TIMESTAMP prints the current YMDHMS date as a time stamp.
!      Example:
!      31 May 2001   9:45:54.872 AM
!      Licensing:
!      This code is distributed under the GNU LGPL license.
!      Modified:
!      18 May 2013
!      Author:
!      John Burkardt
!      Parameters:
!      None
!      ------------------------------------------------------------------------
implicit none
Integer, Parameter ::  Ounit = 100
Character(len=8) :: ampm
Integer(kind=4) :: d
Integer(kind=4) :: h
Integer(kind=4) :: m
Integer(kind=4) :: mm
Character(len=9), Parameter, Dimension(12) :: month = (/ &
       'January  ', 'February ', 'March    ', 'April    ', &
       'May      ', 'June     ', 'July     ', 'August   ', &
       'September', 'October  ', 'November ', 'December ' /)
Integer(kind=4) :: n
Integer(kind=4) :: s
Integer(kind=4) :: values(8)
Integer(kind=4) :: y

    call date_and_time (values = values)
    y = values(1)
    m = values(2)
    d = values(3)
    h = values(5)
    n = values(6)
    s = values(7)
    mm = values(8)
    if (h < 12) Then
       ampm = 'AM'
    Else if (h == 12) Then
        if (n == 0 .and. s == 0) Then
            ampm = 'Noon'
        Else
            ampm = 'PM'
        End if
    Else
        h = h - 12
        if ( h < 12 ) Then
            ampm = 'PM'
        Else if ( h == 12 ) Then
            if (n == 0 .And. s == 0) Then
                ampm = 'Midnight'
            else
                ampm = 'AM'
            End if
        End if
    End if

    Write(*,*)
    write (*,'(2X,i6,1x,a,1x,i4,2x,i2,a1,i2.2,a1,i2.2,a1,i3.3,1x,a)') &
    d, trim (month(m)), y, h, ':', n, ':', s, '.', mm, trim (ampm)
    Return
    Write(*,*)
    Write(*,*)'             _______________________             '  

    Write(Ounit,*)
    write (Ounit,'(2X,i6,1x,a,1x,i4,2x,i2,a1,i2.2,a1,i2.2,a1,i3.3,1x,a)') &
    d, trim (month(m)), y, h, ':', n, ':', s, '.', mm, trim (ampm)
    Return
    Write(Ounit,*)
    Write(Ounit,*)'             _______________________             '  
End subroutine

Subroutine title1() 
implicit none
Integer, Parameter ::  Ounit = 100
Open (Unit=Ounit, File='app/Output/NEM.out') 
    Write(*,*) ''
    ! Write(*,*) 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM' &
    ! 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM'
    ! Write(*,*) ''
    ! Write(*,*) '     CCCCCCCCCC                                            NN           NN      EEEEEEEEE     MM             MM    '
    ! Write(*,*) '    CCCCCCCCCCCCC                                         NNNN         NNN     EEEEEEEEE     MMMM           MMMM   '
    ! Write(*,*) '   CCCC      CCCCC                                       NNNNNN       NNNN    EEEE          MMMMMM         MMMMMM  '
    ! Write(*,*) '  CCCC        CCCC                                       NNNNNNN      NNNN    EEEE          MMMMMMM       MMMMMMM  '
    ! Write(*,*) ' CCCC           CC                                       NNNN  NN     NNNN    EEEE          MMMM  MMM   MMM  MMMM  '
    ! Write(*,*) ' CCCC                                                    NNNN  NNN    NNNN    EEEE          MMMM   MMMMMMM   MMMM  '
    ! Write(*,*) ' CCCC                    AAAAAAAAAA         RRRRRRRRR    NNNN   NNN   NNNN    EEEEEEEEE     MMMM    MMMMM    MMMM  '
    ! Write(*,*) ' CCCC                   AAAAAAAAAAAA       RRRRRRRR      NNNN   NNN   NNNN    EEEEEEEEEE    MMMM     MMM     MMMM  '
    ! Write(*,*) ' CCCC                  AAAA      AAAA     RRR            NNNN    NNN  NNNN    EEEEEEEEE     MMMM             MMMM  '
    ! Write(*,*) ' CCCC           CC    AAAA       AAAA    RRRR            NNNN     NN  NNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '  CCCC        CCCC    AAAA       AAAA    RRRR            NNNN      NNNNNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '   CCCC      CCCCC     AAAA      AAAA    RRRR            NNNN       NNNNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '    CCCCCCCCCCCCC       AAAAAAAAAAAAA    RRRR            NNN         NNNN      EEEEEEEEE    MMM               MMM  '
    ! Write(*,*) '     CCCCCCCCCC          AAAAAAAAAAAA    RRRR            NN           NN        EEEEEEEEE   MM                 MM  '
    ! Write(*,*)
    ! Write(*,*) 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM' &
    ! 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM'




    Write(*,*) '                                                                               '
    Write(*,*) '     /\               /\                                                       '
    Write(*,*) '    //\\             //\\                                                      '
    Write(*,*) '   //**\\           //**\\                                                     '
    Write(*,*) '  //****\\         //****\\                                                    '
    Write(*,*) ' //******\\       //******\\   ____                   _   _           _        '  
    Write(*,*) ' ---------   /*\   ---------  / __ \                 | \ | |         | |       '
    Write(*,*) '            (***)            | |  | |_ __   ___ _ __ |  \| | ___   __| | ___   '
    Write(*,*) '             \*/             | |  | | "_ \ / _ \ "_ \| . ` |/ _"\ / _" |/ _ \  '
    Write(*,*) '                             | |__| | |_) |  __/ | | | |\  | |_) | (_| |  __/  '
    Write(*,*) '             //\\             \____/| .__/ \___)_| |_|_| \_|\___/ \___/ \___|  '
    Write(*,*) '            //**\\                  | |                                        '
    Write(*,*) '           //****\\                 |_|                                        '
    Write(*,*) '          //******\\                                                           '
    Write(*,*) '          ----------                                                           '
    Write(*,*) '                                                                               '
    Write(*,*) '____________________________________________________________'
    Write(*,*) '         | The OpenNode, Nodal Methods for Neutron Diffusion'       
    Write(*,*) 'Version  | Version Number: 1.1                              '     
    Write(*,*) 'Copyright| 2021 Radiation & Nuclear System Laboratory       '
    Write(*,*) '         | University Abdelmalek Essaadi                    '
    Write(*,*) '         | Faculty of Sciences, Tetouan, Morocco            '
    Write(*,*) 'Source   | FORTRAN90 version                                ' 
    Write(*,*) 'GUI      | PyQt5                                            ' 
    Write(*,*) 'Method   | The Nodal Expansion Method (NEM)                 '  
    Write(*,*) 'Dimension| Three Dimensions (3D)                            '
    Write(*,*) 'Geometry | Cartesian                                        ' 
    Write(*,*) '____________________________________________________________'
    ! Write(*,*) ''
    ! Write(*,*) '     CCCCCCCCCC                                          &
       ! NN           NN      EEEEEEEEE     MM             MM    '
    ! Write(*,*) '    CCCCCCCCCCCCC                                       &
     ! NNNN         NNN     EEEEEEEEE     MMMM           MMMM   '
    ! Write(*,*) '   CCCC      CCCCC                                     &
    ! NNNNNN       NNNN    EEEE          MMMMMM         MMMMMM  '
    ! Write(*,*) '  CCCC        CCCC                                     &
    ! NNNNNNN      NNNN    EEEE          MMMMMMM       MMMMMMM  '
    ! Write(*,*) ' CCCC           CC                                     &
    ! NNNN  NN     NNNN    EEEE          MMMM  MMM   MMM  MMMM  '
    ! Write(*,*) ' CCCC                                                  &
    ! NNNN  NNN    NNNN    EEEE          MMMM   MMMMMMM   MMMM  '
    ! Write(*,*) ' CCCC                    AAAAAAAAAA         RRRRRRRRR  &
    ! NNNN   NNN   NNNN    EEEEEEEEE     MMMM    MMMMM    MMMM  '
    ! Write(*,*) ' CCCC                   AAAAAAAAAAAA       RRRRRRRR    &
    ! NNNN   NNN   NNNN    EEEEEEEEEE    MMMM     MMM     MMMM  '
    ! Write(*,*) ' CCCC                  AAAA      AAAA     RRR          &
    ! NNNN    NNN  NNNN    EEEEEEEEE     MMMM             MMMM  '
    ! Write(*,*) ' CCCC           CC    AAAA       AAAA    RRRR          &
    ! NNNN     NN  NNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '  CCCC        CCCC    AAAA       AAAA    RRRR          &
    ! NNNN      NNNNNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '   CCCC      CCCCC     AAAA      AAAA    RRRR          &
    ! NNNN       NNNNNN    EEEE          MMMM             MMMM  '
    ! Write(*,*) '    CCCCCCCCCCCCC       AAAAAAAAAAAAA    RRRR          &
    ! NNN         NNNN      EEEEEEEEE    MMM               MMM  '
    ! Write(*,*) '     CCCCCCCCCC          AAAAAAAAAAAA    RRRR          &
    ! NN           NN        EEEEEEEEE   MM                 MM  '
    Write(ounit,*) '                                                                               '
    Write(ounit,*) '     /\               /\                                                       '
    Write(ounit,*) '    //\\             //\\                                                      '
    Write(ounit,*) '   //**\\           //**\\                                                     '
    Write(ounit,*) '  //****\\         //****\\                                                    '
    Write(ounit,*) ' //******\\       //******\\   ____                   _   _           _        '  
    Write(ounit,*) ' ---------   /*\   ---------  / __ \                 | \ | |         | |       '
    Write(ounit,*) '            (***)            | |  | |_ __   ___ _ __ |  \| | ___   __| | ___   '
    Write(ounit,*) '             \*/             | |  | | "_ \ / _ \ "_ \| . ` |/ _"\ / _" |/ _ \  '
    Write(ounit,*) '                             | |__| | |_) |  __/ | | | |\  | |_) | (_| |  __/  '
    Write(ounit,*) '             //\\             \____/| .__/ \___)_| |_|_| \_|\___/ \___/ \___|  '
    Write(ounit,*) '            //**\\                  | |                                        '
    Write(ounit,*) '           //****\\                 |_|                                        '
    Write(ounit,*) '          //******\\                                                           '
    Write(ounit,*) '          ----------                                                           '
    Write(ounit,*) '                                                                               '
    Write(ounit,*) '____________________________________________________________'
    Write(ounit,*) '         | The OpenNode, Nodal Methods for Neutron Diffusion'       
    Write(ounit,*) 'Version  | Version Number: 1.1                              '     
    Write(ounit,*) 'Copyright| 2021 Radiation & Nuclear System Laboratory       '
    Write(ounit,*) '         | University Abdelmalk Essaadi                     '
    Write(ounit,*) '         | Faculty of Sciences, Tetouan, Morocco            '
    Write(ounit,*) 'Source   | FORTRAN90 version                                ' 
    Write(ounit,*) 'GUI      | PyQt5                                            ' 
    Write(ounit,*) 'Method   | The Nodal Expansion Method (NEM)                 '  
    Write(ounit,*) 'Dimension| Three Dimensions (3D)                            '
    Write(ounit,*) 'Geometry | Cartesian                                        ' 
    Write(ounit,*) '____________________________________________________________'
    ! Write(ounit,*) ''
    ! Write(ounit,*) 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM' &
    ! 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM'
    ! Write(ounit,*) ''    
    ! Write(ounit,*) '     CCCCCCCCCC                                          &
       ! NN           NN      EEEEEEEEE     MM             MM    '
    ! Write(ounit,*) '    CCCCCCCCCCCCC                                       &
     ! NNNN         NNN     EEEEEEEEE     MMMM           MMMM   '
    ! Write(ounit,*) '   CCCC      CCCCC                                     &
    ! NNNNNN       NNNN    EEEE          MMMMMM         MMMMMM  '
    ! Write(ounit,*) '  CCCC        CCCC                                     &
    ! NNNNNNN      NNNN    EEEE          MMMMMMM       MMMMMMM  '
    ! Write(ounit,*) ' CCCC           CC                                     &
    ! NNNN  NN     NNNN    EEEE          MMMM  MMM   MMM  MMMM  '
    ! Write(ounit,*) ' CCCC                                                  &
    ! NNNN  NNN    NNNN    EEEE          MMMM   MMMMMMM   MMMM  '
    ! Write(ounit,*) ' CCCC                    AAAAAAAAAA         RRRRRRRRR  &
    ! NNNN   NNN   NNNN    EEEEEEEEE     MMMM    MMMMM    MMMM  '
    ! Write(ounit,*) ' CCCC                   AAAAAAAAAAAA       RRRRRRRR    &
    ! NNNN   NNN   NNNN    EEEEEEEEEE    MMMM     MMM     MMMM  '
    ! Write(ounit,*) ' CCCC                  AAAA      AAAA     RRR          &
    ! NNNN    NNN  NNNN    EEEEEEEEE     MMMM             MMMM  '
    ! Write(ounit,*) ' CCCC           CC    AAAA       AAAA    RRRR          &
    ! NNNN     NN  NNNN    EEEE          MMMM             MMMM  '
    ! Write(ounit,*) '  CCCC        CCCC    AAAA       AAAA    RRRR          &
    ! NNNN      NNNNNNN    EEEE          MMMM             MMMM  '
    ! Write(ounit,*) '   CCCC      CCCCC     AAAA      AAAA    RRRR          &
    ! NNNN       NNNNNN    EEEE          MMMM             MMMM  '
    ! Write(ounit,*) '    CCCCCCCCCCCCC       AAAAAAAAAAAAA    RRRR          &
    ! NNN         NNNN      EEEEEEEEE    MMM               MMM  '
    ! Write(ounit,*) '     CCCCCCCCCC          AAAAAAAAAAAA    RRRR          &
    ! NN           NN        EEEEEEEEE   MM                 MM  '
    ! Write(ounit,*)
    ! Write(ounit,*) 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM' &
    ! 'CarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEMCarNEM'

End Subroutine

Subroutine title2()
       Write(*,*)''
       Write(*,*)'                         Finished                         '                             
       Write(*,*)'                         --------                         '  
End Subroutine
