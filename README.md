# Manual Installation installation:
```bash
pip install pandas scikit-learn flask numpy
```

# Install from requirements.txt
```bash
pip install -r requirements.txt
```
# Run with Docker commands
```bash
docker build -t sakit .
docker run -it -d --name app -p 5000:5000 sak1t
```
---
# ML Model Development Lifecycle (Test to Deploy)

## Flow:
| Stage                | Description                                      |
|----------------------|--------------------------------------------------|
| Data Collection      | Collect CSV file, clean data                    |
| Model Training       | Train model, evaluate performance               |
| Model Testing        | Test on unseen data                             |
| Save Model           | Save as `model.pkl`                             |
| Integrate Model      | Load in Flask app                               |
| Deploy Locally       | Use Docker (containerize)                       |
| Deploy on Cloud      | Push Docker image to Cloud / EC2                |
| Test in Production   | Validate with real users                        |

