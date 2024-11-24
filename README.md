There are 2 parts to this model as explained here and in the demo interface vedio:

1-Light enhancement Model_interface_final is the light enhancement MIRNet model with gradio interface- upload a low light, low quality image from the test datset and obtain an enhanced image-can download from colab

2- Training for resolution enhancement(we have cloned a github repo and file size was too large so uploaded it on drive- https://drive.google.com/drive/folders/1MbECJ9Zou4OjSVePty4UI_Vjk7X1N6B5?usp=drive_link, this contains a .pth trained file at location-\Real-ESRGAN\experiments\finetune_RealESRGANx4plus_400k_pairdata_archived_20241103_193603\models\net_g_latest.pth which needs to be uploaded in the resolution model( this is our fine tuned model)
The \Real-ESRGAN\datasets\DF2K is the location to the few shot learning inputs and resizing (10 pairs of lr and corresponding hr with meta data present in this folder)

3- The Resolution enhancement fine tuned model is in Few_Shot_Learning Folder- enhanced intermediate image from Light_Enhanceemnt model has to be run locally on git_bash as the following:

cd  <path to <few_shot_model >>

streamlit run app.py

This leads to the final interface where the net_g.pth file has to be uploaded (as training mentioned in the drive link attached-https://drive.google.com/file/d/1ptjkaP6cGFuzqcnCbrKAoFxyuG8Y4tfY/view?usp=sharing and the code walktrough vedio)

