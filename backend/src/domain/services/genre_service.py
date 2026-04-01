from transformers import pipeline
from transformers import BertTokenizerFast, EncoderDecoderModel
import torch

model_1 = "MoritzLaurer/mDeBERTa-v3-base-mnli-xnli"
model_2 = "mrm8488/bert2bert_shared-spanish-finetuned-summarization"

class HuggingFaceGenreModel:
    def __init__(self, clf_model=model_1, sum_model=model_2):
        # Clasificador zero-shot con pipeline
        self.classifier = pipeline("zero-shot-classification", model=clf_model)
        self.standard_labels = ["Drama", "Poesía", "Terror", "Ciencia ficción", "Fantasía", "Misterio", "Romance"]

        # usando Torch para resumen 
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        self.tokenizer = BertTokenizerFast.from_pretrained(sum_model)
        self.summarizer_model = EncoderDecoderModel.from_pretrained(sum_model).to(self.device)

        # Resumidor con pipeline 
        # self.summarizer = pipeline("text2text-generation", model=sum_model)

    def summarize(self, text: str, max_length=200, min_length=50):
        """Genera un resumen en español del texto"""
        
        # result = self.summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        # return result[0]["summary_text"]

        #  versión Torch 
        inputs = self.tokenizer([text], padding="max_length", truncation=True,
                                max_length=512, return_tensors="pt")
        input_ids = inputs.input_ids.to(self.device)
        attention_mask = inputs.attention_mask.to(self.device)
        output = self.summarizer_model.generate(
            input_ids,
            attention_mask=attention_mask,
            max_length=max_length,
            min_length=min_length
        )
        return self.tokenizer.decode(output[0], skip_special_tokens=True)

    def classify(self, text: str, use_summary=True):
        """Clasifica el género del texto, opcionalmente usando un resumen"""
        if use_summary:
            text = self.summarize(text)

        result = self.classifier(text, candidate_labels=self.standard_labels)
        return {
            "genre": result["labels"][0],
            "confidence": result["scores"][0]
        }

