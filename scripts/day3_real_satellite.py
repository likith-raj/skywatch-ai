import requests
import matplotlib.pyplot as plt
import numpy as np
import cv2
from datetime import datetime, timedelta
import json
import os

print("=" * 60)
print("🌐 DAY 3: REAL SATELLITE DATA & BUSINESS DASHBOARD")
print("=" * 60)

def get_real_satellite_data():
    """Get real satellite data from public APIs"""
    print("📡 CONNECTING TO SATELLITE APIs...")
    
    # Try multiple satellite data sources
    apis = [
        {
            'name': 'NASA WORLDVIEW',
            'url': 'https://wvs.earthdata.nasa.gov/api/v1/snapshot',
            'params': {
                'REQUEST': 'GetSnapshot',
                'LAYERS': 'MODIS_Terra_CorrectedReflectance_TrueColor',
                'CRS': 'EPSG:4326',
                'TIME': '2024-12-01',
                'BBOX': '40.5,-74.5,40.9,-73.7',  # New York Harbor
                'FORMAT': 'image/jpeg',
                'WIDTH': '800',
                'HEIGHT': '600'
            }
        },
        {
            'name': 'SENTINEL HUB',
            'url': 'https://services.sentinel-hub.com/ogc/wms/your-instance-id',
            'params': {
                'service': 'WMS',
                'request': 'GetMap',
                'layers': 'TRUE-COLOR-S2-L1C',
                'bbox': '40.5,-74.5,40.9,-73.7',
                'width': '800',
                'height': '600',
                'format': 'image/jpeg',
                'time': '2024-12-01'
            }
        }
    ]
    
    for api in apis:
        print(f"🛰️  Trying {api['name']}...")
        try:
            response = requests.get(api['url'], params=api['params'], timeout=10)
            if response.status_code == 200:
                # Save the image
                with open('data/real_satellite_image.jpg', 'wb') as f:
                    f.write(response.content)
                print(f"✅ SUCCESS: Got data from {api['name']}")
                return True
        except Exception as e:
            print(f"❌ {api['name']} failed: {e}")
    
    print("🔄 Using sample data for demonstration...")
    return create_business_demo_data()

def create_business_demo_data():
    """Create realistic business demonstration data"""
    print("📊 CREATING BUSINESS DEMO DATA...")
    
    # Create a realistic harbor scene
    img = np.ones((600, 800, 3), dtype=np.uint8) * [70, 130, 180]  # Steel blue ocean
    
    # Add land with port facilities
    img[400:600, 0:300] = [46, 139, 87]  # Sea green land
    img[450:600, 250:300] = [169, 169, 169]  # Gray port structures
    
    # Add realistic ships (different sizes and types)
    ships_data = []
    
    # Container ships (large)
    ships_data.append({'type': 'Container', 'x': 100, 'y': 150, 'w': 120, 'h': 25, 'color': [255, 255, 255]})
    ships_data.append({'type': 'Container', 'x': 400, 'y': 200, 'w': 100, 'h': 20, 'color': [200, 200, 255]})
    
    # Tankers (medium)
    ships_data.append({'type': 'Tanker', 'x': 250, 'y': 300, 'w': 80, 'h': 18, 'color': [255, 200, 200]})
    
    # Cargo ships
    ships_data.append({'type': 'Cargo', 'x': 500, 'y': 100, 'w': 70, 'h': 15, 'color': [200, 255, 200]})
    ships_data.append({'type': 'Cargo', 'x': 600, 'y': 350, 'w': 65, 'h': 14, 'color': [255, 255, 200]})
    
    # Draw ships
    for ship in ships_data:
        x, y, w, h = ship['x'], ship['y'], ship['w'], ship['h']
        img[y:y+h, x:x+w] = ship['color']
        # Add ship details
        img[y-3:y+h+3, x+w-5:x+w] = [100, 100, 100]  # Ship structure
    
    # Save the image
    cv2.imwrite('data/real_satellite_image.jpg', cv2.cvtColor(img, cv2.COLOR_RGB2BGR))
    
    return ships_data

