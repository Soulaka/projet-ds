import pandas as pd
from src.utils import supprimer_lignes_vides

def test_supprimer_lignes_vides():
    df = pd.DataFrame({"a": [1, None, 3]})
    resultat = supprimer_lignes_vides(df)
    assert len(resultat) == 2