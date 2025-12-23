# SpamBuster
SpamBuster is a machine-learning powered web application that classifies email text as Spam or Ham using OpenAI embeddings and a logistic regression classifier.
The project includes:

* A full machine learning pipeline (model.py)

* A Flask web app (app.py)

* Pre-built Email Embeddings (email_embeddings.py)

* Pre-trained Spam Classifier Model (spam_classifier.pkl)

* Two bash scripts for easy setup and execution (run.sh, run2.sh)

## Requirements

* Python

* pip

* A Unix-like environment (Linux, macOS, WSL, or Git Bash)

* An OpenAI API key (Paste your API key in secrets.env located in the env folder by replacing "PLACE_THE_KEY_HERE")

## How to Run

We trained our spam classifier model (spam_classifier.pkl) and email embeddings (email_embeddings.npy) and put it in this zip, giving the users the option to either use the pre-trained model or build their own model.

To use the pre-trained model, enable execution permission by:

```
chmod +x run2.sh
```

Then, run the script by:


```
./run2.sh
```

When the Flask server starts, you will see a message like:
```
Running on http://127.0.0.1:5000
```

Open that link in your browser to access the SpamBuster web interface.

To build your own model and run it, enable execution permission by:
```
chmod +x run.sh
```

Delete the exisiting model (spam_classifier.pkl) and embeddings (email_embeddings.npy) files:
```
rm spam_classifier.pkl email_embeddings.npy
```



Then, run the script by:

```
./run.sh
```

* **Note**: Generating the embeddings and training the logistic regression model might take anywhere from 45 minutes to 1 hour depending on the performance of your GPU.

When it is done executing, 2 new files will appear:
* spam_classifier.pkl
* email_embeddings.npy

When the Flask server starts, you will see a message like:
```
Running on http://127.0.0.1:5000
```

Open that link in your browser to access the SpamBuster web interface.


