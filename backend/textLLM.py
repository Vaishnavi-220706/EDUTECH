from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


prompt = tokenizer.apply_chat_template(
    [{"role": "user", "content": "Road map for python? Think step-by-step."}],
    return_tensors="pt"
).to(device)


outputs = model.generate(
    input_ids=prompt,
    max_new_tokens=100,
    temperature=0.7,
    do_sample=True,
    pad_token_id=tokenizer.eos_token_id
)


response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
