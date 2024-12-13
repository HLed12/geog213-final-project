## Step-by-step guide to running the container

Instead of creating the docker image using the `dockerfile` and `environment.yml` file, you will instead pull the pre-existing image from my personal Docker Hub account (hleduc12).

In your terminal, run the following:
```
docker pull hleduc12/us_structures_analysis:latest
```

After some time, the image will be built. A common error is not having Docker running on your system, ensure it is.

Run the following code to make sure it has been built to your local machine
```
docker images
```
Now we will run the image and create the docker container. Since we want to make new files and be able to access them after the container is closed, we must mount a folder within the environment to the current directory. Make sure you are in your desired directory!

Run the following:
```
docker run -v $(pwd):/home/gisuser/saved -p 8888:8888 -p 8787:8787 hleduc12/us_structures_analysis:latest
```
(pwd) connects your current directory to the container which allows you to save any edits. You can hard-code the file path to a different directory if you desire. However, (pwd) is the suggested approach.
MAKE SURE TO MOVE ANY FILES YOU DESIRE TO SAVE INTO THE 'saved' FOLDER!!

-p 8888:8888 sets your local machine to be connected (or 'talk') with the port 8888 where the container will be running.

Since we are also using a dask client, we must use a second port, hence the -p 8787:8787. This will allow you to see how your computer is handling the computations of the data. After running the chunk regarding Client, you can click the outputted link to see this dask dashboard.
 
Going back to your terminal where you just ran the above code. Copy and paste one of the bottom 3 links into a browser if the container does not automatically open JupyterLab. Click the first kernel.

Now, on the left hand side of the Jupyter interface, you should see the all the files that were used to create this image. Open the analysis_ALL file to review the specific project analysis on Worcester. Open the analysis_SPECIFIED for details on how you can reproduce this approach with another dataset OR location, it also details ways to combat the large file downloads.

Note: the Dockerfile has several COPY lines because the jupyter notebook was fully created before the image/container could successfully run (ran into several bugs). The dockerfile technically should not contain this, and the edits should have been made then re-pushed to the image.
