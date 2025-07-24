

![banner](img/github_banner_fullscene_1600x350.png)


> *An aligned multilingual corpus of the* Lancelot en prose, *processed with [Aquilign](https://github.com/ProMeText/Aquilign).*  
> This repository hosts the training data and aligned outputs for a multilingual medieval tradition.

## 📚 Description

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

## 🔖 Citation

If you use the corpus or refer to the alignment, please cite:

