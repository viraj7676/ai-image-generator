# 🎨 AI Image Generator

A beginner-friendly text-to-image generator using Stable Diffusion. Create stunning images from text descriptions!

![AI Generated Image](https://img.shields.io/badge/AI-Generated-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.9+-green?style=for-the-badge)
![Stable Diffusion](https://img.shields.io/badge/Stable%20Diffusion-1.5-orange?style=for-the-badge)

## ✨ Features

- 🖼️ Generate high-quality images from text prompts
- 🌐 Web interface using Gradio
- ⚡ GPU acceleration support
- 🎯 Customizable generation parameters
- 📁 Automatic image saving with timestamps
- 🔧 Easy-to-use command line interface

## 🚀 Quick Start

### Prerequisites

- Python 3.9 or higher
- NVIDIA GPU (recommended) or CPU
- 8GB+ RAM

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/viraj7676/ai-image-generator.git
   cd ai-image-generator
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Usage

### Command Line Interface

Run the basic generator:
```bash
python basic_generator.py
```

### Web Interface

Launch the web app:
```bash
python web_app.py
```

Then open your browser to `http://localhost:7860`

## 🎯 Example Prompts

Try these example prompts to get started:

- `"a majestic lion in a magical forest, digital art"`
- `"futuristic city skyline at sunset, cyberpunk style"`
- `"cute robot playing with butterflies, cartoon style"`
- `"ancient temple in the mountains, mystical atmosphere"`

## ⚙️ Configuration

### Generation Parameters

- **Steps**: Higher values (20-50) = better quality but slower
- **Guidance Scale**: How closely to follow the prompt (7-15 recommended)
- **Size**: Default 512x512 pixels

### Hardware Requirements

- **Minimum**: 8GB RAM, CPU only
- **Recommended**: 16GB RAM, NVIDIA GPU with 6GB+ VRAM
- **Optimal**: 32GB RAM, NVIDIA RTX 3080 or better

## 📁 Project Structure

```
ai-image-generator/
├── basic_generator.py      # Command line interface
├── web_app.py             # Web interface
├── requirements.txt       # Dependencies
├── README.md             # This file
├── generated_images/     # Output directory (auto-created)
└── venv/                # Virtual environment
```

## 🛠️ Troubleshooting

### Common Issues

**Out of Memory Error**
- Reduce image size or use CPU instead of GPU
- Close other applications to free up RAM

**Slow Generation**
- Enable GPU acceleration
- Reduce number of inference steps

**Model Download Issues**
- Check internet connection
- Ensure sufficient disk space (5GB+ required)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Stability AI](https://stability.ai/) for Stable Diffusion
- [Hugging Face](https://huggingface.co/) for the Diffusers library
- [Gradio](https://gradio.app/) for the web interface



---
## Output 

![Screenshot 2025-06-16 130637](https://github.com/user-attachments/assets/736ef2cd-cf8d-4b26-b55c-3eeda591952a)



