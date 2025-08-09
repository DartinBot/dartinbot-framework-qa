# DartinBot IoT Development Template

<dartinbot-template 
    name="IoT Development Template"
    category="iot"
    version="3.0.0"
    framework-version="3.0.0"
    scope="iot-device-cloud-integration"
    difficulty="advanced"
    confidence-score="0.89"
    auto-improve="true">

## Project Overview
<dartinbot-detect>
Target: IoT device development with cloud integration and edge computing
Tech Stack: Arduino, Raspberry Pi, MQTT, AWS IoT, Python, C++
Purpose: Build connected IoT solutions with device management and data analytics
</dartinbot-detect>

## Tech Stack Configuration
<dartinbot-brain 
    specialty="iot-development"
    model="gpt-4"
    focus="embedded-systems,mqtt,cloud-integration,edge-computing"
    expertise-level="advanced">

### Device Development
- **Microcontrollers**: Arduino (ESP32, ESP8266), Raspberry Pi
- **Programming**: C/C++ for Arduino, Python for Raspberry Pi
- **Sensors**: Temperature, Humidity, Motion, GPS, Camera
- **Connectivity**: WiFi, Bluetooth, LoRaWAN, Cellular
- **Protocols**: MQTT, HTTP/HTTPS, CoAP, WebSocket

### Cloud Integration
- **Platform**: AWS IoT Core, Google Cloud IoT, Azure IoT Hub
- **Data Storage**: AWS S3, DynamoDB, InfluxDB
- **Real-time Processing**: AWS Kinesis, Apache Kafka
- **Analytics**: AWS Analytics, Google BigQuery
- **Device Management**: AWS IoT Device Management

### Edge Computing
- **Edge Runtime**: AWS IoT Greengrass, Azure IoT Edge
- **Container**: Docker for ARM, Kubernetes
- **ML at Edge**: TensorFlow Lite, AWS IoT SiteWise
- **Local Processing**: Node-RED, Apache NiFi
- **Security**: Hardware Security Module (HSM)

## Project Structure

### IoT Project Structure
```
iot-project/
├── devices/
│   ├── arduino/
│   │   ├── esp32_sensor/
│   │   │   ├── main.cpp
│   │   │   ├── config.h
│   │   │   ├── sensors.cpp
│   │   │   └── wifi_manager.cpp
│   │   └── libraries/
│   │       ├── MQTTClient/
│   │       └── SensorLib/
│   ├── raspberry_pi/
│   │   ├── gateway/
│   │   │   ├── main.py
│   │   │   ├── mqtt_handler.py
│   │   │   ├── sensor_reader.py
│   │   │   └── data_processor.py
│   │   └── edge_ml/
│   │       ├── model_inference.py
│   │       ├── model_trainer.py
│   │       └── models/
├── cloud/
│   ├── aws/
│   │   ├── iot_core/
│   │   │   ├── thing_types.json
│   │   │   ├── policies.json
│   │   │   └── rules.json
│   │   ├── lambda/
│   │   │   ├── data_processor/
│   │   │   ├── device_manager/
│   │   │   └── alert_handler/
│   │   └── cloudformation/
│   │       └── iot_infrastructure.yaml
│   ├── api/
│   │   ├── device_api.py
│   │   ├── data_api.py
│   │   └── dashboard_api.py
│   └── analytics/
│       ├── data_pipeline.py
│       ├── ml_models.py
│       └── dashboards/
├── dashboard/
│   ├── web/
│   │   ├── src/
│   │   │   ├── components/
│   │   │   ├── pages/
│   │   │   └── services/
│   │   └── public/
│   └── mobile/
│       ├── src/
│       └── assets/
├── edge/
│   ├── containers/
│   │   ├── data_collector/
│   │   ├── ml_inference/
│   │   └── local_storage/
│   ├── orchestration/
│   │   ├── docker-compose.yml
│   │   └── kubernetes/
│   └── configs/
│       ├── edge_config.json
│       └── ml_config.yaml
├── tests/
│   ├── device_tests/
│   ├── integration_tests/
│   └── performance_tests/
├── docs/
│   ├── device_setup.md
│   ├── cloud_deployment.md
│   └── troubleshooting.md
└── scripts/
    ├── provision_devices.py
    ├── deploy_cloud.sh
    └── monitor_health.py
```

