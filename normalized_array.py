import numpy as np

def normalized_array(data):
  data_arr = np.array(input_array)
  if np.all(data_arr == data_arr[0]):
    return np.zeros(data_arr.shape)
  else:
    new_arr = (data_arr - np.min(data_arr))/(np.max(data_arr) - np.min(data_arr))

  return new_arr

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
