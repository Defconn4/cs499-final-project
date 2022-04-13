from transformers import GPT2Tokenizer, TFGPT2Model         # Need to use Python 3.8.12 (anaconda `cs499` environment) as interpreter

# Ask the user what artist they would like to generate lyrics for - this will later be used in Lyric_Grabber objects.


tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = TFGPT2Model.from_pretrained('gpt2')
text = "The Industrial Revolution has destroyed the foundations of American culture."
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)