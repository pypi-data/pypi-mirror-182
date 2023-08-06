# `modgraph`

`modgraph` is a tool to explore a collection of tracker <i>mod</i>ule files as a module->sample _graph_.
It can function both as a CLI app, and as a library to use in notebooks.
In fact, this file is a [notebook](README.ipynb)!

## Using through CLI


```python
!python -m modgraph --help
```

    usage: modgraph [-h] [-f {csv,d2}] [-r RANK] files [files ...]
    
    positional arguments:
      files                 module files to analyze
    
    options:
      -h, --help            show this help message and exit
      -f {csv,d2}, --format {csv,d2}
                            output format
      -r RANK, --rank RANK  min number of repeats for sample to be included


### Example:


```python
!python -m modgraph *.it --rank 6 --format csv
```

    mod_path,sample_name,sample_hash
    catherine on the waves.it,tambourin.steel.quiet     ,e1b32f84b2b788f0a58e277f4e152df5
    catherine on the waves.it,piano.001                 ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    dallying sadly in space.it,                          ,e1b32f84b2b788f0a58e277f4e152df5
    drifting to plutonia.it,tambourine.steel.quiet    ,e1b32f84b2b788f0a58e277f4e152df5
    heavenly fantasy.it,tambourin.steel.quiet     ,e1b32f84b2b788f0a58e277f4e152df5
    neverending illusion.it,piano.001                 ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    "so close to you, my angel.it",piano.001                 ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    sorrow.it,                          ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    sylvia.it,piano.001                 ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    tender storm.it,tambourin.steel.quiet     ,e1b32f84b2b788f0a58e277f4e152df5
    why (enhanced version).it,piano.001                 ,8ef52cdf9c20c9ada9df7bf4d3b59fc3
    why (enhanced version).it,tambourin.steel.quiet     ,e1b32f84b2b788f0a58e277f4e152df5


## Using as a library


```python
import pandas as pd
from modgraph import modgraph
from glob import glob

# digest your library into a mod_path -> sample_hash mapping
df = pd.DataFrame(modgraph(glob("*.it")))
df = df.set_index(['mod_path', 'sample_hash']).sort_index()
df
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>sample_name</th>
    </tr>
    <tr>
      <th>mod_path</th>
      <th>sample_hash</th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">a day at the river.it</th>
      <th>13dc761472f1e73cff4ed428be35a5c2</th>
      <td>SoundWave.HiQual</td>
    </tr>
    <tr>
      <th>29797bec77f15b782ee0d8f855720213</th>
      <td>rimshot</td>
    </tr>
    <tr>
      <th>3e741972e4147bfc395467a293bb11a4</th>
      <td>Flute (Skaven)</td>
    </tr>
    <tr>
      <th>46a82c17348315db0ec7d4558fb4a9e9</th>
      <td>fx.750</td>
    </tr>
    <tr>
      <th>6ce9cd4d2bd435dc6b410b4bc65eab2d</th>
      <td>river.wav (Eagle)</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">why (enhanced version).it</th>
      <th>d9d2074594be1e44cebafdc840c84b94</th>
      <td>DX-Strings 1</td>
    </tr>
    <tr>
      <th>dcacd358eb1c8a23027d1dad35e44726</th>
      <td>osterm1bass1</td>
    </tr>
    <tr>
      <th>e1b32f84b2b788f0a58e277f4e152df5</th>
      <td>tambourin.steel.quiet</td>
    </tr>
    <tr>
      <th>e4f1c0e5019b51ff947d0966eeac29f8</th>
      <td>electric.guitar.solo1</td>
    </tr>
    <tr>
      <th>f8d42ab1418cdbf77a53355b600fc7fe</th>
      <td>bassdrum.459</td>
    </tr>
  </tbody>
</table>
<p>216 rows × 1 columns</p>
</div>




```python
def most_used(df, cutoff):
    df = df.groupby("sample_hash")
    df = df.agg({"sample_name": [("name", lambda g: g.mode()[0]), "count"]})
    df = df.sort_values(("sample_name", "count"), ascending=False)
    df = df[df[("sample_name", "count")] >= cutoff]
    return df

most_used(df, cutoff=3).plot(kind="barh", x=('sample_name', 'name'))
```




    <AxesSubplot: ylabel='(sample_name, name)'>




    
![png](README_files/README_7_1.png)
    

