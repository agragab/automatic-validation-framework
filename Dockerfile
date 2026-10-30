FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN RUN robot --outputdir /tmp/robot --pythonpath . tests/
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]