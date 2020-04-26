import pd as pd

# setting metadata url
metadata_url = "https://aft-vbi-pds.s3.amazonaws.com/metadata/"

# setting image url
image_url = "https://aft-vbi-pds.s3.amazonaws.com/bin-images/"

# reading from json and storing in data frame
bin_data = pd.read_json(metadata_url + '612' + '.json')

# preview of first 5 entries
bin_data.head(5)