from nbformat import write
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

#titleの追加
st.title("Streamlit 入門")
#コマンドの追加
st.write("DataFrame")

df = pd.DataFrame({
    "1列目": [1,2,3,4],
    "2列目": [10,20,30,40]
})
#表の作成write or DataFrame
st.write(df)
st.dataframe(df.style.highlight_max(axis=0),width=600,height=300)
#dataframe 細かい指定が可能highlight:data内の指定データにハイライトをつける
st.table(df)
#表示のデータを動かさない場合table

"""
# 章
## 節
### 項

```python
import streamlit as st
import numpy as np
import pandas as pd
```
"""

#📈
df = pd.DataFrame(
    np.random.rand(20,3),
    columns=["a","b","c"]
)
#rand(20,3) 乱数０−１

st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)

#map
df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.69,139.70],
    columns=["lat","lon"]
)
#lat:緯度,lon:経度,乱数0-1.50 ,[35.69,139.7]新宿の緯度経度
st.map(df)

#画像
img = Image.open("img1.jpg")
st.image(img, caption="yukihami", use_column_width = True)