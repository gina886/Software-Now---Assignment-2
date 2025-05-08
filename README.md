# HIT137 - Group Assignment 2

## 📚 Overview

This repository contains the solution to HIT137 Group Assignment 2, worth 20% of the final mark. The assignment includes three main programming tasks involving text encryption/decryption, weather data analysis, and turtle graphics recursion.

> 📁 This repository is public and all group contributions are tracked here as per the submission guidelines.

---

## 📌 Submission Instructions

- A file named `github_link.txt` contains the link to this GitHub repository.
- All programming files and their respective output files are included.
- These files will be zipped and submitted to Learline as `assignment2.zip`.

---

## 🧠 Assignment Questions

### ✅ Question 1 - Text File Encryption

**Objective:**  
Read from `raw_text.txt`, encrypt the text using custom logic, write to `encrypted_text.txt`, and include functions to decrypt and verify correctness.

**Encryption Rules:**

- Takes two user inputs: `n` and `m`.

#### Rules:
- Lowercase letters:
  - `a-m`: shift **forward** by `n * m`
  - `n-z`: shift **backward** by `n + m`
- Uppercase letters:
  - `A-M`: shift **backward** by `n`
  - `N-Z`: shift **forward** by `m^2`
- All other characters (digits, symbols, etc.) remain **unchanged**.

#### Example

##### Input
- Enter value for n: 2
- Enter value for m: 3

----

##### Output

##### Contents of `raw_text.txt`:
The quick brown fox jumps over the lazy dog beneath the shady willows. The dog, startled from his peaceful afternoon nap, quickly rises and chases after the mischievous fox. Through vibrant meadows and past buzzing beehives they race, disturbing a flock of quails that scatter into the crisp autumn sky. The fox, quite pleased with his clever prank, dashes into his cozy underground den while the dog, now exhausted from the zealous pursuit, returns to his favorite spot under the whispering branches to resume his quiet slumber.

##### Contents of `encrypted_text.txt`:
Cnk lpoiq hmjri ljs ppskn jqkm onk rgut jjm hkikgon onk nngjt rorrjrn. Cnk jjm, nogmorkj lmjs non kkgiklpr glokmijji igk, lpoiqrt monkn gij ingnkn glokm onk soninokqjpn ljs. Cnmjpmn qohmgio skgjjrn gij kgno hpuuoim hkknoqkn onkt mgik, jonopmhoim g lrjiq jl lpgorn ongo nigookm oioj onk imonk gpopsi nqt. Cnk ljs, lpook krkgnkj roon non irkqkm kmgiq, jgnnkn oioj non ijut pijkmmmjpij jki rnork onk jjm, ijr ksngpnokj lmjs onk ukgrjpn kpmnpoo, mkopmin oj non lgqjmook nkjo pijkm onk rnonkkmoim hmgiinkn oj mknpsk non lpoko nrpshkm.

##### Contents of `decrypted_text.txt`:
The quick brown fox jumps over the lazy dog beneath the shady willows. The dog, startled from his peaceful afternoon nap, quickly rises and chases after the mischievous fox. Through vibrant meadows and past buzzing beehives they race, disturbing a flock of quails that scatter into the crisp autumn sky. The fox, quite pleased with his clever prank, dashes into his cozy underground den while the dog, now exhausted from the zealous pursuit, returns to his favorite spot under the whispering branches to resume his quiet slumber.

##### Result

- ✅ Decryption is correct!


### 📊 Question 2 - Weather Data Analysis

**Objective:**  
Analyze temperature data stored in multiple CSV files (one per year) inside the `temperatures/` folder.

#### Tasks:
- Calculate **average seasonal temperatures** and save to `average_temp.txt`.
- Identify the station(s) with the **largest temperature range** and save to `largest_temp_range_station.txt`.
- Find the **warmest and coolest station(s)** and save to `warmest_and_coolest_station.txt`.

### 🌳 Question 3 - Recursive Tree Pattern with Turtle

**Objective:**  
Draw a tree using recursive turtle graphics.

#### User Inputs:
- Left and Right Branch Angles
- Starting Branch Length
- Recursion Depth
- Branch Length Reduction Factor

#### Example:
- Left Angle: `20°`
- Right Angle: `25°`
- Start Length: `100 px`
- Depth: `5`
- Reduction Factor: `0.7`

#### Output:
![image](https://github.com/user-attachments/assets/0918da16-1dc2-4673-94c7-28ac8811033f)


---

## 👨‍💻 Contributors

- Anish Machamasi (anishmachamasi2262@gmail.com)
- Xiaoyu Wang
- Veli Oz

---

## 🛠️ Requirements

Make sure you have Python 3.x installed. To install required packages (if any), run:

```bash
pip install -r requirements.txt
```
