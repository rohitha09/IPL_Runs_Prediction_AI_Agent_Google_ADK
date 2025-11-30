# Intelligent IPL Analytics and Predictor System
**Problem Statement**

The Indian Premier League (IPL) generates massive amounts of batting performance data every season. Teams, analysts, and fans struggle to extract accurate, actionable insights due to inconsistent data formats, limited feature engineering, and difficulty comparing players objectively. Traditional analysis is manual, time-consuming, and often biased, preventing data-driven decision-making for player selection, match preparation, and predictive insights.

**Solution**

An AI-powered multi-agent pipeline that:

1. Loads raw IPL batting data automatically.
2. Cleans and preprocesses numerical and categorical fields.
3. Applies scalable feature engineering (imputation, scaling, encoding).
4. Trains multiple Machine Learning models.
5. Evaluates accuracy and selects the best model.
6. Produces structured prediction results via JSON.
7. Works fully automated through a Sequential Agent Architecture.

**Core Concept and Value**

**Automated Multi-Agent Pipeline**
- **Load Data Agent **– loads IPL dataset  
- **Clean Agent** – cleans numeric fields, fixes missing data 
- **Feature Engineering Agent**  – scales, imputes, encodes  the cleaned data
- **Prediction Agent **– trains 3 Machine Learning models and selects the best Model
- **Memory Agent **- cleaned file paths, engineered features, model performance, best model metadata, user queries and context
**Outputs:** best model, accuracy, and analytic summary

**Architecture**
![](https://www.googleapis.com/download/storage/v1/b/kaggle-user-content/o/inbox%2F4157411%2F0c6892cd766d760bf80505cb5dc939cc%2FChatGPT%20Image%20Nov%2030%202025%2004_41_49%20PM.png?generation=1764501176594525&alt=media)

This architecture shows a clean Machine Learning pipeline where raw IPL data flows through a Cleaning Agent, Feature Engineering Agent, and ML Agent, producing the Best Model, while a Memory Agent continuously stores and recalls insights to improve future runs.

**Project Journey**

**1. Starting with Raw IPL Data(Load Data Agent)**

The project begins by collecting raw IPL batting statistics, which are often inconsistent, incomplete, and difficult to use directly for machine-learning tasks.

**2. Cleaning the Data (Cleaning Agent)**

The raw dataset first enters the Cleaning Agent, which standardizes formats, removes invalid characters, fixes missing values, and prepares clean numeric fields—establishing a reliable foundation for ML.

**3. Transforming Data into Features (Feature Engineering Agent)**

The cleaned dataset flows into the Feature Engineering Agent, where numerical scaling, categorical encoding, and imputations are applied. This prepares the dataset with meaningful ML-ready features.

**4. Training & Selecting the Best ML Model (Prediction Agent)**

The engineered dataset is sent to the ML Agent, which trains multiple models, evaluates accuracy, and chooses the best-performing one. This stage produces the output: Best Model and  Accuracy Score.

**5. Continuous Learning & Context Retention (Memory Agent)**

Throughout the entire pipeline, the Memory Agent stores:

cleaned file paths

engineered features

model performance

best model metadata

user queries and context

This memory is reused in future runs, allowing the system to become smarter and more efficient over time.

**6. Final Output Delivery**

The pipeline produces the final prediction output, which can be integrated into dashboards, Streamlit apps, or further analysis notebooks.

**Summary**

The project journey follows a simple yet powerful flow:
Raw Data → Clean → Engineer → Train → Predict → Improve (Memory)

A minimal, modular, and intelligent architecture ensures automation, reusability, and continuous evolution of the IPL analytics system.

**Value Proposition**

1. Fully automated ML pipeline: Zero manual preprocessing
2. Fast predictions for IPL 2026 player analysis
3. Reusable & scalable for any cricket dataset
4. Perfect for dashboards, scouting, fantasy cricket & sports analytics
5. Modern multi-agent architecture ensures modularity and clarity

**Implementation**
**1. Technical Design**

The project follows a modular, multi-agent architecture, ensuring each step of the ML workflow is cleanly separated:

1. Cleaning Agent

Handles parsing errors, missing values, type conversions, outlier handling, and normalization.
This ensures the downstream pipeline receives consistent, high-quality inputs.

2.  Feature Engineering Agent

Implements transformers (imputation, scaling, encoding) using scikit-learn pipelines and ColumnTransformer. This guarantees reproducibility and prevents data leakage.

3. Prediction Agent

Trains multiple models—Logistic Regression, Decision Tree, Random Forest—evaluates them, and auto-selects the best one. Outputs include accuracy comparison and structured JSON results.

4.  Memory Agent

A persistent layer that stores:

intermediate file paths

model accuracy

session states

previous user interactions
This enables context continuity, reproducibility, and long-term learning.

Together, these create a clean, testable, maintainable system.

**2. Code Quality**

The code is designed with strong engineering practices:

1. Clear Modular Functions

Each tool (load_csv, clean_data, feature_engineering, prediction) is isolated, making debugging easy and ensuring maintainability.

2. Reproducibility & Determinism

Random states are fixed (random_state=42) and preprocessing is standardized through pipelines.

3. Error Handling

Graceful exception handling around API keys and environment variables prevents silent failures.

4. State Management

Using Runner, InMemorySessionService, and InMemoryMemoryService, the entire workflow preserves execution context across agents.

5.  File-Based Outputs

Every stage writes structured output (.csv or .json) to /kaggle/working/, making outputs traceable and reusable across notebooks.

**3. AI Integration**

The project integrates Google Gemini ADK Agents to build an autonomous ML pipeline:

1.  SequentialAAgent Orchestration

Agents run in fixed order: Load -> Clean -> Feature Engineering->Predict. Each agent receives state from the previous one—just like a real-world ETL + ML workflow.

2.  LLM Agents for Reasoning

Gemini models interpret instructions, call tools programmatically, and summarize results without manual intervention.

3.  Memory-Enhanced AI

The Memory Agent adds intelligent continuity:

remembers previous runs

stores outputs

retrieves context

enables long-running, evolving analytics systems

This elevates the pipeline from traditional ML to AI-assisted automation.

**RESULTS**

**BEST MODEL AND ACCURACY**

<img width="1912" height="764" alt="bESTM" src="https://github.com/user-attachments/assets/2b1805ef-de93-4699-9daa-83b0720a94f8" />

**MODELS COMPARISON**

![Model_Acc](https://github.com/user-attachments/assets/9901b629-6e16-4d71-87f8-f5daecf28254)





