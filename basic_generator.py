"""
Basic Image Generator using Stable Diffusion
A beginner-friendly script for text-to-image generation
"""

import torch
from diffusers import StableDiffusionPipeline
from datetime import datetime
import os

class ImageGenerator:
    def __init__(self):
        """Initialize the image generator"""
        print("🚀 Starting Image Generator...")
        print("📦 Loading Stable Diffusion model (this may take a few minutes first time)...")
        
        # Create output directory
        self.output_dir = "generated_images"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        
        # Load the model
        model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            safety_checker=None,  # Disable for faster loading
            requires_safety_checker=False
        )
        
        # Use GPU if available
        if torch.cuda.is_available():
            self.pipe = self.pipe.to("cuda")
            print("✅ Using GPU for faster generation")
        else:
            print("⚠️ Using CPU (will be slower)")
        
        print("✅ Model loaded successfully!")
    
    def generate_image(self, prompt, num_images=1, steps=20, guidance_scale=7.5):
        """
        Generate images from text prompt
        
        Args:
            prompt (str): Text description of the image
            num_images (int): Number of images to generate
            steps (int): Number of denoising steps (higher = better quality)
            guidance_scale (float): How closely to follow the prompt
        """
        print(f"🎨 Generating {num_images} image(s) for: '{prompt}'")
        
        try:
            # Generate images
            with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
                result = self.pipe(
                    prompt,
                    num_images_per_prompt=num_images,
                    num_inference_steps=steps,
                    guidance_scale=guidance_scale,
                    height=512,
                    width=512
                )
            
            images = result.images
            
            # Save images
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            saved_files = []
            
            for i, image in enumerate(images):
                filename = f"img_{timestamp}_{i+1:02d}.png"
                filepath = os.path.join(self.output_dir, filename)
                image.save(filepath)
                saved_files.append(filepath)
                print(f"💾 Saved: {filepath}")
            
            return images, saved_files
            
        except Exception as e:
            print(f"❌ Error generating image: {e}")
            return None, None

def main():
    """Main function to run the image generator"""
    print("=" * 50)
    print("🎯 AI Image Generator")
    print("=" * 50)
    
    # Initialize generator
    try:
        generator = ImageGenerator()
    except Exception as e:
        print(f"❌ Failed to initialize generator: {e}")
        return
    
    # Interactive loop
    while True:
        print("\n" + "-" * 30)
        prompt = input("Enter your image prompt (or 'quit' to exit): ").strip()
        
        if prompt.lower() in ['quit', 'exit', 'q']:
            print("👋 Goodbye!")
            break
        
        if not prompt:
            print("⚠️ Please enter a valid prompt")
            continue
        
        # Ask for number of images
        try:
            num_imgs = input("Number of images (default 1): ").strip()
            num_imgs = int(num_imgs) if num_imgs else 1
            if num_imgs < 1 or num_imgs > 4:
                print("⚠️ Using default: 1 image")
                num_imgs = 1
        except ValueError:
            num_imgs = 1
        
        # Generate images
        images, files = generator.generate_image(prompt, num_imgs)
        
        if images:
            print(f"✅ Successfully generated {len(images)} image(s)!")
            print(f"📁 Check the '{generator.output_dir}' folder")
        else:
            print("❌ Failed to generate images")

if __name__ == "__main__":
    main()