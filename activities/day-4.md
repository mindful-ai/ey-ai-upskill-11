### 4.1 RAG Capstone [15]

##### Part 1

- Ref: 16-rag-capstone\rag-app-v1.11\prompts.md
- Generate the server.py using the prompt using ChatGPT/Copilot/Gemini

------------------------------------------------------------------------
11:30 - 11:50 Break
11:50 - 12:05 Exercise 4.1.1
------------------------------------------------------------------------

##### Part 2

- Ref: 16-rag-capstone\rag-app-v1.11\prompts.md
- Generate the ui.py using the prompt using ChatGPT/Copilot/Gemini
  
------------------------------------------------------------------------
12:50 - 1:00 Exercise 4.1.2
------------------------------------------------------------------------

### 4.2 Capstone Project - Part 1

#### Phase 1

Pinecone setup

- https://www.pinecone.io/product/
- Sign-up
- Create an index in Database section
- Generate an API key in the Overview section

------------------------------------------------------------------------
1:30 - 2:15 Lunch Break
2:15 - 2:30 Exercise 4.2.1
------------------------------------------------------------------------

Document Store setup

- Access Documents Stores
- Choose PDF document loader
- Select the pdf file to upload
- Select Recursive Character Text Splitter with 1000 size with a 20% overlap
- Preview Chunks
- Select process

Upserting Chunks

- Select the Embeddings
  - API Key (OpenAI API Key)
  - Embedding function
- Select the Vector Store
  - API Key (Pinecone API Key)
  - Index Name (consider this as the main database unit)
  - Namespace (consdider this as a separate table in the index)
- Save the configuration
- Upsert
- Wait for a minute
- Test retrieval
- Observe the index and namespace in pinecone

#### Phase 2

Building the System

- Ref: 17-capstone-part-1\02-complete-project-new-version.png
- Test with sample queries
  - Ref: 16-rag-capstone\cis-basic\sample-queries\test-queries
  
------------------------------------------------------------------------
4:20 - 4:40 Tea Break
4:40 - 5:00 Set up the complete Agentic RAG system and test (4.2.2)
------------------------------------------------------------------------