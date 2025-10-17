# Q-Learning on Taxi-v3 Environment
### CSCN8020 – Reinforcement Learning Programming  
**Author:** Adhitya Kondeti  
**Instructor:** Prof. David Espinosa Carrillo  
**Date:** October 2025  

---

##  Overview
This project implements a **Q-Learning algorithm** to train a taxi agent in the **Taxi-v3** environment from OpenAI Gymnasium.  
The taxi learns to pick up passengers and drop them off efficiently while minimizing steps and maximizing rewards.

---

##  Key Features
- Implementation of **Q-Learning** with Bellman update rule  
- **ε-greedy policy** for exploration and exploitation  
- Visualization using **Gymnasium’s human render mode**  
- Automatic saving and loading of trained **Q-table**  
- Reward and steps tracking across episodes  

---

##  Installation
Clone this repository and install the dependencies:

```bash
git clone https://github.com/akondeti7046/Reinforcement-Learning-Programming--assignment-2.git
cd Reinforcement-Learning-Programming--assignment-2
pip install -r requirements.txt

