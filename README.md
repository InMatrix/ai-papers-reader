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

Provider and model selection live in the committed [config.yaml](config.yaml). The supported provider defaults are:

| Provider | Default model | API key |
| --- | --- | --- |
| Gemini | `gemini-flash-latest` | `GOOGLE_API_KEY` |
| DeepSeek | `deepseek-v4-flash` | `DEEPSEEK_API_KEY` |

The current committed selection is DeepSeek:

```yaml
provider: deepseek
model: deepseek-v4-flash
```

To use Gemini instead, change those two values to:

```yaml
provider: gemini
model: gemini-flash-latest
```

Store credentials locally in an ignored `.env` file. Start from `.env.example`:

```bash
cp .env.example .env
# Edit .env and set GOOGLE_API_KEY and/or DEEPSEEK_API_KEY.
```

The CLI `--provider` and `--model` flags remain available as one-off overrides. If no model override is supplied, the configured model is used when it matches the selected provider; otherwise the provider default from the table above is used.

```bash
pip install -r requirements.txt
python src/generate_report.py
```

DeepSeek PDF summarization extracts text locally, so scanned PDFs without a text layer are not supported.

PDF handling is bounded for reliability: both providers receive the complete file when it is under the configured 15 MiB default. For oversized PDFs, text extraction/PDF upload first tries the complete body before a configurable References/Bibliography heading, then drops trailing pages one at a time from the configured page limit until the generated PDF fits. Downloads stream in chunks and retry transient network/HTTP failures with exponential backoff; tune the PDF timeout/retry settings in `config.yaml` as needed. Set `pdf.stop_at_references` to `false` or customize `pdf.references_headings` when needed.

For GitHub Actions, commit the desired `config.yaml` selection and add the matching API key as a repository secret (`GOOGLE_API_KEY` or `DEEPSEEK_API_KEY`).
