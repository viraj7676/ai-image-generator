"""
Web Interface for Image Generator using Gradio
Run this to get a user-friendly web interface
"""

import gradio as gr
import torch
from diffusers import StableDiffusionPipeline
import os

class WebImageGenerator:
    def __init__(self):
        """Initialize the web image generator"""
        print("Loading Stable Diffusion model...")
        
        model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            safety_checker=None,
            requires_safety_checker=False
        )
        
        if torch.cuda.is_available():
            self.pipe = self.pipe.to("cuda")
            print("Using GPU")
        else:
            print("Using CPU")
    
    def generate_image(self, prompt, num_steps, guidance_scale):
        """Generate image for web interface"""
        if not prompt.strip():
            return None, "Please enter a prompt"
        
        try:
            with torch.autocast("cuda" if torch.cuda.is_available() else "cpu"):
                result = self.pipe(
                    prompt,
                    num_inference_steps=int(num_steps),
                    guidance_scale=guidance_scale,
                    height=512,
                    width=512
                )
            
            image = result.images[0]
            return image, f"Generated: {prompt}"
            
        except Exception as e:
            return None, f"Error: {str(e)}"

def create_web_app():
    """Create and launch the web application"""
    generator = WebImageGenerator()
    
    def generate_wrapper(prompt, steps, guidance):
        return generator.generate_image(prompt, steps, guidance)
    
    # Create Gradio interface
    with gr.Blocks(title="AI Image Generator", theme=gr.themes.Soft()) as app:
        gr.Markdown("# 🎨 AI Image Generator")
        gr.Markdown("Generate images from text descriptions using Stable Diffusion")
        
        with gr.Row():
            with gr.Column():
                prompt_input = gr.Textbox(
                    label="Image Prompt",
                    placeholder="e.g., a beautiful sunset over mountains, digital art",
                    lines=3
                )
                
                with gr.Row():
                    steps_slider = gr.Slider(
                        minimum=10,
                        maximum=50,
                        value=20,
                        step=1,
                        label="Quality Steps (higher = better quality, slower)"
                    )
                    
                    guidance_slider = gr.Slider(
                        minimum=1,
                        maximum=20,
                        value=7.5,
                        step=0.5,
                        label="Guidance Scale (how closely to follow prompt)"
                    )
                
                generate_btn = gr.Button("🚀 Generate Image", variant="primary")
                
            with gr.Column():
                output_image = gr.Image(label="Generated Image")
                output_text = gr.Textbox(label="Status")
        
        # Example prompts
        gr.Markdown("### 💡 Example Prompts:")
        examples = [
            "a majestic lion in a magical forest, digital art",
            "futuristic city skyline at sunset, cyberpunk style",
            "cute robot playing with butterflies, cartoon style",
            "ancient temple in the mountains, mystical atmosphere"
        ]
        
        example_buttons = []
        for example in examples:
            btn = gr.Button(example, size="sm")
            btn.click(lambda x=example: x, outputs=prompt_input)
        
        # Connect the generate button
        generate_btn.click(
            fn=generate_wrapper,
            inputs=[prompt_input, steps_slider, guidance_slider],
            outputs=[output_image, output_text]
        )
    
    return app

if __name__ == "__main__":
    print("Starting web application...")
    app = create_web_app()
    app.launch(
        share=True,  # Creates public link
        server_name="0.0.0.0",
        server_port=7860
    )