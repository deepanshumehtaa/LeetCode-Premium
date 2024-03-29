"""
Easy

An experiment is being conducted in a lab. To ensure accuracy, there are two sensors collecting data simultaneously.
You are given two arrays sensor1 and sensor2, where sensor1[i] and sensor2[i] are the ith data points collected by the two sensors.

However, this type of sensor has a chance of being defective, which causes exactly one data point to be dropped.
After the data is dropped, all the data points to the right of the dropped data are shifted one place to the left, and the last data point is replaced with some random value. It is guaranteed that this random value will not be equal to the dropped value.

For example, if the correct data is [1,2,3,4,5] and 3 is dropped, the sensor could return [1,2,4,5,7] (the last position can be any value, not just 7).
We know that there is a defect in at most one of the sensors. Return the sensor number (1 or 2) with the defect.
If there is no defect in either sensor or if it is impossible to determine the defective sensor, return -1.


Ex1:
Input: sensor1 = [2,3,4,5], sensor2 = [2,1,3,4]
Output: 1
Explanation: Sensor 2 has the correct values.
The second data point from sensor 2 is dropped, and the last value of sensor 1 is replaced by a 5.

Ex2:
Input: sensor1 = [2,2,2,2,2], sensor2 = [2,2,2,2,5]
Output: -1
Explanation: It is impossible to determine which sensor has a defect.
Dropping the last value for either sensor could produce the output for the other sensor.
"""



def badSensor(self, sensor1: List[int], sensor2: List[int]) -> int:
        n = len(sensor1)
        for i in range(n):
            if sensor1[i] != sensor2[i]: # find point at which the sensors differ
                break
        j = k = i # init two pointers
        while j < n-1 and sensor1[j] == sensor2[j+1]: # find to what point sensor1 data is shifted
            j += 1
        while k < n-1 and sensor1[k+1] == sensor2[k]: # find to what point sensor2 data is shifted
            k += 1
        # a sensor is faulty if the ptr reaches end of arr
        # if both reach end of arr, it's impossible to tell
        return -1 if k == n-1 and j == n-1 else 1 if j == n-1 else 2

