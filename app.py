"""
Aparna — 25-Minute Showcase Speaking Guide
Mobile-friendly Streamlit reader for practice and presentation.
"""

import streamlit as st

st.set_page_config(
    page_title="Aparna — 25-Min Speaking Guide",
    page_icon="🎤",
    layout="centered",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
      .block-container {
        padding-top: 1.2rem;
        padding-bottom: 3rem;
        max-width: 720px;
      }
      h1, h2, h3 {
        line-height: 1.25;
      }
      .speak {
        background: #f7f4ef;
        border-left: 4px solid #1f6f5b;
        padding: 0.85rem 1rem;
        margin: 0.65rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 1.05rem;
        line-height: 1.55;
      }
      .onscreen {
        background: #eef3f8;
        border-left: 4px solid #2c5aa0;
        padding: 0.75rem 1rem;
        margin: 0.65rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 1rem;
        line-height: 1.5;
      }
      .meta {
        color: #444;
        font-size: 0.98rem;
        line-height: 1.5;
        margin: 0.4rem 0;
      }
      .priority {
        display: inline-block;
        background: #fff3cd;
        color: #664d03;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        margin-left: 0.35rem;
      }
      .secondary {
        display: inline-block;
        background: #e9ecef;
        color: #495057;
        font-size: 0.85rem;
        font-weight: 600;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        margin-left: 0.35rem;
      }
      .file-label {
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        background: #f1f3f5;
        padding: 0.1rem 0.35rem;
        border-radius: 4px;
        font-size: 0.95rem;
      }
      .section-time {
        color: #1f6f5b;
        font-weight: 600;
        font-size: 0.95rem;
      }
      .qa-q {
        background: #eef6f3;
        border-left: 4px solid #1f6f5b;
        padding: 0.85rem 1rem;
        margin: 0.85rem 0 0.35rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 1.05rem;
        line-height: 1.5;
        font-weight: 600;
      }
      .qa-a {
        background: #f7f4ef;
        border-left: 4px solid #8a6d3b;
        padding: 0.85rem 1rem;
        margin: 0.35rem 0 1rem 0;
        border-radius: 0 8px 8px 0;
        font-size: 1.05rem;
        line-height: 1.55;
      }
      @media (max-width: 640px) {
        .speak, .onscreen, .qa-q, .qa-a { font-size: 1.02rem; }
      }
    </style>
    """,
    unsafe_allow_html=True,
)


def speak(text: str) -> None:
    st.markdown(f'<div class="speak"><strong>Speak:</strong> {text}</div>', unsafe_allow_html=True)


def on_screen(text: str) -> None:
    st.markdown(f'<div class="onscreen"><strong>ON SCREEN:</strong> {text}</div>', unsafe_allow_html=True)


def meta(text: str) -> None:
    st.markdown(f'<p class="meta">{text}</p>', unsafe_allow_html=True)


def lines(label: str, priority=None) -> None:
    badge = ""
    if priority == "high":
        badge = '<span class="priority">★ HIGH PRIORITY</span>'
    elif priority == "secondary":
        badge = '<span class="secondary">○ SECONDARY</span>'
    st.markdown(
        f'<p class="meta"><strong>Exact lines:</strong> {label}{badge}</p>',
        unsafe_allow_html=True,
    )


def qa(question: str, answer: str) -> None:
    st.markdown(f'<div class="qa-q">{question}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="qa-a"><strong>A:</strong> {answer}</div>', unsafe_allow_html=True)


SECTIONS = [
    "Full guide (all sections)",
    "SECTION 1 — Introduction, role, and idea (0:00–2:00)",
    "SECTION 2 — Architecture and Azure (2:00–4:30)",
    "SECTION 3 — Homepage live walkthrough (4:30–10:30)",
    "SECTION 4 — Homepage code — Home.py (10:30–14:00)",
    "SECTION 5 — Voice Assistant live walkthrough (14:00–20:00)",
    "SECTION 6 — Voice + Azure + API code (20:00–23:30)",
    "SECTION 7 — Challenges (23:30–24:30)",
    "SECTION 8 — Future enhancements + closing (24:30–25:30)",
    "Q&A — 10 likely teacher questions",
]

st.sidebar.title("Jump to section")
choice = st.sidebar.radio("Sections", SECTIONS, label_visibility="collapsed")
st.sidebar.markdown("---")
st.sidebar.caption("Open this Streamlit link on your phone to read while practicing.")

st.title("Aparna — 25-Minute Showcase Speaking Guide")
st.caption("MediGuide Capstone · Full speaking script · Mobile-friendly reader")


def section_1() -> None:
    st.header("SECTION 1 — Introduction, my role, and the idea (0:00–2:00)")
    st.markdown('<p class="section-time">0:00–2:00</p>', unsafe_allow_html=True)

    on_screen("Teams screen share ON. Open live Home page.")
    speak(
        "Good morning Sir. Today I will present my individual contribution to our Capstone project, MediGuide — Clinical Knowledge and Patient Education Assistant."
    )
    speak(
        "MediGuide is a healthcare GenAI application that answers questions only from approved synthetic documents, using Azure OpenAI, FastAPI, Streamlit, and ChromaDB. The goal is safe, source-grounded assistance for clinical and patient-service teams."
    )
    meta("My role in the project: I owned three connected areas.")
    meta(
        "Product entry experience —that is the Homepage users see first when opening the hosted website."
    )
    meta(
        "Voice Assistant end-to-end — that is recording UI, Azure Whisper transcription (speech-to-text), and integration with the RAG answer pipeline."
    )
    meta(
        "Azure API configuration and FastAPI wiring — which had environment configuration, Azure OpenAI service layer, telemetry logging, application startup scripts, and the `/voice-ask` backend route."
    )
    meta("Files I implemented and pushed:")
    st.markdown(
        """
- `frontend/pages/Home.py`
- `frontend/pages/Speech_to_Text.py`
- `.env.example`
- `backend/app/config.py`
- `backend/app/main.py`
- `backend/app/services/azure_openai.py`
- `backend/app/services/telemetry.py`
- `scripts/start.sh`
- `scripts/test_azure.sh`
        """
    )
    speak(
        "How I came up with this idea is that While designing MediGuide, I noticed two practical gaps. First, users opening a multi-tool GenAI system can feel lost — so I designed a Homepage that explains the product, proves the backend is healthy, and guides them into each workspace. Second, in real clinic or support settings, staff often need hands-free access — so I designed Voice Assistant as speech input into the same grounded pipeline, not a separate unsafe chatbot. My unique contribution is connecting Azure configuration + API entry + Home gateway + Voice multimodal input into one experience."
    )
    speak(
        "Sir, my work sits in three areas. In the frontend pages folder, Home.py is the product gateway and Speech_to_Text.py is the Voice Assistant UI. Inside backend/app/services and main, Azure OpenAI and the /voice-ask route connect Whisper transcription into the same grounded RAG path. And supporting files such as telemetry and config, plus start.sh, keep secrets, logging, and local startup organized."
    )


def section_2() -> None:
    st.header("SECTION 2 — Architecture and Azure (2:00–4:30)")
    st.markdown('<p class="section-time">2:00–4:30</p>', unsafe_allow_html=True)

    on_screen(
        "Briefly show README architecture if available, or stay on Home ‘How it works’. Optional: Azure deployments with keys hidden."
    )
    speak("At a high level, my parts sit here in the architecture:")
    meta("Streamlit Home and Voice pages are the user-facing modules I built.")
    meta("Those pages call FastAPI endpoints that I wired in `main.py`.")
    meta("`config.py` and `.env.example` load Azure endpoints, deployment names, and keys securely.")
    meta("`azure_openai.py` is my service layer for Azure chat and Whisper speech-to-text.")
    meta("`telemetry.py` records request IDs, sources, grounding, and latency for LLMOps.")
    meta("`start.sh` starts API and UI together for local and hosted demos.")
    meta("Azure services I configured and integrated:")
    st.markdown(
        """
- gpt-5-mini for grounded generation
- text-embedding-3-small used by the RAG stack for embeddings
- Whisper for speech-to-text in Voice Assistant (not text-to-speech)
        """
    )
    speak(
        "I kept secrets out of GitHub. Only `.env.example` is committed. Real keys stay in environment variables. For this Capstone, Azure API access and keys were managed by me personally."
    )


def section_3() -> None:
    st.header("SECTION 3 — Homepage live walkthrough, step by step (4:30–10:30)")
    st.markdown('<p class="section-time">4:30–10:30</p>', unsafe_allow_html=True)

    on_screen("Live site Home page. Click slowly through each part as you speak.")
    speak("I will now demonstrate the Homepage feature-by-feature.")
    on_screen("Point to MediGuide title and lead paragraph.")
    speak(
        "When the hosted website opens, Homepage is the first screen — the brand hero with MediGuide and a short lead about clinical knowledge and patient education."
    )
    speak(
        "Behind the scenes at a high level: Streamlit renders markdown and CSS I wrote in Home.py so the first viewport feels like a product entry page."
    )
    on_screen("Click Light and Dark once each, return to the clearer theme.")
    speak("Sidebar Light and Dark theme buttons that change the whole Home look.")
    speak(
        "Behind the scenes: Theme choice is stored in Streamlit session state (`theme_mode`), then I inject either the dark or light CSS block."
    )
    on_screen("Point to Approved docs / Guidelines / Model cards.")
    speak(
        "Live metrics cards — documents indexed, guideline-related counts, and model information from the backend."
    )
    speak(
        "Behind the scenes: Homepage calls the FastAPI `/health` endpoint with httpx. I parse the JSON and display metrics — this proves Azure-backed indexing and backend readiness."
    )
    on_screen("Scroll to ‘Who it helps’.")
    speak("The audience section — clinical staff and patient-service teams.")
    on_screen("Point to the five pipeline steps.")
    speak("A five-step pipeline summary of the whole MediGuide system.")
    meta("The five steps I show:")
    st.markdown(
        """
1. Ask a question
2. Safety guardrails
3. RAG over approved docs
4. Azure OpenAI grounded answer
5. Citations + disclaimer
        """
    )
    on_screen("Hover/point to each tile; click one then come back to Home if needed.")
    speak(
        "Six uplifted navigation tiles — each with icon, title, and short description. If we click any tile, it will navigate to that specific feature."
    )


def section_4() -> None:
    st.header("SECTION 4 — Homepage code on GitHub — Home.py (10:30–14:00)")
    st.markdown('<p class="section-time">10:30–14:00</p>', unsafe_allow_html=True)

    on_screen("Switch to GitHub → open frontend/pages/Home.py")
    speak("Now I will explain the Homepage implementation using code chunks.")
    meta('File: <span class="file-label">frontend/pages/Home.py</span>')
    speak(
        "This is Home.py in the frontend pages folder. It is the first screen users see. It loads the API URL, manages Light/Dark theme in session state, calls /health for live metrics, and renders a FEATURES list as navigation tiles using switch_page. I will walk the high-priority chunks only."
    )

    lines("Lines 1–17")
    speak(
        "At the top I import Streamlit and httpx, put the project root on the path, load environment variables, and set API_URL so every health call hits the correct backend."
    )
    lines("Lines 19–46")
    speak(
        "Here I store theme_mode in session state and render Light and Dark buttons. Choosing one updates state and reruns so the selected CSS theme applies."
    )
    lines("Lines 48–324")
    speak(
        "This large block is styling for readability and brand. I won’t read every CSS rule — the important idea is I maintain separate dark and light style blocks and pick one from session state."
    )
    lines("Lines 326–337")
    speak(
        "After selecting CSS, I inject it and render the MediGuide brand and lead text — that is the first impression from the live demo."
    )
    lines("Lines 340–360")
    speak(
        "This chunk calls /health. If the API is online I show document and model metrics from the JSON. If it is offline I show a friendly message — intentional resilient UI, not a crash."
    )
    lines("Lines 362–403")
    speak(
        "These lines are the copy for Who it helps, How it works, and the tools intro — the same story I walked live. I’ll keep this brief and move to the navigation data."
    )
    lines("Lines 405–455")
    speak(
        "I defined a FEATURES list with path, title, icon, and blurb, then render tiles in columns. Each button calls switch_page — that is how Home opens Voice or other tools."
    )
    lines("Lines 457–480")
    speak(
        "Finally I explain why the six tools belong together and show the educational-use disclaimer — same safety boundary I pointed to on the live site."
    )
    speak("That completes Homepage code. Next I will demonstrate Voice Assistant live.")


def section_5() -> None:
    st.header("SECTION 5 — Voice Assistant live walkthrough (14:00–20:00)")
    st.markdown('<p class="section-time">14:00–20:00</p>', unsafe_allow_html=True)

    on_screen("Open Voice Assistant on live site (Speech to Text page).")
    speak(
        "Voice Assistant is my major feature. See, users speak a healthcare question; Azure Whisper converts speech to text; then the same guardrail and RAG pipeline produces a grounded answer with sources."
    )
    on_screen("Point to theme, audience mode, summarize checkbox, how-it-works expander.")
    speak(
        "In the sidebar I provide theme, audience mode, summary toggle, and guidance tips. Mode and summarize are sent to the backend with the audio request so the answer tone and optional summary match the user’s choice."
    )
    on_screen("Point to Record → Transcribe & Ask → Get Answer steps.")
    speak(
        "I added a step indicator so users understand the workflow before using the microphone — Record, then Transcribe & Ask, then Get Answer."
    )
    on_screen("Show wave animation and microphone input.")
    speak(
        "Step 1 is recording. I implemented an animated wave visualization for presence and clarity, and used Streamlit audio_input for browser microphone capture. IStep 4 — Review and send"
    )
    on_screen(
        'If you can record a short safe question now, do it. Example: “What lifestyle changes help with high blood pressure?” Otherwise explain using a prepared prior result.'
    )
    speak(
        "After recording, Step 2 lets the user review audio, clear and re-record, or press Transcribe & ask. Clearing rotates the audio widget key so the mic remounts cleanly after Streamlit reruns."
    )
    on_screen("While spinner shows, narrate this full path slowly.")
    speak("Here is the full path:")
    st.markdown(
        """
- Speech_to_Text.py takes the pending audio bytes from session state when the user clicks Transcribe & ask.
- The UI builds an httpx multipart POST to `/voice-ask` — audio file plus form fields for mode and summarize.
- FastAPI `/voice-ask` reads the upload, checks size/type, and calls `transcribe_audio` in azure_openai.py (Azure Whisper speech-to-text).
- The transcript is checked by the same safety guardrails as text ask — unsafe or out-of-scope prompts can be blocked with a clear response.
- Approved document chunks are retrieved for the transcribed question.
- `generate_answer` (and optional summarize) runs through Azure OpenAI gpt-5-mini with grounded context.
- The API returns transcript, answer, optional summary, sources, grounding flags, and related metadata; telemetry is logged.
- Streamlit renders transcript, answer, summary, disclaimer, guardrail details, download, and the sources panel.
        """
    )
    on_screen("Show transcript, answer, summary, badges, disclaimer, download.")
    st.markdown(
        """
- What I heard — the Whisper transcript
- Grounded answer text
- Optional quick summary if summarize was enabled
- Safety disclaimer
- Guardrail checks expander
- Download button for documentation during demos
        """
    )
    on_screen("Point to approved sources / expanders; open one source if time.")
    speak(
        "Below the answer I show a Sources panel so Voice stays citation-backed. Each source card typically shows category and relevance, and expanders reveal the approved chunk text that grounded the answer."
    )
    speak(
        "Even though the user spoke, the model still answers from retrieved approved documents — Whisper did not invent clinical facts; it only produced text for the same RAG pipeline."
    )
    st.subheader("Public value of Voice")
    speak(
        "Overall, Voice makes MediGuide accessible in hands-busy clinic or support situations while preserving healthcare safety and grounding through speech-to-text into RAG — not free-form spoken generation."
    )


def section_6() -> None:
    st.header("SECTION 6 — Voice + Azure + API code on GitHub (20:00–23:30)")
    st.markdown('<p class="section-time">20:00–23:30</p>', unsafe_allow_html=True)

    speak(
        "Now I will show the inner workings through selected code chunks across six file groups."
    )

    st.subheader("FILE A — frontend/pages/Speech_to_Text.py")
    on_screen("GitHub → frontend/pages/Speech_to_Text.py")
    speak(
        "This is Speech_to_Text.py in the frontend pages folder — my Voice Assistant page. It captures microphone audio, keeps it in session state across Streamlit reruns, posts multipart data to /voice-ask, then renders transcript, grounded answer, and sources."
    )
    meta("A1 — Imports + API_URL")
    lines("Lines 1–19", "high")
    speak("Top of the Voice page: imports and API_URL so all voice requests hit the correct backend.")
    lines("Lines 21–46", "secondary")
    speak(
        "These constants style the animated wave. I won’t read the CSS — the idea is presence during recording even after Streamlit reruns."
    )
    lines("Lines 57–165", "secondary")
    speak("Secondary styling for dark and light Voice layouts")
    lines("Lines 168–205", "high")
    speak(
        "Sidebar mode and summarize controls are important because they are included in the /voice-ask request with the audio."
    )
    lines("Lines 207–226", "secondary")
    speak("This is the Voice page hero header")
    lines("Lines 228–237", "high")
    speak(
        "I keep an audio_widget_key and a reset_voice helper so clearing a recording remounts the mic cleanly after reruns."
    )
    lines("Lines 240–259", "secondary")
    speak(
        "The step indicator is the same Record, Transcribe & Ask, Get Answer strip from the live walkthrough."
    )
    lines("Lines 262–290", "high")
    speak(
        "Here I use audio_input and save pending_audio in session state so the recording survives reruns until the user reviews and sends."
    )
    lines("Lines 292–331", "high")
    speak(
        "This is the most important UI integration: after review, I POST multipart form data to /voice-ask with the audio, mode, and summarize flag, then read the JSON result."
    )
    lines("Lines 333–412", "high")
    speak(
        "After a successful response I display transcript, grounded answer, optional summary, safety info, and a download button for demos."
    )
    lines("Lines 414–463", "high")
    speak(
        "Finally the sources panel — category, relevance, and chunk expanders — so spoken questions still produce citation-backed answers."
    )

    st.subheader("FILE B — backend/app/services/azure_openai.py")
    on_screen("Open backend/app/services/azure_openai.py")
    speak(
        "Azure OpenAI service layer — dual clients (chat + Whisper), chat helper, grounded generate_answer, helpers for other features, and transcribe_audio."
    )
    lines("Lines 1–39", "high")
    speak(
        "At the top I define mode instructions and a system preamble so every Azure chat call shares the same safety and audience framing."
    )
    lines("Lines 42–68", "high")
    speak(
        "In __init__ I create dual Azure clients because Whisper can live on a different Azure resource than chat. Endpoints and keys come from settings/env."
    )
    lines("Lines 70–110", "high")
    speak(
        "The _chat helper centralizes completion settings. I use high max_completion_tokens and minimal reasoning effort so gpt-5-mini returns visible answers consistently."
    )
    lines("Lines 112–154")
    speak(
        "generate_answer assembles the grounded prompt with retrieved context and calls _chat — Voice uses this after transcription and retrieve."
    )
    lines("Lines 156–166", "secondary")
    speak("summarize is a secondary helper used when the user asks for a quick summary.")
    lines("Lines 168–203", "secondary")
    speak(
        "This appointment-questions helper supports other features through the same Azure service layer — I’ll only mention it briefly."
    )
    lines("Lines 205–239", "secondary")
    speak(
        "Symptom overview is another secondary helper for teammate-facing features using the same client."
    )
    lines("Lines 241–280", "high")
    speak(
        "transcribe_audio is my Whisper speech-to-text method — mime mapping, named buffer, English transcription. This is how voice becomes text before guardrails and RAG."
    )

    st.subheader("FILE C — backend/app/main.py (focus /voice-ask; mention lifespan & /health)")
    on_screen("Open backend/app/main.py — jump to lifespan, /health, then @app.post('/voice-ask')")
    speak(
        "FastAPI app wiring. For my showcase: startup creates Azure-backed services; /health feeds Home metrics; /voice-ask is the Voice pipeline."
    )
    lines("Lines 65–88", "high")
    speak(
        "In lifespan startup I initialize Azure-related services so routes like /voice-ask and /health share ready clients."
    )
    lines("Lines 121–134", "high")
    speak("This /health route is what Homepage calls for live system metrics.")
    lines("Lines 393–400", "secondary")
    speak("ALLOWED_AUDIO_TYPES is a secondary safety check on upload content types.")
    lines("Lines 403–421", "high")
    speak(
        "voice_ask starts by reading the audio, checking size, and calling transcribe_audio on my Azure service."
    )
    lines("Lines 423–456", "high")
    speak(
        "If transcription is unclear, I return a friendly retry response — I do not invent an answer from bad audio."
    )
    lines("Lines 458–494", "high")
    speak(
        "Next I run guardrails on the transcript. If blocked, the route returns a safe response — Voice never skips this layer."
    )
    lines("Lines 496–539", "high")
    speak(
        "On the success path I retrieve approved chunks, generate a grounded answer, optionally summarize, log telemetry, and return transcript, answer, and sources."
    )

    st.subheader("FILE D — backend/app/config.py + .env.example")
    on_screen("Quickly open backend/app/config.py and .env.example (never real .env).")
    speak("Typed settings from environment; example template committed to GitHub without secrets.")
    lines("Lines 1–10 (config.py)", "high")
    speak(
        "config.py starts by resolving ROOT and the .env file path so Settings loads from the right place."
    )
    lines("Lines 13–45 (config.py)", "high")
    speak(
        "The Settings class lists Azure chat, embeddings, Whisper, and path fields. Real values come from environment variables."
    )
    lines("Lines 48–50 (config.py)", "high")
    speak("get_settings caches Settings so FastAPI and services share one configuration object.")
    lines("Lines 1–24 (.env.example — whole file)", "high")
    speak(
        "I commit only .env.example — a template of variable names. Real keys stay in local or hosted environment variables, managed by me for this Capstone."
    )

    st.subheader("FILE E — backend/app/services/telemetry.py")
    on_screen("Open backend/app/services/telemetry.py")
    speak("LLMOps logging — request IDs, query records, feedback, append-only JSONL files.")
    lines("Lines 15–20", "high")
    speak("Telemetry __init__ sets the log file paths used for query and feedback records.")
    lines("Lines 22–23", "high")
    speak(
        "new_request_id creates a unique ID so each Voice or text request can be traced in logs."
    )
    lines("Lines 25–67", "high")
    speak(
        "log_query records request ID, endpoint, truncated question, sources, grounding, risk, latency, prompt version, and model — the LLMOps evidence for Voice and text."
    )
    lines("Lines 69–85", "secondary")
    speak("log_feedback is secondary — it stores user feedback when that UI path is used.")
    lines("Lines 87–89", "secondary")
    speak("_append is a small helper that appends one JSON line to the log file.")

    st.subheader("FILE F — scripts/start.sh + scripts/test_azure.sh")
    on_screen("Open scripts/start.sh briefly, then mention test_azure.sh.")
    speak("Local/hosted boot sequence and Azure smoke tests.")
    lines("Lines 1–36 (start.sh)", "high")
    speak(
        "start.sh begins with environment and proxy/thread setup so Azure HTTP calls behave reliably when we boot."
    )
    lines("Lines 46–70 (start.sh)", "high")
    speak(
        "Next the script validates Azure-related .env configuration so we fail fast before UI startup if something is missing."
    )
    lines("Lines 72–103 (start.sh)", "high")
    speak(
        "I start uvicorn and wait until /health responds — so Streamlit does not open against a dead API."
    )
    lines("Lines 105–113 (start.sh)", "high")
    speak(
        "Finally start.sh launches Streamlit so Home and Voice are available after the API is healthy."
    )
    lines("Lines 1–51 (test_azure.sh)", "high")
    speak(
        "test_azure.sh smoke-tests Azure embeddings and chat so I know the deployments are reachable before a presentation."
    )
    lines("Lines 54–63 (test_azure.sh)", "secondary")
    speak("Optionally it can hit /health and /ask — secondary if the API is already up.")


def section_7() -> None:
    st.header("SECTION 7 — Challenges I faced and how I solved them (23:30–24:30)")
    st.markdown('<p class="section-time">23:30–24:30</p>', unsafe_allow_html=True)

    on_screen("Back to live Home or Voice.")
    speak("Key challenges during my development:")
    st.markdown(
        """
- Chat/embeddings and Whisper were not on one identical setup. I solved this with dual-client configuration in azure_openai.py and clear env vars.
- I debugged completion token behavior and adjusted generation settings so answers were visible and stable.
- Selected Light button became white-on-white. I redesigned selected/unselected contrast in CSS.
- Multipage navigation required careful placement of page configuration in the app entrypoint so pages did not crash.
- Streamlit reruns can reset widgets. I used session state and widget key rotation to preserve a smooth record → review → ask flow.
- I kept real keys out of GitHub and committed only .env.example. For this Capstone, I manage Azure keys personally.
        """
    )


def section_8() -> None:
    st.header("SECTION 8 — Future enhancements + closing (24:30–25:30)")
    st.markdown('<p class="section-time">24:30–25:30</p>', unsafe_allow_html=True)

    meta("Future enhancements I would add next:")
    st.markdown(
        """
- Streaming transcription status and partial transcripts for longer audio
- Stronger indexing progress bar on Homepage during first boot
        """
    )
    st.subheader("Closing")
    speak(
        "To summarize: I, Aparna, owned MediGuide’s first impression and its voice channel, plus the Azure configuration and API wiring that make those features real. I designed Homepage as a trustworthy gateway, and Voice Assistant as speech-to-text multimodal entry into the same grounded Azure RAG pipeline. I implemented and documented these modules in GitHub and solved practical engineering challenges around Azure, Streamlit UX, and safety-conscious product design."
    )
    speak("Thank you sir and everyone.")


def section_qa() -> None:
    st.header("Q&A — 10 likely teacher questions")
    st.caption("Practice answers for viva / follow-up questions after the showcase.")

    qa(
        "Q1. What was your main responsibility in this capstone project?",
        "My main responsibility was the product gateway and the voice path into MediGuide. I built the Home page so users can understand the project and open all six tools, and I built the Voice Assistant page for speech-based questions. On the backend side, I handled Azure OpenAI configuration, the Whisper transcription path, the `/voice-ask` API flow, telemetry logging, and the startup scripts so the demo runs reliably.",
    )
    qa(
        "Q2. Why did you design a separate Home page instead of jumping straight into the assistant?",
        "Because MediGuide has six different tools, and a teacher or first-time user needs orientation before diving into features. Home explains who the product helps, how the pipeline works, and shows live system health. From there, the six tiles act as a gateway into each workspace. So Home is not just a poster — it is the entry point that connects branding, status, and navigation.",
    )
    qa(
        "Q3. How does the Voice Assistant work from click to answer?",
        "The user records a question in `Speech_to_Text.py`, then clicks Transcribe & ask. The frontend sends the audio plus mode and summarize settings to FastAPI `/voice-ask`. The backend uses Azure Whisper to convert speech to text, runs guardrails, retrieves approved documents through RAG, and generates a grounded answer with Azure OpenAI. The JSON response comes back to the UI with the transcript, answer, optional summary, and sources. Voice only changes the input method — after transcription, it follows the same trusted RAG path.",
    )
    qa(
        "Q4. Why did you use Azure Whisper instead of doing everything in the browser?",
        "Browser recording only captures the audio. Accurate healthcare transcription and grounded answering need a controlled backend. Whisper on Azure turns speech into text securely on the server, then the same backend can apply guardrails, RAG, and Azure chat. That keeps API keys off the frontend and keeps voice answers consistent with text-based asking.",
    )
    qa(
        "Q5. You mentioned Azure OpenAI — which services did you configure, and how are secrets handled?",
        "I configured three Azure capabilities: `gpt-5-mini` for grounded generation, `text-embedding-3-small` for embeddings used in retrieval, and Whisper for speech-to-text. Chat and embeddings are on one Azure resource, and Whisper is on a separate resource. Secrets stay in environment variables through `config.py` and `.env` — never in GitHub. I personally manage the Azure API keys for this project.",
    )
    qa(
        "Q6. What is the role of `azure_openai.py` in your work?",
        "`azure_openai.py` is the service layer that talks to Azure. It creates the Azure clients, builds the chat calls, generates grounded answers from retrieved chunks, and handles Whisper transcription. So the UI and routes do not hardcode Azure details — they call this service. That separation makes the Voice and Ask flows cleaner and easier to maintain.",
    )
    qa(
        "Q7. What happens inside the `/voice-ask` endpoint?",
        "`/voice-ask` receives the uploaded audio and form fields for mode and summarize. It checks the knowledge base is ready, reads the audio, and calls Whisper transcription. If transcription fails, it returns a clear retry message. If the transcript passes, it runs guardrails, retrieves relevant chunks, generates a grounded answer, optionally summarizes, logs telemetry, and returns a structured response with sources. That endpoint is the bridge between my Voice UI and Azure plus RAG.",
    )
    qa(
        "Q8. Why do you show sources after a voice answer?",
        "Because MediGuide is meant to be grounded, not a free-form chatbot. The Sources panel shows which approved local documents supported the answer, with relevance and snippets. That improves transparency and trust — the teacher can see the answer is tied to our knowledge base, not random web content. For a healthcare assistant, showing sources is as important as showing the answer itself.",
    )
    qa(
        "Q9. What does telemetry do, and why did you include it?",
        "`telemetry.py` logs each request with a request ID, endpoint, question, mode, sources used, grounding status, risk level, and response time. For Voice, that means we can track whether Whisper and the RAG answer path behaved correctly. It supports LLMOps — not just “it answered,” but “how it answered, from what sources, and how long it took.” That is useful for debugging demos and proving the system is observable.",
    )
    qa(
        "Q10. If the teacher asks what challenge you personally solved, what would you say?",
        "One major challenge was making Voice feel simple while connecting many moving parts — Streamlit audio capture, multipart upload, Whisper transcription, guardrails, RAG, Azure chat, and source display. Another was Azure configuration across two resources without exposing keys. I solved this by keeping secrets in environment config, centralizing Azure calls in `azure_openai.py`, and making `/voice-ask` reuse the same grounded pipeline after transcription so Voice stays safe and consistent with the rest of MediGuide.",
    )


RENDERERS = {
    SECTIONS[0]: None,
    SECTIONS[1]: section_1,
    SECTIONS[2]: section_2,
    SECTIONS[3]: section_3,
    SECTIONS[4]: section_4,
    SECTIONS[5]: section_5,
    SECTIONS[6]: section_6,
    SECTIONS[7]: section_7,
    SECTIONS[8]: section_8,
    SECTIONS[9]: section_qa,
}

if choice == SECTIONS[0]:
    section_1()
    st.divider()
    section_2()
    st.divider()
    section_3()
    st.divider()
    section_4()
    st.divider()
    section_5()
    st.divider()
    section_6()
    st.divider()
    section_7()
    st.divider()
    section_8()
    st.divider()
    section_qa()
else:
    RENDERERS[choice]()
