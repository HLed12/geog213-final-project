Geog 213 Advanced Geospatial Analytics w/ Python - Final Project

US Structures from Oak Ridge National Laboratory data set


Purpose:
- Reproducibility: This project offers different methods for users to install the US Structures dataset, in case the total size cannot be stored. Additionally, it provides users with a walkthrough on grabbing any source.coop dataset through the AWS S3 link (focused on geoparquet data but can easily be altered).
- Advise users on possible errors/concerns associated with not installing the entire dataset. While still providing an example analysis.
- Investigate the US Structure dataset integrity. Showing users how to specify a location within the dataset columns or using a shapefile. Comparing the two results.
- Although computational limits are present, show users different ways to filter the dataset for analysis and provide plotting examples.
* This project has a lot of opportunities for fine-tuning and future additions.

First Steps:
- Open the customization_advice.ipynb file and read through it to gather an overall understanding of the download process and data.
- Next, open the main_analysis.ipynb file and examine possible issues, advice, and initial analyses.


Understanding the install process:
There are 2 ways to approach doing this work. Downloading all of the dataset (main_analysis) or downloading sections of it (customization_advice).

To see how a user can: 
- 1. Download a different dataset
- 2. Learn what needs to be changed in the utils.py file IF the source.coop dataset changes
- 3. Not install ALL of the data files, plus possible issues this could raise.

Then focus on the customization_advice.ipynb. Bullet 2 can also review the 'testing' folder.

No matter what, you should still review both jupyter notebooks. There will be outputs and plenty of resourceful information in both.

At this point, you may be asking yourself, 'Why would I want to install only some of the data?'...

This dataset is always changing, there is a chance the data will be too large for users to download. Currently, 12/8/2024, all the parquet files require ~20 GiBs of space. However, one week prior, it was only ~3.2 GiBs. 
To review if this has changed, check the following site:
https://source.coop/wherobots/usa-structures/geoparquet


Understand, the 'customization_advice' jupyter notebook will not be an analysis. You will need to refer to the 'main_analysis' if you wish to follow similar analysis patterns. The biggest concern for partial install is if the user has a desired area in mind. At this time, it is not possible to tell which portion of the United States is covered by each parquet file. This will require the user to do trial-and-error. However, if the user isn't deadset on a location, they can install one or two parquet files and plot based on partitions to start their analysis.



Additional Note: the 'testing' folder is not crucial at the time this project is posted, however, this dataset size and file-naming patterns changed from an update. The testing folder will allow users to possibly troubleshoot future issues from future updates.

The Shapefile data for Worcester is included in the image to avoid confusion.
