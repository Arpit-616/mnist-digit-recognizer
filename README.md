# 🖊️ MNIST Handwritten Digit Recognizer

A simple and interactive **Streamlit web app** that recognizes handwritten digits (0–9) using a trained deep learning model on the [MNIST dataset](http://yann.lecun.com/exdb/mnist/).

## 🚀 Features
- 📂 **Upload a digit image** (PNG/JPG/JPEG) for recognition  
- ✍️ **Draw a digit** directly in the browser with an interactive canvas  
- ⚡ **Real-time prediction** with confidence scores visualized as a bar chart  
- 🎯 Uses a **TensorFlow/Keras CNN model** trained on MNIST  

## 🖼️ Demo
Example workflow:  
1. Upload or draw a digit  
2. The model predicts the digit  
3. Confidence distribution is shown as a bar chart  


## 📦 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/mnist-digit-recognizer.git
   cd mnist-digit-recognizer
   ````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Make sure you have the trained model file `mnist_model.h5` in the project directory.

   * If you don’t have it, you can train one yourself using TensorFlow/Keras on MNIST.

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

## 🛠️ Requirements

* Python 3.8+
* TensorFlow / Keras
* NumPy
* Pillow (PIL)
* Streamlit
* streamlit-drawable-canvas

Install them with:

```bash
pip install tensorflow numpy pillow streamlit streamlit-drawable-canvas
```

## 📂 Project Structure

```
mnist-digit-recognizer/
│── app.py              # Streamlit app
│── mnist_model.h5      # Trained CNN model
│── requirements.txt    # Dependencies
│── README.md           # Project documentation
```

## 📊 Model Details

* Trained on the MNIST dataset (60,000 training digits, 10,000 test digits)
* Input: 28x28 grayscale images
* Output: Probability distribution over digits (0–9)
* Architecture: Convolutional Neural Network (CNN)

## ✨ Future Improvements

* Improve accuracy on non-MNIST style digits (different handwriting styles)
* Add option to retrain the model directly from the app
* Deploy on **Streamlit Cloud** or **Heroku** for easy access

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repo and submit a pull request.

## 📜 License

This project is licensed under the MIT License.

---

💡 Made with ❤️ using Streamlit and TensorFlow

```
