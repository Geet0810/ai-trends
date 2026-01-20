from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_curve, auc
import plotly.graph_objects as go
import numpy as np

def roc_hvc_curve(data):
    X = np.random.rand(200,2)
    y = (X[:,0] > 0.6).astype(int)

    model = LogisticRegression().fit(X,y)
    preds = model.predict_proba(X)[:,1]

    fpr, tpr, _ = roc_curve(y, preds)
    roc_auc = auc(fpr, tpr)

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, name=f"AUC={roc_auc:.2f}"))
    st.plotly_chart(fig)
