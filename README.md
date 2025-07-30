
![banner](img/lancelot_banner_final_1600x400_clean.png)

# 📜 Across Languages, Lancelot Rides  
*Tracing Lancelot’s journey not only through lands and courts, but through languages, manuscripts, and time.*

> An aligned multilingual corpus of the *Lancelot en prose*, processed with [Aquilign](https://github.com/ProMeText/Aquilign).


## 📚 Description
This repository hosts the training data and aligned outputs for a multilingual medieval tradition.

This repository contains a subset of aligned witnesses from the *Lancelot en prose*, one of the core cycles of the Arthurian literary tradition. The corpus is multilingual (Old French, Castilian, Italian) and has been segmented and aligned using the [Aquilign](https://github.com/ProMeText/Aquilign) pipeline, a BERT-based tool for multilingual clause-level alignment of medieval texts.

## 🧰 Alignment Tool

The corpus was processed using **Aquilign**, a multilingual alignment tool developed by the [ProMeText](https://github.com/ProMeText) team.  
The texts were first segmented into clauses (`<cl>`) with custom-trained token classification models, and then aligned based on contextual embeddings.

- Repository for the alignment engine: [Aquilign](https://github.com/ProMeText/Aquilign)
- Alignment model: `LaBSE` (Language-Agnostic BERT Sentence Embedding)
- Languages: Old French, Old Spanish (Castilian), Old Italian

## 🔍 Visualization

Example of multilingual alignment table:
👉 [View aligned chapter](https://prometext.github.io/Multilingual_Aegidius/data/aegidius/results/multilingual_tables_ft/livre_1/partie_2/chapitre_1/final_result.html)

## 🗂️ Structure

- `data/`: source XMLs and aligned outputs
- `json/`: structured export (training data or evaluation sets)
- `README.md`: documentation (you are here)

- ## Citation

Gille Levenson, M., Ing, L., & Camps, J.-B. (2024). Textual Transmission without Borders: Multiple Multilingual Alignment and Stemmatology of the ``Lancelot en prose’’ (Medieval French, Castilian, Italian). In W. Haverals, M. Koolen, & L. Thompson (Eds.), Proceedings of the Computational Humanities   Research Conference 2024 (Vol. 3834, pp. 65–92). CEUR. https://ceur-ws.org/Vol-3834/#paper104


```
@inproceedings{gillelevenson_TextualTransmissionBorders_2024a,
  title = {Textual {{Transmission}} without {{Borders}}: {{Multiple Multilingual Alignment}} and {{Stemmatology}} of the ``{{Lancelot}} En Prose'' ({{Medieval French}}, {{Castilian}}, {{Italian}})},
  shorttitle = {Textual {{Transmission}} without {{Borders}}},
  booktitle = {Proceedings of the {{Computational Humanities}}   {{Research Conference}} 2024},
  author = {Gille Levenson, Matthias and Ing, Lucence and Camps, Jean-Baptiste},
  editor = {Haverals, Wouter and Koolen, Marijn and Thompson, Laure},
  date = {2024},
  series = {{{CEUR Workshop Proceedings}}},
  volume = {3834},
  pages = {65--92},
  publisher = {CEUR},
  location = {Aarhus, Denmark},
  issn = {1613-0073},
  url = {https://ceur-ws.org/Vol-3834/#paper104},
  urldate = {2024-12-09},
  eventtitle = {Computational {{Humanities Research}} 2024},
  langid = {english},
  file = {/home/mgl/Bureau/Travail/Bibliotheque_zoteros/storage/CIH7IAHV/Levenson et al. - 2024 - Textual Transmission without Borders Multiple Multilingual Alignment and Stemmatology of the ``Lanc.pdf}
}


## 🔖 Citation

If you use the corpus or refer to the alignment, please cite:

