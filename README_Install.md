## Step-by-step guide to running the container

Instead of creating the docker image using the `dockerfile` and `environment.yml` file, you may pull the pre-existing image from my personal Docker Hub account (hleduc12).

In your terminal, run the following:
```
docker pull hleduc12/us_structures_analysis:latest
```

After some time, the image will be built. A common error is not having Docker running on your system, ensure it is.

Run the following code to make sure it has been built to your local machine
```
docker images
```
Now we will run the image and create a docker container. Since we want to edit files and be able to access them after the container is closed, we must mount a folder within the environment to your current local directory. Make sure you are in your desired directory. It is best practice to make a separate directory folder for this docker image. Each time you wish to run the container, make sure to CD into the same directory that you made the first time.

Run the following:
```
docker run -v $(pwd):/home/gisuser/saved -p 8888:8888 -p 8787:8787 hleduc12/us_structures_analysis:latest
```
(pwd) connects your current directory to the container which allows you to save any edits. You can hard-code the file path to a different directory if you desire. However, (pwd) is the suggested approach.
MAKE SURE TO MOVE ANY FILES YOU DESIRE TO SAVE INTO THE 'saved' FOLDER!! Additionally, if you do not wish to mount a folder, delete '/saved' from the above code run.

-p 8888:8888 sets your local machine to be connected (or 'talk') with the port 8888 where the container/JupyterLab will be running.

Since we are also using a dask client, we must use a second port, hence the -p 8787:8787. This will allow you to see how your computer is handling the computations of the data. After running the chunk regarding Client, you can click the outputted link to see this dask dashboard.
 
Going back to your terminal where you just ran the above code. Copy and paste one of the bottom 3 links into a browser if the container does not automatically open JupyterLab. Click the first kernel.

Now, on the left hand side of the Jupyter interface, you should see the all the files that were used to create this image. Remember to move desired files to the 'saved' folder if you make edits you wish to keep//access on your local machine.