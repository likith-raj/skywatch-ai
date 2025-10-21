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
                body {
                    margin: 0;
                    padding: 0;
                    overflow: hidden;
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
# ULTIMATE GLOBAL MULTI-PORT SYSTEM
# =============================================================================

class GlobalPortSystem:
    def __init__(self):
        self.ports = {
            # NORTH AMERICA
            "New York": {"lat": 40.68, "lon": -74.02, "country": "USA", "region": "North America", "volume": "High"},
            "Los Angeles": {"lat": 33.72, "lon": -118.27, "country": "USA", "region": "North America", "volume": "High"},
            "Long Beach": {"lat": 33.76, "lon": -118.19, "country": "USA", "region": "North America", "volume": "High"},
            "Seattle": {"lat": 47.60, "lon": -122.33, "country": "USA", "region": "North America", "volume": "Medium"},
            "Vancouver": {"lat": 49.28, "lon": -123.11, "country": "Canada", "region": "North America", "volume": "Medium"},
            "Montreal": {"lat": 45.50, "lon": -73.55, "country": "Canada", "region": "North America", "volume": "Medium"},
            
            # EUROPE
            "Rotterdam": {"lat": 51.92, "lon": 4.48, "country": "Netherlands", "region": "Europe", "volume": "High"},
            "Hamburg": {"lat": 53.54, "lon": 9.98, "country": "Germany", "region": "Europe", "volume": "High"},
            "Antwerp": {"lat": 51.23, "lon": 4.40, "country": "Belgium", "region": "Europe", "volume": "High"},
            "Felixstowe": {"lat": 51.96, "lon": 1.35, "country": "UK", "region": "Europe", "volume": "High"},
            "Le Havre": {"lat": 49.48, "lon": 0.12, "country": "France", "region": "Europe", "volume": "Medium"},
            "Bremen": {"lat": 53.08, "lon": 8.80, "country": "Germany", "region": "Europe", "volume": "Medium"},
            "Valencia": {"lat": 39.45, "lon": -0.32, "country": "Spain", "region": "Europe", "volume": "Medium"},
            "Piraeus": {"lat": 37.94, "lon": 23.64, "country": "Greece", "region": "Europe", "volume": "Medium"},
            
            # ASIA
            "Shanghai": {"lat": 31.23, "lon": 121.47, "country": "China", "region": "Asia", "volume": "Very High"},
            "Singapore": {"lat": 1.26, "lon": 103.82, "country": "Singapore", "region": "Asia", "volume": "Very High"},
            "Shenzhen": {"lat": 22.54, "lon": 114.05, "country": "China", "region": "Asia", "volume": "Very High"},
            "Ningbo": {"lat": 29.86, "lon": 121.55, "country": "China", "region": "Asia", "volume": "Very High"},
            "Hong Kong": {"lat": 22.28, "lon": 114.16, "country": "China", "region": "Asia", "volume": "High"},
            "Busan": {"lat": 35.10, "lon": 129.04, "country": "South Korea", "region": "Asia", "volume": "High"},
            "Tokyo": {"lat": 35.44, "lon": 139.77, "country": "Japan", "region": "Asia", "volume": "High"},
            "Yokohama": {"lat": 35.44, "lon": 139.64, "country": "Japan", "region": "Asia", "volume": "High"},
            "Kaohsiung": {"lat": 22.61, "lon": 120.28, "country": "Taiwan", "region": "Asia", "volume": "High"},
            "Port Klang": {"lat": 3.00, "lon": 101.40, "country": "Malaysia", "region": "Asia", "volume": "High"},
            "Colombo": {"lat": 6.94, "lon": 79.84, "country": "Sri Lanka", "region": "Asia", "volume": "Medium"},
            "Dubai": {"lat": 25.27, "lon": 55.29, "country": "UAE", "region": "Middle East", "volume": "High"},
            "Jebel Ali": {"lat": 25.02, "lon": 55.06, "country": "UAE", "region": "Middle East", "volume": "High"},
            
            # SOUTH AMERICA
            "Santos": {"lat": -23.96, "lon": -46.33, "country": "Brazil", "region": "South America", "volume": "High"},
            "Buenos Aires": {"lat": -34.60, "lon": -58.37, "country": "Argentina", "region": "South America", "volume": "Medium"},
            "Callao": {"lat": -12.06, "lon": -77.15, "country": "Peru", "region": "South America", "volume": "Medium"},
            "Cartagena": {"lat": 10.39, "lon": -75.51, "country": "Colombia", "region": "South America", "volume": "Medium"},
            
            # AFRICA
            "Durban": {"lat": -29.87, "lon": 31.04, "country": "South Africa", "region": "Africa", "volume": "Medium"},
            "Mombasa": {"lat": -4.06, "lon": 39.67, "country": "Kenya", "region": "Africa", "volume": "Medium"},
            "Lagos": {"lat": 6.45, "lon": 3.40, "country": "Nigeria", "region": "Africa", "volume": "Medium"},
            "Alexandria": {"lat": 31.20, "lon": 29.89, "country": "Egypt", "region": "Africa", "volume": "Medium"},
            
            # OCEANIA
            "Sydney": {"lat": -33.86, "lon": 151.20, "country": "Australia", "region": "Oceania", "volume": "Medium"},
            "Melbourne": {"lat": -37.84, "lon": 144.94, "country": "Australia", "region": "Oceania", "volume": "Medium"},
            "Auckland": {"lat": -36.84, "lon": 174.76, "country": "New Zealand", "region": "Oceania", "volume": "Low"}
        }
        
        # Regional company patterns
        self.regional_companies = {
            "Asia": ["COSCO", "Evergreen", "ONE", "Yang Ming", "HMM", "OOCL", "PIL"],
            "Europe": ["Maersk", "MSC", "Hapag-Lloyd", "CMA CGM", "Hamburg Sud"],
            "North America": ["Maersk", "MSC", "COSCO", "CMA CGM", "Evergreen", "Matson"],
            "South America": ["Maersk", "MSC", "COSCO", "Hapag-Lloyd", "Grimaldi"],
            "Africa": ["Maersk", "MSC", "CMA CGM", "COSCO", "Safmarine"],
            "Middle East": ["Maersk", "MSC", "COSCO", "Hapag-Lloyd", "UASC"],
            "Oceania": ["Maersk", "MSC", "COSCO", "Hapag-Lloyd", "ANL"]
        }
        
        self.regional_ship_types = {
            "Asia": ["Container", "Container", "Bulk Carrier", "Tanker", "General Cargo"],
            "Europe": ["Container", "Ro-Ro", "General Cargo", "Tanker", "Bulk Carrier"],
            "North America": ["Container", "Tanker", "Bulk Carrier", "Vehicle Carrier", "General Cargo"],
            "South America": ["Bulk Carrier", "Container", "Tanker", "General Cargo"],
            "Africa": ["General Cargo", "Container", "Bulk Carrier", "Tanker"],
            "Middle East": ["Tanker", "Container", "Bulk Carrier", "General Cargo"],
            "Oceania": ["Container", "Bulk Carrier", "General Cargo", "Vehicle Carrier"]
        }
    
    def get_port_ships(self, port_name):
        """Get ships for specific port with realistic regional patterns"""
        port = self.ports[port_name]
        region = port.get('region', 'Asia')
        
        # Get regional-specific companies and ship types
        companies = self.regional_companies.get(region, ["Maersk", "MSC", "COSCO"])
        ship_types = self.regional_ship_types.get(region, ["Container", "Tanker", "Bulk Carrier"])
        
        # Adjust ship count based on port volume
        volume_multiplier = {
            'Very High': 1.5,
            'High': 1.2,
            'Medium': 1.0,
            'Low': 0.7
        }
        base_count = 15
        ship_count = int(base_count * volume_multiplier.get(port.get('volume', 'Medium'), 1.0))
        
        ships = []
        base_lat, base_lon = port["lat"], port["lon"]
        
        for i in range(np.random.randint(ship_count-5, ship_count+5)):
            lat = base_lat + (np.random.random() - 0.5) * 0.06
            lon = base_lon + (np.random.random() - 0.5) * 0.06
            
            company = np.random.choice(companies)
            ship_type = np.random.choice(ship_types)
            
            # Adjust cargo value based on ship type and region
            base_value = {
                'Container': np.random.randint(20, 100),
                'Tanker': np.random.randint(50, 150),
                'Bulk Carrier': np.random.randint(10, 60),
                'Cargo': np.random.randint(5, 40),
                'Ro-Ro': np.random.randint(15, 80),
                'Vehicle Carrier': np.random.randint(25, 90),
                'General Cargo': np.random.randint(8, 50)
            }.get(ship_type, 30)
            
            # Asian ports have higher values
            if region == 'Asia':
                base_value = int(base_value * 1.3)
            
            ships.append({
                'MMSI': f"367{np.random.randint(100000, 999999)}",
                'Name': f"{company} {np.random.choice(['SEA', 'OCEAN', 'MARINE', 'GLOBAL', 'WORLD'])} {np.random.randint(1000, 9999)}",
                'Type': ship_type,
                'Company': company,
                'Latitude': round(lat, 6),
                'Longitude': round(lon, 6),
                'Speed': np.random.randint(0, 22),
                'Status': np.random.choice(["Underway", "Anchored", "Moored", "Docked", "Berthed"]),
                'Destination': port_name,
                'Port': port_name,
                'Timestamp': datetime.now().strftime('%H:%M:%S'),
                'Cargo_Value_M': base_value
            })
        
        return ships

# =============================================================================
# USER AUTHENTICATION SYSTEM
# =============================================================================

class AuthSystem:
    def __init__(self):
        self.users = {
            'admin': {
                'password': self._hash_password('admin123'),
                'role': 'admin',
                'name': 'System Administrator'
            },
            'operator': {
                'password': self._hash_password('operator123'),
                'role': 'operator', 
                'name': 'Port Operator'
            },
            'viewer': {
                'password': self._hash_password('viewer123'),
                'role': 'viewer',
                'name': 'Viewer'
            }
        }
    
    def _hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()
    
    def authenticate(self, username, password):
        if username in self.users:
            if self.users[username]['password'] == self._hash_password(password):
                return True, self.users[username]
        return False, None

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

class SkyWatchAIEnterprise:
    def __init__(self):
        self.auth_system = AuthSystem()
        self.port_system = GlobalPortSystem()
        self.predictive_ai = PredictiveAI()
        self.business_intel = BusinessIntelligence()
        self.animations = PremiumCanvasAnimations()
        
        # Initialize session state
        if 'authenticated' not in st.session_state:
            st.session_state.authenticated = False
        if 'current_user' not in st.session_state:
            st.session_state.current_user = None
        if 'selected_port' not in st.session_state:
            st.session_state.selected_port = "Singapore"
        if 'auto_refresh' not in st.session_state:
            st.session_state.auto_refresh = True
    
    def add_premium_styles(self):
        """Add premium CSS styles"""
        st.markdown("""
        <style>
            /* Premium Glass Morphism */
            .glass-card {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(20px);
                -webkit-backdrop-filter: blur(20px);
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 20px;
                padding: 2rem;
                margin: 1rem 0;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
                transition: all 0.3s ease;
            }
            
            .glass-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 15px 40px rgba(102, 126, 234, 0.4);
                border: 1px solid rgba(102, 126, 234, 0.5);
            }
            
            /* Animated Background */
            .animated-gradient {
                background: linear-gradient(-45deg, #0c0c2e, #1a1a3e, #2d2d5e, #3d3d7e);
                background-size: 400% 400%;
                animation: gradientShift 15s ease infinite;
            }
            
            @keyframes gradientShift {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }
            
            /* Enhanced Metrics */
            .metric-card {
                background: linear-gradient(135deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
                border: 1px solid rgba(102, 126, 234, 0.3);
                border-radius: 15px;
                padding: 1.5rem;
                margin: 0.5rem;
                transition: all 0.3s ease;
                position: relative;
                overflow: hidden;
            }
            
            .metric-card::before {
                content: '';
                position: absolute;
                top: 0;
                left: 0;
                right: 0;
                height: 2px;
                background: linear-gradient(90deg, #667eea, #764ba2, #f093fb);
            }
            
            .metric-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
            }
            
            /* Premium Button */
            .stButton button {
                background: linear-gradient(45deg, #667eea, #764ba2);
                border: none;
                border-radius: 25px;
                padding: 12px 30px;
                color: white;
                font-weight: bold;
                text-transform: uppercase;
                letter-spacing: 1px;
                transition: all 0.3s ease;
            }
            
            .stButton button:hover {
                transform: translateY(-2px);
                box-shadow: 0 10px 20px rgba(102, 126, 234, 0.4);
            }
            
            /* Live Indicator */
            .live-indicator {
                display: inline-block;
                width: 8px;
                height: 8px;
                background: #ff6b6b;
                border-radius: 50%;
                margin-right: 8px;
                animation: livePulse 1.5s infinite;
            }
            
            @keyframes livePulse {
                0% { transform: scale(1); opacity: 1; }
                50% { transform: scale(1.5); opacity: 0.7; }
                100% { transform: scale(1); opacity: 1; }
            }
            
            /* Hide Streamlit elements */
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
        </style>
        """, unsafe_allow_html=True)
    
    def login_page(self):
        """Enhanced login page with premium styling"""
        st.markdown("""
        <div style='text-align: center; padding: 5rem 0;'>
            <h1 style='color: #667eea; font-size: 3.5rem; margin-bottom: 1rem;'>🌌 SkyWatch AI Enterprise</h1>
            <p style='color: #a0a0c0; font-size: 1.2rem;'>Advanced Maritime Intelligence Platform</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col2:
            with st.container():
                st.markdown("<div class='glass-card'>", unsafe_allow_html=True)
                
                st.markdown("""
                <h2 style='text-align: center; color: #667eea; margin-bottom: 2rem;'>🔐 Secure Login</h2>
                """, unsafe_allow_html=True)
                
                username = st.text_input("👤 Username", placeholder="Enter your username")
                password = st.text_input("🔒 Password", type="password", placeholder="Enter your password")
                
                col1, col2, col3 = st.columns([1, 2, 1])
                with col2:
                    if st.button("🚀 Login", use_container_width=True):
                        success, user_info = self.auth_system.authenticate(username, password)
                        if success:
                            st.session_state.authenticated = True
                            st.session_state.current_user = user_info
                            st.success(f"Welcome {user_info['name']}!")
                            time.sleep(1)
                            st.rerun()
                        else:
                            st.error("Invalid credentials. Please try again.")
                
                st.markdown("""
                <div style='text-align: center; margin-top: 2rem; color: #a0a0c0;'>
                    <p><strong>Demo Credentials:</strong></p>
                    <p>👑 admin / admin123</p>
                    <p>⚡ operator / operator123</p>
                    <p>👀 viewer / viewer123</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("</div>", unsafe_allow_html=True)
    
    def dashboard_header(self):
        """Premium dashboard header"""
        col1, col2, col3 = st.columns([1, 2, 1])
        
        with col1:
            st.markdown(f"""
            <div style='text-align: left;'>
                <h3 style='color: #667eea; margin: 0;'>👤 {st.session_state.current_user['name']}</h3>
                <p style='color: #a0a0c0; margin: 0;'>{st.session_state.current_user['role'].title()}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div style='text-align: center;'>
                <h1 style='color: #667eea; margin: 0;'>🌌 SkyWatch AI Enterprise</h1>
                <p style='color: #a0a0c0; margin: 0;'>Real-time Global Maritime Intelligence</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            if st.button("🚪 Logout"):
                st.session_state.authenticated = False
                st.session_state.current_user = None
                st.rerun()
        
        st.markdown("---")
    
    def global_overview(self):
        """Global overview with premium metrics"""
        st.markdown("""
        <div style='text-align: center; margin-bottom: 2rem;'>
            <h2>🌍 Global Maritime Overview</h2>
            <p style='color: #a0a0c0;'>Real-time monitoring across all major ports</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Key Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>🚢 Total Vessels</h3>
                <h1 style='color: #fff; margin: 1rem 0;'>2,847</h1>
                <p style='color: #a0a0c0; margin: 0;'>+12 this hour</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>💰 Cargo Value</h3>
                <h1 style='color: #fff; margin: 1rem 0;'>$42.8B</h1>
                <p style='color: #a0a0c0; margin: 0;'>Active shipments</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>⚡ Port Efficiency</h3>
                <h1 style='color: #fff; margin: 1rem 0;'>87%</h1>
                <p style='color: #a0a0c0; margin: 0;'>Global average</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin: 0;'>🌡️ AI Predictions</h3>
                <h1 style='color: #fff; margin: 1rem 0;'>94%</h1>
                <p style='color: #a0a0c0; margin: 0;'>Accuracy rate</p>
            </div>
            """, unsafe_allow_html=True)
    
    def port_monitoring(self):
        """Advanced port monitoring section"""
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0 2rem 0;'>
            <h2>🏢 Port Monitoring & Analytics</h2>
            <p style='color: #a0a0c0;'>Real-time vessel tracking and port operations</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Port Selection
        col1, col2 = st.columns([2, 1])
        
        with col1:
            selected_port = st.selectbox(
                "Select Port",
                list(self.port_system.ports.keys()),
                index=list(self.port_system.ports.keys()).index(st.session_state.selected_port)
            )
            st.session_state.selected_port = selected_port
        
        with col2:
            st.session_state.auto_refresh = st.checkbox("🔄 Live Auto-Refresh", value=True)
        
        # Get port data
        port_data = self.port_system.ports[selected_port]
        ships_data = self.port_system.get_port_ships(selected_port)
        
        # Port Information
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown(f"""
            <div class='glass-card'>
                <h3 style='color: #667eea;'>📍 Port Details</h3>
                <p><strong>Country:</strong> {port_data['country']}</p>
                <p><strong>Region:</strong> {port_data['region']}</p>
                <p><strong>Volume:</strong> {port_data['volume']}</p>
                <p><strong>Coordinates:</strong> {port_data['lat']:.2f}, {port_data['lon']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            # AI Predictions
            congestion_prediction = self.predictive_ai.predict_port_congestion(selected_port)
            st.markdown(f"""
            <div class='glass-card'>
                <h3 style='color: #667eea;'>🤖 AI Predictions</h3>
                <p><strong>Congestion Level:</strong> {congestion_prediction['congestion_level']*100}%</p>
                <p><strong>Trend:</strong> {congestion_prediction['trend'].title()}</p>
                <p><strong>Peak Hours:</strong> {', '.join(congestion_prediction['peak_hours'])}</p>
                <p><strong>Recommendation:</strong> {congestion_prediction['recommendation']}</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            # Real-time Statistics
            total_ships = len(ships_data)
            moving_ships = len([s for s in ships_data if s['Speed'] > 0])
            avg_speed = np.mean([s['Speed'] for s in ships_data])
            total_cargo = sum([s['Cargo_Value_M'] for s in ships_data])
            
            st.markdown(f"""
            <div class='glass-card'>
                <h3 style='color: #667eea;'>📊 Live Statistics</h3>
                <p><strong>Total Vessels:</strong> {total_ships}</p>
                <p><strong>Moving Vessels:</strong> {moving_ships}</p>
                <p><strong>Avg Speed:</strong> {avg_speed:.1f} knots</p>
                <p><strong>Cargo Value:</strong> ${total_cargo}M</p>
            </div>
            """, unsafe_allow_html=True)
        
        # Ships Data Table
        st.markdown("### 🚢 Active Vessels")
        if ships_data:
            df = pd.DataFrame(ships_data)
            st.dataframe(df[['Name', 'Type', 'Company', 'Speed', 'Status', 'Cargo_Value_M', 'Timestamp']], 
                        use_container_width=True)
        else:
            st.info("No vessel data available for this port.")
        
        # Anomaly Detection
        anomalies = self.predictive_ai.detect_anomalies(ships_data)
        if anomalies:
            st.markdown("### ⚠️ AI Anomaly Detection")
            for anomaly in anomalies:
                st.warning(f"**{anomaly['type']}** - {anomaly['message']} ({anomaly['timestamp']})")
    
    def satellite_network_view(self):
        """Premium satellite network visualization"""
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0 2rem 0;'>
            <h2>🛰️ Global Satellite Network</h2>
            <p style='color: #a0a0c0;'>Real-time data flow and communication network</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Add the satellite network animation
        self.animations.create_satellite_network()
        
        # Satellite Metrics
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown("""
            <div class='metric-card'>
                <h4 style='color: #667eea; margin: 0;'>Active Satellites</h4>
                <h2 style='color: #fff; margin: 0.5rem 0;'>42</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class='metric-card'>
                <h4 style='color: #667eea; margin: 0;'>Data Flow</h4>
                <h2 style='color: #fff; margin: 0.5rem 0;'>2.4 GB/s</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class='metric-card'>
                <h4 style='color: #667eea; margin: 0;'>Uptime</h4>
                <h2 style='color: #fff; margin: 0.5rem 0;'>99.98%</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown("""
            <div class='metric-card'>
                <h4 style='color: #667eea; margin: 0;'>Coverage</h4>
                <h2 style='color: #fff; margin: 0.5rem 0;'>Global</h2>
            </div>
            """, unsafe_allow_html=True)
    
    def analytics_dashboard(self):
        """Advanced analytics with interactive visualizations"""
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0 2rem 0;'>
            <h2>📈 Advanced Analytics</h2>
            <p style='color: #a0a0c0;'>AI-powered insights and predictive analytics</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            # Ship Type Distribution
            ships_data = self.port_system.get_port_ships(st.session_state.selected_port)
            if ships_data:
                ship_types = [ship['Type'] for ship in ships_data]
                type_counts = pd.Series(ship_types).value_counts()
                
                fig = px.pie(
                    values=type_counts.values,
                    names=type_counts.index,
                    title="🚢 Vessel Type Distribution",
                    color_discrete_sequence=px.colors.sequential.Blues_r
                )
                fig.update_traces(textposition='inside', textinfo='percent+label')
                st.plotly_chart(fig, use_container_width=True)
        
        with col2:
            # Cargo Value by Company
            if ships_data:
                company_data = {}
                for ship in ships_data:
                    company = ship['Company']
                    value = ship['Cargo_Value_M']
                    if company in company_data:
                        company_data[company] += value
                    else:
                        company_data[company] = value
                
                fig = px.bar(
                    x=list(company_data.keys()),
                    y=list(company_data.values()),
                    title="💰 Cargo Value by Shipping Company",
                    labels={'x': 'Company', 'y': 'Cargo Value (M$)'},
                    color=list(company_data.values()),
                    color_continuous_scale='Viridis'
                )
                st.plotly_chart(fig, use_container_width=True)
        
        # Time Series Analysis
        st.markdown("### 📊 Port Activity Timeline")
        
        # Generate sample time series data
        hours = list(range(24))
        activity_levels = [max(0, min(100, 50 + 30 * np.sin(h/24 * 2 * np.pi) + np.random.normal(0, 10))) for h in hours]
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=hours,
            y=activity_levels,
            mode='lines+markers',
            name='Port Activity',
            line=dict(color='#667eea', width=3),
            marker=dict(size=6)
        ))
        
        fig.update_layout(
            title="24-Hour Port Activity Forecast",
            xaxis_title="Hour of Day",
            yaxis_title="Activity Level (%)",
            template="plotly_dark",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    def business_intelligence(self):
        """Business intelligence dashboard"""
        st.markdown("""
        <div style='text-align: center; margin: 3rem 0 2rem 0;'>
            <h2>💼 Business Intelligence</h2>
            <p style='color: #a0a0c0;'>ROI Analysis and Strategic Insights</p>
        </div>
        """, unsafe_allow_html=True)
        
        ships_data = self.port_system.get_port_ships(st.session_state.selected_port)
        
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
            st.session_state.selected_port, ships_data
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
    
    def show_global_real_time_map(self):
        """Enhanced global real-time map with all features"""
        st.markdown("""
        <div style='text-align: center; margin: 2rem 0;'>
            <h2>🌍 Global Real-Time Shipping Network</h2>
            <p style='color: #a0a0c0;'>Live vessel tracking across all major ports worldwide</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Create a massive dataset of ships across all ports
        all_ships = []
        for port_name in self.port_system.ports.keys():
            port_ships = self.port_system.get_port_ships(port_name)
            all_ships.extend(port_ships)
        
        if all_ships:
            all_ships_df = pd.DataFrame(all_ships)
            
            # Create unique color mapping for ship types
            ship_type_colors = {
                'Container': '#FF6B6B',
                'Tanker': '#4ECDC4', 
                'Bulk Carrier': '#45B7D1',
                'Cargo': '#96CEB4',
                'Ro-Ro': '#FFEAA7',
                'Vehicle Carrier': '#DDA0DD',
                'General Cargo': '#98D8C8'
            }
            
            # Create the global map
            fig = px.scatter_mapbox(
                all_ships_df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Name",
                hover_data={
                    "Type": True,
                    "Company": True,
                    "Speed": True,
                    "Port": True,
                    "Cargo_Value_M": True,
                    "Timestamp": True
                },
                color="Type",
                color_discrete_map=ship_type_colors,
                zoom=1,
                height=700,
                title="🚢 LIVE GLOBAL SHIPPING NETWORK - Real-Time Vessel Tracking",
                size_max=15
            )
            
            # Add port locations as larger points
            port_df = pd.DataFrame([
                {
                    'Port': name, 
                    'Latitude': data['lat'], 
                    'Longitude': data['lon'], 
                    'Country': data['country'],
                    'Volume': data['volume'],
                    'Size': 20 if data['volume'] in ['Very High', 'High'] else 15
                }
                for name, data in self.port_system.ports.items()
            ])
            
            # Add ports to the map
            fig.add_trace(px.scatter_mapbox(
                port_df,
                lat="Latitude",
                lon="Longitude",
                hover_name="Port",
                hover_data={"Country": True, "Volume": True},
                size="Size",
                size_max=20,
                color_discrete_sequence=["red"]
            ).data[0])
            
            fig.update_layout(
                mapbox_style="dark",
                mapbox=dict(
                    accesstoken=None,
                    center=dict(lat=20, lon=0),
                    zoom=1
                ),
                showlegend=True,
                legend=dict(
                    yanchor="top",
                    y=0.99,
                    xanchor="left",
                    x=0.01,
                    bgcolor="rgba(0,0,0,0.5)"
                ),
                margin={"r":0,"t":50,"l":0,"b":0}
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Global statistics
            st.markdown("### 📊 Global Shipping Intelligence")
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                total_ships = len(all_ships)
                st.metric("Total Active Vessels", f"{total_ships:,}")
            
            with col2:
                total_value = sum(ship.get('Cargo_Value_M', 0) for ship in all_ships)
                st.metric("Total Cargo Value", f"${total_value:,.0f}M")
            
            with col3:
                avg_speed = np.mean([ship.get('Speed', 0) for ship in all_ships])
                st.metric("Avg Speed", f"{avg_speed:.1f} knots")
            
            with col4:
                container_ships = len([s for s in all_ships if s.get('Type') == 'Container'])
                st.metric("Container Ships", f"{container_ships:,}")
    
    def run_enterprise_dashboard(self):
        """Main enterprise dashboard"""
        # Add cosmic background
        self.animations.create_cosmic_starfield()
        
        # Add premium styles
        self.add_premium_styles()
        
        if not st.session_state.authenticated:
            self.login_page()
            return
        
        # Main Dashboard
        self.dashboard_header()
        
        # Navigation
        tab1, tab2, tab3, tab4, tab5 = st.tabs([
            "🌍 Global Overview", 
            "🏢 Port Monitoring", 
            "🛰️ Satellite Network", 
            "📈 Analytics",
            "💼 Business Intelligence"
        ])
        
        with tab1:
            self.global_overview()
            self.show_global_real_time_map()
            
        with tab2:
            self.port_monitoring()
            
        with tab3:
            self.satellite_network_view()
            
        with tab4:
            self.analytics_dashboard()
            
        with tab5:
            self.business_intelligence()
        
        # Auto-refresh functionality
        if st.session_state.auto_refresh:
            time.sleep(5)
            st.rerun()

# =============================================================================
# APPLICATION ENTRY POINT
# =============================================================================

def main():
    # Configure page
    st.set_page_config(
        page_title="SkyWatch AI Enterprise",
        page_icon="🌌",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    # Initialize and run application
    app = SkyWatchAIEnterprise()
    app.run_enterprise_dashboard()

if __name__ == "__main__":
    main()