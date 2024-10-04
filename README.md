# Forecasting Solar Flares with Machine Learning to Mitigate Solar Flare Damage

**Objective:**  
Predict solar flares to provide early warnings, helping to protect Earth’s electrical infrastructure. Strong solar flares can permanently damage these systems, and advanced forecasting could allow for preventive measures, like diverting electricity and creating buffers.

---

## Background

Solar flares occur when the Sun’s magnetic field lines become too tangled, causing them to “snap” and release a surge of energy toward Earth. While no single pathway reliably predicts a solar flare, physics equations that describe magnetic activity provide a foundation for prediction.

This research aims to combine machine learning and physics to optimize solar flare prediction times, making the process practical and actionable.

---

## Data Types and Sources

1. **Image Data**  
   - Filtograms, HMI continuums, and magnetograms from the **Solar Dynamics Observatory**.

2. **Numerical Data**  
   - The **F10.7 index** of solar weather from the Canadian government, which shows spikes during flares.

---

## Methodology

- **Data Processing**  
  Images are processed with a Spatial Possibilistic Clustering Algorithm, while F10.7 index data is interpolated. The processed data is then split into training and test sets.

- **Modeling**  
  - A **Convolutional Neural Network (CNN)** predicts solar flares using input variables from the training set.
  - The model’s accuracy is evaluated on the test set with **Mean Squared Error (MSE)** and **Root Mean Squared Error (RMSE)**.

- **Optimization**  
  - A **Physics-Informed Neural Network (PINN)** is incorporated to improve CNN predictions without significantly increasing computation.

---

## Future Work

Future improvements may include:
- An **ensemble learning model** combining CNN and PINN methods for greater prediction accuracy.
- Exploring alternative model architectures that can integrate with the current approach.

---

## Authors
*Indira Mariya* <br>
*Aviv Kanarik*

--- 
