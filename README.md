# AI Papers Reader
AI Papers Reader is an AI agent that brings you weekly digests of latest AI papers, customizable to topics you care about. Check out the published digests at https://ai-papers-reader.taodong.net/.

<img alt="a robot reading papers and taking notes" src="https://github.com/user-attachments/assets/faf07dd6-2196-4070-8680-c22fafa65823" width="300">

# Implementation

AI Papers Reader is built with the following building blocks:

* Hugging Face's [Daily Papers API](https://huggingface.co/api/daily_papers): It's used to retrieve the metadata of recently published AI papers.
* [Gemini 2.0 Flash](https://deepmind.google/technologies/gemini/flash/): It's the LLM used to process the paper metadata and identify those that are most relevant to a set of topics specified in [the prompt](https://github.com/InMatrix/ai-papers-reader/blob/main/prompts/recommend_papers.txt#L8-L50). The LLM is also used for summarizing recommended papers.
* Github Actions: [A workflow](https://github.com/InMatrix/ai-papers-reader/blob/main/.github/workflows/fetch_generate_publish.yml) runs automatically on Fridays to retrieve the latest paper metadata and use the AI model to generate a new digest. The digests are saved in the [docs](https://github.com/InMatrix/ai-papers-reader/tree/main/docs) folder as markdown files.
* Netlify: The markdown files are then deployed to a static website using [Netlify](https://www.netlify.com/).

# Customizing Agent Behavior

The default set of topics AI Papers Reader currently use to identify relevant papers are based on my research interest. You can customize them by forking the repo and edit [the prompt template](https://github.com/InMatrix/ai-papers-reader/blob/main/prompts/recommend_papers.txt) to your liking. To generate digests from your own fork of the repo, you will need to supply an API key for Gemini models. You can obtain one for free at http://aistudio.google.com.    
