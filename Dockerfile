FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN robot test.robot
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]