# SPC
Scenario Potentiality-Constrain Network for RGB-D Salient Object Detection

## Attention!!!
It is recommended to reproduce our code in the Linux system. 

If you want to run the test.py in Windows, please make sure that the path where you save the test results exists.

## Experimental environment 

python==3.7.0

pytorch==1.8.0

torchvision==0.9.0

tensorboardX==2.5

opencv-python==4.5.5.64

## Training
The training code will coming soon ...

## Testing
If you would like to reproduce our results, please follow these steps.

1. We provide a link to download the parameters of the trained model [code:0617][https://pan.baidu.com/s/1ZsddhG5dm6PHByvzaUSS0w](https://pan.baidu.com/s/11JUyWNfMqGT5ygCQKFuxbg).

2. Place the parametric model under the './best/modal/' path.

3. Open terminal. run：python3 test.py

4. We also provide links to download the results of our experiments [code:0617] https://pan.baidu.com/s/14NemZ9E5_htkckmKwVfPhQ. 

## Evaluation
If you would like to evaluate our entire model parameters through quantitative metrics, please follow these steps.

1. Download the results of our experiments and place them in any path.

2. The evaluation metric code has been placed in the eval_code folder, please use MATLAB to open it.

3. Modify the path to the dataset in main.m.

4. run main.m.

