import requests
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
import numpy as np
import hashlib
import time
from PIL import Image
import io
import base64
import streamlit.components.v1 as components

# =============================================================================
# PREMIUM CANVAS ANIMATIONS
# =============================================================================

class PremiumCanvasAnimations:
    def __init__(self):
        pass
    
    def create_cosmic_starfield(self):
        """Create advanced cosmic starfield with constellations"""
        cosmic_js = """
        <!DOCTYPE html>
        <html>
        <head>
            <style>
                .cosmic-canvas {
                    position: fixed;
                    top: 0;
                    left: 0;
                    width: 100%;
                    height: 100%;
                    pointer-events: none;
                    z-index: -1;
                }
            </style>
        </head>
        <body>
            <canvas class="cosmic-canvas" id="cosmicCanvas"></canvas>
            
            <script>
                class CosmicStarfield {
                    constructor() {
                        this.canvas = document.getElementById('cosmicCanvas');
                        this.ctx = this.canvas.getContext('2d');
                        this.stars = [];
                        this.meteors = [];
                        this.nebulas = [];
                        this.constellations = [];
                        
                        this.init();
                    }
                    
                    init() {
                        this.resize();
                        this.createStars();
                        this.createNebulas();
                        this.createConstellations();
                        this.animate();
                        
                        window.addEventListener('resize', () => this.resize());
                    }
                    
                    resize() {
                        this.canvas.width = window.innerWidth;
                        this.canvas.height = window.innerHeight;
                        this.stars = [];
                        this.createStars();
                    }
                    
                    createStars() {
                        const starCount = Math.min(400, Math.floor((this.canvas.width * this.canvas.height) / 3000));
                        
                        for (let i = 0; i < starCount; i++) {
                            this.stars.push({
                                x: Math.random() * this.canvas.width,
                                y: Math.random() * this.canvas.height,
                                size: Math.random() * 3 + 0.5,
                                speed: Math.random() * 0.8 + 0.1,
                                brightness: Math.random() * 0.8 + 0.2,
                                twinkleSpeed: Math.random() * 0.05 + 0.02,
                                twinkleOffset: Math.random() * Math.PI * 2,
                                color: this.getStarColor()
                            });
                        }
                    }
                    
                    createNebulas() {
                        for (let i = 0; i < 3; i++) {
                            this.nebulas.push({
                                x: Math.random() * this.canvas.width,
                                y: Math.random() * this.canvas.height,
                                radius: Math.random() * 200 + 100,
                                color: this.getNebulaColor(),
                                pulseSpeed: Math.random() * 0.002 + 0.001,
                                pulsePhase: Math.random() * Math.PI * 2
                            });
                        }
                    }
                    
                    createConstellations() {
                        const constellationCount = 8;
                        for (let i = 0; i < constellationCount; i++) {
                            const starsInConstellation = Math.floor(Math.random() * 6) + 4;
                            const constellation = {
                                stars: [],
                                lines: [],
                                brightness: Math.random() * 0.3 + 0.7
                            };
                            
                            // Create constellation stars
                            const baseX = Math.random() * this.canvas.width;
                            const baseY = Math.random() * this.canvas.height;
                            
                            for (let j = 0; j < starsInConstellation; j++) {
                                constellation.stars.push({
                                    x: baseX + (Math.random() - 0.5) * 300,
                                    y: baseY + (Math.random() - 0.5) * 200,
                                    size: Math.random() * 2 + 1,
                                    brightness: Math.random() * 0.4 + 0.6
                                });
                            }
                            
                            // Create constellation lines
                            for (let j = 0; j < starsInConstellation - 1; j++) {
                                for (let k = j + 1; k < starsInConstellation; k++) {
                                    if (Math.random() > 0.7) { // 30% chance to connect stars
                                        constellation.lines.push({
                                            from: j,
                                            to: k,
                                            brightness: Math.random() * 0.2 + 0.3
                                        });
                                    }
                                }
                            }
                            
                            this.constellations.push(constellation);
                        }
                    }
                    
                    getStarColor() {
                        const colors = [
                            '#ffffff', '#f8f7ff', '#e3f2fd', '#f3e5f5',
                            '#fff8e1', '#e8f5e8', '#ffebee', '#e0f2f1'
                        ];
                        return colors[Math.floor(Math.random() * colors.length)];
                    }
                    
                    getNebulaColor() {
                        const colors = [
                            'rgba(102, 126, 234, 0.1)', 'rgba(118, 75, 162, 0.1)',
                            'rgba(240, 147, 251, 0.1)', 'rgba(79, 195, 247, 0.1)',
                            'rgba(129, 199, 132, 0.1)', 'rgba(255, 183, 77, 0.1)'
                        ];
                        return colors[Math.floor(Math.random() * colors.length)];
                    }
                    
                    animate() {
                        this.ctx.fillStyle = 'rgba(12, 12, 46, 0.05)';
                        this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                        
                        this.drawNebulas();
                        this.drawStars();
                        this.drawConstellations();
                        this.drawDataParticles();
                        
                        requestAnimationFrame(() => this.animate());
                    }
                    
                    drawNebulas() {
                        this.nebulas.forEach(nebula => {
                            const gradient = this.ctx.createRadialGradient(
                                nebula.x, nebula.y, 0,
                                nebula.x, nebula.y, nebula.radius
                            );
                            
                            const pulse = Math.sin(nebula.pulsePhase) * 0.5 + 0.5;
                            nebula.pulsePhase += nebula.pulseSpeed;
                            
                            gradient.addColorStop(0, nebula.color.replace('0.1', (0.15 * pulse).toFixed(2)));
                            gradient.addColorStop(1, nebula.color.replace('0.1', '0.01'));
                            
                            this.ctx.fillStyle = gradient;
                            this.ctx.beginPath();
                            this.ctx.arc(nebula.x, nebula.y, nebula.radius, 0, Math.PI * 2);
                            this.ctx.fill();
                        });
                    }
                    
                    drawStars() {
                        this.stars.forEach(star => {
                            const twinkle = Math.sin(star.twinkleOffset) * 0.3 + 0.7;
                            star.twinkleOffset += star.twinkleSpeed;
                            
                            star.y += star.speed;
                            if (star.y > this.canvas.height) {
                                star.y = 0;
                                star.x = Math.random() * this.canvas.width;
                            }
                            
                            this.ctx.beginPath();
                            this.ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
                            
                            // Create star glow
                            const gradient = this.ctx.createRadialGradient(
                                star.x, star.y, 0,
                                star.x, star.y, star.size * 3
                            );
                            gradient.addColorStop(0, star.color.replace(')', `, ${star.brightness * twinkle})`).replace('rgb', 'rgba'));
                            gradient.addColorStop(1, star.color.replace(')', ', 0)').replace('rgb', 'rgba'));
                            
                            this.ctx.fillStyle = gradient;
                            this.ctx.fill();
                        });
                    }
                    
                    drawConstellations() {
                        this.constellations.forEach(constellation => {
                            // Draw constellation lines
                            constellation.lines.forEach(line => {
                                const fromStar = constellation.stars[line.from];
                                const toStar = constellation.stars[line.to];
                                
                                this.ctx.strokeStyle = `rgba(102, 126, 234, ${line.brightness * 0.3})`;
                                this.ctx.lineWidth = 1;
                                this.ctx.beginPath();
                                this.ctx.moveTo(fromStar.x, fromStar.y);
                                this.ctx.lineTo(toStar.x, toStar.y);
                                this.ctx.stroke();
                            });
                            
                            // Draw constellation stars
                            constellation.stars.forEach(star => {
                                this.ctx.beginPath();
                                this.ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
                                
                                const gradient = this.ctx.createRadialGradient(
                                    star.x, star.y, 0,
                                    star.x, star.y, star.size * 4
                                );
                                gradient.addColorStop(0, `rgba(102, 126, 234, ${star.brightness})`);
                                gradient.addColorStop(1, 'rgba(102, 126, 234, 0)');
                                
                                this.ctx.fillStyle = gradient;
                                this.ctx.fill();
                            });
                        });
                    }
                    
                    drawDataParticles() {
                        // Occasionally create data flow particles
                        if (Math.random() < 0.1) {
                            this.createDataParticle();
                        }
                        
                        // Update and draw data particles
                        for (let i = this.meteors.length - 1; i >= 0; i--) {
                            const meteor = this.meteors[i];
                            
                            meteor.x += meteor.vx;
                            meteor.y += meteor.vy;
                            meteor.life -= 0.02;
                            
                            if (meteor.life <= 0 || meteor.x < 0 || meteor.x > this.canvas.width || 
                                meteor.y < 0 || meteor.y > this.canvas.height) {
                                this.meteors.splice(i, 1);
                                continue;
                            }
                            
                            // Draw meteor with trail
                            this.ctx.strokeStyle = `rgba(102, 126, 234, ${meteor.life})`;
                            this.ctx.lineWidth = 2;
                            this.ctx.beginPath();
                            this.ctx.moveTo(meteor.x, meteor.y);
                            this.ctx.lineTo(meteor.x - meteor.vx * 3, meteor.y - meteor.vy * 3);
                            this.ctx.stroke();
                            
                            // Draw meteor head
                            this.ctx.beginPath();
                            this.ctx.arc(meteor.x, meteor.y, 2, 0, Math.PI * 2);
                            this.ctx.fillStyle = `rgba(255, 255, 255, ${meteor.life})`;
                            this.ctx.fill();
                        }
                    }
                    
                    createDataParticle() {
                        this.meteors.push({
                            x: Math.random() * this.canvas.width,
                            y: 0,
                            vx: (Math.random() - 0.5) * 4,
                            vy: Math.random() * 3 + 2,
                            life: 1
                        });
                    }
                }
                
                // Initialize when page loads
                document.addEventListener('DOMContentLoaded', () => {
                    new CosmicStarfield();
                });
            </script>
        </body>
        </html>
        """
        components.html(cosmic_js, height=0)
    
    def create_satellite_network(self):
        """Create animated satellite network visualization"""
        satellite_js = """
        <div style="text-align: center; margin: 2rem 0;">
            <div style="position: relative; width: 100%; height: 300px; background: rgba(12, 12, 46, 0.3); 
                border-radius: 20px; overflow: hidden; border: 1px solid rgba(102, 126, 234, 0.3);">
                <canvas id="satelliteNetwork" style="width: 100%; height: 100%;"></canvas>
            </div>
        </div>
        
        <script>
            class SatelliteNetwork {
                constructor() {
                    this.canvas = document.getElementById('satelliteNetwork');
                    this.ctx = this.canvas.getContext('2d');
                    this.satellites = [];
                    this.connections = [];
                    this.dataPackets = [];
                    
                    this.init();
                }
                
                init() {
                    this.resize();
                    this.createSatellites();
                    this.createConnections();
                    this.animate();
                    
                    window.addEventListener('resize', () => this.resize());
                }
                
                resize() {
                    this.canvas.width = this.canvas.offsetWidth;
                    this.canvas.height = this.canvas.offsetHeight;
                }
                
                createSatellites() {
                    const satelliteCount = 8;
                    const padding = 80;
                    
                    for (let i = 0; i < satelliteCount; i++) {
                        const angle = (i / satelliteCount) * Math.PI * 2;
                        const radius = Math.min(this.canvas.width, this.canvas.height) / 2 - padding;
                        
                        this.satellites.push({
                            x: this.canvas.width / 2 + Math.cos(angle) * radius,
                            y: this.canvas.height / 2 + Math.sin(angle) * radius,
                            size: 8,
                            orbitSpeed: 0.0005 + Math.random() * 0.0005,
                            orbitAngle: angle,
                            orbitRadius: radius,
                            color: this.getSatelliteColor(),
                            pulsePhase: Math.random() * Math.PI * 2
                        });
                    }
                    
                    // Add central hub
                    this.satellites.push({
                        x: this.canvas.width / 2,
                        y: this.canvas.height / 2,
                        size: 12,
                        orbitSpeed: 0,
                        orbitAngle: 0,
                        orbitRadius: 0,
                        color: '#764ba2',
                        pulsePhase: 0
                    });
                }
                
                createConnections() {
                    // Connect satellites to central hub
                    for (let i = 0; i < this.satellites.length - 1; i++) {
                        this.connections.push({
                            from: i,
                            to: this.satellites.length - 1, // Central hub
                            strength: 0.8,
                            dataFlow: Math.random() * 0.02 + 0.01
                        });
                    }
                    
                    // Connect some satellites to each other
                    for (let i = 0; i < this.satellites.length - 1; i++) {
                        for (let j = i + 1; j < this.satellites.length - 1; j++) {
                            if (Math.random() > 0.7) {
                                this.connections.push({
                                    from: i,
                                    to: j,
                                    strength: 0.4,
                                    dataFlow: Math.random() * 0.01 + 0.005
                                });
                            }
                        }
                    }
                }
                
                getSatelliteColor() {
                    const colors = ['#667eea', '#764ba2', '#f093fb', '#4fc3f7', '#81c784', '#fff176'];
                    return colors[Math.floor(Math.random() * colors.length)];
                }
                
                animate() {
                    this.ctx.fillStyle = 'rgba(12, 12, 46, 0.1)';
                    this.ctx.fillRect(0, 0, this.canvas.width, this.canvas.height);
                    
                    this.updateSatellites();
                    this.drawConnections();
                    this.drawSatellites();
                    this.drawDataFlow();
                    
                    requestAnimationFrame(() => this.animate());
                }
                
                updateSatellites() {
                    this.satellites.forEach((sat, index) => {
                        if (sat.orbitSpeed > 0) {
                            sat.orbitAngle += sat.orbitSpeed;
                            sat.x = this.canvas.width / 2 + Math.cos(sat.orbitAngle) * sat.orbitRadius;
                            sat.y = this.canvas.height / 2 + Math.sin(sat.orbitAngle) * sat.orbitRadius;
                        }
                        
                        sat.pulsePhase += 0.05;
                    });
                }
                
                drawConnections() {
                    this.connections.forEach(conn => {
                        const from = this.satellites[conn.from];
                        const to = this.satellites[conn.to];
                        
                        // Animated connection line
                        const gradient = this.ctx.createLinearGradient(from.x, from.y, to.x, to.y);
                        gradient.addColorStop(0, `${from.color}33`);
                        gradient.addColorStop(1, `${to.color}33`);
                        
                        this.ctx.strokeStyle = gradient;
                        this.ctx.lineWidth = 1;
                        this.ctx.setLineDash([5, 5]);
                        this.ctx.beginPath();
                        this.ctx.moveTo(from.x, from.y);
                        this.ctx.lineTo(to.x, to.y);
                        this.ctx.stroke();
                        this.ctx.setLineDash([]);
                        
                        // Occasionally send data packets
                        if (Math.random() < conn.dataFlow) {
                            this.createDataPacket(conn.from, conn.to);
                        }
                    });
                }
                
                drawSatellites() {
                    this.satellites.forEach(satellite => {
                        const pulse = Math.sin(satellite.pulsePhase) * 0.3 + 0.7;
                        
                        // Satellite glow
                        const gradient = this.ctx.createRadialGradient(
                            satellite.x, satellite.y, 0,
                            satellite.x, satellite.y, satellite.size * 4
                        );
                        gradient.addColorStop(0, `${satellite.color}${Math.floor(pulse * 255).toString(16).padStart(2, '0')}`);
                        gradient.addColorStop(1, `${satellite.color}00`);
                        
                        this.ctx.fillStyle = gradient;
                        this.ctx.beginPath();
                        this.ctx.arc(satellite.x, satellite.y, satellite.size * 4, 0, Math.PI * 2);
                        this.ctx.fill();
                        
                        // Satellite body
                        this.ctx.fillStyle = satellite.color;
                        this.ctx.beginPath();
                        this.ctx.arc(satellite.x, satellite.y, satellite.size, 0, Math.PI * 2);
                        this.ctx.fill();
                        
                        // Satellite details
                        this.ctx.strokeStyle = '#ffffff';
                        this.ctx.lineWidth = 1;
                        this.ctx.beginPath();
                        this.ctx.arc(satellite.x, satellite.y, satellite.size * 0.7, 0, Math.PI * 2);
                        this.ctx.stroke();
                    });
                }
                
                drawDataFlow() {
                    // Update and draw data packets
                    for (let i = this.dataPackets.length - 1; i >= 0; i--) {
                        const packet = this.dataPackets[i];
                        const from = this.satellites[packet.from];
                        const to = this.satellites[packet.to];
                        
                        packet.progress += 0.02;
                        
                        if (packet.progress >= 1) {
                            this.dataPackets.splice(i, 1);
                            continue;
                        }
                        
                        // Calculate current position
                        const currentX = from.x + (to.x - from.x) * packet.progress;
                        const currentY = from.y + (to.y - from.y) * packet.progress;
                        
                        // Draw data packet
                        this.ctx.fillStyle = `rgba(102, 126, 234, ${1 - packet.progress})`;
                        this.ctx.beginPath();
                        this.ctx.arc(currentX, currentY, 3, 0, Math.PI * 2);
                        this.ctx.fill();
                        
                        // Draw packet trail
                        this.ctx.strokeStyle = `rgba(102, 126, 234, ${0.3 * (1 - packet.progress)})`;
                        this.ctx.lineWidth = 1;
                        this.ctx.beginPath();
                        this.ctx.moveTo(from.x, from.y);
                        this.ctx.lineTo(currentX, currentY);
                        this.ctx.stroke();
                    }
                }
                
                createDataPacket(fromIndex, toIndex) {
                    this.dataPackets.push({
                        from: fromIndex,
                        to: toIndex,
                        progress: 0
                    });
                }
            }
            
            // Initialize satellite network
            document.addEventListener('DOMContentLoaded', () => {
                new SatelliteNetwork();
            });
        </script>
        """
        components.html(satellite_js, height=320)

