# Path of Jewel - PoE 2 Jewel Pricing Engine

## Overview

**Path of Jewel** is an open-source pricing engine for **Path of Exile 2** jewels.

The goal of this project is to estimate the value of a jewel by analyzing its modifiers, comparing it against similar items listed on the official PoE 2 Trade market, and providing an estimated market price with a confidence score.

Unlike a simple trade search tool, Path of Jewel is being designed as a **smart pricing assistant** capable of:

* Parsing copied item text directly from Path of Exile 2
* Mapping modifiers to official trade stat IDs
* Finding similar jewels listed on the trade market
* Comparing modifier similarity
* Filtering out unrealistic listings
* Estimating a fair market price
* Explaining why the estimate was chosen

---

# Project Goals

* Build a clean, modular pricing engine.
* Integrate with the official Path of Exile 2 Trade API.
* Make the project easy to understand and contribute to.
* Create a useful tool for the PoE community while serving as a professional portfolio project.

---

# Current Features

## Item Parsing

* Parse copied jewel text
* Extract:

  * Base Type
  * Item Level
  * Explicit Modifiers

---

## Stat Mapping

Maps parsed modifiers to internal trade identifiers.

Example:

```
+7% increased Maximum Life
        ↓
maximum life
        ↓
Trade Stat ID
```

---

## Trade Query Builder

Generates trade search queries from parsed jewels.

---

## Similarity Engine

Compares jewels based on shared modifiers.

Current implementation:

* Modifier matching
* Similarity scoring

Future improvements:

* Weighted similarity
* Value scaling
* Modifier importance
* Machine learning ranking

---

## Mock Trade Provider

A development provider that returns mock trade listings.

Used for:

* Testing
* Development
* Pricing algorithm validation

---

## Pricing Engine

Current features:

* Weighted modifier scoring
* Similarity comparison
* Median price calculation
* Average price calculation
* Listing statistics

Future versions will use live trade listings.

---

## FastAPI Backend

Built using FastAPI.

Interactive documentation:

```
http://127.0.0.1:8000/docs
```

---

# Project Structure

```
PathofJewel-PoE-2
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── core
│   │   ├── data
│   │   ├── models
│   │   ├── providers
│   │   ├── services
│   │   └── main.py
│   │
│   └── requirements.txt
│
├── docs
│
├── tests
│
└── README.md
```

---

# Technology Stack

Backend

* Python
* FastAPI
* Pydantic
* Requests

Architecture

* Provider Pattern
* Service Layer
* Dependency Separation

Future

* SQLite/PostgreSQL
* Docker
* GitHub Actions
* React Frontend

---

# Current Architecture

```
                FastAPI
                   │
         ┌─────────┴─────────┐
         │                   │
    Parse Routes      Estimate Routes
         │                   │
         ▼                   ▼
 Item Parser Service   Pricing Service
         │                   │
         ├───────────┬────────┘
         ▼           ▼
   Stat Mapper   Similarity Service
                       │
                       ▼
             Trade Provider Service
                │              │
        Mock Provider   PoE Provider
                │
                ▼
         Price Estimator
```

---

# Development Roadmap

## Phase 1 – Foundation ✅

* FastAPI backend
* Item parser
* Pricing service
* Similarity engine
* Mock trade provider
* Response models

---

## Phase 2 – Trade Integration 🚧

* Trade client
* Official stat IDs
* Trade query builder
* Live search
* Live fetch

---

## Phase 3 – Smart Pricing

* Similarity ranking
* Outlier removal
* Median pricing
* Confidence score
* Recommended listing price

---

## Phase 4 – User Interface

* Web interface
* Paste item text
* Display comparable listings
* Price history
* Saved searches

---

## Phase 5 – Production

* Docker support
* Automated testing
* GitHub Actions CI/CD
* Performance optimization
* Full documentation

---

# Planned Features

* Clipboard import from Path of Exile 2
* Real-time trade price estimation
* Similar jewel recommendations
* Confidence scoring
* Outlier detection
* Price history
* Listing recommendations
* Modifier quality analysis
* Market trend analysis
* Cache for trade searches

---

# Running the Project

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/PathofJewel-PoE-2.git
```

Navigate to the project:

```bash
cd PathofJewel-PoE-2
```

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the server:

```bash
python -m uvicorn app.main:app --reload
```

Open the API documentation:

```
http://127.0.0.1:8000/docs
```

---

# Contributing

Contributions are welcome.

If you would like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Make your changes.
4. Add tests if applicable.
5. Submit a pull request.

---

# License

This project is open source. A license will be added before the first public release.

---

# Current Status

**Version:** 0.1 (Development)

This project is actively under development.

The current implementation focuses on building a robust architecture before connecting to the live Path of Exile 2 Trade market. Future updates will replace mock data with real trade listings and expand the pricing engine with advanced similarity scoring and market analysis.
