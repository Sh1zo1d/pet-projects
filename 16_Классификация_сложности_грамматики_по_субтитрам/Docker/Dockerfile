FROM python
RUN mkdir /nlp_streamlit
WORKDIR /nlp_streamlit 
COPY ./requirements.txt . 
COPY ./app.py  .
COPY ./lr_model.pkl .
COPY ./rfc_model.pkl .
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8501
CMD  ["streamlit","run","/nlp_streamlit/app.py"]
ENTRYPOINT ["streamlit","run","/nlp_streamlit/app.py"]