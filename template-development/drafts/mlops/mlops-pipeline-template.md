# DartinBot Machine Learning MLOps Template

<dartinbot-template 
    name="MLOps Pipeline Template"
    category="mlops"
    version="3.0.0"
    framework-version="3.0.0"
    scope="machine-learning-operations"
    difficulty="advanced"
    confidence-score="0.92"
    auto-improve="true">

## Project Overview
<dartinbot-detect>
Target: End-to-end MLOps pipeline for production machine learning
Tech Stack: Python, MLflow, Kubeflow, Docker, Kubernetes, Apache Airflow
Purpose: Build scalable ML pipelines with automated training, deployment, and monitoring
</dartinbot-detect>

## Tech Stack Configuration
<dartinbot-brain 
    specialty="mlops-engineering"
    model="gpt-4"
    focus="ml-pipelines,model-deployment,monitoring,automation"
    expertise-level="advanced">

### Core Technologies
- **ML Framework**: scikit-learn, TensorFlow, PyTorch
- **Experiment Tracking**: MLflow, Weights & Biases
- **Pipeline Orchestration**: Apache Airflow, Kubeflow Pipelines
- **Model Serving**: MLflow Model Serving, TensorFlow Serving, FastAPI
- **Containerization**: Docker, Kubernetes
- **Monitoring**: Prometheus, Grafana, MLflow

### Data Infrastructure
- **Data Storage**: AWS S3, Google Cloud Storage, MinIO
- **Data Processing**: Apache Spark, Dask, Pandas
- **Feature Store**: Feast, Tecton
- **Data Validation**: Great Expectations, TensorFlow Data Validation
- **Version Control**: DVC (Data Version Control)

### Deployment Infrastructure
- **Container Registry**: Docker Hub, AWS ECR, Google GCR
- **Orchestration**: Kubernetes, Docker Swarm
- **CI/CD**: GitHub Actions, GitLab CI, Jenkins
- **Infrastructure as Code**: Terraform, Helm Charts
- **Cloud Platforms**: AWS, GCP, Azure

## Project Structure

### MLOps Project Structure
```
ml-project/
├── data/
│   ├── raw/
│   ├── processed/
│   ├── features/
│   └── external/
├── notebooks/
│   ├── exploratory/
│   ├── experiments/
│   └── reports/
├── src/
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── data_processor.py
│   │   └── feature_engineering.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── train.py
│   │   ├── predict.py
│   │   ├── evaluate.py
│   │   └── model_registry.py
│   ├── pipelines/
│   │   ├── __init__.py
│   │   ├── training_pipeline.py
│   │   ├── inference_pipeline.py
│   │   └── data_pipeline.py
│   ├── monitoring/
│   │   ├── __init__.py
│   │   ├── model_monitor.py
│   │   ├── data_drift.py
│   │   └── performance_tracker.py
│   └── api/
│       ├── __init__.py
│       ├── main.py
│       ├── models.py
│       └── endpoints.py
├── tests/
│   ├── unit/
│   ├── integration/
│   └── performance/
├── configs/
│   ├── model_config.yaml
│   ├── pipeline_config.yaml
│   └── deployment_config.yaml
├── docker/
│   ├── Dockerfile.train
│   ├── Dockerfile.serve
│   └── docker-compose.yml
├── k8s/
│   ├── training-job.yaml
│   ├── serving-deployment.yaml
│   └── monitoring-stack.yaml
├── airflow/
│   └── dags/
│       ├── data_pipeline_dag.py
│       ├── training_pipeline_dag.py
│       └── deployment_pipeline_dag.py
├── mlflow/
│   ├── MLproject
│   └── conda.yaml
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── requirements.txt
├── setup.py
├── dvc.yaml
└── .dvcignore
```

## Configuration Files

