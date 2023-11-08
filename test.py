def interpolate_energy(e1, e2, tmsp_arr, speed_arr):
    # Iterating the arraysand creating the slope array
    print("Inside interpolate_energy")
    print(tmsp_arr)
    print(speed_arr)
    slope_arr = []
    for i in range(len(tmsp_arr)):
        if i == 0:
            continue
        else:
            slope_arr.append((speed_arr[i] - speed_arr[i-1])/(tmsp_arr[i] - tmsp_arr[i-1]))
    print(slope_arr)
    # Now solving the slopes
    coeff = 0
    for i in range(1, len(tmsp_arr)):
        if slope_arr[i-1] < 0 or (slope_arr[i-1] == 0 and speed_arr[i] < 1):
            continue
        else:
            coeff = coeff + (slope_arr[i-1]+1) * (tmsp_arr[i] - tmsp_arr[i-1])
    print(coeff)
    # Now getting the common factor
    common_factor = 0
    if coeff != 0:
        common_factor = (e2 - e1)/coeff
    print(common_factor)
    # Now we have the slope array, we can interpolate the energy values
    energy_arr = [e1]
    for i in range(len(tmsp_arr)):
        if i == 0:
            continue
        else:
            if slope_arr[i-1] < 0:
                energy_arr.append(energy_arr[i-1])
            else:
                energy_arr.append(energy_arr[i-1] + (slope_arr[i-1]+1) * common_factor * (tmsp_arr[i] - tmsp_arr[i-1]))
    for i in range(len(energy_arr)):
        print(tmsp_arr[i], speed_arr[i], energy_arr[i])
    exit()
    return energy_arr

if __name__ == '__main__':
    interpolate_energy(0,10,[10,30,40,80,110], [10,20,30,40,40])