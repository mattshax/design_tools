import sys,json
import numpy as np

def f_xy(x,y):
    f1x = (np.sin(5.1 * np.pi * x + 0.5))**6
    f2x = np.exp(-4*np.log(2) * (x - 0.0667)**2/0.64)
    f1y = (np.sin(5.1 * np.pi * y + 0.5))**6
    f2y = np.exp(-4*np.log(2) * (y - 0.0667)**2/0.64)
    return f1x*f2x*f1y*f2y

if __name__ == '__main__':
    
    # Reading x and y
    x = float(sys.argv[1])
    y = float(sys.argv[2])
    
    # Calculating f_xy
    z = f_xy(x, y)
    
    ###################
    # Writing metrics #
    ###################
    # Reading name of .txt file
    #metricsfile = sys.argv[3]
    # f = open(metricsfile, 'w')
    # f.write("x="+str(x)+'\n')
    # f.write("y="+str(y)+'\n')
    # f.write("z="+str(z)+'\n')
    # f.close()
    
    result = {
        "x": x,
        "y": y,
        "z": round(z,6)
    }
    
    print(json.dumps(result))