## Device Development

### ESP32 Sensor Node
<dartinbot-device type="arduino-esp32">
```cpp
#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>
#include <ArduinoJson.h>
#include <WiFiClientSecure.h>
#include "config.h"

// Sensor definitions
#define DHT_PIN 4
#define DHT_TYPE DHT22
#define MOTION_PIN 2
#define LED_PIN 13

// Initialize sensors
DHT dht(DHT_PIN, DHT_TYPE);

// WiFi and MQTT clients
WiFiClientSecure wifiClient;
PubSubClient mqttClient(wifiClient);

// Device configuration
const char* deviceId = "esp32_sensor_001";
const char* topicPublish = "sensors/data";
const char* topicSubscribe = "devices/commands";

// Timing
unsigned long lastSensorRead = 0;
unsigned long sensorInterval = 5000; // 5 seconds

void setup() {
  Serial.begin(115200);
  
  // Initialize pins
  pinMode(MOTION_PIN, INPUT);
  pinMode(LED_PIN, OUTPUT);
  
  // Initialize sensors
  dht.begin();
  
  // Connect to WiFi
  connectWiFi();
  
  // Configure MQTT
  configureMQTT();
  
  Serial.println("ESP32 sensor node initialized");
}

void loop() {
  // Ensure MQTT connection
  if (!mqttClient.connected()) {
    reconnectMQTT();
  }
  mqttClient.loop();
  
  // Read sensors periodically
  if (millis() - lastSensorRead > sensorInterval) {
    readAndPublishSensors();
    lastSensorRead = millis();
  }
  
  // Handle deep sleep for power saving
  handlePowerManagement();
  
  delay(100);
}

void connectWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  
  Serial.print("Connecting to WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  
  Serial.println();
  Serial.print("Connected to WiFi. IP: ");
  Serial.println(WiFi.localIP());
}

void configureMQTT() {
  // Configure SSL/TLS
  wifiClient.setCACert(AWS_CERT_CA);
  wifiClient.setCertificate(AWS_CERT_CRT);
  wifiClient.setPrivateKey(AWS_CERT_PRIVATE);
  
  // Set MQTT server
  mqttClient.setServer(AWS_IOT_ENDPOINT, 8883);
  mqttClient.setCallback(mqttCallback);
  
  // Connect to MQTT
  reconnectMQTT();
}

void reconnectMQTT() {
  while (!mqttClient.connected()) {
    Serial.print("Attempting MQTT connection...");
    
    if (mqttClient.connect(deviceId)) {
      Serial.println("connected");
      
      // Subscribe to command topic
      mqttClient.subscribe(topicSubscribe);
      
      // Publish device online status
      publishDeviceStatus("online");
      
    } else {
      Serial.print("failed, rc=");
      Serial.print(mqttClient.state());
      Serial.println(" retrying in 5 seconds");
      delay(5000);
    }
  }
}

void readAndPublishSensors() {
  // Read sensors
  float temperature = dht.readTemperature();
  float humidity = dht.readHumidity();
  bool motion = digitalRead(MOTION_PIN);
  
  // Check if readings are valid
  if (isnan(temperature) || isnan(humidity)) {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  
  // Create JSON payload
  StaticJsonDocument<200> doc;
  doc["deviceId"] = deviceId;
  doc["timestamp"] = millis();
  doc["temperature"] = temperature;
  doc["humidity"] = humidity;
  doc["motion"] = motion;
  doc["battery"] = readBatteryLevel();
  doc["rssi"] = WiFi.RSSI();
  
  // Serialize JSON
  char jsonBuffer[256];
  serializeJson(doc, jsonBuffer);
  
  // Publish to MQTT
  if (mqttClient.publish(topicPublish, jsonBuffer)) {
    Serial.printf("Published: %s\n", jsonBuffer);
    blinkLED(1); // Indicate successful transmission
  } else {
    Serial.println("Failed to publish sensor data");
    blinkLED(3); // Indicate error
  }
}

void mqttCallback(char* topic, byte* payload, unsigned int length) {
  // Parse incoming commands
  StaticJsonDocument<200> doc;
  deserializeJson(doc, payload, length);
  
  String command = doc["command"];
  
  if (command == "setSensorInterval") {
    sensorInterval = doc["interval"];
    Serial.printf("Sensor interval updated to: %lu ms\n", sensorInterval);
  }
  else if (command == "reboot") {
    Serial.println("Rebooting device...");
    ESP.restart();
  }
  else if (command == "led") {
    bool state = doc["state"];
    digitalWrite(LED_PIN, state);
    Serial.printf("LED set to: %s\n", state ? "ON" : "OFF");
  }
}

void publishDeviceStatus(const char* status) {
  StaticJsonDocument<100> doc;
  doc["deviceId"] = deviceId;
  doc["status"] = status;
  doc["timestamp"] = millis();
  
  char jsonBuffer[128];
  serializeJson(doc, jsonBuffer);
  
  mqttClient.publish("devices/status", jsonBuffer);
}

float readBatteryLevel() {
  // Read battery voltage (assuming voltage divider)
  int adcValue = analogRead(A0);
  float voltage = (adcValue / 4095.0) * 3.3 * 2; // Voltage divider factor
  float percentage = ((voltage - 3.0) / (4.2 - 3.0)) * 100;
  
  return constrain(percentage, 0, 100);
}

void blinkLED(int times) {
  for (int i = 0; i < times; i++) {
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    digitalWrite(LED_PIN, LOW);
    delay(100);
  }
}

void handlePowerManagement() {
  float batteryLevel = readBatteryLevel();
  
  // Enter deep sleep if battery is low
  if (batteryLevel < 10) {
    Serial.println("Low battery. Entering deep sleep...");
    publishDeviceStatus("sleeping");
    
    // Wake up every 30 minutes
    esp_sleep_enable_timer_wakeup(30 * 60 * 1000000);
    esp_deep_sleep_start();
  }
}
```
</dartinbot-device>

