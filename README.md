
# TTool-AI

🌲 TTool-AI is developed at the [**Laboratory for Timber Construction**](https://www.epfl.ch/labs/ibois/) (director: Prof.Yves Weinand) with the support of the [**EPFL Center for Imaging**](https://imaging.epfl.ch/), at [**EPFL**](https://www.epfl.ch/en/), Lausanne, Switzerland. The project is part of the [**Augmented Carpentry Research**](https://www.epfl.ch/labs/ibois/augmented-carpentry/).


🤖 TTool-AI automates the integration of new tools into AC (Augmented Carpentry), enhancing efficiency and simplifying the process. It is developed in Python and relies on the [**FastAPI**](https://fastapi.tiangolo.com/) framework. The project is containerized with [**Docker**](https://www.docker.com/) and [**Docker Compose**](https://docs.docker.com/compose/). The Training Service is based on [**PyTorch**](https://pytorch.org/). The project is developed and tested on Linux (Ubuntu 22.04) with NVIDIA GPUs.


🚀 For a quick hands-on start or more details, check out our [Wiki](https://github.com/ibois-epfl/TTool-ai/wiki).

## System dependencies

1. **Install Docker and Docker Compose**:

    Ensure you have Docker and Docker Compose installed on your system with NVIDIA Runtime support for the Training Service.

2. **Environment Variables**:
    TTool-AI relies on environment variables defined in a .env file. 
    Make sure to set up this file as per the project's requirements.


## Getting Started

### Clone the repository:

```bash
git clone git@github.com:ibois-epfl/TTool-ai.git
```

### Run the project:

Navigate to the project's root directory and run the following command:
```bash
cd TTool-ai/
```
Run Docker Compose to build the project in the background:
```bash
docker-compose up -d
```
Run Docker Compose to build the project in the foreground:
```bash
docker-compose up
```
   
### Check the status of the containers:

```bash
docker-compose ps -a
```
### Access the Service:
Once everything is up and running, you can access the FastAPI interface at:
```bash
http://localhost:16666/docs
```


