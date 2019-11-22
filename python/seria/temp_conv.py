from datetime import datetime
from csv import reader
from netCDF4 import Dataset
import numpy as np

def convert_time(time):
    time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f")
    return time

def convert_temp(temp):
    value = temp.strip("+").strip("C").lstrip("0")
    return float(value) + 273.15

infile='serial_temp.tsv'
outfile='sensor_data.nc'

times=[]
temps=[]

with open(infile, 'rt') as tsvfile:
    tsvreader = reader(tsvfile, delimiter='\t')
    for row in tsvreader:
        times.append(convert_time(row[0]))
        temps.append(convert_temp(row[1]))

base_time = times[0]
time_values = []

for t in times:
    value = t - base_time
    ts = value.total_seconds()
    time_values.append(ts)

time_units = "seconds since " + base_time.strftime('%Y-%m-%d %H:%M:%S')

dataset = Dataset(outfile, "w", format='NETCDF4_CLASSIC')

time_dim = dataset.createDimension("time", None)

time_var = dataset.createVariable("time", np.float64, ("time",))
time_var[:] = time_values
time_var.units = time_units
time_var.standard_name = "time"
time_var.calendar = "standard"

temp = dataset.createVariable("temp", np.float32, ("time",))
temp[:] = temps
temp.var_id = "temp"
temp.long_name = "Temperature of sensor (K)"
temp.units = "K"
temp.standard_name = "air_temperature"

dataset.Conventions = "CF-1.6"
dataset.instituion = "NCAS"
dataset.title = "My first CF-netCDF file"
dataset.history = "%s: Written with script: write_data_to_netcdf.py" % (datetime.now)
