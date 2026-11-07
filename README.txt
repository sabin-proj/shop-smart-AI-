SHOPSMART AI WEBSITE — SIMPLE SETUP

You already trained and saved shopsmart_model.pkcls in Orange.

1. Extract the ShopSmart_AI_Website.zip file.
2. Copy your shopsmart_model.pkcls file from your Desktop into the ShopSmart_AI_Website folder, next to app.py.
3. Open Command Prompt in that folder (in Windows File Explorer, open the folder, click the address bar, type cmd, and press Enter).
4. Install the required Python packages by running:
   python -m pip install -r requirements.txt
5. Start the website by running:
   python app.py
6. Open http://127.0.0.1:5000 in your browser.
7. Fill in the shopping questions and click Get my recommendation.

If Windows says 'python' is not recognized, install Python or use the Python environment where Orange3 is installed.

IMPORTANT:
- The website uses your saved Orange model to make predictions. It does not send data back to the Orange canvas.
- If the model's feature categories are different from the options on the page, adjust the HTML options to match your model's values.
- http://127.0.0.1:5000 is LOCAL: it only works on your own computer. For other people to test remotely, this Flask app and the model file must be deployed to a server. Do not send the local link to other people.
- Only load a .pkcls file you created yourself or trust: Python pickle files can execute code when loaded.
- The model was trained on a small synthetic dataset, so recommendations are experimental.
