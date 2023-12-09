# YOLOv8-pretrained object detection MODEL TESTING

This testing is referenced from the keras's documentation. Pre-trained Model : https://keras.io/guides/keras_cv/object_detection_keras_cv/

If you wanna build custom datasets's training, you can reference this link : https://keras.io/examples/vision/yolov8/
<br>

## To use as Testing data 
- I downloaded one youtube video . 
- Then , extract the frames from the videos. 
 ```sh
  python framesProduce.py
  ```

## Detection 
- I have tested on the GOOGLE COLAB.
 ```sh
  detection.ipynb
  ```

## Create FOLDER
- There must be two folder " Output " and " TestData "
1. Output folder will be empty ( to save the ouput's result)
2. TestData ( extracted images must be in the TestData )

