import numpy as np
import matplotlib.pyplot as plt

x_arr = np.linspace(0,0.4,21)
y_arr = np.linspace(0,0.4,21)
t_arr = np.linspace(0,200,20000)
T_arr = np.ones((21,21,20000))*20 # Indices: x, y, t
T_F = 180
T_0 = -15
T_room = 20
T_arr[10,10,:] = T_0

T_arr[:,0,0] = 180
T_arr[:,20,0] = 180
T_arr[0,:,0] = 180
T_arr[20,:,0] = 180
    
alpha = 1.4e-07
rho = 1110
h = 10
k = 40
deltat = 0.01
deltax = x_arr[1] - x_arr[0]
t_max = 200
A = (alpha * deltat) / (deltax**2)

def Plotting(x_array,y_array,t_array,T_array):
    for t in [0, 1, 10, 100, 1000]:
        t_float = t * deltat
        plt.plot(x_array,T_array[:,10,t],label = 'time = %.2f' % t)

    plt.legend()    
    plt.show()

if __name__ == '__main__':
    for t in range(1,2000):
        time = t * deltat
        for i in range(21):
            for j in range(21):
                # Corners
                if i == 0 and j == 0:
                    T_arr[i,j,t] = A * (T_arr[i+1,j,t-1] + T_arr[i,j+1,t-1]) + (1 - 4 * A) * T_arr[i,j,t-1]
                elif i == 0 and j == 20:
                    T_arr[i,j,t] = A * (T_arr[i+1,j,t-1] + T_arr[i,j-1,t-1]) + (1 - 4 * A) * T_arr[i,j,t-1]                    
                elif i == 20 and j == 0:
                    T_arr[i,j,t] = A * (T_arr[i-1,j,t-1] + T_arr[i,j+1,t-1]) + (1 - 4 * A) * T_arr[i,j,t-1]                    
                elif i == 20 and j == 20:
                    T_arr[i,j,t] = A * (T_arr[i-1,j,t-1] + T_arr[i,j-1,t-1]) + (1 - 4 * A) * T_arr[i,j,t-1]                    
                # Edges.    
                    # One of the corners.

                elif i == 0 and j != 0 and j != 20:
                    T_arr[i,j,t] = A * (T_arr[i,j+1,t-1] + T_arr[i,j-1,t-1] + (2 * h * deltax / k) * T_F) + (1 - 4 * A - (2 * alpha * h * deltat)/(k * deltax)) * T_arr[i,j,t-1]
                elif i == 20 and j != 0 and j != 20:                    
                    # On the i edge.
                    T_arr[i,j,t] = A * (2 * T_arr[i-1,j,t-1] + T_arr[i,j+1,t-1] + T_arr[i,j-1,t-1] + (2 * h * deltax / k) * T_F) + (1 - 4 * A - (2 * alpha * h * deltat)/(k * deltax)) * T_arr[i,j,t-1]   #                elif j == 0 and i != 0 and i != 20:       
                    # On the j edge.
#                elif j == 20 and i != 0 and i != 20:                    
                else:
                    T_arr[i,j,t] = 2 * A * (T_arr[i-1,j,t-1] + T_arr[i,j-1,t-1] + 2 * h * deltax * T_F / k) + (1 - 4 * A - (4 * alpha * h * deltat / (k * deltax))) * T_arr[i,j,t-1] 
    Plotting(x_arr,y_arr,t_arr,T_arr)
    
