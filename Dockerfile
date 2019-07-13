FROM seblucas/alpine-python3:3.7
ADD line.py /fibonacci/
RUN pip3 install flask
CMD python3 line.py
WORKDIR /fibonacci