### MLflow Project Configuration
<dartinbot-config type="MLproject">
```yaml
name: ml-pipeline

conda_env: conda.yaml

entry_points:
  data_preparation:
    parameters:
      input_path: {type: str, default: "data/raw"}
      output_path: {type: str, default: "data/processed"}
    command: "python src/data/data_processor.py --input-path {input_path} --output-path {output_path}"

  feature_engineering:
    parameters:
      input_path: {type: str, default: "data/processed"}
      output_path: {type: str, default: "data/features"}
    command: "python src/data/feature_engineering.py --input-path {input_path} --output-path {output_path}"

  train:
    parameters:
      data_path: {type: str, default: "data/features"}
      model_type: {type: str, default: "random_forest"}
      max_depth: {type: int, default: 10}
      n_estimators: {type: int, default: 100}
    command: "python src/models/train.py --data-path {data_path} --model-type {model_type} --max-depth {max_depth} --n-estimators {n_estimators}"

  evaluate:
    parameters:
      model_uri: {type: str}
      data_path: {type: str, default: "data/features"}
    command: "python src/models/evaluate.py --model-uri {model_uri} --data-path {data_path}"
```
</dartinbot-config>

### DVC Pipeline Configuration
<dartinbot-config type="dvc.yaml">
```yaml
stages:
  data_preparation:
    cmd: python src/data/data_processor.py --input-path data/raw --output-path data/processed
    deps:
    - src/data/data_processor.py
    - data/raw
    outs:
    - data/processed

  feature_engineering:
    cmd: python src/data/feature_engineering.py --input-path data/processed --output-path data/features
    deps:
    - src/data/feature_engineering.py
    - data/processed
    outs:
    - data/features

  train_model:
    cmd: python src/models/train.py --data-path data/features --model-output models/
    deps:
    - src/models/train.py
    - data/features
    params:
    - model_config.yaml:train
    outs:
    - models/model.pkl
    metrics:
    - metrics/train_metrics.json

  evaluate_model:
    cmd: python src/models/evaluate.py --model-path models/model.pkl --data-path data/features --metrics-output metrics/
    deps:
    - src/models/evaluate.py
    - models/model.pkl
    - data/features
    metrics:
    - metrics/eval_metrics.json
```
</dartinbot-config>

### Model Configuration
<dartinbot-config type="model_config.yaml">
```yaml
train:
  model_type: "random_forest"
  parameters:
    n_estimators: 100
    max_depth: 10
    min_samples_split: 2
    min_samples_leaf: 1
    random_state: 42
  
  validation:
    test_size: 0.2
    cv_folds: 5
    stratify: true

  preprocessing:
    scaling: "standard"
    encoding: "one_hot"
    missing_strategy: "median"

  feature_selection:
    method: "rfe"
    n_features: 50

inference:
  batch_size: 1000
  timeout: 30
  retry_attempts: 3

monitoring:
  drift_threshold: 0.1
  performance_threshold: 0.8
  alert_email: "ml-team@company.com"

deployment:
  environment: "production"
  replicas: 3
  cpu_request: "500m"
  memory_request: "1Gi"
  cpu_limit: "2"
  memory_limit: "4Gi"
```
</dartinbot-config>

## Core Components

