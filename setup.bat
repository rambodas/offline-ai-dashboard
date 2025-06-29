
@echo off
echo Setting up your offline AI dashboard environment...
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
echo Setup complete. Run: streamlit run dashboard_app.py
pause
