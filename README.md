# What Do Compressed Deep Neural Networks Forget?

This Project aims to reproduce the claims of the paper titled "What Do Compressed Deep Neural Networks Forget?" by Sara Hooker, Aaron Courville, Gregory Clark, Yann Dauphin and Andrea Frome. 

![](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/main/assets/Pruning.png)

# Weights and Biases Project Page

Weights and Biases Client were used to conduct all the experiments. You can explore the Project [here](https://wandb.ai/sauravmaheshkar/exploring-bias-and-compression).

# Metrics

## Train Top-1 Accuracy

![](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/main/assets/Acc.png)

## Validation Top-1 Accuracy

![](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/main/assets/Val_Acc.png)

## Training Loss

![](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/main/assets/Loss.png)
# Web Application

You can interact with the web app at this [link](https://share.streamlit.io/sauravmaheshkar/compressed-dnns-forget/web-app/app.py). Some identified PIE's are also available on the website.

![Banner Image](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/web-app/App-Image.png)

# Methods of Pruning

![](https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/blob/main/assets/Methods%20of%20Pruning.png)

# Steps for Reproduction

## Conda Approach

(**After Cloning and switching to the `web-app` branch**)

1. Create the conda environment `conda env create -f environment.yml`
2. Activate the Environment `conda activate compression`
3. Run the Application `streamlit run app.py`

## Docker Approach

```
docker pull docker.pkg.github.com/sauravmaheshkar/compressed-dnns-forget/compression-app:latest
docker run -p 8501:8501 compression-app:latest                                                             
```


# Contribute

If you want to contribute to the project kindly mail me at `sauravvmaheshkar@gmail.com`.

### Step 1
 - **Option 1**
   🍴 Fork it!  
 - **Option 2**
    👯‍♂️ Clone this repo to your local machine using `https://github.com/SauravMaheshkar/Compressed-DNNs-Forget.git`
### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using `https://github.com/SauravMaheshkar/Compressed-DNNs-Forget/compare/`


# License

[![License](http://img.shields.io/:license-mit-blue.svg)](http://doge.mit-license.org)

The data for this project was taken from kaggle datasets. You can find the Large-scale CelebFaces Attributes (CelebA) Dataset [here](http://mmlab.ie.cuhk.edu.hk/projects/CelebA.html).

- Copyright 2020 @[Saurav Maheshkar](https://sauravmaheshkar.github.io/)
- [MIT License](https://opensource.org/licenses/MIT)


# Credits

The inspiration for this readme file came from
- [fvcproductions](https://gist.github.com/fvcproductions/1bfc2d4aecb01a834b46#license)
- [Navendu Pottekkat](https://github.com/navendu-pottekkat/awesome-readme/blob/master/README-template.md)
