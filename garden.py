{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyO8Jlc0rgL8OVxvDIs0Q4TH",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/vimbairamwi/git-task/blob/main/garden.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "uaB05ACnWOmO",
        "outputId": "8885c813-e364-4b9b-98b7-85f38964837a"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: spacy in /usr/local/lib/python3.12/dist-packages (3.8.14)\n",
            "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in /usr/local/lib/python3.12/dist-packages (from spacy) (3.0.12)\n",
            "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (1.0.5)\n",
            "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (1.0.15)\n",
            "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.0.13)\n",
            "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in /usr/local/lib/python3.12/dist-packages (from spacy) (3.0.13)\n",
            "Requirement already satisfied: thinc<8.4.0,>=8.3.12 in /usr/local/lib/python3.12/dist-packages (from spacy) (8.3.13)\n",
            "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in /usr/local/lib/python3.12/dist-packages (from spacy) (1.1.3)\n",
            "Requirement already satisfied: srsly<3.0.0,>=2.5.3 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.5.3)\n",
            "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.0.10)\n",
            "Requirement already satisfied: weasel<2.0.0,>=1.0.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (1.0.0)\n",
            "Requirement already satisfied: confection<2.0.0,>=1.3.2 in /usr/local/lib/python3.12/dist-packages (from spacy) (1.3.3)\n",
            "Requirement already satisfied: typer<1.0.0,>=0.3.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (0.26.8)\n",
            "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (4.67.3)\n",
            "Requirement already satisfied: numpy>=1.19.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.0.2)\n",
            "Requirement already satisfied: requests<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.32.4)\n",
            "Requirement already satisfied: pydantic<3.0.0,>=2.0.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (2.13.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.12/dist-packages (from spacy) (3.1.6)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.12/dist-packages (from spacy) (75.2.0)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.12/dist-packages (from spacy) (26.2)\n",
            "Requirement already satisfied: annotated-types>=0.6.0 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.0.0->spacy) (0.7.0)\n",
            "Requirement already satisfied: pydantic-core==2.46.4 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.0.0->spacy) (2.46.4)\n",
            "Requirement already satisfied: typing-extensions>=4.14.1 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.0.0->spacy) (4.16.0)\n",
            "Requirement already satisfied: typing-inspection>=0.4.2 in /usr/local/lib/python3.12/dist-packages (from pydantic<3.0.0,>=2.0.0->spacy) (0.4.2)\n",
            "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.4.9)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (3.18)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2.5.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.12/dist-packages (from requests<3.0.0,>=2.13.0->spacy) (2026.6.17)\n",
            "Requirement already satisfied: blis<1.4.0,>=1.3.0 in /usr/local/lib/python3.12/dist-packages (from thinc<8.4.0,>=8.3.12->spacy) (1.3.3)\n",
            "Requirement already satisfied: shellingham>=1.3.0 in /usr/local/lib/python3.12/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (1.5.4)\n",
            "Requirement already satisfied: rich>=13.8.0 in /usr/local/lib/python3.12/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (13.9.4)\n",
            "Requirement already satisfied: annotated-doc>=0.0.2 in /usr/local/lib/python3.12/dist-packages (from typer<1.0.0,>=0.3.0->spacy) (0.0.4)\n",
            "Requirement already satisfied: cloudpathlib>=0.7.0 in /usr/local/lib/python3.12/dist-packages (from weasel<2.0.0,>=1.0.0->spacy) (0.24.0)\n",
            "Requirement already satisfied: smart-open>=5.2.1 in /usr/local/lib/python3.12/dist-packages (from weasel<2.0.0,>=1.0.0->spacy) (8.0.0)\n",
            "Requirement already satisfied: httpx>=0.24.0 in /usr/local/lib/python3.12/dist-packages (from weasel<2.0.0,>=1.0.0->spacy) (0.28.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.12/dist-packages (from jinja2->spacy) (3.0.3)\n",
            "Requirement already satisfied: anyio in /usr/local/lib/python3.12/dist-packages (from httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy) (4.14.2)\n",
            "Requirement already satisfied: httpcore==1.* in /usr/local/lib/python3.12/dist-packages (from httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy) (1.0.9)\n",
            "Requirement already satisfied: h11>=0.16 in /usr/local/lib/python3.12/dist-packages (from httpcore==1.*->httpx>=0.24.0->weasel<2.0.0,>=1.0.0->spacy) (0.16.0)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.12/dist-packages (from rich>=13.8.0->typer<1.0.0,>=0.3.0->spacy) (4.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.12/dist-packages (from rich>=13.8.0->typer<1.0.0,>=0.3.0->spacy) (2.20.0)\n",
            "Requirement already satisfied: wrapt in /usr/local/lib/python3.12/dist-packages (from smart-open>=5.2.1->weasel<2.0.0,>=1.0.0->spacy) (2.2.2)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.12/dist-packages (from markdown-it-py>=2.2.0->rich>=13.8.0->typer<1.0.0,>=0.3.0->spacy) (0.1.2)\n",
            "Collecting en-core-web-sm==3.8.0\n",
            "  Downloading https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.8.0/en_core_web_sm-3.8.0-py3-none-any.whl (12.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m12.8/12.8 MB\u001b[0m \u001b[31m96.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25h\u001b[38;5;2m✔ Download and installation successful\u001b[0m\n",
            "You can now load the package via spacy.load('en_core_web_sm')\n",
            "\u001b[38;5;3m⚠ Restart to reload dependencies\u001b[0m\n",
            "If you are in a Jupyter or Colab notebook, you may need to restart Python in\n",
            "order to load all the package's dependencies. You can do this by selecting the\n",
            "'Restart kernel' or 'Restart runtime' option.\n"
          ]
        }
      ],
      "source": [
        "!pip install spacy\n",
        "!python -m spacy download en_core_web_sm"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import spacy\n",
        "\n",
        "# Load English language model\n",
        "nlp = spacy.load(\"en_core_web_sm\")"
      ],
      "metadata": {
        "id": "KWLKfwYlXxkq"
      },
      "execution_count": 3,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# List of garden path sentences\n",
        "gardenpathSentences = [\n",
        "\n",
        "    # My chosen garden path sentences\n",
        "    \"The old man the boats.\",\n",
        "    \"The horse raced past the barn fell.\",\n",
        "\n",
        "    # Sentences required by the task\n",
        "    \"Mary gave the child a Band-Aid.\",\n",
        "    \"That Jill is never here hurts.\",\n",
        "    \"The cotton clothing is made of grows in Mississippi.\"\n",
        "]"
      ],
      "metadata": {
        "id": "v1auanNOYO8Y"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Process each sentence\n",
        "for sentence in gardenpathSentences:\n",
        "\n",
        "    print(\"\\n\" + \"=\"*60)\n",
        "    print(\"Sentence:\")\n",
        "    print(sentence)\n",
        "\n",
        "    doc = nlp(sentence)\n",
        "\n",
        "    # Tokenisation\n",
        "    print(\"\\nTokens:\")\n",
        "    for token in doc:\n",
        "        print(token.text)\n",
        "\n",
        "    # Named Entity Recognition\n",
        "    print(\"\\nNamed Entities:\")\n",
        "\n",
        "    if len(doc.ents) == 0:\n",
        "        print(\"No named entities found\")\n",
        "\n",
        "    for ent in doc.ents:\n",
        "        print(f\"{ent.text} --> {ent.label_}\")\n",
        "        print(f\"Explanation: {spacy.explain(ent.label_)}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "egCHkmnWYWJM",
        "outputId": "495f3721-1c3c-4d45-cd2c-20bffcffffe1"
      },
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\n",
            "============================================================\n",
            "Sentence:\n",
            "The old man the boats.\n",
            "\n",
            "Tokens:\n",
            "The\n",
            "old\n",
            "man\n",
            "the\n",
            "boats\n",
            ".\n",
            "\n",
            "Named Entities:\n",
            "No named entities found\n",
            "\n",
            "============================================================\n",
            "Sentence:\n",
            "The horse raced past the barn fell.\n",
            "\n",
            "Tokens:\n",
            "The\n",
            "horse\n",
            "raced\n",
            "past\n",
            "the\n",
            "barn\n",
            "fell\n",
            ".\n",
            "\n",
            "Named Entities:\n",
            "No named entities found\n",
            "\n",
            "============================================================\n",
            "Sentence:\n",
            "Mary gave the child a Band-Aid.\n",
            "\n",
            "Tokens:\n",
            "Mary\n",
            "gave\n",
            "the\n",
            "child\n",
            "a\n",
            "Band\n",
            "-\n",
            "Aid\n",
            ".\n",
            "\n",
            "Named Entities:\n",
            "Mary --> PERSON\n",
            "Explanation: People, including fictional\n",
            "\n",
            "============================================================\n",
            "Sentence:\n",
            "That Jill is never here hurts.\n",
            "\n",
            "Tokens:\n",
            "That\n",
            "Jill\n",
            "is\n",
            "never\n",
            "here\n",
            "hurts\n",
            ".\n",
            "\n",
            "Named Entities:\n",
            "Jill --> PERSON\n",
            "Explanation: People, including fictional\n",
            "\n",
            "============================================================\n",
            "Sentence:\n",
            "The cotton clothing is made of grows in Mississippi.\n",
            "\n",
            "Tokens:\n",
            "The\n",
            "cotton\n",
            "clothing\n",
            "is\n",
            "made\n",
            "of\n",
            "grows\n",
            "in\n",
            "Mississippi\n",
            ".\n",
            "\n",
            "Named Entities:\n",
            "Mississippi --> GPE\n",
            "Explanation: Countries, cities, states\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Entity 1:\n",
        "# PERSON\n",
        "# Explanation: People, including fictional characters.\n",
        "# This made sense because spaCy identified \"Mary\" and \"Jill\"\n",
        "# as people.\n",
        "\n",
        "# Entity 2:\n",
        "# GPE\n",
        "# Explanation: Countries, cities, states.\n",
        "# This made sense because \"Mississippi\" is a geographical\n",
        "# location and was correctly identified by spaCy."
      ],
      "metadata": {
        "id": "2SQqbnVsaS-B"
      }
    }
  ]
}