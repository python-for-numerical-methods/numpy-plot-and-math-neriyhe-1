import numpy as np

def normalized_array(data):
  data_arr = np.array(input_array)
  if np.all(data_arr == data_arr[0]):
    return np.zeros(data_arr.shape)
  else:
    new_arr = (data_arr - np.min(data_arr))/(np.max(data_arr) - np.min(data_arr))

  return new_arr
