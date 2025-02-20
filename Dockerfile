FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --upgrade pip && \
    pip install --no-warn-script-location --root-user-action=ignore -r requirements.txt

RUN python train_model.py

EXPOSE 5000

CMD ["python", "app.py"]
