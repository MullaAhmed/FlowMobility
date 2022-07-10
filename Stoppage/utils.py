import pandas as pd
import numpy as np
def magnitude(x,y,z):
    mag=np.sqrt((x**2)+(y**2)+(z**2))
    return mag

def mag_array(x_arr,y_arr,z_arr):
    mag_arr=[]
    for i in range(len(x_arr)):
        x,y,z=x_arr[i],y_arr[i],z_arr[i]
        mag=magnitude(x,y,z)
        mag_arr.append(mag)
    
    return np.array(mag_arr)

def normalize(arr, t_min, t_max):
    norm_arr = []
    diff = t_max - t_min
    diff_arr = max(arr) - min(arr)    
    for i in arr:
        temp = (((i - min(arr))*diff)/diff_arr) + t_min
        norm_arr.append(temp)

    return np.array(norm_arr)

def rolling_avg(arr,window_size):
    numbers_series = pd.Series(arr)
    windows = numbers_series.rolling(window_size)
    moving_averages = windows.mean()
    moving_averages_list = moving_averages.tolist()
    final_list = moving_averages_list[window_size - 1:]

    return(final_list)


def get_detection(df):
    data=df
    x,y,z=[],[],[]

    for i in (range(data.shape[0])):
        d=data.iloc[i,:].values
        x.append(d[4])
        y.append(d[5])
        z.append(d[6])

    x,y,z=np.array(x),np.array(y),np.array(z)
    mag_arr=mag_array(x,y,z)
    datasamples=len(mag_arr)

    mag_arr=rolling_avg(mag_arr,int(len(mag_arr)*0.1))
    if datasamples>=2000:
        mag_arr=rolling_avg(mag_arr,int(len(mag_arr)*0.1))
    if datasamples>=5000:
        mag_arr=rolling_avg(mag_arr,int(len(mag_arr)*0.1))

    normal_mag_arr=normalize(mag_arr,0,1)
    decision=[]
    for n in normal_mag_arr[-50:]:
        if n<0.09:
            decision.append(1)
    if sum(decision)>45:
        return True