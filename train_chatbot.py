from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load Pretrained Model and Tokenizer
model_name = "gpt2"  # You can change this to "mistralai/Mistral-7B-Instruct" for a better model
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

print("Model Loaded Successfully!")