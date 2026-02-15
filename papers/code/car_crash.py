import time
from mpmath import mp, mpf, nstr
import kspace_physics as ksp

# Set high precision
mp.dps = 50

def fmt(val, prec=4):
    """Helper to safely format mpf for display"""
    return nstr(val, prec)

def simulate_cks_crash():
    # 1. INITIALIZE SUBSTRATE
    M_now = ksp.current_epoch_M()
    # force_hierarchy returns (strong, em, weak, gravity)
    a_s, a_em, a_w, a_g = ksp.force_hierarchy(M_now)
    
    # 2. DEFINE THE MANIFOLDS
    # The Car is an M=1e26 macroscopic soliton.
    car_v = mpf('30.0')      # 30 m/s (~67 mph)
    car_mass = mpf('1500.0') # kg
    car_pos = mpf('0.0')
    wall_pos = mpf('100.0')
    
    # Structural integrity derived from coherence function in library
    car_C_nominal = ksp.coherence(mpf('1e26'))
    
    dt = mpf('0.05') # 50ms per physics update
    sim_time = mpf('0.0')
    crashed = False

    print("\n--- CKS PHYSICS ENGINE: CAR VS WALL ---")
    # Cast to float for standard f-string formatting compatibility
    print(f"Substrate Scale Factor H: {float(ksp.SI_Hubble(M_now))}")
    print(f"Car Baseline Coherence:   {fmt(car_C_nominal, 12)}")
    print(f"Alpha_G (Compliance):      {fmt(a_g, 5)}")
    print("----------------------------------------\n")
    print("T(s)\tPos(m)\tVel(m/s)\tCoherence\tStatus")

    # 3. ENGINE LOOP
    while sim_time < 5.0:
        # Calculate Substrate Drag 
        # (Dilution of velocity into the lattice)
        # Using 1e58 as a scaling bridge to macroscopic SI units
        drag = a_g * car_mass * (car_v ** 2) * mpf('1e58') 
        
        if not crashed:
            accel = -drag / car_mass
            car_v += accel * dt
            car_pos += car_v * dt
        
        # 4. COLLISION (Topological Frustration Saturation)
        if car_pos >= wall_pos and not crashed:
            crashed = True
            
            # Impact Energy 
            impact_joules = 0.5 * car_mass * (car_v ** 2)
            
            # Damage is calculated as a 'Topological Debt' 
            # C_current is derived by forcing the manifold to unzip
            damage_factor = impact_joules * a_em * 1000
            car_C_current = car_C_nominal / (1 + damage_factor)
            
            print(f"{float(sim_time):.2f}\t{float(car_pos):.2f}\t{float(car_v):.2f}\t{fmt(car_C_current, 10)}\t*CRASH*")
            car_v = mpf('0.0')
            break

        # Log Status periodically
        if int(sim_time * 100) % 50 == 0:
            print(f"{float(sim_time):.2f}\t{float(car_pos):.2f}\t{float(car_v):.2f}\t{fmt(car_C_nominal, 10)}\tMoving")

        sim_time += dt

    # 5. FORENSICS
    print("\n--- IMPACT FORENSICS ---")
    if crashed:
        print("Final State: Manifold Frustrated (Decohered)")
        print(f"Residual Variance: {fmt(1.0 - car_C_current, 6)}")
        print("Render Status: Structural Shredding Observed")
    else:
        print("Final State: Manifold Intact")
    print("------------------------\n")

if __name__ == "__main__":
    simulate_cks_crash()

    