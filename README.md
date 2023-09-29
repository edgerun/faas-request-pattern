# faas-request-pattern
Framework to generate request pattern, based on the faas-topologies repository generated topology datasets.
## data
We use the generated topology datasets from https://github.com/edgerun/faas-topologies and the public available taxi trip data from https://chriswhong.com/open-data/foil_nyc_taxi/

- place the  `.csv` <i>topology</i> data file into the `data/topologies` folder
- place the `.csv` <i>trip</i> data file into the `data/trips` folder

## prepare dataset

To prepare the trip dataset, execute following command and specify the required parameter.
`python prepare_trip_dataset.py --path data/trips/example.csv --topology data/topologies/example.csv --name example_output`

It creates a new csv file and names it like the given `--name`
parameter. The `--trip` data got filtered by the maximum boundaries of the given `--topology` file.

## generate request pattern
To generate the pattern use `python generate_request_pattern.py --name example --trips data/trips/example.csv --topology data/topologies/example.csv --start "2013-10-01 18:00:00" --end "2013-10-01 19:00:00"` where the start and end parameters define the time range in which the pattern will be created.
The ouput files are saved in a seperate folder in `output/${name}/1_pickups.csv` where the number in front of the filename indicates the cloudlet number in the selected topology. The file contains the time deltas of each request in the defined time range. 
`[1.5, 1.5, 1.5, 1.5]` means e.g. that 4 requests were sent to the specific cloudlet within an interval of 1.5 seconds.

<b>trip input:</b><br>
- <b>medallion:</b> string
- <b>pickup_datetime:</b> string
- <b>passenger_count:</b> float
- <b>pickup_longitude:</b> float
- <b>pickup_latitude:</b> float

<b>topology input:</b><br>
- <b>cell:</b> string
- <b>lon:</b> float
- <b>lat:</b> float
- <b>cloudlet:</b> string
