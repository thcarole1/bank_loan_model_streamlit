# bank_loan_model_streamlit:

# Explanation of the purpose of this app
st.markdown(
    """
    <h1>Bank loan prediction </h1>
    <h2> The big picture </h2>
    This case is about a bank (<b>Thera Bank</b>) which has a growing customer base. <br>
    Majority of these customers are <b>liability customers</b> (depositors) with varying size of deposits.
    The number of customers who are also borrowers (asset customers) is quite small, and <b>the bank is interested in expanding this base rapidly to bring in more loan business and in the process, earn more through the interest on loans</b>. <br>
    In particular, the management wants to <b>explore ways of converting its liability customers to personal loan customers (while retaining them as depositors)</b>. <br>

    A campaign that the bank ran last year for liability customers showed **a healthy conversion rate of over 9% success**. <br>
    This has encouraged the retail marketing department to devise campaigns to better target marketing to increase the success ratio with a minimal budget.<br><br>

    <h2> Framing the problem </h2>
    <h3> What is the business objective is?</h3>
    The department wants to build a model that will <b>help them identify the potential customers who have a higher probability of purchasing the loan</b>.<br>
    <b>This will increase the success ratio while at the same time reduce the cost of the campaign</b>.<br><br>

    <b>Impact of errors</b>: <br>
    - False negatives (**eligible customers rejected**) can lead to **revenue losses** for the bank.<br>
    - False positives (**ineligible customers accepted**) can lead to **payment default risks**.<br>

    <h3> What is the type of learning ?</h3>
    With the gathered information, we are ready to design our system.<br>
    - This is a <b>supervised learning task</b> because the model can train on labeled examples (customers who actually purchased a loan). <br>
    - It’s a <b>classification task</b> since the goal is to predict the likelihood of customers to purchase a loan or not. <br><br>

    <h2> Selecting a performance measure </h2>
    The next step is to choose a performance measure: <br>
    - <b>Recall</b> may be favored if the goal is <b>to minimize false negatives</b>, <br>
    - or <b>F1-score</b> to <b>balance precision and recall</b>.<br><br>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """ We will compute : <br>
    - the F1 score : """,
    unsafe_allow_html=True
)
st.latex(r'''
            F_1  = \frac{2}{\frac{1}{precision}+ \frac{1}{recall}}
            = 2 \times \frac{precision \times recall}{precision + recall}
            = \frac{TP}{TP +  \frac{FN + FP}{2}}
         ''')

st.markdown(
    """ - the recall : """,
    unsafe_allow_html=True
)

st.latex(r'''
        recall  = \frac{TP}{TP + FN}
         ''')

st.markdown(
    """ - the precision : """,
    unsafe_allow_html=True
)
st.latex(r'''
        precision  = \frac{TP}{TP + FP}
         ''')

st.markdown(
    """ with **TP** : True Positives and **FN** : False Negatives""",
    unsafe_allow_html=True
)
st.markdown(
    """ <h1> Let's go ! </h1>""",
    unsafe_allow_html=True
)
