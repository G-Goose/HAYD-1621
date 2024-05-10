
FROM tensorflow/tensorflow:2.10.0

WORKDIR /prod


COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY hayd1621 hayd1621
COPY setup.py setup.py
COPY api api
COPY model model
#RUN pip install .

COPY Makefile Makefile
#RUN make reset_local_files

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT
