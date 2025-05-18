from flask import Flask, request, jsonify, render_template, abort, Response
import logging
from logic.SVO import process_svo
from logic.SV import process_sv
from logic.full_sentence import process_full_sentences

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def index() -> str:
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask() -> 'Response':
    data = request.get_json(force=True)  # force=True to ensure JSON parsing
    question = data.get("question", "").strip()
    qtype = data.get("type", "").strip()

    if not question or not qtype:
        abort(400, description="Invalid input: question and type are required.")

    try:
        if qtype == "sv":
            results = process_sv(question)
        elif qtype == "svo":
            results = process_svo(question)
        elif qtype == "full_sentences":
            results = process_full_sentences(question)
        else:
            results = ["Unknown sentence type."]
    except Exception as e:
        app.logger.error(f"Error processing question: {e}", exc_info=True)
        return jsonify({"results": [f"Error processing question: {str(e)}"]})

    return jsonify({"results": results})

if __name__ == "__main__":
    app.run(debug=True)
