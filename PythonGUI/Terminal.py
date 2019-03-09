from DataManger import DataManger as DM
import PosDist
import sys
import spiceypy as spice

if __name__ == "__main__":


 
    data_source = DM()
    data_source.update()
    kernel_list = data_source.datasets
    for kernel in kernel_list:           
        spice.furnsh(kernel)

        utc_time = sys.argv[1:3]
        et_time = [ spice.str2et(x) for x in utc_time]

        step = sys.argv[3]    
        timestep = [x*(et_time[0]-et_time[1])/step + et_time[0] for x in range(step)]

        target = sys.argv[4]
        obs = sys.argv[5]      
        pos_vec, lightdist = spice.spkpos(target, timestep, 'J2000', 'None', obs)
        spice.kclear()

    
    


    
