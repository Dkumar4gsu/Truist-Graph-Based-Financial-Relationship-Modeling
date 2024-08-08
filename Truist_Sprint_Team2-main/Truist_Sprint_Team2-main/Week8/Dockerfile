FROM jupyter/datascience-notebook

RUN pip install -U pip
RUN pip install jupyterlab neo4j py2neo

ENV JUPYTER_ENABLE_LAB=yes JUPYTER_TOKEN=docker

# COPY --chown=${NB_UID}:${NB_GID} . /home/truist_proj
COPY . /home/truist_proj
WORKDIR /home/truist_proj

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--notebook-dir=/home/truist_proj", "--allow-root"]