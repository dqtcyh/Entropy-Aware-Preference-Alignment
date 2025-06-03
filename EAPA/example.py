import os
import torch
import argparse
from pathlib import Path
from diffusers import StableDiffusionPipeline
from contextlib import nullcontext

def parse_args():
    parser = argparse.ArgumentParser(description="EAPA generation")
    parser.add_argument("--device", type=str, default="cuda:0", help="GPU device to use")
    parser.add_argument("--model", type=str, default="runwayml/stable-diffusion-v1-5", help="Base model to use")
    parser.add_argument("--lora_path", type=str, required=True, help="Path to LoRA weights")
    parser.add_argument("--prompt", type=str, required=True, help="Prompt for image generation")
    parser.add_argument("--output_dir", type=str, default="./outputs", help="Directory to save generated images")
    parser.add_argument("--guidance_scale", type=float, default=6.0, help="Guidance scale for stable diffusion")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")
    parser.add_argument("--precision", type=str, choices=["float16", "float32"], default="float16", help="Precision for model inference")
    return parser.parse_args()

def setup_pipeline(args):
    # Set device for CUDA
    if args.device.startswith("cuda"):
        cuda_id = args.device.split(":")[-1]
        os.environ["CUDA_VISIBLE_DEVICES"] = cuda_id
    
    # Setup dtype based on precision argument
    inference_dtype = torch.float16 if args.precision == "float16" else torch.float32
    
    # Get cache directory from environment
    huggingface_cache_dir = os.environ.get('HUGGING_FACE_CACHE_DIR', None)
    
    # Create pipeline with error handling
    try:
        pipe = StableDiffusionPipeline.from_pretrained(
            args.model,
            torch_dtype=inference_dtype,
            cache_dir=huggingface_cache_dir,
        )
        
        # Load LoRA weights
        pipe.load_lora_weights(args.lora_path)
        
        
        # Move to device
        pipe = pipe.to(args.device)
        
        return pipe
    except Exception as e:
        print(f"Error setting up pipeline: {e}")
        raise

def generate_image(pipe, args):
    # Create output directory if it doesn't exist
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Setup generator with seed
    device = args.device
    generator = torch.Generator(device=device)
    generator = generator.manual_seed(args.seed)
    
    # Generate image with autocast for efficiency when using float16
    autocast = torch.cuda.amp.autocast if args.precision == "float16" else nullcontext
    
    try:
        with autocast():
            result = pipe(
                prompt=args.prompt,
                generator=generator,
                guidance_scale=args.guidance_scale
            )
        
        # Save image
        image = result.images[0]
        output_path = output_dir / f"generation_seed_{args.seed}.png"
        image.save(output_path)
        print(f"Image saved to {output_path}")
        
        return image
    except Exception as e:
        print(f"Error generating image: {e}")
        raise

def main():
    args = parse_args()
    pipe = setup_pipeline(args)
    
    # Free up VRAM before generation
    torch.cuda.empty_cache()
    
    image = generate_image(pipe, args)
    
    # Free VRAM after generation
    del pipe
    torch.cuda.empty_cache()

if __name__ == "__main__":
    main()