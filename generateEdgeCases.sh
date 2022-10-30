# prepare trip data
python prepare_trip_dataset.py --name new_york_2x2 --topology data/topologies/new_york_2x2_1x1.csv --path trip_data
# generate edge cases
python get_edge_cases.py --name new_york_2x2 --trips data/trips/new_york_2x2/trips.csv

# prepare trip data
python prepare_trip_dataset.py --name new_york_1x1 --topology data/topologies/new_york_1x1_1x1.csv --path trip_data
# generate edge cases
python get_edge_cases.py --name new_york_1x1 --trips data/trips/new_york_1x1/trips.csv