# object_tracking
   Implementation of object tracking apps based on yolov4 and custom tracking algorithm.

# Run the app

   Navigate to object_tracking/ directory and run the following code.

    $ python main.py

# Architecture

    object_tracking/
    ├── main.py
    ├── Pipfile
    ├── README.md
    └── source_code
        ├── dnn_model
        │   ├── classes.txt               # gitignore
        │   ├── yolov4.cfg                # gitignore
        │   └── yolov4.weights            # gitignore
        ├── los_angeles.mp4               # gitignore
        ├── object_detection.py
        ├── object_tracking.py
        └── __pycache__
            └── object_detection.cpython-38.pyc