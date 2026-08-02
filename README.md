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

Provider and model selection live in the committed [config.yaml](config.yaml):

```yaml
provider: deepseek
model: deepseek-v4-flash
```

Store credentials locally in an ignored `.env` file. Start from `.env.example`:

```bash
cp .env.example .env
# Edit .env and set GOOGLE_API_KEY and/or DEEPSEEK_API_KEY.
```

Gemini remains the default provider. To use DeepSeek, edit `config.yaml` as shown above:

```bash
pip install -r requirements.txt
python src/generate_report.py
```

CLI `--provider` and `--model` flags remain available as one-off overrides. DeepSeek PDF summarization extracts text locally, so scanned PDFs without a text layer are not supported.

PDF handling is bounded for reliability: DeepSeek uses the first 12 pages, while Gemini receives the full PDF up to 20 MiB and a first-12-page PDF above that threshold. Adjust `llm_timeout_seconds` and the `pdf` limits in `config.yaml` to change this behavior.

For GitHub Actions, commit the desired `config.yaml` selection and add the matching API key as a repository secret (`GOOGLE_API_KEY` or `DEEPSEEK_API_KEY`).
