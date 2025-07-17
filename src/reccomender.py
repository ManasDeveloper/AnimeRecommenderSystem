from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_groq import ChatGroq 
from src.prompt_template import get_anime_prompt


class AnimeRecommender:
    def __init__(self,retriever,api_key:str,model_name:str):
        self.llm = ChatGroq(api_key=api_key, model=model_name,temperature=0)
        self.prompt = get_anime_prompt()

        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever,
            return_source_documents=True,
            chain_type_kwargs={"prompt": self.prompt}
        )

    def get_recommendation(self, query: str):
        """
        Get anime recommendations based on the query.
        
        Args:
            query (str): The user's query for anime recommendations.
        
        Returns:
            dict: A dictionary containing the answer and source documents.
        """
        response = self.qa_chain({"query": query})
        return response['result']