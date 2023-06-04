# peak_detector
Measuring various metrics from ECG signals.

Code is maintained by Anthony Pinzone and Christian Niebling. 

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

## Development

Updating requirements.txt document
```
pip install pipreqs
pipreqs . --force
```

If you are maintaining a virtual environment, you can also generate the requirements.txt like so.
```
pip freeze > requirements.txt
```

We are trying to adhere to the coding guidelines specificed in [PEP 8](https://peps.python.org/pep-0008/). To automatically adhere code to the PEP 8 style guide you can run [autopep8](https://pypi.org/project/autopep8/).
```
pip install autopep8
autopep8 --in-place -a <filename>
```

In VSCode, the `pylint` extension can be installed to do code linting. Long term stretch goals would be to clean up all the linting errors. 

## Resources

[Inital Code example](https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.electrocardiogram.html#scipy.misc.electrocardiogram)
https://mne.tools/dev/generated/mne.io.read_raw_edf.html 
https://stackoverflow.com/questions/51869713/how-to-read-edf-data-in-python-3

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
