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

## Acronyms 
## NN -> Normal-Normal, refers to R intervals that display normal characteristics
## RMS -> Root Mean Square

## Poincare -> Refers to a type of graph (Poincare Plot)

## SDNN -> Standard deviation of all Normal-Normal R Intervals
## RMSSD -> Root mean square of all successive differences between R-R Intervals

## SD1 and SD2 -> Variables calculated off of SDNN and SDSD, represent the long and short axes of the ellipse on the Poincare plot

## HR and BP -> Heart Rate and Blood Pressure

## pNN50 -> Number of R-R intervals with successive differences that exceed 50 ms, expressed as a percentage 
## RRI -> plot generated of all of the successive differences between RR Intervals
