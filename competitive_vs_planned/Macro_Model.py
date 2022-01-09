#Macro Model

from scipy.optimize import fsolve
import math

'https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html'

sigma = 3.0 # σ elasticity of substitution across products
gamma = 5.0 # γ elasticity of substitution across competing products
kappa = 0.5 # κ extent to which firms producing competing products collude
upsilon = 1.0 # ν value of leisure  
psi = 2.0 # ψ slope of labor supply
phi = 0.1 # φ scale of the cost externality
f = 0.05 # f magnitude of the cost to move between location
 
current_U = 0
current_Z = 1

def func(p):

    y_j, y_a, y_d, s_d = p

    #3.1/2/3: Labor Usage
    l_j = y_j * math.exp(-(phi)*(1+N))
    l_a = y_a * math.exp(-(phi)*(1+N))
    l_d = y_d * math.exp(-(phi)*(1+N))

    #3.4/5/6: Aggregate number of firms, consumption and wages
    n = (2*l_j*N) + ((1-N)*l_a) + ((1-N)*l_d) + (2*f*(N+((1-N)*math.log(1-N))))
    C = (pow(  ((pow(2,(1+((gamma/sigma)*((sigma-1)/(gamma-1))))) * N * pow(y_j, (1-(1/sigma))))) +   (2 * (1 - N) * pow((pow(y_a, (1-(1.0/gamma))) + pow(y_d, (1-(1.0/gamma)))), ((gamma/sigma)*(sigma-1)*(1/(gamma - 1)))))   ,sigma/(sigma - 1)))
    w = C*upsilon*(pow(n,1/psi))

    #3.15
    s_a = 1.0 - s_d

    #3.8/9/10
    mi_j = (1/(1-(1/gamma)+((1+kappa)/2)*((1/gamma)-(1/sigma))))
    mi_a = (1/(1-(1/gamma)+(1-s_d)*((1/gamma)-(1/sigma))))
    mi_d = (1/(1-(1/gamma)+(s_d)*((1/gamma)-(1/sigma))))
    

    return [
            w*mi_j*math.exp(-phi*(1+N)) - ((pow(y_j,(-1/gamma)))*(pow(2*C, 1/sigma))*(pow(pow(2*y_j,1-(1/gamma)),((gamma/sigma)*((sigma-1)/gamma-1) - 1 )))),
            w*mi_a*math.exp(-phi*(1+N)) - ((pow(y_a,(-1/gamma)))*(pow(2*C, 1/sigma))*(pow(pow(2*y_a,1-(1/gamma)) + pow(2*y_d,1-(1/gamma)),((gamma/sigma)*((sigma-1)/gamma-1) - 1 )))),
            w*mi_d*math.exp(-phi*(1+N)) - ((pow(y_d,(-1/gamma)))*(pow(2*C, 1/sigma))*(pow(pow(2*y_a,1-(1/gamma)) + pow(2*y_d,1-(1/gamma)),((gamma/sigma)*((sigma-1)/gamma-1) - 1 )))),   
            math.exp(2*N*phi) - (pow((s_d/s_a),1/(1-gamma)) * (1 - (1/gamma) + s_d*((1/gamma) - (1/sigma)))/(1 - (1/gamma) + s_a*((1/gamma) - (1/sigma)))) 
            ]


for N in range(0,1000):

    N = float(N) * float(0.001)

    #print('For N = ' + str(N) + ':')

    y_j, y_a, y_d, s_d =  fsolve(func, [0.2,0.3,0.1,0.2])
    #print(root)

    #print('y_j = ' + str(y_j))
    #print('y_a = ' + str(y_a))
    #print('y_d = ' + str(y_d))
    #print('s_d = ' + str(s_d))

    l_j = y_j * math.exp(-(phi)*(1+N))
    l_a = y_a * math.exp(-(phi)*(1+N))
    l_d = y_d * math.exp(-(phi)*(1+N))

    mi_j = 1/(1-(1/gamma)+((1+kappa)/2)*((1/gamma)-(1/sigma)))
    mi_a = 1/(1-(1/gamma)+(1-s_d)*((1/gamma)-(1/sigma)))
    mi_d = 1/(1-(1/gamma)+(s_d)*((1/gamma)-(1/sigma)))

    n = (2*l_j*N) + ((1-N)*l_a) + ((1-N)*l_d) + (2*f*(N+((1-N)*math.log(1-N))))
    C = (pow(  ((pow(2,(1+((gamma/sigma)*((sigma-1)/(gamma-1))))) * N * pow(y_j, (1-(1/sigma))))) +   (2 * (1 - N) * pow((pow(y_a, (1-(1.0/gamma))) + pow(y_d, (1-(1.0/gamma)))), ((gamma/sigma)*(sigma-1)*(1/(gamma - 1)))))   ,sigma/(sigma - 1)))
    w = C*upsilon*(pow(n,1/psi))

    #Equations for profits
    pi_j = (mi_j - 1)*w*math.exp(-phi*(1+N))*y_j
    pi_a = (mi_a - 1)*w*math.exp(-phi*(1+N))*y_j
    pi_d = (mi_d - 1)*w*math.exp(-phi*(1+N))*y_j

    #3.7
    U = math.log(C) - upsilon*(pow(n,1+psi))/(1+psi)
    #4.6
    Z = pi_j - pi_d + (f)*(w)*(math.log(1-N))

    #print('U is ' + str(U))
    #print('Z is ' + str(Z))
   
    if U > current_U: 
        current_U = U
        j = N    
     
    if math.fabs(Z) < math.fabs(current_Z): 
        current_Z = Z
        k = N


#Competitive outcome 
print('Competitive outcome has ' + str(k) + ' firms moving')

#Planner's Outcome
print("Planner's outcome has " + str(j) + " firms moving")
