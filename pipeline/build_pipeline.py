from src.dataloader import AnimeDataLoader 
from src.vectorstore import VectorStoreBuilder 
from dotenv import load_dotenv
from utils.logger import get_logger 
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__) 


# this will be used to create the vectorstore from the anime data
def main():
    try:
        logger.info("Starting Anime Data Pipeline")

        loader = AnimeDataLoader("data/anime_with_synopsis.csv","data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        logger.info(f"Data loaded and processed successfully. Processed file saved at {processed_csv}")

        vector_builder = VectorStoreBuilder(
            csv_path=processed_csv,
            persist_dir="chroma_db"
        )

        vector_builder.build_and_save_vectorstore()

        logger.info("Vectorstore built and saved successfully")
        logger.info("Pipeline completed successfully")
    except Exception as e:
        logger.error(f"Error in Anime Data Pipeline: {str(e)}")
        raise CustomException("Failed to run Anime Data Pipeline", e)
    
if __name__ == "__main__":
    main()