# =============================================================================
# ENTERPRISE AI PREDICTIVE ANALYTICS
# =============================================================================

class PredictiveAI:
    def __init__(self):
        self.historical_data = {}
    
    def predict_ship_eta(self, ship_data, destination):
        """AI predicts ship arrival time with confidence"""
        # Simulate ML model prediction
        base_hours = np.random.uniform(2.0, 48.0)
        
        # Factors: distance, speed, weather, historical patterns
        speed_factor = max(0.5, ship_data.get('Speed', 10) / 20)
        weather_factor = np.random.uniform(0.8, 1.2)
        
        predicted_hours = base_hours * speed_factor * weather_factor
        confidence = min(95, 80 + (ship_data.get('Speed', 0) * 0.5))
        
        arrival_time = datetime.now() + timedelta(hours=predicted_hours)
        
        return {
            'eta': arrival_time.strftime('%Y-%m-%d %H:%M'),
            'hours': round(predicted_hours, 1),
            'confidence': round(confidence),
            'factors': {
                'speed_impact': f"{speed_factor:.1f}x",
                'weather_impact': f"{weather_factor:.1f}x"
            }
        }
    
    def predict_port_congestion(self, port_name, hours_ahead=24):
        """Predict port congestion for next 24 hours"""
        # Simulate congestion prediction AI
        base_congestion = np.random.uniform(0.3, 0.9)
        time_of_day_factor = 0.8 + (0.4 * np.sin((datetime.now().hour / 24) * 2 * np.pi))
        
        predicted_congestion = min(1.0, base_congestion * time_of_day_factor)
        
        return {
            'congestion_level': round(predicted_congestion, 2),
            'trend': 'increasing' if predicted_congestion > 0.6 else 'stable',
            'peak_hours': ['09:00-11:00', '14:00-16:00'],
            'recommendation': self.get_congestion_recommendation(predicted_congestion)
        }
    
    def get_congestion_recommendation(self, congestion):
        if congestion > 0.8:
            return "Consider rerouting - severe congestion expected"
        elif congestion > 0.6:
            return "Moderate delays expected - schedule buffer time"
        else:
            return "Normal operations - minimal delays expected"
    
    def detect_anomalies(self, ships_data):
        """AI anomaly detection for unusual ship behavior"""
        anomalies = []
        
        for ship in ships_data:
            # Detect unusual speed patterns
            if ship.get('Speed', 0) > 25:  # Unusually fast for port area
                anomalies.append({
                    'ship_name': ship.get('Name', 'Unknown'),
                    'type': 'HIGH_SPEED',
                    'severity': 'MEDIUM',
                    'message': f"Vessel moving at {ship['Speed']} knots in port area",
                    'timestamp': datetime.now().strftime('%H:%M:%S')
                })
            
            # Detect unusual locations
            if ship.get('Status') == 'Underway' and ship.get('Speed', 0) < 2:
                anomalies.append({
                    'ship_name': ship.get('Name', 'Unknown'),
                    'type': 'DRIFTING',
                    'severity': 'LOW', 
                    'message': "Vessel appears to be drifting",
                    'timestamp': datetime.now().strftime('%H:%M:%S')
                })
        
        return anomalies

