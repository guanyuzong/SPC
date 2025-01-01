# SPC
Scenario Potentiality-Constrain Network for RGB-D Salient Object Detection 
![3-eps-converted-to_page-0001](https://github.com/user-attachments/assets/161439b6-547a-44ff-8f68-517af812b521)
```bibtex
@article{CAVER-TIP2023,
  author={Pang, Youwei and Zhao, Xiaoqi and Zhang, Lihe and Lu, Huchuan},
  journal={IEEE Transactions on Image Processing},
  title={CAVER: Cross-Modal View-Mixed Transformer for Bi-Modal Salient Object Detection},
  year={2023},
  volume={},
  number={},
  pages={1-1},
  doi={10.1109/TIP.2023.3234702}
}
```bibtex
## The module's parameter count and computational load
![image](https://github.com/user-attachments/assets/06efd1a1-6c87-4043-ad23-14f8c5dd3fa2)

We introduce two metrics: FLOPs (Floating Point Operations, in G) and Params (the total number of trainable parameters, in M). FLOPs measure the computational complexity of a module during a forward propagation, while Params reflect the total number of parameters in the module.

1.	The CDM module infers the confidence of depth images through the combination of fully connected layers, without involving a large feature extraction network, has a relatively low parameter count and computational load (FLOPs: 0.002G; Params: 2.229M)

2.	The computational complexity of the SPC and MFR modules is higher, mainly due to two factors: 1) these modules are used multiple times throughout the network, and 2) at higher resolution levels, the computational complexity of SPC and MFR increases significantly as the resolution of the input feature maps rises.

3.  The MF module generates the final prediction by integrating multi-modal features through the introduction of depth map confidence g. Its network architecture is relatively simple, with lower parameter count and computational complexity (FLOPs: 4.836G; Params: 1.181M).

run： python3 Params.py
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

1. Complete the experimental environment setup as described above.

2. Download the dataset and place it in the data folder [0617] https://pan.baidu.com/s/1L9l1p9WS2T0lh-ZOvkMKJQ].

3. We provide a link to download the parameters of the trained model [code:0617] [https://pan.baidu.com/s/1nmcqa18cc5pbcRA76KhH9g?pwd=0617].

4. Place the parametric model under the './best/modal/' path.

5. Open terminal. run：python3 test.py

6. We also provide links to download the results of our experiments [code:0617] https://pan.baidu.com/s/14NemZ9E5_htkckmKwVfPhQ. 

## Evaluation
If you would like to evaluate our entire model parameters through quantitative metrics, please follow these steps.

1. Download the results of our experiments and place them in any path.

2. The evaluation metric code has been placed in the eval_code folder, please use MATLAB to open it.

3. Modify the path to the dataset in main.m.

4. run main.m.

