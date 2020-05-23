# cnn-ssp

Apply ideas from <a href="https://arxiv.org/pdf/1903.04254.pdf">[1]</a> and <a href="https://www.aaai.org/Conferences/AAAI/2017/PreliminaryPapers/14-XiaoH-14306.pdf">[2]</a> to product graph completion problem.

# Problem description

According to <a href="https://www.alibabacloud.com/blog/learn-how-a-knowledge-graph-can-improve-your-online-shopping-experience_595668">[3]</a>, knowledge graph backed recommender system has been proved to overcome challenges encountered by ecommerce platforms in providing customers with personalised experience. However, product graph is usally far from complete. Practioners are required to explore methods to continuously enrich the product knowledge base in an attempt to improve the completeness of the graph.

I propose to follow the setup in [1]:
* First, encode structured and unstructured textual features of products into embeddings,

* then, pass the embeddings as node semantics into ssp model as described in [2], and lastly

* perfrom the link/head/tail prediction.

# Roadmap

* Code implementation (in progress).
* Test implementation with Neo4j movielens graph dataset.


# Reference

[1] <a href="https://arxiv.org/pdf/1903.04254.pdf">Large Scale Product Categorization using Structured and Unstructured Attributes</a>

[2] <a href="https://www.aaai.org/Conferences/AAAI/2017/PreliminaryPapers/14-XiaoH-14306.pdf">SSP: Semantic Space Projection for Knowledge Graph Embedding with Text Descriptions</a>

[3] <a href="https://www.alibabacloud.com/blog/learn-how-a-knowledge-graph-can-improve-your-online-shopping-experience_595668">Learn How a Knowledge Graph Can Improve Your Online Shopping Experience</a>