### Model Training Pipeline
<dartinbot-component type="training-pipeline">
```python
import os
import yaml
import joblib
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
import pandas as pd
import numpy as np
from typing import Dict, Any, Tuple

class ModelTrainer:
    """Handles model training with experiment tracking"""
    
    def __init__(self, config_path: str = "configs/model_config.yaml"):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
        self.model = None
        self.scaler = StandardScaler()
        self.label_encoder = LabelEncoder()
        
        # Initialize MLflow
        mlflow.set_tracking_uri("http://localhost:5000")
        mlflow.set_experiment("ml-pipeline-experiment")
    
    def load_data(self, data_path: str) -> Tuple[pd.DataFrame, pd.Series]:
        """Load and prepare training data"""
        data = pd.read_csv(data_path)
        
        # Separate features and target
        target_column = self.config['train']['target_column']
        X = data.drop(columns=[target_column])
        y = data[target_column]
        
        return X, y
    
    def preprocess_data(self, X: pd.DataFrame, y: pd.Series) -> Tuple[np.ndarray, np.ndarray]:
        """Preprocess features and target"""
        # Handle missing values
        missing_strategy = self.config['train']['preprocessing']['missing_strategy']
        if missing_strategy == "median":
            X = X.fillna(X.median())
        elif missing_strategy == "mean":
            X = X.fillna(X.mean())
        
        # Scale features
        scaling = self.config['train']['preprocessing']['scaling']
        if scaling == "standard":
            X_scaled = self.scaler.fit_transform(X)
        else:
            X_scaled = X.values
        
        # Encode target if necessary
        if y.dtype == 'object':
            y_encoded = self.label_encoder.fit_transform(y)
        else:
            y_encoded = y.values
        
        return X_scaled, y_encoded
    
    def train_model(self, X: np.ndarray, y: np.ndarray) -> None:
        """Train the model with experiment tracking"""
        
        with mlflow.start_run():
            # Log parameters
            model_params = self.config['train']['parameters']
            mlflow.log_params(model_params)
            
            # Initialize model
            if self.config['train']['model_type'] == "random_forest":
                self.model = RandomForestClassifier(**model_params)
            
            # Split data
            test_size = self.config['train']['validation']['test_size']
            X_train, X_test, y_train, y_test = train_test_split(
                X, y, test_size=test_size, random_state=42, stratify=y
            )
            
            # Train model
            self.model.fit(X_train, y_train)
            
            # Evaluate model
            y_pred = self.model.predict(X_test)
            
            # Calculate metrics
            metrics = {
                'accuracy': accuracy_score(y_test, y_pred),
                'precision': precision_score(y_test, y_pred, average='weighted'),
                'recall': recall_score(y_test, y_pred, average='weighted'),
                'f1_score': f1_score(y_test, y_pred, average='weighted')
            }
            
            # Cross-validation
            cv_folds = self.config['train']['validation']['cv_folds']
            cv_scores = cross_val_score(self.model, X_train, y_train, cv=cv_folds)
            metrics['cv_mean'] = cv_scores.mean()
            metrics['cv_std'] = cv_scores.std()
            
            # Log metrics
            mlflow.log_metrics(metrics)
            
            # Log model
            mlflow.sklearn.log_model(
                self.model, 
                "model",
                registered_model_name="ml-pipeline-model"
            )
            
            # Save preprocessing artifacts
            mlflow.log_artifact("preprocessor.pkl")
            joblib.dump(self.scaler, "preprocessor.pkl")
            
            print(f"Model trained successfully. Metrics: {metrics}")
    
    def save_model(self, output_path: str) -> None:
        """Save trained model and preprocessors"""
        os.makedirs(output_path, exist_ok=True)
        
        # Save model
        joblib.dump(self.model, os.path.join(output_path, "model.pkl"))
        
        # Save preprocessors
        joblib.dump(self.scaler, os.path.join(output_path, "scaler.pkl"))
        joblib.dump(self.label_encoder, os.path.join(output_path, "label_encoder.pkl"))
        
        print(f"Model saved to {output_path}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-path", required=True)
    parser.add_argument("--model-output", default="models/")
    args = parser.parse_args()
    
    trainer = ModelTrainer()
    X, y = trainer.load_data(args.data_path)
    X_processed, y_processed = trainer.preprocess_data(X, y)
    trainer.train_model(X_processed, y_processed)
    trainer.save_model(args.model_output)
```
</dartinbot-component>

