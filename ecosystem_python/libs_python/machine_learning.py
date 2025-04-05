# scikit-learn (ML tradicional)
from sklearn.ensemble import RandomForestClassifier

clf = RandomForestClassifier()
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

# tensorflow/pytorch (Deep Learning)
import torch

model = torch.nn.Linear(10, 2)  # Camada fully-connected
# Comparação C++: LibTorch (PyTorch C++ API)
