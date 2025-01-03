# Bank loan prediction
## The big picture
This case is about a bank (**Thera Bank**) which has a growing customer base. <br>
Majority of these customers are **liability customers** (depositors) with varying size of deposits.
The number of customers who are also borrowers (asset customers) is quite small, and **the bank is interested in expanding this base rapidly to bring in more loan business and in the process, earn more through the interest on loans**. <br>
In particular, the management wants to **explore ways of converting its liability customers to personal loan customers (while retaining them as depositors)**. <br>

A campaign that the bank ran last year for liability customers showed **a healthy conversion rate of over 9% success**. <br>
This has encouraged the retail marketing department to devise campaigns to better target marketing to increase the success ratio with a minimal budget.<br><br>

## Framing the problem
### What is the business objective is?
The department wants to build a model that will **help them identify the potential customers who have a higher probability of purchasing the loan**.<br>
**This will increase the success ratio while at the same time reduce the cost of the campaign**.<br><br>

**Impact of errors**: <br>
- False negatives (**eligible customers rejected**) can lead to **revenue losses** for the bank.<br>
- False positives (**ineligible customers accepted**) can lead to **payment default risks**.<br>

### What is the type of learning ?
With the gathered information, we are ready to design our system.<br>
- This is a **supervised learning task** because the model can train on labeled examples (customers who actually purchased a loan). <br>
- It’s a **classification task** since the goal is to predict the likelihood of customers to purchase a loan or not. <br><br>

## Selecting a performance measure
The next step is to choose a performance measure: <br>
- **Recall** may be favored if the goal is **to minimize false negatives**, <br>
- or **F1-score** to **balance precision and recall**.<br><br>

We will compute : <br>
    - the F1 score : <br><br>
    $$F_1  = \frac{2}{\frac{1}{precision}+ \frac{1}{recall}} = 2 \times \frac{precision \times recall}{precision + recall} = \frac{TP}{TP +  \frac{FN + FP}{2}}$$ <br><br>
    - the recall : <br><br>
      $$recall  = \frac{TP}{TP + FN}$$ <br><br>
    - the precision : <br><br>
      $$precision  = \frac{TP}{TP + FP}$$<br><br>

with **TP** : True Positives and **FN** : False Negatives<br><br>

# Let's go !
