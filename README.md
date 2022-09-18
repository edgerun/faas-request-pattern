# faas-request-pattern

##data
We use the generated topology datasets from https://github.com/edgerun/faas-topologies and the public available taxi trip data from https://chriswhong.com/open-data/foil_nyc_taxi/

- place the  `.csv` <i>topology</i> data file into the `data/topologies` folder
- place the `.csv` <i>trip</i> data file into the `data/trips` folder

## prepare dataset

To prepare the trip dataset, execute following command and specify the required parameter.
`python prepare_trip_dataset.py --path data/trips/example.csv --topology data/topologies/example.csv --name example_output`

It creates a new csv file and names it like the given `--name`
parameter. The `--trip` data got filtered by the maximum boundaries of the given `--topology` file.

## generate request pattern
`python generate_request_pattern.py --name example --trips data/trips/example.csv --topology data/topologies/example.csv`

<b>trip input:</b><br>
- <b>medallion:</b> string
- <b>pickup_datetime:</b> string
- <b>dropoff_datetime:</b> string
- <b>passenger_count:</b> float
- <b>pickup_longitude:</b> float
- <b>pickup_latitude:</b> float
- <b>dropoff_longitude:</b> float
- <b>dropoff_latitude:</b> float

<b>topology input:</b><br>
- <b>radio:</b> string
- <b>cell:</b> string
- <b>lon:</b> float
- <b>lat:</b> float
- <b>distances:</b> float