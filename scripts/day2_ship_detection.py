import cv2
import numpy as np
import matplotlib.pyplot as plt
import rasterio
from PIL import Image
import os

print("=" * 60)
print("🚢 DAY 2: SHIP DETECTION AI")
print("=" * 60)

def load_satellite_image():
    """Load the image we downloaded yesterday"""
    print("📡 LOADING SATELLITE IMAGE...")
    try:
        with rasterio.open('data/first_satellite_image.tif') as src:
            image = src.read()
            # Convert to RGB format for OpenCV
            if len(image.shape) == 3:
                image = np.transpose(image, (1, 2, 0))
            return image
    except Exception as e:
        print(f"❌ Failed to load image: {e}")
        # Create a sample harbor image with ships
        return create_sample_harbor_image()

def create_sample_harbor_image():
    """Create a sample image with synthetic ships for testing"""
    print("🔄 CREATING SAMPLE HARBOR IMAGE...")
    # Create blue ocean background
    img = np.ones((800, 1000, 3), dtype=np.uint8) * [30, 144, 255]  # Ocean blue
    
    # Add some land (green)
    img[600:800, 0:400] = [34, 139, 34]  # Forest green
    
    # Add synthetic ships (white rectangles)
    # Ship 1
    img[200:220, 100:180] = [255, 255, 255]  # Large ship
    img[195:225, 175:185] = [200, 200, 200]  # Ship detail
    
    # Ship 2
    img[300:315, 400:450] = [255, 255, 255]  # Medium ship
    img[295:320, 445:455] = [200, 200, 200]  # Ship detail
    
    # Ship 3
    img[500:510, 700:730] = [255, 255, 255]  # Small ship
    
    print("✅ SAMPLE HARBOR WITH SHIPS CREATED!")
    return img

def detect_ships(image):
    """Simple ship detection using computer vision"""
    print("🔍 DETECTING SHIPS...")
    
    # Convert to grayscale for processing
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    else:
        gray = image
    
    # Enhance contrast
    gray = cv2.equalizeHist(gray)
    
    # Threshold to find bright objects (ships are usually bright)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    
    # Find contours (object boundaries)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Filter contours by size (remove noise)
    ship_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if 50 < area < 5000:  # Reasonable ship size range
            ship_contours.append(contour)
    
    print(f"✅ FOUND {len(ship_contours)} POTENTIAL SHIPS!")
    return ship_contours

def visualize_detection(original_image, ship_contours):
    """Create visualization with detected ships"""
    print("🎨 CREATING DETECTION VISUALIZATION...")
    
    # Create a copy of the original image
    result_image = original_image.copy()
    if len(result_image.shape) == 2:
        result_image = cv2.cvtColor(result_image, cv2.COLOR_GRAY2RGB)
    
    # Draw bounding boxes around detected ships
    for i, contour in enumerate(ship_contours):
        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)
        
        # Draw rectangle
        cv2.rectangle(result_image, (x, y), (x + w, y + h), (255, 0, 0), 2)
        
        # Add ship number
        cv2.putText(result_image, f'Ship {i+1}', (x, y-10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    
    # Create comparison plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Original image
    ax1.imshow(original_image)
    ax1.set_title('Original Satellite Image', fontweight='bold')
    ax1.axis('off')
    
    # Detection result
    ax2.imshow(result_image)
    ax2.set_title(f'Ship Detection: Found {len(ship_contours)} Ships', 
                 fontweight='bold', color='blue')
    ax2.axis('off')
    
    plt.tight_layout()
    plt.savefig('outputs/day2_ship_detection.png', dpi=150, bbox_inches='tight')
    plt.show()
    
    return result_image

def main():
    # Load satellite image
    satellite_image = load_satellite_image()
    
    # Detect ships
    ships = detect_ships(satellite_image)
    
    # Visualize results
    result_img = visualize_detection(satellite_image, ships)
    
    print("\n🎉 DAY 2 MISSION ACCOMPLISHED!")
    print(f"📍 SHIPS DETECTED: {len(ships)}")
    print("📁 Check 'outputs/day2_ship_detection.png'")
    print("\n🚀 READY FOR DAY 3: REAL SATELLITE DATA INTEGRATION!")

if __name__ == "__main__":
    main()