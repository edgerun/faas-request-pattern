# 1 km * 1 km, cloudlet area = 1 km x 1 km
python generate_request_pattern.py --name new_york_1x1_1x1_min --topology data/topologies/new_york_1x1_1x1.csv --trips data/trips/new_york_1x1/minInterval.csv
python generate_request_pattern.py --name new_york_1x1_1x1_avg --topology data/topologies/new_york_1x1_1x1.csv --trips data/trips/new_york_1x1/avgInterval.csv
python generate_request_pattern.py --name new_york_1x1_1x1_max --topology data/topologies/new_york_1x1_1x1.csv --trips data/trips/new_york_1x1/maxInterval.csv

# 0.5 km * 0.5 km, cloudlet area = 0.5 km * 0.5 km
python generate_request_pattern.py --name new_york_1x1_05x05_min --topology data/topologies/new_york_1x1_05x05.csv --trips data/trips/new_york_1x1/minInterval.csv
python generate_request_pattern.py --name new_york_1x1_05x05_avg --topology data/topologies/new_york_1x1_05x05.csv --trips data/trips/new_york_1x1/avgInterval.csv
python generate_request_pattern.py --name new_york_1x1_05x05_max --topology data/topologies/new_york_1x1_05x05.csv --trips data/trips/new_york_1x1/maxInterval.csv

# 2.0 km * 2.0 km, cloudlet area = 1 km x 1 km

python generate_request_pattern.py --name new_york_2x2_1x1_min --topology data/topologies/new_york_2x2_1x1.csv --trips data/trips/new_york_2x2/minInterval.csv
python generate_request_pattern.py --name new_york_2x2_1x1_avg --topology data/topologies/new_york_2x2_1x1.csv --trips data/trips/new_york_2x2/avgInterval.csv
python generate_request_pattern.py --name new_york_2x2_1x1_max --topology data/topologies/new_york_2x2_1x1.csv --trips data/trips/new_york_2x2/maxInterval.csv

# 2.0 km * 2.0 km, cloudlet area = 2 km x 1 km
python generate_request_pattern.py --name new_york_2x2_2x1_min --topology data/topologies/new_york_2x2_2x1.csv --trips data/trips/new_york_2x2/minInterval.csv
python generate_request_pattern.py --name new_york_2x2_2x1_avg --topology data/topologies/new_york_2x2_2x1.csv --trips data/trips/new_york_2x2/avgInterval.csv
python generate_request_pattern.py --name new_york_2x2_2x1_max --topology data/topologies/new_york_2x2_2x1.csv --trips data/trips/new_york_2x2/maxInterval.csv