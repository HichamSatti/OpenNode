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
