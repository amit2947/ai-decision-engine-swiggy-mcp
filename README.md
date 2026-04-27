# AI Decision Engine for Food Ordering (Swiggy MCP Use Case)

## Overview

This project demonstrates an AI-driven decision intelligence system for optimizing food ordering under constraints such as budget, delivery time, and user preferences.

The system is designed to integrate with Swiggy MCP APIs to enable real-world execution of recommendations.

---

## Problem

Users face decision fatigue due to multiple competing factors:
- Price vs rating trade-offs
- Delivery time vs quality
- Cuisine preferences

Current systems focus on search rather than optimized decision-making.

---

## Solution

This system converts user intent into structured constraints and applies a scoring-based decision engine to recommend optimal choices.

---

## Architecture

User Input → Constraint Extraction → Feature Engineering → Scoring Model → Ranked Results

Future integration:
→ Swiggy MCP APIs for real-time data and execution

---

## Key Features

- Constraint-based recommendation (no historical data required)
- Dynamic weighting based on user priorities
- Scalable to ML-based learning and personalization
- Designed for safe and controlled API usage

---

## Tech Stack

- Frontend: Streamlit
- Backend: Python
- Data: Mock dataset (to be replaced with Swiggy MCP APIs)

---

## Future Enhancements

- Integration with Swiggy MCP APIs
- LLM-based intent understanding
- Learning from user interactions
- Collaborative filtering for personalization

---

## Note

This is a prototype using mock data to demonstrate system design. Swiggy MCP APIs will be integrated upon access approval.