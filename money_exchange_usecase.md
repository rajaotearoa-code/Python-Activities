# Money Exchange System — Use Case Analysis

## 1. System Overview
A **Customer** uses the **Exchange Machine** to swap money, which automatically verifies their ID and charges their card (`<<include>>`), grants a bulk discount only if they trade a large amount (`<<extend>>`), and connects to payment processors and live forex market feeds behind the scenes to complete the transaction.

---

## 2. Use Case Diagram Layout

```text
+---------------------------------------------------------------------------------+
|                              Money Exchange System                              |
|                                                                                 |
|   [Customer] ---------> (View Live Exchange Rates) <--- [Forex Rate Feed API]   |
|         |                                                                       |
|         +-------------> (Calculate Conversion Estimate)                         |
|         |                                                                       |
|         +-------------> (Execute Currency Exchange)                             |
|                                |                                                |
|                                +---<<include>>---> (Verify Identity / KYC)      |
|                                |                          ^                     |
|                                |                          |                     |
|                                |                [AML Compliance System]         |
|                                |                                                |
|                                +---<<include>>---> (Process Payment)            |
|                                |                          ^                     |
|                                |                          |                     |
|                                |                  [Payment Gateway]             |
|                                |                                                |
|                                +---<<extend>>----> (Apply Volume Discount)      |
|                                                                                 |
|   [Teller] -----------> (Dispense Physical Currency)                            |
|   [Admin] ------------> (Adjust Currency Spread Margins)                        |
+---------------------------------------------------------------------------------+
```

---

## 3. Relationship Explanations

* **`<<include>>` (Verify Identity / KYC):** A mandatory subtask required for regulatory compliance that runs automatically for every exchange transaction.
* **`<<include>>` (Process Payment):** A mandatory step that extracts funds (via cash or payment gateway) before currency can be dispensed.
* **`<<extend>>` (Apply Volume Discount):** A conditional branch that only activates if the transaction amount exceeds a set threshold (e.g., trades over $5,000).

---

## 4. Formal Use Case Specification

| Field | Description |
| :--- | :--- |
| **Use Case Name** | `Execute Currency Exchange` |
| **Primary Actor** | Customer (or Teller) |
| **Supporting Actors** | Forex Rate Feed API, Payment Gateway, AML Registry |
| **Preconditions** | Forex rate feeds active; target currency stock available in local reserve |
| **Postconditions** | Source funds deducted, target currency dispensed, transaction logged |

### Normal Flow of Activities
1. Customer specifies source currency, target currency, and amount.
2. System fetches current spot rate from Forex API, applies margins, and displays quote.
3. Customer accepts quote and selects payment method.
4. System executes `Verify Identity` against AML database records (`<<include>>`).
5. System checks transaction amount and evaluates `Apply Volume Discount` condition (`<<extend>>`).
6. System executes `Process Payment` via connected payment gateway (`<<include>>`).
7. System updates internal reserves, dispenses currency/prints confirmation, and logs the transaction.

### Exception Conditions
* **Payment Declined:** Payment gateway rejects card $\rightarrow$ Transaction aborts immediately with no reserve change.
* **Insufficient Reserves:** Physical currency out of stock $\rightarrow$ System offers digital transfer or cancels safely.