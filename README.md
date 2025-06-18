# 🧬 Acute Lymphoblastic Leukemia (ALL) Subtype Classification using MobileNetV2
**Acute Lymphoblastic Leukemia (ALL)** is the most common type of childhood cancer, affecting the white blood cells (lymphocytes) that help fight infection. In ALL, the bone marrow produces an excessive number of immature lymphoblasts, which can interfere with the production of normal blood cells.

This repository provides a deep learning solution to classify **Acute Lymphoblastic Leukemia (ALL)** subtypes using **peripheral blood smear (PBS)** images. It uses **MobileNetV2** as a feature extractor and a custom classifier to predict between four classes:

- Benign
- Early Pre-B ALL
- Pre-B ALL
- Pro-B ALL

> ✅ This project aims to support early detection of leukemia using AI by reducing manual misclassification in medical imaging.

---

## 📊 Dataset Description

**Source**: [Kaggle - Leukemia Classification Dataset](https://www.kaggle.com/datasets/mehradaria/leukemia)

- **Images**: 3256 blood smear images
- **Classes**:
  - Benign
  - Early Pre-B
  - Pre-B
  - Pro-B
- **Acquisition**: Zeiss microscope (100x magnification)
- **Segmentation**: HSV color-space based
- **Labeling**: Verified by flow cytometry

📝 *Please credit the authors when using this dataset.*

---

## 🧠 Model Details

- **Base**: MobileNetV2 (ImageNet pretrained)
- **Input Size**: 128x128 RGB
- **Final Layers**:
  - Global Average Pooling
  - Dropout (0.4)
  - Linear (1280 → 4 output classes)
- **Optimizer**: Adam
- **Loss Function**: CrossEntropyLoss
- **Epochs**: Up to 25 (with early stopping)

---

## 📈 Performance Metrics

| Class   | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| Benign  | 0.95      | 0.90   | 0.92     |
| Early   | 0.89      | 0.95   | 0.92     |
| Pre     | 0.96      | 0.93   | 0.94     |
| Pro     | 0.99      | 0.98   | 0.98     |

- **Accuracy**: `94%`
- **Macro Avg F1-Score**: `0.94`

---

## 📚 Citation
### Dataset Citation:

Mehrad Aria, Mustafa Ghaderzadeh, Davood Bashash, Hassan Abolghasemi, Farkhondeh Asadi, and Azamossadat Hosseini, “Acute Lymphoblastic Leukemia (ALL) image dataset.” Kaggle, (2021). DOI: 10.34740/KAGGLE/DSV/2175623.

### Publication Citation:
Ghaderzadeh, M, Aria, M, Hosseini, A, Asadi, F, Bashash, D, Abolghasemi, H. A fast and efficient CNN model for B-ALL diagnosis and its subtypes classification using peripheral blood smear images. Int J Intell Syst. 2022; 37: 5113- 5133. DOI:10.1002/int.22753



