# 🚨 AI-Powered Emergency Call Center Assistant

> A real-time intelligent assistant designed to improve emergency response through automated speech recognition, natural language understanding, emotion detection, and geospatial awareness.

---

## 📌 Overview

This project introduces an **AI-enhanced emergency call center assistant** that automates the transcription, interpretation, and visualization of emergency calls to improve decision-making and reduce dispatcher workload. It integrates state-of-the-art models such as:

* **Whisper & Wav2Vec2** for speech-to-text and emotion recognition
* **BERT** for Named Entity Recognition (NER)
* **Google Maps API** for real-time geospatial visualization

The system extracts caller location, type of emergency, and emotional state to assist dispatchers in making faster, data-driven decisions.

---

## 🧠 Key Features

* 🎧 **Real-time speech transcription** using Whisper and Wav2Vec2
* 📟 **Named Entity Recognition (NER)** with BERT for extracting key information (location, emergency type)
* 😟 **Emotion detection** to assess urgency and distress levels in the caller’s voice
* 🗺️ **Geolocation mapping** using Google Maps API for precise incident visualization
* 🧹 **Noise reduction** and audio preprocessing for reliable performance in chaotic call environments
* 🤗 **Modular REST APIs** for easy integration with existing emergency infrastructure

---

## ⚙️ System Architecture

1. **Audio Input**
   → Whisper/Wav2Vec2 transcribes voice to text
2. **Preprocessing**
   → Noise removal, tokenization, stopword removal, spelling correction
3. **Information Extraction**
   → BERT-based NER to identify entities like locations, incidents
4. **Emotion Analysis**
   → Wav2Vec2 evaluates caller tone for urgency
5. **Geolocation**
   → Google Maps API converts location entities to coordinates
6. **Dispatcher Interface**
   → Outputs structured call summary and situational map

---

## 📊 Performance

| Component            | Model    | Accuracy |
| -------------------- | -------- | -------- |
| ASR (Speech-to-Text) | Wav2Vec2 | 92.5%    |
|                      | Whisper  | 90.0%    |
| NER (NLP)            | BERT     | 92.5%    |
| Emotion Detection    | Wav2Vec2 | 91.5%    |

* **WER (Word Error Rate)** was significantly lower with Wav2Vec2 in noisy conditions.
* **BERT** outperformed rule-based approaches in entity recognition.
* Emotion detection enabled dynamic call prioritization.

---

## 🧪 Datasets Used

* **RAVDESS**: Ryerson Audio-Visual Database for Emotion Recognition
* **IEMOCAP**: For training emotion detection models
* **Custom annotated transcripts**: For NER training and evaluation

Noise overlays and speed variation techniques were applied to simulate real emergency conditions.

---

## 🤀 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/ryanbinny/Main-Project.git
cd Main-Project

# Install dependencies
pip install -r requirements.txt
```

> Note: Large model files (e.g., `.safetensors`) are managed via Git LFS. Make sure [Git LFS](https://git-lfs.github.com/) is installed and initialized.

---

## 🚀 How to Run

```bash
# Run the main pipeline
python main.py
```

Ensure you have:

* A valid Google Maps API key (if geolocation is used)
* Pretrained model files (Wav2Vec2, BERT, etc.) downloaded or loaded

---

## 📍 Real-World Applications

* Emergency dispatch centers
* Natural disaster response systems
* Public safety operations
* Smart city incident management

---

## ⚠️ Limitations & Challenges

* Emotion analysis can underperform in multilingual or noisy settings.
* Accuracy may be affected by dialects or slang not present in training data.
* Real-world deployment requires strong data privacy compliance (e.g., GDPR, DPDP Act).

---

## 🔮 Future Enhancements

* **Multilingual support** for broader accessibility
* **Graph Neural Networks (GNN)** and **YOLOv8** for real-time IoT + video integration
* **T5 and GPT-based text generation** for automated reporting and summary
* Enhanced **robustness** against ambient noise and overlapping speech
* More inclusive training datasets for cultural and regional diversity

---

## 👨‍💼 Authors

* Annmaria Mathew Shibu
* Alphin Tom
* Rohan Majo Mathew
* Ryan Binny Mathews
* Jacob Thomas
* Renjith Thomas

---
