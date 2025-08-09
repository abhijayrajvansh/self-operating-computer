#!/usr/bin/env python3
"""
OpenRouter Integration Example for Self-Operating Computer

This script demonstrates how to use OpenRouter models with the Self-Operating Computer Framework.
"""

import os
import subprocess
import sys

def main():
    print("🤖 Self-Operating Computer - OpenRouter Integration Example")
    print("="*70)
    
    print("\n📖 What is OpenRouter?")
    print("-" * 25)
    print("OpenRouter is a unified API that provides access to multiple AI models")
    print("from different providers (OpenAI, Anthropic, Google, Meta, etc.) through")
    print("a single interface. This allows you to:")
    print("• Compare different models easily")  
    print("• Access the latest models from multiple providers")
    print("• Get competitive pricing")
    print("• Have unified billing and usage tracking")
    
    print("\n🔧 Setup Instructions:")
    print("-" * 20)
    print("1. Visit https://openrouter.ai/ and create an account")
    print("2. Go to the API Keys section and create a new key")
    print("3. Copy your API key (starts with 'sk-or-...')")
    print("4. Run any OpenRouter command below")
    
    print("\n🚀 Available Commands:")
    print("-" * 18)
    
    commands = [
        {
            "name": "Claude 3.5 Sonnet (Recommended)", 
            "cmd": "operate -m openrouter-anthropic/claude-3.5-sonnet",
            "desc": "Latest Claude model, excellent for complex tasks"
        },
        {
            "name": "GPT-4o via OpenRouter",
            "cmd": "operate -m openrouter-openai/gpt-4o", 
            "desc": "OpenAI's flagship model through OpenRouter"
        },
        {
            "name": "Gemini Pro Vision",
            "cmd": "operate -m openrouter-google/gemini-pro-vision",
            "desc": "Google's multimodal model"
        },
        {
            "name": "Llama 3.2 Vision 90B",
            "cmd": "operate -m openrouter-meta-llama/llama-3.2-90b-vision-instruct",
            "desc": "Meta's open-source vision model"
        }
    ]
    
    for i, cmd in enumerate(commands, 1):
        print(f"\n{i}. {cmd['name']}")
        print(f"   Command: {cmd['cmd']}")
        print(f"   Description: {cmd['desc']}")
    
    print("\n🎯 Advanced Usage:")
    print("-" * 15)
    print("• Voice mode: operate -m openrouter-anthropic/claude-3.5-sonnet --voice")
    print("• Verbose mode: operate -m openrouter-openai/gpt-4o --verbose")
    print("• Direct prompt: operate -m openrouter-google/gemini-pro-vision --prompt \"Open Chrome\"")
    
    print("\n💰 Pricing Benefits:")
    print("-" * 17)
    print("• Often cheaper than direct provider APIs")
    print("• Transparent pricing comparison")
    print("• Pay-as-you-go with no minimums")
    print("• Volume discounts available")
    
    print("\n🔍 Model Selection Tips:")
    print("-" * 21)
    print("• Claude 3.5 Sonnet: Best for complex reasoning and coding")
    print("• GPT-4o: Well-balanced, good for most tasks")
    print("• Gemini Pro Vision: Good for image understanding")
    print("• Llama models: Open-source, cost-effective")
    
    print("\n📊 Monitoring Usage:")
    print("-" * 17)
    print("• Check usage at https://openrouter.ai/activity")
    print("• Set spending limits in your OpenRouter dashboard")
    print("• Monitor costs per model")
    
    print("\n" + "="*70)
    print("Ready to get started? Choose a command above and run it!")
    print("Your API key will be requested on first use and saved for future sessions.")
    print("="*70)

if __name__ == "__main__":
    main()
