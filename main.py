import os
from datetime import datetime
from google import genai

def run_cloud_automation(task_prompt: str):
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
raise ValueError("Missing GEMINI_API_KEY environment variable.")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
model="gemini-2.5-flash",
contents=task_prompt,
)
return response.text
if name == "main":
prompt = "Generate a concise daily system status and automation checklist."
output = run_cloud_automation(prompt)
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log_entry = f"[{timestamp}]\n{output}\n{'-'*40}\n"
with open("automation_log.txt", "a", encoding="utf-8") as f:
f.write(log_entry)
print("Automation executed successfully:")
print(output)