### Raspberry Pi Gateway
<dartinbot-device type="raspberry-pi">
```python
import json
import time
import logging
import threading
from datetime import datetime
from typing import Dict, Any, List
import paho.mqtt.client as mqtt
import sqlite3
import requests
from dataclasses import dataclass, asdict
import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@dataclass
class SensorReading:
    device_id: str
    timestamp: float
    temperature: float
    humidity: float
    motion: bool
    battery: float
    rssi: int

class IoTGateway:
    """Raspberry Pi IoT Gateway for local processing and cloud relay"""
    
    def __init__(self, config_path: str = "config.yaml"):
        self.config = self.load_config(config_path)
        self.local_db = LocalDatabase()
        self.cloud_client = CloudClient(self.config['cloud'])
        self.mqtt_client = self.setup_mqtt()
        self.device_registry = {}
        self.last_cloud_sync = time.time()
        
        # Start background threads
        self.start_background_tasks()
    
    def load_config(self, config_path: str) -> Dict[str, Any]:
        """Load configuration from YAML file"""
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    
    def setup_mqtt(self) -> mqtt.Client:
        """Setup MQTT client for local device communication"""
        client = mqtt.Client()
        client.username_pw_set(
            self.config['mqtt']['username'],
            self.config['mqtt']['password']
        )
        
        # Set callbacks
        client.on_connect = self.on_mqtt_connect
        client.on_message = self.on_mqtt_message
        client.on_disconnect = self.on_mqtt_disconnect
        
        # Connect to MQTT broker
        client.connect(
            self.config['mqtt']['host'],
            self.config['mqtt']['port'],
            60
        )
        
        return client
    
    def on_mqtt_connect(self, client, userdata, flags, rc):
        """Callback for MQTT connection"""
        if rc == 0:
            logger.info("Connected to MQTT broker")
            
            # Subscribe to device topics
            client.subscribe("sensors/+/data")
            client.subscribe("devices/+/status")
            client.subscribe("gateway/commands")
            
        else:
            logger.error(f"Failed to connect to MQTT broker: {rc}")
    
    def on_mqtt_message(self, client, userdata, msg):
        """Handle incoming MQTT messages"""
        try:
            topic_parts = msg.topic.split('/')
            payload = json.loads(msg.payload.decode())
            
            if "sensors" in topic_parts and "data" in topic_parts:
                self.process_sensor_data(payload)
            elif "devices" in topic_parts and "status" in topic_parts:
                self.process_device_status(payload)
            elif "gateway" in topic_parts and "commands" in topic_parts:
                self.process_gateway_command(payload)
                
        except Exception as e:
            logger.error(f"Error processing MQTT message: {e}")
    
    def on_mqtt_disconnect(self, client, userdata, rc):
        """Callback for MQTT disconnection"""
        logger.warning("Disconnected from MQTT broker")
    
    def process_sensor_data(self, data: Dict[str, Any]):
        """Process incoming sensor data"""
        try:
            # Parse sensor reading
            reading = SensorReading(
                device_id=data['deviceId'],
                timestamp=data['timestamp'],
                temperature=data['temperature'],
                humidity=data['humidity'],
                motion=data['motion'],
                battery=data['battery'],
                rssi=data['rssi']
            )
            
            # Store locally
            self.local_db.store_reading(reading)
            
            # Update device registry
            self.update_device_registry(reading.device_id, reading)
            
            # Process data locally
            self.process_local_analytics(reading)
            
            # Queue for cloud sync
            self.queue_for_cloud_sync(reading)
            
            logger.info(f"Processed sensor data from {reading.device_id}")
            
        except Exception as e:
            logger.error(f"Error processing sensor data: {e}")
    
    def process_device_status(self, data: Dict[str, Any]):
        """Process device status updates"""
        device_id = data.get('deviceId')
        status = data.get('status')
        
        if device_id and status:
            self.device_registry[device_id] = {
                'status': status,
                'last_seen': time.time()
            }
            
            logger.info(f"Device {device_id} status: {status}")
    
    def process_gateway_command(self, data: Dict[str, Any]):
        """Process commands sent to the gateway"""
        command = data.get('command')
        
        if command == 'sync_cloud':
            self.sync_to_cloud()
        elif command == 'reboot':
            logger.info("Rebooting gateway...")
            # Implement reboot logic
        elif command == 'get_status':
            self.publish_gateway_status()
    
    def update_device_registry(self, device_id: str, reading: SensorReading):
        """Update device registry with latest reading"""
        if device_id not in self.device_registry:
            self.device_registry[device_id] = {}
        
        self.device_registry[device_id].update({
            'last_reading': asdict(reading),
            'last_seen': time.time(),
            'status': 'online'
        })
    
    def process_local_analytics(self, reading: SensorReading):
        """Process data locally for immediate insights"""
        # Temperature threshold alert
        if reading.temperature > self.config['thresholds']['temperature_max']:
            self.send_alert(
                f"High temperature alert: {reading.temperature}°C from {reading.device_id}"
            )
        
        # Low battery alert
        if reading.battery < self.config['thresholds']['battery_min']:
            self.send_alert(
                f"Low battery alert: {reading.battery}% on {reading.device_id}"
            )
        
        # Motion detection
        if reading.motion and self.config['features']['motion_alerts']:
            self.send_alert(
                f"Motion detected by {reading.device_id}"
            )
    
    def send_alert(self, message: str):
        """Send alert via configured channels"""
        logger.warning(f"ALERT: {message}")
        
        # Publish to MQTT alert topic
        alert_data = {
            'timestamp': time.time(),
            'message': message,
            'severity': 'warning'
        }
        
        self.mqtt_client.publish(
            "gateway/alerts",
            json.dumps(alert_data)
        )
    
    def queue_for_cloud_sync(self, reading: SensorReading):
        """Queue data for cloud synchronization"""
        self.local_db.queue_for_sync(reading)
    
    def sync_to_cloud(self):
        """Synchronize local data to cloud"""
        try:
            # Get queued data
            queued_data = self.local_db.get_queued_data()
            
            if queued_data:
                # Send to cloud
                success = self.cloud_client.send_batch_data(queued_data)
                
                if success:
                    # Mark as synced
                    self.local_db.mark_as_synced([r['id'] for r in queued_data])
                    logger.info(f"Synced {len(queued_data)} records to cloud")
                else:
                    logger.error("Failed to sync data to cloud")
            
            self.last_cloud_sync = time.time()
            
        except Exception as e:
            logger.error(f"Error syncing to cloud: {e}")
    
    def publish_gateway_status(self):
        """Publish gateway status information"""
        status = {
            'gateway_id': self.config['gateway']['id'],
            'timestamp': time.time(),
            'uptime': time.time() - self.config['gateway']['start_time'],
            'devices_count': len(self.device_registry),
            'local_db_records': self.local_db.get_record_count(),
            'last_cloud_sync': self.last_cloud_sync,
            'memory_usage': self.get_memory_usage(),
            'cpu_usage': self.get_cpu_usage()
        }
        
        self.mqtt_client.publish(
            "gateway/status",
            json.dumps(status)
        )
    
    def get_memory_usage(self) -> float:
        """Get memory usage percentage"""
        import psutil
        return psutil.virtual_memory().percent
    
    def get_cpu_usage(self) -> float:
        """Get CPU usage percentage"""
        import psutil
        return psutil.cpu_percent(interval=1)
    
    def start_background_tasks(self):
        """Start background threads for gateway operations"""
        # Cloud sync thread
        sync_thread = threading.Thread(target=self.cloud_sync_loop)
        sync_thread.daemon = True
        sync_thread.start()
        
        # Health check thread
        health_thread = threading.Thread(target=self.health_check_loop)
        health_thread.daemon = True
        health_thread.start()
        
        # MQTT loop thread
        mqtt_thread = threading.Thread(target=self.mqtt_client.loop_forever)
        mqtt_thread.daemon = True
        mqtt_thread.start()
    
    def cloud_sync_loop(self):
        """Background loop for cloud synchronization"""
        while True:
            try:
                # Sync every 60 seconds
                time.sleep(60)
                self.sync_to_cloud()
            except Exception as e:
                logger.error(f"Error in cloud sync loop: {e}")
    
    def health_check_loop(self):
        """Background loop for health checks"""
        while True:
            try:
                # Health check every 30 seconds
                time.sleep(30)
                self.perform_health_check()
            except Exception as e:
                logger.error(f"Error in health check loop: {e}")
    
    def perform_health_check(self):
        """Perform gateway health checks"""
        # Check device connectivity
        current_time = time.time()
        offline_devices = []
        
        for device_id, info in self.device_registry.items():
            last_seen = info.get('last_seen', 0)
            if current_time - last_seen > 300:  # 5 minutes
                offline_devices.append(device_id)
        
        if offline_devices:
            logger.warning(f"Offline devices detected: {offline_devices}")
        
        # Publish status
        self.publish_gateway_status()
    
    def run(self):
        """Main gateway loop"""
        logger.info("IoT Gateway started")
        
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Gateway shutting down...")
            self.mqtt_client.disconnect()

class LocalDatabase:
    """Local SQLite database for edge data storage"""
    
    def __init__(self, db_path: str = "gateway.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Sensor readings table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sensor_readings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                device_id TEXT NOT NULL,
                timestamp REAL NOT NULL,
                temperature REAL,
                humidity REAL,
                motion BOOLEAN,
                battery REAL,
                rssi INTEGER,
                synced BOOLEAN DEFAULT FALSE,
                created_at REAL DEFAULT (julianday('now'))
            )
        ''')
        
        conn.commit()
        conn.close()
    
    def store_reading(self, reading: SensorReading):
        """Store sensor reading in local database"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO sensor_readings 
            (device_id, timestamp, temperature, humidity, motion, battery, rssi)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            reading.device_id,
            reading.timestamp,
            reading.temperature,
            reading.humidity,
            reading.motion,
            reading.battery,
            reading.rssi
        ))
        
        conn.commit()
        conn.close()
    
    def queue_for_sync(self, reading: SensorReading):
        """Mark reading for cloud synchronization"""
        # In this implementation, all readings are automatically queued
        pass
    
    def get_queued_data(self, limit: int = 100) -> List[Dict[str, Any]]:
        """Get data queued for cloud sync"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            SELECT * FROM sensor_readings 
            WHERE synced = FALSE 
            ORDER BY timestamp ASC 
            LIMIT ?
        ''', (limit,))
        
        columns = [desc[0] for desc in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        
        conn.close()
        return results
    
    def mark_as_synced(self, record_ids: List[int]):
        """Mark records as synced to cloud"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        placeholders = ','.join(['?'] * len(record_ids))
        cursor.execute(f'''
            UPDATE sensor_readings 
            SET synced = TRUE 
            WHERE id IN ({placeholders})
        ''', record_ids)
        
        conn.commit()
        conn.close()
    
    def get_record_count(self) -> int:
        """Get total number of records"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT COUNT(*) FROM sensor_readings')
        count = cursor.fetchone()[0]
        
        conn.close()
        return count

class CloudClient:
    """Client for cloud service communication"""
    
    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.base_url = config['api_endpoint']
        self.headers = {
            'Authorization': f"Bearer {config['api_key']}",
            'Content-Type': 'application/json'
        }
    
    def send_batch_data(self, data: List[Dict[str, Any]]) -> bool:
        """Send batch data to cloud"""
        try:
            response = requests.post(
                f"{self.base_url}/sensor-data/batch",
                json={'readings': data},
                headers=self.headers,
                timeout=30
            )
            
            return response.status_code == 200
            
        except Exception as e:
            logger.error(f"Failed to send data to cloud: {e}")
            return False

if __name__ == "__main__":
    gateway = IoTGateway()
    gateway.run()
```
</dartinbot-device>

