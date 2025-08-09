# Self-Operating Computer - OpenRouter Integration Guide

## 🏗️ Architecture Overview

The **Self-Operating Computer Framework** is a revolutionary multimodal AI system that can autonomously control your computer by viewing the screen and performing actions like a human would.

### Core Components:

1. **Entry Point** (`main.py`): Handles command-line arguments and model selection
2. **Main Controller** (`operate.py`): Core execution loop that orchestrates the entire process
3. **Model Interface** (`models/apis.py`): Contains implementations for different AI providers
4. **Configuration** (`config.py`): Manages API keys and client initialization
5. **Utilities**: Screenshot capture, OCR, operating system interactions

### 🔄 End-to-End Flow:

```
User Input (Objective) 
    ↓
Screenshot Capture (with cursor)
    ↓ 
Vision Model Processing (AI analyzes screen + objective)
    ↓
Action Planning (AI returns JSON operations)
    ↓
Action Execution (Mouse/keyboard automation)
    ↓
Loop until complete (max 10 iterations)
```

### 🎯 Action Types:
- **`click`**: Mouse clicks at specified coordinates (percentage-based)
- **`write`**: Keyboard text input  
- **`press`**: Hotkey combinations (Cmd+Space, Enter, etc.)
- **`done`**: Task completion signal with summary

## 🚀 OpenRouter Integration

### What We Added:

1. **Config Support** (`config.py`):
   - Added `openrouter_api_key` attribute
   - Added `initialize_openrouter()` method  
   - Added API key validation for OpenRouter models
   - Added OpenRouter API key prompt and save functionality

2. **API Implementation** (`models/apis.py`):
   - Added `call_openrouter_with_ocr()` function
   - Added model routing for `openrouter-*` models
   - Integrated with existing screenshot and OCR pipeline
   - Added error handling and retry logic

3. **CLI Enhancement** (`main.py`):
   - Updated help text to include OpenRouter examples
   - Support for `openrouter-{provider}/{model}` format

4. **Documentation** (`README.md`):
   - Added comprehensive OpenRouter section
   - Listed popular models and usage examples
   - Explained benefits and setup instructions

### 🔧 How to Use OpenRouter:

#### 1. Get API Key
- Visit https://openrouter.ai/
- Create account and generate API key
- Key format: `sk-or-v1-...`

#### 2. Run with OpenRouter Models
```bash
# Claude 3.5 Sonnet (Recommended)
operate -m openrouter-anthropic/claude-3.5-sonnet

# GPT-4o via OpenRouter  
operate -m openrouter-openai/gpt-4o

# Gemini Pro Vision
operate -m openrouter-google/gemini-pro-vision

# Meta Llama Vision
operate -m openrouter-meta-llama/llama-3.2-90b-vision-instruct
```

#### 3. Advanced Usage
```bash
# With voice input
operate -m openrouter-anthropic/claude-3.5-sonnet --voice

# With verbose logging
operate -m openrouter-openai/gpt-4o --verbose

# Direct prompt
operate -m openrouter-google/gemini-pro-vision --prompt "Open a web browser"
```

### 🎯 Benefits of OpenRouter:

1. **Multiple Providers**: Access models from OpenAI, Anthropic, Google, Meta through one API
2. **Cost Effective**: Often cheaper than direct provider APIs  
3. **Latest Models**: Quick access to newest models across providers
4. **Unified Billing**: Single dashboard for usage tracking and billing
5. **Easy Comparison**: Test different models with same interface

### 📊 Model Recommendations:

- **Claude 3.5 Sonnet**: Best for complex reasoning, coding, detailed analysis
- **GPT-4o**: Well-balanced, reliable for most computer operation tasks
- **Gemini Pro Vision**: Strong image understanding, good for visual tasks
- **Llama 3.2 Vision**: Open-source option, cost-effective for simple tasks

## 🔍 Technical Implementation Details

### Model Routing Logic:
```python
if model.startswith("openrouter-"):
    operation = await call_openrouter_with_ocr(messages, objective, model)
    return operation, None
```

### API Client Initialization:
```python
def initialize_openrouter(self):
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )
    return client
```

### Model Name Processing:
```python
# Extract actual model name (remove "openrouter-" prefix)
actual_model = model.replace("openrouter-", "")
```

### Vision Message Format:
```python
vision_message = {
    "role": "user",
    "content": [
        {"type": "text", "text": user_prompt},
        {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{img_base64}"}},
    ],
}
```

## 🚀 Getting Started

1. **Clone/Update the project** with OpenRouter integration
2. **Install dependencies**: `pip install -r requirements.txt`
3. **Get OpenRouter API key** from https://openrouter.ai/
4. **Run a command**: `operate -m openrouter-anthropic/claude-3.5-sonnet`
5. **Enter API key** when prompted (saved for future use)
6. **Give your objective** and watch the AI control your computer!

## 📝 Files Modified

- `operate/config.py`: Added OpenRouter configuration support
- `operate/models/apis.py`: Added OpenRouter API implementation  
- `operate/main.py`: Enhanced CLI help text
- `README.md`: Added comprehensive documentation
- `validate_openrouter.py`: Validation script (new)
- `openrouter_example.py`: Usage examples (new)

The integration is complete and ready to use! 🎉