### Model Serving API
<dartinbot-component type="serving-api">
```python
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd
import logging
from typing import List, Dict, Any
import mlflow
import mlflow.sklearn
from prometheus_client import Counter, Histogram, generate_latest
import time
import uuid

# Metrics
PREDICTION_COUNTER = Counter('ml_predictions_total', 'Total predictions made')
PREDICTION_LATENCY = Histogram('ml_prediction_duration_seconds', 'Prediction latency')
ERROR_COUNTER = Counter('ml_prediction_errors_total', 'Total prediction errors')

app = FastAPI(title="ML Model Serving API", version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class PredictionRequest(BaseModel):
    features: List[float]
    request_id: str = None

class PredictionResponse(BaseModel):
    prediction: float
    probability: List[float] = None
    request_id: str
    model_version: str
    processing_time: float

class ModelService:
    """Model serving service with monitoring"""
    
    def __init__(self):
        self.model = None
        self.scaler = None
        self.label_encoder = None
        self.model_version = None
        self.load_model()
    
    def load_model(self) -> None:
        """Load the latest model from MLflow"""
        try:
            # Load latest model version
            client = mlflow.MlflowClient()
            model_name = "ml-pipeline-model"
            
            latest_version = client.get_latest_versions(
                model_name, 
                stages=["Production"]
            )[0]
            
            self.model_version = latest_version.version
            model_uri = f"models:/{model_name}/{self.model_version}"
            
            # Load model
            self.model = mlflow.sklearn.load_model(model_uri)
            
            # Load preprocessors
            self.scaler = joblib.load("models/scaler.pkl")
            self.label_encoder = joblib.load("models/label_encoder.pkl")
            
            logger.info(f"Model loaded successfully. Version: {self.model_version}")
            
        except Exception as e:
            logger.error(f"Failed to load model: {e}")
            raise
    
    def preprocess_features(self, features: List[float]) -> np.ndarray:
        """Preprocess input features"""
        features_array = np.array(features).reshape(1, -1)
        
        # Scale features
        if self.scaler:
            features_scaled = self.scaler.transform(features_array)
        else:
            features_scaled = features_array
        
        return features_scaled
    
    def predict(self, features: List[float]) -> Dict[str, Any]:
        """Make prediction with monitoring"""
        start_time = time.time()
        
        try:
            # Preprocess features
            features_processed = self.preprocess_features(features)
            
            # Make prediction
            prediction = self.model.predict(features_processed)[0]
            
            # Get prediction probabilities if available
            probabilities = None
            if hasattr(self.model, 'predict_proba'):
                probabilities = self.model.predict_proba(features_processed)[0].tolist()
            
            # Decode prediction if necessary
            if self.label_encoder:
                prediction = self.label_encoder.inverse_transform([prediction])[0]
            
            processing_time = time.time() - start_time
            
            # Update metrics
            PREDICTION_COUNTER.inc()
            PREDICTION_LATENCY.observe(processing_time)
            
            return {
                "prediction": prediction,
                "probability": probabilities,
                "processing_time": processing_time
            }
            
        except Exception as e:
            ERROR_COUNTER.inc()
            logger.error(f"Prediction error: {e}")
            raise

# Global model service instance
model_service = ModelService()

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "model_version": model_service.model_version,
        "timestamp": time.time()
    }

@app.post("/predict", response_model=PredictionResponse)
async def predict(request: PredictionRequest, background_tasks: BackgroundTasks):
    """Main prediction endpoint"""
    
    request_id = request.request_id or str(uuid.uuid4())
    
    try:
        result = model_service.predict(request.features)
        
        # Log prediction for monitoring
        background_tasks.add_task(
            log_prediction, 
            request_id, 
            request.features, 
            result["prediction"]
        )
        
        return PredictionResponse(
            prediction=result["prediction"],
            probability=result["probability"],
            request_id=request_id,
            model_version=model_service.model_version,
            processing_time=result["processing_time"]
        )
        
    except Exception as e:
        logger.error(f"Prediction failed for request {request_id}: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/batch_predict")
async def batch_predict(requests: List[PredictionRequest]):
    """Batch prediction endpoint"""
    
    results = []
    
    for request in requests:
        try:
            result = model_service.predict(request.features)
            results.append({
                "request_id": request.request_id or str(uuid.uuid4()),
                "prediction": result["prediction"],
                "probability": result["probability"],
                "processing_time": result["processing_time"]
            })
        except Exception as e:
            results.append({
                "request_id": request.request_id or str(uuid.uuid4()),
                "error": str(e)
            })
    
    return {"predictions": results}

@app.get("/metrics")
async def get_metrics():
    """Prometheus metrics endpoint"""
    return generate_latest()

@app.post("/reload_model")
async def reload_model():
    """Reload model endpoint"""
    try:
        model_service.load_model()
        return {"status": "success", "model_version": model_service.model_version}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def log_prediction(request_id: str, features: List[float], prediction: float):
    """Log prediction for monitoring and drift detection"""
    log_data = {
        "request_id": request_id,
        "timestamp": time.time(),
        "features": features,
        "prediction": prediction,
        "model_version": model_service.model_version
    }
    
    # Log to monitoring system
    logger.info(f"Prediction logged: {log_data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
```
</dartinbot-component>

## Airflow DAGs

