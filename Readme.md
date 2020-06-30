# Simple Image Processing Server

A Flask Wrapper for [Pillow](https://pillow.readthedocs.io/en/stable/) with integrated file handling.
Current operations supported:
- Cropping
- Rotation
- Resizing


## Setup

A Dockerfile is provided. Just clone this repository, build an image and run with an image folder mounted:

`docker build -t image-server .`

and

`docker run -d -p 9000:9000 -it --name image-server --mount type=bind,source=/path/to/image/folder/,target=/mnt image-server`


## API
*Example runs on localhost:9000*
### File Upload

You may use the form provided under `GET http://localhost:9000/file`. A non expiring accesstoken is provided inside the HTML as well as an implementation example of uploading a file via fetch. 

### Image Operations

Once you uploaded an image, you will get a json response with the name of the created file. Go to http://localhost:9000/image/your_file_name to see your uploaded image. 

The image can now be manipulated via query parameters:

http://localhost:9000/image/your_file_name?rotation=90&height=320&width=auto&crop=0,50,200,400



