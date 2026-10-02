# Personalized Meal & Diet Subscription Manager

A clinical dietary subscription service that generates weekly menus based on patient metabolic constraints such as allergies, diabetic limits, and calorie goals, and tracks daily delivery fulfillment.

## 1. Project Overview

The Personalized Meal & Diet Subscription Manager allows subscribers to manage their dietary profiles and subscriptions while generating personalized weekly meal plans based on dietary constraints.

Generated meal plans are reviewed and approved by a dietitian before being made available to the subscriber. The system also supports subscription schedule management and daily meal delivery fulfillment tracking.

## 2. Target Stakeholders / Actors

### Subscriber

The subscriber can:

- Manage their dietary profile
- Generate and view weekly meal plans
- Pause, skip, or reschedule their subscription
- Check daily meal delivery fulfillment status

### Dietitian

The dietitian can:

- Review generated meal plans
- Approve generated meal plans
- Intervene when a compliant meal plan cannot be generated

## 3. Functional Requirements

The project contains exactly five functional requirements:

| ID | Requirement |
|---|---|
| **FR-001** | Generate weekly meal plans according to macro-nutrient constraints and allergen exclusions. |
| **FR-002** | Allow the subscriber to manage their dietary profile. |
| **FR-003** | Allow the dietitian to review and approve generated meal plans. |
| **FR-004** | Allow the subscriber to pause, skip, or reschedule the subscription. |
| **FR-005** | Record and display daily meal delivery fulfillment status. |

## 4. Non-Functional Requirements

The project contains exactly two non-functional requirements:

| ID | Requirement |
|---|---|
| **NFR-001** | Support subscription schedule modifications up to 12 hours before dispatch. |
| **NFR-002** | Protect subscriber dietary information using authenticated access and role-based authorization. |

## 5. Primary Use Cases

The UML model contains five primary use cases:

- **UC-01:** Manage Dietary Profile
- **UC-02:** Generate Weekly Meal Plan
- **UC-03:** Review & Approve Meal Plan
- **UC-04:** Manage Subscription
- **UC-05:** Track Delivery Fulfillment

The UML diagram also shows the required `«include»` and `«extend»` relationships.

## 6. Use-Case Flow

### UC-01 – Manage Dietary Profile

**Primary Actor:** Subscriber

The subscriber manages the dietary information used by the system for personalized meal planning.

The dietary profile includes relevant information such as:

- Allergies
- Dietary restrictions
- Calorie goals
- Diabetic limits
- Macro-nutrient requirements

The saved profile is used during weekly meal-plan generation.

### UC-02 – Generate Weekly Meal Plan

**Primary Actor:** Subscriber  
**Supporting Actor:** Dietitian

#### Preconditions

- Subscriber is authenticated.
- Subscriber has a saved dietary profile.
- The subscription is active for the requested week.

#### Postconditions

- A weekly meal plan is generated according to the subscriber's constraints.
- The plan is saved for dietitian review.
- No excluded allergen is included in the generated menu.

#### Main Success Scenario

1. Subscriber selects **Generate Weekly Meal Plan**.
2. System retrieves the dietary profile and subscription details.
3. System validates dietary constraints and allergen exclusions.
4. System generates a weekly menu within the configured calorie and macro-nutrient limits.
5. System checks the menu for excluded allergens and constraint violations.
6. System saves the meal plan as **Pending Dietitian Review**.
7. System notifies the dietitian.
8. Dietitian reviews and approves the plan.
9. System changes the plan status to **Approved** and makes it available for the subscription.

#### Alternate Flow – Constraint Violation

If the generated menu violates a dietary constraint or contains an excluded ingredient:

1. System rejects the generated menu.
2. System identifies the violated constraint or excluded ingredient.
3. System regenerates the menu using valid constraints.
4. If no compliant plan can be generated, the system flags the case for dietitian intervention.

### UC-03 – Review & Approve Meal Plan

**Primary Actor:** Dietitian

The dietitian reviews the generated weekly meal plan before it becomes available to the subscriber.

1. Dietitian receives a meal plan requiring review.
2. Dietitian reviews the generated menu and dietary constraints.
3. Dietitian approves the meal plan.
4. System changes the meal plan status to **Approved**.
5. The approved plan becomes available for the subscription.

### UC-04 – Manage Subscription

**Primary Actor:** Subscriber

The subscriber can:

- Pause the subscription
- Skip a scheduled delivery
- Reschedule the subscription

Subscription schedule modifications must follow the **12-hour-before-dispatch** requirement defined by **NFR-001**.

### UC-05 – Track Delivery Fulfillment

**Primary Actor:** Subscriber

The system records and displays the daily meal delivery fulfillment status.

The subscriber can check whether the scheduled meal delivery has been fulfilled.

## 7. Requirement-to-Use-Case Mapping

| Requirement | Related Use Case |
|---|---|
| **FR-001** | UC-02 – Generate Weekly Meal Plan |
| **FR-002** | UC-01 – Manage Dietary Profile |
| **FR-003** | UC-03 – Review & Approve Meal Plan |
| **FR-004** | UC-04 – Manage Subscription |
| **FR-005** | UC-05 – Track Delivery Fulfillment |
| **NFR-001** | UC-04 – Manage Subscription |
| **NFR-002** | Applies to system access and protected subscriber information |

## 8. System Architecture

The system follows a layered architecture consisting of:

### Presentation Layer

- Subscriber Interface
- Dietitian Interface

### Business / Application Layer

- Dietary Profile Management Service
- Meal Plan Generation Service
- Dietitian Review & Approval Service
- Authentication & Authorization Service
- Subscription Management Service
- Delivery Fulfillment Service

### Data Layer

- Application Database

The UML component architecture represents the interactions between these components using provided and required interfaces.

## 9. Major System Components

| Component | Responsibility |
|---|---|
| **Subscriber Interface** | Provides subscriber-facing functions. |
| **Dietitian Interface** | Provides dietitian-facing functions. |
| **Dietary Profile Management Service** | Manages subscriber dietary profiles. |
| **Meal Plan Generation Service** | Generates weekly meal plans according to dietary constraints. |
| **Dietitian Review & Approval Service** | Handles review and approval of generated meal plans. |
| **Authentication & Authorization Service** | Provides authenticated access and role-based authorization. |
| **Subscription Management Service** | Handles pause, skip, and reschedule operations. |
| **Delivery Fulfillment Service** | Records and displays daily delivery fulfillment status. |
| **Application Database** | Stores application data. |

## 10. Security

Subscriber dietary information is protected using:

- Authenticated access
- Role-based authorization
- Controlled access to subscriber dietary information

These requirements are defined under **NFR-002**.

## 11. System Workflow


Subscriber
    ↓
Manage Dietary Profile
    ↓
Generate Weekly Meal Plan
    ↓
Validate Dietary Constraints
    ↓
Generate Menu
    ↓
Dietitian Review
    ↓
Approve Meal Plan
    ↓
Meal Plan Available
    ↓
Subscription Management
    ↓
Daily Delivery
    ↓
Track Delivery Fulfillment