### Training Pipeline DAG
<dartinbot-pipeline type="airflow-dag">
```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from airflow.operators.email_operator import EmailOperator
from airflow.sensors.s3_sensor import S3KeySensor
import pandas as pd
import os

# Default arguments
default_args = {
    'owner': 'ml-team',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'email': ['ml-team@company.com']
}

# DAG definition
dag = DAG(
    'ml_training_pipeline',
    default_args=default_args,
    description='ML model training pipeline',
    schedule_interval='@daily',
    catchup=False,
    max_active_runs=1
)

def check_data_quality(**context):
    """Validate data quality before training"""
    import great_expectations as ge
    
    # Load data
    data_path = context['params']['data_path']
    df = pd.read_csv(data_path)
    
    # Create expectation suite
    expectations = ge.from_pandas(df)
    
    # Add expectations
    expectations.expect_table_row_count_to_be_between(min_value=1000, max_value=None)
    expectations.expect_column_values_to_not_be_null('target')
    expectations.expect_column_values_to_be_between('feature_1', min_value=0, max_value=100)
    
    # Validate
    results = expectations.validate()
    
    if not results['success']:
        raise ValueError(f"Data quality check failed: {results}")
    
    print("Data quality check passed")

def trigger_model_deployment(**context):
    """Trigger model deployment after successful training"""
    # Check if model meets performance criteria
    model_metrics_path = context['params']['metrics_path']
    
    if os.path.exists(model_metrics_path):
        with open(model_metrics_path, 'r') as f:
            import json
            metrics = json.load(f)
        
        # Check if model performance is acceptable
        if metrics.get('accuracy', 0) > 0.8:
            print("Model performance acceptable, triggering deployment")
            # Trigger deployment pipeline
            return True
        else:
            print("Model performance below threshold, skipping deployment")
            return False
    
    return False

# Data quality check
data_quality_task = PythonOperator(
    task_id='data_quality_check',
    python_callable=check_data_quality,
    params={
        'data_path': '/data/training_data.csv'
    },
    dag=dag
)

# Data preprocessing
data_preprocessing_task = BashOperator(
    task_id='data_preprocessing',
    bash_command='cd /ml-project && python src/data/data_processor.py --input-path /data/raw --output-path /data/processed',
    dag=dag
)

# Feature engineering
feature_engineering_task = BashOperator(
    task_id='feature_engineering',
    bash_command='cd /ml-project && python src/data/feature_engineering.py --input-path /data/processed --output-path /data/features',
    dag=dag
)

# Model training
model_training_task = BashOperator(
    task_id='model_training',
    bash_command='cd /ml-project && python src/models/train.py --data-path /data/features --model-output /models/',
    dag=dag
)

# Model evaluation
model_evaluation_task = BashOperator(
    task_id='model_evaluation',
    bash_command='cd /ml-project && python src/models/evaluate.py --model-path /models/model.pkl --data-path /data/features --metrics-output /metrics/',
    dag=dag
)

# Deployment trigger
deployment_trigger_task = PythonOperator(
    task_id='deployment_trigger',
    python_callable=trigger_model_deployment,
    params={
        'metrics_path': '/metrics/eval_metrics.json'
    },
    dag=dag
)

# Success notification
success_notification = EmailOperator(
    task_id='success_notification',
    to=['ml-team@company.com'],
    subject='ML Training Pipeline Completed Successfully',
    html_content="""
    <h3>ML Training Pipeline Completed</h3>
    <p>The model training pipeline has completed successfully.</p>
    <p>Check MLflow for experiment details and model artifacts.</p>
    """,
    dag=dag
)

# Define task dependencies
data_quality_task >> data_preprocessing_task >> feature_engineering_task
feature_engineering_task >> model_training_task >> model_evaluation_task
model_evaluation_task >> deployment_trigger_task >> success_notification
```
</dartinbot-pipeline>

## Monitoring and Observability

