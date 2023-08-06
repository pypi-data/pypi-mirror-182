# rainreader
Python Package for reading KMD files from The Danish Meterological Institute (DMI) as well as simple analysis of the gauge data.
<b>To install:</b>

```
python -m pip install https://github.com/enielsen93/rainreader/tarball/master
```

## Example:
```
import rainreader
import matplotlib.pyplot as plt

rain = rainreader.KM2(r"\\files\Projects\RWA2022N000XX\RWA2022N00009\_Modtaget_modeller\Regnserier\Viby_godkendte_1979_2018.txt")

plt.figure()
plt.step(rain.gaugetime, rain.gaugeint)
plt.show()
```

<b>Function plot_IDF and rain_statistics are only available if python version is >3</b>
```
plt.figure()
rain.plot_IDF(time_aggregate_periods = [10, 30, 60, 120, 360, 1080])
plt.show()

rain_statistics = rain.rainStatistics()
```
