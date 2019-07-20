FROM continuumio/miniconda3
COPY environment.yaml .
RUN conda update conda --yes && \
	conda env update --file environment.yaml && \
	conda clean -a && \
	echo "source activate flask_env" > ~/.bashrc 
ENV PATH /opt/conda/envs/env/bin:$PATH VOLUME app EXPOSE 5000

WORKDIR app

ENTRYPOINT ["python"]
CMD ["start_server.py"]
