# Miniconda parent image
FROM continuumio/miniconda3:24.7.1-0

# Copy project files
COPY environment.yml /home/environment.yml

# Create a Conda environment with JupyterLab installed
RUN conda env create -f /home/environment.yml

# Activate the Conda environment
RUN echo "conda activate building-footprint-analysis" >> ~/.bashrc
ENV PATH="$PATH:/opt/conda/envs/building-footprint-analysis/bin"

# Create a non-root user and switch to that user
RUN useradd -m gisuser
USER gisuser

# Set the working directory to /home/gisuser
WORKDIR /home/gisuser
COPY utils.py .
COPY basic_analysis.ipynb .

# Expose the JupyterLab port
EXPOSE 8888
# Expost the Dask Dashboard port
EXPOSE 8787

# Start JupyterLab
CMD ["jupyter", "lab", "--ip=0.0.0.0"]
