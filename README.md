# SWC_Capstone_Design
Decentralized Brain Age Estimation using MRI Data

## Dataset
Human Cunnectome Projects(HCP) Young Adults Diffusion MRI
- Number : 1065
- Age : 22 ~ 35
- Diffusion Matrix : FA

## Timeline
- 2022.03
    - 주제선정
    - 계획서 제출
    - 논문 읽기

- 2022.04
    - 데이터 이해: Diffusion MRI  
        Youtube: https://www.youtube.com/playlist?list=PLRZ9VSqV-6soOC0rUEAOV-QiSa_Qxk8JM
    - DSI Studio를 이용한 data export
        auto_dti_fa.py를 통해서 dMRI에서 FA map export
    - Data Slicing
    - 모델 구현

- 2022.05
    - 모델 Training
    - 결과 시각화

- 2022.06
    - 결과 제출


## 1. 과제개요
의료데이터를 활용한 머신러닝 모델 개발의 경우 데이터의 수집 및 활용에 있어서 개인정보 보호 및 규제로 인해 어려움을 겪고 있다. 이에 대해서 Federated Learning은 데이터를 직접 수집하지 않아 이 문제로부터 자유로우며 머신러닝의 성능에 있어서도 우수하여 이 문제에 대한 해결책으로 제시되었다. 따라서 이에 대해서 의료데이터를 활용한 모델의 성능향상 및 시험과정이 필요하다. 많은 의료데이터 중 뇌연령은 알츠하이머, 파킨슨병과 같은 뇌질환과 관련하여 Biomarker로 사용될 수 있어서 딥러닝과 접목될 경우 정확도를 높일 수 있어 진단에 활용될 수 있다. 따라서 이를 MRI 데이터를 활용하여 모델의 성능을 높이고자 하는 노력이 이어지고 있다. 이때 주로 사용되는 데이터는fMRI 또는 structural MRI이다. MRI는 종류가 많은데, 이 중 fMRI의 경우 혈류와 관련된 변화를 감지해 뇌연령 예측에 있어서 중요한 정보를 제공하고 structural MRI의 경우 뇌의 구조를 이용하여 유의미한 정보를 제공한다. 하지만 dMRI 또한 뇌연령 예측에 있어서 유의미한 feature를 찾아낼 수 있어이에 대해서 활용해보고자 한다.

## 2. 수행과정
### 1) dMRI 
- 데이터 수집 : 1mm & 2mm
- 데이터 Export : fib → nii map (Diffusion Matrix: FA)
- Data Explore : DataGenerator.ipynb
- Data Slicing : DataSlicing.py

### 2) Global-Local Transformter for Brain Age Estimation
모델코드는 논문에서 제공되는 것을 활용하였다.   
- Dataloader을 이용한 Train, Validation, Test로 데이터 분리
- Train 코드를 작성하여 이에 대해서 수행함
    - Baseline : Vgg8
    - Hyper Parameter : N_block, Thans head, Drop rate
- Test 코드를 작성하여 모델 Testing 진행
- Best model select


### 3) Federated Learning 
(추후 진행 계획 중)

## 3. 수행결과 

### 1) dMRI train
![image](https://user-images.githubusercontent.com/51522587/174273595-ffd4deee-8b41-4a93-94ce-9eef85631767.png)
![image](https://user-images.githubusercontent.com/51522587/174273640-0666972f-cf49-408f-ab2d-d4fb91e18109.png)
![image](https://user-images.githubusercontent.com/51522587/174273666-d7fa8520-9abd-486d-b16a-42e01c6aac52.png)


