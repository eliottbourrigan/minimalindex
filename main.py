import logging
import argparse
from indexer import Indexer

# Parsing command-line arguments
parser = argparse.ArgumentParser(description="Minimal Indexer")
parser.add_argument("-f", "--file", help="Path to the JSON file containing the crawled webpages.", default="data/crawled_urls.json")
parser.add_argument("-m", "--model", help="Name of the SpaCy model to use.", default="fr_core_news_sm")
parser.add_argument("-o", "--output", help="Path to the output directory.", default="output")
parser.add_argument("-l", "--limit", help="Maximum number of webpages to index.", default=None, type=int)
args = parser.parse_args()

# Setting up the logger
open("output/logs.log", "w").close() # Clearing the log file
logging.basicConfig(
   level=logging.INFO, 
   format="%(asctime)s - %(levelname)s - %(message)s",
   filename="output/logs.log")

# Create instance of Indexer
indexer = Indexer(model=args.model, output_dir=args.output, limit=args.limit)

# Start indexing the webpages
indexer.index(args.file)
indexer.save_results()
logging.info(f"Done.")