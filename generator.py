import os
import random

from transformers import GPT2Tokenizer, GPT2LMHeadModel


class Generator:
    def __init__(self):
        cache_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "storage", "hfcache")

        # Load pretrained model and tokenizer
        self.model = GPT2LMHeadModel.from_pretrained("antoiloui/belgpt2", cache_dir=cache_path)
        self.tokenizer = GPT2Tokenizer.from_pretrained("antoiloui/belgpt2", cache_dir=cache_path)

    def initialize(self):
        """
        Initializes the model, takes a bit of time
        """
        self.model.eval()

    def generate(self):
        output = self.model.generate(
            bos_token_id=random.randint(1, 50000),
            do_sample=True,
            top_k=50,
            max_length=100,
            top_p=0.95,
            num_return_sequences=1
        )

        # Decode it
        decoded_output = []
        for sample in output:
            decoded_output.append(self.tokenizer.decode(sample, skip_special_tokens=True))
        return decoded_output

    def complete(self, prefix, length=80):
        # encode input context
        input_ids = self.tokenizer(prefix, return_tensors="pt").input_ids
        # generate a candidate using sampling
        outputs = self.model.generate(input_ids=input_ids, max_length=length, num_return_sequences=1, do_sample=True)
        decoded_output = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)
        return decoded_output[0]


if __name__ == "__main__":
    print("Init")
    gen = Generator()
    print("OK")
    gen.initialize()
    print("OK2")
    print(gen.generate())
    print(gen.complete("Coucou, tu veux"))