### Model Performance Monitor
<dartinbot-monitoring type="model-monitor">
```python
import pandas as pd
import numpy as np
from scipy import stats
from sklearn.metrics import accuracy_score, precision_score, recall_score
import mlflow
import logging
from typing import Dict, Any, List
from datetime import datetime, timedelta
import warnings
import json

class ModelMonitor:
    """Monitor model performance and data drift"""
    
    def __init__(self, model_name: str, reference_data_path: str):
        self.model_name = model_name
        self.reference_data = pd.read_csv(reference_data_path)
        self.logger = logging.getLogger(__name__)
        
        # Thresholds
        self.drift_threshold = 0.05
        self.performance_threshold = 0.1
        
    def detect_data_drift(self, current_data: pd.DataFrame) -> Dict[str, Any]:
        """Detect data drift using statistical tests"""
        
        drift_results = {
            'drift_detected': False,
            'features_with_drift': [],
            'drift_scores': {},
            'timestamp': datetime.now().isoformat()
        }
        
        for column in current_data.columns:
            if column in self.reference_data.columns:
                # Kolmogorov-Smirnov test for continuous variables
                if pd.api.types.is_numeric_dtype(current_data[column]):
                    ks_statistic, p_value = stats.ks_2samp(
                        self.reference_data[column].dropna(),
                        current_data[column].dropna()
                    )
                    
                    drift_results['drift_scores'][column] = {
                        'ks_statistic': ks_statistic,
                        'p_value': p_value,
                        'drift_detected': p_value < self.drift_threshold
                    }
                    
                    if p_value < self.drift_threshold:
                        drift_results['features_with_drift'].append(column)
                        drift_results['drift_detected'] = True
                
                # Chi-square test for categorical variables
                elif pd.api.types.is_categorical_dtype(current_data[column]) or current_data[column].dtype == 'object':
                    ref_counts = self.reference_data[column].value_counts()
                    curr_counts = current_data[column].value_counts()
                    
                    # Align categories
                    all_categories = set(ref_counts.index) | set(curr_counts.index)
                    ref_aligned = [ref_counts.get(cat, 0) for cat in all_categories]
                    curr_aligned = [curr_counts.get(cat, 0) for cat in all_categories]
                    
                    if sum(curr_aligned) > 0:  # Avoid division by zero
                        chi2_statistic, p_value = stats.chisquare(curr_aligned, ref_aligned)
                        
                        drift_results['drift_scores'][column] = {
                            'chi2_statistic': chi2_statistic,
                            'p_value': p_value,
                            'drift_detected': p_value < self.drift_threshold
                        }
                        
                        if p_value < self.drift_threshold:
                            drift_results['features_with_drift'].append(column)
                            drift_results['drift_detected'] = True
        
        return drift_results
    
    def monitor_model_performance(self, predictions: List[float], 
                                 actuals: List[float]) -> Dict[str, Any]:
        """Monitor model performance metrics"""
        
        # Calculate current performance metrics
        current_accuracy = accuracy_score(actuals, predictions)
        current_precision = precision_score(actuals, predictions, average='weighted')
        current_recall = recall_score(actuals, predictions, average='weighted')
        
        # Get baseline performance from MLflow
        baseline_metrics = self._get_baseline_metrics()
        
        # Calculate performance degradation
        performance_results = {
            'current_metrics': {
                'accuracy': current_accuracy,
                'precision': current_precision,
                'recall': current_recall
            },
            'baseline_metrics': baseline_metrics,
            'performance_degradation': {},
            'alerts': [],
            'timestamp': datetime.now().isoformat()
        }
        
        # Check for performance degradation
        for metric in ['accuracy', 'precision', 'recall']:
            if metric in baseline_metrics:
                degradation = baseline_metrics[metric] - performance_results['current_metrics'][metric]
                performance_results['performance_degradation'][metric] = degradation
                
                if degradation > self.performance_threshold:
                    alert = f"{metric.capitalize()} degraded by {degradation:.3f} (threshold: {self.performance_threshold})"
                    performance_results['alerts'].append(alert)
                    self.logger.warning(alert)
        
        return performance_results
    
    def _get_baseline_metrics(self) -> Dict[str, float]:
        """Get baseline metrics from MLflow"""
        try:
            client = mlflow.MlflowClient()
            
            # Get latest production model
            latest_version = client.get_latest_versions(
                self.model_name, 
                stages=["Production"]
            )[0]
            
            # Get metrics from the model version
            model_version = client.get_model_version(self.model_name, latest_version.version)
            run_id = model_version.run_id
            
            metrics = client.get_metric_history(run_id, "accuracy")
            if metrics:
                return {
                    'accuracy': metrics[-1].value,
                    'precision': 0.85,  # Would get from MLflow in practice
                    'recall': 0.83      # Would get from MLflow in practice
                }
        
        except Exception as e:
            self.logger.error(f"Failed to get baseline metrics: {e}")
        
        return {}
    
    def generate_monitoring_report(self, drift_results: Dict[str, Any], 
                                 performance_results: Dict[str, Any]) -> Dict[str, Any]:
        """Generate comprehensive monitoring report"""
        
        report = {
            'timestamp': datetime.now().isoformat(),
            'model_name': self.model_name,
            'data_drift': drift_results,
            'performance_monitoring': performance_results,
            'overall_status': 'healthy',
            'recommendations': []
        }
        
        # Determine overall status
        if drift_results['drift_detected']:
            report['overall_status'] = 'drift_detected'
            report['recommendations'].append('Investigate data drift and consider model retraining')
        
        if performance_results['alerts']:
            report['overall_status'] = 'performance_degraded'
            report['recommendations'].append('Performance degradation detected - consider model update')
        
        if drift_results['drift_detected'] and performance_results['alerts']:
            report['overall_status'] = 'critical'
            report['recommendations'].append('Critical: Both drift and performance issues detected')
        
        return report
    
    def log_monitoring_results(self, report: Dict[str, Any]) -> None:
        """Log monitoring results to MLflow"""
        
        with mlflow.start_run(run_name=f"monitoring_{datetime.now().strftime('%Y%m%d_%H%M%S')}"):
            # Log drift metrics
            if report['data_drift']['drift_detected']:
                mlflow.log_metric("drift_detected", 1)
                mlflow.log_metric("features_with_drift_count", len(report['data_drift']['features_with_drift']))
            else:
                mlflow.log_metric("drift_detected", 0)
            
            # Log performance metrics
            for metric, value in report['performance_monitoring']['current_metrics'].items():
                mlflow.log_metric(f"current_{metric}", value)
            
            # Log degradation metrics
            for metric, degradation in report['performance_monitoring']['performance_degradation'].items():
                mlflow.log_metric(f"{metric}_degradation", degradation)
            
            # Log report as artifact
            with open("monitoring_report.json", "w") as f:
                json.dump(report, f, indent=2)
            mlflow.log_artifact("monitoring_report.json")

# Usage example
if __name__ == "__main__":
    monitor = ModelMonitor("ml-pipeline-model", "data/reference_data.csv")
    
    # Simulate current data
    current_data = pd.read_csv("data/current_data.csv")
    
    # Simulate predictions and actuals
    predictions = [1, 0, 1, 1, 0]
    actuals = [1, 0, 0, 1, 0]
    
    # Run monitoring
    drift_results = monitor.detect_data_drift(current_data)
    performance_results = monitor.monitor_model_performance(predictions, actuals)
    
    # Generate and log report
    report = monitor.generate_monitoring_report(drift_results, performance_results)
    monitor.log_monitoring_results(report)
    
    print(f"Monitoring complete. Status: {report['overall_status']}")
```
</dartinbot-monitoring>

