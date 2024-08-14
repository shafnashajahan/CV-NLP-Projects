import torch
import cv2
import numpy as np
from PIL import Image
from torchvision.transforms import Compose, Resize, ToTensor, CenterCrop

# Load MiDaS model
model = torch.hub.load("intel-isl/MiDaS", "MiDaS_small")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device).eval()

# Preprocessing pipeline
transform = Compose([
    Resize(384),  # Resize to a multiple of 32
    CenterCrop(384), # Center crop to 384x384
    ToTensor()
])

def estimate_depth(frame):
    """Estimate depth from a single RGB frame."""
    # Ensure frame is uint8 before conversion
    frame = (frame * 255).astype(np.uint8)  # Scale to [0, 255] and convert to uint8
    
    # Convert numpy.ndarray to PIL Image
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame_pil = Image.fromarray(frame_rgb)
    
    # Apply transformations
    input_tensor = transform(frame_pil).unsqueeze(0).to(device)
    
    with torch.no_grad():
        depth_map = model(input_tensor)
    
    # Squeeze and process depth_map
    depth_map = depth_map.squeeze().cpu().numpy()
    
    # Normalize depth_map
    depth_map = cv2.normalize(depth_map, None, 0, 255, cv2.NORM_MINMAX)
    
    # Convert depth_map to uint8
    depth_map = depth_map.astype(np.uint8)
    
    # Resize depth_map to match the original frame size
    depth_map_resized = cv2.resize(depth_map, (frame.shape[1], frame.shape[0]), interpolation=cv2.INTER_LINEAR)
    return depth_map_resized

# Example usage
# Create a dummy image of type uint8
frame = (np.random.rand(480, 640, 3) * 255).astype(np.uint8)  
depth_map = estimate_depth(frame)
print("Depth map size:", depth_map.shape)