# =============================================================================
# GLOBAL MULTI-PORT SYSTEM
# =============================================================================

class GlobalPortSystem:
    def __init__(self):
        self.ports = {
            "New York": {"lat": 40.68, "lon": -74.02, "country": "USA", "timezone": "EST"},
            "Singapore": {"lat": 1.26, "lon": 103.82, "country": "Singapore", "timezone": "SGT"},
            "Rotterdam": {"lat": 51.92, "lon": 4.48, "country": "Netherlands", "timezone": "CET"},
            "Shanghai": {"lat": 31.23, "lon": 121.47, "country": "China", "timezone": "CST"},
            "Los Angeles": {"lat": 33.72, "lon": -118.27, "country": "USA", "timezone": "PST"},
            "Hamburg": {"lat": 53.54, "lon": 9.98, "country": "Germany", "timezone": "CET"},
            "Dubai": {"lat": 25.27, "lon": 55.29, "country": "UAE", "timezone": "GST"},
            "Tokyo": {"lat": 35.44, "lon": 139.77, "country": "Japan", "timezone": "JST"}
        }
    
    def get_port_ships(self, port_name):
        """Get ships for specific port with realistic local patterns"""
        port = self.ports[port_name]
        
        # Different ship patterns by region
        if port_name in ["Singapore", "Shanghai", "Tokyo"]:
            companies = ["COSCO", "Evergreen", "ONE", "Yang Ming", "HMM"]
            ship_types = ["Container", "Container", "Bulk Carrier", "Tanker"]
        elif port_name in ["Rotterdam", "Hamburg"]:
            companies = ["Maersk", "MSC", "Hapag-Lloyd", "CMA CGM"]
            ship_types = ["Container", "Ro-Ro", "General Cargo"]
        else:  # Americas
            companies = ["Maersk", "MSC", "COSCO", "CMA CGM", "Evergreen"]
            ship_types = ["Container", "Tanker", "Bulk Carrier", "Cargo"]
        
        ships = []
        base_lat, base_lon = port["lat"], port["lon"]
        
        for i in range(np.random.randint(8, 20)):
            lat = base_lat + (np.random.random() - 0.5) * 0.04
            lon = base_lon + (np.random.random() - 0.5) * 0.04
            
            company = np.random.choice(companies)
            ship_type = np.random.choice(ship_types)
            
            ships.append({
                'MMSI': f"367{i:06d}",
                'Name': f"{company} {port_name.split()[0].upper()} {i+1}",
                'Type': ship_type,
                'Company': company,
                'Latitude': round(lat, 6),
                'Longitude': round(lon, 6),
                'Speed': np.random.randint(0, 18),
                'Status': np.random.choice(["Underway", "Anchored", "Moored", "Docked"]),
                'Destination': port_name,
                'Port': port_name,
                'Timestamp': datetime.now().strftime('%H:%M:%S'),
                'Cargo_Value_M': np.random.randint(10, 150)
            })
        
        return ships

