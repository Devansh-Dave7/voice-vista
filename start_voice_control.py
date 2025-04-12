import os
import subprocess
import sys

def setup_and_run():
    """Set up environment and run voice browser control"""
    api_key = os.environ.get("GROQ_API_KEY")
    
    if not api_key:
        print("\n=== Voice Browser Control with LLM Setup ===")
        print("No Groq API key found in environment variables.")
        
        api_key = input("Enter your Groq API key (press Enter to skip): ").strip()
        
        if api_key:
            os.environ["GROQ_API_KEY"] = api_key
            print(f"API key set for this session.")
        else:
            print("No API key provided. Voice Browser Control will use basic intent recognition only.")
    
    print("\nStarting Voice Browser Control...")
    subprocess.call([sys.executable, "voice_browser_control.py"])

if __name__ == "__main__":
    setup_and_run() 