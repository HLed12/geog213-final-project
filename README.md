Geog 213 Advanced Geospatial Analytics w/ Python - Final Project


2020 Census Block Maps and US Structures from Oak Ridge National Laboratory data sets


Purpose:
- Reproducibility. This project will focus on summarizing building data into one US Census block. This will allow others to follow my approach and use for other blocks or future adaptations.
- Analyze the Census block for trends.


Understanding what to use:
There are 2 ways to approach doing this work:

The ALL function method, which utilizes the following functions:
- get_s3_keys_all()
- get_US_structures_all()

The SPECIFIED function method, which utilizes the following functions:
- get_s3_keys_specified()
- get_US_structures_specified()

The All method should be taken and will be the main jupyter notebook that is used.

However, since the dataset is always changing, there is a chance the data will be too large for users to run. Currently, 12/8/2024, all the parquet files require ~20 GiBs of space. To review if this has changed, check the following site:
https://source.coop/wherobots/usa-structures/geoparquet

If you do not have space for all of the .parquet file sizes (on right side of feature box on source.coop page), then do NOT use the 'building_analysis_ALL' jupyter notebook. Instead, use the 'building_analysis_SPECIFIED' jupyter notebook. You will manually have to update certain aspects, the notebook will go into more detail. Understand, the SPECIFIED jupyter notebook will not be a complete analysis, instead, you are expected to copy and paste code from the ALL jupyter notebook if you wish to follow similar analysis patterns. The biggest concern is not knowing which parquet files cover which portion of the United States. This will require the user to do trial-and-error. Which means the analysis portion of this project may not work for the parquet file you download (i.e., if parquet file doesn't cover Massachusetts but that is what is being analyzed), which is why the SPECIFIED notebook will only give the layout and will require the USER to do the heavy lifting.

IMPORTANT (REPRODUCIBILITY): If you wish to use these functions on different source.coop s3 dataset retreivals, I highly suggest reviewing the SPECIFIED notebook, utils.py SPECIFIED functions and the testing -> get_s3_keys notebook. These can be read through to easily understand the features that are required to grab keys and download associated data.

Additional Note: the 'testing' folder is not crucial at the time this project is posted, however, this dataset is constantly changing. Within just one week of working on this project, the entire dataset went from 3.2 GiBs to 20 GiBs, with different file-naming patterns. Because of reasons such as that, the testing folder/sub-directory will allow users to possibly troubleshoot future issues with the code.