# =============================================================================
# USER AUTHENTICATION SYSTEM
# =============================================================================

class AuthSystem:
    def __init__(self):
        self.users = {
            "admin": {"password": self.hash_password("admin123"), "role": "admin", "company": "SkyWatch AI"},
            "demo": {"password": self.hash_password("demo123"), "role": "user", "company": "Demo Corp"}
        }
    
    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username, password):
        if username in self.users:
            if self.users[username]["password"] == self.hash_password(password):
                return True
        return False
    
    def get_user_role(self, username):
        return self.users.get(username, {}).get("role", "user")

# =============================================================================
# BUSINESS INTELLIGENCE ANALYTICS
# =============================================================================

class BusinessIntelligence:
    def __init__(self):
        pass
    
    def calculate_roi(self, port_efficiency_improvement):
        """Calculate ROI for clients"""
        base_savings = 50000  # $50K per day base
        efficiency_savings = base_savings * port_efficiency_improvement
        annual_savings = efficiency_savings * 365
        
        return {
            'daily_savings': f"${efficiency_savings:,.0f}",
            'annual_savings': f"${annual_savings:,.0f}",
            'efficiency_gain': f"{port_efficiency_improvement * 100:.1f}%",
            'payback_period': "3-6 months",
            'roi': f"{(annual_savings / 50000) * 100:.0f}%"
        }
    
    def generate_executive_summary(self, port_data, ships_data):
        """Generate executive-level business summary"""
        total_ships = len(ships_data)
        total_cargo_value = sum(ship.get('Cargo_Value_M', 0) for ship in ships_data)
        avg_ship_value = total_cargo_value / max(1, total_ships)
        
        return {
            'total_vessels': total_ships,
            'total_cargo_value': f"${total_cargo_value:,.0f}M",
            'average_ship_value': f"${avg_ship_value:,.1f}M",
            'port_efficiency': f"{np.random.uniform(65, 92):.1f}%",
            'risk_level': "LOW" if total_ships < 15 else "MEDIUM",
            'recommendations': [
                "Optimize berth allocation for faster turnaround",
                "Implement predictive arrival system",
                "Increase monitoring during peak hours"
            ]
        }

