@echo off
cd "D:\First Puthon"  # Aapke project ka folder
call ".venv\Scripts\activate"  # Virtual environment activate karein
streamlit run deshbord.py  # Streamlit dashboard run karein
pause  # Command prompt window ko khulne ke liye

