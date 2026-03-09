# 🌐 Frontend → Backend Communication Pipeline

This document explains how a **frontend (JavaScript running in the browser)** communicates with a **backend server (Python Flask)** using HTTP requests.

---

# Overview

When a user interacts with a webpage (for example clicking a button), JavaScript can send a request to a backend server. The server processes the request and sends a response back, usually in **JSON format**.

```
Frontend (Browser)
        │
        │ HTTP Request
        ▼
Backend (Server)
        │
        │ JSON Response
        ▼
Frontend Updates Page
```

---

# Visual Pipeline

```
┌───────────────────────────────┐
│           Browser             │
│                               │
│  HTML Page                    │
│  Button Click                 │
│  <button onclick="getMessage()"> 
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        JavaScript Engine      │
│                               │
│  getMessage() runs            │
│  fetch("/api/message")        │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│         Web API Layer         │
│                               │
│  Browser networking API       │
│  handles the fetch request    │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        Network Stack          │
│                               │
│  HTTP request created         │
│                               │
│  GET /api/message             │
│  Host: 127.0.0.1:5000         │
└───────────────┬───────────────┘
                │
                ▼
══════════════ NETWORK / TCP ══════════════
                │
                ▼
┌───────────────────────────────┐
│        Flask Web Server       │
│                               │
│  Request received             │
│  GET /api/message             │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│         Flask Router          │
│                               │
│  Matches route                │
│  @app.route("/api/message")   │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      Python Function Runs     │
│                               │
│  return jsonify({             │
│    "message": "Hello..."      │
│  })                           │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│        HTTP Response          │
│                               │
│  Status: 200 OK               │
│  Content-Type: application/json
│                               │
│  {"message":"Hello..."}       │
└───────────────┬───────────────┘
                │
══════════════ NETWORK / TCP ══════════════
                │
                ▼
┌───────────────────────────────┐
│           Browser             │
│                               │
│  fetch() promise resolves     │
│  response.json() parses data  │
└───────────────┬───────────────┘
                │
                ▼
┌───────────────────────────────┐
│      JavaScript Updates UI    │
│                               │
│ document.getElementById()     │
│ .innerText = data.message     │
└───────────────────────────────┘
```

---

# Step-by-Step Flow

### 1. User Action

A user clicks a button in the browser.

```html
<button onclick="getMessage()">Get Message</button>
```

---

### 2. JavaScript Sends Request

```javascript
fetch("/api/message")
```

The browser sends an **HTTP request** to the backend.

---

### 3. Backend Receives Request

The Flask server receives:

```
GET /api/message
```

Flask finds the matching route:

```python
@app.route("/api/message")
def get_message():
    return jsonify({"message": "Hello from Flask backend!"})
```

---

### 4. Backend Sends Response

The server sends a JSON response:

```json
{
  "message": "Hello from Flask backend!"
}
```

---

### 5. Frontend Processes Response

JavaScript converts the response to a JavaScript object:

```javascript
const data = await response.json();
```

---

### 6. Page Updates

JavaScript updates the HTML:

```javascript
document.getElementById("output").innerText = data.message;
```

---

# Key Concept

Most modern web applications follow this architecture:

```
Browser (Frontend)
        ↓
API Request
        ↓
Backend Server
        ↓
Database
        ↓
JSON Response
        ↓
Frontend Updates UI
```

---

# Summary

Frontend and backend communicate using **HTTP requests and responses**.

**Frontend responsibilities**

* Display user interface
* Send requests
* Render results

**Backend responsibilities**

* Handle requests
* Run business logic
* Access databases
* Return responses
