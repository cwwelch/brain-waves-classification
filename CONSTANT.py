FEATURES = ['Fp1', 'F3', 'C3', 'P3', 'F7', 'T3', 'T5', 'O1', 'Fz', 'Cz', 'Pz', 'Fp2', 'F4', 'C4', 'P4', 'F8', 'T4', 'T6', 'O2', 'EKG']

LL = ['Fp1', 'F7', 'T3', 'T5', 'O1']
LP = ['Fp1', 'F3', 'C3', 'P3', 'O1']
RP = ['Fp2', 'F4', 'C4', 'P4', 'O2']
RR = ['Fp2', 'F8', 'T4', 'T6', 'O2']
IMPT_ELECTRODES = ['Fp1', 'O1', 'Fp2', 'O2']


PATH_TO_FILES_TRAIN_EEG = '/Users/Patron/Documents/brain-waves-classification/hms_data/train_eegs'
PATH_TO_TRAIN_CSV = '/Users/Patron/Documents/brain-waves-classification/hms_data/train.csv'
PATH_TO_MERGE_PARQUET = '/Users/Patron/Documents/brain-waves-classification/hms_data/combined_parqs'
PATH_TO_FILES_TRAIN_SPECT = '/Users/Patron/Documents/brain-waves-classification/hms_data/train_spectrograms'

SAMPLE_RATE = 44100  # Hertz
DURATION = 5  # Seconds