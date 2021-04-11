import random

import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load pretrained model and tokenizer
model = GPT2LMHeadModel.from_pretrained("antoiloui/belgpt2")
tokenizer = GPT2Tokenizer.from_pretrained("antoiloui/belgpt2")

# Generate a sample of text
model.eval()
output = model.generate(
            bos_token_id=random.randint(1,50000),
            do_sample=True,
            top_k=50,
            max_length=100,
            top_p=0.95,
            num_return_sequences=1
)

# Decode it
decoded_output = []
for sample in output:
    decoded_output.append(tokenizer.decode(sample, skip_special_tokens=True))
print(decoded_output)


input_context = "Il faut absolument"
# encode input context
input_ids = tokenizer(input_context, return_tensors="pt").input_ids
# generate 3 candidates using sampling
outputs = model.generate(input_ids=input_ids, max_length=20, num_return_sequences=3, do_sample=True)
print("Generated:", tokenizer.batch_decode(outputs, skip_special_tokens=True))