## Container Configuration

### Training Dockerfile
<dartinbot-container type="dockerfile-train">
```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY src/ ./src/
COPY configs/ ./configs/
COPY setup.py .

# Install package
RUN pip install -e .

# Set environment variables
ENV PYTHONPATH=/app
ENV MLFLOW_TRACKING_URI=http://mlflow:5000

# Create directories for data and models
RUN mkdir -p /data /models /metrics

# Default command
CMD ["python", "src/models/train.py", "--data-path", "/data", "--model-output", "/models"]
```
</dartinbot-container>

### Serving Dockerfile
<dartinbot-container type="dockerfile-serve">
```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements for serving
COPY requirements-serve.txt .
RUN pip install --no-cache-dir -r requirements-serve.txt

# Copy source code
COPY src/api/ ./src/api/
COPY models/ ./models/

# Set environment variables
ENV PYTHONPATH=/app
ENV MLFLOW_TRACKING_URI=http://mlflow:5000

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health || exit 1

# Run the API
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```
</dartinbot-container>

## Kubernetes Deployment

### Model Serving Deployment
<dartinbot-k8s type="serving-deployment">
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ml-model-serving
  labels:
    app: ml-model-serving
spec:
  replicas: 3
  selector:
    matchLabels:
      app: ml-model-serving
  template:
    metadata:
      labels:
        app: ml-model-serving
    spec:
      containers:
      - name: ml-api
        image: ml-model-serving:latest
        ports:
        - containerPort: 8000
        env:
        - name: MLFLOW_TRACKING_URI
          value: "http://mlflow:5000"
        resources:
          requests:
            memory: "1Gi"
            cpu: "500m"
          limits:
            memory: "4Gi"
            cpu: "2"
        livenessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 30
          periodSeconds: 10
        readinessProbe:
          httpGet:
            path: /health
            port: 8000
          initialDelaySeconds: 5
          periodSeconds: 5

---
apiVersion: v1
kind: Service
metadata:
  name: ml-model-serving-service
spec:
  selector:
    app: ml-model-serving
  ports:
  - port: 80
    targetPort: 8000
  type: LoadBalancer

