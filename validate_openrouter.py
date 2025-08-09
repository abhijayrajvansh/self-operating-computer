#!/usr/bin/env python3
"""
Simple validation script for OpenRouter integration
"""

import os
import sys

def test_config_file():
    """Test that config.py has been properly modified"""
    print("Testing config.py modifications...")
    
    config_path = os.path.join(os.path.dirname(__file__), 'operate', 'config.py')
    
    with open(config_path, 'r') as f:
        content = f.read()
    
    # Check for OpenRouter-related code
    checks = [
        'self.openrouter_api_key',
        'def initialize_openrouter',
        'OPENROUTER_API_KEY',
        'openrouter.ai/api/v1'
    ]
    
    for check in checks:
        if check in content:
            print(f"✓ Found: {check}")
        else:
            print(f"✗ Missing: {check}")
            return False
    
    print("✅ Config file modifications look good!")
    return True

def test_apis_file():
    """Test that apis.py has been properly modified"""
    print("\nTesting apis.py modifications...")
    
    apis_path = os.path.join(os.path.dirname(__file__), 'operate', 'models', 'apis.py')
    
    with open(apis_path, 'r') as f:
        content = f.read()
    
    # Check for OpenRouter-related code
    checks = [
        'openrouter-',
        'call_openrouter_with_ocr',
        'config.initialize_openrouter()',
        'actual_model = model.replace("openrouter-", "")'
    ]
    
    for check in checks:
        if check in content:
            print(f"✓ Found: {check}")
        else:
            print(f"✗ Missing: {check}")
            return False
    
    print("✅ APIs file modifications look good!")
    return True

def test_main_file():
    """Test that main.py has been properly modified"""
    print("\nTesting main.py modifications...")
    
    main_path = os.path.join(os.path.dirname(__file__), 'operate', 'main.py')
    
    with open(main_path, 'r') as f:
        content = f.read()
    
    # Check for OpenRouter help text
    if 'openrouter-{provider}/{model}' in content:
        print("✓ Found OpenRouter help text in main.py")
    else:
        print("✗ Missing OpenRouter help text in main.py")
        return False
    
    print("✅ Main file modifications look good!")
    return True

def test_readme():
    """Test that README has been updated"""
    print("\nTesting README.md modifications...")
    
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Check for OpenRouter documentation
    checks = [
        'Try OpenRouter Models',
        'openrouter-anthropic/claude-3.5-sonnet',
        'openrouter.ai',
        'Benefits of using OpenRouter'
    ]
    
    for check in checks:
        if check in content:
            print(f"✓ Found: {check}")
        else:
            print(f"✗ Missing: {check}")
            return False
    
    print("✅ README modifications look good!")
    return True

def show_usage_examples():
    """Show usage examples"""
    print("\n" + "="*60)
    print("🚀 OPENROUTER INTEGRATION COMPLETE!")
    print("="*60)
    
    print("\n📋 Available OpenRouter Models:")
    models = [
        "openrouter-anthropic/claude-3.5-sonnet",
        "openrouter-openai/gpt-4o", 
        "openrouter-google/gemini-pro-vision",
        "openrouter-meta-llama/llama-3.2-90b-vision-instruct",
        "openrouter-anthropic/claude-3-opus"
    ]
    
    for model in models:
        print(f"  • {model}")
    
    print("\n💡 Usage Examples:")
    print("1. Basic usage:")
    print("   operate -m openrouter-anthropic/claude-3.5-sonnet")
    
    print("\n2. With voice mode:")  
    print("   operate -m openrouter-openai/gpt-4o --voice")
    
    print("\n3. With verbose mode:")
    print("   operate -m openrouter-google/gemini-pro-vision --verbose")
    
    print("\n🔑 Setup Instructions:")
    print("1. Get your API key from https://openrouter.ai/")
    print("2. Run any OpenRouter model command")
    print("3. Enter your API key when prompted")
    print("4. The key will be saved to .env file for future use")

def main():
    """Main validation function"""
    print("🔍 Validating OpenRouter Integration")
    print("="*60)
    
    all_tests_passed = True
    
    tests = [
        test_config_file,
        test_apis_file, 
        test_main_file,
        test_readme
    ]
    
    for test in tests:
        try:
            if not test():
                all_tests_passed = False
        except Exception as e:
            print(f"❌ Test {test.__name__} failed with error: {e}")
            all_tests_passed = False
    
    if all_tests_passed:
        show_usage_examples()
    else:
        print("\n❌ Some validation checks failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()
