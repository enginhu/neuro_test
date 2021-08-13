## Virtual Environment Instructions

To run the application, first you need to create a virtual environment. 
```
python -m venv venv
```

Then activate the environment and install required packages with pip.
```
source venv/bin/activate
pip install - r requirements.txt
```

After a successful install of packages to run the application just run `neuro_app.py` with
```
python neuro_app.py
```

Now you can access the application in your browser by visiting http://127.0.0.1:5000.

## Docker Container  Instructions

First you need to build the docker image.
```
docker build -t neuro:latest .
```

After building the image you can run the container with the image
```
docker run -p 8000:3000 neuro:latest
```
Now you can access the application in your browser by visiting http://127.0.0.1:8000.

You can also add -d parameter to run the docker container in background and use the docker image id to specify the image. To get the ID of image run `docker images` command.

```
docker images

REPOSITORY         TAG       IMAGE ID       CREATED         SIZE
neuro              latest    12b39eb81589   45 minutes ago   160MB


docker run -d -p 8000:3000 12b39eb81589
```

The functions are stored in `app/calculate_distance/routes.py` file.