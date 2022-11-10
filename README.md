# peak_detector
measuring various metrics from ECG

## How to run

### set up a virtual environment called dev1
```
python -m venv dev1
```

### activate the virtual environment
```
.\dev1\Scripts\activate
```

### install dependencies 
```
pip install -r requirements.txt
```

### run the main script
```
python main.py
```

## Resources

[following this example code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.electrocardiogram.html#scipy.misc.electrocardiogram)

https://mne.tools/dev/generated/mne.io.read_raw_edf.html 
https://stackoverflow.com/questions/51869713/how-to-read-edf-data-in-python-3