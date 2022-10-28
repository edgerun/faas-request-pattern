# 0.5 km * 0.5 km, cloudlet area = 0.25 km^2
python generate_request_pattern.py --name new_york_05x05km_025km2_min --topology data/topologies/new_york_05x05km_025km2.csv --trips data/trips/minInterval.csv
python generate_request_pattern.py --name new_york_05x05km_025km2_avg --topology data/topologies/new_york_05x05km_025km2.csv --trips data/trips/avgInterval.csv
python generate_request_pattern.py --name new_york_05x05km_025km2_max --topology data/topologies/new_york_05x05km_025km2.csv --trips data/trips/maxInterval.csv

# 0.5 km * 0.5 km, cloudlet area = 0.5 km^2
python generate_request_pattern.py --name new_york_05x05km_05km2_min --topology data/topologies/new_york_05x05km_05km2.csv --trips data/trips/minInterval.csv
python generate_request_pattern.py --name new_york_05x05km_05km2_avg --topology data/topologies/new_york_05x05km_05km2.csv --trips data/trips/avgInterval.csv
python generate_request_pattern.py --name new_york_05x05km_05km2_max --topology data/topologies/new_york_05x05km_05km2.csv --trips data/trips/maxInterval.csv

# 2.0 km * 2.0 km, cloudlet area = 0.5 km^2
python generate_request_pattern.py --name new_york_2x2km_05km2_min --topology data/topologies/new_york_2x2km_05km2.csv --trips data/trips/minInterval.csv
python generate_request_pattern.py --name new_york_2x2km_05km2_avg --topology data/topologies/new_york_2x2km_05km2.csv --trips data/trips/avgInterval.csv
python generate_request_pattern.py --name new_york_2x2km_05km2_max --topology data/topologies/new_york_2x2km_05km2.csv --trips data/trips/maxInterval.csv

# 2.0 km * 2.0 km, cloudlet area = 1 km^2
python generate_request_pattern.py --name new_york_2x2km_1km2_min --topology data/topologies/new_york_2x2km_1km2.csv --trips data/trips/minInterval.csv
python generate_request_pattern.py --name new_york_2x2km_1km2_avg --topology data/topologies/new_york_2x2km_1km2.csv --trips data/trips/avgInterval.csv
python generate_request_pattern.py --name new_york_2x2km_1km2_max --topology data/topologies/new_york_2x2km_1km2.csv --trips data/trips/maxInterval.csv