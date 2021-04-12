# FinisMaPhrase

Twitter bot that replies to messages with a complete phrase in French.

To see it in action, look here: https://twitter.com/FinisMaPhrase/with_replies

Based on [BelGTP2](https://huggingface.co/antoiloui/belgpt2) model (GPT-2 retrained for French) for text generation and [TF-Allocine](https://huggingface.co/tblard/tf-allocine) (based on CamemBERT itself based on BERT) for sentiment analysis.

## Process
* Take the provided prefix
* Generate a candidate sentence
* Check it with the sentiment analyzer to ensure it's positive
* If it's good, return it. Otherwise, generate a new candidate sentence (max of 20 iterations)


## References
I took inspiration from these sources:
* https://huggingface.co/antoiloui/belgpt2
* https://huggingface.co/tblard/tf-allocine
* https://medium.com/@timohear/nous-avons-form%C3%A9-gpt-2-pour-%C3%A9crire-des-lettres-damour-f65b40e31ff8
* https://minimaxir.com/2020/01/twitter-gpt2-bot/

## Thanks
Thanks to those who trained the models I use, and thanks to HuggingFace for hosting such a nice collection of
ready-to-use models as well as providing a very easy-to-use API! 🤗
