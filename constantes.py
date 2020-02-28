class CONSTANTE:
    DB_NAME = "ma_base.db"

    MOCK_DATA = [
        {"client_name": "Laurent", "tech_name": "Bob", "intervention_date": "2020/11/01",
         "intervention_type": "réparation",
         "description": "Le client à une fuite avec sa machine à laver"},
        {"client_name": "Natacha", "tech_name": "Dorian", "intervention_date": "2020/06/23",
         "intervention_type": "diagnostique",
         "description": "Le client demande une intervention pour vérifier son lave vaisselle"}
    ]

    TABLE_NAME = "intervention"
    INTERV_VALID_ERROR = "Champ manquant ou incomplet: "
    GET_ALL_EMPTY_LIST = "Aucune intervention n'est disponible"