# =============================================================================
# MAIN ENTERPRISE APPLICATION
# =============================================================================

class SkyWatchEnterprise:
    def __init__(self):
        self.predictive_ai = PredictiveAI()
        self.port_system = GlobalPortSystem()
        self.auth_system = AuthSystem()
        self.business_intel = BusinessIntelligence()
        self.current_port = "New York"
        self.animations = PremiumCanvasAnimations()  # Add animations
    
    def run_enterprise_dashboard(self):
        """Main enterprise dashboard"""
        
        # ===== AUTHENTICATION =====
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        
        if not st.session_state.authenticated:
            self.show_login()
            return
        
        # ===== ENTERPRISE DASHBOARD =====
        self.setup_enterprise_ui()
        
        # Sidebar controls
        with st.sidebar:
            self.show_sidebar_controls()
        
        # Main dashboard
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            self.show_business_metrics()
        
        with col2:
            self.show_ai_predictions()
        
        with col3:
            self.show_port_efficiency()
        
        with col4:
            self.show_risk_alerts()
        
        # Main content area
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🌍 Global Overview", 
            "🚢 Live Tracking", 
            "📈 Analytics",
            "🤖 AI Insights",
            "💼 Business Intelligence"
        ])
        
        with tab1:
            self.show_global_overview()
        
        with tab2:
            self.show_live_tracking()
        
        with tab3:
            self.show_analytics_dashboard()
        
        with tab4:
            self.show_ai_insights()
        
        with tab5:
            self.show_business_intelligence()
    
    def show_login(self):
        """User authentication interface"""
        st.markdown("""
        <style>
        .login-container {
            max-width: 400px;
            margin: 100px auto;
            padding: 2rem;
            background: white;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        }
        </style>
        """, unsafe_allow_html=True)
        
        st.markdown('<div class="login-container">', unsafe_allow_html=True)
        st.title("🔐 SkyWatch AI Enterprise")
        st.write("**Login to access satellite intelligence platform**")
        
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        if st.button("Login", type="primary"):
            if self.auth_system.authenticate(username, password):
                st.session_state.authenticated = True
                st.session_state.username = username
                st.rerun()
            else:
                st.error("Invalid credentials")
        
        st.info("**Demo Accounts:** admin/admin123 or demo/demo123")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def setup_enterprise_ui(self):
        """Setup enterprise UI theme"""
        st.set_page_config(
            page_title="SkyWatch AI Enterprise",
            page_icon="🛰️",
            layout="wide",
            initial_sidebar_state="expanded"
        )
        
        # Custom CSS for enterprise look
        st.markdown("""
        <style>
        .enterprise-header {
            background: linear-gradient(45deg, #667eea, #764ba2);
            color: white;
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 2rem;
        }
        .metric-card {
            background: #f8f9fa;
            padding: 1.5rem;
            border-radius: 10px;
            border-left: 5px solid #667eea;
            margin: 0.5rem 0;
        }
        .prediction-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
        }
        .alert-card {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Header
        st.markdown(f"""
        <div class="enterprise-header">
            <h1>🛰️ SKYWATCH AI ENTERPRISE PLATFORM</h1>
            <h3>Global Satellite Intelligence • AI Predictive Analytics • Business Intelligence</h3>
            <p>Welcome, {st.session_state.username} | Last Updated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
        </div>
        """, unsafe_allow_html=True)
    
    def show_sidebar_controls(self):
        """Sidebar controls"""
        st.sidebar.title("Control Panel")
        
        # Port selection
        self.current_port = st.sidebar.selectbox(
            "🌍 Select Port",
            list(self.port_system.ports.keys()),
            index=0
        )
        
        # AI Settings
        st.sidebar.subheader("AI Settings")
        enable_predictions = st.sidebar.checkbox("Enable AI Predictions", True)
        alert_threshold = st.sidebar.slider("Alert Sensitivity", 1, 10, 7)
        
        # Theme settings
        st.sidebar.subheader("Display")
        theme = st.sidebar.selectbox("Theme", ["Light", "Dark"])
        
        # Logout
        if st.sidebar.button("🚪 Logout"):
            st.session_state.authenticated = False
            st.rerun()
    
    def show_business_metrics(self):
        """Business metrics cards"""
        ships_data = self.port_system.get_port_ships(self.current_port)
        total_value = sum(ship.get('Cargo_Value_M', 0) for ship in ships_data)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Active Vessels", len(ships_data), "Live")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Cargo Value", f"${total_value}M", "+12%")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def show_ai_predictions(self):
        """AI prediction cards"""
        congestion_pred = self.predictive_ai.predict_port_congestion(self.current_port)
        
        st.markdown('<div class="prediction-card">', unsafe_allow_html=True)
        st.metric("Port Congestion", f"{congestion_pred['congestion_level']*100:.0f}%")
        st.write(f"Trend: {congestion_pred['trend'].title()}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def show_port_efficiency(self):
        """Port efficiency metrics"""
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.metric("Port Efficiency", "87%", "+5%")
        st.metric("Avg Turnaround", "18h", "-2h")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def show_risk_alerts(self):
        """Risk and alert cards"""
        ships_data = self.port_system.get_port_ships(self.current_port)
        anomalies = self.predictive_ai.detect_anomalies(ships_data)
        
        st.markdown('<div class="alert-card">', unsafe_allow_html=True)
        st.metric("Active Alerts", len(anomalies))
        if anomalies:
            st.write(f"Latest: {anomalies[0]['type']}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    def show_global_overview(self):
        """Global port overview"""
        st.subheader("🌍 Global Port Network")
        
        # Add satellite network animation
        self.animations.create_satellite_network()
        
        # Create global map with all ports
        port_df = pd.DataFrame([
            {'Port': name, 'Latitude': data['lat'], 'Longitude': data['lon'], 'Country': data['country']}
            for name, data in self.port_system.ports.items()
        ])
        
        fig = px.scatter_mapbox(
            port_df,
            lat="Latitude",
            lon="Longitude", 
            hover_name="Port",
            hover_data=["Country"],
            size=[10] * len(port_df),
            color_discrete_sequence=["red"],
            zoom=1,
            height=500
        )
        fig.update_layout(mapbox_style="open-street-map")
        st.plotly_chart(fig, use_container_width=True)
        
        # Port comparison table
        st.subheader("📊 Port Performance Comparison")
        comparison_data = []
        for port_name in list(self.port_system.ports.keys())[:4]:
            ships = self.port_system.get_port_ships(port_name)
            comparison_data.append({
                'Port': port_name,
                'Active Vessels': len(ships),
                'Avg Cargo Value': f"${np.mean([s.get('Cargo_Value_M', 0) for s in ships]):.1f}M",
                'Efficiency': f"{np.random.uniform(70, 95):.1f}%"
            })
        
        st.dataframe(pd.DataFrame(comparison_data), use_container_width=True)
    
    def show_live_tracking(self):
        """Live ship tracking"""
        st.subheader(f"🚢 Live Vessel Tracking - {self.current_port}")
        
        ships_data = self.port_system.get_port_ships(self.current_port)
        
        if ships_data:
            ships_df = pd.DataFrame(ships_data)
            
            # Interactive map
            fig = px.scatter_mapbox(
                ships_df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Name",
                hover_data=["Type", "Company", "Speed", "Status"],
                color="Type",
                zoom=12,
                height=600,
                title=f"Live Vessels - {self.current_port}"
            )
            fig.update_layout(mapbox_style="open-street-map")
            st.plotly_chart(fig, use_container_width=True)
            
            # Vessel details
            st.subheader("📋 Vessel Details")
            display_cols = ['Name', 'Company', 'Type', 'Speed', 'Status', 'Cargo_Value_M']
            st.dataframe(ships_df[display_cols], use_container_width=True)
    
    def show_analytics_dashboard(self):
        """Advanced analytics dashboard"""
        st.subheader("📈 Advanced Analytics")
        
        ships_data = self.port_system.get_port_ships(self.current_port)
        ships_df = pd.DataFrame(ships_data)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Ship type distribution
            if not ships_df.empty:
                type_counts = ships_df['Type'].value_counts()
                fig_pie = px.pie(
                    values=type_counts.values, 
                    names=type_counts.index,
                    title="Vessel Type Distribution"
                )
                st.plotly_chart(fig_pie, use_container_width=True)
        
        with col2:
            # Company distribution
            if not ships_df.empty:
                company_counts = ships_df['Company'].value_counts()
                fig_bar = px.bar(
                    x=company_counts.values,
                    y=company_counts.index,
                    orientation='h',
                    title="Shipping Companies"
                )
                st.plotly_chart(fig_bar, use_container_width=True)
        
        # Time series simulation
        st.subheader("⏱️ Port Activity Timeline")
        hours = list(range(24))
        activity = [max(5, int(20 * (0.5 + 0.5 * np.sin(h/24 * 2 * np.pi)))) for h in hours]
        
        fig_line = px.line(
            x=hours, y=activity,
            title="24-Hour Port Activity Pattern",
            labels={'x': 'Hour of Day', 'y': 'Vessels in Port'}
        )
        st.plotly_chart(fig_line, use_container_width=True)
    
    def show_ai_insights(self):
        """AI-powered insights"""
        st.subheader("🤖 AI Predictive Insights")
        
        ships_data = self.port_system.get_port_ships(self.current_port)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### 📊 Port Congestion Forecast")
            congestion = self.predictive_ai.predict_port_congestion(self.current_port)
            
            st.metric("Current Level", f"{congestion['congestion_level']*100:.0f}%")
            st.metric("Trend", congestion['trend'].title())
            st.write(f"**Recommendation:** {congestion['recommendation']}")
            st.write(f"**Peak Hours:** {', '.join(congestion['peak_hours'])}")
        
        with col2:
            st.markdown("#### 🚨 Anomaly Detection")
            anomalies = self.predictive_ai.detect_anomalies(ships_data)
            
            if anomalies:
                for anomaly in anomalies[:3]:  # Show top 3
                    st.warning(f"**{anomaly['type']}** - {anomaly['message']}")
            else:
                st.success("✅ No anomalies detected")
        
        # ETA Predictions for sample ships
        st.markdown("#### ⏰ Arrival Predictions")
        if ships_data:
            sample_ships = ships_data[:3]  # Show predictions for first 3 ships
            for ship in sample_ships:
                eta_pred = self.predictive_ai.predict_ship_eta(ship, self.current_port)
                
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.write(f"**{ship['Name']}**")
                with col2:
                    st.write(f"ETA: {eta_pred['eta']}")
                with col3:
                    st.write(f"Confidence: {eta_pred['confidence']}%")
    
    def show_business_intelligence(self):
        """Business intelligence dashboard"""
        st.subheader("💼 Business Intelligence")
        
        ships_data = self.port_system.get_port_ships(self.current_port)
        
        # ROI Calculator
        st.markdown("#### 💰 ROI Calculator")
        efficiency_improvement = st.slider(
            "Expected Efficiency Improvement", 
            0.05, 0.30, 0.15, 0.05,
            help="Expected improvement in port efficiency using SkyWatch AI"
        )
        
        roi_data = self.business_intel.calculate_roi(efficiency_improvement)
        
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Daily Savings", roi_data['daily_savings'])
        with col2:
            st.metric("Annual Savings", roi_data['annual_savings'])
        with col3:
            st.metric("Efficiency Gain", roi_data['efficiency_gain'])
        with col4:
            st.metric("ROI", roi_data['roi'])
        
        # Executive Summary
        st.markdown("#### 📋 Executive Summary")
        exec_summary = self.business_intel.generate_executive_summary(
            self.current_port, ships_data
        )
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Vessels", exec_summary['total_vessels'])
            st.metric("Total Cargo Value", exec_summary['total_cargo_value'])
        with col2:
            st.metric("Port Efficiency", exec_summary['port_efficiency'])
            st.metric("Risk Level", exec_summary['risk_level'])
        
        st.markdown("#### 💡 Strategic Recommendations")
        for i, recommendation in enumerate(exec_summary['recommendations'], 1):
            st.write(f"{i}. {recommendation}")

# =============================================================================
# RUN THE ENTERPRISE APPLICATION WITH PREMIUM ANIMATIONS
# =============================================================================

def main():
    # Initialize premium animations
    premium_animations = PremiumCanvasAnimations()
    
    # Add cosmic starfield background
    premium_animations.create_cosmic_starfield()
    
    # Run enterprise dashboard
    enterprise_app = SkyWatchEnterprise()
    enterprise_app.run_enterprise_dashboard()

if __name__ == "__main__":
    main()