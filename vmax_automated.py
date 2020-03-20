# Created By: Dennis Zvigelsky
# 2020

import subprocess
import scipy as sp


FlexCode = """

TITLE 'Finding Max Voltage that produces 100deg'     { the problem identification }
COORDINATES cartesian2  { coordinate system, 1D,2D,3D, etc }
VARIABLES        { system variables }
	Voltage
	u
	v
	Temp
SELECT         { method controls }
errlim = 1e-6
DEFINITIONS    { parameter definitions }

! Heat flow stuff

rho_d ! material density

Tinitial = 20
Tsurr = 20
k  !Thermal conductivity
qdot = -k*grad(Temp) !heat flux density


h = 20
qconv = h*(Temp-Tsurr)

! Dimensions

mag = 0.1*globalmax(magnitude(x,y))/globalmax(magnitude(U,V))
hbot = 1e-6
htop = 2e-6
hmid = 1e-6
Lx = 24e-6
Ltip = 4e-6

! optimize for Vmax
Vmax = %s

! E and M properties

rho_e !Ohm-m, electrical resistivity
sigma_e = 1/rho_e !1/(Ohm-m)

Efield = -grad(Voltage) !V/m = N/C
J = sigma_e*Efield !N/(C-Ohm-m) = V/(m^2-Ohm)
qdotvol = dot(J, Efield) !Joule's law

{

! piezo electric stuff

epsilonr ! relative epsilon for material
epsilon = 8.85e-12*epsilonr

Dfield = epsilon*Efield
Qtheory = (epsilon*(Lx-Ltip)*1/hmid)*Vmax
}

{
! piezo electric fields
Efieldx = xcomp(Efield)
Efieldy = ycomp(Efield)
Efieldz = 0
}

!Stiffness matrix components (isotropic material)

E ! Stiffness
nu ! poisson's ratio

C11 =E*(1-nu)/(1+nu)/(1-2*nu)
C22 = C11
C33 = C11

C12 = E*nu/(1+nu)/(1-2*nu)
C13 = C12
C21 = C12
C23 = C12
C31 = C12
C32 = C12

C44 = E*(1-2*nu)/(1+nu)/(1-2*nu)
C55 = C44
C66 = C44

C14 = 0
C15 = C14
C16 = C14

C24 = 0
C25 = C14
C26 = C14

C34 = 0
C35 = C14
C36 = C14

C41 = 0
C42 = C41
C43 = C41

C51 = 0
C52 = C41
C53 = C41

C61 = 0
C62 = C41
C63 = C41

C45 = 0
C46 = 0

C54 = 0
C56 = 0

C64 = 0
C65 = 0

!thermal expansion coefficients
alpha

alphax = alpha
alphay = alpha 
alphaz = 0

alphayz = 0
alphaxz = 0
alphaxy = 0

DeltaTemp =Temp - Tinitial !If starting (unstrained) temperature is 20

{
!piezoelectric coupling coefficients
d11 =+2.3e-12		d12 = 2.3e-12	d13 = 0	d14 =0	d15 = 0				d16 = 0
d21 =+2.3e-12				d22 = -2.3e-12		d23 = 0		d24 = 0				d25 =0 d26 =0
d31 = 0				d32 = 0		d33 = 0		d34 = 0				d35 = 0				d36 = 0
}

!Strain definitions from displacements
ex = dx(u)
ey = dy(v)
ez = 0 !dz(w)
gyz = 0 !dy(w) + dz(v)
gxz = 0 !dx(w) + dz(u)
gxy = dx(v) + dy(u)

!Mechanical strain (Don't need to include piezo electrics)
exm  = ex  - alphax *DeltaTemp !- (d11*Efieldx+d21*Efieldy+d31*Efieldz)
eym  = ey  - alphay *DeltaTemp !- (d12*Efieldx+d22*Efieldy+d32*Efieldz)
ezm  = ez  - alphaz *DeltaTemp !- (d13*Efieldx+d23*Efieldy+d33*Efieldz)
gyzm = gyz - alphayz*DeltaTemp !- (d14*Efieldx+d24*Efieldy+d34*Efieldz)
gxzm = gxz - alphaxz*DeltaTemp !- (d15*Efieldx+d25*Efieldy+d35*Efieldz)
gxym = gxy - alphaxy*DeltaTemp !- (d16*Efieldx+d26*Efieldy+d36*Efieldz)

!Hookes Law
sx  = C11*exm + C12*eym + C13*ezm + C14*gyzm + C15*gxzm + C16*gxym
sy  = C21*exm + C22*eym + C23*ezm + C24*gyzm + C25*gxzm + C26*gxym
sz  = C31*exm + C32*eym + C33*ezm + C34*gyzm + C35*gxzm + C36*gxym
syz = C41*exm + C42*eym + C43*ezm + C44*gyzm + C45*gxzm + C46*gxym
sxz = C51*exm + C52*eym + C53*ezm + C54*gyzm + C55*gxzm + C56*gxym
sxy = C61*exm + C62*eym + C63*ezm + C64*gyzm + C65*gxzm + C66*gxym

 INITIAL VALUES !added to give a starting point for the simulation (even though not time-dependent) in attempt to make it start more smoothly

Voltage = Vmax
Temp = Tinitial

EQUATIONS        { PDE's, one for each variable }
  !div(grad(Voltage))=0 { one possibility }
	!div(J+Dfield) = 0
Voltage: div(J) = 0
u: dx(sx) + dy(sxy) = 0
v: dx(sxy) + dy(sy)  = 0
Temp: -div(k*grad(Temp)) = qdotvol


! CONSTRAINTS    { Integral constraints }
BOUNDARIES       { The domain definition }

	REGION 'Gold'       { For each material region }

	! properties
	rho_d = 19320
	E = 79e9
	nu = 0.42
	k = 314
	rho_e = 2.44e-8
	alpha = 14e-6

	START(0,0) load(Temp) = qconv line to (Lx, 0) load(Temp) = qconv line to (Lx, hbot+hmid) load(Temp) = 0 line to (Lx-Ltip, hbot+hmid) load(Temp) = qconv
		line to (Lx-Ltip, hbot) load(Temp) = qconv line to (0,hbot)
	value(Voltage) = 0 value(u) = 0 value(v) = 0 value(Temp) = 20 LINE TO close

	REGION 'Aluminum'       { For each material region }

	! properties
	rho_d = 2700
	E=69e9
	nu = 0.33
	k = 205	
	rho_e = 3.99e-8
	alpha = 23.2e-6	

    START(0,hbot+hmid) load(Temp) = qconv line to (Lx-Ltip,hbot+hmid) load(Temp) = 0 line to (Lx, hbot+hmid) load(Temp) = qconv line to (Lx, hbot+hmid+htop) load(Temp) = qconv line to (0, hbot+hmid+htop)
	value(Voltage) = Vmax value(u) = 0 value(v) = 0 value(Temp) = 20 LINE TO close
  

! TIME 0 TO 1    { if time dependent }
MONITORS         { show progress }
PLOTS            { save result displays }
 grid(x+mag*u, y+mag*v)
	
	!elevation(v) from (0,hbot+hmid+htop) to (Lx,hbot+hmid+htop) as "Displacement of v on the top of aluminum"
	!CONTOUR(Voltage) painted as "Voltage, V"
	!contour(Temp) painted as "Temperature, T"
	!vector(qdot) norm as "Heat Flux Density, qDot" 
	!vector(J) norm as "Electric Current Density, J"
	!vector(Efield) norm as "Electric Field, Efield"
	contour(Temp) export format "#1" file="tempVal.txt"! Max Temp [Deg C]
summary
	!report globalmax(Temp) export format "#Temp" file="tempVal.txt"! Max Temp [Deg C]
	!report val(u,Lx,hbot+hmid+htop) as "u displacement [m]"
	!report val(v,Lx,hbot+hmid+htop) as "v displacement [m]"
	report globalmax(Temp) as "Max Temp [deg C]"
	report Vmax as "Highest allowed Vmax [V] "
END


"""

FlexFileName = "C:\\Users\\denni\\OneDrive\\Documents\\McMaster\\Winter 2020\\Computational Multiphysics - 2CM4\\M8-Multiphysics\\automatedVmax.pde"

maxVolts = 0
maxTemp = 10000000

print("Temp","     ","Volts")
VoltRange = sp.arange(0.06,0.1,0.002)
for Volts in VoltRange:
    with open(FlexFileName, "w") as f:
        print(FlexCode%Volts, file=f)
        
    completed =subprocess.run(["FlexPDE6s","-S",FlexFileName],timeout=100, shell=True)#,shell=True)
    
    with open("C:\\Users\\denni\\OneDrive\\Documents\\McMaster\\Winter 2020\\Computational Multiphysics - 2CM4\\M8-Multiphysics\\tempVal.txt","r") as f:
        data=sp.loadtxt(f, skiprows=6)
    highTemp=max(data)
    
    space="     "
    print(highTemp,space,Volts)
    
    if abs(100-highTemp) < maxTemp:
        maxTemp=abs(100-highTemp)
        temp100=highTemp
        maxVolts=Volts

print("")
print("The maximum Voltage was ", maxVolts, "which caused a temperature of: ", temp100)