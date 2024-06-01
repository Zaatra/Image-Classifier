import ast
from PIL import Image
from pathlib import Path
import torch
import torchvision.transforms as transforms
from torch.autograd import Variable
from torchvision.models import resnet18, ResNet18_Weights, alexnet, AlexNet_Weights, vgg16, VGG16_Weights

model_dict = {
    'resnet': resnet18(weights=ResNet18_Weights.IMAGENET1K_V1),
    'alexnet': alexnet(weights=AlexNet_Weights.IMAGENET1K_V1),
    'vgg': vgg16(weights=VGG16_Weights.IMAGENET1K_V1)
}

imagenet_classes_file = Path('imagenet1000_clsid_to_human.txt')
with imagenet_classes_file.open() as f:
    imagenet_classes_dict = ast.literal_eval(f.read())

def classifier(img_path, model_name):
    img_pil = Image.open(img_path)
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])
    img_tensor = preprocess(img_pil).unsqueeze_(0)
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    img_tensor = img_tensor.to(device)
    
    model = model_dict[model_name].to(device).eval()
    with torch.no_grad():
        result = model(img_tensor)
    idx = result.cpu().numpy().argmax()
    return imagenet_classes_dict[idx]