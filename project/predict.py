from project.utils import load_model, process_image
from PIL import Image
import io
import torch

model, processor = load_model()

async def predict_image(file):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    inputs = process_image(image, processor)

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class_idx = outputs.logits.argmax(-1).item()
        predicted_class = model.config.id2label[predicted_class_idx]

    return {"class": predicted_class}
