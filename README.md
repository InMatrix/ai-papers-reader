# AI Papers Reader
AI Papers Reader is an AI agent that brings you weekly digests of latest AI papers, customizable to topics you care about. Check out the published digests at https://ai-papers-reader.taodong.net/.

<img alt="a robot reading papers and taking notes" src="https://github.com/user-attachments/assets/faf07dd6-2196-4070-8680-c22fafa65823" width="300">

# Implementation

AI Papers Reader is built with the following building blocks:

* Hugging Face's [Daily Papers API](https://huggingface.co/api/daily_papers): It's used to retrieve the metadata of recently published AI papers.
* Google Gemini or DeepSeek: The selected LLM processes paper metadata, identifies papers relevant to the topics in [the prompt](https://github.com/InMatrix/ai-papers-reader/blob/main/prompts/recommend_papers.txt), and summarizes recommended papers.
* Github Actions: [A workflow](https://github.com/InMatrix/ai-papers-reader/blob/main/.github/workflows/fetch_generate_publish.yml) runs automatically on Fridays to retrieve the latest paper metadata and use the AI model to generate a new digest. The digests are saved in the [docs](https://github.com/InMatrix/ai-papers-reader/tree/main/docs) folder as markdown files.
* Netlify: The markdown files are then deployed to a static website using [Netlify](https://www.netlify.com/).

# Customizing Agent Behavior

The default set of topics AI Papers Reader currently uses to identify relevant papers is based on my research interests. You can customize it by forking the repo and editing [the prompt template](https://github.com/InMatrix/ai-papers-reader/blob/main/prompts/recommend_papers.txt).

Gemini remains the default provider:

```bash
export GOOGLE_API_KEY=your_key_here
python src/generate_report.py
```

To use DeepSeek, install the dependencies and select the provider. `deepseek-v4-flash` is the default DeepSeek model; `LLM_MODEL` or `--model` can select another available model.

```bash
pip install -r requirements.txt
export LLM_PROVIDER=deepseek
export DEEPSEEK_API_KEY=your_key_here
export LLM_MODEL=deepseek-v4-flash  # optional
python src/generate_report.py
```

The equivalent CLI form is `python src/generate_report.py --provider deepseek --model deepseek-v4-pro`. DeepSeek PDF summarization extracts text locally, so scanned PDFs without a text layer are not supported.

For GitHub Actions, set the repository variable `LLM_PROVIDER` to `deepseek`, optionally set `LLM_MODEL`, and add the `DEEPSEEK_API_KEY` repository secret.
