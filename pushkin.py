from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name_or_path = ".\Pushkin"
tokenizer = GPT2Tokenizer.from_pretrained(
    "sberbank-ai/rugpt3small_based_on_gpt2")
model = GPT2LMHeadModel.from_pretrained(model_name_or_path).to(DEVICE)

def response(text):
    input_ids = tokenizer.encode(text, return_tensors="pt").to(DEVICE)
    model.eval()
    with torch.no_grad():
        out = model.generate(input_ids,
                            do_sample=True,
                            top_k=20,
                            temperature=1.1,
                            max_length=70,
                            )

    generated_text = list(map(tokenizer.decode, out))[0]
    return generated_text