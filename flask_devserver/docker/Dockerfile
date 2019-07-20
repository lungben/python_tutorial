FROM continuumio/miniconda3
COPY environment.yaml .
RUN conda update conda --yes && \
	conda env update -f environment.yaml -n base && \
	conda clean -a

COPY start_server.py .

EXPOSE 5000
VOLUME app

ENTRYPOINT ["python"]
CMD ["start_server.py"]
