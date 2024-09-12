# 🐘 WildGuard | AnimalHack 2024

WildGuard (Poaching Detection System) is a web application designed to monitor and detect wildlife poaching activities. By leveraging the power of **Google Earth Engine** and a **machine learning model** trained on historical elephant poaching data, we provide insights into poaching hotspots. Our goal is to support conservation efforts and protect endangered wildlife species.

## ✨ Features
- **Geospatial Data Integration**: Uses Google Earth Engine to provide satellite imagery and geospatial data.
- **Poaching Detection**: Machine learning model trained on elephant poaching statistics to identify potential incidents.
- **User-Friendly Interface**: Built with **Svelte** and **Bootstrap** for a responsive and accessible front-end experience.
- **Backend Support**: Powered by **Django** to manage user data and handle server-side logic.

## 🛠️ Tech Stack
- **Frontend**: Svelte, Bootstrap
- **Backend**: Django
- **Machine Learning**: Yolo V5, Pytorch, TensorFlow, Jupyter Notebook
- **API**: Google Earth Engine API

## 🚀 Setup and Installation

### Prerequisites
- **Python 3.8+**
- **Node.js**
- **pip** (Python package manager)
- **Google Earth Engine Account** (Authenticated)

### Installation Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/wildguard.git
   cd wildguard

2. **Set up the virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt

4. **Install frontend dependencies:**
    ```bash
    cd frontend
    npm install

5. **Set up Google Earth Engine authentication:**
    Run the following command to authenticate:
    ```bash
    earthengine authenticate

6. **Apply Django mirgrations:**
    ```bash
    cd ../backend
    python manage.py migrate

7. **Run the application:**
    * **Start the Django server:**
     ```bash
     python manage.py runserver
     ```
   * **Start the Svelte frontend:**
     ```bash
     cd ../frontend
     npm run dev
     ```

8. **Access the application**:
   * Open `http://127.0.0.1:8000` to access WildGuard locally.

## 👥 Team BAHA

BAHA stands for:
- Britaney Do
- Aurelisa Sindhu
- Hong Le
- Aurelia Sindhu


## 🤝 Contributions

We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## 🎉 Achievements


* **2nd Place Winner**: Won second place in the conservation-themed hackathon for wildlife protection. [View on Devpost](https://devpost.com/software/wildguard)
* **Successful API Integration**: Integrated Google Earth Engine for satellite data analysis.
* **Developed ML Model**: Trained a model using a specialized elephant poaching dataset from Roboflow.

## 🔮 What's Next

* Expand detection capabilities to other endangered species.
* Introduce real-time alerts for conservationists and authorities.
* Improve public engagement and education on wildlife protection.


