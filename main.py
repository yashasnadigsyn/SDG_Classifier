import argparse
import scrape, summarize
from OneVsRest.one_vs_rest import predict_sdg

parser = argparse.ArgumentParser(description="A simple program to predict SGDs of a company")

parser.add_argument("path", help="Give the URL of a website or pitch PPT or youtube pitch URL")
parser.add_argument("--mode", type=str, default="URL", help="Three options: URL for website input, PPT for pitch PPT input, YT for youtube pitch input")

args = parser.parse_args()

if args.mode == "URL":
    text_content = scrape.scrape_content(args.path)
    summarized = summarize.summarize_content(text_content)
    predicted_sdgs = predict_sdg(summarized)
    print(predicted_sdgs)
