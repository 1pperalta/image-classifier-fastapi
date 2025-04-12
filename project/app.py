from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from project.predict import predict_image

app = FastAPI()

@app.post("/predict-image")
async def predict(file: UploadFile = File(...)):
    result = await predict_image(file)
    return JSONResponse(content=result)
