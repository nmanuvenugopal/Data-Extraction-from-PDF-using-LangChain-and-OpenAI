# Data-Extraction-from-PDF-using-LangChain-and-OpenAI


I have used LangChain for this operqtion. LangChain is simple and easy to carry out various operation due to extensive functionalities avalibale.
For extracting the data from the PDF I have used the **PyMuPDFLoader** library.
I have done the following task in this scenario:
1. Extract the texts from the PDF by using PyMuPDFLoader.
2. Split the tesxt using RecursiveCharacterTextSplitter.
3. After splitting the text I have embedded the texts using the OpenAIEmbedding model.
4. Once everything is embedded, FAISS is used for storing and indexing purposes.
5. ChatOpenAI model is used query and retrive the correct information from vector database based on user query.
6. For retrieval puposes, I have used the RetrievalQA of LangChain chain.


# Following are the output from GPT3.5 Turbo and GPT4o models

**Enter the query: What is the name of the document?**
The output from **GPT3.5** turbo model is: The name of the document is "Microsoft Partner Agreement."
The output from **GPT4o model** is The name of the document is the "Microsoft Partner Agreement."

**Enter the query: Please provide the summary of the document?**
The output from **GPT3.5 turbo model** is: The document is a Microsoft Partner Agreement that outlines the terms and conditions for partnership. It includes provisions related to audits, compliance with the Microsoft Partner Code of Conduct, handling of intellectual property claims, and the responsibilities of both Microsoft and the partner company in case of legal issues.

The output from **GPT4o model** is The document appears to be an excerpt from the Microsoft Partner Agreement, which outlines various obligations and procedures for companies partnering with Microsoft. Key points include:

1. **Audit Access**: Companies must provide reasonable access to auditors, allow copying of records, and make relevant employees available during audits. Microsoft will provide a summary of audit findings upon request.

2. **Compliance**: Companies must comply with the Microsoft Partner Code of Conduct.

3. **Claims and Notifications**: If a claim arises, the party must promptly notify the other in writing, specifying the nature and relief sought. Failure to do so promptly may affect the handling of the claim.

4. **Intellectual Property Claims**: Microsoft may take additional actions to mitigate or resolve intellectual property claims, such as procuring rights or licenses.

The document emphasizes compliance, cooperation during audits, and proper handling of claims and intellectual property issues.


**Enter the query: What are the Compliance items spoken in this document?**
The output from **GPT3.5 turbo model** is: The compliance items mentioned in the document include conducting business activities in full compliance with all laws, complying with laws that apply to the other party's Marks or to the use, transfer, providing information, assistance, and cooperation necessary to comply with laws, and conducting business activities with integrity.

The output from ** GPT4o model** is The document outlines several compliance items:

1. **Compliance with Laws**: Each party must conduct its business activities in full compliance with all applicable laws, including those related to the other party’s Marks or the use, transfer, and distribution of products.

2. **Microsoft Partner Code of Conduct**: The company must comply with the Microsoft Partner Code of Conduct.

3. **Truthful Communications**: Ensure that all communications to customers and the other party are complete, truthful, accurate, not misleading, and include any required disclosures.

4. **Non-Retaliation**: Refrain from retaliating against anyone who has, in good faith, reported a possible violation of the commitments.

5. **Business Conduct Training**: Microsoft will provide regular training on anti-corruption laws and business integrity.

6. **Information and Cooperation**: Timely provide information, assistance, and cooperation as necessary to comply with laws or to register, renew registration, or report to any governmental agency or certification body that regulates or certifies the use, licensing, or distribution of products.

7. **Business Integrity**: Conduct business activities with integrity.
**Enter the query: exit**


 ## Refernce 

 https://github.com/thoqbk/pdf-query/blob/master/chat.py
