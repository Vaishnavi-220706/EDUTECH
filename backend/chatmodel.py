from fastapi import FastAPI, Request
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch


# Load model and tokenizer
model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


# FastAPI app
app = FastAPI(title="TinyLlama Chat API")


# Request body model
class PromptRequest(BaseModel):
    prompt: str
    max_new_tokens: int = 100
    temperature: float = 0.7




@app.post("/generate")
async def generate_text(request: PromptRequest):
    try:
        # Use chat template format
        inputs = tokenizer.apply_chat_template(
            [{"role": "user", "content": request.prompt}],
            return_tensors="pt"
        ).to(device)


        # Generate output
        outputs = model.generate(
            input_ids=inputs,
            max_new_tokens=request.max_new_tokens,
            temperature=request.temperature,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id
        )


        # Decode the response
        response_text = tokenizer.decode(outputs[0], skip_special_tokens=True)


        # Optionally, strip the prompt from the response
        assistant_response = response_text.split(request.prompt, 1)[-1].strip()


        return {"response": assistant_response}


    except Exception as e:
        return {"error": str(e)}
