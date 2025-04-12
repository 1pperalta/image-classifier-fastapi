from transformers import AutoModelForImageClassification, AutoProcessor
import torch

def load_model():
    model_name = "microsoft/resnet-50"
    model = AutoModelForImageClassification.from_pretrained(model_name)
    processor = AutoProcessor.from_pretrained(model_name)
    model.eval()
    return model, processor

def process_image(image, processor):
    return processor(images=image, return_tensors="pt")