---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: ml-model-serving-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: ml-model-serving
  minReplicas: 3
  maxReplicas: 10
  metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 70
  - type: Resource
    resource:
      name: memory
      target:
        type: Utilization
        averageUtilization: 80
```
</dartinbot-k8s>

## CI/CD Pipeline

### GitHub Actions MLOps Workflow
<dartinbot-cicd type="github-actions">
```yaml
name: MLOps Pipeline

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

env:
  MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_TRACKING_URI }}
  AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
  AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov
    
    - name: Run tests
      run: |
        pytest tests/ --cov=src/ --cov-report=xml
    
    - name: Upload coverage to Codecov
      uses: codecov/codecov-action@v3

  data-validation:
    runs-on: ubuntu-latest
    needs: test
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install great_expectations pandas
    
    - name: Run data validation
      run: |
        python src/data/validate_data.py

  train-model:
    runs-on: ubuntu-latest
    needs: [test, data-validation]
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Train model
      run: |
        python src/models/train.py \
          --data-path data/features \
          --model-output models/
    
    - name: Evaluate model
      run: |
        python src/models/evaluate.py \
          --model-path models/model.pkl \
          --data-path data/features \
          --metrics-output metrics/

  build-and-push:
    runs-on: ubuntu-latest
    needs: train-model
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure AWS credentials
      uses: aws-actions/configure-aws-credentials@v2
      with:
        aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
        aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
        aws-region: us-west-2
    
    - name: Login to Amazon ECR
      id: login-ecr
      uses: aws-actions/amazon-ecr-login@v1
    
    - name: Build and push Docker image
      env:
        ECR_REGISTRY: ${{ steps.login-ecr.outputs.registry }}
        ECR_REPOSITORY: ml-model-serving
        IMAGE_TAG: ${{ github.sha }}
      run: |
        docker build -f docker/Dockerfile.serve -t $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG .
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG
        docker tag $ECR_REGISTRY/$ECR_REPOSITORY:$IMAGE_TAG $ECR_REGISTRY/$ECR_REPOSITORY:latest
        docker push $ECR_REGISTRY/$ECR_REPOSITORY:latest

  deploy:
    runs-on: ubuntu-latest
    needs: build-and-push
    if: github.ref == 'refs/heads/main'
    steps:
    - uses: actions/checkout@v3
    
    - name: Configure kubectl
      uses: azure/setup-kubectl@v1
    
    - name: Deploy to Kubernetes
      run: |
        kubectl apply -f k8s/serving-deployment.yaml
        kubectl rollout status deployment/ml-model-serving
    
    - name: Run smoke tests
      run: |
        python tests/smoke_tests.py

  monitoring:
    runs-on: ubuntu-latest
    needs: deploy
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run model monitoring
      run: |
        python src/monitoring/model_monitor.py
```
</dartinbot-cicd>

## Next Steps
<dartinbot-auto-improve>
1. **Advanced Monitoring**: Model explainability and fairness monitoring
2. **AutoML**: Automated hyperparameter tuning and architecture search
3. **Edge Deployment**: Model optimization for edge devices
4. **Multi-Model Serving**: A/B testing and shadow deployments
5. **Real-time Streaming**: Kafka integration for real-time predictions
6. **Model Governance**: Compliance and audit trails
7. **Advanced Security**: Model security and adversarial attack detection
8. **Cost Optimization**: Resource usage optimization and cost monitoring
</dartinbot-auto-improve>

## Troubleshooting Guide
<dartinbot-troubleshooting>
**Common Issues:**
1. **MLflow tracking failures**: Check MLflow server connectivity and credentials
2. **Docker build failures**: Verify Dockerfile syntax and base image availability
3. **Kubernetes deployment issues**: Check resource limits and image pull policies
4. **Model performance degradation**: Review data drift monitoring and feature changes
5. **Pipeline failures**: Check Airflow logs and task dependencies

**Debug Commands:**
- `mlflow ui` - Start MLflow tracking UI
- `kubectl logs deployment/ml-model-serving` - Check Kubernetes logs
- `docker logs <container_id>` - Check container logs
- `airflow test dag_id task_id execution_date` - Test Airflow tasks
- `python -m pytest tests/ -v` - Run tests with verbose output
</dartinbot-troubleshooting>

</dartinbot-template>
