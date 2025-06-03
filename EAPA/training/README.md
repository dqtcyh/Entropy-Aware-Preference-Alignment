# Entropy-Aware Preference Alignment for Diffusion-based Text-to-Image Generation

## Acknowledgements
This implementation is based on the codebase provided by [SPO](https://github.com/RockeyCoss/SPO), [D3PO](https://github.com/yk7333/d3po), [Diffusion-DPO](https://github.com/SalesforceAIResearch/DiffusionDPO), [Diffusers](https://github.com/huggingface/diffusers) and [PickScore](https://github.com/yuvalkirstain/PickScore). The public availability of them significantly facilitated our research, and we gratefully acknowledge their authors' contribution.

## :wrench: Installation
1. Create the Environment
```bash
cd ./training

conda env create -f environment.yaml
```
2. Login to wandb
```bash
wandb login {Your wandb key}
```
3. (Optional) To customize the location for saving models downloaded from Hugging Face, you can use the following command:
```bash
export HUGGING_FACE_CACHE_DIR=/path/to/your/cache/dir
```

## :wrench: Training
Before fine-tuning, please download [the checkpoints of step-aware preference models](https://huggingface.co/SPO-Diffusion-Models/Step-Aware_Preference_Models/resolve/main/sd-v1-5_step-aware_preference_model.bin) that was introduced in [SPO](https://arxiv.org/abs/2406.04314). You can do this by following these steps:
```bash
sudo apt update
sudo apt install wget

mkdir model_ckpts
cd model_ckpts

wget https://huggingface.co/SPO-Diffusion-Models/Step-Aware_Preference_Models/resolve/main/sd-v1-5_step-aware_preference_model.bin

cd ..
```

Now, you can execute the fine-tuning process using the following command:

```bash
PYTHONPATH=$(pwd) accelerate launch --config_file accelerate_cfg/1m4g_fp16.yaml train_scripts/train_spo.py --config configs/spo_sd-v1-5.py
```

When employing different paradigms for training, you may modify line 593-606 in the "./training/train_scripts/train_spo.py"