## Next Steps
<dartinbot-auto-improve>
1. **Security Enhancement**: Device certificate management and OTA updates
2. **Edge AI**: Local machine learning inference capabilities
3. **Mesh Networks**: Device-to-device communication protocols
4. **Advanced Analytics**: Real-time anomaly detection and predictive maintenance
5. **Scale Management**: Device fleet management and bulk operations
6. **Energy Optimization**: Power management and energy harvesting
7. **Industrial Protocols**: Modbus, OPC-UA integration
8. **Digital Twin**: Virtual device modeling and simulation
</dartinbot-auto-improve>

## Troubleshooting Guide
<dartinbot-troubleshooting>
**Common Issues:**
1. **Device connectivity**: Check WiFi credentials and network connectivity
2. **MQTT connection failures**: Verify broker settings and certificates
3. **Sensor reading errors**: Check sensor wiring and power supply
4. **Cloud sync issues**: Verify API endpoints and authentication
5. **Memory issues on devices**: Optimize code and reduce payload sizes

**Debug Commands:**
- `mosquitto_pub -t "test/topic" -m "test message"` - Test MQTT connectivity
- `ping gateway_ip` - Test network connectivity
- `tail -f /var/log/iot-gateway.log` - Monitor gateway logs
- Arduino Serial Monitor for device debugging
- `systemctl status iot-gateway` - Check service status
</dartinbot-troubleshooting>

</dartinbot-template>
