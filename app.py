import plotly.express as px
import pandas as pd

données = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSC4KusfFzvOsr8WJRgozzsCxrELW4G4PopUkiDbvrrV2lg0S19-zeryp02MC9WYSVBuzGCUtn8ucZW/pub?output=csv')

figure = px.pie(données, values='qte', names='region', title='quantité vendue par région')

figure.write_html('ventes-par-region.html')

figure = px.pie(données, values='qte', names='produit', title='quantité vendue par produits')

figure.write_html('ventes-par-produit.html')

données['CA'] = données['qte'] * données['prix']

figure = px.pie(données, values ='CA', names='produit', title='CA par produits')

figure.write_html('ca-par-produit.html')

print('ventes-par-région.html généré avec succès !\n')
print('ventes-par-produit.html généré avec succès !\n')
print('ca-par-produit.html généré avec succès !\n')