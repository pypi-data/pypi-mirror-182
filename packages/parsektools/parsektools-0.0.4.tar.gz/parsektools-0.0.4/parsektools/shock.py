# =============================================================================
# SHOCK RELATIONS
# =============================================================================

from parsektools.isa_athmosphere import *
from parsektools.ise

def normal_shock(h, m):
    
    [p0, t0, rho0, a0, g0] = atmosisa(h, "SI")
    
    
    p1 = p0*((2*gama*m**2-(gama-1))/(gama+1))
    
       
    return p1 