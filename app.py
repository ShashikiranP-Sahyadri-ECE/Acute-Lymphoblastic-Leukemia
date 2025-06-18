import gradio as gr
import torch
import torch.nn as nn
from torchvision import transforms
from torchvision.models import mobilenet_v2
from PIL import Image

# Define class labels
classes = ['Benign', 'Early', 'Pre', 'Pro']

# Image preprocessing
transform = transforms.Compose([
    transforms.Resize((128, 128)),
    transforms.ToTensor()
])

# Load model
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = mobilenet_v2(pretrained=False)
model.classifier = nn.Sequential(
    nn.Dropout(0.4),
    nn.Linear(model.last_channel, len(classes))
)
model.load_state_dict(torch.load("best_model.pth", map_location=device))
model.to(device)
model.eval()

# Prediction function
def predict(image):
    image = image.convert("RGB")
    input_tensor = transform(image).unsqueeze(0).to(device)
    with torch.no_grad():
        output = model(input_tensor)
        probabilities = torch.softmax(output, dim=1).cpu().numpy()[0]
    return {classes[i]: float(probabilities[i]) for i in range(len(classes))}

# Launch Gradio UI
gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=4),
    title="Blood Cell Stage Classifier",
    description="Upload a blood cell image to classify its stage."
).launch()
