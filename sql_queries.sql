SELECT *
FROM ventes;

SELECT 
SUM(
  CASE
  WHEN produit = 'Produit A' then prix * qte
  WHEN produit = 'Produit B' then prix * qte
  WHEN produit = 'Produit C' then prix * qte
  ELSE 0
  END) as chiffre_affaire,
SUM(CASE WHEN produit = 'Produit A' THEN qte else 0 END) as ventes_produit_a,
SUM(CASE WHEN produit = 'Produit B' THEN qte ELSE 0 END) as ventes_produit_b,
SUM(CASE WHEN produit = 'Produit C' THEN qte ELSE 0 END) as ventes_produit_c,
SUM(CASE WHEN region = 'Sud' then qte ELSE 0 END) as ventes_sud,
SUM(CASE WHEN region = 'Nord' then qte ELSE 0 END) as ventes_nord
FROM ventes
