### **Hybrid Neural Networks with Signal Transformation for EEG-Based Abnormal Brain Activity Classification**

GitHub Project Link : https://github.com/Advaith789/brain-waves-classification 

Manasi Gosavi mjgosavi@wisc.edu 

Advaith Chandra Srivastav asrivastav4@wisc.edu 

Yash Deshpande yadeshpande@wisc.edu 

Connor Welch cwwelch@wisc.edu

1. Overview:

With this project, we plan to classify brain activity as detected by electroencephalography (EEG) into seizure, generalized periodic discharges, lateralized periodic discharges, generalized rhythmic delta activity, lateralized rhythmic delta activity, or other. The goal is to create a model that can accurately detect abnormal brain activity and therefore result in better healthcare.

2. Background:

EEG monitoring relies on specialized neurologists, making it costly, time-consuming, and prone to human error and subjective interpretation. This limits healthcare efficiency, highlighting the need for a more objective assessment method.
Historically, traditional machine learning algorithms have been proposed to automate seizure detection using SVM, random forests, and ensemble learning. While there has been some promise in these proposals, the inherent weakness has mainly been the necessity for manual optimization of parameters which requires expertise and opens the door for biases.[2]
Over the last decade, advances have been made through the application of deep learning techniques like convolutional neural networks, recurrent neural networks, and deep belief networks. Further promise has been shown by hybrid algorithms that use either a combination of deep learning techniques or a combination of deep learning methods with more traditional machine learning algorithms.
Hybrid methods using CNNs, RNNs, and deep learning lead in seizure detection but focus solely on binary classification. Manual monitoring is still required for a full assessment of brain health.
Recent advancements in EEG analysis for seizure detection integrate AI-driven monitoring devices, advanced computational tools, and intracortical signal analysis. Technologies like CeriBell's AI-powered headband enable rapid seizure detection in clinical settings[7], while tools like EZTrack improve epileptogenic zone identification, enhancing surgical outcome predictions. Additionally, intracortical EEG signal analysis (minedICE) leverages AI to interpret brain activity in real-time, aiding timely interventions. These innovations significantly improve the accuracy and speed of seizure detection, benefiting patient care and neurological research.

3. Statement of Work

3-1. Datasets: 

We will be using the dataset found here on kaggle provided by Harvard Medical School for the Harmful Brain Activity Classification competition. It provides 28,440 files of data consisting of a combination of 17,301 files of raw EEG data and 11,139 files of EEG data assembled into spectrograms. In addition, there is a metadata spreadsheet that comes with labels of seizure, lateralized periodic discharges, generalized periodic discharges, lateralized rhythmic delta activity, generalized rhythmic delta activity, or other for the datasets. It also comes with a vote distribution displaying how many neurologists voted for the consensus label and how many disagreed and what they thought the label should be instead [3].
3-2. Method:

We plan to explore a variety of different methods for achieving classification of brain activity. The first step will be some type of signal processing to make the data more useful as input to a neural network. This may involve but would not be limited to a discrete fourier transform of a discrete wavelet transform. It also may involve filtering of some kind such as a bandpass filter to try and isolate the signals that are the most relevant to classification as was done in a study by Sameer and Gupta in 2020 [4].
After being processed, the data will then be input into a neural network. This may take the form of a multilayer perceptron, a convolution neural network, a recurrent neural network (such as a long short-term memory), a transformer, or most likely some hybrid combination of these networks, such as the hybrid convolution neural network and recurrent neural network model developed by Abdulwahhab, Abdulaal, et al. in 2024 [5]. For the voltage signal in particular, we may also use a model that’s been pre-trained on audio signals due to the similarity between the brain wave signals and the audio signals.
The output of the neural network will be a predictive probability distribution of the brain activity being a seizure, generalized periodic discharges, lateralized periodic discharges, generalized rhythmic delta activity, lateralized rhythmic delta activity, or other. The brain activity will be classified as the one with the highest probability.
The hope with this project is that more accurate classification of harmful brain activity can result in better treatment and ultimately better outcomes for patients.

3-3. Outcome and Performance Evaluation

Expected Outcome:

This project aims to develop a robust and efficient method for classifying brain activity using deep learning models. By evaluating various architectures—including MLPs, CNNs, LSTMs, Transformers, and hybrid models—we seek to determine the optimal approach in terms of accuracy and computational efficiency. A successful outcome would enhance classification precision, enabling neurologists to make faster and more reliable diagnoses.
Evaluation Metrics:

To assess the performance and feasibility of our approach, we will employ the following key metrics:

Classification Accuracy: Quantify the model’s ability to correctly classify brain activity compared to expert neurologist consensus.

Kullback-Leibler (KL) Divergence: Measure the alignment between the model’s probability distribution and neurologist-assessed labels.

F1 Score, Precision, and Recall: A balanced evaluation of classification performance, particularly for imbalanced EEG and spectrogram data.

Computational Efficiency & Cost: Analyze training time, inference speed, and resource requirements to ensure a cost-effective solution.

Robustness & Generalization: Evaluate the model’s ability to maintain high performance across different datasets and real-world scenarios.

Comparison with Baseline Models: Benchmark deep learning models against traditional machine learning methods such as SVMs and Random Forests.

Success Criteria:

Achieves classification accuracy comparable to or better than existing high-performing models.
Minimizes KL divergence to closely align with expert-assessed probability distributions.
Maintains a high F1 score with strong precision and recall.
Balances computational efficiency with classification performance.
Demonstrates strong generalization across diverse datasets.
By systematically comparing multiple deep learning models, this project aims to identify the most effective approach for brain activity classification, ultimately contributing to improved clinical outcomes and advancing automated diagnostic tools.


Gantt Chart:
<img width="1196" alt="image" src="https://github.com/user-attachments/assets/521a52f8-b46a-49e0-9334-181e3bdef979" />


4. References

[1] https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/overview

[2] https://www.sciencedirect.com/science/article/abs/pii/S0925231224014152

[3] https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/data

[4] https://link.springer.com/article/10.1007/s11277-020-07542-5

[5] https://www.sciencedirect.com/science/article/pii/S0960077924002522

[6] https://www.kaggle.com/competitions/hms-harmful-brain-activity-classification/leaderboard

[7]https://pmc.ncbi.nlm.nih.gov/articles/PMC8013275/
