# Image Classifier with FastAPI

This project is an image classification API built using FastAPI. It allows users to upload images and receive predictions based on a pre-trained machine learning model.

## Features

- Upload images for classification.
- Get predictions with confidence scores.
- Easy-to-use RESTful API.

## Requirements

- Python 3.8+
- FastAPI
- Uvicorn
- Pillow
- Pre-trained ML model (e.g., TensorFlow, PyTorch)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/1pperalta/image-classifier-fastapi.git
    cd image-classifier-fastapi
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Start the FastAPI server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to:
    ```
    http://127.0.0.1:8000/docs
    ```

3. Use the Swagger UI to test the API.

## API Endpoints

- `POST /predict`: Upload an image and get predictions.

## Example Request

```bash
curl -X POST "http://127.0.0.1:8000/predict" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@path_to_your_image.jpg"
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- Pre-trained models from [TensorFlow](https://www.tensorflow.org/) or [PyTorch](https://pytorch.org/).
- Inspiration from open-source projects.