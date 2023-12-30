# COBOL to Python conversion using GenAI

![Process Diagram](docs/assets/GenAI%20COBOL%20Converter.png)

## Project setup

Create python virtual environment and activate
```
> python -m venv .venv
> .venv/Scripts/activate 
```

Install Python packages
```
(.venv) > pip install -r requirements.txt
```

Create .env file copy from .env_local and add openai & google api key

## Run Conversion pipeline

***playbook.yml*** provides GenAI provider settings and source COBOL artifacts
Execute the below command to start the execution
```
> python -m cob2py_app.main playbook.yml
```