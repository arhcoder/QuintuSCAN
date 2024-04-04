import joblib
from sklearn.ensemble import RandomForestClassifier

class AnomalIA:
    def __init__(self, binary_model, multi_model):

        '''# Modelo de clasificación binaria;
        # 0: Actividad normal; 1: Actividad anómala 
        self.binary_model = joblib.load(binary_model)

        # Modelo de clasificación multiclase;
        # Tipo de ataque [0, 9]:
        self.multi_model = joblib.load(multi_model)'''

        print("Espera un momenyo...")

        import pandas as pd
        train = pd.read_csv("data/UNSW_NB15_fisher_train.csv")
        test = pd.read_csv("data/UNSW_NB15_fisher_test.csv")
        # Data separation:
        train = train.drop(columns=["attack_cat", "attack"])
        test = test.drop(columns=["attack_cat", "attack"])

        X_train = train.drop(columns=["label"])
        y_train = train["label"]
        X_test = test.drop(columns=["label"])
        y_test = test["label"]

        seed = 11

        from sklearn.ensemble import RandomForestClassifier
        from sklearn.metrics import classification_report

        # Model training:
        self.binary_model = RandomForestClassifier(n_estimators=100, random_state=seed)
        self.binary_model.fit(X_train, y_train)
        y_pred = self.binary_model.predict(X_test)

        # binary_model evaluation:
        y_pred = self.binary_model.predict(X_test)
        print(classification_report(y_test, y_pred))

        train = pd.read_csv("data/UNSW_NB15_fisher_train.csv")
        test = pd.read_csv("data/UNSW_NB15_fisher_test.csv")

        train = train.drop(columns=["attack_cat", "label"])
        train = train[train["attack"] != 0]

        test = test.drop(columns=["attack_cat", "label"])
        test = test[test["attack"] != 0]

        X_train = train.drop(columns=["attack"])
        y_train = train["attack"]
        X_test = test.drop(columns=["attack"])
        y_test = test["attack"]

        # Model training:
        self.multi_model = RandomForestClassifier(n_estimators=100, random_state=seed)
        self.multi_model.fit(X_train, y_train)
        y_pred = self.multi_model.predict(X_test)

        # Model evaluation:
        y_pred = self.multi_model.predict(X_test)
        print(classification_report(y_test, y_pred))

        print("LISTO")



    
    def predict_anomaly(self, data_dict):
        try:
            data_array = [[data_dict[key] for key in sorted(data_dict.keys())]]
            predicted_class = self.binary_model.predict(data_array)
            return predicted_class[0]
        except:
            return None
    
    def predict_attack(self, data_dict):
        try:
            data_array = [[data_dict[key] for key in sorted(data_dict.keys())]]
            predicted_class = self.multi_model.predict(data_array)
            return predicted_class[0]
        except:
            return None


data = {
    "sttl": 254,
    "state_INT": 0,
    "ct_state_ttl": 0,
    "proto_tcp": 1,
    "swin": 255,
    "dload": 13446.84766,
    "state_CON": 0,
    "dwin": 255,
    "state_FIN": 1
}

ia = AnomalIA(
    "models/Anomalies_Detector/anomalies_rf.pkl",
    "models/Anomalies_Detector/attacks_rf.pkl"
)

print(ia.predict_anomaly(data))
print(ia.predict_attack(data))