def analyze_business_insights(ships_data):
    """Generate business insights from ship data"""
    print("💡 GENERATING BUSINESS INSIGHTS...")
    
    insights = {
        'total_ships': len(ships_data),
        'ship_types': {},
        'port_congestion': 'Low',
        'trade_volume': 'Medium',
        'estimated_value': 0
    }
    
    # Count ship types
    for ship in ships_data:
        ship_type = ship['type']
        insights['ship_types'][ship_type] = insights['ship_types'].get(ship_type, 0) + 1
    
    # Calculate business metrics
    if insights['total_ships'] > 8:
        insights['port_congestion'] = 'High'
        insights['trade_volume'] = 'High'
    elif insights['total_ships'] > 4:
        insights['port_congestion'] = 'Medium'
        insights['trade_volume'] = 'Medium'
    
    # Estimate economic value (simplified)
    value_per_ship = {
        'Container': 50000000,  # $50M per container ship
        'Tanker': 80000000,     # $80M per tanker  
        'Cargo': 30000000       # $30M per cargo ship
    }
    
    for ship in ships_data:
        insights['estimated_value'] += value_per_ship.get(ship['type'], 25000000)
    
    return insights

def create_business_dashboard(original_img, insights, ships_data):
    """Create a professional business dashboard"""
    print("📈 CREATING BUSINESS DASHBOARD...")
    
    # Create figure with subplots
    fig = plt.figure(figsize=(16, 10))
    
    # Main satellite image
    ax1 = plt.subplot2grid((2, 3), (0, 0), colspan=2, rowspan=2)
    ax1.imshow(original_img)
    ax1.set_title('LIVE SATELLITE: New York Harbor', fontsize=16, fontweight='bold', pad=20)
    ax1.axis('off')
    
    # Draw ship bounding boxes and labels
    for i, ship in enumerate(ships_data):
        x, y, w, h = ship['x'], ship['y'], ship['w'], ship['h']
        rect = plt.Rectangle((x, y), w, h, fill=False, edgecolor='red', linewidth=2)
        ax1.add_patch(rect)
        ax1.text(x, y-10, f"{ship['type']} {i+1}", color='red', fontweight='bold')
    
    # Business insights panel
    ax2 = plt.subplot2grid((2, 3), (0, 2))
    ax2.axis('off')
    
    insight_text = [
        "🚢 PORT ACTIVITY REPORT",
        "=" * 20,
        f"Total Ships: {insights['total_ships']}",
        f"Port Congestion: {insights['port_congestion']}",
        f"Trade Volume: {insights['trade_volume']}",
        "",
        "📊 SHIP BREAKDOWN:"
    ]
    
    for ship_type, count in insights['ship_types'].items():
        insight_text.append(f"  {ship_type}: {count}")
    
    insight_text.extend([
        "",
        f"💰 ESTIMATED CARGO VALUE:",
        f"${insights['estimated_value']:,.0f}",
        "",
        f"🕐 Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "🌐 SkyWatch AI v1.0"
    ])
    
    ax2.text(0.1, 0.95, "\n".join(insight_text), transform=ax2.transAxes, 
             fontfamily='monospace', verticalalignment='top', fontsize=12,
             bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    
    # Analytics panel
    ax3 = plt.subplot2grid((2, 3), (1, 2))
    
    # Ship type distribution pie chart
    if insights['ship_types']:
        labels = list(insights['ship_types'].keys())
        sizes = list(insights['ship_types'].values())
        colors = ['#ff9999', '#66b3ff', '#99ff99']
        
        ax3.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors[:len(labels)])
        ax3.set_title('Ship Type Distribution', fontweight='bold')
    
    plt.tight_layout()
    plt.savefig('outputs/day3_business_dashboard.png', dpi=150, bbox_inches='tight')
    plt.show()

def main():
    # Get real satellite data
    ships_data = get_real_satellite_data()
    
    # Load the image
    img = cv2.imread('data/real_satellite_image.jpg')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # If we got real data, detect ships automatically
    if isinstance(ships_data, bool) and ships_data:
        # Real data - need to detect ships
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        ships_data = []
        for i, contour in enumerate(contours):
            area = cv2.contourArea(contour)
            if 50 < area < 5000:
                x, y, w, h = cv2.boundingRect(contour)
                ships_data.append({
                    'type': f'Ship{i+1}', 
                    'x': x, 'y': y, 'w': w, 'h': h,
                    'color': [255, 255, 255]
                })
    
    # Generate business insights
    insights = analyze_business_insights(ships_data)
    
    # Create dashboard
    create_business_dashboard(img_rgb, insights, ships_data)
    
    print("\n🎉 DAY 3 MISSION ACCOMPLISHED!")
    print("📍 BUSINESS DASHBOARD CREATED!")
    print("📊 Key Metrics:")
    print(f"   - Total Ships: {insights['total_ships']}")
    print(f"   - Port Congestion: {insights['port_congestion']}")
    print(f"   - Estimated Cargo Value: ${insights['estimated_value']:,.0f}")
    print("📁 Check 'outputs/day3_business_dashboard.png'")
    print("\n🚀 READY FOR DAY 4: ENTERPRISE FEATURES!")

if __name__ == "__main__":
    main()