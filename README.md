Geog 213 Advanced Geospatial Analytics w/ Python - Final Project


2020 Census Block Maps and US Structures from Oak Ridge National Laboratory data sets


Purpose:
- Reproducibility. This project will focus on summarizing building data into one US Census block. This will allow others to follow my approach and use for other blocks or future adaptations.
- Analyze the Census block for trends.



## Step-by-step guide to running the container

Instead of creating the docker image using the `dockerfile` and `environment.yml` file, you will instead pull the pre-existing image from my personal Docker Hub account (hleduc12).

In your terminal, run the following:
```
docker pull hleduc12/building-footprint-analysis:latest
```

After some time, the image will be built. A common error is not having Docker running on your system, ensure it is.

Run the following code to make sure it has been built to your local machine
```
docker images
```
Now we will run the image and create the docker container. Since we want to make new files and be able to access them after the container is closed, we must mount a folder within the environment to the current directory. Make sure you are in your desired directory!

Run the following:
```
docker run -v $(pwd):/home/gisuser -p 8888:8888 -p 8787:8787 hleduc12/assignment-7:latest
```
(pwd) connects your current directory to the container which allows you to save any edits. You can hard-code the file path to a different directory if you desire. However, (pwd) is the suggested approach.

-p 8888:8888 sets your local machine to be connected (or 'talk') with the port 8888 where the container will be running.

Since we are also using a dask client, we must use a second port, hence the -p 8787:8787. This will allow you to see how your computer is handling the computations of the data. After running the chunk regarding Client, you can click the outputted link to see this dask dashboard.
 
Going back to your terminal where you just ran the above code. Copy and paste one of the bottom 3 links into a browser if the container does not automatically open JupyterLab. Click the first kernel.

Now, on the left hand side of the Jupyter interface, you should see the Dockerfile, environment.yml, utils.py, and README.md that were used to create this image. Additionally, you will see the 'building_analysis' file. Open it to see the analysis.

Note: the Dockerfile has a 'copy building_analysis .' and 'copy utils.py .' portion because the jupyter notebook was fully created before the image/container could successfully run (ran into several bugs). The dockerfile technically should not contain this, and the edits should have been made then re-pushed to the image.
