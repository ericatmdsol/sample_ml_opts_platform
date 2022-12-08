FROM python:3.7
# for independent steps things that rarely change should be 
# higher up in the docker file to take advatnage of caching
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY erics_budget_ml_opts_platform/main.py .
CMD ["python", "main.py"]
