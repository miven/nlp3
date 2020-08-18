
import tensorflow as tf
from transformers import BertTokenizer, TFBertForQuestionAnswering
import tensorflow as tf
tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
model = TFBertForQuestionAnswering.from_pretrained('bert-base-cased')
question, text = "Who was Jim Henson?", "Jim Henson was a nice puppet"
input_dict = tokenizer(question, text, return_tensors='tf')
start_scores, end_scores = model(input_dict)
all_tokens = tokenizer.convert_ids_to_tokens(input_dict["input_ids"].numpy()[0])
answer = ' '.join(all_tokens[tf.math.argmax(start_scores, 1)[0] : tf.math.argmax(end_scores, 1)[0]+1])










from transformers import AutoTokenizer, AutoModelWithLMHead

tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")

model = AutoModelWithLMHead.from_pretrained("bert-base-chinese")









