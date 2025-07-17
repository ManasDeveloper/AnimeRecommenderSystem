from src.vectorstore import VectorStoreBuilder 
from config.config import GROQ_API_KEY, MODEL_NAME
from src.reccomender import AnimeRecommender
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__) 

class AnimeReccomendationPipeline:
    def __init__(self,persist_dir:str = "chroma_db"):
        
        try : 
            logger.info("Initializing Anime Recommendation Pipeline")

            vector_build = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)

            retriever = vector_build.load_vectorstre().as_retriever()

            self.recommender = AnimeRecommender(
                retriever=retriever,
                api_key=GROQ_API_KEY,
                model_name=MODEL_NAME
            )

            logger.info("Anime Recommendation Pipeline initialized successfully")
        except Exception as e:
            logger.error(f"Error initializing Anime Recommendation Pipeline: {str(e)}")
            raise CustomException("Failed to initialize Anime Recommendation Pipeline", e)
        
    def recommend(self, query: str):
        """
        Get anime recommendations based on the user's query.
        
        Args:
            query (str): The user's query for anime recommendations.
        
        Returns:
            dict: A dictionary containing the answer and source documents.
        """
        try :
            logger.info(f"Recieved a query : {query}")
            recommendatiom = self.recommender.get_recommendation(query)
            logger.info("Recommendation generated successfully")
            return recommendatiom
        except Exception as e:
            logger.error(f"Error generating recommendation: {str(e)}")
            raise CustomException("Failed to generate recommendation", e)