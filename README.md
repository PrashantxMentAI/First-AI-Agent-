# 🤖 First AI Agent — LangChain + Google Gemini


A beginner-friendly AI Agent built with **Python, LangChain, and Google Gemini**.


This project demonstrates how an AI agent can understand a user's request, decide which tool to use, execute the tool, use the result, and generate a final response.


The agent is currently focused on **mathematical problem solving using custom tools**.


---


## 🚀 Features


- 🤖 Google Gemini as the LLM
- 🧠 LangChain AI Agent
- 🛠️ Custom tools using LangChain's `@tool`
- ➕ Addition
- ➖ Subtraction
- ✖️ Multiplication
- ➗ Division
- √ Square root
- 🔢 Power calculation
- 🔄 Multi-step tool calling
- 🔐 API key management using `.env`
- 📦 Git and GitHub version control


---


## 🧠 How the Agent Works


The agent doesn't simply calculate the answer directly.


It receives a question, decides which tool is required, executes that tool, receives the result, and can then decide whether another tool is needed.


```text
                    User
                      │
                      ▼
              ┌───────────────┐
              │ Google Gemini │
              │      LLM      │
              └───────┬───────┘
                      │
                      ▼
                ┌───────────┐
                │   Agent   │
                └─────┬─────┘
                      │
               Selects a tool
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
     Addition     Multiplication   Division
        │             │             │
        └─────────────┼─────────────┘
                      │
                      ▼
                 Tool Result
                      │
                      ▼
                 Agent receives
                    result
                      │
                      ▼
                 Final Answer
```

## 🛠️ Tools

The agent currently has six custom mathematical tools.

### 1. Add Numbers
`add_numbers(a, b)`

Adds two numbers.

Example:
42 + 58 → 100

### 2. Multiply Numbers
`multiply_numbers(a, b)`

Multiplies two numbers.

Example:
15 × 8 → 120

### 3. Divide Numbers
`divide_numbers(a, b)`

Divides one number by another.
The tool also checks for division by zero.

Example:
120 ÷ 3 → 40

### 4. Subtract Numbers
`subtract_numbers(a, b)`

Subtracts one number from another.

Example:
100 - 25 → 75

### 5. Square Root
`square_root(a)`

Calculates the square root of a number.

Example:
√84 → 9.165...

### 6. Power
`power(a, b)`

Calculates a number raised to a power.

Example:
2⁵ → 32

---

## 🔄 Multi-Step Agent Execution

One of the main purposes of this project is to demonstrate that the agent can use multiple tools sequentially.

For example:

```text
User:
What is 15 multiplied by 8, then divided by 3?

        ↓

multiply_numbers(15, 8)

        ↓

120

        ↓

divide_numbers(120, 3)

        ↓

40

        ↓

Final Answer:
15 multiplied by 8 is 120, and then divided by 3 is 40.
```

Another example:

```text
User:
I have a rectangle with width 12 and height 7.
What is its area, and what is the square root of that area?

        ↓

multiply_numbers(12, 7)

        ↓

84

        ↓

square_root(84)

        ↓

9.165...

        ↓

Final Answer
```

This shows that the agent can determine that more than one tool is required to complete a task.

---

## 💻 Technologies Used
- Python
- LangChain
- LangGraph
- Google Gemini
- LangChain Google GenAI
- python-dotenv
- Git
- GitHub
- VS Code

---

## 📁 Project Structure

```text
First-AI-Agent-/
│
├── main.py
├── README.md
├── .gitignore
└── .env
```

### Files

* `main.py`: Contains the AI agent, tools, model configuration, and test questions.
* `README.md`: Project documentation.
* `.gitignore`: Prevents sensitive and unnecessary files from being uploaded to GitHub.
* `.env`: Stores the Gemini API key locally.

> [!WARNING]
> `.env` should NEVER be uploaded to GitHub.

---

## 🔐 Environment Variables

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=YOUR_GEMINI_API_KEY
```

Replace `YOUR_GEMINI_API_KEY` with your actual API key. Never share your API key publicly.

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```
2. **Go into the project directory:**
   ```bash
   cd First-AI-Agent-
   ```
3. **Install the required packages:**
   ```bash
   pip install langchain langgraph langchain-google-genai python-dotenv
   ```

---

## ▶️ Run the Agent

Run the Python file:
```bash
python main.py
```

The agent will execute the test questions and display the tool-calling process and final responses.

---

## 🧪 Example Tests

### Test 1
* **Input**: `"What is 42 + 58?"`
* **Expected result**: `42 + 58 = 100`

### Test 2
* **Input**: `"What is 15 multiplied by 8, then divided by 3?"`
* **Expected result**: `15 multiplied by 8 is 120, and then divided by 3 is 40.`

### Test 3
* **Input**: `"I have a rectangle with width 12 and height 7. What is its area, and what is the square root of that area?"`
* **Expected result**: `The area of the rectangle is 84. The square root of the area is approximately 9.165.`

---

## 🔒 Git & Security

The API key is stored in `.env` and should not be committed to GitHub.

The `.gitignore` file should contain:
```text
.env
__pycache__/
*.pyc
```

This keeps the API key and Python cache files out of the repository.

---

## 📚 What I Learned

Through this project, I learned the basics of building an AI Agent with an LLM and external tools.

### Concepts covered
* Python functions & decorators
* Environment variables & API integration
* LLMs (Google Gemini) & LangChain
* AI Agents & Tool calling / Function calling
* Sequential tool execution & Agent orchestration
* Git, GitHub & `.gitignore`

---

## 🔮 Future Improvements

Possible future improvements include:
- Add web search
- Add weather information
- Add file/document analysis
- Add calculator features
- Add conversation memory
- Add RAG
- Add external APIs
- Add a web interface
- Add voice interaction
- Add robotics-related tools
- Deploy the agent as a web application

---

## 🎯 Project Goal

The goal of this project is to understand the fundamental architecture of AI Agents:

```text
LLM → Agent → Tool Selection → Tool Execution → Tool Result → LLM → Final Response
```

This project serves as a foundation for building more advanced AI agents and eventually applying agentic AI concepts to real-world applications.

---

## 👨‍💻 Author

**Prashant**  
*B.Tech — Robotics & AI*

---

## ⭐ Project Status

* **Status**: 🟢 Working
* **Details**: The agent successfully performs single-step and multi-step mathematical tool calling using Google Gemini + LangChain.i