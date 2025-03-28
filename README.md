# AI-Based Personal Finances and Investments Advisor

## 📜 Project Description
A web-based application built with Flask and Streamlit to manage personal finances and investments, featuring an integrated Finance Advisor Chatbot. Users can input financial data (income, expenses, savings, investments, and goals) to receive detailed analysis and predictions, while the chatbot provides expert advice across various finance domains.

## 🪟 Project Images
<div style="display: flex; gap: 10px;">
    <img src="images/chatbot.png" alt="Chatbot Image" width="200"/>
    <img src="images/financial_tracker_prompt.png" alt="Financial Tracker Prompt Image" width="200" height="360"/>
    <img src="images/financial_tracker_analyze.png" alt="Financial Tracker Analyze Image" width="200" height="360"/>
</div>

## 🛠️ Tech Stack
- **Programming Language:** Python 
- **Backend:** Flask (for APIs)  
- **Frontend:** HTML/CSS  
- **Machine Learning:** Scikit-learn, TensorFlow, PyTorch  
- **APIs & Data Sources:** Hugging Face, Alpha Vantage, Yahoo Finance  

## ✨ Features
- **Financial Tracking**: Input monthly income, expenses (e.g., rent, groceries), savings, and custom stock investments (any ticker symbol and share count).
- **Analysis**: Calculates total expenses, surplus, net worth, and current portfolio value using live stock data from Yahoo Finance (`yfinance`).
- **Machine Learning**: Trains a linear regression model to predict portfolio value 30 days ahead based on historical stock prices.
- **Chatbot**: An AI-powered Finance Advisor Chatbot, offering advice on:
  - Personal Finance (budgeting, savings, investing, retirement, debt, insurance)
  - Corporate Finance (capital budgeting, structure, M&A)
  - Public Finance (government budgeting, taxation)
  - International Finance (FX, trade, cross-border investments)
  - Behavioral, Quantitative, Islamic, ESG, Fintech, and Wealth Management
- **Modern UI**: Responsive design with Bootstrap, a gradient background, and a sleek chat popup with animations.

## ✅ Prerequisites
- **Python**: 3.10 or higher
- **Dependencies**: Install required libraries with:
  ```bash
  pip install pandas yfinance numpy flask scikit-learn python-dotenv langchain-community
  ```
- **Hugging Face API Token**: Required for the chatbot. Sign up at Hugging Face and generate a token.

## 📂 Project Structure
```
project/
├── app.py          # Flask app with PFIM logic
├── chat.py          # Streamlit app with Chatbot logic
├── static/
│   └── index.css   # style sheet for PFIM form
├── templates/
│   └── index.html   # Template for PFIM form
├── images/          # Screenshot Images of the project
│   ├── chatbot.png
│   ├── financial_tracker_analyze.png
│   └── fianacial_tracker_prompt.png
├── .env             # Environment file for API token
├── README.md        # This file
```

## ⚙️ Installation Guide
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ai-finance-advisor
   ```
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Configure Environment:
   Create a `.env` file in the root directory with your Hugging Face API token:
   ```
   HUGGINGFACEHUB_API_TOKEN = your_huggingface_api_token_here
   ```
6. Organize Files:
   Ensure `app.py` is in the root directory and `index.html`   is inside a `templates` subfolder.

7. Run the Application:
   In the terminal, navigate to the project directory and   execute:
   ```bash
   streamlit run chat.py
   ```
   In the second terminal, navigate to the project directory and   execute:
   ```bash
   python app.py
   ```

## ▶️ Usage
### Access the Website:
Open a browser and go to `http://127.0.0.1:5000/` (or `http://<your-ip>:5000/` on your network).

### PFIM Form:
- **Income and Savings**: Enter your monthly income and current savings.
- **Expenses**: Fill in amounts for rent, groceries, entertainment, and utilities.
- **Investments**: Add stock investments by entering ticker symbols (e.g., "TSLA") and share counts. Click "Add Investment" for more entries.
- **Goals**: Specify targets for an emergency fund and retirement savings.
- Click "Analyze" to see results (expenses, surplus, net worth, portfolio values, and recommendations).

### Chatbot:
- Type a finance-related question (e.g., "How do I budget?").
- The chatbot responds with expert advice based on the Mistral-7B model from Hugging Face.

## 🌟 Example
### PFIM Input
```
Income: $3000
Expenses: Rent $1000, Groceries $500
Savings: $2000
Investments: TSLA (10 shares), GOOGL (5 shares)
Goals: Emergency Fund $5000, Retirement $50000
```
### PFIM Output
```
Total Expenses: $1500
Monthly Surplus: $1500
Net Worth: $X.XX (savings + current portfolio)
Current Portfolio Value: $Y.YY (based on live prices)
Predicted Portfolio Value (30 days): $Z.ZZ (ML prediction)
Recommendations:
- Monthly surplus: $1500. Consider saving $900.00 and investing $600.00.
- Emergency fund shortfall: $3000.00. Prioritize savings.
- Current portfolio value: $Y.YY. Predicted value in 30 days: $Z.ZZ.
```

### Chatbot Interaction
```
User: "Hello"
Chatbot: "Hello! How can I assist you today? Are you looking for advice on personal finance, corporate finance, public finance, or international finance? ..."
User: "Investment options"
Chatbot: [Detailed response on investment strategies from the model]
```

## 🏗️ Technical Details
- **PFIM Model**: Linear Regression (`scikit-learn`) trained on 1 year of historical stock prices from `yfinance`. Predicts portfolio value 30 days ahead.
- **Chatbot Model**: Mistral-7B-Instruct-v0.3 via Hugging Face Endpoint (`langchain-community`), with a custom prompt for finance expertise.
- **UI**: Bootstrap 5.3 for responsiveness, Font Awesome for the chat icon, and custom CSS for a gradient background, shadows, and animations.

## 🛑 Troubleshooting
- **Portfolio Value $0**: Check internet connection or verify ticker symbols (e.g., "AAPL" not "Apple").
- **Chatbot Not Responding**: Ensure the Hugging Face API token is valid in `.env`.
- **Layout Issues**: Test on different screen sizes; adjust `.chat-window` width/position if needed.

## 🔮 Future Enhancements
- Add chat history persistence with a database (e.g., SQLite).
- Implement auto-scroll to the latest chat message.
- Add a close button to the chat window.
- Enhance ML model with time series forecasting (e.g., LSTM).

## 🤝 Collaborators
- Devanshu Sawarkar ([GithubID](https://github.com/DevanshuSawarkar))
- Pratham Agrawal ([GithubID](https://github.com/PrathamAgrawal51))
- Devansh Motghare ([GithubID](https://github.com/devansh7444))

## 🎓 Mentors
- Dr. Latika Pinjarkar

## 📖 Guides
- Dr. Parul Dubey

## ⚖️ License
This project is open-source under the MIT License. Feel free to modify and distribute. 
