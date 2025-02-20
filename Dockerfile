FROM python:3.9-slim

WORKDIR /app

COPY . .

# Upgrade pip and install dependencies with warning suppression
RUN pip install --upgrade pip --no-warn-script-location --root-user-action=ignore && \
    pip install --no-warn-script-location --root-user-action=ignore -r requirements.txt

# Train the model
RUN python train_model.py

EXPOSE 5000

CMD ["python", "app.py"]
