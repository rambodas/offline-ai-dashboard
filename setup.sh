
#!/bin/bash
echo "🔧 Setting up your offline AI dashboard environment..."
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "✅ Setup complete. Run: streamlit run dashboard_app.py"
