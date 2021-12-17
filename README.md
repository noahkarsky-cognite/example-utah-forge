# example-utah-forge
contains example notebooks leveraging Cognite Python SDK to upload geothermal well data


Execute order for notebooks
1. asset_creation_file_upload.ipynb
2. sequence_creation.ipynb
3. sequence_visualization.ipynb


## Dataset Notes:
All data comes from a U.S. Department of Energy website known as the Geothermal Data Repository. This website contains a number of data submissions from various public projects across the US. One popular project featured on the website is the Utah FORGE Project. The FORGE site on the GDR website contains a 3D view of 3 wells and contains some well stimulation data. My main goal was to reproduce what we see here, but I will do it leveraging data within CDF.

From the FORGE project, the data I chose to leverage are 3 wells (68-32,78-32,58-32).

Data types used in this example:
.pdf's of various drilling reports
.jpg's of the well site
.las files containing log data
.pdf versions of the logs


We first create the assets using the three wells. Then we upload associated files for each well. We then leverage some functions to read .las files and upload them to sequences for our wells. Finally we show how easy it is to retrieve the log data from CDF.
