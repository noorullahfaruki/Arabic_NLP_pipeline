# Arabic_NLP_pipeline
An open-source text cleaning and normalization pipeline for Arabic NLP
# Arabic NLP Preprocessing & Morphological Pipeline

## The Problem: The MRL Bottleneck
Standard NLP tokenization architectures are inherently biased toward Western languages. They rely heavily on whitespace to define words. This approach completely fails when applied to Morphologically Rich Languages (MRLs) like Arabic, where prefixes (like conjunctions and prepositions) and suffixes attach directly to the root word (e.g., "وبالسيارة"). 

When standard Large Language Models process these attached forms, they hallucinate vocabulary, treating the attached form as a completely separate entity from its core root. This results in massive memory waste and degraded contextual understanding.

## The Solution
This project implements an automated, linguistically aware preprocessing pipeline designed to handle the complex morphology of Modern Standard Arabic (MSA).

### Pipeline Architecture:
1. **Noise Reduction:** Custom Regex implementations surgically strip non-Arabic alphanumeric characters and foreign punctuation without damaging Arabic encoding.
2. **Unicode Cleansing:** Automated identification and stripping of complex Unicode emojis.
3. **Morphological Tokenization:** Integrates the **CAMeL Tools** library (developed by NYU Abu Dhabi) using Maximum Likelihood Estimation (MLE) disambiguation. It utilizes the `calima-msa-r13` database and the `d3tok` scheme to mathematically isolate grammatical particles (conjunctions, prepositions, definite articles) from core nouns.

### Example Output:
**Raw Input:** `مرحبا بك!!! 123 في الورشة 😂`
**Cleaned & Tokenized Output:** `['مرحبا', 'بك', 'في', 'ال+_ورشة']`

By splitting `الورشة` into its definite article `ال` and the core noun `ورشة`, downstream AI models can accurately map the root vocabulary, drastically improving mathematical efficiency for training sets.

## Technical Stack
* **Python 3**
* **Pandas** (Data Handling)
* **Regex / re** (Pattern Matching)
* **Emoji** (Unicode Cleansing)
* **CAMeL Tools** (Morphological Disambiguation & Tokenization)
