# Entropy-Aware Preference Alignment for Diffusion-based Text-to-Image Generation

## Acknowledgements
This implementation is based on the codebase provided by [SPO](https://github.com/RockeyCoss/SPO), [D3PO](https://github.com/yk7333/d3po), [Diffusion-DPO](https://github.com/SalesforceAIResearch/DiffusionDPO), [Diffusers](https://github.com/huggingface/diffusers) and [PickScore](https://github.com/yuvalkirstain/PickScore). The public availability of them significantly facilitated our research, and we gratefully acknowledge their authors' contribution.

## :wrench: Training
Please refer to the README.md in the folder "./training"

## :wrench: Example: have a try
Before running the example file, please ensure that you have completed the environment configuration in "./training/environment.yaml".

Due to the size limitations for supplementary materials, we only attach the Lora weights of model training here for your reference, which is available at "./lora_weights.safetensors". 

You can have a try using the following command line:

```bash
python example.py --device "cuda:0" --lora_path "./lora_weights.safetensors" --prompt "morgan freeman, by martine johanna, by Loish, by Greg Rutkowski, strong shadows, by Rossdraws, artgerm, smooth, sharp focus, artstation, Detailed and Intricate, beauty, backlighting" 
```

## Prompts in Figure 1

- a city with a lot of buildings, a detailed matte painting by Jordan Grimmer, cgsociety, fantasy art, artstyle andree wallin, bastien grivet, matte painting of steam machines
  
- steam train driving through the snow , the polar express , scenic landscape , stunning environment , dusk , ultra detailed , octane render , ultra detail , intricate detail , volumetric lighting , vivid colours , photorealistic , photography , lifelike , high resolution , digital art , ultra wide angle lens , aerial view , elevated view , wallpaper

- 3d fluffy pumpkin, Halloween, closeup cute and adorable, cute big circular reflective eyes, Pixar render, unreal engine cinematic smooth, intricate detail, cinematic

- Illustration of a hyperrealistic , otherworldly, ultrasky scene featuring a giant crystal tree full body,very detailed and magical lighting, intricate forest details, vegetation and river around, solarpunk ,landscape, giant tree, beatifull leafy with beautiful lighting and realistic proportions, as if it were a cinematic background, 8k, highest quality, masterpiece, clouds and stars in the sky

- An astronaut on a planet, hyper-realistic environments, 8K resolution, Blender, Octane Render, sci-fi, adventurous, cutting-edge, thrilling, Trippy, Cartoon

- arcane style, Posh girl wearing an open blazer, tie, detailed portrait, cell shaded, 4 k, concept art, by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality
  
- Henry Cavill The Witcher long white hair with beard,  perfect face, perfect eyes, perfect composition, beautiful detailed intricate insanely detailed, trending on artstation, 8 k artistic photography, photorealistic concept art, soft natural volumetric cinematic perfect light, chiaroscuro, oil on canvas, caravaggio, greg rutkowski, Tom Bagshaw and Seb McKinnon , noir
  
- cute fluffy kitten, detailed, in the style of detective pikachu, pixar, ultra sharp focus, bright colours, vibrant multi-colour, 8k, octane render

- Elsa, fantasy, intricate, elegant, highly detailed, digital painting, artstation, concept art, matte, sharp focus, illustration, hearthstone, art by artgerm and greg rutkowski and alphonse mucha, 8k

- elegant girl in urban outfit , cute fine face , rounded eyes , digital painting , fan art , pixiv , by Ilya Kuvshinov , katsuhiro otomo ghost-in-the-shell , magali villeneuve , artgerm , Jeremy Lipkin and Michael Garmash and Rob Rey

- morgan freeman, by martine johanna, by Loish, by Greg Rutkowski, strong shadows, by Rossdraws, artgerm, smooth, sharp focus, artstation, Detailed and Intricate, beauty, backlighting

- A noir-style portrait of a detective, drawn with pen and paper. The image features a strong focus on the character's face, with intricate details of the wrinkles and shadows enhancing the overall mood of the piece. The dynamic pose and angle of the character create a sense of action, with the overall composition reflecting a high-quality, award-winning piece.
