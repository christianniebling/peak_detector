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

## GUI

To generate the gui python code from the ui xml file
```
pyuic5 -x form.ui -o form.py
```

## Resources

[following this example code](https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.electrocardiogram.html#scipy.misc.electrocardiogram)